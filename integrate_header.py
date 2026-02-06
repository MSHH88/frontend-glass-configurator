#!/usr/bin/env python3
"""
Script to integrate header-v7 into homepage-v1.html
Preserves the navigation menu while adding header-v7 design
"""

# Read header-v7.html
with open('header-v7.html', 'r', encoding='utf-8') as f:
    header_v7_content = f.read()

# Read homepage-v1.html
with open('homepage-v1.html', 'r', encoding='utf-8') as f:
    homepage_content = f.read()

# Extract CSS from header-v7 (lines 7-718)
header_v7_lines = header_v7_content.split('\n')
# Get CSS content (from <style> to </style>)
style_start = None
style_end = None
for i, line in enumerate(header_v7_lines):
    if '<style>' in line and style_start is None:
        style_start = i
    if '</style>' in line and style_end is None:
        style_end = i
        break

header_v7_css = '\n'.join(header_v7_lines[style_start+1:style_end])

# Extract HTML from header-v7 (lines 722-779)
html_start = None
html_end = None
for i, line in enumerate(header_v7_lines):
    if '<header class="site-header">' in line:
        html_start = i
    if '</header>' in line and html_start is not None and html_end is None:
        html_end = i
        break

header_v7_html = '\n'.join(header_v7_lines[html_start:html_end+1])

# Now insert into homepage-v1.html
homepage_lines = homepage_content.split('\n')

# Find where to insert CSS (before </head>)
head_end_index = None
for i, line in enumerate(homepage_lines):
    if '</head>' in line:
        head_end_index = i
        break

# Find the default-header location (search for page-header id)
default_header_index = None
for i, line in enumerate(homepage_lines):
    if 'id="page-header"' in line and 'header' in line.lower():
        default_header_index = i
        break

print(f"Found </head> at line {head_end_index}")
print(f"Found default-header at line {default_header_index}")

# Insert header-v7 CSS before </head>
homepage_lines.insert(head_end_index, '    <!-- Header-v7 Styles -->')
homepage_lines.insert(head_end_index + 1, '    <style>')
homepage_lines.insert(head_end_index + 2, header_v7_css)
homepage_lines.insert(head_end_index + 3, '    </style>')

# Adjust index after insertions
default_header_index += 4

# Insert header-v7 HTML before the default-header
homepage_lines.insert(default_header_index, '')
homepage_lines.insert(default_header_index + 1, '    <!-- Header-v7 Integration -->')
homepage_lines.insert(default_header_index + 2, header_v7_html)
homepage_lines.insert(default_header_index + 3, '')

# Write the updated homepage-v1.html
with open('homepage-v1.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(homepage_lines))

print("✅ Integration complete!")
print(f"- Inserted header-v7 CSS before </head>")
print(f"- Inserted header-v7 HTML before default-header")
print(f"- Navigation menu preserved")
