import json

def add_force_projectiles():
    colors = ['blue', 'green', 'red', 'purple', 'yellow', 'white']
    
    for color in colors:
        active_path = f'lightsaber_behavior_pack/items/{color}_active.json'
        
        with open(active_path, 'r') as f:
            data = json.load(f)
        
        # Update the deactivate event to include sneak detection
        events = data['minecraft:item']['events']
        
        # Replace the simple deactivate with a sequence
        events[f"lightsaber:deactivate_{color}"] = {
            "sequence": [
                {
                    "condition": "!q.is_sneaking",
                    "run_command": {
                        "command": [
                            f"function lightsaber/deactivate_{color}",
                            "playsound random.orb @s ~ ~ ~ 1 0.5",
                            f"particle lightsaber:{color}_extinguish ~ ~1 ~"
                        ],
                        "target": "holder"
                    }
                },
                {
                    "condition": "q.is_sneaking",
                    "sequence": [
                        {
                            "run_command": {
                                "command": [
                                    "playsound random.explode @a[r=16] ~ ~ ~ 0.5 1.5",
                                    f"particle lightsaber:{color}_ignite ~ ~1 ~",
                                    "effect @s slowness 1 2 true"
                                ],
                                "target": "holder"
                            }
                        },
                        {
                            "shoot": {
                                "projectile": "lightsaber:force_push",
                                "launch_power": 1.5
                            }
                        }
                    ]
                }
            ]
        }
        
        with open(active_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    print("Added force push projectiles!")
    print("\nNew controls:")
    print("- Hold right-click: Toggle lightsaber on/off")
    print("- Sneak + Hold right-click: Shoot force push!")

if __name__ == "__main__":
    add_force_projectiles()