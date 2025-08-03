# Master lightsaber toggle
# Run this to activate/deactivate any held lightsaber

execute @s ~ ~ ~ function lightsaber/toggle_blue
execute @s ~ ~ ~ function lightsaber/toggle_green
execute @s ~ ~ ~ function lightsaber/toggle_red
execute @s ~ ~ ~ function lightsaber/toggle_purple
execute @s ~ ~ ~ function lightsaber/toggle_yellow
execute @s ~ ~ ~ function lightsaber/toggle_white

# Feedback
execute @s[hasitem={item=lightsaber:blue_active}] ~ ~ ~ title @s actionbar §bLightsaber Activated
execute @s[hasitem={item=lightsaber:green_active}] ~ ~ ~ title @s actionbar §aLightsaber Activated
execute @s[hasitem={item=lightsaber:red_active}] ~ ~ ~ title @s actionbar §cLightsaber Activated
execute @s[hasitem={item=lightsaber:purple_active}] ~ ~ ~ title @s actionbar §5Lightsaber Activated
execute @s[hasitem={item=lightsaber:yellow_active}] ~ ~ ~ title @s actionbar §eLightsaber Activated
execute @s[hasitem={item=lightsaber:white_active}] ~ ~ ~ title @s actionbar §fLightsaber Activated