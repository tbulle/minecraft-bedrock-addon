import json
import os

# Path to the lightsaber items directory
items_dir = r"C:\Users\trull\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs\lightsaber\items"

# Template for active lightsaber as weapon
def create_weapon_template(color, damage=15):
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
                        "melee"
                    ]
                },
                "minecraft:icon": {
                    "texture": f"{color}_active"
                },
                "minecraft:max_stack_size": 1,
                "minecraft:use_duration": 2,
                "minecraft:hand_equipped": True,
                "minecraft:durability": {
                    "max_durability": 5000
                },
                "minecraft:mining_speed": 1.5,
                "minecraft:damage": damage,
                "minecraft:enchantable": {
                    "value": 14,
                    "slot": "sword"
                },
                "minecraft:can_destroy_in_creative": False,
                "minecraft:digger": {
                    "use_efficiency": True,
                    "destroy_speeds": [
                        {
                            "block": "minecraft:web",
                            "speed": 15,
                            "on_dig": {
                                "event": "minecraft:break"
                            }
                        },
                        {
                            "block": "minecraft:bamboo",
                            "speed": 10,
                            "on_dig": {
                                "event": "minecraft:break"
                            }
                        }
                    ]
                },
                "minecraft:weapon": {
                    "on_hurt_entity": {
                        "event": "minecraft:break"
                    }
                }
            },
            "events": {
                "minecraft:break": {
                    "sequence": [
                        {
                            "condition": "query.is_sprinting",
                            "sequence": [
                                {
                                    "damage": {
                                        "type": "durability",
                                        "amount": 2
                                    }
                                },
                                {
                                    "damage": {
                                        "type": "magic",
                                        "amount": 20,
                                        "target": "other"
                                    }
                                }
                            ]
                        },
                        {
                            "condition": "!query.is_sprinting",
                            "damage": {
                                "type": "durability",
                                "amount": 1
                            }
                        }
                    ]
                }
            }
        }
    }

# Update all active lightsabers
colors = ['blue', 'green', 'red', 'purple', 'yellow', 'white']

for color in colors:
    filename = f"{color}_active.json"
    filepath = os.path.join(items_dir, filename)
    
    # Create weapon data
    weapon_data = create_weapon_template(color)
    
    # Write the file
    with open(filepath, 'w') as f:
        json.dump(weapon_data, f, indent=2)
    
    print(f"Updated {filename} as simple weapon")

print("\nAll active lightsabers have been updated to be simple weapons!")
print("They will now:")
print("- Deal 15 damage (20 magic damage when sprinting)")
print("- Have 5000 durability")
print("- Be enchantable as swords")
print("- Cut through webs and bamboo quickly")
print("\nTo test: /give @s lightsaber:blue_active")