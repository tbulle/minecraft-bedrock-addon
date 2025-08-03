# Toggle purple lightsaber
execute @s[hasitem={item=lightsaber:purple_hilt}] ~ ~ ~ function lightsaber/activate_purple
execute @s[hasitem={item=lightsaber:purple_active}] ~ ~ ~ function lightsaber/deactivate_purple