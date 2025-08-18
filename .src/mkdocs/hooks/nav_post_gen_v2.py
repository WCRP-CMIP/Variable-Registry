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
    
    # Collect all files and directories from docs directory
    all_items = []
    
    for md_file in docs_path.rglob("*.md*"):  # This will catch both .md and .md.jinja
        if any(part.startswith('.') for part in md_file.parts):
            continue
        if md_file.name == "SUMMARY.md" or md_file.name.startswith("_"):
            continue
        
        rel_path = md_file.relative_to(docs_path)
        parts = list(rel_path.parts)
        
        # Skip src-data-docs and data-summaries (handled separately)
        if parts and parts[0] in ['src-data-docs', 'data-summaries']:
            continue
            
        if len(parts) == 1:
            # Root level file
            all_items.append({
                'type': 'file',
                'name': md_file.name,
                'path': md_file,
                'sort_key': get_sort_key(md_file.name)
            })
        else:
            # File in subdirectory - add directory info
            dir_name = parts[0]
            all_items.append({
                'type': 'directory',
                'name': dir_name,
                'sort_key': get_sort_key(dir_name)
            })
    
    # Get unique directories for later processing
    directories = {}
    for md_file in docs_path.rglob("*.md*"):  # This will catch both .md and .md.jinja
        if any(part.startswith('.') for part in md_file.parts):
            continue
        if md_file.name == "SUMMARY.md" or md_file.name.startswith("_"):
            continue
        
        rel_path = md_file.relative_to(docs_path)
        parts = list(rel_path.parts)
        
        # Skip src-data-docs and data-summaries (handled separately)
        if parts and parts[0] in ['src-data-docs', 'data-summaries']:
            continue
            
        if len(parts) > 1:
            dir_name = parts[0]
            if dir_name not in directories:
                directories[dir_name] = []
            directories[dir_name].append(md_file)
    
    # Generate navigation with mixed ordering
    nav_lines = []
    processed_dirs = set()
    
    # Get all unique items (files and directories) and sort them together
    unique_items = []
    
    # Add root files
    root_files = [item for item in all_items if item['type'] == 'file']
    for item in root_files:
        unique_items.append(item)
    
    # Add directories
    for dir_name in directories.keys():
        unique_items.append({
            'type': 'directory',
            'name': dir_name,
            'sort_key': get_sort_key(dir_name)
        })
    
    # Always add Home first if index.md exists
    index_file_exists = any(item['type'] == 'file' and item['path'].name == 'index.md' for item in unique_items)
    if index_file_exists:
        nav_lines.append('- [Home](index.md)')
    
    # Remove duplicates and sort all items together
    seen = set()
    unique_sorted_items = []
    for item in sorted(unique_items, key=lambda x: x['sort_key']):
        key = (item['type'], item['name'])
        if key not in seen:
            seen.add(key)
            unique_sorted_items.append(item)
    
    # Generate navigation in sorted order, but ensure Home comes first
    for item in unique_sorted_items:
        if item['type'] == 'file':
            # Handle root files - skip index.md here, we'll add it first
            file_path = item['path']
            if file_path.name == 'index.md':
                continue  # Skip here, will be added first
            else:
                title = clean_title(file_path.name)
                nav_lines.append(f'- [{title}]({file_path.name})')
        
        elif item['type'] == 'directory':
            # Handle directories
            dir_name = item['name']
            if dir_name not in processed_dirs:
                processed_dirs.add(dir_name)
                
                dir_title = clean_title(dir_name)
                nav_lines.append(f'- {dir_title}:')
                
                # Add files in this directory
                if dir_name in directories:
                    dir_files = sorted(directories[dir_name], key=lambda f: get_sort_key(f.name))
                    for f in dir_files:
                        rel_path = f.relative_to(docs_path)
                        title = clean_title(f.name)
                        nav_lines.append(f'  - [{title}]({str(rel_path).replace(os.sep, "/")})')
                

    
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
    elif any(item['type'] == 'directory' and item['name'] in ['json_data', 'src', 'content', 'repository'] for item in unique_sorted_items):
        nav_lines.append('- Repository Contents:')
        # Add any directories that might contain repository content
        for item in unique_sorted_items:
            if item['type'] == 'directory' and item['name'] in ['json_data', 'src', 'content', 'repository']:
                dir_name = item['name']
                if dir_name in directories:
                    dir_title = clean_title(dir_name)
                    nav_lines.append(f'  - {dir_title}:')
                    dir_files = sorted(directories[dir_name], key=lambda f: get_sort_key(f.name))
                    for f in dir_files:
                        rel_path = f.relative_to(docs_path)
                        title = clean_title(f.name)
                        nav_lines.append(f'    - [{title}]({str(rel_path).replace(os.sep, "/")})')
    
    # Add data summaries from virtual files
    if has_data_summaries:
        nav_lines.append('- Summary of Data:')
        nav_lines.append('  - [Overview](data-summaries/index.md)')
        
        # Add each data file directly to detailed page (not nested)
        for data_file in sorted(data_summaries_files):
            title = clean_data_summary_title(data_file)
            nav_lines.append(f'  - [{title}](data-summaries/{data_file}_detailed.md)')
    
    # Always add auxilary/auxiliary section if it exists and wasn't already processed
    auxilary_dir = docs_path / 'auxilary'
    auxiliary_dir = docs_path / 'auxiliary'  # Alternative spelling
    
    # Check if auxilary directory wasn't already processed in main loop
    auxilary_already_processed = 'auxilary' in processed_dirs or 'auxiliary' in processed_dirs
    
    if not auxilary_already_processed:
        auxilary_exists = auxilary_dir.exists() and (any(auxilary_dir.glob('*.md')) or any(auxilary_dir.glob('*.md.jinja')))
        auxiliary_exists = auxiliary_dir.exists() and (any(auxiliary_dir.glob('*.md')) or any(auxiliary_dir.glob('*.md.jinja')))
        
        if auxilary_exists or auxiliary_exists:
            nav_lines.append('- Additional Resources:')
            
            # Process auxilary directory (primary spelling)
            if auxilary_exists:
                auxilary_files = list(auxilary_dir.glob('*.md')) + list(auxilary_dir.glob('*.md.jinja'))
                for md_file in sorted(auxilary_files, key=lambda f: get_sort_key(f.name)):
                    if md_file.name.startswith('_'):
                        continue
                    rel_path = md_file.relative_to(docs_path)
                    title = clean_title(md_file.name)
                    nav_lines.append(f'  - [{title}]({str(rel_path).replace(os.sep, "/")})')
            
            # Process auxiliary directory (alternative spelling)
            elif auxiliary_exists:
                auxiliary_files = list(auxiliary_dir.glob('*.md')) + list(auxiliary_dir.glob('*.md.jinja'))
                for md_file in sorted(auxiliary_files, key=lambda f: get_sort_key(f.name)):
                    if md_file.name.startswith('_'):
                        continue
                    rel_path = md_file.relative_to(docs_path)
                    title = clean_title(md_file.name)
                    nav_lines.append(f'  - [{title}]({str(rel_path).replace(os.sep, "/")})')
    
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
