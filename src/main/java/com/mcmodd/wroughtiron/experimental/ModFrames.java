package com.mcmodd.wroughtiron.experimental;

import net.minecraft.component.DataComponentTypes;
import net.minecraft.component.type.DyedColorComponent;
import net.minecraft.entity.EntityType;
import net.minecraft.entity.SpawnGroup;
import net.minecraft.item.Item;
import net.minecraft.item.ItemFrameItem;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.registry.RegistryKey;
import net.minecraft.registry.RegistryKeys;
import net.minecraft.util.Identifier;

import com.mcmodd.wroughtiron.WroughtIronMod;

/**
 * EXPERIMENTAL / UNVERIFIED registration of the dyeable item frame entity and its placement item.
 */
public final class ModFrames {
	public static final EntityType<DyeableItemFrameEntity> DYEABLE_ITEM_FRAME = Registry.register(
			Registries.ENTITY_TYPE, id("dyeable_item_frame"),
			EntityType.Builder.<DyeableItemFrameEntity>create(DyeableItemFrameEntity::new, SpawnGroup.MISC)
					.dimensions(0.5F, 0.5F)
					.maxTrackingRange(10)
					.build(RegistryKey.of(RegistryKeys.ENTITY_TYPE, id("dyeable_item_frame"))));

	public static final Item DYEABLE_ITEM_FRAME_ITEM = Registry.register(
			Registries.ITEM, id("dyeable_item_frame"),
			new ItemFrameItem(DYEABLE_ITEM_FRAME, new Item.Settings().component(DataComponentTypes.DYED_COLOR,
					new DyedColorComponent(DyeableItemFrameEntity.DEFAULT_COLOR, false))));

	private ModFrames() {
	}

	private static Identifier id(String path) {
		return Identifier.of(WroughtIronMod.MOD_ID, path);
	}

	public static void initialize() {
	}
}
