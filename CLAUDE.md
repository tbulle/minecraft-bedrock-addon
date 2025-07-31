# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Minecraft Bedrock Edition Add-On development project.

## Project Structure

- `/halo` - Add-on directory (will contain behavior packs and resource packs)
- `/.claude/settings.local.json` - Claude Code settings file

## Minecraft Add-On Development

### Development Setup
1. Place packs in:
   - Windows: `C:\Users\<USERNAME>\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang`
   - `development_resource_packs/` for resource packs
   - `development_behavior_packs/` for behavior packs
2. Use `format_version: 2` in manifests
3. Generate unique UUIDs for each pack
4. Include `pack_icon.png` (128×128 recommended)
5. Enable Content Log for debugging

### Key File Types
- `.mcfunction` - Function files containing Minecraft commands
- `.json` - Manifest files, behavior definitions, animations, etc.
- `.lang` - Localization files (format: `item.namespace:id=Display Name`)
- `.mcstructure` - Structure files
- `.png` - Textures (16×16 recommended for blocks/items)

### Common Commands
When developing add-ons, useful commands include:
- Reloading behavior packs: `/reload`
- Testing functions: `/function <namespace:function_name>`
- Debugging entities: `/summon`, `/kill @e[type=...]`

### Resource Pack Structure
- **manifest.json** - Pack metadata with `resources` module
- **textures/**
  - `terrain_texture.json` - Block texture definitions
  - `item_texture.json` - Item texture definitions
  - `blocks/` - Block texture files
  - `items/` - Item texture files
- **texts/** - Localization files
  - `en_US.lang` - English translations
  - `languages.json` - Available languages
- **models/** - 3D models for entities and blocks
- **sounds/** - Audio files and definitions

### Behavior Pack Structure
- **manifest.json** - Pack metadata with `data` module
- **entities/** - Entity behavior definitions
  - Components: Pre-defined behaviors (e.g., `minecraft:can_climb`)
  - Component Groups: Custom groupings for dynamic behavior
  - Events: Add/remove component groups based on triggers
- **items/** - Item definitions
  - Use `minecraft:icon` component for texture linking
  - Include menu_category for creative inventory
- **blocks/** - Block behavior definitions
  - Use `minecraft:geometry` for shape
  - Use `minecraft:material_instances` for textures
- **functions/** - MCFunction command files
- **recipes/** - Crafting recipes

### Texture System
- **Blocks**: Define in `terrain_texture.json`
  - Uniform texture: `"*": { "texture": "namespace:block" }`
  - Per-face: Specify `down`, `up`, `north`, `east`, `south`, `west`
- **Items**: Define in `item_texture.json`
  - Link with `minecraft:icon` component in behavior pack
- **Recommended**: 16×16 pixels, PNG format

### Entity System
- **Components**: Hard-coded behaviors that can't be created
- **Component Groups**: Custom collections of components
- **Events**: Dynamic behavior changes
  ```json
  "events": {
      "namespace:event_name": {
          "add": { "component_groups": ["group_name"] },
          "remove": { "component_groups": ["other_group"] }
      }
  }
  ```

### Best Practices
1. **Always use Content Log** - Primary debugging tool
2. **Validate JSON** - Use JSON linters before testing
3. **Reference vanilla packs** - Download and study official packs
4. **Reload completely** - Close and reopen Minecraft to catch all errors
5. **Check file paths** - Most common source of errors
6. **Use proper namespacing** - `namespace:identifier` format
7. **Test incrementally** - Add features one at a time
8. **Create placeholder images** - Generate placeholder textures/icons when needed
   - Pack icons: 128×128 PNG
   - Block/item textures: 16×16 PNG
   - Entity textures: Varies by model
   - Use solid colors or simple patterns for testing

### Common Issues
- Missing textures: Check paths in texture JSON files
- Entity not spawning: Verify spawn rules and biome filters
- Commands not working: Check function syntax and permissions
- Pack not loading: Validate manifest.json and UUID uniqueness

### Development Workflow
1. Create pack folders with proper manifests
2. Add pack icon and basic metadata
3. Set up language files for localization
4. Build features incrementally
5. Use Content Log to debug issues
6. Test in a dedicated world with experiments enabled

## Official Microsoft Tools and Resources

### Recommended Development Environment
- **Visual Studio Code** - Official recommendation
- **VS Code Extensions**:
  - Blockception's Minecraft Bedrock Development
  - Bedrock Definitions
  - JSON validation support

### Official Creation Tools
1. **Minecraft Block Wizard** - Rapidly design and deploy custom blocks
2. **Minecraft Entity Wizard** - Blockbench plugin for custom entities
   - Provides presets for mob appearances
   - Guides through behavior selection
   - Generates spawn eggs
   - Exports complete resource and behavior packs
3. **Blockbench** - 3D model editor for Minecraft
   - Desktop and web versions available
   - Direct integration with Entity Wizard

### Advanced Development Features
- **Scripting APIs** - TypeScript support for dynamic content
- **Molang** - Expression language for entity programming
- **JSON Schemas** - Official validation for configuration files
- **Command-based mechanics** - Extend functionality with commands

### Content Creation Categories
- Custom Blocks with wizards
- Custom Entities with presets
- NPCs with dialogue
- Loot and Trading Tables
- Game Mechanics via commands

### Learning Resources
- Creator Learning Journey guide
- Scripting API Reference
- Vanilla Content Reference
- Official Microsoft Learn documentation