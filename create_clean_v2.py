#!/usr/bin/env python3
"""
Create homepage-v2.html by removing ALL old header code from homepage-v1.html
while preserving the navigation menu and all other functionality.
"""

def create_clean_v2():
    # Read homepage-v1.html
    with open('homepage-v1.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Original file size:", len(content), "characters")
    print("Original lines:", content.count('\n'))
    
    # Find and remove NEW HEADER section (around lines 2375-2483)
    # Look for <header class="new-header"> until </header>
    import re
    
    # Pattern 1: Remove NEW HEADER V13
    # Find <header class="new-header"> ... </header>
    new_header_pattern = r'<header class="new-header">.*?</header>'
    matches = re.findall(new_header_pattern, content, re.DOTALL)
    if matches:
        print(f"\nFound NEW HEADER section: {len(matches[0])} characters")
        content = re.sub(new_header_pattern, '', content, flags=re.DOTALL)
        print("Removed NEW HEADER section")
    
    # Pattern 2: Remove DEFAULT HEADER but extract navigation first
    # Find the navigation menu to preserve it
    nav_pattern = r'<nav class="navbar p-0 megamenu">.*?</nav>'
    nav_matches = re.findall(nav_pattern, content, re.DOTALL)
    
    if nav_matches:
        # Save the FIRST navigation menu (the main one)
        navigation_menu = nav_matches[0]
        print(f"\nExtracted navigation menu: {len(navigation_menu)} characters")
        
        # Now remove the entire DEFAULT HEADER section
        # Pattern: <header id="page-header" class="default-header"...> ... </header>
        # But this is tricky because the header on line 2485 is all on one line until </header>
        
        # Find the default-header on line 2485
        default_header_pattern = r'<header id="page-header" class="default-header[^>]*>.*?</header>'
        default_matches = re.findall(default_header_pattern, content, re.DOTALL)
        
        if default_matches:
            # Get the first match (main header)
            first_header = default_matches[0]
            print(f"\nFound DEFAULT HEADER section: {len(first_header)} characters")
            
            # Remove ONLY the first occurrence (the one at line 2485)
            content = content.replace(first_header, '', 1)
            print("Removed first DEFAULT HEADER section")
            
            # Insert the navigation menu back in its place
            # Find a good insertion point - after </style> before countdown
            countdown_pattern = r'(<div id="countdown-wrapper")'
            if re.search(countdown_pattern, content):
                # Insert navigation before countdown
                content = re.sub(countdown_pattern, 
                                f'\n<!-- Preserved Navigation Menu -->\n<nav class="navbar p-0 megamenu">\n{navigation_menu[len("<nav class=\"navbar p-0 megamenu\">"):-len("</nav>")]}\n</nav>\n\n\\1',
                                content, count=1)
                print("Inserted preserved navigation menu before countdown")
    
    # Pattern 3: Remove sticky icons (stuck-left, stuck-right)
    # These are in <div class="hidden-unstuck stuck-left/right">
    stuck_pattern = r'<div class="hidden-unstuck stuck-(?:left|right)">.*?</div>'
    stuck_matches = re.findall(stuck_pattern, content, re.DOTALL)
    print(f"\nFound {len(stuck_matches)} sticky icon sections")
    content = re.sub(stuck_pattern, '', content, flags=re.DOTALL)
    print("Removed all sticky icon sections")
    
    # Pattern 4: Remove old icon color styles (sage-green, ice-blue, orange)
    # These are typically in CSS or inline styles
    # Remove CSS classes for old icons
    old_icon_css_patterns = [
        r'\.icon-sage-green[^}]*}',
        r'\.icon-ice-blue[^}]*}',
        r'\.icon-orange[^}]*}',
        r'\.icon-glassmorphism[^}]*}'
    ]
    
    for pattern in old_icon_css_patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        if matches:
            print(f"\nFound {len(matches)} instances of pattern: {pattern}")
            content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    print("\nCleaned file size:", len(content), "characters")
    print("Cleaned lines:", content.count('\n'))
    print("Difference:", len(content) - len(open('homepage-v1.html', 'r', encoding='utf-8').read()), "characters")
    
    # Write to homepage-v2.html
    with open('homepage-v2.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n✅ Created homepage-v2.html successfully!")
    print("\nSummary:")
    print("- Removed NEW HEADER section")
    print("- Removed DEFAULT HEADER section")
    print("- Preserved navigation menu")
    print("- Removed sticky icons (stuck-left, stuck-right)")
    print("- Removed old icon color CSS")
    
    return True

if __name__ == '__main__':
    create_clean_v2()
