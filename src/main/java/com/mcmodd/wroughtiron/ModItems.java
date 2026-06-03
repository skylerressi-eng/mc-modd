package com.mcmodd.wroughtiron;

import net.minecraft.item.ArmorItem;
import net.minecraft.item.AxeItem;
import net.minecraft.item.HoeItem;
import net.minecraft.item.Item;
import net.minecraft.item.PickaxeItem;
import net.minecraft.item.ShovelItem;
import net.minecraft.item.SwordItem;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

/**
 * All non-block items added by the mod: ingots/nuggets, the full tool sets and the full armor sets
 * for both wrought iron and steel.
 */
public final class ModItems {
	// ----- Materials -----
	public static final Item WROUGHT_IRON_INGOT = register("wrought_iron_ingot", new Item(new Item.Settings()));
	public static final Item WROUGHT_IRON_NUGGET = register("wrought_iron_nugget", new Item(new Item.Settings()));
	public static final Item STEEL_INGOT = register("steel_ingot", new Item(new Item.Settings()));
	public static final Item STEEL_NUGGET = register("steel_nugget", new Item(new Item.Settings()));

	// ----- Wrought iron tools (iron-style attack values) -----
	public static final Item WROUGHT_IRON_SWORD = register("wrought_iron_sword",
			new SwordItem(ModToolMaterials.WROUGHT_IRON, 3, -2.4F, new Item.Settings()));
	public static final Item WROUGHT_IRON_PICKAXE = register("wrought_iron_pickaxe",
			new PickaxeItem(ModToolMaterials.WROUGHT_IRON, 1, -2.8F, new Item.Settings()));
	public static final Item WROUGHT_IRON_AXE = register("wrought_iron_axe",
			new AxeItem(ModToolMaterials.WROUGHT_IRON, 6.0F, -3.1F, new Item.Settings()));
	public static final Item WROUGHT_IRON_SHOVEL = register("wrought_iron_shovel",
			new ShovelItem(ModToolMaterials.WROUGHT_IRON, 1.5F, -3.0F, new Item.Settings()));
	public static final Item WROUGHT_IRON_HOE = register("wrought_iron_hoe",
			new HoeItem(ModToolMaterials.WROUGHT_IRON, -2, -1.0F, new Item.Settings()));

	// ----- Steel tools -----
	public static final Item STEEL_SWORD = register("steel_sword",
			new SwordItem(ModToolMaterials.STEEL, 3, -2.4F, new Item.Settings()));
	public static final Item STEEL_PICKAXE = register("steel_pickaxe",
			new PickaxeItem(ModToolMaterials.STEEL, 1, -2.8F, new Item.Settings()));
	public static final Item STEEL_AXE = register("steel_axe",
			new AxeItem(ModToolMaterials.STEEL, 6.0F, -3.1F, new Item.Settings()));
	public static final Item STEEL_SHOVEL = register("steel_shovel",
			new ShovelItem(ModToolMaterials.STEEL, 1.5F, -3.0F, new Item.Settings()));
	public static final Item STEEL_HOE = register("steel_hoe",
			new HoeItem(ModToolMaterials.STEEL, -2, -1.0F, new Item.Settings()));

	// ----- Wrought iron armor -----
	public static final Item WROUGHT_IRON_HELMET = register("wrought_iron_helmet",
			new ArmorItem(ModArmorMaterials.WROUGHT_IRON, ArmorItem.Type.HELMET,
					new Item.Settings().maxDamage(ArmorItem.Type.HELMET.getMaxDamage(ModArmorMaterials.WROUGHT_IRON_DURABILITY))));
	public static final Item WROUGHT_IRON_CHESTPLATE = register("wrought_iron_chestplate",
			new ArmorItem(ModArmorMaterials.WROUGHT_IRON, ArmorItem.Type.CHESTPLATE,
					new Item.Settings().maxDamage(ArmorItem.Type.CHESTPLATE.getMaxDamage(ModArmorMaterials.WROUGHT_IRON_DURABILITY))));
	public static final Item WROUGHT_IRON_LEGGINGS = register("wrought_iron_leggings",
			new ArmorItem(ModArmorMaterials.WROUGHT_IRON, ArmorItem.Type.LEGGINGS,
					new Item.Settings().maxDamage(ArmorItem.Type.LEGGINGS.getMaxDamage(ModArmorMaterials.WROUGHT_IRON_DURABILITY))));
	public static final Item WROUGHT_IRON_BOOTS = register("wrought_iron_boots",
			new ArmorItem(ModArmorMaterials.WROUGHT_IRON, ArmorItem.Type.BOOTS,
					new Item.Settings().maxDamage(ArmorItem.Type.BOOTS.getMaxDamage(ModArmorMaterials.WROUGHT_IRON_DURABILITY))));

	// ----- Steel armor -----
	public static final Item STEEL_HELMET = register("steel_helmet",
			new ArmorItem(ModArmorMaterials.STEEL, ArmorItem.Type.HELMET,
					new Item.Settings().maxDamage(ArmorItem.Type.HELMET.getMaxDamage(ModArmorMaterials.STEEL_DURABILITY))));
	public static final Item STEEL_CHESTPLATE = register("steel_chestplate",
			new ArmorItem(ModArmorMaterials.STEEL, ArmorItem.Type.CHESTPLATE,
					new Item.Settings().maxDamage(ArmorItem.Type.CHESTPLATE.getMaxDamage(ModArmorMaterials.STEEL_DURABILITY))));
	public static final Item STEEL_LEGGINGS = register("steel_leggings",
			new ArmorItem(ModArmorMaterials.STEEL, ArmorItem.Type.LEGGINGS,
					new Item.Settings().maxDamage(ArmorItem.Type.LEGGINGS.getMaxDamage(ModArmorMaterials.STEEL_DURABILITY))));
	public static final Item STEEL_BOOTS = register("steel_boots",
			new ArmorItem(ModArmorMaterials.STEEL, ArmorItem.Type.BOOTS,
					new Item.Settings().maxDamage(ArmorItem.Type.BOOTS.getMaxDamage(ModArmorMaterials.STEEL_DURABILITY))));

	private ModItems() {
	}

	private static Item register(String name, Item item) {
		return Registry.register(Registries.ITEM, Identifier.of(WroughtIronMod.MOD_ID, name), item);
	}

	/** Forces this holder class to load so the static registration above runs. */
	public static void initialize() {
		// Ensure material holders are loaded as well (they are referenced above, but be explicit).
		ModArmorMaterials.initialize();
	}
}
