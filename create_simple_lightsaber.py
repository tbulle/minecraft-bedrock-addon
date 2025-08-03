import json
import os

# Path to the behavior pack items
items_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/items"

# Create a simple blue hilt without food component
hilt_data = {
    "format_version": "1.20.50",
    "minecraft:item": {
        "description": {
            "identifier": "lightsaber:blue_hilt",
            "menu_category": {
                "category": "equipment"
            }
        },
        "components": {
            "minecraft:icon": {
                "texture": "blue_hilt"
            },
            "minecraft:display_name": {
                "value": "Blue Lightsaber Hilt"
            },
            "minecraft:max_stack_size": 1,
            "minecraft:hand_equipped": True,
            "minecraft:on_use": {
                "on_use": {
                    "event": "activate",
                    "target": "self"
                }
            }
        },
        "events": {
            "activate": {
                "swing": {},
                "run_command": {
                    "command": [
                        "clear @s lightsaber:blue_hilt 0 1",
                        "give @s lightsaber:blue_active 1",
                        "playsound random.levelup @s ~ ~ ~ 1 1.5"
                    ],
                    "target": "holder"
                }
            }
        }
    }
}

# Create active version
active_data = {
    "format_version": "1.20.50", 
    "minecraft:item": {
        "description": {
            "identifier": "lightsaber:blue_active",
            "menu_category": {
                "category": "equipment"
            }
        },
        "components": {
            "minecraft:icon": {
                "texture": "blue_active"
            },
            "minecraft:display_name": {
                "value": "Blue Lightsaber"
            },
            "minecraft:max_stack_size": 1,
            "minecraft:hand_equipped": True,
            "minecraft:damage": 15,
            "minecraft:durability": {
                "max_durability": 5000
            },
            "minecraft:weapon": {
                "on_hurt_entity": {
                    "event": "hit"
                }
            },
            "minecraft:enchantable": {
                "value": 14,
                "slot": "sword"
            },
            "minecraft:on_use": {
                "on_use": {
                    "event": "deactivate",
                    "target": "self"
                }
            }
        },
        "events": {
            "hit": {
                "damage": {
                    "type": "durability", 
                    "amount": 1
                }
            },
            "deactivate": {
                "swing": {},
                "run_command": {
                    "command": [
                        "clear @s lightsaber:blue_active 0 1",
                        "give @s lightsaber:blue_hilt 1",
                        "playsound random.fizz @s ~ ~ ~ 1 0.8"
                    ],
                    "target": "holder"
                }
            }
        }
    }
}

# Save files
with open(os.path.join(items_path, "blue_hilt.json"), 'w') as f:
    json.dump(hilt_data, f, indent=2)

with open(os.path.join(items_path, "blue_active.json"), 'w') as f:
    json.dump(active_data, f, indent=2)

print("Created simplified lightsaber without food component")
print("Activation is now instant on right-click")