package com.mcmodd.wroughtiron.client;

import net.fabricmc.api.ClientModInitializer;
import net.fabricmc.api.EnvType;
import net.fabricmc.api.Environment;
import net.fabricmc.fabric.api.client.rendering.v1.ColorProviderRegistry;
import net.minecraft.component.type.DyedColorComponent;

import com.mcmodd.wroughtiron.dye.DyeableWoolBlockEntity;
import com.mcmodd.wroughtiron.dye.ModDye;

/**
 * Client entrypoint: registers the tint providers that colour the dyeable items and the dyeable
 * wool block from their stored dye colour.
 */
@Environment(EnvType.CLIENT)
public class WroughtIronClient implements ClientModInitializer {
	private static final int WHITE = 0xFFFFFF;

	@Override
	public void onInitializeClient() {
		// Items: tint layer 0 by the item's dyed_color component.
		ColorProviderRegistry.ITEM.register(
				(stack, tintIndex) -> tintIndex == 0 ? DyedColorComponent.getColor(stack, WHITE) : -1,
				ModDye.DYEABLE_WOOL_ITEM, ModDye.DYEABLE_NAME_TAG);

		// Dyeable wool block: tint by the colour stored in its block entity.
		ColorProviderRegistry.BLOCK.register((state, world, pos, tintIndex) -> {
			if (tintIndex == 0 && world != null && pos != null
					&& world.getBlockEntity(pos) instanceof DyeableWoolBlockEntity be) {
				return be.getColor();
			}
			return WHITE;
		}, ModDye.DYEABLE_WOOL);
	}
}
