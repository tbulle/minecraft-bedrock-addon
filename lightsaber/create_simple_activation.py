import json

def create_simple_activation():
    colors = ['blue', 'green', 'red', 'purple', 'yellow', 'white']
    
    # Create a simple toggle function for each color
    for color in colors:
        toggle_function = f'''# Toggle {color} lightsaber
execute @s[hasitem={{item=lightsaber:{color}_hilt}}] ~ ~ ~ function lightsaber/activate_{color}
execute @s[hasitem={{item=lightsaber:{color}_active}}] ~ ~ ~ function lightsaber/deactivate_{color}'''
        
        with open(f'lightsaber_behavior_pack/functions/toggle_{color}.mcfunction', 'w') as f:
            f.write(toggle_function)
    
    # Create a master toggle function
    master_toggle = '''# Master lightsaber toggle
# Run this to activate/deactivate any held lightsaber

execute @s ~ ~ ~ function lightsaber/toggle_blue
execute @s ~ ~ ~ function lightsaber/toggle_green
execute @s ~ ~ ~ function lightsaber/toggle_red
execute @s ~ ~ ~ function lightsaber/toggle_purple
execute @s ~ ~ ~ function lightsaber/toggle_yellow
execute @s ~ ~ ~ function lightsaber/toggle_white

# Feedback
execute @s[hasitem={item=lightsaber:blue_active}] ~ ~ ~ title @s actionbar §bLightsaber Activated
execute @s[hasitem={item=lightsaber:green_active}] ~ ~ ~ title @s actionbar §aLightsaber Activated
execute @s[hasitem={item=lightsaber:red_active}] ~ ~ ~ title @s actionbar §cLightsaber Activated
execute @s[hasitem={item=lightsaber:purple_active}] ~ ~ ~ title @s actionbar §5Lightsaber Activated
execute @s[hasitem={item=lightsaber:yellow_active}] ~ ~ ~ title @s actionbar §eLightsaber Activated
execute @s[hasitem={item=lightsaber:white_active}] ~ ~ ~ title @s actionbar §fLightsaber Activated'''
    
    with open('lightsaber_behavior_pack/functions/toggle.mcfunction', 'w') as f:
        f.write(master_toggle)
    
    # Update the test function with instructions
    updated_test = '''# Test function to verify pack is loaded
say §eLightsaber Pack v1.0 Loaded Successfully!
say §aUse /function lightsaber/give_all to get all items

# Give starter items
give @s lightsaber:blue_hilt 1
give @s lightsaber:kyber_crystal_blue 2
give @s lightsaber:durasteel_ingot 4
give @s lightsaber:power_cell 1
give @s lightsaber:hilt_casing 1
give @s lightsaber:focusing_lens 1

# Instructions
tellraw @s {"rawtext":[{"text":"§b[Lightsaber] §fCraft lightsabers using kyber crystals!"}]}
tellraw @s {"rawtext":[{"text":"§b[Lightsaber] §fFind kyber crystals in End Cities and Strongholds"}]}
tellraw @s {"rawtext":[{"text":"§b[Lightsaber] §6To activate: Hold lightsaber and run §e/function lightsaber/toggle"}]}
tellraw @s {"rawtext":[{"text":"§b[Lightsaber] §6For quick toggle: Bind §e/function lightsaber/toggle §6to a hotkey!"}]}
tellraw @s {"rawtext":[{"text":"§b[Lightsaber] §fUse /function lightsaber/force_push for Force abilities"}]}'''
    
    with open('lightsaber_behavior_pack/functions/test.mcfunction', 'w') as f:
        f.write(updated_test)
    
    print("Created simple activation system!")
    print("\nTo use:")
    print("1. Hold a lightsaber hilt")
    print("2. Run: /function lightsaber/toggle")
    print("3. The lightsaber will activate/deactivate")

if __name__ == "__main__":
    create_simple_activation()