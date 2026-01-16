# Website Redesign Implementation Guide

## 🎯 OVERVIEW

This guide provides step-by-step instructions to implement the glassmorphism redesign on your WordPress website using Elementor Pro.

---

## 📋 PREREQUISITE CHECKLIST

Before starting, ensure you have:

- [ ] WordPress site with Elementor Pro installed
- [ ] Access to upload custom CSS
- [ ] Background image (glass building) ready
- [ ] Google Fonts API key (if needed)
- [ ] Font Awesome icons library v6. 4.0+

---

## 🔧 STEP 1: ADD GOOGLE FONTS (INTER)

### In WordPress: 

1. Go to: **Appearance** → **Customize**
2. Look for:  **Additional CSS** or **Custom CSS**
3. Add this code:

```css
@import url('https://fonts.googleapis.com/css2?family=Inter: wght@400;500;600;700&display=swap');
```

Alternative: Use Elementor's Google Fonts integration: 
1. Open any Elementor page
2. Go to: **Settings** (bottom left gear icon)
3. **Fonts**:  Search for "Inter"
4. Click **Load** next to Inter font
5. Select weights: 400, 500, 600, 700

---

## 🔧 STEP 2: UPLOAD BACKGROUND IMAGE

### For the Glassmorphism Effect:

1. Go to: **WordPress Dashboard** → **Media** → **Add New**
2. Upload your glass building image (recommended size: 2560x1440px)
3. Copy the image URL
4. In your CSS, replace: 
   ```
   background-image: url('path-to-glass-building-image. jpg');
   ```
   With:
   ```
   background-image: url('YOUR_IMAGE_URL_HERE');
   ```

---

## 🔧 STEP 3: ADD CUSTOM CSS TO WORDPRESS

### Option A: Via Elementor (Recommended)

1. Edit your Konfigurator page with Elementor
2. Click **Page Settings** (bottom left gear icon)
3. Go to:  **Advanced** tab
4. Scroll to: **Custom CSS**
5. Paste the entire CSS from `WEBSITE_REDESIGN_CSS.css`
6. Click **Update**

### Option B: Via WordPress Customizer

1. Go to: **Appearance** → **Customize**
2. Click:  **Additional CSS**
3. Paste the CSS code
4. Click: **Publish**

### Option C: Via Child Theme functions.php

Add to your child theme's `functions.php`:

```php
function enqueue_redesign_css() {
    wp_enqueue_style(
        'glassmorphism-redesign',
        get_stylesheet_directory_uri() . '/css/glassmorphism-redesign.css'
    );
}
add_action('wp_enqueue_scripts', 'enqueue_redesign_css');
```

---

## 🎨 STEP 4: UPDATE KONFIGURATOR LAYOUT IN ELEMENTOR

### Step A: Create Left Menu Toggle Button

1. Edit your Konfigurator page with Elementor
2. Add a new **Button** element on the left side
3. Set properties:
   - **Text**: (empty - we'll use icon)
   - **Icon**: **Hamburger menu** (☰)
   - **Classes**: `menu-toggle-left`
   - **Position**: Fixed (via Custom CSS)

**Custom CSS for the button:**
```css
.menu-toggle-left {
    position: fixed ! important;
    left: 24px !important;
    top:  50% !important;
    transform: translateY(-50%) !important;
}
```

### Step B: Create Left Menu Panel

1. Add a new **Section** element
2. Set **Classes**: `konfigurator-steps-menu`
3. Add text showing all configuration steps: 
   ```
   Schritt 1: Größe
   Schritt 2: Typ
   Schritt 3: Farbe
   ... 
   ```
4. Each step in its own **Text** element with **Classes**: `step-item`

### Step C: Create Right Menu Toggle Button

1. Add another **Button** element on the right side
2. Set properties:
   - **Text**: (empty)
   - **Icon**: **List menu** (≡) or **Bars**
   - **Classes**: `menu-toggle-right`

**Custom CSS:**
```css
.menu-toggle-right {
    position: fixed !important;
    right: 24px !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
}
```

### Step D: Create Right Summary Panel

1. Add a new **Section** element
2. Set **Classes**: `konfigurator-summary-menu`
3. Add content:
   - Title: "Zusammenfassung" (Summary)
   - Selected options list
   - Running price total

---

## 🎨 STEP 5: UPDATE CONFIGURATION OPTIONS

All clickable option boxes must use: 

**Classes**: `config-option`

**Structure in Elementor:**
- Add **Image** or **Icon Box** element
- Set **Classes**: `config-option`
- Add icon from glassmorphism icons (Font Awesome)
- Add label text
- Add price

---

## 🎨 STEP 6: UPDATE BUTTONS

All buttons must use the glassmorphism style:

**Classes to add**:  `btn` or `glass-container`

**Remove old classes:**
- Remove:  `btn-red`
- Remove: `btn-yellow`
- Remove any inline styles with old colors

---

## 🎨 STEP 7: COLOR UPDATES

### Search and Replace in Elementor:

1. **Brand Red** (#E10B17) → **Glass Clear** (#E7F2E6)
   - Find all red elements
   - Change background to glass clear

2. **Accent Yellow** (#FFC107) → **Glass Iron** (#E1F4F2)
   - Find all yellow elements
   - Change background to glass iron

### In Elementor: 
- Open each widget
- Go to **Style** tab
- Change background colors
- Change text colors to #212529

---

## 🎨 STEP 8: TYPOGRAPHY UPDATES

### Change all fonts to Inter:

1. Select all text elements in Elementor
2. In **Style** tab → **Typography**
3. Set **Family**: Inter
4. Set **Weight**: 
   - Headers: 700 (Bold)
   - Body text: 400 (Regular)
   - Buttons: 600 (Semi-Bold)

### Font Sizes:
- **H1/Main Title**: 2. 5rem (40px)
- **H2/Sections**: 1.25rem (20px)
- **Body/Button**: 1rem (16px)

---

## 🎨 STEP 9: SPACING & LAYOUT

Apply consistent spacing using these values:

- **XS**: 4px
- **SM**: 8px
- **MD**: 16px
- **LG**: 24px
- **XL**: 32px
- **XXL**: 48px

In Elementor, for each element:
1. Go to **Advanced** tab
2. **Spacing**:
   - **Padding**: Use MD or LG
   - **Margin**: Use MD or LG

---

## 🎨 STEP 10: MOBILE RESPONSIVENESS

Elementor handles responsive design.  For each section:

1. Click the **responsive icon** (phone/tablet/desktop icons)
2. For **Tablet** view (768px):
   - Adjust spacing to SM/MD
   - Change grid columns if needed
3. For **Mobile** view (480px):
   - Change grid to single column
   - Reduce padding to SM
   - Stack navigation vertically

---

## 🔌 STEP 11: ADD JAVASCRIPT FOR MENU TOGGLE

Add to your page via **Elementor** → **Page Settings** → **Custom Code**:

```javascript
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Left Menu Toggle
    const leftMenuBtn = document.querySelector('.menu-toggle-left');
    const leftMenu = document.querySelector('.konfigurator-steps-menu');
    
    if (leftMenuBtn && leftMenu) {
        leftMenuBtn.addEventListener('click', function() {
            leftMenu.classList.toggle('active');
        });
    }
    
    // Right Menu Toggle
    const rightMenuBtn = document.querySelector('.menu-toggle-right');
    const rightMenu = document.querySelector('.konfigurator-summary-menu');
    
    if (rightMenuBtn && rightMenu) {
        rightMenuBtn.addEventListener('click', function() {
            rightMenu.classList.toggle('active');
        });
    }
    
    // Close menus when clicking outside
    document. addEventListener('click', function(event) {
        if (leftMenu && !leftMenu.contains(event.target) && !leftMenuBtn.contains(event.target)) {
            leftMenu.classList.remove('active');
        }
        if (rightMenu && ! rightMenu.contains(event.target) && !rightMenuBtn.contains(event.target)) {
            rightMenu.classList.remove('active');
        }
    });
});
</script>
```

---

## ✅ TESTING CHECKLIST

- [ ] Colors changed (no more red #E10B17 or yellow #FFC107)
- [ ] Fonts changed to Inter (all text)
- [ ] Glassmorphism effect visible (blur background)
- [ ] Left menu toggle works
- [ ] Right menu toggle works
- [ ] All buttons have glass effect
- [ ] Responsive on mobile (test in DevTools)
- [ ] Responsive on tablet (768px)
- [ ] Responsive on desktop (1920px)
- [ ] No old styling visible
- [ ] Icons are glassmorphism style
- [ ] Background image shows through blur effect

---

## 🆘 TROUBLESHOOTING

### Issue: Colors not changing
**Solution**: Check CSS specificity. Add `!important` to override inline styles.

### Issue: Blur effect not showing
**Solution**:  Ensure background-attachment:  fixed is applied.  Check browser support for backdrop-filter.

### Issue: Menus not toggling
**Solution**:  Check JavaScript console for errors. Ensure class names match CSS.

### Issue: Font not loading
**Solution**: Check Google Fonts import. Clear browser cache.  Try system fonts temporarily.

### Issue: Mobile layout broken
**Solution**: Check responsive breakpoints in CSS. Use Elementor's responsive tools.

---

## 📱 BROWSER COMPATIBILITY

| Browser | Glassmorphism | Support |
|---------|---------------|---------|
| Chrome | ✅ Full | backdrop-filter supported |
| Firefox | ✅ Full | backdrop-filter supported |
| Safari | ✅ Full | -webkit prefix required |
| Edge | ✅ Full | backdrop-filter supported |
| Mobile Safari | ✅ Full | -webkit prefix required |
| Chrome Mobile | ✅ Full | backdrop-filter supported |

---

## 🚀 DEPLOYMENT

1. **Test on staging** first
2. **Test all browsers** (Chrome, Safari, Firefox)
3. **Test all devices** (Mobile, Tablet, Desktop)
4. **Get approval** before pushing to live
5. **Deploy to production**
6. **Monitor for issues** 24 hours

---

**Status**: Ready for Implementation  
**Last Updated**: 2026-01-16
