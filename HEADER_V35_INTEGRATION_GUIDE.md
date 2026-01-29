# Header V35 Integration Guide

## 📋 Overview

This guide provides step-by-step instructions for integrating the perfect Header V35 design into any page of the website.

**Preview File:** `header-preview-v35.html`
**Version:** 35
**Date:** 2026-01-29
**Status:** Production Ready

---

## 🎯 Specifications

### Header Dimensions
- **Total Height:** 260px
- **Logo Size:** 250×250px (forced, no auto-scaling)
- **Top Padding:** 5px
- **Bottom Padding:** 5px
- **Horizontal Padding:** 20px

### Search Bar
- **Container Max-Width:** 450px
- **Input Padding:** 14px 45px 14px 60px
- **Icon Position:** right: -20px (close to input)
- **Gap:** ~40px between icon and text (reduced from 200px)

### Design Principles
- ✅ No Vue.js interference
- ✅ Pure HTML/CSS
- ✅ No !important overrides
- ✅ Clean, maintainable code
- ✅ Fully responsive

---

## 🔧 Integration Steps

### Step 1: Locate Existing Header

Find the current header in your file:
```html
<header class="old-header-class">
    <!-- old header content -->
</header>
```

Or search for:
- `<header`
- Class names like `.header`, `.main-header`, `.site-header`
- Logo image tags

### Step 2: Extract V35 CSS

From `header-preview-v35.html`, copy the CSS section marked:
```css
/* ========================================
   HEADER V35 - PERFECT DESIGN
   Copy from here for integration
   ======================================== */
```

**Lines to Copy:** 27-275 in header-preview-v35.html

### Step 3: Add CSS to Your Page

**Option A: Inline in `<style>` tag**
```html
<head>
    <!-- ... other head content ... -->
    <style>
        /* Paste V35 header CSS here */
        .new-header { min-height: 260px; ... }
        /* ... rest of CSS ... */
    </style>
</head>
```

**Option B: External CSS file**
```html
<head>
    <link rel="stylesheet" href="header-v35.css">
</head>
```

### Step 4: Replace Header HTML

Remove old header and replace with V35 header HTML:
```html
<!-- HEADER V35 - PERFECT IMPLEMENTATION -->
<header class="new-header">
    <div class="header-main">
        <!-- LEFT: Logo Section -->
        <div class="logo-section-v13">
            <a href="/">
                <img src="Logo-01.png" 
                     alt="FenTuRo Logo" 
                     width="250" 
                     height="250">
            </a>
        </div>

        <!-- CENTER: Search Section -->
        <div class="search-section-v13">
            <div class="search-container-v13">
                <input type="text" 
                       class="search-input-v13" 
                       placeholder="Suchen Sie nach Produkten..."
                       aria-label="Suche">
                <button class="search-button-v13" type="submit" aria-label="Suchen">
                    <div class="icon-glassmorphism-v13">
                        <svg viewBox="0 0 24 24" fill="none">
                            <path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" 
                                  stroke="currentColor" 
                                  stroke-width="2.5" 
                                  stroke-linecap="round" 
                                  stroke-linejoin="round" 
                                  fill="none"
                                  style="color: #4299e1;"/>
                        </svg>
                    </div>
                </button>
            </div>
        </div>

        <!-- RIGHT: Contact Section -->
        <div class="contact-section-v13">
            <a href="tel:+4932221092363" class="contact-item-v13">
                <div class="contact-icon-v13">
                    <svg viewBox="0 0 24 24" fill="currentColor">
                        <path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z"/>
                    </svg>
                </div>
                <div class="contact-text-v13">
                    <span class="contact-label-v13">Telefon</span>
                    <span class="contact-value-v13">0322 2109 2363</span>
                </div>
            </a>

            <a href="mailto:info@fenstermaxx24.com" class="contact-item-v13">
                <div class="contact-icon-v13">
                    <svg viewBox="0 0 24 24" fill="currentColor">
                        <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
                    </svg>
                </div>
                <div class="contact-text-v13">
                    <span class="contact-label-v13">E-Mail</span>
                    <span class="contact-value-v13">info@fenstermaxx24.com</span>
                </div>
            </a>
        </div>
    </div>
</header>
```

### Step 5: Verify Logo Path

Ensure the logo image is accessible:
```html
<img src="Logo-01.png" ...>
```

**Adjust path if needed:**
- Same directory: `Logo-01.png`
- Assets folder: `assets/Logo-01.png`
- Root: `/Logo-01.png`

### Step 6: Remove Old CSS

Search for and remove old header CSS:
- `.old-header { ... }`
- `.site-header { ... }`
- Any conflicting styles

**Important:** Don't remove global styles like `*`, `body`, `html`

---

## ✅ Verification Checklist

After integration, verify these measurements:

### Visual Checks
- [ ] Header height measures exactly 260px
- [ ] Logo displays at 250×250px (not auto-scaled)
- [ ] Search icon is ~40px from input text (not 200px)
- [ ] Search bar max-width is 450px
- [ ] Contact icons are visible and aligned
- [ ] All elements vertically centered

### Functional Checks
- [ ] Logo link goes to homepage
- [ ] Search input is focusable
- [ ] Search button is clickable
- [ ] Phone link opens dialer (mobile)
- [ ] Email link opens mail client
- [ ] No JavaScript errors in console

### Responsive Checks
- [ ] Desktop (>1200px): All elements in one row
- [ ] Tablet (768-1200px): Search moves below, spans full width
- [ ] Mobile (<768px): Logo shrinks to 180px, contact info stacked
- [ ] Small mobile (<480px): Logo 150px, contact text hidden

### Browser Compatibility
- [ ] Chrome/Edge (Chromium)
- [ ] Safari (WebKit)
- [ ] Firefox (Gecko)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

---

## 🐛 Troubleshooting

### Issue: Header Still Too Tall

**Possible Causes:**
1. Old CSS not removed
2. Vue.js overriding styles
3. Parent container constraining height

**Solutions:**
```css
/* Add higher specificity if needed */
header.new-header {
    min-height: 260px !important; /* Last resort */
}

/* Or check parent */
#vue-app > header.new-header {
    min-height: 260px;
}
```

### Issue: Logo Auto-Scaling

**Problem:** Logo not displaying at 250×250px

**Solution:**
```css
.logo-section-v13 img {
    width: 250px !important;
    height: 250px !important;
    max-width: 250px;
    max-height: 250px;
}
```

### Issue: Search Icon Too Far

**Problem:** Gap still ~200px between icon and input

**Solutions:**
1. Check section padding:
   ```css
   .search-section-v13 {
       padding: 0 0px; /* Should be 0, not 20px */
   }
   ```

2. Check container width:
   ```css
   .search-container-v13 {
       max-width: 450px; /* Should be 450, not 538 */
   }
   ```

3. Check icon position:
   ```css
   .search-button-v13 {
       right: -20px; /* Should be -20, not 8px */
   }
   ```

### Issue: Vue.js Conflicts

**Problem:** Styles reset after page load

**Solution A:** Move header outside Vue app:
```html
<body>
    <header class="new-header">...</header>
    <div id="vue-app">
        <!-- Rest of content -->
    </div>
</body>
```

**Solution B:** Use Vue component:
```javascript
Vue.component('site-header', {
    template: `<header class="new-header">...</header>`
});
```

---

## 📝 Integration for Specific Pages

### Homepage
1. Replace header in `homepage-v34.html`
2. Keep configurator section below header
3. Test manufacturers section alignment

### Configurator Pages
1. Replace header at top of page
2. Ensure configurator tool remains functional
3. Test product images load correctly

### Product Pages
1. Replace header
2. Verify product details section alignment
3. Test "Add to Cart" functionality

### Info Pages (Contact, About, etc.)
1. Replace header
2. Keep page-specific content
3. Test form submissions (if any)

---

## 🚀 Quick Copy-Paste Integration

### Minimal Integration (CSS + HTML)

1. **Add to `<style>` section:**
```css
.new-header { min-height: 260px; padding: 5px 20px; background-color: #ffffff; border-bottom: 1px solid #e0e0e0; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); }
.header-main { display: flex; align-items: center; justify-content: space-between; max-width: 1500px; margin: 0 auto; height: 100%; }
.logo-section-v13 { flex: 0 0 auto; margin-right: 60px; }
.logo-section-v13 a { display: block; text-decoration: none; }
.logo-section-v13 img { display: block; width: 250px; height: 250px; object-fit: contain; }
.search-section-v13 { flex: 1; display: flex; justify-content: center; align-items: center; padding: 0 0px; max-width: 600px; }
.search-container-v13 { position: relative; width: 100%; max-width: 450px; }
.search-input-v13 { width: 100%; padding: 14px 45px 14px 60px; border: 2px solid #e2e8f0; border-radius: 24px; font-size: 15px; color: #2d3748; background-color: #f7fafc; transition: all 0.3s ease; outline: none; }
.search-button-v13 { position: absolute; right: -20px; top: 50%; transform: translateY(-50%); background: none; border: none; cursor: pointer; padding: 0; z-index: 10; }
.icon-glassmorphism-v13 { width: 48px; height: 48px; border-radius: 50%; background: rgba(66, 153, 225, 0.1); backdrop-filter: blur(10px) saturate(180%); border: 1.5px solid rgba(66, 153, 225, 0.2); display: flex; align-items: center; justify-content: center; transition: all 0.3s ease; box-shadow: 0 2px 8px rgba(66, 153, 225, 0.15); }
.contact-section-v13 { flex: 0 0 auto; display: flex; align-items: center; gap: 24px; margin-left: 60px; }
```

2. **Replace `<header>` in body:**
Copy HTML from `header-preview-v35.html` lines 292-349

---

## 📞 Support

If issues persist after following this guide:

1. Check browser DevTools → Elements tab
2. Inspect `.new-header` computed styles
3. Look for overriding CSS rules (strikethrough in DevTools)
4. Check JavaScript console for errors
5. Compare with `header-preview-v35.html` directly

**Common Issues:**
- Cache not cleared → Hard refresh (Cmd+Shift+R / Ctrl+Shift+R)
- Wrong file version → Ensure you're editing the correct file
- CSS load order → V35 CSS should load after other stylesheets
- JavaScript conflicts → Check console for errors

---

## 📚 Additional Resources

- **Preview File:** `header-preview-v35.html` - Working standalone example
- **Design System:** `V33_DESIGN_SYSTEM_DOCUMENTATION.md` - Complete design specs
- **Original Code:** `homepage-v34.html` - Full page implementation

---

**Last Updated:** 2026-01-29
**Version:** 35
**Status:** ✅ Production Ready
