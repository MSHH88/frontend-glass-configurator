# V32 Configurator Steps Section Redesign - Integration Plan

## 📋 **OVERVIEW**

**Objective:** Complete redesign of the 4-step configurator explanation section with glassmorphism effects, iOS-style design, modern German text, and interactive hover animations

**Section Location:** Homepage, after "Fenster nach Maß konfigurieren" heading

**Current State:** 4 plain boxes with red/white theme, basic text, no special effects

**Target State:** 4 glassmorphism cards with light blue accents, Berlin Sans font, sophisticated German text, iOS-style borders, and 1.5x zoom hover effect with blur

---

## 🎯 **THREE-PHASE IMPLEMENTATION PLAN**

### **PHASE 1: CONTENT MODERNIZATION (Text Rewrite)**
### **PHASE 2: VISUAL REDESIGN (Colors, Fonts, Glassmorphism)**  
### **PHASE 3: INTERACTION EFFECTS (Hover Animations)**

---

## 📝 **PHASE 1: CONTENT MODERNIZATION**

### **Current Text Analysis:**

**Step 1: Profil festlegen**
- Old: "Wählen Sie zuerst Material, den Hersteller und das Profil aus. Entscheiden Sie sich dann für eine Fensterart, den Typ und Öffnungsrichtung."
- Issues: Somewhat dry, formal, multiple sentences
- Meaning: Choose material, manufacturer, profile, window type, and opening direction

**Step 2: Maße wählen**
- Old: "Nun können Sie Ihre gewünschten Maße eingeben, die Dichtungen, den Kern und den Rahmen ganz individuell anpassen."
- Issues: Long sentence, technical jargon
- Meaning: Enter dimensions and customize seals, core, and frame

**Step 3: Farbe aussuchen**
- Old: "Je nach Material und Fensterhersteller können die Farbpaletten und Gestaltungsoptionen vielfältige Möglichkeiten bereithalten."
- Issues: Overly complex sentence structure, passive voice
- Meaning: Choose from various color palettes based on material

**Step 4: Glas auswählen**
- Old: "Im vierten Schritt geht es zur Verglasung der Fenster. Extra Schallschutz oder sogar..."
- Issues: Incomplete in snippet, formal structure
- Meaning: Select glass type with options for sound insulation

---

### **NEW MODERNIZED TEXT (Sophisticated German)**

**Step 1: Profil festlegen**
```
Bestimmen Sie Material, Hersteller und Profiltyp Ihres Wunschfensters. 
Legen Sie anschließend Fensterart und Öffnungsmechanik fest.
```
- More direct, modern verb usage
- Flows better, easier to understand
- Professional but accessible tone

**Step 2: Maße wählen**
```
Geben Sie Ihre individuellen Maße ein und passen Sie Details wie 
Dichtungen, Kern und Rahmen präzise an Ihre Anforderungen an.
```
- Clearer structure, active voice
- Emphasizes customization
- More sophisticated language flow

**Step 3: Farbe aussuchen**
```
Entdecken Sie vielfältige Farbpaletten und Gestaltungsmöglichkeiten, 
die je nach Material und Hersteller zur Verfügung stehen.
```
- More engaging verb ("Entdecken Sie")
- Clearer relationship between parts
- Modern, elegant phrasing

**Step 4: Glas auswählen**
```
Wählen Sie die passende Verglasung für Ihre Anforderungen – 
von erhöhtem Schallschutz bis zu speziellen Sicherheitsgläsern.
```
- Clear, direct communication
- Shows range of options
- Professional yet accessible

---

## 🎨 **PHASE 2: VISUAL REDESIGN**

### **Color Scheme Changes:**

**REMOVE (No More Red):**
- ❌ Red accents in numbers
- ❌ Red highlights
- ❌ Any warm red tones

**IMPLEMENT (Light Blue #6690CC):**
- ✅ Numbers: Grey (#6c757d or #555555) - **NOT light blue**
- ✅ First word (Profil, Maße, Farbe, Glas): **Light blue #6690CC**
- ✅ iOS border: Light blue (#6690CC) with 0.4mm thickness, slightly glowing fade around edge
- ✅ Hover state: Light blue glow intensifies

**Background:**
- Base: Glassmorphism (semi-transparent, frosted glass effect)
- Backdrop-filter: blur(10px)
- Background: rgba(255, 255, 255, 0.15) or rgba(230, 240, 255, 0.2) for slight blue tint
- Border: 1px solid rgba(102, 144, 204, 0.3) with glow effect

---

### **Typography Changes:**

**Font Family:**
```css
font-family: 'Berlin Sans FB Demi', 'Berlin Sans FB', Arial, 'Helvetica Neue', sans-serif;
```

**Text Hierarchy:**
- **Heading (1. Profil festlegen):**
  - Font-weight: 600 (Demi Bold)
  - First word color: #6690CC (light blue)
  - Rest of heading: #333333 (dark grey)
  - Size: ~20px (1.25rem)

- **Body Text:**
  - Font-weight: 400 (Regular)
  - Color: #6c757d (grey)
  - Size: ~14px (0.875rem)
  - Line-height: 1.6

---

### **Glassmorphism Implementation:**

```css
.config-step-card-v32 {
    /* Glassmorphism base */
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    
    /* iOS-style border with glow */
    border: 1px solid rgba(102, 144, 204, 0.3);
    box-shadow: 
        0 8px 32px 0 rgba(102, 144, 204, 0.15),
        inset 0 0 0 1px rgba(255, 255, 255, 0.2),
        0 0 0 0.4mm rgba(102, 144, 204, 0.4); /* 0.4mm glowing edge */
    
    /* Smooth corners */
    border-radius: 16px;
    
    /* Padding */
    padding: 2rem 1.5rem;
    
    /* Transition for hover */
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
```

**iOS-Style Border Glow:**
```css
.config-step-card-v32::before {
    content: '';
    position: absolute;
    top: -1px;
    left: -1px;
    right: -1px;
    bottom: -1px;
    background: linear-gradient(
        135deg,
        rgba(102, 144, 204, 0.5) 0%,
        rgba(102, 144, 204, 0.2) 50%,
        rgba(102, 144, 204, 0.5) 100%
    );
    border-radius: 16px;
    opacity: 0.5;
    z-index: -1;
    filter: blur(0.4mm); /* Soft glowing edge */
}
```

---

## 🎬 **PHASE 3: INTERACTION EFFECTS**

### **Hover Effect Specification:**

**Requirements:**
1. Hovered card grows to **1.5x size** (scale: 1.5)
2. Background remains **glassmorphism clear**
3. Card grows **over/on top of** adjacent cards (z-index increase)
4. Content **behind the expanded card** becomes **blurred**
5. Smooth animation with easing
6. Other cards remain at normal size

---

### **Implementation Strategy:**

```css
.config-step-card-v32 {
    position: relative;
    transform-origin: center center;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    z-index: 1;
}

.config-step-card-v32:hover {
    /* Scale up to 1.5x */
    transform: scale(1.5);
    z-index: 10; /* Bring to front */
    
    /* Intensify glassmorphism */
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    
    /* Enhance border glow */
    box-shadow: 
        0 12px 48px 0 rgba(102, 144, 204, 0.3),
        inset 0 0 0 1px rgba(255, 255, 255, 0.3),
        0 0 0 0.6mm rgba(102, 144, 204, 0.6); /* Stronger glow */
}
```

**Blur Background Content:**
```css
.config-steps-container-v32:has(.config-step-card-v32:hover) 
.config-step-card-v32:not(:hover) {
    /* Blur non-hovered cards slightly */
    filter: blur(2px);
    opacity: 0.7;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
```

**Container Setup:**
```css
.config-steps-container-v32 {
    display: flex;
    gap: 1.5rem;
    padding: 3rem 1rem;
    position: relative;
    overflow: visible; /* Allow cards to expand beyond container */
}
```

---

## 💻 **COMPLETE CSS IMPLEMENTATION**

```css
/* ============================================
   V32 CONFIGURATOR STEPS REDESIGN
   Glassmorphism + iOS Style + Hover Effects
   ============================================ */

/* Container */
.config-steps-container-v32 {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    padding: 3rem 1rem;
    position: relative;
    overflow: visible;
    perspective: 1000px; /* For 3D effect */
}

/* Individual Step Card */
.config-step-card-v32 {
    /* Layout */
    flex: 1 1 calc(25% - 1.5rem);
    min-width: 250px;
    position: relative;
    
    /* Glassmorphism Base */
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    
    /* iOS-style Border */
    border: 1px solid rgba(102, 144, 204, 0.3);
    border-radius: 16px;
    
    /* Shadows & Glow */
    box-shadow: 
        0 8px 32px 0 rgba(102, 144, 204, 0.15),
        inset 0 0 0 1px rgba(255, 255, 255, 0.2),
        0 0 0 0.4mm rgba(102, 144, 204, 0.4);
    
    /* Spacing */
    padding: 2rem 1.5rem;
    
    /* Animation */
    transform-origin: center center;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    z-index: 1;
}

/* Hover State - 1.5x Growth */
.config-step-card-v32:hover {
    transform: scale(1.5);
    z-index: 10;
    
    /* Enhanced Glassmorphism */
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    
    /* Intensified Glow */
    box-shadow: 
        0 12px 48px 0 rgba(102, 144, 204, 0.3),
        inset 0 0 0 1px rgba(255, 255, 255, 0.3),
        0 0 0 0.6mm rgba(102, 144, 204, 0.6);
}

/* Blur Other Cards When One is Hovered */
.config-steps-container-v32:has(.config-step-card-v32:hover) 
.config-step-card-v32:not(:hover) {
    filter: blur(2px);
    opacity: 0.7;
    transform: scale(0.95);
}

/* Step Number/Heading */
.config-step-heading-v32 {
    font-family: 'Berlin Sans FB Demi', 'Berlin Sans FB', Arial, 'Helvetica Neue', sans-serif;
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #333333;
}

/* First Word Highlighting (Light Blue) */
.config-step-heading-v32 .first-word {
    color: #6690CC;
}

/* Step Number (Grey, Not Blue) */
.config-step-heading-v32 strong {
    color: #555555;
    font-weight: 700;
}

/* Icon Container */
.config-step-icon-v32 {
    width: 60px;
    height: 60px;
    margin-right: 1rem;
    flex-shrink: 0;
}

/* Body Text */
.config-step-text-v32 {
    font-family: 'Berlin Sans FB Demi', 'Berlin Sans FB', Arial, 'Helvetica Neue', sans-serif;
    font-size: 0.875rem;
    font-weight: 400;
    line-height: 1.6;
    color: #6c757d;
}

/* Responsive Adjustments */
@media (max-width: 1199px) {
    .config-step-card-v32 {
        flex: 1 1 calc(50% - 1.5rem);
    }
}

@media (max-width: 767px) {
    .config-step-card-v32 {
        flex: 1 1 100%;
    }
    
    .config-step-card-v32:hover {
        transform: scale(1.2); /* Smaller scale on mobile */
    }
}
```

---

## 📦 **COMPLETE HTML STRUCTURE**

```html
<div class="widget widget-code widget-none">
    <div class="widget-inner bg-appearance">
        <div class="config-steps-container-v32">
            
            <!-- Step 1: Profil -->
            <div class="config-step-card-v32">
                <span class="config-step-heading-v32">
                    <strong>1.</strong> <span class="first-word">Profil</span> festlegen
                </span>
                <div class="d-flex flex-row align-items-start mt-3">
                    <img src="https://cdn03.plentymarkets.com/xbqx3akj5qia/frontend/assets/img/profil-icon.svg" 
                         width="60" 
                         height="60" 
                         loading="lazy" 
                         alt="Konfigurator Schritte: Profil" 
                         class="config-step-icon-v32">
                    <p class="config-step-text-v32">
                        Bestimmen Sie Material, Hersteller und Profiltyp Ihres Wunschfensters. 
                        Legen Sie anschließend Fensterart und Öffnungsmechanik fest.
                    </p>
                </div>
            </div>
            
            <!-- Step 2: Maße -->
            <div class="config-step-card-v32">
                <span class="config-step-heading-v32">
                    <strong>2.</strong> <span class="first-word">Maße</span> wählen
                </span>
                <div class="d-flex flex-row align-items-start mt-3">
                    <img src="https://cdn03.plentymarkets.com/xbqx3akj5qia/frontend/assets/img/masse-icon.svg" 
                         width="60" 
                         height="60" 
                         loading="lazy" 
                         alt="Konfigurator Schritte: Maße" 
                         class="config-step-icon-v32">
                    <p class="config-step-text-v32">
                        Geben Sie Ihre individuellen Maße ein und passen Sie Details wie 
                        Dichtungen, Kern und Rahmen präzise an Ihre Anforderungen an.
                    </p>
                </div>
            </div>
            
            <!-- Step 3: Farbe -->
            <div class="config-step-card-v32">
                <span class="config-step-heading-v32">
                    <strong>3.</strong> <span class="first-word">Farbe</span> aussuchen
                </span>
                <div class="d-flex flex-row align-items-start mt-3">
                    <img src="https://cdn03.plentymarkets.com/xbqx3akj5qia/frontend/assets/img/farbe-icon.svg" 
                         width="60" 
                         height="60" 
                         loading="lazy" 
                         alt="Konfigurator Schritte: Farbe" 
                         class="config-step-icon-v32">
                    <p class="config-step-text-v32">
                        Entdecken Sie vielfältige Farbpaletten und Gestaltungsmöglichkeiten, 
                        die je nach Material und Hersteller zur Verfügung stehen.
                    </p>
                </div>
            </div>
            
            <!-- Step 4: Glas -->
            <div class="config-step-card-v32">
                <span class="config-step-heading-v32">
                    <strong>4.</strong> <span class="first-word">Glas</span> auswählen
                </span>
                <div class="d-flex flex-row align-items-start mt-3">
                    <img src="https://cdn03.plentymarkets.com/xbqx3akj5qia/frontend/assets/img/glas-icon.svg" 
                         width="60" 
                         height="60" 
                         loading="lazy" 
                         alt="Konfigurator Schritte: Glas" 
                         class="config-step-icon-v32">
                    <p class="config-step-text-v32">
                        Wählen Sie die passende Verglasung für Ihre Anforderungen – 
                        von erhöhtem Schallschutz bis zu speziellen Sicherheitsgläsern.
                    </p>
                </div>
            </div>
            
        </div>
    </div>
</div>
```

---

## ✅ **IMPLEMENTATION CHECKLIST**

### **Phase 1: Content (Text Rewrite)**
- [ ] Replace Step 1 text with modern German version
- [ ] Replace Step 2 text with modern German version
- [ ] Replace Step 3 text with modern German version
- [ ] Replace Step 4 text with modern German version
- [ ] Verify grammar and flow
- [ ] Ensure professional tone maintained

### **Phase 2: Visual Design**
- [ ] Remove all red colors from numbers and accents
- [ ] Change numbers to grey (#555555)
- [ ] Change first word to light blue (#6690CC)
- [ ] Apply Berlin Sans FB Demi font to all text
- [ ] Implement glassmorphism background (rgba + backdrop-filter)
- [ ] Add iOS-style border with 0.4mm glow (#6690CC)
- [ ] Set proper border-radius (16px)
- [ ] Add multi-layer box-shadow for depth
- [ ] Adjust text colors (headings #333333, body #6c757d)

### **Phase 3: Hover Effects**
- [ ] Implement 1.5x scale on hover
- [ ] Add z-index elevation on hover
- [ ] Blur non-hovered cards (blur(2px) + opacity: 0.7)
- [ ] Intensify glassmorphism on hover
- [ ] Enhance border glow on hover
- [ ] Add smooth cubic-bezier transition
- [ ] Test overflow: visible on container
- [ ] Verify mobile responsiveness (1.2x on mobile)

### **Testing**
- [ ] Test on desktop (Chrome, Firefox, Safari, Edge)
- [ ] Test on mobile devices
- [ ] Verify blur effects work (backdrop-filter support)
- [ ] Check hover animation smoothness
- [ ] Ensure cards don't overlap incorrectly
- [ ] Verify text readability on glassmorphism background
- [ ] Test with different screen sizes
- [ ] Verify all 4 cards behave consistently

---

## 🎯 **SUCCESS CRITERIA**

**Visual:**
- ✅ No red colors anywhere (numbers are grey)
- ✅ First words are light blue (#6690CC)
- ✅ Glassmorphism effect clearly visible
- ✅ iOS-style glowing border (0.4mm blur, light blue)
- ✅ Berlin Sans FB Demi font applied
- ✅ Text is grey (#6c757d), readable on glassmorphism

**Interactive:**
- ✅ Hover scales card to 1.5x smoothly
- ✅ Hovered card appears on top of others
- ✅ Non-hovered cards blur and fade slightly
- ✅ Background content behind expanded card is visible but blurred
- ✅ Animation is smooth with no jank
- ✅ Mobile hover works at 1.2x scale

**Content:**
- ✅ Text is in sophisticated, modern German
- ✅ Text is easier to understand than original
- ✅ Professional tone maintained
- ✅ Same meaning preserved
- ✅ Shorter, clearer sentences

---

## 📋 **RISK ASSESSMENT**

**Low Risk:**
- Text rewrite (reversible, doesn't affect functionality)
- Font changes (fallbacks in place)
- Color changes (CSS-only)

**Medium Risk:**
- Glassmorphism (browser support issues in older browsers)
  - Mitigation: Fallback to solid background
- Hover scale effect (may cause layout shifts)
  - Mitigation: overflow: visible, careful z-index management

**High Risk:**
- None identified

---

## 🔄 **ROLLBACK PLAN**

If issues occur:
1. Keep V31 version available
2. Document exact line numbers changed
3. Can revert section-by-section:
   - Text only (Phase 1)
   - Visual only (Phase 2)
   - Hover only (Phase 3)

---

## 📝 **NEXT STEPS**

1. **Review this plan** with stakeholder
2. **Create V32 HTML file** with changes
3. **Test in browser** (all phases)
4. **Iterate** based on visual results
5. **Deploy** to production

---

**Status:** ✅ INTEGRATION PLAN COMPLETE - READY FOR IMPLEMENTATION
**Risk Level:** LOW-MEDIUM - Non-invasive visual changes, glassmorphism fallbacks in place
**Confidence Level:** HIGH - Clear requirements, detailed specifications, comprehensive plan
