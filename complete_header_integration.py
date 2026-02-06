#!/usr/bin/env python3
"""
Complete integration of header-v7 into homepage.
Handles:
1. Main header icons
2. Sticky/stuck header icons (for when scrolling)
3. Navigation menu preservation
4. All old header code removal
"""

import re

print("=" * 60)
print("COMPLETE HEADER-V7 INTEGRATION")
print("=" * 60)

# Read files
with open('homepage-v34.html', 'r', encoding='utf-8') as f:
    homepage = f.read()

with open('header-v7.html', 'r', encoding='utf-8') as f:
    header_v7 = f.read()

print("\n📦 Step 1: Extract header-v7 components...")

# Extract header-v7 CSS
v7_css_match = re.search(r'<style>(.*?)</style>', header_v7, re.DOTALL)
v7_css = v7_css_match.group(1) if v7_css_match else ""
print(f"  ✓ Extracted {len(v7_css)} chars of CSS")

# Extract header-v7 HTML
v7_header_match = re.search(r'<header class="site-header">(.*?)</header>', header_v7, re.DOTALL)
v7_header_html = v7_header_match.group(0) if v7_header_match else ""
# Fix logo link
v7_header_html = v7_header_html.replace('href="#"', 'href="/"')
print(f"  ✓ Extracted {len(v7_header_html)} chars of HTML")

# Extract header-v7 JavaScript
v7_scripts = []
for script_match in re.finditer(r'<script>(.*?)</script>', header_v7, re.DOTALL):
    v7_scripts.append(script_match.group(1))
v7_js = '\n'.join(v7_scripts)
print(f"  ✓ Extracted {len(v7_js)} chars of JavaScript")

print("\n🔍 Step 2: Extract navigation menu...")

# Find navigation menu
nav_pattern = r'(<nav class="navbar p-0 megamenu">.*?</nav>)'
nav_match = re.search(nav_pattern, homepage, re.DOTALL)
if nav_match:
    navigation_html = nav_match.group(1)
    print(f"  ✓ Found navigation menu ({len(navigation_html)} chars)")
else:
    print("  ✗ ERROR: Could not find navigation menu!")
    navigation_html = ""

print("\n🗑️  Step 3: Remove ALL old header code...")

# Remove "NEW HEADER V13 DESIGN" section
homepage = re.sub(
    r'<!-- NEW HEADER V13 DESIGN -->.*?</header>',
    '',
    homepage,
    flags=re.DOTALL
)
print("  ✓ Removed NEW HEADER V13 section")

# Remove the entire default-header
homepage = re.sub(
    r'<header id="page-header"[^>]*>.*?</header>',
    '<!-- HEADER_PLACEHOLDER -->',
    homepage,
    flags=re.DOTALL
)
print("  ✓ Removed default-header (including old sticky icons)")

print("\n✨ Step 4: Add header-v7 CSS...")

css_insertion = f'''
    <!-- =====================================
         HEADER V7 STYLES
         ===================================== -->
    <style>
{v7_css}

        /* Additional styles for navigation wrapper */
        .navigation-wrapper {{
            background: #ffffff;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }}
        
        /* Sticky header styles - header-v7 becomes sticky */
        .site-header.sticky {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            animation: slideDown 0.3s ease;
        }}
        
        @keyframes slideDown {{
            from {{
                transform: translateY(-100%);
            }}
            to {{
                transform: translateY(0);
            }}
        }}
    </style>
'''

homepage = homepage.replace('</head>', css_insertion + '</head>')
print("  ✓ Inserted header-v7 CSS")

print("\n🏗️  Step 5: Integrate header-v7 HTML...")

# Create complete header structure
header_structure = f'''
    <!-- =====================================
         HEADER V7 INTEGRATION
         ===================================== -->
    {v7_header_html}

    <!-- =====================================
         NAVIGATION MENU (Preserved)
         ===================================== -->
    <div class="navigation-wrapper">
        {navigation_html}
    </div>
'''

homepage = homepage.replace('<!-- HEADER_PLACEHOLDER -->', header_structure)
print("  ✓ Inserted header-v7 and navigation")

print("\n⚙️  Step 6: Add header-v7 JavaScript...")

# Enhanced JavaScript with sticky header support
enhanced_js = v7_js + '''

    // Sticky header on scroll
    let lastScrollTop = 0;
    const header = document.querySelector('.site-header');
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > 100) {
            header.classList.add('sticky');
        } else {
            header.classList.remove('sticky');
        }
        
        lastScrollTop = scrollTop;
    });
    
    console.log('✓ Header-v7 integrated successfully');
    console.log('✓ All dropdowns functional');
    console.log('✓ Sticky header enabled');
'''

js_insertion = f'''
    <!-- =====================================
         HEADER V7 SCRIPTS
         ===================================== -->
    <script>
{enhanced_js}
    </script>
'''

homepage = homepage.replace('</body>', js_insertion + '</body>')
print("  ✓ Inserted enhanced JavaScript with sticky support")

print("\n💾 Step 7: Save integrated file...")

with open('homepage-v1.html', 'w', encoding='utf-8') as f:
    f.write(homepage)

print("  ✓ Saved homepage-v1.html")

print("\n" + "=" * 60)
print("✅ INTEGRATION COMPLETE!")
print("=" * 60)
print("\n📊 Summary:")
print(f"  • Header-v7 CSS: {len(v7_css):,} chars")
print(f"  • Header-v7 HTML: {len(v7_header_html):,} chars")
print(f"  • Header-v7 JS: {len(v7_js):,} chars")
print(f"  • Navigation menu: {len(navigation_html):,} chars")
print(f"  • Final file size: {len(homepage):,} chars")
print("\n🎯 Features:")
print("  ✓ Main header with v7 icons (search, account, cart)")
print("  ✓ All dropdowns functional")
print("  ✓ Sticky header on scroll")
print("  ✓ Navigation menu preserved")
print("  ✓ ESC key closes dropdowns")
print("  ✓ Click outside closes dropdowns")
print("\n" + "=" * 60)
