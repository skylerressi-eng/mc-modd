package com.mcmodd.wroughtiron;

import net.fabricmc.fabric.api.itemgroup.v1.FabricItemGroup;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;

/**
 * Creative inventory tab that gathers everything the mod adds, in a sensible order.
 */
public final class ModItemGroups {
	public static final ItemGroup WROUGHT_IRON_GROUP = Registry.register(
			Registries.ITEM_GROUP,
			Identifier.of(WroughtIronMod.MOD_ID, "general"),
			FabricItemGroup.builder()
					.icon(() -> new ItemStack(ModItems.STEEL_INGOT))
					.displayName(Text.translatable("itemgroup.wroughtiron.general"))
					.entries((displayContext, entries) -> {
						// Materials
						entries.add(ModItems.WROUGHT_IRON_INGOT);
						entries.add(ModItems.WROUGHT_IRON_NUGGET);
						entries.add(ModItems.STEEL_INGOT);
						entries.add(ModItems.STEEL_NUGGET);

						// Storage + decorative blocks
						entries.add(ModBlocks.WROUGHT_IRON_BLOCK);
						entries.add(ModBlocks.WROUGHT_IRON_BARS);
						entries.add(ModBlocks.WROUGHT_IRON_LANTERN);
						entries.add(ModBlocks.WROUGHT_IRON_CHAIN);
						entries.add(ModBlocks.WROUGHT_IRON_DOOR);
						entries.add(ModBlocks.WROUGHT_IRON_TRAPDOOR);
						entries.add(ModBlocks.STEEL_BLOCK);
						entries.add(ModBlocks.STEEL_BARS);
						entries.add(ModBlocks.STEEL_LANTERN);
						entries.add(ModBlocks.STEEL_CHAIN);
						entries.add(ModBlocks.STEEL_DOOR);
						entries.add(ModBlocks.STEEL_TRAPDOOR);

						// Wrought iron tools + armor
						entries.add(ModItems.WROUGHT_IRON_SWORD);
						entries.add(ModItems.WROUGHT_IRON_PICKAXE);
						entries.add(ModItems.WROUGHT_IRON_AXE);
						entries.add(ModItems.WROUGHT_IRON_SHOVEL);
						entries.add(ModItems.WROUGHT_IRON_HOE);
						entries.add(ModItems.WROUGHT_IRON_HELMET);
						entries.add(ModItems.WROUGHT_IRON_CHESTPLATE);
						entries.add(ModItems.WROUGHT_IRON_LEGGINGS);
						entries.add(ModItems.WROUGHT_IRON_BOOTS);

						// Steel tools + armor
						entries.add(ModItems.STEEL_SWORD);
						entries.add(ModItems.STEEL_PICKAXE);
						entries.add(ModItems.STEEL_AXE);
						entries.add(ModItems.STEEL_SHOVEL);
						entries.add(ModItems.STEEL_HOE);
						entries.add(ModItems.STEEL_HELMET);
						entries.add(ModItems.STEEL_CHESTPLATE);
						entries.add(ModItems.STEEL_LEGGINGS);
						entries.add(ModItems.STEEL_BOOTS);
					})
					.build());

	private ModItemGroups() {
	}

	/** Forces this holder class to load so the static registration above runs. */
	public static void initialize() {
	}
}
