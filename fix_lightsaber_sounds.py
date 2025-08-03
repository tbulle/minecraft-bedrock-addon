import json
import os

# Path to the behavior pack items
items_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/items"

# List of lightsaber colors
colors = ["blue", "green", "purple", "red", "white", "yellow"]

def fix_sounds_in_file(file_path):
    """Replace custom sounds with vanilla sounds"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace custom sounds with vanilla ones
    content = content.replace('playsound lightsaber.ignite', 'playsound random.levelup')
    content = content.replace('playsound lightsaber.extinguish', 'playsound random.fizz')
    
    # Also remove the entity events that don't exist
    content = content.replace('event entity @s lightsaber:blue_activated', '')
    content = content.replace('event entity @s lightsaber:blue_deactivated', '')
    content = content.replace('event entity @s lightsaber:green_activated', '')
    content = content.replace('event entity @s lightsaber:green_deactivated', '')
    content = content.replace('event entity @s lightsaber:purple_activated', '')
    content = content.replace('event entity @s lightsaber:purple_deactivated', '')
    content = content.replace('event entity @s lightsaber:red_activated', '')
    content = content.replace('event entity @s lightsaber:red_deactivated', '')
    content = content.replace('event entity @s lightsaber:white_activated', '')
    content = content.replace('event entity @s lightsaber:white_deactivated', '')
    content = content.replace('event entity @s lightsaber:yellow_activated', '')
    content = content.replace('event entity @s lightsaber:yellow_deactivated', '')
    
    # Clean up the command arrays
    content = content.replace('",\n                ""', '"')
    content = content.replace('",\r\n                ""', '"')
    
    with open(file_path, 'w') as f:
        f.write(content)

# Fix all lightsaber files
for color in colors:
    hilt_path = os.path.join(items_path, f"{color}_hilt.json")
    active_path = os.path.join(items_path, f"{color}_active.json")
    
    if os.path.exists(hilt_path):
        fix_sounds_in_file(hilt_path)
        print(f"Fixed sounds in {color} hilt")
    
    if os.path.exists(active_path):
        fix_sounds_in_file(active_path)
        print(f"Fixed sounds in {color} active")

print("\nAll lightsaber sounds fixed to use vanilla sounds!")
print("- Ignite sound: random.levelup")
print("- Extinguish sound: random.fizz")