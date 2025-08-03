import json
import os

# Path to the lightsaber items directory
items_dir = r"C:\Users\trull\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\development_behavior_packs\lightsaber\items"

# Process all lightsaber item files
for filename in os.listdir(items_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(items_dir, filename)
        
        # Read the file
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Add food component and use_duration if not already present
        components = data['minecraft:item']['components']
        
        if 'minecraft:food' not in components:
            # Find position after icon or display_name
            new_components = {}
            for key, value in components.items():
                new_components[key] = value
                if key == 'minecraft:icon' or key == 'minecraft:display_name':
                    new_components['minecraft:food'] = {
                        "can_always_eat": True
                    }
                    new_components['minecraft:use_duration'] = 0.1
            
            # If food wasn't added yet (no icon or display_name), add it after max_stack_size
            if 'minecraft:food' not in new_components:
                newer_components = {}
                for key, value in new_components.items():
                    newer_components[key] = value
                    if key == 'minecraft:max_stack_size':
                        newer_components['minecraft:food'] = {
                            "can_always_eat": True
                        }
                        newer_components['minecraft:use_duration'] = 0.1
                new_components = newer_components
            
            data['minecraft:item']['components'] = new_components
        else:
            # Update existing use_duration
            components['minecraft:use_duration'] = 0.1
        
        # Write back
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Updated: {filename}")

print("\nAll lightsaber items have been updated with animation controller support!")
print("\nIMPORTANT: You need to reload the behavior pack in Minecraft for changes to take effect.")
print("Use /reload command or restart Minecraft.")