import json
import os

def create_particle_effects():
    colors = {
        'blue': [0.4, 0.6, 1.0, 1.0],
        'green': [0.4, 1.0, 0.4, 1.0],
        'red': [1.0, 0.4, 0.4, 1.0],
        'purple': [0.8, 0.4, 1.0, 1.0],
        'yellow': [1.0, 1.0, 0.4, 1.0],
        'white': [1.0, 1.0, 1.0, 1.0]
    }
    
    effects = ['ignite', 'extinguish', 'trail', 'idle']
    
    all_particles = {}
    
    for color_name, color_values in colors.items():
        for effect in effects:
            particle_id = f"lightsaber:{color_name}_{effect}"
            
            if effect == 'ignite':
                particle_data = {
                    "format_version": "1.10.0",
                    "particle_effect": {
                        "description": {
                            "identifier": particle_id,
                            "basic_render_parameters": {
                                "material": "particles_alpha",
                                "texture": "textures/particle/particles"
                            }
                        },
                        "components": {
                            "minecraft:emitter_rate_instant": {
                                "num_particles": 20
                            },
                            "minecraft:emitter_lifetime_once": {
                                "active_time": 0.5
                            },
                            "minecraft:emitter_shape_sphere": {
                                "radius": 0.5,
                                "direction": "outwards"
                            },
                            "minecraft:particle_lifetime_expression": {
                                "max_lifetime": 0.8
                            },
                            "minecraft:particle_initial_speed": 3.0,
                            "minecraft:particle_motion_dynamic": {
                                "linear_acceleration": [0, -1, 0]
                            },
                            "minecraft:particle_appearance_billboard": {
                                "size": [0.1, 0.1],
                                "facing_camera_mode": "lookat_xyz",
                                "uv": {
                                    "texture_width": 128,
                                    "texture_height": 128,
                                    "uv": [0, 0],
                                    "uv_size": [8, 8]
                                }
                            },
                            "minecraft:particle_appearance_tinting": {
                                "color": color_values
                            }
                        }
                    }
                }
            
            elif effect == 'extinguish':
                particle_data = {
                    "format_version": "1.10.0",
                    "particle_effect": {
                        "description": {
                            "identifier": particle_id,
                            "basic_render_parameters": {
                                "material": "particles_alpha",
                                "texture": "textures/particle/particles"
                            }
                        },
                        "components": {
                            "minecraft:emitter_rate_instant": {
                                "num_particles": 10
                            },
                            "minecraft:emitter_lifetime_once": {
                                "active_time": 0.3
                            },
                            "minecraft:emitter_shape_point": {
                                "direction": [0, 1, 0]
                            },
                            "minecraft:particle_lifetime_expression": {
                                "max_lifetime": 0.5
                            },
                            "minecraft:particle_initial_speed": 2.0,
                            "minecraft:particle_motion_dynamic": {
                                "linear_acceleration": [0, 2, 0]
                            },
                            "minecraft:particle_appearance_billboard": {
                                "size": [0.08, 0.08],
                                "facing_camera_mode": "lookat_xyz",
                                "uv": {
                                    "texture_width": 128,
                                    "texture_height": 128,
                                    "uv": [0, 0],
                                    "uv_size": [8, 8]
                                }
                            },
                            "minecraft:particle_appearance_tinting": {
                                "color": color_values
                            }
                        }
                    }
                }
            
            elif effect == 'trail':
                particle_data = {
                    "format_version": "1.10.0",
                    "particle_effect": {
                        "description": {
                            "identifier": particle_id,
                            "basic_render_parameters": {
                                "material": "particles_alpha",
                                "texture": "textures/particle/particles"
                            }
                        },
                        "components": {
                            "minecraft:emitter_rate_steady": {
                                "spawn_rate": 50,
                                "max_particles": 100
                            },
                            "minecraft:emitter_lifetime_looping": {
                                "active_time": 1
                            },
                            "minecraft:emitter_shape_point": {},
                            "minecraft:particle_lifetime_expression": {
                                "max_lifetime": 0.3
                            },
                            "minecraft:particle_initial_speed": 0.1,
                            "minecraft:particle_appearance_billboard": {
                                "size": [0.05, 0.05],
                                "facing_camera_mode": "lookat_xyz",
                                "uv": {
                                    "texture_width": 128,
                                    "texture_height": 128,
                                    "uv": [0, 0],
                                    "uv_size": [8, 8]
                                }
                            },
                            "minecraft:particle_appearance_tinting": {
                                "color": [color_values[0], color_values[1], color_values[2], 0.5]
                            }
                        }
                    }
                }
            
            elif effect == 'idle':
                particle_data = {
                    "format_version": "1.10.0",
                    "particle_effect": {
                        "description": {
                            "identifier": particle_id,
                            "basic_render_parameters": {
                                "material": "particles_alpha",
                                "texture": "textures/particle/particles"
                            }
                        },
                        "components": {
                            "minecraft:emitter_rate_steady": {
                                "spawn_rate": 5,
                                "max_particles": 20
                            },
                            "minecraft:emitter_lifetime_looping": {
                                "active_time": 1
                            },
                            "minecraft:emitter_shape_sphere": {
                                "radius": 0.2
                            },
                            "minecraft:particle_lifetime_expression": {
                                "max_lifetime": 1.0
                            },
                            "minecraft:particle_initial_speed": 0.5,
                            "minecraft:particle_motion_dynamic": {
                                "linear_acceleration": [0, 0.5, 0]
                            },
                            "minecraft:particle_appearance_billboard": {
                                "size": [0.03, 0.03],
                                "facing_camera_mode": "lookat_xyz",
                                "uv": {
                                    "texture_width": 128,
                                    "texture_height": 128,
                                    "uv": [0, 0],
                                    "uv_size": [8, 8]
                                }
                            },
                            "minecraft:particle_appearance_tinting": {
                                "color": [color_values[0], color_values[1], color_values[2], 0.3]
                            }
                        }
                    }
                }
            
            # Write individual particle file
            filename = f'lightsaber_resource_pack/particles/{color_name}_{effect}.json'
            with open(filename, 'w') as f:
                json.dump(particle_data, f, indent=2)
    
    print(f"Created {len(colors) * len(effects)} particle effect files!")

if __name__ == "__main__":
    create_particle_effects()