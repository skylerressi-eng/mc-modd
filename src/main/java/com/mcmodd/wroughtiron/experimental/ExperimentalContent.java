package com.mcmodd.wroughtiron.experimental;

import net.fabricmc.fabric.api.itemgroup.v1.ItemGroupEvents;
import net.minecraft.item.ItemGroup;
import net.minecraft.registry.RegistryKey;
import net.minecraft.registry.RegistryKeys;
import net.minecraft.util.Identifier;

import com.mcmodd.wroughtiron.WroughtIronMod;

/**
 * EXPERIMENTAL / UNVERIFIED. Common (both-sides) setup for the experimental dye features: forces the
 * fluid + frame holders to load and adds their items to the creative tab.
 */
public final class ExperimentalContent {
	private ExperimentalContent() {
	}

	public static void initialize() {
		ModFluids.initialize();
		ModFrames.initialize();

		RegistryKey<ItemGroup> group = RegistryKey.of(RegistryKeys.ITEM_GROUP,
				Identifier.of(WroughtIronMod.MOD_ID, "general"));
		ItemGroupEvents.modifyEntriesEvent(group).register(entries -> {
			entries.add(ModFluids.DYED_WATER_BUCKET);
			entries.add(ModFrames.DYEABLE_ITEM_FRAME_ITEM);
		});
	}
}
