package com.mcmodd.wroughtiron.dye;

import com.mojang.serialization.Codec;

import net.fabricmc.fabric.api.itemgroup.v1.ItemGroupEvents;
import net.fabricmc.fabric.api.object.builder.v1.block.entity.FabricBlockEntityTypeBuilder;
import net.minecraft.block.AbstractBlock;
import net.minecraft.block.Block;
import net.minecraft.block.entity.BlockEntityType;
import net.minecraft.component.DataComponentType;
import net.minecraft.component.DataComponentTypes;
import net.minecraft.component.type.DyedColorComponent;
import net.minecraft.item.AnimalArmorItem;
import net.minecraft.item.ArmorMaterials;
import net.minecraft.item.BlockItem;
import net.minecraft.item.Item;
import net.minecraft.network.codec.PacketCodecs;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.registry.RegistryKey;
import net.minecraft.registry.RegistryKeys;
import net.minecraft.sound.BlockSoundGroup;
import net.minecraft.util.Identifier;

import com.mcmodd.wroughtiron.WroughtIronMod;

/**
 * Registers the "full dye rework" content: dyeable wool (with its block entity) and dyeable name
 * tags, plus the {@link #GLOWING} component used to turn name tags into glow tags.
 *
 * <p>Each dyeable item is registered with a default {@code minecraft:dyed_color} component and is
 * added to the {@code #minecraft:dyeable} item tag (see the generated data), which is what lets the
 * vanilla crafting-table dye-mixing recipe tint them to any shade.
 */
public final class ModDye {
	/** Marks a name tag as carrying glow ink, so naming a mob also makes it glow. */
	public static final DataComponentType<Boolean> GLOWING = Registry.register(
			Registries.DATA_COMPONENT_TYPE,
			Identifier.of(WroughtIronMod.MOD_ID, "glowing"),
			DataComponentType.<Boolean>builder().codec(Codec.BOOL).packetCodec(PacketCodecs.BOOL).build());

	// ----- Dyeable wool -----
	public static final Block DYEABLE_WOOL = Registry.register(
			Registries.BLOCK,
			Identifier.of(WroughtIronMod.MOD_ID, "dyeable_wool"),
			new DyeableWoolBlock(AbstractBlock.Settings.create()
					.strength(0.8F).sounds(BlockSoundGroup.WOOL).burnable()));

	public static final Item DYEABLE_WOOL_ITEM = Registry.register(
			Registries.ITEM,
			Identifier.of(WroughtIronMod.MOD_ID, "dyeable_wool"),
			new BlockItem(DYEABLE_WOOL, new Item.Settings().component(DataComponentTypes.DYED_COLOR,
					new DyedColorComponent(DyeableWoolBlockEntity.DEFAULT_COLOR, false))));

	public static final BlockEntityType<DyeableWoolBlockEntity> DYEABLE_WOOL_BLOCK_ENTITY = Registry.register(
			Registries.BLOCK_ENTITY_TYPE,
			Identifier.of(WroughtIronMod.MOD_ID, "dyeable_wool"),
			FabricBlockEntityTypeBuilder.create(DyeableWoolBlockEntity::new, DYEABLE_WOOL).build());

	// ----- Dyeable / glowing name tag -----
	public static final Item DYEABLE_NAME_TAG = Registry.register(
			Registries.ITEM,
			Identifier.of(WroughtIronMod.MOD_ID, "dyeable_name_tag"),
			new DyeableNameTagItem(new Item.Settings().maxCount(64).component(DataComponentTypes.DYED_COLOR,
					new DyedColorComponent(0xFFFFFF, false))));

	// ----- Dyeable water (translucent, any-shade decorative block) -----
	public static final Block DYED_WATER = Registry.register(
			Registries.BLOCK,
			Identifier.of(WroughtIronMod.MOD_ID, "dyed_water"),
			new DyedWaterBlock(AbstractBlock.Settings.create()
					.strength(0.4F).sounds(BlockSoundGroup.GLASS).nonOpaque()
					.allowsSpawning((state, world, pos, type) -> false)));

	public static final Item DYED_WATER_ITEM = Registry.register(
			Registries.ITEM,
			Identifier.of(WroughtIronMod.MOD_ID, "dyed_water"),
			new BlockItem(DYED_WATER, new Item.Settings().component(DataComponentTypes.DYED_COLOR,
					new DyedColorComponent(DyedWaterBlockEntity.DEFAULT_COLOR, false))));

	public static final BlockEntityType<DyedWaterBlockEntity> DYED_WATER_BLOCK_ENTITY = Registry.register(
			Registries.BLOCK_ENTITY_TYPE,
			Identifier.of(WroughtIronMod.MOD_ID, "dyed_water"),
			FabricBlockEntityTypeBuilder.create(DyedWaterBlockEntity::new, DYED_WATER).build());

	// ----- Dyeable horse armor (leather-based, so it tints on the horse) -----
	public static final Item DYEABLE_HORSE_ARMOR = Registry.register(
			Registries.ITEM,
			Identifier.of(WroughtIronMod.MOD_ID, "dyeable_horse_armor"),
			new AnimalArmorItem(ArmorMaterials.LEATHER, AnimalArmorItem.Type.EQUESTRIAN,
					new Item.Settings().maxCount(1).component(DataComponentTypes.DYED_COLOR,
							new DyedColorComponent(0xA06540, false))));

	private ModDye() {
	}

	public static void initialize() {
		// Append the dye content to the mod's creative tab.
		RegistryKey<net.minecraft.item.ItemGroup> group = RegistryKey.of(RegistryKeys.ITEM_GROUP,
				Identifier.of(WroughtIronMod.MOD_ID, "general"));
		ItemGroupEvents.modifyEntriesEvent(group).register(entries -> {
			entries.add(DYEABLE_WOOL_ITEM);
			entries.add(DYED_WATER_ITEM);
			entries.add(DYEABLE_NAME_TAG);
			entries.add(DYEABLE_HORSE_ARMOR);
		});
	}
}
