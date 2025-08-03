# Simplified sneak activation
# Double-sneak (crouch twice quickly) to toggle lightsaber

# Increment sneak counter when sneaking
scoreboard objectives add sneak_time dummy
scoreboard objectives add lightsaber_cooldown dummy

# Detect sneaking and count
execute @a[scores={sneak_time=..20}] ~ ~ ~ detect ~ ~-0.3 ~ air 0 scoreboard players add @s sneak_time 0
execute @a ~ ~ ~ detect ~ ~-0.3 ~ air -1 scoreboard players add @s[scores={sneak_time=..20}] sneak_time 1
execute @a ~ ~ ~ detect ~ ~-0.3 ~ air 0 scoreboard players set @s[scores={sneak_time=1..}] sneak_time 0

# Toggle on sneak
execute @a[scores={sneak_time=10,lightsaber_cooldown=0}] ~ ~ ~ function lightsaber/toggle
execute @a[scores={sneak_time=10}] ~ ~ ~ scoreboard players set @s lightsaber_cooldown 30

# Cooldown
scoreboard players remove @a[scores={lightsaber_cooldown=1..}] lightsaber_cooldown 1