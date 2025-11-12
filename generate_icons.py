#!/usr/bin/env python3
"""
Generate PWA icons for BetArena application.
Creates app icons and favicons in various sizes.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size, color_scheme, filename, is_maskable=False):
    """
    Create a square icon with the BetArena theme.
    
    Args:
        size: Icon size in pixels (e.g., 192, 512)
        color_scheme: Tuple of (primary_color, secondary_color, text_color)
        filename: Output filename
        is_maskable: Whether to create a maskable icon (safe area for rounded corners)
    """
    primary, secondary, text = color_scheme
    
    # Create new image with gradient background
    img = Image.new('RGBA', (size, size), color=primary)
    draw = ImageDraw.Draw(img)
    
    # Create a gradient-like effect by drawing a rectangle
    for i in range(size):
        # Interpolate between primary and secondary color
        r = int(primary[0] + (secondary[0] - primary[0]) * i / size)
        g = int(primary[1] + (secondary[1] - primary[1]) * i / size)
        b = int(primary[2] + (secondary[2] - primary[2]) * i / size)
        draw.line([(0, i), (size, i)], fill=(r, g, b, 255))
    
    # Draw a circle in the center for the maskable variant
    margin = size // 8
    circle_color = text
    
    # Draw outer circle
    draw.ellipse(
        [(margin, margin), (size - margin, size - margin)],
        fill=circle_color,
        outline=None
    )
    
    # Draw inner circle for contrast
    inner_margin = margin + size // 16
    draw.ellipse(
        [(inner_margin, inner_margin), (size - inner_margin, size - inner_margin)],
        fill=secondary,
        outline=None
    )
    
    # Draw a stylized "B" in the center
    center_x = size // 2
    center_y = size // 2
    
    # Draw letter "B" using simple geometric shapes
    letter_size = size // 3
    letter_x = center_x - letter_size // 2
    letter_y = center_y - letter_size // 2
    
    # Vertical bar of B
    bar_width = letter_size // 4
    draw.rectangle(
        [(letter_x, letter_y), (letter_x + bar_width, letter_y + letter_size)],
        fill=circle_color
    )
    
    # Top bump of B
    draw.arc(
        [(letter_x + bar_width, letter_y), (letter_x + letter_size, letter_y + letter_size // 2)],
        0, 180, fill=circle_color, width=bar_width
    )
    
    # Bottom bump of B
    draw.arc(
        [(letter_x + bar_width, letter_y + letter_size // 2), (letter_x + letter_size, letter_y + letter_size)],
        180, 360, fill=circle_color, width=bar_width
    )
    
    img.save(filename, 'PNG')
    print(f"✓ Created {filename} ({size}x{size})")

def create_favicon(size, color_scheme, filename):
    """Create a small favicon."""
    primary, secondary, text = color_scheme
    
    img = Image.new('RGBA', (size, size), color=primary)
    draw = ImageDraw.Draw(img)
    
    # Simple gradient
    for i in range(size):
        r = int(primary[0] + (secondary[0] - primary[0]) * i / size)
        g = int(primary[1] + (secondary[1] - primary[1]) * i / size)
        b = int(primary[2] + (secondary[2] - primary[2]) * i / size)
        draw.line([(0, i), (size, i)], fill=(r, g, b, 255))
    
    # Draw a small "B"
    margin = size // 6
    draw.ellipse([(margin, margin), (size - margin, size - margin)], fill=text)
    
    img.save(filename, 'PNG')
    print(f"✓ Created {filename} ({size}x{size})")

def create_screenshot(width, height, filename):
    """Create a mockup screenshot for PWA install prompt."""
    # Create a background with app colors
    img = Image.new('RGB', (width, height), color=(102, 126, 234))
    draw = ImageDraw.Draw(img)
    
    # Draw a header bar
    draw.rectangle([(0, 0), (width, height // 6)], fill=(118, 75, 162))
    
    # Draw some content blocks to simulate app content
    block_height = height // 10
    block_margin = width // 20
    
    for i in range(1, 5):
        y_pos = height // 6 + (i - 1) * block_height + block_margin
        draw.rectangle(
            [(block_margin, y_pos), (width - block_margin, y_pos + block_height - block_margin)],
            fill=(255, 255, 255)
        )
    
    img.save(filename, 'PNG')
    print(f"✓ Created {filename} ({width}x{height})")

def main():
    """Generate all required PWA assets."""
    
    # Define color scheme: (primary, secondary, text)
    color_scheme = (
        (102, 126, 234),  # primary: #667eea
        (118, 75, 162),   # secondary: #764ba2
        (255, 255, 255)   # text: white
    )
    
    # Create directories if they don't exist
    os.makedirs('apps/web/public/icons', exist_ok=True)
    os.makedirs('apps/web/public/screenshots', exist_ok=True)
    
    print("Generating PWA Icons...")
    print("-" * 50)
    
    # Generate app icons
    icon_sizes = [192, 256, 384, 512]
    for size in icon_sizes:
        create_icon(
            size,
            color_scheme,
            f'apps/web/public/icons/icon-{size}x{size}.png'
        )
    
    print()
    print("Generating Maskable Icons...")
    print("-" * 50)
    
    # Generate maskable icons
    for size in [192, 512]:
        create_icon(
            size,
            color_scheme,
            f'apps/web/public/icons/icon-maskable-{size}x{size}.png',
            is_maskable=True
        )
    
    print()
    print("Generating Favicons...")
    print("-" * 50)
    
    # Generate favicons
    create_favicon(16, color_scheme, 'apps/web/public/favicon-16x16.png')
    create_favicon(32, color_scheme, 'apps/web/public/favicon-32x32.png')
    
    # Create favicon.ico (use 32x32 as base)
    favicon_img = Image.new('RGBA', (32, 32), color=color_scheme[0])
    draw = ImageDraw.Draw(favicon_img)
    
    for i in range(32):
        r = int(color_scheme[0][0] + (color_scheme[1][0] - color_scheme[0][0]) * i / 32)
        g = int(color_scheme[0][1] + (color_scheme[1][1] - color_scheme[0][1]) * i / 32)
        b = int(color_scheme[0][2] + (color_scheme[1][2] - color_scheme[0][2]) * i / 32)
        draw.line([(0, i), (32, i)], fill=(r, g, b, 255))
    
    favicon_img.save('apps/web/public/favicon.ico', 'ICO')
    print("✓ Created favicon.ico (32x32)")
    
    print()
    print("Generating Screenshots...")
    print("-" * 50)
    
    # Generate screenshots
    create_screenshot(540, 720, 'apps/web/public/screenshots/screenshot-540x720.png')
    create_screenshot(1280, 720, 'apps/web/public/screenshots/screenshot-1280x720.png')
    
    print()
    print("-" * 50)
    print("✅ All PWA assets generated successfully!")
    print()
    print("Generated files:")
    print("  Icons: apps/web/public/icons/icon-{192,256,384,512}x{192,256,384,512}.png")
    print("  Maskable Icons: apps/web/public/icons/icon-maskable-{192,512}x{192,512}.png")
    print("  Favicons: apps/web/public/favicon-{16,32}x{16,32}.png, favicon.ico")
    print("  Screenshots: apps/web/public/screenshots/screenshot-{540x720,1280x720}.png")

if __name__ == '__main__':
    main()
