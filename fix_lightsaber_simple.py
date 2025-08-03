import json
import os

# Path to the behavior pack items
items_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/items"

# List of lightsaber colors
colors = ["blue", "green", "purple", "red", "white", "yellow"]

def fix_hilt_simple(color):
    """Fix hilt to work with simple right-click activation"""
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
                "minecraft:hand_equipped": True,
                "minecraft:interact_button": True,
                "minecraft:on_use": {
                    "on_use": {
                        "event": f"lightsaber:activate_{color}",
                        "target": "self"
                    }
                }
            },
            "events": {
                f"lightsaber:activate_{color}": {
                    "run_command": {
                        "command": [
                            f"function lightsaber/activate_{color}"
                        ],
                        "target": "holder"
                    }
                }
            }
        }
    }
    
    with open(hilt_path, 'w') as f:
        json.dump(hilt_data, f, indent=2)
    
    print(f"Fixed {color} hilt")

def fix_active_simple(color):
    """Fix active lightsaber to work as weapon item"""
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
                "minecraft:interact_button": True,
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
                            "block": "minecraft:wool",
                            "speed": 100
                        },
                        {
                            "block": "minecraft:web", 
                            "speed": 100
                        },
                        {
                            "block": "minecraft:bamboo",
                            "speed": 100
                        }
                    ]
                },
                "minecraft:on_use": {
                    "on_use": {
                        "event": f"lightsaber:deactivate_{color}",
                        "target": "self"
                    }
                }
            },
            "events": {
                f"lightsaber:deactivate_{color}": {
                    "run_command": {
                        "command": [
                            f"function lightsaber/deactivate_{color}"
                        ],
                        "target": "holder"
                    }
                }
            }
        }
    }
    
    with open(active_path, 'w') as f:
        json.dump(active_data, f, indent=2)
    
    print(f"Fixed {color} active lightsaber")

# Fix all lightsabers
for color in colors:
    fix_hilt_simple(color)
    fix_active_simple(color)

print("\nAll lightsabers fixed!")
print("\nIMPORTANT: The lightsabers will work as weapons but won't show as swords.")
print("This is a Bedrock limitation - custom items can have damage but aren't true weapon items.")
print("\nThey will:")
print("- Deal 12 damage when hitting mobs")
print("- Be enchantable as swords")
print("- Have durability")
print("- Activate/deactivate with right-click")