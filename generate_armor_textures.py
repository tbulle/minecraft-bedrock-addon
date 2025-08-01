#!/usr/bin/env python3
"""
Generate placeholder armor model texture files for Halo Minecraft add-on.
Creates 64x32 pixel PNG files with solid colors for armor textures.
"""

from PIL import Image
import os

# Define the output directory
output_dir = r"C:\Projects\minecraft-bedrock-addon\halo\halo_resource_pack\textures\models\armor"

# Define the armor textures with their colors
armor_textures = {
    "spartan_mark_vi_1.png": "#2D5016",  # Green for Spartan VI layer 1
    "spartan_mark_vi_2.png": "#2D5016",  # Green for Spartan VI layer 2
    "spartan_mark_v_1.png": "#4B5320",   # Olive for Spartan V layer 1
    "spartan_mark_v_2.png": "#4B5320",   # Olive for Spartan V layer 2
    "odst_1.png": "#2F2F2F",             # Dark gray for ODST layer 1
    "odst_2.png": "#2F2F2F",             # Dark gray for ODST layer 2
}

# Image dimensions
width = 64
height = 32

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Generate each texture file
for filename, color_hex in armor_textures.items():
    # Convert hex color to RGB tuple
    color_rgb = tuple(int(color_hex[1:][i:i+2], 16) for i in (0, 2, 4))
    
    # Create a new image with the specified color
    image = Image.new('RGB', (width, height), color_rgb)
    
    # Save the image
    output_path = os.path.join(output_dir, filename)
    image.save(output_path, 'PNG')
    
    print(f"Created {filename} ({width}x{height}) with color {color_hex}")

print(f"\nAll armor texture placeholders created in: {output_dir}")