import json
import os

# Path to the behavior pack items
items_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/items"

# List of lightsaber colors
colors = ["blue", "green", "purple", "red", "white", "yellow"]

def fix_active_weapon(color):
    """Fix the active lightsaber to be a proper weapon"""
    active_path = os.path.join(items_path, f"{color}_active.json")
    
    with open(active_path, 'r') as f:
        data = json.load(f)
    
    components = data["minecraft:item"]["components"]
    
    # Add weapon component if not present
    if "minecraft:weapon" not in components:
        # Find the position after minecraft:hand_equipped
        components_list = list(components.items())
        new_components = {}
        
        for key, value in components_list:
            new_components[key] = value
            if key == "minecraft:hand_equipped":
                new_components["minecraft:weapon"] = {
                    "on_hurt_entity": {
                        "event": f"lightsaber:hit_effect"
                    }
                }
        
        data["minecraft:item"]["components"] = new_components
    
    # Add hit effect event if not present
    events = data["minecraft:item"]["events"]
    if "lightsaber:hit_effect" not in events:
        events["lightsaber:hit_effect"] = {
            "run_command": {
                "command": [
                    f"particle lightsaber:{color}_trail ~ ~ ~",
                    "playsound lightsaber.hit @a[r=10] ~ ~ ~ 0.5"
                ],
                "target": "holder"
            }
        }
    
    # Save the file
    with open(active_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Fixed {color} active lightsaber as weapon")

# Fix all lightsabers
for color in colors:
    if color != "blue":  # Blue is already fixed
        fix_active_weapon(color)

print("\nAll lightsabers are now proper weapons!")
print("\nThe lightsabers will now:")
print("- Deal 12 damage when hitting entities")
print("- Show particle effects on hit")
print("- Play sound effects on hit")
print("\nReload the world with /reload to test!")