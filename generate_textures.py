#!/usr/bin/env python3
"""
Generate placeholder textures for Halo Minecraft Add-on
Creates pack icons (128x128) and item textures (16x16)
"""

from PIL import Image, ImageDraw, ImageFont
import os
import sys

def create_pack_icon(color, text, filename, size=128):
    """Create a pack icon with specified color and text"""
    img = Image.new('RGBA', (size, size), color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fall back to default if not available
    try:
        font_size = size // 8
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # Draw text in center
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size - text_width) // 2
    y = (size - text_height) // 2
    
    # Add text shadow for better visibility
    draw.text((x+2, y+2), text, fill=(0, 0, 0, 128), font=font)
    draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
    
    # Add border
    draw.rectangle([0, 0, size-1, size-1], outline=(255, 255, 255, 200), width=2)
    
    img.save(filename)
    print(f"Created pack icon: {filename}")

def create_item_texture(color, item_name, filename, size=16):
    """Create a simple item texture with specified color"""
    img = Image.new('RGBA', (size, size), color)
    draw = ImageDraw.Draw(img)
    
    # Add simple pattern based on item type
    if 'helmet' in item_name.lower():
        # Helmet pattern - curved top
        draw.arc([2, 2, size-3, size-3], 0, 180, fill=(255, 255, 255, 100), width=2)
        draw.rectangle([4, size//2, size-5, size-3], fill=(0, 0, 0, 50))
    elif 'chestplate' in item_name.lower():
        # Chestplate pattern - rectangular with shoulder pads
        draw.rectangle([2, 2, size-3, size-3], outline=(255, 255, 255, 100), width=1)
        draw.rectangle([1, 3, 3, 6], fill=(255, 255, 255, 80))
        draw.rectangle([size-4, 3, size-2, 6], fill=(255, 255, 255, 80))
    elif 'leggings' in item_name.lower():
        # Leggings pattern - two legs
        draw.rectangle([2, 2, 6, size-2], outline=(255, 255, 255, 100), width=1)
        draw.rectangle([9, 2, 13, size-2], outline=(255, 255, 255, 100), width=1)
    elif 'boots' in item_name.lower():
        # Boots pattern - L-shaped
        draw.rectangle([2, size//2, size-3, size-2], fill=(255, 255, 255, 100))
        draw.rectangle([2, size-4, size//2, size-2], fill=(255, 255, 255, 80))
    elif 'sword' in item_name.lower():
        # Sword pattern - blade and hilt
        draw.line([size//2, 1, size//2, size-4], fill=(200, 200, 255, 255), width=2)
        draw.rectangle([size//2-2, size-4, size//2+1, size-1], fill=(139, 69, 19, 255))
    elif 'rifle' in item_name.lower() or 'launcher' in item_name.lower():
        # Rifle pattern - horizontal weapon
        draw.rectangle([2, size//2-1, size-3, size//2+1], fill=(100, 100, 100, 255))
        draw.circle([size-4, size//2], 2, fill=(50, 50, 50, 255))
    elif 'grenade' in item_name.lower():
        # Grenade pattern - oval with pin
        draw.ellipse([3, 4, size-4, size-3], fill=(50, 100, 50, 255))
        draw.circle([size//2, 3], 1, fill=(255, 255, 0, 255))
    else:
        # Generic pattern - simple border with center dot
        draw.rectangle([1, 1, size-2, size-2], outline=(255, 255, 255, 150), width=1)
        draw.circle([size//2, size//2], 2, fill=(255, 255, 255, 200))
    
    img.save(filename)
    print(f"Created item texture: {filename}")

def main():
    base_path = "halo"
    
    # Create pack icons
    pack_icons = [
        {
            'path': os.path.join(base_path, 'halo_behavior_pack', 'pack_icon.png'),
            'color': (34, 139, 34, 255),  # Forest green
            'text': 'HALO\nBEHAVIOR'
        },
        {
            'path': os.path.join(base_path, 'halo_resource_pack', 'pack_icon.png'),
            'color': (30, 144, 255, 255),  # Dodger blue
            'text': 'HALO\nRESOURCE'
        }
    ]
    
    for icon in pack_icons:
        os.makedirs(os.path.dirname(icon['path']), exist_ok=True)
        create_pack_icon(icon['color'], icon['text'], icon['path'])
    
    # Create item textures
    texture_base = os.path.join(base_path, 'halo_resource_pack', 'textures', 'items')
    
    # Armor textures - different colors for different sets
    armor_items = [
        # Spartan Mark VI (Blue-ish)
        ('armor/spartan_mark_vi_helmet.png', (70, 130, 180, 255), 'spartan_mark_vi_helmet'),
        ('armor/spartan_mark_vi_chestplate.png', (70, 130, 180, 255), 'spartan_mark_vi_chestplate'),
        ('armor/spartan_mark_vi_leggings.png', (70, 130, 180, 255), 'spartan_mark_vi_leggings'),
        ('armor/spartan_mark_vi_boots.png', (70, 130, 180, 255), 'spartan_mark_vi_boots'),
        
        # Spartan Mark V (Green-ish)
        ('armor/spartan_mark_v_helmet.png', (85, 107, 47, 255), 'spartan_mark_v_helmet'),
        ('armor/spartan_mark_v_chestplate.png', (85, 107, 47, 255), 'spartan_mark_v_chestplate'),
        ('armor/spartan_mark_v_leggings.png', (85, 107, 47, 255), 'spartan_mark_v_leggings'),
        ('armor/spartan_mark_v_boots.png', (85, 107, 47, 255), 'spartan_mark_v_boots'),
        
        # ODST (Dark gray)
        ('armor/odst_helmet.png', (47, 79, 79, 255), 'odst_helmet'),
        ('armor/odst_chestplate.png', (47, 79, 79, 255), 'odst_chestplate'),
        ('armor/odst_leggings.png', (47, 79, 79, 255), 'odst_leggings'),
        ('armor/odst_boots.png', (47, 79, 79, 255), 'odst_boots'),
    ]
    
    # Weapon textures
    weapon_items = [
        ('weapons/energy_sword.png', (128, 0, 128, 255), 'energy_sword'),
        ('weapons/plasma_rifle.png', (255, 20, 147, 255), 'plasma_rifle'),
        ('weapons/needler.png', (255, 69, 0, 255), 'needler'),
        ('weapons/assault_rifle.png', (105, 105, 105, 255), 'assault_rifle'),
        ('weapons/battle_rifle.png', (119, 136, 153, 255), 'battle_rifle'),
        ('weapons/sniper_rifle.png', (64, 64, 64, 255), 'sniper_rifle'),
        ('weapons/rocket_launcher.png', (139, 69, 19, 255), 'rocket_launcher'),
        ('weapons/plasma_grenade.png', (0, 191, 255, 255), 'plasma_grenade'),
        ('weapons/frag_grenade.png', (34, 139, 34, 255), 'frag_grenade'),
    ]
    
    # Equipment textures
    equipment_items = [
        ('equipment/active_camo.png', (173, 216, 230, 128), 'active_camo'),
        ('equipment/overshield.png', (255, 215, 0, 255), 'overshield'),
    ]
    
    all_items = armor_items + weapon_items + equipment_items
    
    for item_path, color, item_name in all_items:
        full_path = os.path.join(texture_base, item_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        create_item_texture(color, item_name, full_path)
    
    print(f"\nGenerated {len(pack_icons)} pack icons and {len(all_items)} item textures!")
    print("All placeholder textures created successfully.")

if __name__ == "__main__":
    main()