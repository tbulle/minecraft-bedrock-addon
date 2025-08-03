# Lightsaber Manual Activation Guide

Since Minecraft Bedrock has limitations with functions, here are alternative ways to use lightsabers:

## Method 1: Direct Commands (Works Now!)

### To Activate:
```
/clear @s lightsaber:blue_hilt 0 1
/give @s lightsaber:blue_active
```

### To Deactivate:
```
/clear @s lightsaber:blue_active 0 1  
/give @s lightsaber:blue_hilt
```

## Method 2: Command Block Setup

1. Place two command blocks
2. Set them to "Repeat" and "Always Active"
3. Add these commands:

**Command Block 1 (Activation):**
```
execute @a[hasitem={item=lightsaber:blue_hilt,location=slot.weapon.mainhand}] ~ ~ ~ give @s lightsaber:blue_active
execute @a[hasitem={item=lightsaber:blue_active}] ~ ~ ~ clear @s lightsaber:blue_hilt 0 1
```

**Command Block 2 (Deactivation with sneaking):**
```
execute @a[rxm=-90,rx=-60,hasitem={item=lightsaber:blue_active}] ~ ~ ~ give @s lightsaber:blue_hilt
execute @a[hasitem={item=lightsaber:blue_hilt}] ~ ~ ~ clear @s lightsaber:blue_active 0 1
```

## Method 3: Simple Swap Commands

Bind these to keys in Settings:
- Activate: `/give @s lightsaber:blue_active`
- Deactivate: `/give @s lightsaber:blue_hilt`

## All Color Commands:

### Blue Lightsaber
- Activate: `/clear @s lightsaber:blue_hilt 0 1` then `/give @s lightsaber:blue_active`
- Deactivate: `/clear @s lightsaber:blue_active 0 1` then `/give @s lightsaber:blue_hilt`

### Green Lightsaber  
- Activate: `/clear @s lightsaber:green_hilt 0 1` then `/give @s lightsaber:green_active`
- Deactivate: `/clear @s lightsaber:green_active 0 1` then `/give @s lightsaber:green_hilt`

### Red Lightsaber
- Activate: `/clear @s lightsaber:red_hilt 0 1` then `/give @s lightsaber:red_active`
- Deactivate: `/clear @s lightsaber:red_active 0 1` then `/give @s lightsaber:red_hilt`

### Purple Lightsaber
- Activate: `/clear @s lightsaber:purple_hilt 0 1` then `/give @s lightsaber:purple_active`
- Deactivate: `/clear @s lightsaber:purple_active 0 1` then `/give @s lightsaber:purple_hilt`

### Yellow Lightsaber
- Activate: `/clear @s lightsaber:yellow_hilt 0 1` then `/give @s lightsaber:yellow_active`
- Deactivate: `/clear @s lightsaber:yellow_active 0 1` then `/give @s lightsaber:yellow_hilt`

### White Lightsaber
- Activate: `/clear @s lightsaber:white_hilt 0 1` then `/give @s lightsaber:white_active`
- Deactivate: `/clear @s lightsaber:white_active 0 1` then `/give @s lightsaber:white_hilt`

## Working Features:
- ✅ 30 attack damage
- ✅ Instant mining for wood/leaves
- ✅ 5000 durability  
- ✅ Repairable with kyber crystals
- ✅ All crafting recipes work
- ✅ Found in End Cities and Strongholds