#!/usr/bin/env python3
"""
Image Optimizer Tool

Resizes and compresses images for web use.

Usage:
    python tools/optimize_images.py input.jpg
    python tools/optimize_images.py input.png --max-width 800 --quality 85
    python tools/optimize_images.py input.jpg --output ./images/

Requirements:
    pip install Pillow
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
        print("\nOr with pip3:")
        print("  pip3 install Pillow")
        sys.exit(1)


def get_output_path(input_path: Path, output_dir: Path, suffix: str = '') -> Path:
    """Generate output path for optimized image."""
    stem = input_path.stem
    ext = input_path.suffix.lower()

    # Convert PNG to JPG if not transparent
    if ext == '.png':
        ext = '.png'  # Keep PNG for now, could add transparency detection
    elif ext in ['.jpeg', '.jpg']:
        ext = '.jpg'

    if suffix:
        return output_dir / f"{stem}{suffix}{ext}"
    return output_dir / f"{stem}_optimized{ext}"


def optimize_image(
    input_path: Path,
    output_path: Path,
    max_width: int = 1200,
    max_height: int = None,
    quality: int = 85
) -> dict:
    """
    Optimize an image for web use.

    Returns dict with stats about the optimization.
    """
    check_pillow()

    # Open image
    img = Image.open(input_path)
    original_size = input_path.stat().st_size
    original_dimensions = img.size

    # Convert RGBA to RGB for JPEG (remove alpha channel)
    if img.mode == 'RGBA' and output_path.suffix.lower() in ['.jpg', '.jpeg']:
        # Create white background
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
        img = background
    elif img.mode != 'RGB' and output_path.suffix.lower() in ['.jpg', '.jpeg']:
        img = img.convert('RGB')

    # Calculate new dimensions maintaining aspect ratio
    width, height = img.size

    if max_width and width > max_width:
        ratio = max_width / width
        width = max_width
        height = int(height * ratio)

    if max_height and height > max_height:
        ratio = max_height / height
        height = max_height
        width = int(width * ratio)

    # Resize if needed
    if (width, height) != img.size:
        img = img.resize((width, height), Image.Resampling.LANCZOS)

    # Save optimized image
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_path.suffix.lower() in ['.jpg', '.jpeg']:
        img.save(output_path, 'JPEG', quality=quality, optimize=True)
    elif output_path.suffix.lower() == '.png':
        img.save(output_path, 'PNG', optimize=True)
    else:
        img.save(output_path, quality=quality, optimize=True)

    new_size = output_path.stat().st_size

    return {
        'input': str(input_path),
        'output': str(output_path),
        'original_size': original_size,
        'new_size': new_size,
        'original_dimensions': original_dimensions,
        'new_dimensions': (width, height),
        'reduction': round((1 - new_size / original_size) * 100, 1)
    }


def format_size(bytes_size: int) -> str:
    """Format bytes to human readable string."""
    for unit in ['B', 'KB', 'MB']:
        if bytes_size < 1024:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.1f} GB"


def print_results(stats: dict):
    """Print optimization results."""
    print(f"\n{'='*50}")
    print("IMAGE OPTIMIZATION RESULTS")
    print('='*50)
    print(f"  Input:  {stats['input']}")
    print(f"  Output: {stats['output']}")
    print(f"\n  Original: {stats['original_dimensions'][0]}x{stats['original_dimensions'][1]} "
          f"({format_size(stats['original_size'])})")
    print(f"  Optimized: {stats['new_dimensions'][0]}x{stats['new_dimensions'][1]} "
          f"({format_size(stats['new_size'])})")
    print(f"\n  Size reduction: {stats['reduction']}%")
    print('='*50)


def main():
    parser = argparse.ArgumentParser(
        description='Optimize images for web use'
    )
    parser.add_argument('input', type=Path, help='Input image file')
    parser.add_argument('--output', '-o', type=Path, default=None,
                       help='Output directory (default: same as input)')
    parser.add_argument('--max-width', '-w', type=int, default=1200,
                       help='Maximum width in pixels (default: 1200)')
    parser.add_argument('--max-height', type=int, default=None,
                       help='Maximum height in pixels')
    parser.add_argument('--quality', '-q', type=int, default=85,
                       help='JPEG quality 1-100 (default: 85)')
    parser.add_argument('--suffix', '-s', type=str, default='_optimized',
                       help='Suffix for output filename (default: _optimized)')

    args = parser.parse_args()

    # Validate input
    if not args.input.exists():
        print(f"ERROR: Input file not found: {args.input}")
        sys.exit(1)

    if not args.input.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp', '.gif']:
        print(f"ERROR: Unsupported image format: {args.input.suffix}")
        print("Supported formats: JPG, PNG, WebP, GIF")
        sys.exit(1)

    # Determine output path
    output_dir = args.output or args.input.parent
    output_path = get_output_path(args.input, output_dir, args.suffix)

    print(f"\nOptimizing: {args.input}")

    try:
        stats = optimize_image(
            args.input,
            output_path,
            max_width=args.max_width,
            max_height=args.max_height,
            quality=args.quality
        )
        print_results(stats)
        print("\nSuccess!")

    except Exception as e:
        print(f"\nERROR: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
