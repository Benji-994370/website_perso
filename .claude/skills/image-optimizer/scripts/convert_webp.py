#!/usr/bin/env python3
"""
WebP Conversion Tool

Converts images to WebP format for optimal web performance.

Usage:
    python convert_webp.py input.jpg
    python convert_webp.py input.png --quality 85
    python convert_webp.py images/*.jpg --output ./webp/
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


def check_pillow():
    """Check if Pillow is installed."""
    if not PIL_AVAILABLE:
        print("ERROR: Pillow library is required but not installed.")
        print("\nInstall it with:")
        print("  pip install Pillow")
        sys.exit(1)


def convert_to_webp(
    input_path: Path,
    output_path: Path = None,
    quality: int = 85,
    max_width: int = None
) -> dict:
    """
    Convert image to WebP format.

    Returns dict with stats about the conversion.
    """
    check_pillow()

    # Open image
    img = Image.open(input_path)
    original_size = input_path.stat().st_size
    original_dimensions = img.size

    # Resize if max_width specified
    if max_width and img.size[0] > max_width:
        ratio = max_width / img.size[0]
        new_size = (max_width, int(img.size[1] * ratio))
        img = img.resize(new_size, Image.Resampling.LANCZOS)

    # Handle transparency
    if img.mode == 'RGBA':
        # Keep alpha channel for WebP
        pass
    elif img.mode != 'RGB':
        img = img.convert('RGB')

    # Generate output path if not specified
    if output_path is None:
        output_path = input_path.with_suffix('.webp')

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save as WebP
    img.save(output_path, 'WEBP', quality=quality, method=6)

    new_size_bytes = output_path.stat().st_size

    return {
        'input': str(input_path),
        'output': str(output_path),
        'original_size': original_size,
        'new_size': new_size_bytes,
        'original_dimensions': original_dimensions,
        'new_dimensions': img.size,
        'reduction': round((1 - new_size_bytes / original_size) * 100, 1)
    }


def format_size(bytes_size: int) -> str:
    """Format bytes to human readable string."""
    for unit in ['B', 'KB', 'MB']:
        if bytes_size < 1024:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.1f} GB"


def print_results(stats: dict):
    """Print conversion results."""
    print(f"\n{'='*50}")
    print("WEBP CONVERSION RESULTS")
    print('='*50)
    print(f"  Input:  {stats['input']}")
    print(f"  Output: {stats['output']}")
    print(f"\n  Original: {stats['original_dimensions'][0]}x{stats['original_dimensions'][1]} "
          f"({format_size(stats['original_size'])})")
    print(f"  WebP: {stats['new_dimensions'][0]}x{stats['new_dimensions'][1]} "
          f"({format_size(stats['new_size'])})")
    print(f"\n  Size reduction: {stats['reduction']}%")
    print('='*50)


def main():
    parser = argparse.ArgumentParser(
        description='Convert images to WebP format'
    )
    parser.add_argument('input', type=Path, nargs='+', help='Input image file(s)')
    parser.add_argument('--output', '-o', type=Path, default=None,
                       help='Output directory (default: same as input)')
    parser.add_argument('--quality', '-q', type=int, default=85,
                       help='WebP quality 1-100 (default: 85)')
    parser.add_argument('--max-width', '-w', type=int, default=None,
                       help='Maximum width in pixels')

    args = parser.parse_args()

    for input_path in args.input:
        if not input_path.exists():
            print(f"ERROR: Input file not found: {input_path}")
            continue

        if input_path.suffix.lower() not in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            print(f"ERROR: Unsupported format: {input_path.suffix}")
            continue

        # Determine output path
        if args.output:
            output_path = args.output / f"{input_path.stem}.webp"
        else:
            output_path = input_path.with_suffix('.webp')

        print(f"\nConverting: {input_path}")

        try:
            stats = convert_to_webp(
                input_path,
                output_path,
                quality=args.quality,
                max_width=args.max_width
            )
            print_results(stats)
            print("Success!")

        except Exception as e:
            print(f"\nERROR: {e}")


if __name__ == '__main__':
    main()
