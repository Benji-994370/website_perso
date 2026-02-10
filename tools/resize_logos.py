#!/usr/bin/env python3
"""
Logo Resizer and Optimizer

Processes logos from images/logos/raw/ and outputs optimized versions to images/logos/
- Resizes to consistent dimensions (max 120px height for PNG/JPG)
- Optimizes file size
- Preserves SVG files as-is (they're already vector)
- Keeps originals in raw/ folder
"""

import os
import sys
from pathlib import Path
from PIL import Image

# Configuration
RAW_DIR = Path("images/logos/raw")
OUTPUT_DIR = Path("images/logos")
MAX_HEIGHT = 120  # Maximum height in pixels for raster images
QUALITY = 85  # JPEG/PNG quality (1-100)

def optimize_logo(input_path: Path, output_path: Path):
    """Resize and optimize a logo image."""

    # Skip SVG files - they're already optimized vectors
    if input_path.suffix.lower() == '.svg':
        print(f"  📄 {input_path.name} → Copying SVG as-is")
        output_path.write_bytes(input_path.read_bytes())
        return

    try:
        # Open image
        img = Image.open(input_path)

        # Get original dimensions
        original_size = img.size
        original_file_size = input_path.stat().st_size / 1024  # KB

        # Calculate new dimensions maintaining aspect ratio
        if img.height > MAX_HEIGHT:
            aspect_ratio = img.width / img.height
            new_height = MAX_HEIGHT
            new_width = int(MAX_HEIGHT * aspect_ratio)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            print(f"  🔄 {input_path.name}")
            print(f"     Resized: {original_size[0]}x{original_size[1]} → {new_width}x{new_height}")
        else:
            print(f"  ✓ {input_path.name} (already optimal size)")

        # Convert RGBA to RGB if saving as JPEG
        if output_path.suffix.lower() in ['.jpg', '.jpeg']:
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create white background
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background

        # Save optimized image
        save_kwargs = {
            'optimize': True,
            'quality': QUALITY
        }

        if output_path.suffix.lower() == '.png':
            save_kwargs = {'optimize': True}

        img.save(output_path, **save_kwargs)

        # Show file size reduction
        new_file_size = output_path.stat().st_size / 1024  # KB
        reduction = ((original_file_size - new_file_size) / original_file_size) * 100
        print(f"     Size: {original_file_size:.1f}KB → {new_file_size:.1f}KB ({reduction:.0f}% reduction)")

    except Exception as e:
        print(f"  ❌ Error processing {input_path.name}: {e}")

def main():
    """Process all logos in the raw directory."""

    # Ensure directories exist
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Get all image files from raw directory
    image_extensions = {'.png', '.jpg', '.jpeg', '.svg', '.webp'}
    raw_files = [
        f for f in RAW_DIR.iterdir()
        if f.is_file() and f.suffix.lower() in image_extensions
    ]

    if not raw_files:
        print(f"📁 No logos found in {RAW_DIR}/")
        print(f"   Drop your logo files there and run this script again.")
        return

    print(f"🎨 Processing {len(raw_files)} logo(s)...\n")

    # Process each logo
    for raw_file in raw_files:
        output_file = OUTPUT_DIR / raw_file.name
        optimize_logo(raw_file, output_file)

    print(f"\n✅ Done! Optimized logos saved to {OUTPUT_DIR}/")
    print(f"   Original files remain in {RAW_DIR}/")

if __name__ == "__main__":
    # Check if PIL is installed
    try:
        from PIL import Image
    except ImportError:
        print("❌ Error: Pillow library not found")
        print("   Install it with: pip install Pillow")
        sys.exit(1)

    main()
