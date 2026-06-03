package com.mcmodd.wroughtiron.experimental;

import net.fabricmc.api.EnvType;
import net.fabricmc.api.Environment;
import net.fabricmc.fabric.api.blockrenderlayer.v1.BlockRenderLayerMap;
import net.fabricmc.fabric.api.client.render.fluid.v1.FluidRenderHandlerRegistry;
import net.fabricmc.fabric.api.client.render.fluid.v1.SimpleFluidRenderHandler;
import net.fabricmc.fabric.api.client.rendering.v1.ColorProviderRegistry;
import net.fabricmc.fabric.api.client.rendering.v1.EntityRendererRegistry;
import net.minecraft.client.render.RenderLayer;
import net.minecraft.client.render.entity.ItemFrameEntityRenderer;
import net.minecraft.component.type.DyedColorComponent;
import net.minecraft.util.Identifier;

/**
 * EXPERIMENTAL / UNVERIFIED client setup for the flowing fluid and dyeable item frame.
 *
 * <p>The fluid reuses vanilla water sprites with a fixed dyed tint. The item frame uses the vanilla
 * renderer for now (so the placed frame is not yet tinted) but its inventory item is tinted.
 */
@Environment(EnvType.CLIENT)
public final class ExperimentalClient {
	/** Fixed tint for the flowing dyed water (a fluid can't carry an arbitrary per-block color). */
	private static final int DYED_WATER_TINT = 0x8A5BE0;

	private ExperimentalClient() {
	}

	public static void onInitializeClient() {
		FluidRenderHandlerRegistry.INSTANCE.register(
				ModFluids.STILL_DYED_WATER, ModFluids.FLOWING_DYED_WATER,
				new SimpleFluidRenderHandler(
						Identifier.of("minecraft", "block/water_still"),
						Identifier.of("minecraft", "block/water_flow"),
						DYED_WATER_TINT));
		BlockRenderLayerMap.INSTANCE.putFluids(RenderLayer.getTranslucent(),
				ModFluids.STILL_DYED_WATER, ModFluids.FLOWING_DYED_WATER);

		// Renders like a normal item frame for now; tinting the frame model is the remaining hook.
		EntityRendererRegistry.register(ModFrames.DYEABLE_ITEM_FRAME, ItemFrameEntityRenderer::new);

		// Inventory item is tinted by its dyed color.
		ColorProviderRegistry.ITEM.register(
				(stack, tintIndex) -> tintIndex == 0 ? DyedColorComponent.getColor(stack, 0xFFFFFF) : -1,
				ModFrames.DYEABLE_ITEM_FRAME_ITEM);
	}
}
