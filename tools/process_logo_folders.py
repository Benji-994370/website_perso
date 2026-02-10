#!/usr/bin/env python3
"""
Extract logos from nested folders and organize them.

Prioritizes:
1. SVG files (vector, best quality)
2. PNG files (raster, good for complex logos)
3. WebP/AVIF (modern formats)

Outputs to images/logos/ with clean, lowercase names.
"""

import os
import shutil
from pathlib import Path
from typing import Optional

SOURCE_DIR = Path("images/logos/raw/Logos tools")
OUTPUT_DIR = Path("images/logos")

# Format priority: SVG > PNG > WebP > AVIF
FORMAT_PRIORITY = ['.svg', '.png', '.webp', '.avif']

def clean_filename(name: str) -> str:
    """Convert company name to clean lowercase filename."""
    # Remove special characters and convert to lowercase
    name = name.lower()
    name = name.replace(' ', '-')
    name = name.replace('.', '-')
    name = name.replace('_', '-')
    # Remove consecutive hyphens
    while '--' in name:
        name = name.replace('--', '-')
    return name.strip('-')

def find_best_logo(folder_path: Path) -> Optional[Path]:
    """Find the best quality logo in a folder (prefer SVG)."""
    if not folder_path.is_dir():
        return None

    # Get all image files in the folder
    logo_files = {}
    for ext in FORMAT_PRIORITY:
        matches = list(folder_path.glob(f"*{ext}"))
        if matches:
            logo_files[ext] = matches[0]  # Take first match

    # Return highest priority format available
    for ext in FORMAT_PRIORITY:
        if ext in logo_files:
            return logo_files[ext]

    return None

def process_logos():
    """Extract and organize logos from nested folders."""

    if not SOURCE_DIR.exists():
        print(f"❌ Source directory not found: {SOURCE_DIR}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    processed = []
    skipped = []

    # Process company folders
    for item in sorted(SOURCE_DIR.iterdir()):
        if item.is_dir():
            company_name = item.name
            best_logo = find_best_logo(item)

            if best_logo:
                # Create clean output filename
                clean_name = clean_filename(company_name)
                output_file = OUTPUT_DIR / f"{clean_name}{best_logo.suffix}"

                # Copy logo
                shutil.copy2(best_logo, output_file)

                file_size = output_file.stat().st_size / 1024  # KB
                processed.append({
                    'name': company_name,
                    'format': best_logo.suffix,
                    'size': file_size,
                    'output': output_file.name
                })
            else:
                skipped.append(company_name)

    # Also process loose files in the root
    for item in SOURCE_DIR.iterdir():
        if item.is_file() and item.suffix.lower() in ['.svg', '.png', '.jpg', '.webp', '.avif']:
            clean_name = clean_filename(item.stem)
            output_file = OUTPUT_DIR / f"{clean_name}{item.suffix}"
            shutil.copy2(item, output_file)

            file_size = output_file.stat().st_size / 1024
            processed.append({
                'name': item.stem,
                'format': item.suffix,
                'size': file_size,
                'output': output_file.name
            })

    # Print summary
    print(f"🎨 Processed {len(processed)} logos:\n")

    for logo in processed:
        format_emoji = "📄" if logo['format'] == '.svg' else "🖼️"
        print(f"  {format_emoji} {logo['name']:20} → {logo['output']:30} ({logo['size']:.1f}KB)")

    if skipped:
        print(f"\n⚠️  Skipped {len(skipped)} folders (no logos found):")
        for name in skipped:
            print(f"  - {name}")

    print(f"\n✅ All logos saved to {OUTPUT_DIR}/")

if __name__ == "__main__":
    process_logos()
