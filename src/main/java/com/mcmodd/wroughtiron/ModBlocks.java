package com.mcmodd.wroughtiron;

import net.minecraft.block.AbstractBlock;
import net.minecraft.block.Block;
import net.minecraft.block.BlockSetType;
import net.minecraft.block.ChainBlock;
import net.minecraft.block.DoorBlock;
import net.minecraft.block.LanternBlock;
import net.minecraft.block.PaneBlock;
import net.minecraft.block.TrapdoorBlock;
import net.minecraft.item.BlockItem;
import net.minecraft.item.Item;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.sound.BlockSoundGroup;
import net.minecraft.util.Identifier;

/**
 * All blocks added by the mod (and their matching block items): a storage block, ornate bars, a
 * lantern, a chain, a door and a trapdoor, for both wrought iron and steel.
 *
 * <p>Doors and trapdoors use {@link BlockSetType#IRON} so, like vanilla iron doors, they can only be
 * toggled by redstone &mdash; fitting for heavy metal fixtures.
 */
public final class ModBlocks {
	// ----- Wrought iron -----
	public static final Block WROUGHT_IRON_BLOCK = register("wrought_iron_block",
			new Block(metal().strength(5.0F, 6.0F)), true);
	public static final Block WROUGHT_IRON_BARS = register("wrought_iron_bars",
			new PaneBlock(metal().strength(5.0F, 6.0F).nonOpaque()), true);
	public static final Block WROUGHT_IRON_LANTERN = register("wrought_iron_lantern",
			new LanternBlock(AbstractBlock.Settings.create().requiresTool().strength(3.5F)
					.sounds(BlockSoundGroup.LANTERN).luminance(state -> 15).nonOpaque()), true);
	public static final Block WROUGHT_IRON_CHAIN = register("wrought_iron_chain",
			new ChainBlock(AbstractBlock.Settings.create().requiresTool().strength(5.0F, 6.0F)
					.sounds(BlockSoundGroup.CHAIN).nonOpaque()), true);
	public static final Block WROUGHT_IRON_DOOR = register("wrought_iron_door",
			new DoorBlock(BlockSetType.IRON, metal().strength(5.0F, 6.0F).nonOpaque()), true);
	public static final Block WROUGHT_IRON_TRAPDOOR = register("wrought_iron_trapdoor",
			new TrapdoorBlock(BlockSetType.IRON, metal().strength(5.0F, 6.0F).nonOpaque()
					.allowsSpawning((state, world, pos, type) -> false)), true);

	// ----- Steel -----
	public static final Block STEEL_BLOCK = register("steel_block",
			new Block(metal().strength(6.0F, 7.0F)), true);
	public static final Block STEEL_BARS = register("steel_bars",
			new PaneBlock(metal().strength(6.0F, 7.0F).nonOpaque()), true);
	public static final Block STEEL_LANTERN = register("steel_lantern",
			new LanternBlock(AbstractBlock.Settings.create().requiresTool().strength(3.5F)
					.sounds(BlockSoundGroup.LANTERN).luminance(state -> 15).nonOpaque()), true);
	public static final Block STEEL_CHAIN = register("steel_chain",
			new ChainBlock(AbstractBlock.Settings.create().requiresTool().strength(6.0F, 7.0F)
					.sounds(BlockSoundGroup.CHAIN).nonOpaque()), true);
	public static final Block STEEL_DOOR = register("steel_door",
			new DoorBlock(BlockSetType.IRON, metal().strength(6.0F, 7.0F).nonOpaque()), true);
	public static final Block STEEL_TRAPDOOR = register("steel_trapdoor",
			new TrapdoorBlock(BlockSetType.IRON, metal().strength(6.0F, 7.0F).nonOpaque()
					.allowsSpawning((state, world, pos, type) -> false)), true);

	private ModBlocks() {
	}

	/** Shared base settings for solid metal blocks. */
	private static AbstractBlock.Settings metal() {
		return AbstractBlock.Settings.create().requiresTool().sounds(BlockSoundGroup.METAL);
	}

	private static Block register(String name, Block block, boolean withItem) {
		Identifier id = Identifier.of(WroughtIronMod.MOD_ID, name);
		Block registered = Registry.register(Registries.BLOCK, id, block);
		if (withItem) {
			Registry.register(Registries.ITEM, id, new BlockItem(registered, new Item.Settings()));
		}
		return registered;
	}

	/** Forces this holder class to load so the static registration above runs. */
	public static void initialize() {
	}
}
