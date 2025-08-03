import json
import os

def fix_lightsaber_activation():
    colors = ['blue', 'green', 'red', 'purple', 'yellow', 'white']
    
    # Update hilt items to use interact button
    for color in colors:
        hilt_path = f'lightsaber_behavior_pack/items/{color}_hilt.json'
        
        with open(hilt_path, 'r') as f:
            data = json.load(f)
        
        # Update components for activation
        components = data['minecraft:item']['components']
        
        # Remove use_duration, add food component as workaround
        if 'minecraft:use_duration' in components:
            del components['minecraft:use_duration']
        
        # Add food component that triggers instantly
        components['minecraft:food'] = {
            "nutrition": 0,
            "saturation_modifier": "none",
            "can_always_eat": True,
            "on_consume": {
                "event": f"lightsaber:activate_{color}",
                "target": "self"
            }
        }
        
        # Add events section
        data['minecraft:item']['events'] = {
            f"lightsaber:activate_{color}": {
                "run_command": {
                    "command": [
                        f"/function lightsaber/activate_{color}",
                        "/playsound random.eat @s"
                    ],
                    "target": "self"
                }
            }
        }
        
        with open(hilt_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    # Update active items for deactivation
    for color in colors:
        active_path = f'lightsaber_behavior_pack/items/{color}_active.json'
        
        with open(active_path, 'r') as f:
            data = json.load(f)
        
        components = data['minecraft:item']['components']
        
        # Add food component for deactivation
        components['minecraft:food'] = {
            "nutrition": 0,
            "saturation_modifier": "none", 
            "can_always_eat": True,
            "on_consume": {
                "event": f"lightsaber:deactivate_{color}",
                "target": "self"
            }
        }
        
        # Add events
        data['minecraft:item']['events'] = {
            f"lightsaber:deactivate_{color}": {
                "run_command": {
                    "command": [
                        f"/function lightsaber/deactivate_{color}",
                        "/playsound random.eat @s"
                    ],
                    "target": "self"
                }
            }
        }
        
        with open(active_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    print("Fixed activation system!")

if __name__ == "__main__":
    fix_lightsaber_activation()