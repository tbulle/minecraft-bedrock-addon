# Force Jump ability - enhanced jump
# Execute from player holding active lightsaber

# Visual effect at feet
particle lightsaber:blue_trail ~ ~ ~
playsound lightsaber.activate @s ~ ~ ~ 0.5 1.5

# Give jump boost and slow falling
effect @s jump_boost 5 4 true
effect @s slow_falling 6 0 true

# Small levitation boost
effect @s levitation 1 5 true