# Images Directory

## 📁 Folder Structure

```
images/
├── logos/              # Optimized logos ready for web
│   ├── raw/           # 👈 DROP NEW LOGOS HERE
│   │   └── DROP_LOGOS_HERE.md
│   └── *.svg, *.png   # Optimized logos (max 120px height)
├── screenshots/       # Project screenshots
├── profile/          # Team/testimonial photos
```

## 🎨 How to Add New Logos

### Option 1: Drop individual logo files

```bash
# 1. Drag and drop logos to:
images/logos/raw/

# 2. Run the optimizer:
python tools/resize_logos.py

# Accepted formats: SVG, PNG, JPG, WebP
```

### Option 2: Drop logo folders (from brand kits)

```bash
# 1. Drag company folders with multiple logo files to:
images/logos/raw/Logos tools/

# 2. Extract the best format from each folder:
python tools/process_logo_folders.py

# Automatically picks: SVG > PNG > WebP > AVIF
```

### What happens:

- ✅ Prioritizes SVG files (vector, best quality)
- ✅ Resizes raster images to max 120px height
- ✅ Optimizes file sizes (60-80% reduction)
- ✅ Creates clean lowercase-with-hyphens filenames
- ✅ Keeps originals in `raw/` as backup

## 📊 Current Stats

- **Logos**: 34 files (25 SVG, 7 PNG, 1 JPG, 1 AVIF) - duplicates removed ✨
- **Screenshots**: 3 project previews
- **Profiles**: 4 team/testimonial photos

## 🎯 Logo Best Practices

**Preferred formats:**
1. **SVG** - Vector format, scales perfectly, smallest file size
2. **PNG** - For logos with transparency
3. **JPG** - Only if SVG/PNG unavailable (no transparency)

**File naming:**
- Use lowercase with hyphens: `company-name.svg`
- Avoid spaces and special characters

## 🔧 Troubleshooting

**"Cannot identify image file" error:**
- The file is likely corrupted or not a real image
- Try re-downloading from the official brand source
- Use SVG when possible (search "company-name svg logo")

**Logo looks blurry:**
- Original resolution was too low
- Try to find a higher-res version or use SVG
