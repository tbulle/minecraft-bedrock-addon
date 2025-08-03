# Toggle red lightsaber
execute @s[hasitem={item=lightsaber:red_hilt}] ~ ~ ~ function lightsaber/activate_red
execute @s[hasitem={item=lightsaber:red_active}] ~ ~ ~ function lightsaber/deactivate_red