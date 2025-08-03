import json
import os

# Path to the lightsaber items directory
items_dir = r"C:\Users\trull\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs\lightsaber\items"

# Simple hilt that can be swapped manually
def create_simple_hilt(color):
    return {
        "format_version": "1.20.50",
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
                    "value": f"{color.capitalize()} Lightsaber (Inactive)"
                },
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True
            }
        }
    }

# Keep active lightsabers as weapons
def create_simple_active(color):
    return {
        "format_version": "1.20.50",
        "minecraft:item": {
            "description": {
                "identifier": f"lightsaber:{color}_active",
                "menu_category": {
                    "category": "equipment"
                }
            },
            "components": {
                "minecraft:icon": {
                    "texture": f"{color}_active"
                },
                "minecraft:display_name": {
                    "value": f"{color.capitalize()} Lightsaber (Active)"
                },
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True,
                "minecraft:durability": {
                    "max_durability": 5000
                },
                "minecraft:damage": 15,
                "minecraft:enchantable": {
                    "value": 14,
                    "slot": "sword"
                },
                "minecraft:can_destroy_in_creative": False,
                "minecraft:weapon": {
                    "on_hurt_entity": {
                        "event": "damage_dealt"
                    }
                },
                "minecraft:digger": {
                    "use_efficiency": True,
                    "destroy_speeds": [
                        {
                            "block": "minecraft:web",
                            "speed": 15
                        },
                        {
                            "block": "minecraft:bamboo",
                            "speed": 10
                        }
                    ]
                }
            },
            "events": {
                "damage_dealt": {
                    "damage": {
                        "type": "durability",
                        "amount": 1
                    }
                }
            }
        }
    }

# Update all lightsabers
colors = ['blue', 'green', 'red', 'purple', 'yellow', 'white']

for color in colors:
    # Update hilt
    hilt_filename = f"{color}_hilt.json"
    hilt_filepath = os.path.join(items_dir, hilt_filename)
    hilt_data = create_simple_hilt(color)
    with open(hilt_filepath, 'w') as f:
        json.dump(hilt_data, f, indent=2)
    print(f"Updated {hilt_filename} - simple hilt")
    
    # Update active
    active_filename = f"{color}_active.json"
    active_filepath = os.path.join(items_dir, active_filename)
    active_data = create_simple_active(color)
    with open(active_filepath, 'w') as f:
        json.dump(active_data, f, indent=2)
    print(f"Updated {active_filename} - weapon")

print("\nAll lightsabers simplified!")
print("\nUse these commands to swap between hilt and active:")
print("Activate: /replaceitem entity @s slot.weapon.mainhand 0 lightsaber:blue_active")
print("Deactivate: /replaceitem entity @s slot.weapon.mainhand 0 lightsaber:blue_hilt")