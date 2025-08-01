from PIL import Image, ImageDraw
import os

def create_lightsaber_model_texture(color_name, blade_color, glow_color):
    """Create 64x32 model texture for lightsaber"""
    img = Image.new('RGBA', (64, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Hilt texture mapping (0,0 to 16,16)
    # Main hilt body
    draw.rectangle([0, 0, 16, 16], fill=(120, 120, 120, 255))
    # Grip pattern
    for i in range(0, 16, 4):
        draw.rectangle([2, i+1, 14, i+3], fill=(80, 80, 80, 255))
    
    # Blade texture mapping (16,0 to 48,16)
    # Blade core
    draw.rectangle([16, 0, 48, 16], fill=blade_color)
    # Blade edge gradient
    for i in range(4):
        alpha = 255 - (i * 50)
        color = (*glow_color[:3], alpha)
        draw.rectangle([16-i, 0, 16, 16], fill=color)
        draw.rectangle([48, 0, 48+i, 16], fill=color)
    
    # Emitter texture (48,0 to 64,16)
    draw.rectangle([48, 0, 64, 16], fill=(150, 150, 150, 255))
    draw.rectangle([50, 2, 62, 14], fill=(100, 100, 100, 255))
    
    # Bottom cap texture (0,16 to 16,32)
    draw.rectangle([0, 16, 16, 32], fill=(100, 100, 100, 255))
    draw.ellipse([2, 18, 14, 30], fill=(80, 80, 80, 255))
    
    return img

def create_hilt_model_texture():
    """Create texture for inactive hilt model"""
    img = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Main hilt texture
    draw.rectangle([0, 0, 16, 32], fill=(120, 120, 120, 255))
    
    # Grip details
    for i in range(0, 32, 4):
        draw.rectangle([2, i+1, 14, i+3], fill=(80, 80, 80, 255))
    
    # Emitter (top section)
    draw.rectangle([16, 0, 32, 8], fill=(150, 150, 150, 255))
    draw.rectangle([18, 2, 30, 6], fill=(100, 100, 100, 255))
    
    # Bottom cap
    draw.rectangle([16, 24, 32, 32], fill=(100, 100, 100, 255))
    draw.ellipse([18, 25, 30, 31], fill=(80, 80, 80, 255))
    
    # Control panel
    draw.rectangle([16, 12, 32, 20], fill=(60, 60, 60, 255))
    draw.rectangle([20, 14, 28, 18], fill=(40, 40, 40, 255))
    
    return img

def main():
    # Define lightsaber colors
    lightsabers = {
        'blue': {
            'blade': (100, 150, 255, 255),
            'glow': (150, 200, 255, 150)
        },
        'green': {
            'blade': (100, 255, 100, 255),
            'glow': (150, 255, 150, 150)
        },
        'red': {
            'blade': (255, 100, 100, 255),
            'glow': (255, 150, 150, 150)
        },
        'purple': {
            'blade': (200, 100, 255, 255),
            'glow': (225, 150, 255, 150)
        },
        'yellow': {
            'blade': (255, 255, 100, 255),
            'glow': (255, 255, 150, 150)
        },
        'white': {
            'blade': (255, 255, 255, 255),
            'glow': (255, 255, 255, 150)
        }
    }
    
    # Create model texture directory
    texture_dir = 'lightsaber_resource_pack/textures/models'
    os.makedirs(texture_dir, exist_ok=True)
    
    # Generate lightsaber model textures
    for color_name, colors in lightsabers.items():
        texture = create_lightsaber_model_texture(color_name, colors['blade'], colors['glow'])
        texture.save(f'{texture_dir}/lightsaber_{color_name}.png')
    
    # Generate hilt texture
    hilt_texture = create_hilt_model_texture()
    hilt_texture.save(f'{texture_dir}/lightsaber_hilt.png')
    
    print(f"Created {len(lightsabers) + 1} model textures!")

if __name__ == "__main__":
    main()