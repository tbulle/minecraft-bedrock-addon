# Toggle white lightsaber
execute @s[hasitem={item=lightsaber:white_hilt}] ~ ~ ~ function lightsaber/activate_white
execute @s[hasitem={item=lightsaber:white_active}] ~ ~ ~ function lightsaber/deactivate_white