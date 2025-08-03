# Lightsaber Activation Fix

## Problem
The lightsabers weren't activating because Minecraft Bedrock's `minecraft:on_use` event doesn't trigger properly without additional player entity modifications.

## Solution
Based on how Ararath's gun mod works, I've added:

1. **Player Entity Modification** (`entities/player.json`)
   - Adds animation controller reference to the player entity
   - This allows the game to detect when items are being used

2. **Animation Controller** (`animation_controllers/lightsaber_activation.json`)
   - Detects when a lightsaber is being used (`q.is_using_item`)
   - Runs the appropriate commands to swap items
   - Handles both activation (hilt → active) and deactivation (active → hilt)

3. **Item Updates**
   - Added `minecraft:food` component with `can_always_eat: true`
   - Added `minecraft:use_duration: 0.1` (short duration for quick activation)
   - This combination allows the animation controller to detect item use

## How It Works
1. When you right-click with a hilt, the animation controller detects `q.is_using_item`
2. It triggers the appropriate state transition based on the equipped item
3. The `on_entry` commands swap the item and play a sound
4. When you release, it returns to the default state

## Testing
1. Reload the behavior pack with `/reload` command
2. Get a lightsaber hilt (e.g., `/give @s lightsaber:blue_hilt`)
3. Right-click to activate/deactivate

## Key Differences from Previous Attempts
- **Player entity modification**: This was the missing piece - Ararath's items work because the mod modifies the player entity
- **Animation controller**: More reliable than relying on item events alone
- **Food component**: Enables the `q.is_using_item` query to work properly