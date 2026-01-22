# FenTuRo Rebranding Integration Plan - V20

## Executive Summary

This document outlines the comprehensive integration plan for rebranding the website from FensterMaxx24 to FenTuRo, including:
1. Logo replacement
2. Brand name updates throughout the site
3. Color scheme migration from sage green (#a9cbb7) to light blue (#6690CC)
4. Font family update to Berlin Sans FB Demi Bold
5. Navigation menu hover color fixes

---

## 📋 **PHASE 1: NAVIGATION TEXT COLOR FIX (IMMEDIATE)**

### **Issue:**
Navigation menu text may not be consistently staying black on hover despite V19 implementation.

### **Action Required:**
1. Deep code review of all navigation hover states
2. Ensure all menu item selectors use `color: #333333 !important` on hover
3. Check for conflicting CSS rules that might override black text
4. Verify both main menu and submenu items

### **Affected Selectors:**
```css
.mainmenu > li > a:hover
.mainmenu > li > a:focus
.mainmenu > li > a:active
.submenu a:hover
.submenu li a:hover
.dropdown-menu a:hover
/* Any other navigation link variants */
```

### **Testing:**
- Hover over all main menu items (Konfigurator, Fenster, Balkontüren, Terrassentüren, Türen, Rollläden)
- Open dropdowns and hover over submenu items
- Verify text remains black/dark (#333333) in all cases

---

## 📋 **PHASE 2: LOGO FILES PREPARATION**

### **Required Files:**
1. `FenTuRo-01.jpg.jpeg` - Primary logo file
2. `Fenturo logo.jpeg` - Alternative logo format
3. `Logo Style Guide UPD.pdf` - Style guide with specifications

### **File URLs:**
- https://github.com/MSHH88/frontend-glass-configurator/blob/main/FenTuRo-01.jpg.jpeg
- https://github.com/MSHH88/frontend-glass-configurator/blob/main/Fenturo%20logo.jpeg
- https://github.com/MSHH88/frontend-glass-configurator/blob/main/Logo%20Style%20Guide%20UPD.pdf

### **Actions:**
1. **Download files** from repository main branch
2. **Analyze logo dimensions** and optimal sizing for header
3. **Convert format if needed** - likely need SVG or PNG with transparency
4. **Optimize file size** for web performance
5. **Create responsive versions** if needed for mobile

### **Logo Specifications:**
- **Current logo**: 180×60px placeholder with sage green gradient
- **New logo sizing**: TBD based on actual logo aspect ratio
- **Format**: Convert JPEG to PNG or SVG for better quality
- **Placement**: Replace existing fenstermaxx24-logo-2.svg
- **Alt text**: Update to "FenTuRo"

---

## 📋 **PHASE 3: BRAND NAME REPLACEMENT**

### **Search & Replace Strategy:**

#### **Case Variations to Replace:**
```
fenstermaxx    → fenturo
FensterMaxx    → FenTuRo
FENSTERMAXX    → FENTURO
Fenstermaxx    → Fenturo
fenstermaxx24  → fenturo
FensterMaxx24  → FenTuRo
```

### **Affected Areas:**
1. **HTML Content**
   - Page titles (`<title>`)
   - Meta descriptions
   - Alt text for images
   - Heading text
   - Body copy
   - Footer content

2. **URLs and Links**
   - Internal links (keep functional, update display text)
   - Canonical URLs (careful - may affect SEO)
   - Image source paths
   - Stylesheet references

3. **CSS**
   - Class names (if any contain brand name)
   - Comments

4. **JavaScript** (if inline in HTML)
   - Variable names
   - String literals

### **Special Considerations:**
- **Domain names**: `fenstermaxx24.com` URLs may need to stay functional for redirects
- **CDN paths**: `cdn03.plentymarkets.com/xbqx3akj5qia/frontend/` - likely stay same
- **External references**: Third-party integrations may reference old name

### **Estimated Occurrences:**
```bash
grep -i "fenstermaxx" homepage-v19.html | wc -l
# Result: Approximately 100+ instances
```

---

## 📋 **PHASE 4: COLOR SCHEME MIGRATION**

### **Color Changes:**

#### **FROM (Current Colors):**
- **Sage Green**: #a9cbb7 (primary brand color)
- **Ice Blue**: (various shades)

#### **TO (New Colors):**
- **Light Blue**: #6690CC (new primary color)
- **Dark Blue**: #000C49 (accent, reserved for future)

### **Implementation Scope (Phase 4):**
Focus ONLY on #6690CC for now:
- Icon backgrounds
- Hover effects and shadows
- Button colors
- Border colors
- Text highlights

### **CSS Selectors to Update:**

#### **1. Background Colors:**
```css
/* OLD */
.bg-sage-green, .btn-sage-green, .btn-primary {
    background-color: #a9cbb7;
}

/* NEW */
.bg-light-blue, .btn-light-blue, .btn-primary {
    background-color: #6690CC;
}
```

#### **2. Border Colors:**
```css
/* OLD */
border-color: #a9cbb7;

/* NEW */
border-color: #6690CC;
```

#### **3. Text Colors:**
```css
/* OLD */
.text-sage-green {
    color: #a9cbb7;
}

/* NEW */
.text-light-blue {
    color: #6690CC;
}
```

#### **4. Icon Colors:**
```css
/* Header icons (account, create account, search) */
background: rgba(169, 203, 183, 0.5); /* OLD sage green */
background: rgba(102, 144, 204, 0.5); /* NEW light blue */
```

#### **5. Hover Effects:**
```css
/* Text shadows */
text-shadow: 
    0 2px 16px rgba(169, 203, 183, 0.8),  /* OLD */
    0 2px 16px rgba(102, 144, 204, 0.8);  /* NEW */

/* Drop shadows */
filter: drop-shadow(0 6px 12px rgba(169, 203, 183, 0.5));  /* OLD */
filter: drop-shadow(0 6px 12px rgba(102, 144, 204, 0.5));  /* NEW */
```

#### **6. Navigation Hover:**
```css
/* Main menu and submenu hover effects */
.mainmenu > li > a:hover {
    text-shadow: 
        0 2px 16px rgba(169, 203, 183, 0.8),  /* OLD */
        0 2px 16px rgba(102, 144, 204, 0.8);  /* NEW */
}
```

### **Affected Components:**

1. **Header Elements:**
   - Logo placeholder gradient
   - Search button background
   - Account icon background
   - Create account icon background
   - Contact icons (phone, email) backgrounds

2. **Navigation Menu:**
   - Hover text shadows
   - Hover drop shadows
   - Active/focus states

3. **Contact Info:**
   - Icon backgrounds
   - Hover text shadows
   - Hover drop shadows

4. **Buttons & CTAs:**
   - Primary buttons
   - Secondary buttons
   - Button hover states
   - Button focus states

5. **Links & Interactions:**
   - Link colors
   - Link hover states
   - Active states

### **Search & Replace Pattern:**
```
Find: rgba\(169, 203, 183,
Replace: rgba(102, 144, 204,

Find: #a9cbb7
Replace: #6690CC
```

### **Estimated Changes:**
- CSS color declarations: ~50-70 instances
- RGBA values: ~30-40 instances
- Inline styles (if any): TBD

---

## 📋 **PHASE 5: FONT FAMILY UPDATE**

### **New Font:**
**Berlin Sans FB Demi Bold**

### **Implementation:**

#### **1. Font Loading:**
```css
/* Check if font is system font or needs web font loading */
/* Berlin Sans FB is a Windows system font */
/* May need fallback for non-Windows systems */
```

#### **2. Font Stack:**
```css
font-family: 'Berlin Sans FB Demi Bold', 'Arial', 'Helvetica', sans-serif;
```

#### **3. Application Scope:**
Determine which elements should use the new font:
- Headers (h1, h2, h3, etc.)
- Body text
- Navigation menu
- Buttons
- Form elements

#### **4. Weight Consideration:**
"Demi Bold" suggests a specific weight (typically 600)
```css
font-family: 'Berlin Sans FB', sans-serif;
font-weight: 600; /* Demi Bold */
```

### **Testing Requirements:**
- Test on Windows (native font)
- Test on Mac (fallback font)
- Test on Linux (fallback font)
- Test on mobile devices

---

## 📋 **PHASE 6: LOGO INTEGRATION**

### **Current Logo Implementation:**
```html
<!-- Line ~360 in homepage-v19.html -->
<link rel="preload" as="image" href="https://cdn03.plentymarkets.com/xbqx3akj5qia/frontend/img/fenstermaxx24-logo-2.svg">

<!-- Line ~2188 in header -->
<div class="logo-section-v13">
    <div class="logo-placeholder-v13">LOGO</div>
</div>
```

### **New Logo Implementation:**

#### **Step 1: Prepare Logo File**
1. Convert JPEG to PNG with transparency (if needed)
2. Or create SVG version for scalability
3. Optimize file size (<50KB recommended)
4. Create 2x version for retina displays

#### **Step 2: Upload Logo**
Options:
- Use GitHub as CDN: Direct link to raw file
- Use existing CDN: Upload to plentymarkets CDN
- Embed as base64 (not recommended for large files)

#### **Step 3: Update HTML**
```html
<!-- Preload -->
<link rel="preload" as="image" href="[NEW_LOGO_URL]">

<!-- Header logo -->
<div class="logo-section-v13">
    <img src="[NEW_LOGO_URL]" 
         alt="FenTuRo" 
         class="logo-fenturo-v20"
         width="180" 
         height="60">
</div>
```

#### **Step 4: Update CSS**
```css
.logo-fenturo-v20 {
    width: 180px;
    height: 60px;
    object-fit: contain; /* Maintain aspect ratio */
    display: block;
}

/* Remove old placeholder styles */
.logo-placeholder-v13 {
    /* Delete or comment out */
}
```

#### **Step 5: Responsive Adjustments**
```css
@media (max-width: 768px) {
    .logo-fenturo-v20 {
        width: 140px;
        height: auto;
    }
}
```

---

## 📋 **PHASE 7: QUALITY ASSURANCE**

### **Testing Checklist:**

#### **Visual Testing:**
- [ ] Logo displays correctly at all screen sizes
- [ ] Logo maintains aspect ratio
- [ ] Logo loads quickly (check network tab)
- [ ] New color (#6690CC) appears consistently
- [ ] Font displays correctly across browsers
- [ ] No broken images or missing assets

#### **Functional Testing:**
- [ ] Logo links to homepage (if clickable)
- [ ] Navigation menu dropdowns work
- [ ] Hover effects work on all icons
- [ ] Search functionality works
- [ ] Cart and account icons functional
- [ ] All internal links work
- [ ] No JavaScript console errors

#### **Brand Consistency:**
- [ ] All instances of "FensterMaxx" changed to "FenTuRo"
- [ ] Consistent capitalization (FenTuRo)
- [ ] All sage green replaced with light blue
- [ ] Navigation text stays black on hover
- [ ] Hover effects use new color

#### **SEO Considerations:**
- [ ] Update meta title
- [ ] Update meta description
- [ ] Update Open Graph tags
- [ ] Update Twitter Card tags
- [ ] Check canonical URLs
- [ ] Update sitemap (if needed)

#### **Cross-Browser Testing:**
- [ ] Chrome (Windows, Mac)
- [ ] Firefox (Windows, Mac)
- [ ] Safari (Mac, iOS)
- [ ] Edge (Windows)
- [ ] Mobile browsers (iOS Safari, Chrome Android)

#### **Performance Testing:**
- [ ] Page load time acceptable
- [ ] Logo file size optimized
- [ ] No render-blocking resources
- [ ] Lighthouse score maintained or improved

---

## 📋 **IMPLEMENTATION TIMELINE**

### **Immediate (V20):**
1. ✅ Fix navigation text color to stay black on hover
2. ⏳ Download and analyze logo files
3. ⏳ Create logo integration plan

### **Phase 2 (V21):**
1. ⏳ Replace all brand name references (fenstermaxx → fenturo)
2. ⏳ Update meta tags and SEO elements
3. ⏳ Prepare logo file for integration

### **Phase 3 (V22):**
1. ⏳ Integrate FenTuRo logo into header
2. ⏳ Update all logo references throughout page
3. ⏳ Test responsive logo display

### **Phase 4 (V23):**
1. ⏳ Replace all sage green (#a9cbb7) with light blue (#6690CC)
2. ⏳ Update icon colors
3. ⏳ Update hover effect colors
4. ⏳ Update navigation hover colors

### **Phase 5 (V24):**
1. ⏳ Implement Berlin Sans FB Demi Bold font
2. ⏳ Test font rendering across devices
3. ⏳ Adjust font weights if needed

### **Final (V25):**
1. ⏳ Comprehensive QA testing
2. ⏳ Performance optimization
3. ⏳ Final WordPress integration preparation

---

## 📋 **RISK ASSESSMENT**

### **High Risk:**
- **SEO Impact**: Changing brand name in URLs/meta tags
  - **Mitigation**: Keep functional URLs, redirect properly
- **External Integration**: Third-party services referencing old name
  - **Mitigation**: Update integrations gradually, maintain compatibility

### **Medium Risk:**
- **Logo File Size**: Large JPEG files slow page load
  - **Mitigation**: Convert to optimized PNG/SVG
- **Font Loading**: Berlin Sans FB not available on all systems
  - **Mitigation**: Provide proper fallback fonts
- **Color Contrast**: Light blue may affect accessibility
  - **Mitigation**: Test contrast ratios, adjust if needed

### **Low Risk:**
- **CSS Specificity**: New colors may not override old ones
  - **Mitigation**: Use !important where necessary
- **Browser Caching**: Users may see old colors/logo
  - **Mitigation**: Update cache-busting versioning

---

## 📋 **ROLLBACK PLAN**

If issues arise during implementation:

1. **Git Revert**: Each phase committed separately
   ```bash
   git revert <commit-hash>
   ```

2. **File Backup**: Keep V19 as stable baseline
   ```bash
   cp homepage-v19.html homepage-v19-backup.html
   ```

3. **Staged Rollback**: Revert only problematic phases
   - Phase 1 (nav fix) independent
   - Phase 2 (name change) independent
   - Phase 3 (logo) independent
   - Phase 4 (colors) independent
   - Phase 5 (font) independent

---

## 📋 **NOTES & CONSIDERATIONS**

### **Style Guide Analysis:**
- Review `Logo Style Guide UPD.pdf` for:
  - Official logo usage guidelines
  - Color specifications (CMYK, RGB, HEX)
  - Minimum size requirements
  - Clear space requirements
  - Acceptable color variations
  - Font specifications

### **Color Accessibility:**
- **#6690CC** (light blue) contrast ratio:
  - Against white: Need to verify meets WCAG AA (4.5:1)
  - Against black text: Should be sufficient
  - For hover effects: Ensure visibility

### **Brand Consistency:**
- Maintain consistent capitalization: **FenTuRo**
- Not: Fenturo, FENTURO, fenTuRo, etc.

### **WordPress Considerations:**
- Final integration into WordPress may require:
  - Custom CSS adjustments
  - Theme compatibility checks
  - Plugin compatibility checks
  - Cache clearing instructions

---

## 📋 **SUCCESS CRITERIA**

### **Phase 1 Complete When:**
- ✅ Navigation text always black on hover
- ✅ No color changes on hover except shadows
- ✅ Tested across all menu items

### **Phase 2 Complete When:**
- ✅ Logo files downloaded and analyzed
- ✅ Logo optimized for web
- ✅ Logo dimensions determined

### **Phase 3 Complete When:**
- ✅ All "fenstermaxx" instances replaced
- ✅ Capitalization consistent
- ✅ No broken references

### **Phase 4 Complete When:**
- ✅ New logo integrated in header
- ✅ Logo displays properly at all sizes
- ✅ Logo loads quickly

### **Phase 5 Complete When:**
- ✅ All sage green replaced with #6690CC
- ✅ Icons use new color
- ✅ Hover effects use new color
- ✅ Visual consistency achieved

### **Phase 6 Complete When:**
- ✅ Font family updated throughout
- ✅ Font renders correctly across devices
- ✅ Typography hierarchy maintained

### **Final Success:**
- ✅ All phases complete
- ✅ QA testing passed
- ✅ Performance acceptable
- ✅ Ready for WordPress deployment

---

**Document Version**: 1.0  
**Created**: 2026-01-22  
**Status**: Draft - Awaiting logo files and style guide review  
**Next Action**: Phase 1 - Fix navigation text color + Download logo files
