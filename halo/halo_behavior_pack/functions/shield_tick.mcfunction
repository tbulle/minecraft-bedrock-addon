# Main shield system tick function - runs every tick
# Check for Spartan armor on all players
execute as @a run function halo:shield_check_armor

# Process shield regeneration for players with Spartan armor
execute as @a[scores={halo.has_spartan_armor=1..,halo.shield_cooldown=0}] run function halo:shield_regenerate

# Decrease cooldown timer for players who took damage
execute as @a[scores={halo.shield_cooldown=1..}] run scoreboard players remove @s halo.shield_cooldown 1

# Update shield display
execute as @a[scores={halo.has_spartan_armor=1..}] run function halo:shield_update_display

# Check for damage and reset cooldown
execute as @a[scores={halo.has_spartan_armor=1..}] run function halo:shield_check_damage

# Apply shield effects
execute as @a[scores={halo.shield=1..}] at @s run particle minecraft:enchanting_table_particle ~ ~1 ~ 0.3 0.5 0.3 0.01 1 normal @s

# Check for ODST armor stealth benefits
execute as @a run function halo:odst_stealth_check