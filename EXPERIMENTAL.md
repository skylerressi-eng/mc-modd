# Experimental branch: flowing fluid + dyeable item frames

This branch (`claude/dye-experimental`) adds the two dye features that are too API-heavy
to write safely without a compiler — and **this sandbox can't compile Fabric mods**
(`maven.fabricmc.net` is firewalled here). So treat everything in
`com.mcmodd.wroughtiron.experimental` as **best-effort and UNVERIFIED**: it follows the
standard 1.21.1 patterns, but expect to fix a mapping name or two on the first
`./gradlew build`. The stable features live on `claude/modest-dijkstra-3FctB`.

## What's here

### Flowing dyed water (custom fluid) — `ModFluids`, `DyedFluid`, `DyedWaterFluidBlock`
- Still + flowing `FlowableFluid`, a `FluidBlock`, and a `dyed_water_bucket`.
- Reuses vanilla water sprites with a **fixed** purple tint.
- **Known limitation:** fluids have no per-block data, so a *flowing* fluid can't carry an
  arbitrary mixed color. For "every shade" water, use the `dyed_water` *block* on the stable
  branch. This is the "real flowing water" version with one fixed color.

### Dyeable item frame — `ModFrames`, `DyeableItemFrameEntity`
- A custom item-frame entity that stores a color (tracked + saved to NBT) and a placement item.
- The **inventory item is tinted**; it's also in `#minecraft:dyeable` so its color mixes like
  leather armor.
- **Two hooks still TODO** (commented in the code):
  1. Copy the placed item's `dyed_color` onto the spawned entity (custom placement).
  2. Tint the frame model in a custom `ItemFrameEntityRenderer` subclass (it currently renders
     like a normal frame).

## How to finish / verify

1. Check out this branch and run `./gradlew build` (or `runClient`) on a machine with internet.
2. If it fails to compile, the likely spots are the `FlowableFluid` method signatures and the
   `EntityType.Builder` / `initDataTracker` calls — paste the errors and they're quick fixes.
3. Once it compiles, wire up the two item-frame rendering hooks above.

To merge into the stable mod later: `git merge claude/dye-experimental` once it builds clean.
