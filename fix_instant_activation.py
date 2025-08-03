import json
import os

# Path to the behavior pack items
items_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/items"

# Just fix blue for testing
hilt_path = os.path.join(items_path, "blue_hilt.json")

with open(hilt_path, 'r') as f:
    data = json.load(f)

# Change use_duration to be very short for instant activation
data["minecraft:item"]["components"]["minecraft:use_duration"] = 0.1

# Simplify the event to directly swap items
data["minecraft:item"]["events"]["lightsaber:activate"] = {
    "run_command": {
        "command": [
            "give @s lightsaber:blue_active 1",
            "clear @s lightsaber:blue_hilt 0 1",
            "playsound random.levelup @s ~ ~ ~ 1 1",
            "title @s actionbar §l§bLightsaber Activated"
        ],
        "target": "holder"
    }
}

with open(hilt_path, 'w') as f:
    json.dump(data, f, indent=2)

print("Fixed blue hilt for instant activation")

# Also fix the active lightsaber
active_path = os.path.join(items_path, "blue_active.json")

with open(active_path, 'r') as f:
    data = json.load(f)

# Change use_duration to be short
data["minecraft:item"]["components"]["minecraft:use_duration"] = 0.1

# Fix deactivation
data["minecraft:item"]["events"]["lightsaber:deactivate"] = {
    "run_command": {
        "command": [
            "give @s lightsaber:blue_hilt 1", 
            "clear @s lightsaber:blue_active 0 1",
            "playsound random.fizz @s ~ ~ ~ 1 1",
            "title @s actionbar §l§7Lightsaber Deactivated"
        ],
        "target": "holder"
    }
}

with open(active_path, 'w') as f:
    json.dump(data, f, indent=2)

print("Fixed blue active for instant deactivation")