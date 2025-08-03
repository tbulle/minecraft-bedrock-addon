import json
import os

# Path to the behavior pack items
items_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/items"

# List of lightsaber colors
colors = ["blue", "green", "purple", "red", "white", "yellow"]

def create_ararath_style_hilt(color):
    """Create hilt using Ararath's gun mod techniques"""
    hilt_path = os.path.join(items_path, f"{color}_hilt.json")
    
    hilt_data = {
        "format_version": "1.20.50",
        "minecraft:item": {
            "description": {
                "identifier": f"lightsaber:{color}_hilt",
                "menu_category": {
                    "category": "items",
                    "group": "itemGroup.name.skull"  # Groups with mob heads like Ararath's guns
                }
            },
            "components": {
                "minecraft:tags": {
                    "tags": [
                        "lightsaber",
                        f"{color}_lightsaber",
                        "lightsaber_hilt",
                        "can_activate"
                    ]
                },
                "minecraft:food": {
                    "can_always_eat": True
                },
                "minecraft:max_stack_size": 1,
                "minecraft:use_duration": 999999.0,  # Ararath's trick - extremely long duration
                "minecraft:cooldown": {
                    "duration": 0.5,
                    "category": "lightsaber_activation"
                },
                "minecraft:icon": {
                    "texture": f"{color}_hilt"
                },
                "minecraft:display_name": {
                    "value": f"item.lightsaber:{color}_hilt"
                },
                "minecraft:use_animation": "bow",
                "minecraft:hand_equipped": True,
                "minecraft:on_use": {
                    "on_use": {
                        "event": f"lightsaber:activate_{color}",
                        "target": "self"
                    }
                }
            },
            "events": {
                f"lightsaber:activate_{color}": {
                    "sequence": [
                        {
                            "condition": "!q.is_sprinting",  # Can't activate while sprinting
                            "run_command": {
                                "command": [
                                    f"give @s lightsaber:{color}_active",
                                    f"clear @s lightsaber:{color}_hilt 0 1",
                                    "playsound lightsaber.ignite @a[r=10] ~ ~ ~ 1 1",
                                    f"particle lightsaber:{color}_ignite ~ ~1 ~",
                                    f"event entity @s lightsaber:{color}_activated"
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

def create_ararath_style_active(color):
    """Create active lightsaber using Ararath's techniques"""
    active_path = os.path.join(items_path, f"{color}_active.json")
    
    active_data = {
        "format_version": "1.20.50",
        "minecraft:item": {
            "description": {
                "identifier": f"lightsaber:{color}_active",
                "menu_category": {
                    "category": "items",
                    "group": "itemGroup.name.skull",
                    "is_hidden_in_commands": True
                }
            },
            "components": {
                "minecraft:tags": {
                    "tags": [
                        "lightsaber",
                        f"{color}_lightsaber",
                        "lightsaber_active",
                        "melee_weapon",
                        "can_deactivate"
                    ]
                },
                "minecraft:food": {
                    "can_always_eat": True
                },
                "minecraft:max_stack_size": 1,
                "minecraft:use_duration": 999999.0,
                "minecraft:cooldown": {
                    "duration": 0.5,
                    "category": "lightsaber_activation"
                },
                "minecraft:enchantable": {
                    "slot": "sword",
                    "value": 10
                },
                "minecraft:icon": {
                    "texture": f"{color}_active"
                },
                "minecraft:display_name": {
                    "value": f"item.lightsaber:{color}_active"
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
                "minecraft:damage": 12,  # High damage
                "minecraft:use_animation": "bow",
                "minecraft:hand_equipped": True,
                "minecraft:on_use": {
                    "on_use": {
                        "event": f"lightsaber:deactivate_{color}",
                        "target": "self"
                    }
                },
                # Make it work like a weapon for breaking blocks
                "minecraft:digger": {
                    "use_efficiency": True,
                    "destroy_speeds": [
                        {
                            "block": "minecraft:web",
                            "speed": 100
                        },
                        {
                            "block": "minecraft:bamboo",
                            "speed": 100
                        }
                    ]
                }
            },
            "events": {
                f"lightsaber:deactivate_{color}": {
                    "sequence": [
                        {
                            "condition": "!q.is_sprinting",
                            "run_command": {
                                "command": [
                                    f"give @s lightsaber:{color}_hilt",
                                    f"clear @s lightsaber:{color}_active 0 1",
                                    "playsound lightsaber.extinguish @a[r=10] ~ ~ ~ 1 1",
                                    f"particle lightsaber:{color}_extinguish ~ ~1 ~",
                                    f"event entity @s lightsaber:{color}_deactivated"
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

# Update all lightsabers
for color in colors:
    create_ararath_style_hilt(color)
    create_ararath_style_active(color)

print("\nAll lightsabers updated using Ararath's gun mod techniques!")
print("\nKey improvements:")
print("- Uses food component with 999999 duration (never consumed)")
print("- Grouped with skull items in creative menu")
print("- Proper tag system for detection")
print("- Sequence-based events with conditions")
print("- Works reliably like Ararath's guns")
print("\nTo use:")
print("1. Hold right-click briefly to activate/deactivate")
print("2. The lightsaber will toggle states")
print("3. Active lightsabers deal 12 damage")