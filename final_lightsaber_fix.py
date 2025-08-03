import json
import os

# Path to the behavior pack items
items_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/items"

# Create blue hilt EXACTLY like Ararath's gun structure
hilt_data = {
    "format_version": "1.20.50",
    "minecraft:item": {
        "description": {
            "identifier": "lightsaber:blue_hilt",
            "menu_category": {
                "category": "items",
                "group": "itemGroup.name.skull"
            }
        },
        "components": {
            "minecraft:tags": {
                "tags": [
                    "lightsaber", "blue_lightsaber", "lightsaber_hilt"
                ]
            },
            "minecraft:food": {
                "can_always_eat": True
            },
            "minecraft:max_stack_size": 1,
            "minecraft:use_duration": 999999.0,
            "minecraft:cooldown": {
                "duration": 0.2,
                "category": "lightsaber"
            },
            "minecraft:icon": {
                "texture": "blue_hilt"
            },
            "minecraft:display_name": {
                "value": "Blue Lightsaber Hilt"
            },
            "minecraft:on_use": {
                "on_use": {
                    "event": "lightsaber:activate",
                    "target": "self"
                }
            },
            "minecraft:hand_equipped": True,
            "minecraft:use_animation": "bow"
        },
        "events": {
            "lightsaber:activate": {
                "sequence": [
                    {
                        "condition": "!q.is_sprinting",
                        "run_command": {
                            "command": [
                                "function activate_blue",
                                "playsound random.levelup @a[r=10] ~ ~1 ~",
                                "event entity @s lightsaber:stop_use"
                            ],
                            "target": "holder"
                        }
                    }
                ]
            }
        }
    }
}

# Save the file
with open(os.path.join(items_path, "blue_hilt.json"), 'w') as f:
    json.dump(hilt_data, f, indent=2)

print("Created final blue hilt with Ararath's exact structure")

# Update the activation function to use replaceitem
activation_function = """# Activate blue lightsaber
replaceitem entity @s slot.weapon.mainhand 0 lightsaber:blue_active 1 0
title @s actionbar §l§bLightsaber Activated"""

functions_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/functions"
with open(os.path.join(functions_path, "activate_blue.mcfunction"), 'w') as f:
    f.write(activation_function)

print("Updated activation function to use replaceitem")