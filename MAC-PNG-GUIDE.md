# 🍎 Mac PNG Editing Guide

Complete guide for checking and editing PNG files on macOS.

## Table of Contents
1. [Check PNG Size](#check-png-size)
2. [Edit PNG Files](#edit-png-files)
3. [Recommended Tools](#recommended-tools)
4. [Step-by-Step Instructions](#step-by-step-instructions)
5. [Verify Your Changes](#verify-your-changes)

---

## Check PNG Size

### Method 1: Finder (Easiest) ⭐
1. Right-click on `Logo-01.png`
2. Select **"Get Info"** (or press `⌘ + I`)
3. Look at **Dimensions** field
4. Should show: `2817 × 2127` (ultra-tight version)
5. If it shows: `2821 × 2131` = needs cropping

### Method 2: Preview (Built-in)
1. Double-click `Logo-01.png` to open in Preview
2. Go to **Tools** → **Show Inspector** (or press `⌘ + I`)
3. Look at the dimensions in the Inspector panel
4. Check width and height values

### Method 3: Quick Look
1. Select `Logo-01.png` in Finder
2. Press **Spacebar** for Quick Look
3. Dimensions shown at bottom of window

### Method 4: Terminal
```bash
cd /path/to/frontend-glass-configurator
sips -g pixelWidth -g pixelHeight Logo-01.png
```

Expected output for ultra-tight version:
```
pixelWidth: 2817
pixelHeight: 2127
```

---

## Edit PNG Files

### Best Tools for Mac

#### 1. Preview (Free, Built-in) ⭐ RECOMMENDED
- **Pros:** Simple, fast, already installed
- **Cons:** Basic features only
- **Best for:** Simple crops, removing borders

#### 2. GIMP (Free)
- **Download:** https://www.gimp.org/downloads/
- **Pros:** Powerful, free, precise control
- **Cons:** Learning curve, not Mac-native
- **Best for:** Advanced editing, batch processing

#### 3. Photoshop (Paid)
- **Pros:** Industry standard, powerful
- **Cons:** Expensive subscription
- **Best for:** Professional work

#### 4. Pixelmator Pro (Paid, Mac-optimized)
- **Pros:** Mac-native, great performance
- **Cons:** One-time purchase ($40)
- **Best for:** Mac users wanting pro features

#### 5. Online Tools (Free, No Install)
- **Photopea:** https://www.photopea.com (free Photoshop alternative)
- **Pixlr:** https://pixlr.com/editor/
- **Pros:** No installation, works anywhere
- **Cons:** Requires internet, uploads your file

---

## Step-by-Step Instructions

### Option 1: Using Preview (Recommended for Mac)

#### Check Current Size:
1. Open `Logo-01.png` in Preview (double-click)
2. **Tools** → **Show Inspector** (`⌘ + I`)
3. Note the dimensions

#### Crop to Remove Borders:
1. Open `Logo-01.png` in Preview
2. Click **Show Markup Toolbar** button (pencil icon)
3. Select **Rectangular Selection** tool
4. Draw a rectangle around the logo content (avoid empty space)
5. **Tools** → **Crop** (or press `⌘ + K`)
6. **File** → **Export**
7. Name: `Logo-01-cropped.png`
8. Format: **PNG**
9. Click **Save**

#### Replace Original:
```bash
# In Terminal:
cd /path/to/frontend-glass-configurator
mv Logo-01.png Logo-01-old.png
mv Logo-01-cropped.png Logo-01.png
```

---

### Option 2: Using GIMP (Advanced)

#### Install GIMP:
1. Download from https://www.gimp.org/downloads/
2. Install the .dmg file
3. Open GIMP

#### Crop Logo:
1. **File** → **Open** → Select `Logo-01.png`
2. **Image** → **Crop to Selection** OR
3. **Tools** → **Crop** (or press `Shift + C`)
4. Drag crop area around logo content
5. Press **Enter** to apply crop
6. **File** → **Export As**
7. Save as `Logo-01.png`

#### Auto-Crop Empty Space:
1. Open `Logo-01.png` in GIMP
2. **Image** → **Autocrop Image**
3. GIMP automatically removes empty borders
4. **File** → **Export As**
5. Save as PNG

---

### Option 3: Using Online Tools (No Install)

#### Photopea (Free Photoshop Alternative):
1. Go to https://www.photopea.com
2. **File** → **Open** → Upload `Logo-01.png`
3. Select **Crop Tool** (C key)
4. Drag around logo content
5. Press **Enter**
6. **File** → **Export As** → **PNG**
7. Download and replace Logo-01.png

---

## Recommended Workflow

### For Quick Border Removal:
1. ✅ **Use Preview** (simplest, already installed)
2. Open logo
3. Select content area
4. Crop
5. Export
6. Done in 1 minute!

### For Precise Control:
1. ✅ **Use GIMP** (free, powerful)
2. Open logo
3. Use Autocrop feature
4. Verify result
5. Export
6. Higher quality result

### For Professional Work:
1. ✅ **Use Photoshop or Pixelmator Pro**
2. Maximum control
3. Best quality
4. Worth it for important projects

---

## Verify Your Changes

### Check New Dimensions:
```bash
sips -g pixelWidth -g pixelHeight Logo-01.png
```

Should show approximately:
- Width: 2817px (100% logo content)
- Height: 2127px (100% logo content)

### Check File Size:
```bash
ls -lh Logo-01.png
```

Should be around 95KB (±10KB is normal)

### Test in Browser:
1. Open `header-v36-final.html` in browser
2. Logo should fill 150px height
3. No extra white space above/below
4. Perfect fit in 160px header

### Visual Inspection:
1. Open Logo-01.png in Preview
2. Zoom to 100%
3. Check edges for any remaining transparent borders
4. Logo content should go right to the edges

---

## Troubleshooting

### "Logo still has white space in browser"
**Solution:** Clear browser cache
```
Safari: ⌘ + ⌥ + E (Clear Cache)
Chrome: ⌘ + Shift + R (Hard Reload)
Firefox: ⌘ + Shift + Delete (Clear Cache)
```

### "Can't crop in Preview"
**Solution:** 
1. Make sure you're in Markup mode (pencil icon)
2. Select Rectangular Selection tool
3. Draw selection THEN use Tools → Crop

### "Crop makes logo look bad"
**Solution:**
1. Undo (⌘ + Z)
2. Select larger area (include more pixels)
3. Try Autocrop in GIMP instead

### "File size increased after crop"
**Solution:**
1. Re-export with lower compression
2. Or use online PNG optimizer: https://tinypng.com

---

## Quick Reference

### Keyboard Shortcuts (Preview):
- `⌘ + I` - Show Inspector (view dimensions)
- `⌘ + K` - Crop to selection
- `⌘ + Z` - Undo
- `⌘ + S` - Save
- `⌘ + Shift + S` - Export

### Keyboard Shortcuts (GIMP):
- `Shift + C` - Crop tool
- `Enter` - Apply crop
- `⌘ + Z` - Undo
- `⌘ + Shift + E` - Export As

### Terminal Commands:
```bash
# Check dimensions
sips -g pixelWidth -g pixelHeight Logo-01.png

# Check file size
ls -lh Logo-01.png

# Backup before editing
cp Logo-01.png Logo-01-backup.png

# Replace logo
mv Logo-01-new.png Logo-01.png
```

---

## Summary

**Easiest Method:** Preview (built-in, free, 1 minute)
**Best Quality:** GIMP Autocrop (free, precise)
**No Install:** Photopea online (browser-based)

**Goal:** Logo should be 2817×2127px with zero borders
**Test:** Open header-v36-final.html - logo should fit perfectly in 160px header

---

**Need Help?** Check LOGO-COMPARISON.md for more details about the logo issue.
