# Navigation Menu Redesign Guide

**Version:** 1.0  
**Last Updated:** February 10, 2026  
**Purpose:** Complete guide for redesigning navigation menu without disrupting code functionality

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Image Integration](#image-integration)
3. [Menu Structure Changes](#menu-structure-changes)
4. [CSS Modifications](#css-modifications)
5. [Manufacturer Management](#manufacturer-management)
6. [Code Preservation Guidelines](#code-preservation-guidelines)
7. [Testing & Verification](#testing--verification)

---

## Overview

This guide documents all changes made to the navigation menu in homepage-v2.html, which became the new baseline (homepage-v1.html). The redesign focused on:

- Adding visual images to menu items
- Implementing fade effects on images
- Removing specific manufacturers
- Optimizing menu layout
- Maintaining all functionality

---

## Image Integration

### Images Used

**DogWIN1.png** (2.6 MB)
- Used for: Fenster, Rolläden
- Location in repository: Root directory
- URL: `DogWIN1.png`

**DogWIN2.png** (2.3 MB)
- Used for: Balkontüren
- Location in repository: Root directory
- URL: `DogWIN2.png`

### HTML Implementation

**Location:** Lines 3110-3117 in homepage-v2.html

```html
<!-- Fenster Menu Image -->
<li class="level1 no-padding forcedColBreak">
    <img loading="lazy" src="DogWIN1.png" alt="blockimage" class="img-fluid menu-block-image">
</li>

<!-- Balkontüren Menu Image -->
<li class="level1 no-padding forcedColBreak">
    <img loading="lazy" src="DogWIN2.png" alt="blockimage" class="img-fluid menu-block-image">
</li>

<!-- Rolläden Menu Image -->
<li class="level1 no-padding forcedColBreak">
    <img loading="lazy" src="DogWIN1.png" alt="blockimage" class="img-fluid menu-block-image">
</li>
```

### Key Attributes

- `loading="lazy"` - Performance optimization, loads image when menu opens
- `alt="blockimage"` - Accessibility compliance
- `class="img-fluid menu-block-image"` - Responsive sizing and custom styling
- `class="level1 no-padding forcedColBreak"` - Menu hierarchy and layout control

---

## Menu Structure Changes

### Structure Overview

The navigation menu uses a hierarchical `<ul>` list structure:

```html
<ul class="sf-menu main-menu">
    <li class="level0 navblock-fenster">
        <a href="/fenster" class="level0 has-children">Fenster</a>
        <ul class="sf-mega level0">
            <li class="level1">
                <ul class="level1">
                    <!-- Menu items here -->
                    <li class="level1 no-padding forcedColBreak">
                        <img src="DogWIN1.png" class="img-fluid menu-block-image">
                    </li>
                </ul>
            </li>
        </ul>
    </li>
</ul>
```

### Important CSS Classes

- `.navblock-fenster` - Identifies Fenster menu block (used for specific styling)
- `.sf-menu` - Superfish menu framework
- `.sf-mega` - Mega menu styling
- `.level0`, `.level1` - Menu hierarchy levels
- `.has-children` - Indicates dropdown presence
- `.forcedColBreak` - Forces column break in layout

---

## CSS Modifications

### Fade Effect on All Images

**Location:** Line 1194 in homepage-v2.html

```css
.menu-block-image {
    -webkit-mask-image: radial-gradient(ellipse at center, 
        rgba(0,0,0,1) 0%, 
        rgba(0,0,0,1) 60%, 
        rgba(0,0,0,0.7) 80%,
        rgba(0,0,0,0) 100%);
    mask-image: radial-gradient(ellipse at center, 
        rgba(0,0,0,1) 0%, 
        rgba(0,0,0,1) 60%, 
        rgba(0,0,0,0.7) 80%,
        rgba(0,0,0,0) 100%);
}
```

**Effect:**
- 0-60%: Full opacity (center fully visible)
- 60-80%: Gradual fade begins
- 80-100%: Fades to transparent
- Applied to all 4 sides (radial gradient)

**Browser Support:**
- `-webkit-mask-image` for Chrome/Safari/Edge
- `mask-image` for Firefox

### Fenster Menu Image Scaling

**Location:** Line 1203 in homepage-v2.html

```css
.navblock-fenster .menu-block-image {
    transform: scale(1.1);
    transform-origin: center;
}
```

**Effect:**
- Makes Fenster image 10% larger than other menu images
- Scales from center to maintain balance
- Uses GPU-accelerated transform for smooth rendering

---

## Manufacturer Management

### Removed Manufacturers (Fenster Menu)

The following manufacturers were removed from the Fenster navigation menu:

1. **Trocal Fenster**
   - Link: `/fenster/trocal`
   - Reason: User request for streamlined menu

2. **Kömmerling Fenster**
   - Link: `/fenster/koemmerling`
   - Reason: User request for streamlined menu

### Remaining Manufacturers (Fenster Menu)

1. Drutex Fenster
2. Gealan Fenster
3. Aluplast Fenster
4. Salamander Fenster
5. Veka Fenster
6. Schüco Fenster

### Removed Links/Sections

**Fenster Sonderposten**
- Previous location: Line 3107
- Type: Special offers section
- Removed: Complete `<li>` element with link and text

---

## Code Preservation Guidelines

### What to Preserve

When making navigation menu changes, always preserve:

1. **Menu Structure**
   - `<ul>` and `<li>` hierarchy
   - Class names on parent elements
   - Menu framework classes (`.sf-menu`, `.sf-mega`)

2. **Functionality Classes**
   - `.has-children` - Required for dropdown detection
   - `.level0`, `.level1`, `.level2` - Menu hierarchy
   - Navigation JavaScript selectors

3. **Links**
   - `href` attributes must remain valid
   - `title` attributes for SEO and accessibility
   - `data-catId` attributes for tracking

4. **Responsive Behavior**
   - Media query breakpoints
   - Mobile menu transformations
   - Touch event handlers

### Safe Modification Areas

You can safely modify:

1. **Images**
   - `src` attributes (change image URLs)
   - `alt` text
   - Image-specific CSS classes

2. **Text Content**
   - Link text (keep descriptive)
   - Menu item labels

3. **CSS Styling**
   - Colors, fonts, sizes
   - Spacing and padding
   - Visual effects (gradients, shadows)

4. **Adding New Items**
   - Follow existing `<li>` structure
   - Include proper class hierarchy
   - Test dropdown behavior

### Dangerous Modifications

Avoid changing:

1. **JavaScript Selectors**
   - Classes used in JavaScript event handlers
   - IDs used for menu manipulation

2. **Framework Classes**
   - Superfish menu classes
   - Bootstrap grid classes
   - Utility classes (`.img-fluid`, etc.)

3. **Menu Hierarchy**
   - Parent-child relationships
   - Level depth (0, 1, 2)
   - Dropdown containers

---

## Testing & Verification

### Visual Testing Checklist

- [ ] Hover over menu items - dropdowns open smoothly
- [ ] Images display correctly in dropdowns
- [ ] Fade effects visible on all sides
- [ ] Fenster image is visibly larger (10%)
- [ ] No layout breaks or overlaps
- [ ] All links clickable and functional

### Functional Testing Checklist

- [ ] All menu items navigate to correct pages
- [ ] Dropdown menus close when clicking away
- [ ] Keyboard navigation works (Tab, Enter, Escape)
- [ ] Mobile menu transforms properly
- [ ] Touch events work on tablets/phones

### Browser Testing

Test in:
- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

### Code Validation

- [ ] HTML validates (no broken tags)
- [ ] CSS validates (proper syntax)
- [ ] No console errors in browser
- [ ] Images load successfully
- [ ] No 404 errors in network tab

---

## Implementation Workflow

### Step-by-Step Process

1. **Backup**
   - Copy current file to backup (e.g., homepage-v1-backup.html)
   - Commit to version control

2. **Add Images to Repository**
   - Upload DogWIN1.png and DogWIN2.png to root directory
   - Verify file sizes and formats

3. **Locate Menu Structure**
   - Find navigation `<ul>` element (search for `class="sf-menu"`)
   - Identify menu blocks (`.navblock-fenster`, etc.)

4. **Add Image Elements**
   - Insert `<li>` with image before closing `</ul>`
   - Use `class="level1 no-padding forcedColBreak"`
   - Add proper `img` tag with attributes

5. **Add CSS Styling**
   - Add fade effect CSS to existing `<style>` section
   - Add menu-specific scaling if needed
   - Test in browser

6. **Remove Unwanted Items**
   - Delete complete `<li>` elements (not just content)
   - Verify no orphaned tags left
   - Check closing tags

7. **Test Thoroughly**
   - Open page in browser
   - Test all menu interactions
   - Verify responsive behavior
   - Check console for errors

8. **Commit Changes**
   - Write descriptive commit message
   - Document what was changed
   - Push to repository

---

## Quick Reference

### CSS Selectors

```css
/* All menu images */
.menu-block-image { }

/* Fenster menu specific */
.navblock-fenster .menu-block-image { }

/* Balkontüren menu specific */
.navblock-balkonturen .menu-block-image { }

/* Rolläden menu specific */
.navblock-rolladen .menu-block-image { }
```

### HTML Template for New Menu Image

```html
<li class="level1 no-padding forcedColBreak">
    <img loading="lazy" 
         src="YOUR_IMAGE.png" 
         alt="blockimage" 
         class="img-fluid menu-block-image">
</li>
```

### Image Requirements

- **Format:** PNG, WebP, or JPG
- **Size:** 2-3 MB max (for performance)
- **Dimensions:** Responsive (will scale with CSS)
- **Location:** Root directory or `/img/` folder
- **Naming:** Descriptive, lowercase, no spaces

---

## Troubleshooting

### Images Not Displaying

**Check:**
1. Image file exists in correct location
2. File name matches exactly (case-sensitive)
3. Path in `src` attribute is correct
4. Browser console for 404 errors

**Solution:**
- Verify file path: `src="DogWIN1.png"` or `src="./DogWIN1.png"`
- Check file permissions
- Clear browser cache

### Fade Effect Not Working

**Check:**
1. CSS is in `<style>` section
2. Class `.menu-block-image` is on `<img>` tag
3. Browser supports mask-image

**Solution:**
- Add `-webkit-` prefix for Safari
- Test in different browser
- Check CSS syntax (closing braces, semicolons)

### Menu Layout Broken

**Check:**
1. All `<li>` tags have closing `</li>`
2. `<ul>` structure is intact
3. No missing closing tags

**Solution:**
- Validate HTML
- Use browser DevTools to inspect structure
- Compare with working version

### Links Not Working

**Check:**
1. `href` attributes present
2. URLs are valid
3. No JavaScript errors blocking clicks

**Solution:**
- Verify href="/correct/path"
- Check browser console for errors
- Test link in new tab

---

## Version History

### Version 1.0 (February 10, 2026)
- Initial documentation
- Covered image integration
- Documented fade effects
- Included manufacturer changes
- Added testing guidelines

---

## Additional Resources

### Files Referenced
- `homepage-v2.html` - Working version with all changes
- `homepage-v1.html` - New baseline (copy of v2)
- `DogWIN1.png` - Menu image for Fenster & Rolläden
- `DogWIN2.png` - Menu image for Balkontüren

### External Documentation
- [Superfish Menu Documentation](http://users.tpg.com.au/j_birch/plugins/superfish/)
- [CSS Mask Image MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/mask-image)
- [Bootstrap Grid System](https://getbootstrap.com/docs/4.6/layout/grid/)

---

**End of Navigation Menu Redesign Guide**
