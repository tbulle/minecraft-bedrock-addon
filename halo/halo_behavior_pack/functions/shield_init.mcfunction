# Initialize shield system for all players
scoreboard objectives add halo.shield dummy "Halo Shield HP"
scoreboard objectives add halo.shield_max dummy "Halo Max Shield HP"
scoreboard objectives add halo.shield_cooldown dummy "Shield Recharge Cooldown"
scoreboard objectives add halo.shield_regen dummy "Shield Regen Rate"
scoreboard objectives add halo.has_spartan_armor dummy "Has Spartan Armor"
scoreboard objectives add halo.armor_count dummy "Spartan Armor Count"

# Set default values
scoreboard players set @a halo.shield 0
scoreboard players set @a halo.shield_max 0
scoreboard players set @a halo.shield_cooldown 0
scoreboard players set @a halo.shield_regen 0
scoreboard players set @a halo.has_spartan_armor 0

# Create shield display
scoreboard objectives add halo.shield_display dummy "§b§lShield"
scoreboard objectives setdisplay sidebar halo.shield_display

# Constants
scoreboard players set #shield_cooldown_time halo.shield_cooldown 60
scoreboard players set #shield_regen_rate halo.shield_regen 2
scoreboard players set #mkvi_shield_max halo.shield_max 100
scoreboard players set #mkv_shield_max halo.shield_max 75

tellraw @a {"rawtext":[{"text":"§b[Halo] §fShield system initialized"}]}