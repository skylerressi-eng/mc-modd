package com.mcmodd.wroughtiron.experimental;

import net.minecraft.block.AbstractBlock;
import net.minecraft.block.Block;
import net.minecraft.block.Blocks;
import net.minecraft.fluid.FlowableFluid;
import net.minecraft.item.BucketItem;
import net.minecraft.item.Item;
import net.minecraft.item.Items;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

import com.mcmodd.wroughtiron.WroughtIronMod;

/**
 * EXPERIMENTAL / UNVERIFIED registration of the flowing "dyed water" fluid, its fluid block and a
 * bucket. Fixed tint applied client-side (see ExperimentalClient).
 */
public final class ModFluids {
	public static final FlowableFluid STILL_DYED_WATER = Registry.register(
			Registries.FLUID, id("dyed_water"), new DyedFluid.Still());

	public static final FlowableFluid FLOWING_DYED_WATER = Registry.register(
			Registries.FLUID, id("flowing_dyed_water"), new DyedFluid.Flowing());

	public static final Block DYED_WATER_FLUID_BLOCK = Registry.register(
			Registries.BLOCK, id("dyed_water_fluid"),
			new DyedWaterFluidBlock(STILL_DYED_WATER, AbstractBlock.Settings.copy(Blocks.WATER)));

	public static final Item DYED_WATER_BUCKET = Registry.register(
			Registries.ITEM, id("dyed_water_bucket"),
			new BucketItem(STILL_DYED_WATER, new Item.Settings().recipeRemainder(Items.BUCKET).maxCount(1)));

	private ModFluids() {
	}

	private static Identifier id(String path) {
		return Identifier.of(WroughtIronMod.MOD_ID, path);
	}

	public static void initialize() {
	}
}
