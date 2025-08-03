import json
import os

# Path to the lightsaber items directory
items_dir = r"C:\Users\trull\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs\lightsaber\items"

# Create hilt items with interact component
def create_hilt_with_interact(color):
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
                    "value": f"{color.capitalize()} Lightsaber Hilt"
                },
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True,
                "minecraft:interact_button": {
                    "text": "Activate"
                },
                "minecraft:on_use": {
                    "on_use": {
                        "event": "activate_lightsaber",
                        "target": "self"
                    }
                }
            },
            "events": {
                "activate_lightsaber": {
                    "run_command": {
                        "command": [
                            f"function toggle_{color}"
                        ],
                        "target": "holder"
                    }
                }
            }
        }
    }

# Update active lightsabers to deactivate on interact  
def create_active_with_deactivate(color):
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
                "minecraft:display_name": {
                    "value": f"{color.capitalize()} Lightsaber"
                },
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True,
                "minecraft:durability": {
                    "max_durability": 5000
                },
                "minecraft:mining_speed": 1.5,
                "minecraft:damage": 15,
                "minecraft:enchantable": {
                    "value": 14,
                    "slot": "sword"
                },
                "minecraft:can_destroy_in_creative": False,
                "minecraft:interact_button": {
                    "text": "Deactivate"
                },
                "minecraft:on_use": {
                    "on_use": {
                        "event": "deactivate_lightsaber",
                        "target": "self"
                    }
                },
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
                },
                "deactivate_lightsaber": {
                    "run_command": {
                        "command": [
                            f"function toggle_{color}"
                        ],
                        "target": "holder"
                    }
                }
            }
        }
    }

# Update all lightsaber items
colors = ['blue', 'green', 'red', 'purple', 'yellow', 'white']

for color in colors:
    # Update hilt
    hilt_filename = f"{color}_hilt.json"
    hilt_filepath = os.path.join(items_dir, hilt_filename)
    hilt_data = create_hilt_with_interact(color)
    with open(hilt_filepath, 'w') as f:
        json.dump(hilt_data, f, indent=2)
    print(f"Updated {hilt_filename}")
    
    # Update active
    active_filename = f"{color}_active.json"
    active_filepath = os.path.join(items_dir, active_filename)
    active_data = create_active_with_deactivate(color)
    with open(active_filepath, 'w') as f:
        json.dump(active_data, f, indent=2)
    print(f"Updated {active_filename}")

print("\nAll lightsabers updated with interact button activation!")
print("Activation should now work via the interact button prompt.")
print("\nTo test: /give @s lightsaber:blue_hilt")