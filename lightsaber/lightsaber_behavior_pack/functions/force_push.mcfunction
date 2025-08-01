# Force Push ability - pushes entities away
# Execute from player holding active lightsaber

# Visual effect
particle lightsaber:white_ignite ~ ~1 ~
playsound lightsaber.deflect @a ~ ~ ~ 1 0.5

# Push all entities within 5 blocks
execute as @e[r=5,type=!player] at @s run tp @s ~ ~ ~ facing entity @p
execute as @e[r=5,type=!player] at @s run tp @s ^ ^ ^-3

# Damage nearby hostile mobs
damage @e[r=5,family=monster] 5 magic entity @s

# Give player brief resistance
effect @s resistance 2 1 true