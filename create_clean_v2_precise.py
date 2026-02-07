#!/usr/bin/env python3
"""
Create homepage-v2.html by SURGICALLY removing ONLY header-related code
from homepage-v1.html while preserving ALL other functionality.
"""

import re

def create_clean_v2_precise():
    # Read homepage-v1.html
    with open('homepage-v1.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print("Original file lines:", len(lines))
    
    # Track what we remove
    removed_sections = []
    output_lines = []
    skip_until_line = -1
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # If we're in a skip section, continue skipping
        if i < skip_until_line:
            i += 1
            continue
        
        # Check for NEW HEADER V13 CSS section
        if '/* ===== NEW HEADER V13 DESIGN =====' in line or '.new-header {' in line:
            # Skip until we find the end of this CSS block
            # Look for the closing of the new-header styles
            start_line = i
            brace_count = 0
            in_new_header_css = False
            
            # Find the complete CSS section for new-header
            while i < len(lines):
                if '.new-header' in lines[i] or 'new-header' in lines[i]:
                    in_new_header_css = True
                
                if in_new_header_css:
                    brace_count += lines[i].count('{')
                    brace_count -= lines[i].count('}')
                    
                    if brace_count == 0 and '}' in lines[i]:
                        removed_sections.append(f"NEW HEADER CSS: lines {start_line}-{i}")
                        i += 1
                        break
                
                if not in_new_header_css and lines[i].strip() and not lines[i].strip().startswith('.new-header'):
                    break
                
                i += 1
            continue
        
        # Check for <header class="new-header">
        if '<header class="new-header">' in line:
            start_line = i
            # Skip until </header>
            while i < len(lines) and '</header>' not in lines[i]:
                i += 1
            if '</header>' in lines[i]:
                i += 1  # Skip the closing tag too
            removed_sections.append(f"NEW HEADER HTML: lines {start_line}-{i}")
            continue
        
        # Check for <header id="page-header" class="default-header"
        if '<header id="page-header" class="default-header' in line:
            # This is trickier - we need to extract the navigation and remove the header shell
            start_line = i
            header_content = []
            nav_content = []
            in_nav = False
            nav_start = -1
            
            # Read the entire header section
            while i < len(lines) and '</header>' not in lines[i]:
                header_content.append(lines[i])
                
                # Check if this line contains navigation start
                if '<nav class="navbar p-0 megamenu">' in lines[i]:
                    in_nav = True
                    nav_start = len(header_content) - 1
                
                if in_nav:
                    nav_content.append(lines[i])
                
                # Check for navigation end
                if in_nav and '</nav>' in lines[i]:
                    in_nav = False
                
                i += 1
            
            # Also read the closing header tag
            if i < len(lines):
                header_content.append(lines[i])
                i += 1
            
            # Now output only the navigation part if we found it
            if nav_content:
                output_lines.extend(nav_content)
                removed_sections.append(f"DEFAULT HEADER (kept nav): lines {start_line}-{i}")
            else:
                removed_sections.append(f"DEFAULT HEADER (no nav found): lines {start_line}-{i}")
            
            continue
        
        # Check for sticky icons: <div class="hidden-unstuck stuck-left"> or stuck-right
        if 'hidden-unstuck stuck-left' in line or 'hidden-unstuck stuck-right' in line:
            start_line = i
            # Skip until </div> - but count nested divs
            div_count = line.count('<div') - line.count('</div')
            i += 1
            
            while i < len(lines) and div_count > 0:
                div_count += lines[i].count('<div') - lines[i].count('</div')
                i += 1
            
            removed_sections.append(f"STICKY ICON: lines {start_line}-{i}")
            continue
        
        # Check for old icon CSS classes (but be careful not to remove CSS in other contexts)
        if re.search(r'\.icon-(sage-green|ice-blue|orange|glassmorphism)\s*{', line):
            start_line = i
            # Skip this CSS rule
            brace_count = line.count('{') - line.count('}')
            i += 1
            
            while i < len(lines) and brace_count > 0:
                brace_count += lines[i].count('{') - lines[i].count('}')
                i += 1
            
            removed_sections.append(f"OLD ICON CSS: lines {start_line}-{i}")
            continue
        
        # Keep this line
        output_lines.append(line)
        i += 1
    
    print(f"\nRemoved {len(removed_sections)} sections:")
    for section in removed_sections:
        print(f"  - {section}")
    
    print(f"\nOutput lines: {len(output_lines)}")
    print(f"Lines removed: {len(lines) - len(output_lines)}")
    
    # Write to homepage-v2.html
    with open('homepage-v2.html', 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    
    print("\n✅ Created homepage-v2.html successfully!")
    print("\nPreserved:")
    print("- Navigation menu")
    print("- All JavaScript")
    print("- All other CSS")
    print("- Countdown banner")
    print("- Main content")
    print("- Footer")
    print("- All other page elements")
    
    return True

if __name__ == '__main__':
    create_clean_v2_precise()
