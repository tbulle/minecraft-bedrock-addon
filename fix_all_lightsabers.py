import json
import os

# Path to the behavior pack items
items_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/items"

# List of lightsaber colors
colors = ["blue", "green", "purple", "red", "white", "yellow"]

def fix_hilt(color):
    """Fix the hilt item to remove food component"""
    hilt_path = os.path.join(items_path, f"{color}_hilt.json")
    
    with open(hilt_path, 'r') as f:
        data = json.load(f)
    
    # Remove food-related components
    components = data["minecraft:item"]["components"]
    if "minecraft:food" in components:
        del components["minecraft:food"]
    if "minecraft:use_animation" in components:
        del components["minecraft:use_animation"]
    if "minecraft:use_duration" in components:
        del components["minecraft:use_duration"]
    if "minecraft:cooldown" in components:
        del components["minecraft:cooldown"]
    
    # Save the file
    with open(hilt_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Fixed {color} hilt")

def fix_active(color):
    """Fix the active lightsaber to be a proper weapon"""
    active_path = os.path.join(items_path, f"{color}_active.json")
    
    with open(active_path, 'r') as f:
        data = json.load(f)
    
    # Update damage to reasonable value
    components = data["minecraft:item"]["components"]
    components["minecraft:damage"] = 12
    
    # Remove food-related components
    if "minecraft:food" in components:
        del components["minecraft:food"]
    if "minecraft:use_animation" in components:
        del components["minecraft:use_animation"]
    if "minecraft:use_duration" in components:
        del components["minecraft:use_duration"]
    if "minecraft:cooldown" in components:
        del components["minecraft:cooldown"]
    
    # Save the file
    with open(active_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Fixed {color} active")

# Fix all lightsabers
for color in colors:
    if color != "blue":  # Blue is already fixed
        fix_hilt(color)
        fix_active(color)

print("\nAll lightsabers fixed!")
print("\nNow you can:")
print("1. Reload the world or use /reload command")
print("2. Right-click with a hilt to activate it")
print("3. Right-click with an active lightsaber to deactivate it")