---
name: image-optimizer
description: Resize, optimize, and convert images for web use. Use when user needs to process profile photos, logos, or any images for their website.
allowed-tools: Bash(python *), Bash(pip *), Bash(mv *), Bash(cp *), Bash(mkdir *), Bash(ls *), Read, Write, WebSearch
---

# Image Optimizer Skill

Optimize images for web performance by resizing, compressing, and converting formats.

## Recommended Dimensions

| Image Type | Max Width | Notes |
|------------|-----------|-------|
| Profile photos | 800px | Square preferred |
| Logos | 400px | Maintain aspect ratio |
| Thumbnails | 200px | Square for avatars |
| Hero images | 1920px | Full-width backgrounds |
| Project screenshots | 1200px | Standard content width |

## How to Optimize

### Using the existing tool (if available)
```bash
python tools/optimize_images.py "input.jpg" --max-width 800 --output ./images/ --suffix ""
```

### Manual optimization with Python
```python
from PIL import Image

def optimize_image(input_path, output_path, max_width=800, quality=85):
    img = Image.open(input_path)

    # Calculate new dimensions
    width, height = img.size
    if width > max_width:
        ratio = max_width / width
        new_size = (max_width, int(height * ratio))
        img = img.resize(new_size, Image.Resampling.LANCZOS)

    # Convert RGBA to RGB for JPEG
    if img.mode == 'RGBA':
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        img = background

    # Save optimized
    img.save(output_path, quality=quality, optimize=True)
```

## WebP Conversion

For best compression, convert to WebP format:
```python
img.save(output_path.replace('.jpg', '.webp'), 'WEBP', quality=85)
```

## Finding Logos Online

When a logo is needed:
1. Search for "[company name] logo png transparent"
2. Prefer official sources or high-quality versions
3. Download the highest resolution available
4. Optimize to 400px width for web use

## Workflow

1. Check image dimensions and file size
2. Create output directory if needed: `mkdir -p images/`
3. Resize to appropriate web dimensions
4. Convert to optimized format (WebP preferred, fallback to optimized JPG/PNG)
5. Rename to web-friendly filename (lowercase, hyphens, no spaces)
6. Report size reduction

## Requirements

Pillow must be installed:
```bash
pip install Pillow
```
