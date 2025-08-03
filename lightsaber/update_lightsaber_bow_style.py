import json
import os

def update_lightsaber_to_bow_style():
    colors = ['blue', 'green', 'red', 'purple', 'yellow', 'white']
    
    # Update hilt items to use bow-style activation
    for color in colors:
        hilt_path = f'lightsaber_behavior_pack/items/{color}_hilt.json'
        
        with open(hilt_path, 'r') as f:
            data = json.load(f)
        
        # Update components
        components = data['minecraft:item']['components']
        
        # Remove old use_duration if exists
        if 'minecraft:use_duration' in components:
            del components['minecraft:use_duration']
        
        # Add food component for continuous use
        components['minecraft:food'] = {
            "can_always_eat": True
        }
        
        # Add use animation
        components['minecraft:use_animation'] = "bow"
        
        # Add use duration for charging
        components['minecraft:use_duration'] = 32
        
        # Add cooldown to prevent spam
        components['minecraft:cooldown'] = {
            "duration": 0.5,
            "category": "lightsaber_activation"
        }
        
        # Update or add on_use component
        components['minecraft:on_use'] = {
            "on_use": {
                "event": f"lightsaber:activate_{color}",
                "target": "self"
            }
        }
        
        # Add events section
        data['minecraft:item']['events'] = {
            f"lightsaber:activate_{color}": {
                "run_command": {
                    "command": [
                        f"function lightsaber/activate_{color}",
                        "playsound random.orb @s ~ ~ ~ 1 1.5",
                        f"particle lightsaber:{color}_ignite ~ ~1 ~"
                    ],
                    "target": "holder"
                }
            }
        }
        
        with open(hilt_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    # Update active lightsabers for deactivation
    for color in colors:
        active_path = f'lightsaber_behavior_pack/items/{color}_active.json'
        
        with open(active_path, 'r') as f:
            data = json.load(f)
        
        components = data['minecraft:item']['components']
        
        # Add similar components for deactivation
        components['minecraft:food'] = {
            "can_always_eat": True
        }
        
        components['minecraft:use_animation'] = "bow"
        components['minecraft:use_duration'] = 32
        
        components['minecraft:cooldown'] = {
            "duration": 0.5,
            "category": "lightsaber_activation"
        }
        
        components['minecraft:on_use'] = {
            "on_use": {
                "event": f"lightsaber:deactivate_{color}",
                "target": "self"
            }
        }
        
        # Add throwable component for special attack
        components['minecraft:throwable'] = {
            "do_swing_animation": True,
            "launch_power_scale": 0.0,
            "max_launch_power": 0.0
        }
        
        # Add events
        data['minecraft:item']['events'] = {
            f"lightsaber:deactivate_{color}": {
                "run_command": {
                    "command": [
                        f"function lightsaber/deactivate_{color}",
                        "playsound random.orb @s ~ ~ ~ 1 0.5",
                        f"particle lightsaber:{color}_extinguish ~ ~1 ~"
                    ],
                    "target": "holder"
                }
            }
        }
        
        with open(active_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    print("Updated lightsabers to use bow-style activation!")
    print("\nHow it works now:")
    print("1. Hold a lightsaber hilt")
    print("2. Hold right-click (like drawing a bow)")
    print("3. After a short charge, it activates automatically!")
    print("4. Same process to deactivate")

if __name__ == "__main__":
    update_lightsaber_to_bow_style()