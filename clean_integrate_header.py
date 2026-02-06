#!/usr/bin/env python3
"""
Clean integration of header-v7 into homepage-v1.
This script:
1. Removes ALL old header code from homepage-v34
2. Extracts and preserves ONLY the navigation menu
3. Integrates header-v7 completely and correctly
"""

import re

# Read files
with open('homepage-v34.html', 'r', encoding='utf-8') as f:
    homepage = f.read()

with open('header-v7.html', 'r', encoding='utf-8') as f:
    header_v7 = f.read()

print("Step 1: Extract header-v7 components...")

# Extract header-v7 CSS (between <style> tags in <head>)
v7_css_match = re.search(r'<style>(.*?)</style>', header_v7, re.DOTALL)
v7_css = v7_css_match.group(1) if v7_css_match else ""
print(f"  - Extracted {len(v7_css)} chars of CSS")

# Extract header-v7 HTML (the <header class="site-header"> element)
v7_header_match = re.search(r'<header class="site-header">(.*?)</header>', header_v7, re.DOTALL)
v7_header_html = v7_header_match.group(0) if v7_header_match else ""
print(f"  - Extracted {len(v7_header_html)} chars of HTML")

# Extract header-v7 JavaScript (all <script> tags in body)
v7_scripts = []
for script_match in re.finditer(r'<script>(.*?)</script>', header_v7, re.DOTALL):
    v7_scripts.append(script_match.group(1))
v7_js = '\n'.join(v7_scripts)
print(f"  - Extracted {len(v7_js)} chars of JavaScript")

print("\nStep 2: Find and extract navigation menu from homepage...")

# Find the navigation menu - it's inside <nav class="navbar p-0 megamenu">
nav_pattern = r'(<nav class="navbar p-0 megamenu">.*?</nav>)'
nav_match = re.search(nav_pattern, homepage, re.DOTALL)
if nav_match:
    navigation_html = nav_match.group(1)
    print(f"  - Found navigation menu ({len(navigation_html)} chars)")
else:
    print("  - ERROR: Could not find navigation menu!")
    navigation_html = ""

print("\nStep 3: Remove ALL old header code...")

# Remove the "NEW HEADER V13 DESIGN" section (around line 2375 in original)
# Pattern: <!-- NEW HEADER V13 DESIGN --> ... </header>
homepage = re.sub(
    r'<!-- NEW HEADER V13 DESIGN -->.*?</header>',
    '',
    homepage,
    flags=re.DOTALL
)
print("  - Removed NEW HEADER V13 section")

# Remove the default-header (but we'll add back just the nav)
# Pattern: <header id="page-header" class="default-header" ... </header>
homepage = re.sub(
    r'<header id="page-header"[^>]*>.*?</header>',
    '<!-- NAVIGATION PLACEHOLDER -->',
    homepage,
    flags=re.DOTALL
)
print("  - Removed default-header section")

print("\nStep 4: Integrate header-v7...")

# Add header-v7 CSS before </head>
css_insertion = f'\n    <!-- Header-v7 Styles -->\n    <style>\n{v7_css}\n    </style>\n'
homepage = homepage.replace('</head>', css_insertion + '</head>')
print("  - Inserted header-v7 CSS")

# Add header-v7 HTML before the navigation placeholder
# Fix logo link to point to / instead of #
v7_header_html = v7_header_html.replace('href="#"', 'href="/"')

header_insertion = f'''
    <!-- Header-v7 Integration -->
    {v7_header_html}

    <!-- Navigation Menu (Preserved from original) -->
    <div class="navigation-wrapper">
        {navigation_html}
    </div>
'''
homepage = homepage.replace('<!-- NAVIGATION PLACEHOLDER -->', header_insertion)
print("  - Inserted header-v7 HTML and navigation")

# Add header-v7 JavaScript before </body>
if v7_js:
    js_insertion = f'\n    <!-- Header-v7 Scripts -->\n    <script>\n{v7_js}\n    </script>\n'
    homepage = homepage.replace('</body>', js_insertion + '</body>')
    print("  - Inserted header-v7 JavaScript")

print("\nStep 5: Save integrated file...")

with open('homepage-v1.html', 'w', encoding='utf-8') as f:
    f.write(homepage)

print("\n✅ DONE! Created homepage-v1.html with clean header-v7 integration")
print("\nVerification:")
print(f"  - Header-v7 CSS: {len(v7_css)} chars")
print(f"  - Header-v7 HTML: {len(v7_header_html)} chars")
print(f"  - Header-v7 JS: {len(v7_js)} chars")
print(f"  - Navigation menu: {len(navigation_html)} chars")
print(f"  - Final file size: {len(homepage)} chars")
