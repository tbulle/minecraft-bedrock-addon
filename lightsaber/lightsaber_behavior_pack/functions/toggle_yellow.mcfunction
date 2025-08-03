# Toggle yellow lightsaber
execute @s[hasitem={item=lightsaber:yellow_hilt}] ~ ~ ~ function lightsaber/activate_yellow
execute @s[hasitem={item=lightsaber:yellow_active}] ~ ~ ~ function lightsaber/deactivate_yellow