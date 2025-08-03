import json
import os

# Path to the behavior pack items
items_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/items"

# List of lightsaber colors
colors = ["blue", "green", "purple", "red", "white", "yellow"]

def simplify_hilt(color):
    """Simplify hilt to basic item"""
    hilt_path = os.path.join(items_path, f"{color}_hilt.json")
    
    hilt_data = {
        "format_version": "1.20.0",
        "minecraft:item": {
            "description": {
                "identifier": f"lightsaber:{color}_hilt",
                "menu_category": {
                    "category": "equipment"
                }
            },
            "components": {
                "minecraft:icon": {
                    "texture": f"{color}_hilt"
                },
                "minecraft:display_name": {
                    "value": f"item.lightsaber:{color}_hilt"
                },
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True
            }
        }
    }
    
    with open(hilt_path, 'w') as f:
        json.dump(hilt_data, f, indent=2)
    
    print(f"Simplified {color} hilt")

def simplify_active(color):
    """Simplify active lightsaber"""
    active_path = os.path.join(items_path, f"{color}_active.json")
    
    active_data = {
        "format_version": "1.20.0",
        "minecraft:item": {
            "description": {
                "identifier": f"lightsaber:{color}_active",
                "menu_category": {
                    "category": "equipment",
                    "is_hidden_in_commands": True
                }
            },
            "components": {
                "minecraft:icon": {
                    "texture": f"{color}_active"
                },
                "minecraft:display_name": {
                    "value": f"item.lightsaber:{color}_active"
                },
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True,
                "minecraft:damage": 12,
                "minecraft:enchantable": {
                    "value": 10,
                    "slot": "sword"
                },
                "minecraft:durability": {
                    "max_durability": 5000
                },
                "minecraft:repairable": {
                    "repair_items": [
                        {
                            "items": [f"lightsaber:kyber_crystal_{color}"],
                            "repair_amount": 1000
                        }
                    ]
                },
                "minecraft:digger": {
                    "use_efficiency": True,
                    "destroy_speeds": [
                        {
                            "block": "minecraft:web",
                            "speed": 100
                        }
                    ]
                }
            }
        }
    }
    
    with open(active_path, 'w') as f:
        json.dump(active_data, f, indent=2)
    
    print(f"Simplified {color} active lightsaber")

# Fix all lightsabers
for color in colors:
    simplify_hilt(color)
    simplify_active(color)

print("\nAll lightsabers simplified!")
print("\nTo activate/deactivate:")
print("1. Hold a lightsaber hilt or active lightsaber")
print("2. Sneak (crouch) for about half a second")
print("3. The lightsaber will toggle between hilt and active")
print("\nNote: The sneaking activation is already set up in the functions")