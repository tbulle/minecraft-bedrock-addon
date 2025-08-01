from PIL import Image, ImageDraw

def create_lightsaber_icon():
    # Create 128x128 image with black background
    img = Image.new('RGBA', (128, 128), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw lightsaber hilt (silver/gray)
    hilt_color = (150, 150, 150, 255)
    draw.rectangle([56, 80, 72, 120], fill=hilt_color)
    
    # Draw hilt details
    draw.rectangle([58, 85, 70, 88], fill=(100, 100, 100, 255))
    draw.rectangle([58, 92, 70, 95], fill=(100, 100, 100, 255))
    draw.rectangle([58, 99, 70, 102], fill=(100, 100, 100, 255))
    
    # Draw lightsaber blade (blue glow)
    blade_color = (100, 150, 255, 255)
    glow_color = (150, 200, 255, 100)
    
    # Main blade
    draw.rectangle([62, 10, 66, 80], fill=blade_color)
    
    # Glow effect
    draw.rectangle([60, 8, 68, 82], fill=glow_color)
    draw.rectangle([58, 6, 70, 84], fill=(150, 200, 255, 50))
    
    # Save icons
    img.save('lightsaber_behavior_pack/pack_icon.png')
    img.save('lightsaber_resource_pack/pack_icon.png')
    print("Pack icons created!")

if __name__ == "__main__":
    create_lightsaber_icon()