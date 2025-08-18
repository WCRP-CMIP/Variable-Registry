#!/usr/bin/env python3
"""
Process JSON files at the same level as docs dir and create pretty table documentation
"""

import os
import sys
import json
import re
import requests
from pathlib import Path
import mkdocs_gen_files
from datetime import datetime

# Flag to prevent multiple runs
_has_run = False
docs_path = mkdocs_gen_files.config.docs_dir

# Cache for prefix mappings
_prefix_mappings = None

def get_prefix_mappings():
    """Fetch and cache prefix mappings from GitHub."""
    global _prefix_mappings
    
    if _prefix_mappings is not None:
        return _prefix_mappings
    
    try:
        url = "https://raw.githubusercontent.com/WCRP-CMIP/CMIPLD/refs/heads/main/cmipld/prefix_mappings.json"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        _prefix_mappings = response.json()
        print(f"✅ Loaded {len(_prefix_mappings)} prefix mappings", file=sys.stderr)
        return _prefix_mappings
    except Exception as e:
        print(f"⚠️  Could not load prefix mappings: {e}", file=sys.stderr)
        _prefix_mappings = {}
        return _prefix_mappings

def convert_prefixed_value(value):
    """Convert prefixed values to GitHub.io links with .json extension.
    
    Examples:
    'vr:area-label/u' -> '<a href="https://wcrp-cmip.github.io/Variable-Registry/area-label/u.json">u</a>'
    'cf:standard_name' -> '<a href="https://wcrp-cmip.github.io/CF/standard_name.json">standard_name</a>'
    """
    if not isinstance(value, str) or ':' not in value:
        return value
    
    # Check if it matches prefix pattern
    match = re.match(r'^([a-zA-Z0-9_-]+):(.+)$', value)
    if not match:
        return value
    
    prefix = match.group(1).lower()
    path = match.group(2)
    
    # Get prefix mappings
    mappings = get_prefix_mappings()
    
    if prefix in mappings:
        mapping = mappings[prefix]
        owner = mapping['owner']
        repo = mapping['repo']
        
        # Extract the display text (part after last slash)
        display_text = path.split('/')[-1] if '/' in path else path
        
        # Create GitHub.io URL with .json extension
        github_io_url = f"https://{owner}.github.io/{repo}/{path}.json"
        
        return f'<a href="{github_io_url}">{display_text}</a>'
    
    return value

def convert_prefixed_list(value):
    """Convert a list of prefixed values to GitHub.io links.
    
    Examples:
    ['vr:area-label/longitude', 'vr:area-label/latitude'] -> 
    '<a href="...">longitude</a>, <a href="...">latitude</a>'
    """
    if not isinstance(value, list):
        return value
    
    converted_items = []
    for item in value:
        converted_item = convert_prefixed_value(item)
        converted_items.append(converted_item)
    
    # Join with commas and spaces
    return ', '.join(converted_items)

def process_value_for_prefixes(value):
    """Process a value that could be a string, list, or other type for prefix conversion."""
    if isinstance(value, list):
        return convert_prefixed_list(value)
    elif isinstance(value, str):
        return convert_prefixed_value(value)
    else:
        return value

def process_json_files():
    """Process JSON files and generate documentation with tables."""
    global _has_run
    
    if _has_run:
        return
    _has_run = True
    
    # Find JSON files at the project root
    json_dir = Path(docs_path).parent
    json_files = list(json_dir.glob("*.json"))
    if json_files:
        print(f"      Found {len(json_files)} JSON files", file=sys.stderr)
    else:
        print("ℹ️  No JSON files found at the same level as docs directory", file=sys.stderr)
        return
    
    print(f"📁 Found {len(json_files)} JSON files at: {json_dir.absolute()}", file=sys.stderr)
    
    output_base = "data-summaries"
    
    # Create index page
    index_content = """# Data Summaries

This section contains formatted views of JSON data files.

## Available Data Files

| File | Description | View | Raw File |
|------|-------------|------|----------|
"""
    
    # Process each JSON file
    for json_file in sorted(json_files):
        try:
            print(f"  📄 Processing: {json_file.name}", file=sys.stderr)
            
            # Read JSON content
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Generate only detailed page (summary page not needed)
            page_name = json_file.stem  # filename without extension
            
            # Generate detailed version
            detailed_content = generate_detailed_json_page(json_file, data)
            with mkdocs_gen_files.open(f"{output_base}/{page_name}_detailed.md", "w") as f:
                f.write(detailed_content)
            
            # Get description from Header if available
            description = "JSON data file"
            if isinstance(data, dict) and 'Header' in data:
                header = data['Header']
                if isinstance(header, dict):
                    # Try to find a description-like field
                    for key in ['description', 'Description', 'title', 'Title', 'name', 'Name']:
                        if key in header:
                            description = str(header[key])[:60]
                            if len(str(header[key])) > 60:
                                description += "..."
                            break
            
            # Add to index
            github_url = f"https://raw.githubusercontent.com/WCRP-CMIP/Variable-Registry/main/{json_file.name}"
            index_content += f"| {json_file.name} | {description} | [View]({page_name}_detailed.md) | [Raw File]({github_url}) |\n"
            
        except Exception as e:
            print(f"  ⚠️  Error processing {json_file.name}: {e}", file=sys.stderr)
            # Still add to index but mark as error
            github_url = f"https://raw.githubusercontent.com/WCRP-CMIP/Variable-Registry/main/{json_file.name}"
            index_content += f"| {json_file.name} | *Error processing file* | [View]({page_name}_detailed.md) | [Raw File]({github_url}) |\n"
    
    # Complete index page
    index_content += f"""

## About

These pages are automatically generated from JSON files located two directories up from the mkdocs.yml file (../../). Each page displays the data in a formatted table view.

### Features

- **Header Information**: Displayed as a formatted table at the top of each page
- **Data Tables**: Main data content displayed in organized tables
- **Prefix Links**: Prefixed values (e.g., 'vr:area-label/u') are converted to GitHub.io links with .json extension
- **List Processing**: Lists of prefixed values are converted to comma-separated links
- **Git Integration**: Direct links to view the source files

---

*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    # Write index page
    with mkdocs_gen_files.open(f"{output_base}/index.md", "w") as f:
        f.write(index_content)
    
    print(f"✅ Processed {len(json_files)} JSON files", file=sys.stderr)

def generate_detailed_json_page(json_file, data):
    """Generate a detailed page with main data as table and header at bottom."""
    github_url = f"https://raw.githubusercontent.com/WCRP-CMIP/Variable-Registry/main/{json_file.name}"
    page_content = f"""# {json_file.stem} - Detailed View

<div class="file-info" style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
    <strong>File Path:</strong> <code>{json_file.name}</code><br>
    <strong>File Size:</strong> {json_file.stat().st_size:,} bytes<br>
    <a href="{github_url}" class="md-button md-button--primary" style="margin-top: 10px;">View Raw File</a>
</div>

"""
    
    # Process main data first (non-Header keys)
    if isinstance(data, dict):
        data_keys = [k for k in data.keys() if k != 'Header']
        
        for data_key in data_keys:
            main_data = data[data_key]
            page_content += f"## {format_key_name(data_key)}\n\n"
            
            # Handle different data structures
            if isinstance(main_data, dict) and all(isinstance(v, dict) for v in main_data.values()):
                # Case 1: Dictionary of objects - use specialized formatting
                page_content += format_dict_of_objects_as_table(main_data)
            elif isinstance(main_data, list):
                # Case 2: List of objects
                page_content += format_list_as_table(main_data, flatten_nested=True)
            elif isinstance(main_data, dict):
                # Case 3: Regular dictionary
                page_content += format_dict_as_table(main_data, flatten_nested=True)
            else:
                page_content += f"```\n{json.dumps(main_data, indent=2)}\n```\n\n"
    
    elif isinstance(data, list):
        # The entire file is a list
        page_content += "## Data\n\n"
        page_content += format_list_as_table(data, flatten_nested=True)
    
    # Add Header information at the bottom
    if isinstance(data, dict) and 'Header' in data:
        header = data['Header']
        page_content += "\n---\n\n## Version Information\n\n"
        
        if isinstance(header, dict):
            page_content += '<details markdown="1">\n'
            page_content += '<summary><strong>Click to expand version details</strong></summary>\n\n'
            page_content += format_dict_as_table(header, flatten_nested=True)
            page_content += '\n</details>\n\n'
        else:
            page_content += f"```\n{header}\n```\n\n"
    
    # Add footer
    page_content += f"""\n---\n
<div style="text-align: center; margin-top: 40px;">
    <a href="index.md" class="md-button">← Back to Data Summaries</a>
</div>
"""
    
    return page_content

def format_dict_of_objects_as_table(data):
    """Format a dictionary of objects as a table with names as first column."""
    if not data:
        return "*No data*\n\n"
    
    # Check if all values are dictionaries
    if not all(isinstance(v, dict) for v in data.values()):
        # Fall back to regular dict formatting if not all values are dicts
        return format_dict_as_table(data, flatten_nested=True)
    
    # Collect all possible keys from all objects
    all_keys = set()
    flattened_objects = {}
    
    for name, obj in data.items():
        if isinstance(obj, dict):
            flattened = flatten_dict(obj)
            flattened_objects[name] = flattened
            all_keys.update(flattened.keys())
    
    # Sort keys for consistent ordering
    keys = sorted(list(all_keys))
    
    # If too many columns, limit to most common ones
    if len(keys) > 15:
        # Count frequency of keys
        key_counts = {}
        for key in keys:
            key_counts[key] = sum(1 for obj in flattened_objects.values() 
                                 if key in obj and obj[key] is not None and str(obj[key]).strip())
        # Sort by frequency and take top 15
        keys = sorted(keys, key=lambda k: key_counts[k], reverse=True)[:15]
    
    # Create table header
    table = "| Name | " + " | ".join(format_key_name(k) for k in keys) + " |\n"
    table += "|---|" + "|".join("---" for _ in keys) + "|\n"
    
    # Add rows
    for name in sorted(data.keys()):
        obj = flattened_objects.get(name, {})
        row = f"| **{name}** |"
        
        for key in keys:
            value = obj.get(key, "")
            formatted_value = format_cell_value(value)
            row += f" {formatted_value} |"
        
        table += row + "\n"
    
    # Add summary info
    table += f"\n*{len(data)} entries with {len(keys)} columns*\n"
    
    return table + "\n"

def format_dict_as_table(data, flatten_nested=True):
    """Format a dictionary as a markdown table."""
    if not data:
        return "*No data*\n\n"
    
    if flatten_nested:
        # Flatten nested objects into columns
        flattened = flatten_dict(data)
        return format_flattened_dict_table(flattened)
    else:
        # Original behavior
        return format_dict_as_table_original(data)

def flatten_dict(data, parent_key='', sep='.'):
    """Flatten a nested dictionary into a single level."""
    items = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        elif isinstance(value, list):
            # Handle lists - keep them as lists for prefix processing
            items.append((new_key, value))
        else:
            items.append((new_key, value))
    
    return dict(items)

def format_flattened_dict_table(flattened_data):
    """Format flattened dictionary data as a table."""
    table = "| Property | Value |\n"
    table += "|----------|-------|\n"
    
    for key, value in sorted(flattened_data.items()):
        # Format the key
        formatted_key = format_key_name(key)
        
        # Format the value using prefix processing
        if value is None:
            formatted_value = "*None*"
        elif isinstance(value, bool):
            formatted_value = "✓" if value else "✗"
        elif isinstance(value, list):
            # Process lists for prefixed values
            converted_value = convert_prefixed_list(value)
            if converted_value != value:
                formatted_value = converted_value
            else:
                # Not prefixed, format as regular list
                if len(value) > 5:
                    formatted_value = f"{', '.join(str(v) for v in value[:5])}, ... ({len(value)} total)"
                else:
                    formatted_value = ', '.join(str(v) for v in value)
        else:
            str_value = str(value)
            
            # Handle URLs specially
            if str_value.startswith(('http://', 'https://')):
                if len(str_value) > 100:
                    display_url = str_value[:97] + "..."
                    formatted_value = f"[{display_url}]({str_value})"
                else:
                    formatted_value = f"[{str_value}]({str_value})"
            else:
                # Check for prefix patterns and convert to links
                converted_value = convert_prefixed_value(str_value)
                if converted_value != str_value:
                    # It was converted to a link, use it as-is
                    formatted_value = converted_value
                else:
                    # Escape and clean the content
                    formatted_value = escape_markdown_content(str_value)
                    
                    # Truncate long values
                    if len(formatted_value) > 200:
                        formatted_value = formatted_value[:200] + "..."
        
        table += f"| {formatted_key} | {formatted_value} |\n"
    
    return table + "\n"

def format_dict_as_table_original(data):
    """Original format_dict_as_table function with prefix processing."""
    # Check if all values are simple types
    all_simple = all(isinstance(v, (str, int, float, bool, list, type(None))) for v in data.values())
    
    if all_simple:
        # Simple key-value table
        table = "| Property | Value |\n"
        table += "|----------|-------|\n"
        
        for key, value in data.items():
            # Format the key
            formatted_key = format_key_name(key)
            
            # Format the value with prefix processing
            if value is None:
                formatted_value = "*None*"
            elif isinstance(value, bool):
                formatted_value = "✓" if value else "✗"
            elif isinstance(value, list):
                # Process lists for prefixed values
                converted_value = convert_prefixed_list(value)
                if converted_value != value:
                    formatted_value = converted_value
                else:
                    # Not prefixed, format as regular list
                    if len(value) > 5:
                        formatted_value = f"{', '.join(str(v) for v in value[:5])}, ... ({len(value)} total)"
                    else:
                        formatted_value = ', '.join(str(v) for v in value)
            else:
                str_value = str(value)
                
                # Handle URLs specially
                if str_value.startswith(('http://', 'https://')):
                    if len(str_value) > 100:
                        display_url = str_value[:97] + "..."
                        formatted_value = f"[{display_url}]({str_value})"
                    else:
                        formatted_value = f"[{str_value}]({str_value})"
                else:
                    # Check for prefix patterns and convert to links
                    converted_value = convert_prefixed_value(str_value)
                    if converted_value != str_value:
                        # It was converted to a link, use it as-is
                        formatted_value = converted_value
                    else:
                        # Escape and clean the content
                        formatted_value = escape_markdown_content(str_value)
                        
                        # Truncate long values
                        if len(formatted_value) > 100:
                            formatted_value = formatted_value[:100] + "..."
            
            table += f"| {formatted_key} | {formatted_value} |\n"
    else:
        # Complex nested data - show type and summary
        table = "| Property | Type | Summary |\n"
        table += "|----------|------|----------|\n"
        
        for key, value in data.items():
            formatted_key = format_key_name(key)
            
            if isinstance(value, dict):
                summary = f"{len(value)} properties"
            elif isinstance(value, list):
                # Process lists for prefixed values in summary
                converted_value = convert_prefixed_list(value)
                if converted_value != value:
                    summary = converted_value
                else:
                    summary = f"{len(value)} items"
            elif isinstance(value, (str, int, float)):
                str_value = str(value)
                # Check for prefix patterns and convert to links
                converted_value = convert_prefixed_value(str_value)
                if converted_value != str_value:
                    summary = converted_value
                else:
                    # Escape the summary content
                    summary = escape_markdown_content(str_value)
                    if len(summary) > 50:
                        summary = summary[:50] + "..."
            else:
                summary = str(type(value).__name__)
            
            table += f"| {formatted_key} | {type(value).__name__} | {summary} |\n"
    
    return table + "\n"

def format_list_as_table(data, flatten_nested=True):
    """Format a list as a markdown table."""
    if not data:
        return "*Empty list*\n\n"
    
    # Check if all items are dictionaries
    if all(isinstance(item, dict) for item in data):
        if flatten_nested:
            return format_list_of_dicts_flattened(data)
        else:
            return format_list_of_dicts_original(data)
    else:
        # List of non-dictionary items
        return format_simple_list_table(data)

def format_list_of_dicts_flattened(data):
    """Format list of dictionaries with flattened nested objects."""
    # First, flatten all dictionaries and collect all possible keys
    flattened_items = []
    all_keys = set()
    
    for item in data:
        flattened = flatten_dict(item)
        flattened_items.append(flattened)
        all_keys.update(flattened.keys())
    
    # Sort keys for consistent ordering
    keys = sorted(list(all_keys))
    
    # If too many columns, limit to most common ones
    if len(keys) > 12:
        # Count frequency of keys
        key_counts = {}
        for key in keys:
            key_counts[key] = sum(1 for item in flattened_items if key in item and item[key] is not None and str(item[key]).strip())
        # Sort by frequency and take top 12
        keys = sorted(keys, key=lambda k: key_counts[k], reverse=True)[:12]
    
    # Create table header
    table = "| # | " + " | ".join(format_key_name(k) for k in keys) + " |\n"
    table += "|---|" + "|".join("---" for _ in keys) + "|\n"
    
    # Add rows (limit to first 100 for very large lists)
    for i, item in enumerate(flattened_items[:100]):
        row = f"| {i+1} |"
        for key in keys:
            value = item.get(key, "")
            formatted_value = format_cell_value(value)
            row += f" {formatted_value} |"
        
        table += row + "\n"
    
    if len(data) > 100:
        table += f"\n*Showing first 100 of {len(data)} items*\n"
    
    return table + "\n"

def format_list_of_dicts_original(data):
    """Original format for list of dictionaries."""
    # Get all unique keys from all dictionaries
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())
    
    # Sort keys for consistent ordering
    keys = sorted(list(all_keys))
    
    # If too many columns, limit to most common ones
    if len(keys) > 8:
        # Count frequency of keys
        key_counts = {}
        for key in keys:
            key_counts[key] = sum(1 for item in data if key in item)
        # Sort by frequency and take top 8
        keys = sorted(keys, key=lambda k: key_counts[k], reverse=True)[:8]
    
    # Create table header
    table = "| # | " + " | ".join(format_key_name(k) for k in keys) + " |\n"
    table += "|---|" + "|".join("---" for _ in keys) + "|\n"
    
    # Add rows (limit to first 100 for very large lists)
    for i, item in enumerate(data[:100]):
        row = f"| {i+1} |"
        for key in keys:
            value = item.get(key, "")
            formatted_value = format_cell_value(value)
            row += f" {formatted_value} |"
        
        table += row + "\n"
    
    if len(data) > 100:
        table += f"\n*Showing first 100 of {len(data)} items*\n"
    
    return table + "\n"

def format_simple_list_table(data):
    """Format a simple list (non-dictionary items) as a table."""
    table = "| # | Value | Type |\n"
    table += "|---|-------|------|\n"
    
    for i, item in enumerate(data[:100]):
        if isinstance(item, (str, int, float, bool)):
            str_value = str(item)
            
            # Handle URLs specially
            if str_value.startswith(('http://', 'https://')):
                if len(str_value) > 100:
                    display_url = str_value[:97] + "..."
                    value_str = f"[{display_url}]({str_value})"
                else:
                    value_str = f"[{str_value}]({str_value})"
            else:
                # Check for prefix patterns and convert to links
                converted_value = convert_prefixed_value(str_value)
                if converted_value != str_value:
                    value_str = converted_value
                else:
                    # Escape and clean the content
                    value_str = escape_markdown_content(str_value)
                    if len(value_str) > 100:
                        value_str = value_str[:100] + "..."
        elif isinstance(item, list):
            # Handle lists in simple list table
            converted_value = convert_prefixed_list(item)
            if converted_value != item:
                value_str = converted_value
            else:
                value_str = f"List of {len(item)} items"
        else:
            value_str = f"*{type(item).__name__} object*"
        
        table += f"| {i+1} | {value_str} | {type(item).__name__} |\n"
    
    if len(data) > 100:
        table += f"\n*Showing first 100 of {len(data)} items*\n"
    
    return table + "\n"

def format_cell_value(value):
    """Format a single cell value for display in a table."""
    if value is None or value == "":
        return "*None*"
    elif isinstance(value, bool):
        return "✓" if value else "✗"
    elif isinstance(value, list):
        # Handle lists with prefix processing
        converted_value = convert_prefixed_list(value)
        if converted_value != value:
            return converted_value
        else:
            # Not prefixed, format as regular list
            if len(value) > 3:
                display_items = [escape_markdown_content(str(v)) for v in value[:3]]
                return f"{', '.join(display_items)}, ... ({len(value)} total)"
            else:
                display_items = [escape_markdown_content(str(v)) for v in value]
                return ', '.join(display_items)
    elif isinstance(value, dict):
        return f"*{type(value).__name__}*"
    else:
        str_value = str(value)
        
        # Handle URLs specially - create clickable links
        if str_value.startswith(('http://', 'https://')):
            # Truncate very long URLs for display
            if len(str_value) > 50:
                display_url = str_value[:47] + "..."
                return f"[{display_url}]({str_value})"
            else:
                return f"[{str_value}]({str_value})"
        
        # Check for prefix patterns and convert to GitHub.io links
        converted_value = convert_prefixed_value(str_value)
        if converted_value != str_value:
            # It was converted to a link, return as-is (already HTML)
            return converted_value
        
        # Escape and clean the content for markdown table display
        formatted_value = escape_markdown_content(str_value)
        
        # Truncate long values
        if len(formatted_value) > 50:
            formatted_value = formatted_value[:50] + "..."
        
        return formatted_value

def escape_markdown_content(text):
    """Escape content for safe display in markdown tables."""
    if not text:
        return text
    
    # Convert to string if not already
    content = str(text)
    
    # Replace newlines with spaces to prevent table breaking
    content = content.replace('\n', ' ').replace('\r', ' ')
    
    # Replace multiple spaces with single space
    content = re.sub(r'\s+', ' ', content)
    
    # Escape HTML tags by converting < and > to HTML entities
    content = content.replace('<', '&lt;').replace('>', '&gt;')
    
    # Escape markdown special characters that could break tables
    content = content.replace('|', '\\|')  # Pipe characters break table formatting
    content = content.replace('`', '\\`')  # Backticks can start code blocks
    content = content.replace('*', '\\*')  # Asterisks can start bold/italic
    content = content.replace('_', '\\_')  # Underscores can start italic
    content = content.replace('[', '\\[')  # Square brackets can start links
    content = content.replace(']', '\\]')  # Square brackets can end links
    content = content.replace('(', '\\(')  # Parentheses can be part of links
    content = content.replace(')', '\\)')  # Parentheses can be part of links
    content = content.replace('#', '\\#')  # Hash can start headers
    content = content.replace('&', '&amp;')  # Ampersands should be escaped
    
    # Handle quotes that might interfere with markdown
    content = content.replace('"', '&quot;')
    content = content.replace("'", '&#39;')
    
    # Remove any remaining control characters
    content = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', content)
    
    # Strip leading/trailing whitespace
    content = content.strip()
    
    return content

def format_key_name(key):
    """Format a key name for display."""
    # Handle dot notation from flattened keys
    if '.' in key:
        # Split by dots and format each part
        parts = key.split('.')
        formatted_parts = []
        for part in parts:
            # Handle array indices like [0], [1]
            if part.startswith('[') and part.endswith(']'):
                formatted_parts.append(part)
            else:
                formatted_parts.append(format_single_key_name(part))
        return ' → '.join(formatted_parts)
    else:
        return format_single_key_name(key)

def format_single_key_name(key):
    """Format a single key name (no dots)."""
    # Convert snake_case or camelCase to Title Case
    # Handle snake_case
    if '_' in key:
        return ' '.join(word.capitalize() for word in key.split('_'))
    # Handle camelCase
    elif key[0].islower() and any(c.isupper() for c in key):
        # Insert spaces before capital letters
        result = key[0].upper()
        for c in key[1:]:
            if c.isupper():
                result += ' ' + c
            else:
                result += c
        return result
    else:
        return key.capitalize()

# Also call when imported by mkdocs-gen-files
process_json_files()
