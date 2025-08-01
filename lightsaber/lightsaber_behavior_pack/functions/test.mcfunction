# Test function to verify pack is loaded
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
tellraw @s {"rawtext":[{"text":"§b[Lightsaber] §fUse /function lightsaber/force_push for Force abilities"}]}