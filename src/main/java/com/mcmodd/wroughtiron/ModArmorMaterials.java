package com.mcmodd.wroughtiron;

import java.util.EnumMap;
import java.util.List;
import java.util.Map;
import java.util.function.Supplier;

import net.minecraft.item.ArmorItem;
import net.minecraft.item.ArmorMaterial;
import net.minecraft.recipe.Ingredient;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.registry.entry.RegistryEntry;
import net.minecraft.sound.SoundEvent;
import net.minecraft.sound.SoundEvents;
import net.minecraft.util.Identifier;
import net.minecraft.util.Util;

/**
 * Custom {@link ArmorMaterial}s for the mod, registered into the armor-material registry so that
 * {@link ArmorItem}s can reference them.
 *
 * <p>Durability is supplied per-piece on the {@link net.minecraft.item.Item.Settings} via
 * {@link ArmorItem.Type#getMaxDamage(int)} using the multipliers below.
 */
public final class ModArmorMaterials {
	/** Durability multiplier (vanilla iron is 15, diamond is 33). */
	public static final int WROUGHT_IRON_DURABILITY = 18;
	public static final int STEEL_DURABILITY = 28;

	public static final RegistryEntry<ArmorMaterial> WROUGHT_IRON = register(
			"wrought_iron",
			Map.of(
					ArmorItem.Type.BOOTS, 2,
					ArmorItem.Type.LEGGINGS, 5,
					ArmorItem.Type.CHESTPLATE, 6,
					ArmorItem.Type.HELMET, 2,
					ArmorItem.Type.BODY, 5),
			12,
			SoundEvents.ITEM_ARMOR_EQUIP_IRON,
			0.5F,
			0.0F,
			() -> Ingredient.ofItems(ModItems.WROUGHT_IRON_INGOT));

	public static final RegistryEntry<ArmorMaterial> STEEL = register(
			"steel",
			Map.of(
					ArmorItem.Type.BOOTS, 3,
					ArmorItem.Type.LEGGINGS, 6,
					ArmorItem.Type.CHESTPLATE, 7,
					ArmorItem.Type.HELMET, 3,
					ArmorItem.Type.BODY, 6),
			11,
			SoundEvents.ITEM_ARMOR_EQUIP_IRON,
			1.5F,
			0.0F,
			() -> Ingredient.ofItems(ModItems.STEEL_INGOT));

	private ModArmorMaterials() {
	}

	private static RegistryEntry<ArmorMaterial> register(String id, Map<ArmorItem.Type, Integer> defense,
			int enchantability, RegistryEntry<SoundEvent> equipSound, float toughness, float knockbackResistance,
			Supplier<Ingredient> repairIngredient) {
		EnumMap<ArmorItem.Type, Integer> defenseMap = new EnumMap<>(ArmorItem.Type.class);
		defenseMap.putAll(defense);

		List<ArmorMaterial.Layer> layers = List.of(
				new ArmorMaterial.Layer(Identifier.of(WroughtIronMod.MOD_ID, id)));

		ArmorMaterial material = new ArmorMaterial(defenseMap, enchantability, equipSound, repairIngredient,
				layers, toughness, knockbackResistance);

		return Registry.registerReference(Registries.ARMOR_MATERIAL,
				Identifier.of(WroughtIronMod.MOD_ID, id), material);
	}

	/** Forces this holder class to load so the static registration above runs. */
	public static void initialize() {
		Util.make(() -> null);
	}
}
