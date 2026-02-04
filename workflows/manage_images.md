# Manage Images

Add, optimize, and update images on the portfolio website.

## Objective
Properly prepare and add images to the website with correct sizing and optimization.

## Required Inputs
- **Image file**: Source image (JPG, PNG, or WebP)
- **Purpose**: Where the image will be used (profile, testimonial, project)

## Image Specifications

| Purpose | Filename | Dimensions | Format |
|---------|----------|------------|--------|
| Profile photo | `benjamin-audry.jpg` | 500x500px | JPEG |
| Testimonial author | `sacha-delcourt.jpg` | 200x200px | JPEG |
| Project (standard) | `project-name.jpg` | 800x500px | JPEG |
| Project (featured) | `project-name.jpg` | 1200x700px | JPEG |

## Steps

### 1. Optimize the Image

```bash
python tools/optimize_images.py input.jpg --output ./ --max-width 500
```

Options:
- `--max-width`: Maximum width in pixels
- `--quality`: JPEG quality (default: 85)
- `--output`: Output directory

### 2. Place the Image

Move the optimized image to the project root:
```bash
mv optimized_image.jpg "/Users/boldysai/Desktop/Claude Code/website_perso/"
```

### 3. Update HTML Reference

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

### 4. Verify

1. Preview locally:
   ```bash
   python3 -m http.server 8000
   ```

2. Check:
   - Image loads correctly
   - No distortion or stretching
   - Reasonable file size (under 200KB for most images)
   - Alt text is descriptive

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

## Tools Used

- `tools/optimize_images.py` - Primary image processing tool
