# Lightsaber Add-on Design Plan

## Core Concept
A lightsaber system that mimics Star Wars lightsabers with activation/deactivation mechanics, multiple colors, and authentic combat features.

## 1. **Item System Design**
- **Two-state system**: Inactive hilt → Active lightsaber
- **Activation method**: Right-click/use to toggle on/off
- **Implementation approach**: 
  - Use custom item components
  - Swap between two items (hilt and active saber) on use
  - Store activation state using item tags

## 2. **Lightsaber Variants**
- **Colors**: Blue, Green, Red, Purple, Yellow, White
- **Each variant has**:
  - Unique hilt item
  - Unique active saber item
  - Color-matched particle effects
  - Lore-appropriate names (Jedi/Sith variants)

## 3. **Combat Mechanics**
- **Damage**: 20-30 attack damage (instant kill most mobs)
- **Projectile deflection**: 
  - Detect nearby projectiles
  - Reflect arrows/tridents back at attackers
  - Use entity events and components
- **Durability**: Unbreakable or very high durability

## 4. **Visual Effects**
- **Glowing blade**: Custom 3D model with emissive textures
- **Particle trails**: Color-matched particles on swing
- **Activation effect**: Burst of particles on ignition
- **Idle glow**: Ambient particles while active

## 5. **Sound Design**
- **Activation**: Classic snap-hiss sound
- **Idle hum**: Continuous ambient sound while active
- **Swing**: Whoosh sounds on attack
- **Clash**: Impact sounds when hitting entities/blocks
- **Deactivation**: Retraction sound

## 6. **Special Mechanics**
- **Block cutting**: Instant break for wood/leaves/wool
- **Light emission**: Acts as light source when active
- **Shield bypass**: Ignores shield blocking

## 7. **Crafting System**
- **Components**:
  - Kyber Crystal (rare drop or End Cities)
  - Durasteel Ingot (iron + obsidian)
  - Power Cell (redstone + glowstone)
  - Hilt Casing (gold/iron variant)
- **Assembly**: Crafting table recipe combining components

## 8. **Technical Implementation**
- **Resource Pack**: Models, textures, sounds, particles
- **Behavior Pack**: Items, recipes, combat mechanics
- **Animation controllers**: Handle state transitions
- **Molang expressions**: For particle effects and animations