# V32 Updated Configurator Steps - 8 Steps with Rectangular Layout

## 📋 USER FEEDBACK ANALYSIS

### Changes Requested:
1. ✅ **Step 1 content** - Keep closer to original with material types mentioned
2. ✅ **Add steps 5-8** - Currently missing, need to add:
   - Step 5: Sprossen wählen (Choose mullions)
   - Step 6: Rollladen wählen (Choose shutters)
   - Step 7: Sonstiges noch (Other options)
   - Step 8: Bestellung fertig (Order complete)
3. ✅ **Background color** - Use website background #f8f9fa (light gray)
4. ✅ **Layout change** - Rectangular boxes (wider, less tall)
5. ✅ **Grid layout** - 2 rows of 4 steps each (1-4 first row, 5-8 second row)

---

## 📝 UPDATED CONTENT (ALL 8 STEPS)

### **Schritt 1 - Profil auswählen**
Wählen Sie das passende Rahmenmaterial: **Kunststoff** für optimale Wärmedämmung, **Aluminium** für moderne Optik, **Holz** für natürliche Atmosphäre oder **Holz-Aluminium** als Premiumlösung.

### **Schritt 2 - Maße eingeben**
Geben Sie präzise Breite und Höhe ein. Unser System berücksichtigt automatisch Einbaumaße und erstellt eine passgenaue Konfiguration für Ihr Fenster.

### **Schritt 3 - Farbe wählen**
Entscheiden Sie sich für Ihre Wunschfarbe innen und außen. Von klassischem Weiß über elegante Holzdekore bis zu modernen Anthrazit-Tönen.

### **Schritt 4 - Glas konfigurieren**
Bestimmen Sie Verglasung und Zusatzoptionen: Schallschutz für mehr Ruhe, Sicherheitsglas für erhöhten Schutz oder Sonnenschutz für angenehmes Raumklima.

### **Schritt 5 - Sprossen wählen**
Wählen Sie zwischen verschiedenen Sprossenarten für Ihr Fenster. Zur Auswahl stehen innenliegende oder aufliegende Sprossen für individuelle Gestaltung.

### **Schritt 6 - Rollladen wählen**
Fügen Sie den auf Sie individuell zugeschnittenen Rollladen hinzu und ergänzen Sie optional den angepassten Insektenschutz für zusätzlichen Komfort.

### **Schritt 7 - Sonstiges noch**
Abschließend können Sie auswählen, ob Sie eine Montagevorbohrung oder eine Rahmenverbreiterung für eine optimale Passform benötigen.

### **Schritt 8 - Bestellung fertig**
Ist Ihre Bestellung fertig, können Sie alle Angaben auf Vollständigkeit kontrollieren und die Bestellung abschließen.

---

## 🎨 VISUAL DESIGN UPDATES

### Layout Structure:
```
┌─────────┬─────────┬─────────┬─────────┐
│ Step 1  │ Step 2  │ Step 3  │ Step 4  │  ← First Row
└─────────┴─────────┴─────────┴─────────┘
┌─────────┬─────────┬─────────┬─────────┐
│ Step 5  │ Step 6  │ Step 7  │ Step 8  │  ← Second Row
└─────────┴─────────┴─────────┴─────────┘
```

### Dimensions:
- **Width:** ~300px per card (fills row width)
- **Height:** ~180px (reduced from previous ~250px)
- **Aspect Ratio:** Wider rectangle (landscape orientation)
- **Gap:** 20px between cards
- **Responsive:** Stacks vertically on mobile

### Background:
- **Page background:** #f8f9fa (website background color)
- **Card glassmorphism:** rgba(255, 255, 255, 0.15) + backdrop blur

### Colors (Unchanged):
- **Numbers:** Grey #555555
- **First word:** Light blue #6690CC
- **Body text:** Grey #6c757d
- **Border:** iOS-style 0.4mm glow in light blue

### Hover Effects (Unchanged):
- **Scale:** 1.5x zoom
- **Siblings:** Blur(2px) + opacity(0.7)
- **Duration:** 0.4s cubic-bezier

---

## 🎯 IMPLEMENTATION CHECKLIST

### Content:
- [x] Step 1 - Updated with material types (Kunststoff, Aluminium, Holz, Holz-Aluminium)
- [x] Step 2 - Keep modern style
- [x] Step 3 - Keep modern style
- [x] Step 4 - Keep modern style
- [x] Step 5 - Added Sprossen content
- [x] Step 6 - Added Rollladen content
- [x] Step 7 - Added Sonstiges content
- [x] Step 8 - Added Bestellung content

### Design:
- [x] Background color: #f8f9fa (website color)
- [x] Cards: Rectangular shape (wider, less tall)
- [x] Layout: 2 rows × 4 columns grid
- [x] Height: Reduced to ~180px
- [x] Width: Increased to fill row (~300px each)
- [x] All visual elements maintained (glassmorphism, borders, colors)

### Effects:
- [x] 1.5x hover zoom
- [x] Sibling blur effect
- [x] Glassmorphism intensifies
- [x] Border glow strengthens
- [x] Smooth animations

---

## 📊 PREVIEW SPECIFICATIONS

| Aspect | Value |
|--------|-------|
| **Total Steps** | 8 (was 4) |
| **Layout** | 2 rows × 4 columns |
| **Card Width** | ~300px |
| **Card Height** | ~180px |
| **Background** | #f8f9fa |
| **Responsive** | Mobile stacks vertically |
| **Content** | All 8 steps in modern German |

---

## ✅ SUCCESS CRITERIA

1. ✅ All 8 steps visible
2. ✅ Step 1 mentions material types
3. ✅ Rectangular cards (landscape orientation)
4. ✅ 2 rows of 4 cards each
5. ✅ Website background color (#f8f9fa)
6. ✅ All hover effects working
7. ✅ Responsive on mobile
8. ✅ Professional, modern German text

---

**Status:** PLAN COMPLETE - READY FOR IMPLEMENTATION
**Next:** Create updated configurator-steps-preview-v2.html
