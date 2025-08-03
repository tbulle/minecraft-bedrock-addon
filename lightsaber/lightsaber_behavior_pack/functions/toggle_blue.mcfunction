# Toggle blue lightsaber
execute @s[hasitem={item=lightsaber:blue_hilt}] ~ ~ ~ function lightsaber/activate_blue
execute @s[hasitem={item=lightsaber:blue_active}] ~ ~ ~ function lightsaber/deactivate_blue