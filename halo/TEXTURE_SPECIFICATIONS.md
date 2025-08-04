# Minecraft Bedrock Texture Specifications

## Based on Analysis of Zombie Apocalypse and Halo Add-ons

### Standard Texture Sizes and Properties

#### Item Textures
- **Standard Size**: 16×16 pixels (most common for handheld items)
- **Format**: PNG with transparency (RGBA)
- **Location**: `textures/items/`

#### Armor/Wearable Textures
- **Helmet Models**: 32×32 pixels (based on Halo helmet)
- **Full Armor Sets**: 64×32 or 64×64 pixels
- **Format**: PNG with transparency
- **Location**: `textures/models/armor/`

#### Entity Textures
Based on zombie apocalypse add-on structure:
- **Standard Zombies**: Various sizes, typically 64×64 or 128×128
- **Giant Zombies**: Larger textures for bigger models
- **Special Effects**: Separate textures for different states

#### Particle Textures
- **Small Particles**: 8×8 or 16×16 pixels
- **Effect Sprites**: 32×32 or 64×64 pixels
- **Format**: PNG with transparency for blending

### Texture Organization Structure

```
textures/
├── items/              # Item icons for inventory
│   ├── armor/          # Armor piece icons
│   ├── weapons/        # Weapon icons
│   └── tools/          # Tool icons
├── models/
│   └── armor/          # 3D model textures for worn armor
├── entities/           # Mob and entity textures
├── particles/          # Particle effect textures
└── blocks/            # Block textures
```

### Key Technical Requirements

1. **File Format**: PNG (Portable Network Graphics)
2. **Color Mode**: RGBA (Red, Green, Blue, Alpha channel)
3. **Bit Depth**: 8-bit per channel (32-bit total)
4. **Compression**: PNG standard compression
5. **Transparency**: Supported and commonly used

### Texture Definition Files

#### item_texture.json Structure
```json
{
  "resource_pack_name": "pack_name",
  "texture_name": "atlas.items",
  "texture_data": {
    "texture_id": {
      "textures": "textures/items/texture_file"
    }
  }
}
```

### Model Geometry Specifications

Based on Master Chief helmet:
- **Texture Width**: 32 pixels
- **Texture Height**: 32 pixels
- **UV Mapping**: Coordinates map to texture pixels
- **Visible Bounds**: Define rendering distance

### Best Practices

1. **Consistency**: Keep similar items at same resolution
2. **Power of 2**: Use dimensions that are powers of 2 (16, 32, 64, 128)
3. **Optimization**: Smaller textures for better performance
4. **Mipmapping**: Consider for larger textures
5. **Alpha Channel**: Use for transparency, avoid for opaque items

### Add-on Structure Observations

From encrypted marketplace content (Zombie Apocalypse):
- Premium content may be encrypted/obfuscated
- File structure remains standard
- Multiple texture variants for customization (angel, aqua, demon, etc.)
- Separate textures for different armor pieces

### Integration with Halo Add-on

The Master Chief helmet has been successfully integrated with:
- 32×32 pixel texture for the 3D model
- Proper UV mapping in geometry file
- Attachable definition for player rendering
- Item icon texture reference
- Netherite crafting recipe for balance

This provides a complete wearable helmet that matches the Halo theme while following Minecraft Bedrock's technical requirements.