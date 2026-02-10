# V33 Design System Documentation

**Complete Reference Guide for FenTuRo Homepage Redesign**

---

## 📋 Table of Contents

1. [Typography System](#typography-system)
2. [Glassmorphism Effects](#glassmorphism-effects)
3. [Shimmer Animation](#shimmer-animation)
4. [Hover Effects](#hover-effects)
5. [Color Scheme](#color-scheme)
6. [Responsive Breakpoints](#responsive-breakpoints)
7. [Complete Code Reference](#complete-code-reference)

---

## 🔤 Typography System

### **Font Family**

**Primary Font:**
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

**Note:** This system font stack approximates **Berlin Sans FB Demi Bold** while ensuring cross-platform compatibility.

---

### **Font Weight**

**Standard Weight for Headers:**
```css
font-weight: 600; /* Semi-bold */
```

**Usage:**
- Configurator heading
- Manufacturers heading
- All primary headers

**Subheader Weight:**
```css
font-weight: 400; /* Normal/Regular */
```

---

### **Font Sizes**

#### **Headers (Configurator & Manufacturers)**

**Desktop (default):**
```css
font-size: 16px;
```

**Tablet (≤768px):**
```css
font-size: 15px;
```

**Mobile (≤480px):**
```css
font-size: 13px;
```

#### **Subheader (Manufacturers)**

**Desktop (default):**
```css
font-size: 13px;
```

**Tablet (≤768px):**
```css
font-size: 11px;
```

**Mobile (≤480px):**
```css
font-size: 10px;
```

---

### **Line Height**

**Standard Line Height:**
```css
line-height: 1.1;
```

**Subheader Line Height:**
```css
line-height: 1.3;
```

---

### **Letter Spacing**

**Standard Letter Spacing:**
```css
letter-spacing: -0.3px;
```

**Usage:** Applied to all headers for a modern, condensed look.

---

### **Complete Typography CSS**

```css
/* Headers (Configurator & Manufacturers) */
.v32-configurator-heading h2,
div.v32-manufacturers-heading h2 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 16px;
    font-weight: 600;
    line-height: 1.1;
    letter-spacing: -0.3px;
    color: #1a202c;
    text-align: center;
}

/* Tablet */
@media (max-width: 768px) {
    .v32-configurator-heading h2,
    div.v32-manufacturers-heading h2 {
        font-size: 15px;
    }
}

/* Mobile */
@media (max-width: 480px) {
    .v32-configurator-heading h2,
    div.v32-manufacturers-heading h2 {
        font-size: 13px;
    }
}

/* Subheader */
div.v32-manufacturers-heading p {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 13px;
    font-weight: 400;
    line-height: 1.3;
    letter-spacing: -0.3px;
    color: #2d3748;
    text-align: center;
}

/* Tablet */
@media (max-width: 768px) {
    div.v32-manufacturers-heading p {
        font-size: 11px;
    }
}

/* Mobile */
@media (max-width: 480px) {
    div.v32-manufacturers-heading p {
        font-size: 10px;
    }
}
```

---

## 🌟 Glassmorphism Effects

### **Core Glassmorphism Properties**

**Background Transparency:**
```css
background: rgba(255, 255, 255, 0); /* 100% transparent */
```

**Backdrop Filter (Blur Effect):**
```css
backdrop-filter: blur(1px) saturate(180%);
-webkit-backdrop-filter: blur(1px) saturate(180%);
```

**Border:**
```css
border: 1.5px solid rgba(255, 255, 255, 0.2);
```

**Border Radius:**
```css
border-radius: 20px; /* Heading cards */
border-radius: 16px; /* Configurator step cards */
```

**Box Shadow:**
```css
box-shadow: 
    0 8px 32px 0 rgba(31, 38, 135, 0.15),
    inset 0 1px 0 0 rgba(255, 255, 255, 0.2);
```

---

### **Complete Glassmorphism CSS**

```css
/* Glassmorphism Container */
.v32-configurator-heading,
.v32-manufacturers-heading {
    background: rgba(255, 255, 255, 0);
    backdrop-filter: blur(1px) saturate(180%);
    -webkit-backdrop-filter: blur(1px) saturate(180%);
    border: 1.5px solid rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    box-shadow: 
        0 8px 32px 0 rgba(31, 38, 135, 0.15),
        inset 0 1px 0 0 rgba(255, 255, 255, 0.2);
    padding: 20px 30px;
    position: relative;
    overflow: hidden;
}

/* Configurator Step Cards */
.v32-step-card {
    background: rgba(255, 255, 255, 0);
    backdrop-filter: blur(1px) saturate(180%);
    -webkit-backdrop-filter: blur(1px) saturate(180%);
    border: 1.5px solid rgba(255, 255, 255, 0.2);
    border-radius: 16px;
    box-shadow: 
        0 8px 32px 0 rgba(31, 38, 135, 0.15),
        inset 0 1px 0 0 rgba(255, 255, 255, 0.2);
}
```

---

## ✨ Shimmer Animation

### **Shimmer Properties**

**Animation Duration:**
```css
animation: v32-shimmer 20s infinite;
```

**Shimmer Color:**
```css
background: linear-gradient(
    90deg,
    transparent,
    rgba(66, 153, 225, 0.15),  /* Light blue, 15% opacity */
    transparent
);
```

**Backdrop Filter:**
```css
backdrop-filter: blur(1px) saturate(180%);
-webkit-backdrop-filter: blur(1px) saturate(180%);
```

---

### **Complete Shimmer Animation Code**

```css
/* Shimmer Pseudo-element */
.v32-configurator-heading::before,
.v32-manufacturers-heading::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(66, 153, 225, 0.15),
        transparent
    );
    backdrop-filter: blur(1px) saturate(180%);
    -webkit-backdrop-filter: blur(1px) saturate(180%);
    animation: v32-config-shimmer 20s infinite;
    z-index: 1;
}

/* Shimmer Keyframes */
@keyframes v32-config-shimmer {
    0% {
        left: -100%;
    }
    100% {
        left: 100%;
    }
}

/* Alternative name for manufacturers */
@keyframes v32-mfr-shimmer {
    0% {
        left: -100%;
    }
    100% {
        left: 100%;
    }
}
```

**Key Parameters:**
- **Duration:** 20 seconds (calm, elegant)
- **Pattern:** Continuous sweep from left to right (0% to 100%)
- **Color:** `rgba(66, 153, 225, 0.15)` (light blue, 15% opacity)
- **Blur:** 1px backdrop-filter

---

## 🎯 Hover Effects

### **Configurator Step Cards Hover**

#### **Scale Transformation**
```css
transform: scale(1.5) translateY(-4px);
```

#### **Z-Index (Bring to Front)**
```css
z-index: 10;
```

#### **Enhanced Backdrop Filter**
```css
backdrop-filter: blur(1.5px) saturate(200%);
-webkit-backdrop-filter: blur(1.5px) saturate(200%);
```

#### **Enhanced Box Shadow**
```css
box-shadow: 
    0 12px 48px 0 rgba(31, 38, 135, 0.25),
    inset 0 0 30px rgba(255, 255, 255, 0.08);
```

#### **Other Cards Blur Effect**
```css
/* When one card is hovered, blur others */
.v32-steps-grid:has(.v32-step-card:hover) .v32-step-card:not(:hover) {
    filter: blur(0.5px);
    opacity: 0.85;
}
```

---

### **Complete Hover Effects CSS**

```css
/* Step Card Base State */
.v32-step-card {
    background: rgba(255, 255, 255, 0);
    backdrop-filter: blur(1px) saturate(180%);
    -webkit-backdrop-filter: blur(1px) saturate(180%);
    border: 1.5px solid rgba(255, 255, 255, 0.2);
    border-radius: 16px;
    height: 178px;
    min-height: 178px;
    max-height: 178px;
    padding: 18px;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 
        0 8px 32px 0 rgba(31, 38, 135, 0.15),
        inset 0 1px 0 0 rgba(255, 255, 255, 0.2);
}

/* Hover State */
.v32-step-card:hover {
    transform: scale(1.5) translateY(-4px);
    z-index: 10;
    backdrop-filter: blur(1.5px) saturate(200%);
    -webkit-backdrop-filter: blur(1.5px) saturate(200%);
    box-shadow: 
        0 12px 48px 0 rgba(31, 38, 135, 0.25),
        inset 0 0 30px rgba(255, 255, 255, 0.08);
}

/* Blur Other Cards When One is Hovered */
.v32-steps-grid:has(.v32-step-card:hover) .v32-step-card:not(:hover) {
    filter: blur(0.5px);
    opacity: 0.85;
}

/* Icon Hover Effect */
.v32-step-card .step-icon {
    opacity: 0.4;
    transition: opacity 0.3s ease;
}

.v32-step-card:hover .step-icon {
    opacity: 0.75;
}

/* Image Brightness on Hover */
.v32-step-card img {
    filter: brightness(1.0);
    transition: filter 0.3s ease;
}

.v32-step-card:hover img {
    filter: brightness(1.1);
}
```

---

## 🎨 Color Scheme

### **Primary Colors**

**Text Colors:**
```css
/* Primary Header Text */
color: #1a202c; /* Dark gray/black */

/* Subheader Text */
color: #2d3748; /* Medium gray */
```

**Blue Accent:**
```css
/* Shimmer, highlights, focus */
rgba(66, 153, 225, 0.15); /* Light blue, 15% opacity */
rgba(66, 153, 225, 0.3);  /* Light blue, 30% opacity (borders) */
rgba(66, 153, 225, 0.5);  /* Light blue, 50% opacity (hover) */
```

**Border Colors:**
```css
/* Glassmorphism borders */
rgba(255, 255, 255, 0.2);  /* 20% white opacity */

/* Hover border */
rgba(66, 153, 225, 0.5);   /* 50% blue opacity */
```

**Shadow Colors:**
```css
/* Box shadows */
rgba(31, 38, 135, 0.15);   /* Primary shadow, 15% opacity */
rgba(31, 38, 135, 0.25);   /* Hover shadow, 25% opacity */

/* Inset highlights */
rgba(255, 255, 255, 0.2);  /* Subtle white highlight */
rgba(255, 255, 255, 0.08); /* Very subtle white highlight */
```

---

### **Complete Color Palette**

```css
:root {
    /* Text Colors */
    --color-text-primary: #1a202c;
    --color-text-secondary: #2d3748;
    
    /* Blue Accent (various opacities) */
    --color-blue-15: rgba(66, 153, 225, 0.15);
    --color-blue-30: rgba(66, 153, 225, 0.3);
    --color-blue-50: rgba(66, 153, 225, 0.5);
    
    /* Borders */
    --color-border-glass: rgba(255, 255, 255, 0.2);
    --color-border-hover: rgba(66, 153, 225, 0.5);
    
    /* Shadows */
    --color-shadow-primary: rgba(31, 38, 135, 0.15);
    --color-shadow-hover: rgba(31, 38, 135, 0.25);
    --color-highlight-subtle: rgba(255, 255, 255, 0.2);
    --color-highlight-very-subtle: rgba(255, 255, 255, 0.08);
    
    /* Background */
    --color-background-transparent: rgba(255, 255, 255, 0);
}
```

---

## 📱 Responsive Breakpoints

### **Breakpoint Definitions**

```css
/* Desktop (default) */
/* No media query needed - base styles */

/* Tablet */
@media (max-width: 768px) {
    /* Styles for tablets and below */
}

/* Mobile */
@media (max-width: 480px) {
    /* Styles for mobile devices */
}
```

---

### **Responsive Font Sizes Summary**

| Element | Desktop | Tablet (≤768px) | Mobile (≤480px) |
|---------|---------|-----------------|-----------------|
| **Headers** | 16px | 15px | 13px |
| **Subheader** | 13px | 11px | 10px |

---

### **Responsive Padding**

**Heading Cards:**
```css
/* Desktop */
padding: 20px 30px;

/* Tablet */
@media (max-width: 768px) {
    padding: 16px 20px;
}

/* Mobile */
@media (max-width: 480px) {
    padding: 14px 16px;
}
```

**Configurator Steps:**
```css
/* Desktop */
padding: 18px;

/* Tablet */
@media (max-width: 768px) {
    padding: 16px;
}

/* Mobile */
@media (max-width: 480px) {
    padding: 14px;
}
```

---

## 📝 Complete Code Reference

### **Full Configurator Heading CSS**

```css
/* Configurator Heading Container */
.v32-configurator-heading {
    background: rgba(255, 255, 255, 0);
    backdrop-filter: blur(1px) saturate(180%);
    -webkit-backdrop-filter: blur(1px) saturate(180%);
    border: 1.5px solid rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    box-shadow: 
        0 8px 32px 0 rgba(31, 38, 135, 0.15),
        inset 0 1px 0 0 rgba(255, 255, 255, 0.2);
    padding: 20px 30px;
    margin-bottom: 40px;
    position: relative;
    overflow: hidden;
    text-align: center;
}

/* Shimmer Effect */
.v32-configurator-heading::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(66, 153, 225, 0.15),
        transparent
    );
    backdrop-filter: blur(1px) saturate(180%);
    -webkit-backdrop-filter: blur(1px) saturate(180%);
    animation: v32-config-shimmer 20s infinite;
    z-index: 1;
}

@keyframes v32-config-shimmer {
    0% { left: -100%; }
    100% { left: 100%; }
}

/* Heading Text */
.v32-configurator-heading h2 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 16px;
    font-weight: 600;
    line-height: 1.1;
    letter-spacing: -0.3px;
    color: #1a202c;
    margin: 0;
    position: relative;
    z-index: 2;
}

/* Responsive */
@media (max-width: 768px) {
    .v32-configurator-heading {
        padding: 16px 20px;
        margin-bottom: 30px;
    }
    
    .v32-configurator-heading h2 {
        font-size: 15px;
    }
}

@media (max-width: 480px) {
    .v32-configurator-heading {
        padding: 14px 16px;
        margin-bottom: 24px;
    }
    
    .v32-configurator-heading h2 {
        font-size: 13px;
    }
}
```

---

### **Full Manufacturers Heading CSS**

```css
/* Manufacturers Heading Container */
.v32-manufacturers-heading {
    background: rgba(255, 255, 255, 0);
    backdrop-filter: blur(1px) saturate(180%);
    -webkit-backdrop-filter: blur(1px) saturate(180%);
    border: 1.5px solid rgba(255, 255, 255, 0.2);
    border-radius: 20px;
    box-shadow: 
        0 8px 32px 0 rgba(31, 38, 135, 0.15),
        inset 0 1px 0 0 rgba(255, 255, 255, 0.2);
    padding: 20px 30px;
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
    text-align: center;
}

/* Shimmer Effect */
.v32-manufacturers-heading::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(66, 153, 225, 0.15),
        transparent
    );
    backdrop-filter: blur(1px) saturate(180%);
    -webkit-backdrop-filter: blur(1px) saturate(180%);
    animation: v32-mfr-shimmer 20s infinite;
    z-index: 1;
}

@keyframes v32-mfr-shimmer {
    0% { left: -100%; }
    100% { left: 100%; }
}

/* Heading Text */
div.v32-manufacturers-heading h2 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 16px;
    font-weight: 600;
    line-height: 1.1;
    letter-spacing: -0.3px;
    color: #1a202c;
    margin: 0 0 6px 0;
    position: relative;
    z-index: 2;
}

/* Subheading Text */
div.v32-manufacturers-heading p {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 13px;
    font-weight: 400;
    line-height: 1.3;
    letter-spacing: -0.3px;
    color: #2d3748;
    margin: 0;
    position: relative;
    z-index: 2;
}

/* Responsive */
@media (max-width: 768px) {
    .v32-manufacturers-heading {
        padding: 16px 20px;
        margin-bottom: 24px;
    }
    
    div.v32-manufacturers-heading h2 {
        font-size: 15px;
    }
    
    div.v32-manufacturers-heading p {
        font-size: 11px;
    }
}

@media (max-width: 480px) {
    .v32-manufacturers-heading {
        padding: 14px 16px;
        margin-bottom: 20px;
    }
    
    div.v32-manufacturers-heading h2 {
        font-size: 13px;
    }
    
    div.v32-manufacturers-heading p {
        font-size: 10px;
    }
}
```

---

### **Full Configurator Step Cards CSS**

```css
/* Steps Grid Container */
.v32-steps-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 24px;
    margin-bottom: 60px;
}

/* Individual Step Card */
.v32-step-card {
    background: rgba(255, 255, 255, 0);
    backdrop-filter: blur(1px) saturate(180%);
    -webkit-backdrop-filter: blur(1px) saturate(180%);
    border: 1.5px solid rgba(255, 255, 255, 0.2);
    border-radius: 16px;
    box-shadow: 
        0 8px 32px 0 rgba(31, 38, 135, 0.15),
        inset 0 1px 0 0 rgba(255, 255, 255, 0.2);
    height: 178px;
    min-height: 178px;
    max-height: 178px;
    padding: 18px;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Hover Effect */
.v32-step-card:hover {
    transform: scale(1.5) translateY(-4px);
    z-index: 10;
    backdrop-filter: blur(1.5px) saturate(200%);
    -webkit-backdrop-filter: blur(1.5px) saturate(200%);
    box-shadow: 
        0 12px 48px 0 rgba(31, 38, 135, 0.25),
        inset 0 0 30px rgba(255, 255, 255, 0.08);
}

/* Blur Other Cards */
.v32-steps-grid:has(.v32-step-card:hover) .v32-step-card:not(:hover) {
    filter: blur(0.5px);
    opacity: 0.85;
}

/* Step Icon */
.v32-step-card .step-icon {
    position: absolute;
    bottom: 5px;
    right: 12px;
    opacity: 0.4;
    transition: opacity 0.3s ease;
}

.v32-step-card:hover .step-icon {
    opacity: 0.75;
}

/* Responsive - Tablet */
@media (max-width: 1400px) {
    .v32-steps-grid {
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
    }
}

/* Responsive - Mobile */
@media (max-width: 768px) {
    .v32-steps-grid {
        grid-template-columns: 1fr;
        gap: 16px;
    }
    
    .v32-step-card {
        height: 168px;
        min-height: 168px;
        max-height: 168px;
        padding: 16px;
    }
}
```

---

## 🎯 Usage Guidelines

### **When to Use This Design System**

1. **All Homepage Headings:** Use the typography system for consistent sizing and spacing
2. **Feature Sections:** Apply glassmorphism effects for modern, elegant appearance
3. **Interactive Elements:** Use hover effects for enhanced user experience
4. **New Components:** Follow the color scheme and spacing guidelines

### **Consistency Rules**

1. **Always use:**
   - Font-weight: 600 for headers
   - Font-weight: 400 for body text
   - Line-height: 1.1 for headers
   - Letter-spacing: -0.3px for all text

2. **Glassmorphism standards:**
   - Background: `rgba(255, 255, 255, 0)` (100% transparent)
   - Backdrop-filter: `blur(1px) saturate(180%)`
   - Border: `1.5px solid rgba(255, 255, 255, 0.2)`

3. **Animation timing:**
   - Shimmer: 20s (calm, elegant)
   - Hover transitions: 0.4s cubic-bezier(0.4, 0, 0.2, 1)

---

## 📌 Quick Reference Table

| Property | Value | Usage |
|----------|-------|-------|
| **Font Weight (Headers)** | 600 | All headers |
| **Font Weight (Body)** | 400 | Subheaders, body text |
| **Line Height (Headers)** | 1.1 | Compact spacing |
| **Letter Spacing** | -0.3px | Modern, condensed |
| **Header Font Size** | 16px | Desktop |
| **Subheader Font Size** | 13px | Desktop |
| **Background** | rgba(255, 255, 255, 0) | 100% transparent |
| **Backdrop Blur** | 1px | Subtle glassmorphism |
| **Border** | 1.5px solid rgba(255, 255, 255, 0.2) | Glass edge |
| **Border Radius** | 20px (headings), 16px (cards) | Rounded corners |
| **Shimmer Duration** | 20s | Calm animation |
| **Shimmer Color** | rgba(66, 153, 225, 0.15) | Light blue, 15% |
| **Hover Scale** | 1.5 | Configurator cards |
| **Hover Blur** | blur(1.5px) | Enhanced on hover |

---

## 🔄 Version History

**V33 - Current Version**
- Headers: 16px (desktop)
- Subheader: 13px (desktop)
- Font-weight: 600 (headers), 400 (body)
- Line-height: 1.1
- Letter-spacing: -0.3px
- Shimmer: 20s duration, continuous sweep
- Glassmorphism: 100% transparent, 1px blur
- Hover: 1.5x scale with blur effects

---

## 📄 File Location

This design system is implemented in:
- **File:** `homepage-v33.html`
- **Section:** Lines 2620-3050 (approximate)
- **Components:** Configurator heading, Manufacturers heading, Step cards

---

## ✅ Implementation Checklist

When applying this design system to new components:

- [ ] Use system font stack (Berlin Sans approximation)
- [ ] Apply font-weight: 600 for headers
- [ ] Apply font-weight: 400 for body text
- [ ] Set line-height: 1.1 for headers
- [ ] Set letter-spacing: -0.3px
- [ ] Use 100% transparent background
- [ ] Apply backdrop-filter: blur(1px) saturate(180%)
- [ ] Add 1.5px border with 20% white opacity
- [ ] Include shimmer animation (20s duration)
- [ ] Add hover effects (1.5x scale, enhanced blur)
- [ ] Test responsive breakpoints (768px, 480px)
- [ ] Verify color scheme consistency
- [ ] Check animation performance

---

**End of Documentation**

*Last Updated: 2026-01-28*
*Version: V33*
*Maintained by: FenTuRo Development Team*
