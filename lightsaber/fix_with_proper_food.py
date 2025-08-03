import json
import os

# Path to the lightsaber items directory
items_dir = r"C:\Users\trull\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs\lightsaber\items"

# Create hilt with PROPER food component like Ararath's
def create_proper_food_hilt(color):
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
                "minecraft:tags": {
                    "tags": [
                        f"{color}_hilt",
                        "lightsaber_hilt"
                    ]
                },
                "minecraft:icon": {
                    "texture": f"{color}_hilt"
                },
                "minecraft:display_name": {
                    "value": f"{color.capitalize()} Lightsaber Hilt"
                },
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True,
                "minecraft:food": {
                    "can_always_eat": True
                },
                "minecraft:use_duration": 999999.0,  # INFINITE like Ararath's
                "minecraft:use_animation": "bow",  # Bow animation like guns
                "minecraft:cooldown": {
                    "category": "lightsaber",
                    "duration": 0.5
                }
            }
        }
    }

# Create active WITHOUT food component (just weapon)
def create_weapon_active(color):
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
                "minecraft:tags": {
                    "tags": [
                        f"{color}_active",
                        "lightsaber_active"
                    ]
                },
                "minecraft:icon": {
                    "texture": f"{color}_active"
                },
                "minecraft:display_name": {
                    "value": f"{color.capitalize()} Lightsaber"
                },
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True,
                "minecraft:damage": 15,
                "minecraft:durability": {
                    "max_durability": 5000
                },
                "minecraft:enchantable": {
                    "value": 14,
                    "slot": "sword"
                },
                "minecraft:weapon": {
                    "on_hurt_entity": {
                        "event": "damage_dealt"
                    }
                },
                "minecraft:food": {
                    "can_always_eat": True
                },
                "minecraft:use_duration": 999999.0,  # INFINITE for deactivation
                "minecraft:use_animation": "bow",
                "minecraft:cooldown": {
                    "category": "lightsaber",
                    "duration": 0.5
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
    hilt_data = create_proper_food_hilt(color)
    with open(hilt_filepath, 'w') as f:
        json.dump(hilt_data, f, indent=2)
    print(f"Updated {hilt_filename} with infinite food duration")
    
    # Update active
    active_filename = f"{color}_active.json"
    active_filepath = os.path.join(items_dir, active_filename)
    active_data = create_weapon_active(color)
    with open(active_filepath, 'w') as f:
        json.dump(active_data, f, indent=2)
    print(f"Updated {active_filename} with infinite food duration")

print("\nAll lightsabers updated with proper food component!")
print("Now we need to add animation controllers to detect usage...")