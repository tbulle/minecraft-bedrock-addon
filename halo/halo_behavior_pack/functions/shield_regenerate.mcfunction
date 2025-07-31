# Regenerate shields
# Add shield points up to max
execute as @s[scores={halo.shield=..98}] if score @s halo.shield < @s halo.shield_max run scoreboard players add @s halo.shield 2
execute as @s[scores={halo.shield=99}] if score @s halo.shield < @s halo.shield_max run scoreboard players add @s halo.shield 1

# Play regeneration sound when shields start charging
execute as @s[scores={halo.shield=2}] at @s run playsound random.orb @s ~ ~ ~ 0.5 2

# Play full shield sound
execute as @s if score @s halo.shield >= @s halo.shield_max at @s run playsound random.levelup @s ~ ~ ~ 0.5 1.5
execute as @s if score @s halo.shield >= @s halo.shield_max run tellraw @s {"rawtext":[{"text":"§b[Shield] §aShields Full"}]}

# Ensure shield doesn't exceed max
execute as @s if score @s halo.shield > @s halo.shield_max run scoreboard players operation @s halo.shield = @s halo.shield_max