# Check if player is wearing full ODST armor
scoreboard objectives add halo.odst_armor dummy
scoreboard players set @s halo.odst_armor 0

# Check each armor piece
execute as @s[hasitem={item=halo:odst_helmet,location=slot.armor.head}] run scoreboard players add @s halo.odst_armor 1
execute as @s[hasitem={item=halo:odst_chestplate,location=slot.armor.chest}] run scoreboard players add @s halo.odst_armor 1
execute as @s[hasitem={item=halo:odst_leggings,location=slot.armor.legs}] run scoreboard players add @s halo.odst_armor 1
execute as @s[hasitem={item=halo:odst_boots,location=slot.armor.feet}] run scoreboard players add @s halo.odst_armor 1

# Apply stealth effects if wearing full set
execute as @s[scores={halo.odst_armor=4}] run effect @s invisibility 1 0 true
execute as @s[scores={halo.odst_armor=4}] run effect @s speed 1 0 true

# Reduce mob detection range when crouching
execute as @s[scores={halo.odst_armor=4},tag=sneaking] run effect @s invisibility 1 1 true