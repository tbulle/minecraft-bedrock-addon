import os

# Path to functions
functions_path = "C:/Users/trull/AppData/Local/Packages/Microsoft.MinecraftUWP_8wekyb3d8bbwe/LocalState/games/com.mojang/development_behavior_packs/lightsaber/functions"

# Lightsaber colors
colors = ["blue", "green", "purple", "red", "white", "yellow"]

# Color codes for actionbar
color_codes = {
    "blue": "§b",
    "green": "§a", 
    "purple": "§d",
    "red": "§c",
    "white": "§f",
    "yellow": "§e"
}

for color in colors:
    # Skip blue since we already fixed it
    if color == "blue":
        continue
        
    # Create activation function
    activate_content = f"""# Activate {color} lightsaber
replaceitem entity @s slot.weapon.mainhand 0 lightsaber:{color}_active 1 0
playsound random.levelup @a[r=10] ~ ~ ~ 1 1
title @s actionbar §l{color_codes[color]}{color.capitalize()} Lightsaber Activated"""
    
    with open(os.path.join(functions_path, f"activate_{color}.mcfunction"), 'w') as f:
        f.write(activate_content)
    
    # Create deactivation function
    deactivate_content = f"""# Deactivate {color} lightsaber
replaceitem entity @s slot.weapon.mainhand 0 lightsaber:{color}_hilt 1 0
playsound random.fizz @a[r=10] ~ ~ ~ 1 1
title @s actionbar §l§7Lightsaber Deactivated"""
    
    with open(os.path.join(functions_path, f"deactivate_{color}.mcfunction"), 'w') as f:
        f.write(deactivate_content)
    
    print(f"Fixed {color} lightsaber functions")

print("\nAll activation functions updated to use replaceitem like Ararath's guns!")