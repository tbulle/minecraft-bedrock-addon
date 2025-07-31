# Check if player took damage and handle shield depletion
# Store current health
scoreboard objectives add halo.health dummy
scoreboard objectives add halo.prev_health dummy

# Get current health
execute as @s store result score @s halo.health run data get entity @s Health

# Check if health decreased (took damage)
execute as @s if score @s halo.health < @s halo.prev_health run function halo:shield_damage_taken

# Update previous health for next tick
scoreboard players operation @s halo.prev_health = @s halo.health