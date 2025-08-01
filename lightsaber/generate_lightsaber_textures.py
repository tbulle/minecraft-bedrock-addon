from PIL import Image, ImageDraw
import os

def create_lightsaber_hilt_texture(color_name, color_accent):
    """Create 16x16 lightsaber hilt texture"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Main hilt body (gray metallic)
    draw.rectangle([5, 2, 10, 14], fill=(120, 120, 120, 255))
    
    # Hilt details (darker gray)
    draw.rectangle([6, 3, 9, 4], fill=(80, 80, 80, 255))
    draw.rectangle([6, 6, 9, 7], fill=(80, 80, 80, 255))
    draw.rectangle([6, 9, 9, 10], fill=(80, 80, 80, 255))
    
    # Activation button (color accent)
    draw.rectangle([7, 11, 8, 12], fill=color_accent)
    
    # Emitter (top)
    draw.rectangle([6, 1, 9, 2], fill=(150, 150, 150, 255))
    
    # Bottom cap
    draw.rectangle([6, 14, 9, 15], fill=(100, 100, 100, 255))
    
    return img

def create_lightsaber_active_texture(color_name, blade_color, glow_color):
    """Create 16x16 active lightsaber texture"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Blade glow (outer)
    draw.rectangle([6, 0, 9, 8], fill=glow_color)
    draw.rectangle([5, 0, 10, 7], fill=(*glow_color[:3], 100))
    
    # Blade core
    draw.rectangle([7, 0, 8, 8], fill=blade_color)
    
    # Hilt (compact version)
    draw.rectangle([6, 9, 9, 14], fill=(120, 120, 120, 255))
    draw.rectangle([7, 10, 8, 11], fill=(80, 80, 80, 255))
    draw.rectangle([6, 14, 9, 15], fill=(100, 100, 100, 255))
    
    return img

def create_kyber_crystal_texture(color_name, crystal_color):
    """Create 16x16 kyber crystal texture"""
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Crystal shape (diamond-like)
    # Top point
    draw.polygon([(8, 2), (5, 5), (11, 5)], fill=crystal_color)
    # Middle
    draw.rectangle([5, 5, 11, 10], fill=crystal_color)
    # Bottom point
    draw.polygon([(8, 14), (5, 10), (11, 10)], fill=crystal_color)
    
    # Shine effect (lighter color)
    lighter = tuple(min(255, c + 50) for c in crystal_color[:3]) + (255,)
    draw.polygon([(8, 3), (6, 5), (8, 5)], fill=lighter)
    draw.rectangle([6, 5, 8, 7], fill=lighter)
    
    return img

def create_component_textures():
    """Create component textures"""
    textures = {}
    
    # Durasteel Ingot
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([2, 6, 14, 10], fill=(100, 100, 120, 255))
    draw.rectangle([3, 7, 13, 9], fill=(120, 120, 140, 255))
    textures['durasteel_ingot'] = img
    
    # Power Cell
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([5, 2, 11, 14], fill=(40, 40, 40, 255))
    draw.rectangle([6, 3, 10, 13], fill=(200, 50, 50, 255))
    draw.rectangle([7, 1, 9, 2], fill=(150, 150, 150, 255))
    draw.rectangle([7, 14, 9, 15], fill=(150, 150, 150, 255))
    textures['power_cell'] = img
    
    # Hilt Casing
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([4, 2, 12, 14], fill=(130, 130, 130, 255))
    draw.rectangle([5, 3, 11, 13], fill=(0, 0, 0, 0))  # Hollow center
    draw.rectangle([4, 4, 5, 12], fill=(150, 150, 150, 255))  # Left edge
    draw.rectangle([11, 4, 12, 12], fill=(110, 110, 110, 255))  # Right edge
    textures['hilt_casing'] = img
    
    # Focusing Lens
    img = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([4, 4, 12, 12], fill=(200, 200, 255, 180))
    draw.ellipse([6, 6, 10, 10], fill=(220, 220, 255, 200))
    draw.ellipse([7, 7, 9, 9], fill=(255, 255, 255, 255))
    textures['focusing_lens'] = img
    
    return textures

def main():
    # Define lightsaber colors
    lightsabers = {
        'blue': {
            'accent': (50, 100, 200, 255),
            'blade': (100, 150, 255, 255),
            'glow': (150, 200, 255, 150),
            'crystal': (50, 100, 255, 255)
        },
        'green': {
            'accent': (50, 200, 50, 255),
            'blade': (100, 255, 100, 255),
            'glow': (150, 255, 150, 150),
            'crystal': (50, 255, 50, 255)
        },
        'red': {
            'accent': (200, 50, 50, 255),
            'blade': (255, 100, 100, 255),
            'glow': (255, 150, 150, 150),
            'crystal': (255, 50, 50, 255)
        },
        'purple': {
            'accent': (150, 50, 200, 255),
            'blade': (200, 100, 255, 255),
            'glow': (225, 150, 255, 150),
            'crystal': (200, 50, 255, 255)
        },
        'yellow': {
            'accent': (200, 200, 50, 255),
            'blade': (255, 255, 100, 255),
            'glow': (255, 255, 150, 150),
            'crystal': (255, 255, 50, 255)
        },
        'white': {
            'accent': (200, 200, 200, 255),
            'blade': (255, 255, 255, 255),
            'glow': (255, 255, 255, 150),
            'crystal': (230, 230, 230, 255)
        }
    }
    
    # Create texture directory
    texture_dir = 'lightsaber_resource_pack/textures/items'
    os.makedirs(texture_dir, exist_ok=True)
    
    # Generate lightsaber textures
    for color_name, colors in lightsabers.items():
        # Hilt texture
        hilt = create_lightsaber_hilt_texture(color_name, colors['accent'])
        hilt.save(f'{texture_dir}/{color_name}_hilt.png')
        
        # Active lightsaber texture
        active = create_lightsaber_active_texture(color_name, colors['blade'], colors['glow'])
        active.save(f'{texture_dir}/{color_name}_active.png')
        
        # Kyber crystal texture
        crystal = create_kyber_crystal_texture(color_name, colors['crystal'])
        crystal.save(f'{texture_dir}/kyber_crystal_{color_name}.png')
    
    # Generate component textures
    components = create_component_textures()
    for name, texture in components.items():
        texture.save(f'{texture_dir}/{name}.png')
    
    print(f"Created {len(lightsabers) * 3 + len(components)} textures!")

if __name__ == "__main__":
    main()