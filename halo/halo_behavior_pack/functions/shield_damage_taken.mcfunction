# Handle damage when player has shields
# Calculate damage amount
scoreboard players operation #damage halo.health = @s halo.prev_health
scoreboard players operation #damage halo.health -= @s halo.health

# Convert damage to shield damage (multiply by 10 for more granular shield system)
scoreboard players operation #damage halo.health *= #10 halo.health

# Apply damage to shields first
execute as @s[scores={halo.shield=1..}] run scoreboard players operation @s halo.shield -= #damage halo.health

# If shields broken
execute as @s[scores={halo.shield=..0}] at @s run playsound random.glass @a[distance=..10] ~ ~ ~ 1 0.5
execute as @s[scores={halo.shield=..0}] at @s run particle minecraft:critical_hit_emitter ~ ~1 ~ 0.5 0.5 0.5 0.1 20
execute as @s[scores={halo.shield=..0}] run tellraw @s {"rawtext":[{"text":"§c[Shield] §4Shields Down!"}]}

# Set minimum shield to 0
execute as @s[scores={halo.shield=..-1}] run scoreboard players set @s halo.shield 0

# Reset cooldown
scoreboard players set @s halo.shield_cooldown 60

# Constants
scoreboard players set #10 halo.health 10