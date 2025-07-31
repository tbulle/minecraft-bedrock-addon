# Check if player is wearing Spartan armor
# Reset armor count
scoreboard players set @s halo.armor_count 0

# Check each armor piece for Mark VI
execute as @s[hasitem={item=halo:spartan_mark_vi_helmet,location=slot.armor.head}] run scoreboard players add @s halo.armor_count 1
execute as @s[hasitem={item=halo:spartan_mark_vi_chestplate,location=slot.armor.chest}] run scoreboard players add @s halo.armor_count 1
execute as @s[hasitem={item=halo:spartan_mark_vi_leggings,location=slot.armor.legs}] run scoreboard players add @s halo.armor_count 1
execute as @s[hasitem={item=halo:spartan_mark_vi_boots,location=slot.armor.feet}] run scoreboard players add @s halo.armor_count 1

# Set Mark VI shield if full set
execute as @s[scores={halo.armor_count=4}] run scoreboard players set @s halo.shield_max 100
execute as @s[scores={halo.armor_count=4}] run scoreboard players set @s halo.has_spartan_armor 1

# Check for Mark V armor if not wearing Mark VI
execute as @s[scores={halo.armor_count=..3}] run scoreboard players set @s halo.armor_count 0
execute as @s[hasitem={item=halo:spartan_mark_v_helmet,location=slot.armor.head}] run scoreboard players add @s halo.armor_count 1
execute as @s[hasitem={item=halo:spartan_mark_v_chestplate,location=slot.armor.chest}] run scoreboard players add @s halo.armor_count 1
execute as @s[hasitem={item=halo:spartan_mark_v_leggings,location=slot.armor.legs}] run scoreboard players add @s halo.armor_count 1
execute as @s[hasitem={item=halo:spartan_mark_v_boots,location=slot.armor.feet}] run scoreboard players add @s halo.armor_count 1

# Set Mark V shield if full set
execute as @s[scores={halo.armor_count=4}] run scoreboard players set @s halo.shield_max 75
execute as @s[scores={halo.armor_count=4}] run scoreboard players set @s halo.has_spartan_armor 1

# Remove shields if not wearing full set
execute as @s[scores={halo.armor_count=..3}] run scoreboard players set @s halo.has_spartan_armor 0
execute as @s[scores={halo.has_spartan_armor=0}] run scoreboard players set @s halo.shield 0
execute as @s[scores={halo.has_spartan_armor=0}] run scoreboard players set @s halo.shield_max 0