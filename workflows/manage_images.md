# Manage Images

Add, optimize, and update images on the portfolio website.

## Objective
Properly prepare and add images to the website with correct sizing and optimization.

## Required Inputs
- **Image file**: Source image (JPG, PNG, or WebP)
- **Purpose**: Where the image will be used (profile, testimonial, project, logo)
- **Target directory**: Where the image should be stored

## Directory Structure

```
images/
├── profile/          # Profile and testimonial photos
│   ├── benjamin-audry.jpg
│   ├── sacha-delcourt.jpg
│   └── greg-photo.jpg
├── screenshots/      # Project screenshots
│   ├── kuration-screenshot.png
│   ├── boldys-screenshot.png
│   └── purple-sales-screenshot.png
└── logos/           # Company and tool logos
    ├── raw/         # Original unprocessed logos
    └── (optimized)  # Processed logos for web
```

## Image Specifications

| Purpose | Directory | Recommended Dimensions | Max File Size | Format |
|---------|-----------|----------------------|---------------|--------|
| Profile photo | `images/profile/` | 500x500px | 100KB | JPEG |
| Testimonial author | `images/profile/` | 200x200px | 50KB | JPEG |
| Project screenshot | `images/screenshots/` | 1920x1080px | 500KB | PNG/JPEG |
| Tool logo | `images/logos/` | Original aspect | 50KB | SVG/PNG |

## Steps

### Pre-Optimization Checklist

Before processing images:
- [ ] Check image dimensions (use Preview, Photoshop, or online tool)
- [ ] Verify file size (should be reasonable, not multi-MB)
- [ ] Confirm image quality is good
- [ ] Check aspect ratio matches target use case
- [ ] Remove any sensitive metadata (EXIF data)

### 1. Optimize the Image

**For profile/testimonial photos (JPEG):**
```bash
python tools/optimize_images.py input.jpg --max-width 500 --quality 85
```

**For project screenshots (PNG/JPEG):**
```bash
python tools/optimize_images.py screenshot.png --max-width 1920 --quality 90
```

**For logos (batch processing):**
```bash
# Use the batch logo processor
python tools/process_logo_folders.py
# Or resize individual logos
python tools/resize_logos.py input-logo.png --max-height 100
```

**Common options:**
- `--max-width`: Maximum width in pixels
- `--max-height`: Maximum height in pixels (maintains aspect ratio)
- `--quality`: JPEG quality (default: 85, range: 1-100)
- `--output`: Output directory (default: current directory)

### 2. Place the Image in Correct Directory

**Profile/testimonial photos:**
```bash
mv optimized-photo.jpg images/profile/
```

**Project screenshots:**
```bash
mv optimized-screenshot.png images/screenshots/
```

**Logos:**
```bash
# Raw originals go here (keep for future processing)
mv original-logo.svg images/logos/raw/

# Optimized versions go in main logos directory
mv optimized-logo.svg images/logos/
```

### 3. Verify File Size

Check that the optimized image meets size requirements:
```bash
ls -lh images/profile/your-image.jpg
```

**Target sizes:**
- Profile photos: < 100KB
- Screenshots: < 500KB
- Logos: < 50KB

If too large, re-optimize with lower quality or smaller dimensions.

### 4. Update HTML Reference

**Profile photo** (About section, ~line 200):
```html
<img src="benjamin-audry.jpg" alt="Benjamin Audry" class="profile-image">
```

**Testimonial photo** (~line 285):
```html
<img src="sacha-delcourt.jpg" alt="Sacha Delcourt" class="author-image">
```

**Project image** (in project card):
```html
<div class="project-media">
    <img src="project-name.jpg" alt="Project Name interface">
</div>
```

### 5. Validate HTML After Changes

After updating HTML references, validate the structure:
```bash
python tools/validate_html.py index.html
```

This checks:
- ✓ All images have alt attributes
- ✓ HTML structure is valid
- ✓ No broken references

### 6. Local Preview & Testing

1. Start local server:
   ```bash
   python3 -m http.server 8000
   ```

2. Open http://localhost:8000 in browser

3. **Testing checklist:**
   - [ ] Image loads correctly
   - [ ] No distortion or stretching
   - [ ] Reasonable file size (check Network tab in DevTools)
   - [ ] Alt text is descriptive and accurate
   - [ ] Image looks good at different screen sizes (responsive)
   - [ ] Image has proper contrast with background

4. Test at different breakpoints:
   - Desktop: 1920px, 1440px, 1024px
   - Tablet: 768px
   - Mobile: 414px, 375px

### 7. Run Pre-Commit Checks

Before committing changes, run the validation script:
```bash
bash tools/pre-commit-check.sh
```

This will:
- Validate all HTML files
- Check for broken links
- Warn about large unoptimized images
- Ensure quality standards

## Image Fallbacks

The CSS includes fallback styling for missing images:
- Profile: Gradient background with centered icon
- Testimonials: Similar gradient fallback
- Projects: Gradient placeholder

This means the site works without images, but they should be added for a professional appearance.

## Currently Missing Images

These images are referenced but not present:
1. `benjamin-audry.jpg` - Profile photo for About section
2. `sacha-delcourt.jpg` - Testimonial author photo

## Edge Cases

- **Large source files**: Always run through optimizer first
- **Wrong aspect ratio**: Crop to match specifications before optimizing
- **Transparent backgrounds**: Use PNG format, not JPEG
- **Retina displays**: Consider providing @2x versions for critical images

## Automation

### GitHub Actions

When you push changes to the repository, GitHub Actions will automatically:
- Validate HTML structure
- Check for broken links
- Report large unoptimized images (>500KB)

See `.github/workflows/validate.yml` for details.

### Batch Processing

For processing multiple logos at once:
```bash
# Place all logos in images/logos/raw/
python tools/process_logo_folders.py

# This will:
# - Optimize all logos
# - Resize to standard dimensions
# - Output to appropriate directories
```

## Tools Used

- `tools/optimize_images.py` - Primary image processing tool
- `tools/resize_logos.py` - Logo-specific resizing
- `tools/process_logo_folders.py` - Batch logo processing
- `tools/validate_html.py` - HTML validation with image checks
