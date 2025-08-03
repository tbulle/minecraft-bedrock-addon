import json
import os

# Path to the behavior pack items
items_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/items"

# List of lightsaber colors
colors = ["blue", "green", "purple", "red", "white", "yellow"]

def create_hilt_ararath_style(color):
    """Create hilt exactly like Ararath's gun format"""
    hilt_path = os.path.join(items_path, f"{color}_hilt.json")
    
    hilt_data = {
        "format_version": "1.20.50",
        "minecraft:item": {
            "description": {
                "identifier": f"lightsaber:{color}_hilt",
                "menu_category": {
                    "category": "equipment"  # Like the machete - equipment category
                }
            },
            "components": {
                "minecraft:tags": {
                    "tags": [
                        "lightsaber_hilt",
                        f"{color}_lightsaber",
                        "lightsaber"
                    ]
                },
                "minecraft:food": {
                    "can_always_eat": True
                },
                "minecraft:max_stack_size": 1,
                "minecraft:use_duration": 999999.0,
                "minecraft:hand_equipped": True,
                "minecraft:icon": {
                    "texture": f"{color}_hilt"
                },
                "minecraft:display_name": {
                    "value": f"item.lightsaber:{color}_hilt"
                },
                "minecraft:use_animation": "bow",
                "minecraft:on_use": {
                    "on_use": {
                        "event": f"lightsaber:activate",
                        "target": "self"
                    }
                },
                "minecraft:render_offsets": {
                    "main_hand": {
                        "first_person": {
                            "scale": [1.0, 1.0, 1.0]
                        },
                        "third_person": {
                            "scale": [1.0, 1.0, 1.0]
                        }
                    },
                    "off_hand": {
                        "first_person": {
                            "scale": [0.0, 0.0, 0.0]
                        },
                        "third_person": {
                            "scale": [0.0, 0.0, 0.0]
                        }
                    }
                }
            },
            "events": {
                "lightsaber:activate": {
                    "sequence": [
                        {
                            "condition": "!q.is_sprinting",
                            "run_command": {
                                "command": [
                                    f"function activate_{color}",
                                    "playsound random.levelup @a[r=10] ~ ~1 ~",
                                    f"scoreboard players set @s lightsaber_active 1"
                                ],
                                "target": "holder"
                            }
                        }
                    ]
                }
            }
        }
    }
    
    with open(hilt_path, 'w') as f:
        json.dump(hilt_data, f, indent=2)
    
    print(f"Created Ararath-style {color} hilt")

def create_active_ararath_style(color):
    """Create active lightsaber exactly like Ararath's machete format"""
    active_path = os.path.join(items_path, f"{color}_active.json")
    
    active_data = {
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
                        "lightsaber_active",
                        f"{color}_lightsaber",
                        "lightsaber",
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
                "minecraft:damage": 15,  # Higher than machete
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
                            "speed": 100,
                            "on_dig": {
                                "event": "lightsaber:hit"
                            }
                        },
                        {
                            "block": "minecraft:bamboo",
                            "speed": 100,
                            "on_dig": {
                                "event": "lightsaber:hit"
                            }
                        }
                    ]
                },
                "minecraft:weapon": {
                    "on_hurt_entity": {
                        "event": "lightsaber:hit"
                    }
                },
                "minecraft:render_offsets": {
                    "main_hand": {
                        "first_person": {
                            "scale": [1.0, 1.0, 1.0]
                        },
                        "third_person": {
                            "scale": [1.0, 1.0, 1.0]
                        }
                    },
                    "off_hand": {
                        "first_person": {
                            "scale": [0.0, 0.0, 0.0]
                        },
                        "third_person": {
                            "scale": [0.0, 0.0, 0.0]
                        }
                    }
                },
                # Add food component for deactivation
                "minecraft:food": {
                    "can_always_eat": True
                },
                "minecraft:use_animation": "bow",
                "minecraft:on_use": {
                    "on_use": {
                        "event": "lightsaber:deactivate",
                        "target": "self"
                    }
                }
            },
            "events": {
                "lightsaber:hit": {
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
                "lightsaber:deactivate": {
                    "sequence": [
                        {
                            "condition": "!q.is_sprinting",
                            "run_command": {
                                "command": [
                                    f"function deactivate_{color}",
                                    "playsound random.fizz @a[r=10] ~ ~1 ~",
                                    f"scoreboard players set @s lightsaber_active 0"
                                ],
                                "target": "holder"
                            }
                        }
                    ]
                }
            }
        }
    }
    
    with open(active_path, 'w') as f:
        json.dump(active_data, f, indent=2)
    
    print(f"Created Ararath-style {color} active lightsaber")

# Create all lightsabers
for color in colors:
    create_hilt_ararath_style(color)
    create_active_ararath_style(color)

print("\nAll lightsabers recreated using Ararath's exact format!")
print("\nKey features:")
print("- Hilts use food component for activation (like guns)")
print("- Active lightsabers are melee weapons (like machete)")
print("- Both appear in Equipment category")
print("- Proper weapon damage and durability")
print("- Hold right-click to activate/deactivate")