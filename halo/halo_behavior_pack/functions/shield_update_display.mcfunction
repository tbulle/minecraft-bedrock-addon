# Update shield display on sidebar
# Calculate shield percentage
scoreboard players operation #shield_percent halo.shield_display = @s halo.shield
scoreboard players operation #shield_percent halo.shield_display *= #100 halo.shield_display
scoreboard players operation #shield_percent halo.shield_display /= @s halo.shield_max

# Update display with percentage
scoreboard players operation @s halo.shield_display = #shield_percent halo.shield_display

# Constants
scoreboard players set #100 halo.shield_display 100