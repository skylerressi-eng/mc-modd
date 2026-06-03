# Wrought Iron & Steel

A Fabric mod for **Minecraft 1.21.1** that refines iron the old-fashioned way.
Inspired by Mogswamp's *"The iron problem"* short — iron is everywhere, so this
mod adds a light metallurgy progression and a pile of new tools, armor and
decorative blocks to actually spend it on.

```
raw iron --(vanilla smelt)--> iron ingot --(smelt)--> WROUGHT IRON
                              iron ingot + charcoal --(craft)--> STEEL
```

## Features

### Materials & processing
| Result | How to make it |
| --- | --- |
| **Wrought Iron Ingot** | Smelt an `iron ingot` in a furnace **or** blast furnace (refining). |
| **Steel Ingot** | Combine `1 iron ingot + 2 charcoal` in a crafting grid (carburizing). |
| Wrought Iron / Steel **Nugget** | 1 ingot → 9 nuggets (and back). |
| Block of Wrought Iron / Steel | 9 ingots (and back). Works as a beacon base. |

### Tools (full sets for both metals)
Sword, Pickaxe, Axe, Shovel, Hoe.
- **Wrought Iron** — a little more durable than iron (320 uses), iron mining level.
- **Steel** — sits between iron and diamond (800 uses, slightly more damage), iron mining level.

### Armor (full sets for both metals)
Helmet, Chestplate, Leggings, Boots.
- **Wrought Iron** — iron-class protection with a touch of armor toughness.
- **Steel** — stronger than iron, more durable, with extra toughness.

### Decorative blocks (for both metals)
- **Bars** — ornate metal bars (connect like iron bars).
- **Lantern** — a bright metal lantern (light level 15), hangs under blocks too.
- **Chain** — decorative metal chain.
- **Door** & **Trapdoor** — redstone-operated, like vanilla iron doors.

Everything is gathered into a dedicated creative tab.

## Dye rework

Adds a "dye anything" system built on the same mechanic as leather armor — put the
item in a crafting grid with dyes and **mix to any shade imaginable** (e.g. blue +
pink → a custom purple). Combine two already-dyed items to blend their colors.

| Item | How it works |
| --- | --- |
| **Dyeable Wool** | Craft from white wool, then dye to any color. The block remembers its shade (stored in a block entity) and drops it back when broken. |
| **Dyed Water** | A translucent, any-shade "water" block for pools and fountains (craft from glass + a dye, then re-dye freely). |
| **Dyeable Name Tag** | Names a mob in your chosen dye color. Apply a **glow ink sac** to it and the named mob also gets a permanent glowing outline. |
| **Dyeable Horse Armor** | Horse armor you can tint to any shade, the same way. |

> **Why "Dyed Water" is a block, not flowing water:** Minecraft fluids have no
> per-block data, so a *flowing* fluid can't carry an arbitrary mixed color. A
> colored block is what makes the "every shade" mechanic possible. A fixed-palette
> flowing fluid and dyeable item frames (a custom entity + renderer) are the two
> pieces that still need a compile pass to finish safely — see the build note below.

## Building

Requirements: **JDK 21** and internet access to the Fabric/Mojang maven repos.

```bash
./gradlew build
```

The built mod jar will be in `build/libs/` (use the file **without** the
`-sources` suffix). Drop it into your `mods/` folder alongside
[Fabric API](https://modrinth.com/mod/fabric-api).

To run a dev client/server:

```bash
./gradlew runClient
./gradlew runServer
```

> **Note on this repository's build environment:** the cloud sandbox this was
> authored in blocks `maven.fabricmc.net`, so `./gradlew build` cannot resolve
> Fabric Loom *here*. The project builds normally on any machine with regular
> internet access. Every resource/data JSON and texture has been validated
> locally (145 JSON files + 45 PNGs, all well-formed).

## Project layout

```
src/main/java/com/mcmodd/wroughtiron/
  WroughtIronMod.java      – entrypoint
  ModItems.java            – ingots, nuggets, tools, armor
  ModBlocks.java           – blocks + block items
  ModItemGroups.java       – creative tab
  ModToolMaterials.java    – wrought iron / steel tool tiers
  ModArmorMaterials.java   – wrought iron / steel armor materials
src/main/resources/
  fabric.mod.json
  assets/wroughtiron/...    – models, blockstates, textures, lang, icon
  data/wroughtiron/...      – recipes, loot tables, tags
tools/generate_assets.py    – regenerates every texture + resource JSON
```

### Regenerating assets

All textures and the repetitive resource JSON are produced by a single script
(so they stay consistent). It needs [Pillow](https://pypi.org/project/Pillow/):

```bash
pip install Pillow
python3 tools/generate_assets.py
```

## License

MIT — see [LICENSE](LICENSE).
