#!/usr/bin/env python3
"""
Post-generation hook that runs AFTER all gen-files plugins have completed
This ensures navigation includes all generated content and custom links
"""

import os
import re
import yaml
from pathlib import Path

def on_files(files, config):
    """Hook that runs after gen-files has generated all virtual files."""
    print("🔧 Files hook: Processing navigation after gen-files...")
    
    docs_dir = Path(config['docs_dir'])
    generate_final_navigation(docs_dir, files)
    
    return files

def clean_title(filename):
    """Clean filename for display."""
    name = filename.replace('.md', '').replace('.md.jinja', '')
    name = re.sub(r'^\d+[-_.](?=\w)', '', name)
    return name.replace('_', ' ').replace('-', ' ').title()

def clean_data_summary_title(filename):
    """Clean data summary filename for display - remove repository name and detailed view text."""
    name = filename.replace('.md', '')
    # Remove numeric prefixes
    name = re.sub(r'^\d+[-_.](?=\w)', '', name)
    
    # Remove repository name prefix (e.g., "Variable-Registry_" -> "")
    # Look for pattern: word-word_ or word_ at the beginning
    name = re.sub(r'^[A-Za-z]+-[A-Za-z]+_', '', name)
    name = re.sub(r'^[A-Za-z]+_', '', name)
    
    # If there's still an underscore, use only the part after the first one
    if '_' in name:
        parts = name.split('_', 1)  # Split on first underscore only
        name = parts[1]  # Use everything after first underscore
    
    # Remove "detailed view" or similar suffixes
    name = re.sub(r'[-_]?detailed[-_]?view?$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'[-_]?detailed$', '', name, flags=re.IGNORECASE)
    
    return name.replace('_', ' ').replace('-', ' ').title()

def parse_links_file(docs_dir, links_filename="links.yml"):
    """Parse custom links YAML file."""
    links_path = docs_dir / links_filename
    
    if not links_path.exists():
        print(f"ℹ️  Links file {links_filename} not found, skipping custom links")
        return []
    
    try:
        with open(links_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if not data:
            print(f"ℹ️  Links file {links_filename} is empty")
            return []
            
        links = data.get('links', [])
        
        if not isinstance(links, list):
            print(f"⚠️  Links data should be a list, got {type(links)}")
            return []
            
        print(f"✅ Found {len(links)} custom links in {links_filename}")
        return links
        
    except Exception as e:
        print(f"⚠️  Error parsing {links_filename}: {e}")
        return []

def add_custom_links_to_nav(nav_lines, custom_links, section_title="External Links"):
    """Add custom links to navigation with support for categories."""
    if not custom_links:
        return nav_lines
    
    # Organize links by category
    categories = {}
    root_links = []
    
    for link in custom_links:
        # Skip invalid entries
        if not isinstance(link, dict) or 'title' not in link or 'url' not in link:
            continue
            
        category = link.get('category')
        if category:
            if category not in categories:
                categories[category] = []
            categories[category].append(link)
        else:
            root_links.append(link)
    
    # Add custom links section
    if root_links or categories:
        nav_lines.append(f'- {section_title}:')
        
        # Add root-level links first
        for link in root_links:
            nav_lines.append(f'  - [{link["title"]}]({link["url"]})')
        
        # Add categories as subsections
        for category_name in sorted(categories.keys()):
            nav_lines.append(f'  - {category_name}:')
            for link in categories[category_name]:
                nav_lines.append(f'    - [{link["title"]}]({link["url"]})')
    
    return nav_lines

def get_sort_key(filename):
    """Get sort key for ordering."""
    # Extract base name without extension
    name = filename.replace('.md', '').replace('_detailed', '')
    
    # Look for number at the start of the filename or after common prefixes
    match = re.match(r'^(.+?)[-_]?(\d+)[-_.]', name)
    if match:
        prefix = match.group(1)
        number = int(match.group(2))
        return (number, prefix, filename)
    
    # Fallback to original logic for files without numbers
    match = re.match(r'^(\d+)[-_.]', name)
    if match:
        return (int(match.group(1)), filename)
    
    return (9999, filename)  # Put non-numbered files at the end

def build_directory_tree(docs_path, exclude_dirs=None):
    """Build a nested directory tree structure."""
    if exclude_dirs is None:
        exclude_dirs = {'src-data-docs', 'data-summaries'}
    
    tree = {}
    
    for md_file in docs_path.rglob("*.md*"):  # This will catch both .md and .md.jinja
        if any(part.startswith('.') for part in md_file.parts):
            continue
        if md_file.name == "SUMMARY.md" or md_file.name.startswith("_"):
            continue
        
        rel_path = md_file.relative_to(docs_path)
        parts = list(rel_path.parts)
        
        # Skip excluded directories
        if parts and parts[0] in exclude_dirs:
            continue
        
        # Build tree structure
        current = tree
        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                # This is the file
                if 'files' not in current:
                    current['files'] = []
                current['files'].append({
                    'name': part,
                    'path': rel_path,
                    'sort_key': get_sort_key(part)
                })
            else:
                # This is a directory
                if 'dirs' not in current:
                    current['dirs'] = {}
                if part not in current['dirs']:
                    current['dirs'][part] = {}
                current = current['dirs'][part]
    
    return tree

def add_tree_to_nav(tree, nav_lines, indent="", base_path=""):
    """Recursively add directory tree to navigation lines."""
    # Add files first (sorted)
    if 'files' in tree:
        files = sorted(tree['files'], key=lambda x: x['sort_key'])
        for file_info in files:
            title = clean_title(file_info['name'])
            file_path = str(file_info['path']).replace(os.sep, "/")
            nav_lines.append(f'{indent}- [{title}]({file_path})')
    
    # Add directories (sorted)
    if 'dirs' in tree:
        dirs = sorted(tree['dirs'].items(), key=lambda x: get_sort_key(x[0]))
        for dir_name, dir_tree in dirs:
            dir_title = clean_title(dir_name)
            nav_lines.append(f'{indent}- {dir_title}:')
            
            # Recursively process subdirectories
            add_tree_to_nav(dir_tree, nav_lines, indent + "  ", f"{base_path}/{dir_name}" if base_path else dir_name)

def generate_final_navigation(docs_path, mkdocs_files):
    """Generate SUMMARY.md after ALL content is created."""
    print(f"📂 Scanning for all content...")
    
    # First, detect src-data virtual files from gen-files
    src_data_sections = {}
    has_src_data = False
    data_summaries_files = []
    has_data_summaries = False
    has_stats_page = False
    
    for file_obj in mkdocs_files:
        src_path = str(file_obj.src_path)
        
        # Check for stats/statistics page in both root and auxiliary
        if (src_path == 'stats.md' or src_path == 'statistics.md' or 
            src_path == 'auxiliary/stats.md' or src_path == 'auxiliary/statistics.md' or 
            src_path == 'auxillary/stats.md' or src_path == 'auxillary/statistics.md'):
            has_stats_page = True
            
        if src_path.startswith('src-data-docs/'):
            has_src_data = True
            # Parse the path
            parts = src_path.split('/')
            if len(parts) >= 2:
                filename = parts[1]
                if filename == 'index.md':
                    continue
                elif filename.endswith('_contents.md'):
                    section = filename[:-13]  # Remove _contents.md
                    if section not in src_data_sections:
                        src_data_sections[section] = {'has_contents': True}
                    else:
                        src_data_sections[section]['has_contents'] = True
                elif filename.endswith('.md'):
                    section = filename[:-3]  # Remove .md
                    if section not in src_data_sections:
                        src_data_sections[section] = {'has_main': True}
                    else:
                        src_data_sections[section]['has_main'] = True
        elif src_path.startswith('data-summaries/'):
            has_data_summaries = True
            # Parse the path
            parts = src_path.split('/')
            if len(parts) >= 2:
                filename = parts[1]
                if filename != 'index.md' and filename.endswith('_detailed.md'):
                    # Only add detailed files to main list
                    base_name = filename[:-12]  # Remove _detailed.md
                    data_summaries_files.append(base_name)
    
    if has_src_data:
        print(f"✅ Found src-data virtual files: {len(src_data_sections)} sections")
    if has_data_summaries:
        print(f"✅ Found data summaries virtual files: {len(data_summaries_files)} files")
    if has_stats_page:
        print(f"✅ Found stats page")
    
    # Build directory tree for proper nesting
    tree = build_directory_tree(docs_path)
    
    # Generate navigation
    nav_lines = []
    
    # Always add Home first if index.md exists
    index_path = docs_path / 'index.md'
    index_jinja_path = docs_path / 'index.md.jinja'
    if index_path.exists() or index_jinja_path.exists():
        nav_lines.append('- [Home](index.md)')
    
    # Process root files first (excluding index.md which we already handled)
    if 'files' in tree:
        root_files = [f for f in tree['files'] if f['name'] not in ['index.md', 'index.md.jinja']]
        root_files = sorted(root_files, key=lambda x: x['sort_key'])
        for file_info in root_files:
            title = clean_title(file_info['name'])
            file_path = str(file_info['path']).replace(os.sep, "/")
            nav_lines.append(f'- [{title}]({file_path})')
    
    # Process directories with proper nesting
    if 'dirs' in tree:
        dirs = sorted(tree['dirs'].items(), key=lambda x: get_sort_key(x[0]))
        for dir_name, dir_tree in dirs:
            # Skip auxilary/auxiliary directories - we'll handle them separately
            if dir_name in ['auxilary', 'auxiliary']:
                continue
                
            dir_title = clean_title(dir_name)
            nav_lines.append(f'- {dir_title}:')
            
            # Recursively add nested content
            add_tree_to_nav(dir_tree, nav_lines, "  ")
    
    # Add src-data documentation from virtual files
    if has_src_data and src_data_sections:
        nav_lines.append('- Repository Contents:')
        nav_lines.append('  - [Available Files](src-data-docs/index.md)')
        
        # Add each section in alphabetical order - show all generated files
        for section in sorted(src_data_sections.keys()):
            info = src_data_sections[section]
            section_title = clean_title(section)
            
            # Add main page if it exists
            if info.get('has_main', False):
                nav_lines.append(f'  - [{section_title}](src-data-docs/{section}.md)')
                
                # Add contents as sub-item if it exists
                if info.get('has_contents', False):
                    nav_lines.append(f'    - [Contents](src-data-docs/{section}_contents.md)')
    
    # If no src-data but we have other content files, still create Repository Contents section
    elif 'dirs' in tree and any(dir_name in ['json_data', 'src', 'content', 'repository'] for dir_name in tree['dirs'].keys()):
        nav_lines.append('- Repository Contents:')
        # Add any directories that might contain repository content
        for dir_name in ['json_data', 'src', 'content', 'repository']:
            if dir_name in tree['dirs']:
                dir_title = clean_title(dir_name)
                nav_lines.append(f'  - {dir_title}:')
                add_tree_to_nav(tree['dirs'][dir_name], nav_lines, "    ")
    
    # Add data summaries from virtual files
    if has_data_summaries:
        nav_lines.append('- Summary of Data:')
        nav_lines.append('  - [Overview](data-summaries/index.md)')
        
        # Add each data file directly to detailed page (not nested)
        for data_file in sorted(data_summaries_files):
            title = clean_data_summary_title(data_file)
            nav_lines.append(f'  - [{title}](data-summaries/{data_file}_detailed.md)')
    
    # Always add auxilary/auxiliary section if it exists
    auxilary_dir_tree = tree.get('dirs', {}).get('auxilary')
    auxiliary_dir_tree = tree.get('dirs', {}).get('auxiliary')  # Alternative spelling
    
    if auxilary_dir_tree or auxiliary_dir_tree:
        nav_lines.append('- Additional Resources:')
        
        # Process auxilary directory (primary spelling)
        if auxilary_dir_tree:
            add_tree_to_nav(auxilary_dir_tree, nav_lines, "  ")
        # Process auxiliary directory (alternative spelling)
        elif auxiliary_dir_tree:
            add_tree_to_nav(auxiliary_dir_tree, nav_lines, "  ")
    
    # Add custom links from YAML links file
    
    custom_links = parse_links_file(docs_path, "links.yml")
    nav_lines = add_custom_links_to_nav(nav_lines, custom_links, "External Links")
    
    
    # Write SUMMARY.md
    summary_content = '\n'.join(nav_lines)
    summary_path = docs_path / 'SUMMARY.md'
    
    with open(summary_path, 'w') as f:
        f.write(summary_content)
    
    print(f"✅ Generated {summary_path} with {len(nav_lines)} entries")
    if has_src_data:
        print(f"📋 Included {len(src_data_sections)} src-data sections")
    if has_data_summaries:
        print(f"📋 Included {len(data_summaries_files)} data summary files")
    if has_stats_page:
        print(f"📋 Included repository statistics page")
