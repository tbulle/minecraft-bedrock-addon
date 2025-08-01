import json
import os

def update_active_lightsabers():
    colors = ['blue', 'green', 'red', 'purple', 'yellow', 'white']
    
    for color in colors:
        filepath = f'lightsaber_behavior_pack/items/{color}_active.json'
        
        # Read existing file
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Add combat enhancements
        components = data['minecraft:item']['components']
        
        # Add mining capabilities
        components['minecraft:digger'] = {
            "use_efficiency": True,
            "destroy_speeds": [
                {
                    "block": "minecraft:wool",
                    "speed": 100
                },
                {
                    "block": "minecraft:leaves",
                    "speed": 100
                },
                {
                    "block": "minecraft:leaves2",
                    "speed": 100
                },
                {
                    "block": "minecraft:log",
                    "speed": 50
                },
                {
                    "block": "minecraft:log2",
                    "speed": 50
                },
                {
                    "block": "minecraft:planks",
                    "speed": 50
                },
                {
                    "block": "minecraft:web",
                    "speed": 100
                },
                {
                    "block": "minecraft:bamboo",
                    "speed": 100
                }
            ]
        }
        
        # Add durability (high)
        components['minecraft:durability'] = {
            "max_durability": 5000,
            "damage_chance": {
                "min": 0,
                "max": 1
            }
        }
        
        # Add repairable component
        components['minecraft:repairable'] = {
            "repair_items": [
                {
                    "items": [f"lightsaber:kyber_crystal_{color}"],
                    "repair_amount": 1000
                }
            ]
        }
        
        # Write updated file
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    print("Updated combat mechanics for all lightsabers!")

if __name__ == "__main__":
    update_active_lightsabers()