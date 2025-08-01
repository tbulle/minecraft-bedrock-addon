import json
import os

def create_lightsaber_items():
    colors = ['green', 'red', 'purple', 'yellow', 'white']
    
    # Create hilt and active items for each color
    for color in colors:
        # Hilt item
        hilt_data = {
            "format_version": "1.20.0",
            "minecraft:item": {
                "description": {
                    "identifier": f"lightsaber:{color}_hilt",
                    "menu_category": {
                        "category": "equipment"
                    }
                },
                "components": {
                    "minecraft:icon": {
                        "texture": f"{color}_hilt"
                    },
                    "minecraft:display_name": {
                        "value": f"item.lightsaber:{color}_hilt"
                    },
                    "minecraft:max_stack_size": 1,
                    "minecraft:hand_equipped": True,
                    "minecraft:use_duration": 32
                }
            }
        }
        
        # Active item
        active_data = {
            "format_version": "1.20.0",
            "minecraft:item": {
                "description": {
                    "identifier": f"lightsaber:{color}_active",
                    "menu_category": {
                        "category": "equipment",
                        "is_hidden_in_commands": True
                    }
                },
                "components": {
                    "minecraft:icon": {
                        "texture": f"{color}_active"
                    },
                    "minecraft:display_name": {
                        "value": f"item.lightsaber:{color}_active"
                    },
                    "minecraft:max_stack_size": 1,
                    "minecraft:hand_equipped": True,
                    "minecraft:damage": 30,
                    "minecraft:can_destroy_in_creative": False,
                    "minecraft:enchantable": {
                        "value": 1,
                        "slot": "sword"
                    }
                }
            }
        }
        
        # Kyber crystal
        crystal_data = {
            "format_version": "1.20.0",
            "minecraft:item": {
                "description": {
                    "identifier": f"lightsaber:kyber_crystal_{color}",
                    "menu_category": {
                        "category": "items"
                    }
                },
                "components": {
                    "minecraft:icon": {
                        "texture": f"kyber_crystal_{color}"
                    },
                    "minecraft:display_name": {
                        "value": f"item.lightsaber:kyber_crystal_{color}"
                    },
                    "minecraft:max_stack_size": 64
                }
            }
        }
        
        # Write files
        with open(f'lightsaber_behavior_pack/items/{color}_hilt.json', 'w') as f:
            json.dump(hilt_data, f, indent=2)
        
        with open(f'lightsaber_behavior_pack/items/{color}_active.json', 'w') as f:
            json.dump(active_data, f, indent=2)
            
        with open(f'lightsaber_behavior_pack/items/kyber_crystal_{color}.json', 'w') as f:
            json.dump(crystal_data, f, indent=2)
        
        # Create activation functions
        with open(f'lightsaber_behavior_pack/functions/activate_{color}.mcfunction', 'w') as f:
            f.write(f'''# Activate {color} lightsaber
playsound lightsaber.activate @s
clear @s lightsaber:{color}_hilt 0 1
give @s lightsaber:{color}_active
particle lightsaber:{color}_ignite ~ ~1 ~''')
        
        with open(f'lightsaber_behavior_pack/functions/deactivate_{color}.mcfunction', 'w') as f:
            f.write(f'''# Deactivate {color} lightsaber
playsound lightsaber.deactivate @s
clear @s lightsaber:{color}_active 0 1
give @s lightsaber:{color}_hilt
particle lightsaber:{color}_extinguish ~ ~1 ~''')

def create_component_items():
    components = {
        "durasteel_ingot": {
            "category": "items",
            "stack_size": 64
        },
        "power_cell": {
            "category": "items", 
            "stack_size": 16
        },
        "hilt_casing": {
            "category": "items",
            "stack_size": 64
        },
        "focusing_lens": {
            "category": "items",
            "stack_size": 64
        }
    }
    
    for name, props in components.items():
        item_data = {
            "format_version": "1.20.0",
            "minecraft:item": {
                "description": {
                    "identifier": f"lightsaber:{name}",
                    "menu_category": {
                        "category": props["category"]
                    }
                },
                "components": {
                    "minecraft:icon": {
                        "texture": name
                    },
                    "minecraft:display_name": {
                        "value": f"item.lightsaber:{name}"
                    },
                    "minecraft:max_stack_size": props["stack_size"]
                }
            }
        }
        
        with open(f'lightsaber_behavior_pack/items/{name}.json', 'w') as f:
            json.dump(item_data, f, indent=2)

if __name__ == "__main__":
    create_lightsaber_items()
    create_component_items()
    print("Created all item definitions!")