import json
import os
import shutil

# Paths
ararath_items = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/behavior_packs/Arath'sGun/items/guns/glock_17/default"
lightsaber_items = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/items"

# Step 1: Copy glock_17 as blue_hilt
glock_path = os.path.join(ararath_items, "glock_17.json")
with open(glock_path, 'r') as f:
    gun_data = json.load(f)

# Modify to lightsaber hilt
gun_data["minecraft:item"]["description"]["identifier"] = "lightsaber:blue_hilt"
gun_data["minecraft:item"]["components"]["minecraft:display_name"]["value"] = "Blue Lightsaber Hilt"
gun_data["minecraft:item"]["components"]["minecraft:icon"]["texture"] = "blue_hilt"

# Update tags
gun_data["minecraft:item"]["components"]["minecraft:tags"]["tags"] = [
    "new_gun",  # Keep this tag since it might be needed
    "lightsaber_hilt",
    "blue_lightsaber",
    "lightsaber"
]

# Modify the shoot event to activate lightsaber
gun_data["minecraft:item"]["events"] = {
    "gunsaddon:shoot": {  # Keep the original event name
        "sequence": [
            {
                "condition": "!q.is_sprinting",
                "run_command": {
                    "command": [
                        "replaceitem entity @s slot.weapon.mainhand 0 lightsaber:blue_active 1 0",
                        "playsound random.levelup @a[r=10] ~ ~1 ~",
                        "title @s actionbar §l§bLightsaber Activated"
                    ],
                    "target": "holder"
                }
            }
        ]
    }
}

# Save blue hilt
with open(os.path.join(lightsaber_items, "blue_hilt.json"), 'w') as f:
    json.dump(gun_data, f, indent=2)

print("Created blue_hilt based on glock_17")

# Step 2: Copy glock_17_empty as blue_active
glock_empty_path = os.path.join(ararath_items, "glock_17_empty.json")
with open(glock_empty_path, 'r') as f:
    empty_data = json.load(f)

# Modify to active lightsaber
empty_data["minecraft:item"]["description"]["identifier"] = "lightsaber:blue_active"
empty_data["minecraft:item"]["components"]["minecraft:display_name"]["value"] = "Blue Lightsaber"
empty_data["minecraft:item"]["components"]["minecraft:icon"]["texture"] = "blue_active"

# Update tags
empty_data["minecraft:item"]["components"]["minecraft:tags"]["tags"] = [
    "new_gun",  # Keep this
    "lightsaber_active",
    "blue_lightsaber",
    "lightsaber",
    "empty"  # Keep empty tag
]

# Add weapon properties
empty_data["minecraft:item"]["components"]["minecraft:damage"] = 15
empty_data["minecraft:item"]["components"]["minecraft:enchantable"] = {
    "value": 14,
    "slot": "sword"
}

# Add durability instead of reload
empty_data["minecraft:item"]["components"]["minecraft:durability"] = {
    "max_durability": 5000
}

# Remove stacked_by_data if present
if "minecraft:stacked_by_data" in empty_data["minecraft:item"]["components"]:
    del empty_data["minecraft:item"]["components"]["minecraft:stacked_by_data"]

# Change reload event to deactivate
if "minecraft:on_use" in empty_data["minecraft:item"]["components"]:
    empty_data["minecraft:item"]["components"]["minecraft:on_use"]["on_use"]["event"] = "gunsaddon:deactivate"

# Add deactivate event
empty_data["minecraft:item"]["events"] = {
    "gunsaddon:deactivate": {
        "run_command": {
            "command": [
                "replaceitem entity @s slot.weapon.mainhand 0 lightsaber:blue_hilt 1 0",
                "playsound random.fizz @a[r=10] ~ ~1 ~",
                "title @s actionbar §l§7Lightsaber Deactivated"
            ],
            "target": "holder"
        }
    }
}

# Save blue active
with open(os.path.join(lightsaber_items, "blue_active.json"), 'w') as f:
    json.dump(empty_data, f, indent=2)

print("Created blue_active based on glock_17_empty")
print("\nLightsaber created using Ararath's exact gun structure!")
print("The activation should work exactly like the guns now.")