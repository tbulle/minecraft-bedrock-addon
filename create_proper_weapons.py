import json
import os

# Path to the behavior pack items
items_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/items"

# List of lightsaber colors
colors = ["blue", "green", "purple", "red", "white", "yellow"]

def create_active_weapon(color):
    """Create a proper weapon-based lightsaber"""
    active_path = os.path.join(items_path, f"{color}_active.json")
    
    # Proper Bedrock weapon structure
    weapon_data = {
        "format_version": "1.21.50",
        "minecraft:item": {
            "description": {
                "identifier": f"lightsaber:{color}_active",
                "menu_category": {
                    "category": "equipment"
                }
            },
            "components": {
                "minecraft:icon": {
                    "textures": {
                        "default": f"{color}_active"
                    }
                },
                "minecraft:display_name": {
                    "value": f"item.lightsaber:{color}_active"
                },
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True,
                "minecraft:damage": {
                    "value": 12
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
                "minecraft:creative_category": {
                    "parent": "itemGroup.name.sword"
                },
                "minecraft:allow_off_hand": True,
                "minecraft:should_despawn": True,
                "minecraft:tags": {
                    "tags": ["minecraft:is_sword"]
                }
            }
        }
    }
    
    # Save the file
    with open(active_path, 'w') as f:
        json.dump(weapon_data, f, indent=2)
    
    print(f"Created proper {color} active lightsaber weapon")

def create_hilt(color):
    """Update hilt with proper format"""
    hilt_path = os.path.join(items_path, f"{color}_hilt.json")
    
    hilt_data = {
        "format_version": "1.21.50",
        "minecraft:item": {
            "description": {
                "identifier": f"lightsaber:{color}_hilt",
                "menu_category": {
                    "category": "equipment"
                }
            },
            "components": {
                "minecraft:icon": {
                    "textures": {
                        "default": f"{color}_hilt"
                    }
                },
                "minecraft:display_name": {
                    "value": f"item.lightsaber:{color}_hilt"
                },
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True,
                "minecraft:interact_button": "interact.activate",
                "minecraft:use_modifiers": {
                    "use_duration": 0,
                    "movement_modifier": 1.0
                },
                "minecraft:tags": {
                    "tags": ["lightsaber:hilt"]
                }
            }
        }
    }
    
    # Save the file  
    with open(hilt_path, 'w') as f:
        json.dump(hilt_data, f, indent=2)
    
    print(f"Updated {color} hilt")

# Create all lightsabers
for color in colors:
    create_active_weapon(color)
    create_hilt(color)

print("\nAll lightsabers recreated as proper weapons!")
print("\nNote: You'll need to use commands/functions to handle the activation toggle")