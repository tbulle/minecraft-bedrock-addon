import json
import os

def create_recipes():
    # Component recipes
    recipes = []
    
    # Durasteel Ingot recipe
    recipes.append({
        "filename": "durasteel_ingot.json",
        "data": {
            "format_version": "1.20.0",
            "minecraft:recipe_shaped": {
                "description": {
                    "identifier": "lightsaber:durasteel_ingot"
                },
                "tags": ["crafting_table"],
                "pattern": [
                    "IOI",
                    "ONO",
                    "IOI"
                ],
                "key": {
                    "I": {
                        "item": "minecraft:iron_ingot"
                    },
                    "O": {
                        "item": "minecraft:obsidian"
                    },
                    "N": {
                        "item": "minecraft:netherite_scrap"
                    }
                },
                "result": {
                    "item": "lightsaber:durasteel_ingot",
                    "count": 2
                }
            }
        }
    })
    
    # Power Cell recipe
    recipes.append({
        "filename": "power_cell.json",
        "data": {
            "format_version": "1.20.0",
            "minecraft:recipe_shaped": {
                "description": {
                    "identifier": "lightsaber:power_cell"
                },
                "tags": ["crafting_table"],
                "pattern": [
                    "RGR",
                    "GBG",
                    "RGR"
                ],
                "key": {
                    "R": {
                        "item": "minecraft:redstone"
                    },
                    "G": {
                        "item": "minecraft:glowstone_dust"
                    },
                    "B": {
                        "item": "minecraft:redstone_block"
                    }
                },
                "result": {
                    "item": "lightsaber:power_cell",
                    "count": 1
                }
            }
        }
    })
    
    # Hilt Casing recipe
    recipes.append({
        "filename": "hilt_casing.json",
        "data": {
            "format_version": "1.20.0",
            "minecraft:recipe_shaped": {
                "description": {
                    "identifier": "lightsaber:hilt_casing"
                },
                "tags": ["crafting_table"],
                "pattern": [
                    "DDD",
                    "D D",
                    "DDD"
                ],
                "key": {
                    "D": {
                        "item": "lightsaber:durasteel_ingot"
                    }
                },
                "result": {
                    "item": "lightsaber:hilt_casing",
                    "count": 1
                }
            }
        }
    })
    
    # Focusing Lens recipe
    recipes.append({
        "filename": "focusing_lens.json",
        "data": {
            "format_version": "1.20.0",
            "minecraft:recipe_shaped": {
                "description": {
                    "identifier": "lightsaber:focusing_lens"
                },
                "tags": ["crafting_table"],
                "pattern": [
                    " D ",
                    "DGD",
                    " D "
                ],
                "key": {
                    "D": {
                        "item": "minecraft:diamond"
                    },
                    "G": {
                        "item": "minecraft:glass"
                    }
                },
                "result": {
                    "item": "lightsaber:focusing_lens",
                    "count": 1
                }
            }
        }
    })
    
    # Lightsaber recipes for each color
    colors = ['blue', 'green', 'red', 'purple', 'yellow', 'white']
    
    for color in colors:
        recipes.append({
            "filename": f"{color}_lightsaber.json",
            "data": {
                "format_version": "1.20.0",
                "minecraft:recipe_shaped": {
                    "description": {
                        "identifier": f"lightsaber:{color}_lightsaber"
                    },
                    "tags": ["crafting_table"],
                    "pattern": [
                        " K ",
                        "LHL",
                        " P "
                    ],
                    "key": {
                        "K": {
                            "item": f"lightsaber:kyber_crystal_{color}"
                        },
                        "L": {
                            "item": "lightsaber:focusing_lens"
                        },
                        "H": {
                            "item": "lightsaber:hilt_casing"
                        },
                        "P": {
                            "item": "lightsaber:power_cell"
                        }
                    },
                    "result": {
                        "item": f"lightsaber:{color}_hilt",
                        "count": 1
                    }
                }
            }
        })
    
    # Write all recipe files
    for recipe in recipes:
        filepath = f'lightsaber_behavior_pack/recipes/{recipe["filename"]}'
        with open(filepath, 'w') as f:
            json.dump(recipe["data"], f, indent=2)
    
    print(f"Created {len(recipes)} recipe files!")

if __name__ == "__main__":
    create_recipes()