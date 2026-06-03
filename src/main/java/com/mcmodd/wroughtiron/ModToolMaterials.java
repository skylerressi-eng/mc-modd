package com.mcmodd.wroughtiron;

import java.util.function.Supplier;

import net.minecraft.block.Block;
import net.minecraft.item.ToolMaterial;
import net.minecraft.recipe.Ingredient;
import net.minecraft.registry.tag.BlockTags;
import net.minecraft.registry.tag.TagKey;

/**
 * Custom {@link ToolMaterial}s for the mod.
 *
 * <p>Both tiers can mine everything an iron tool can (they share
 * {@link BlockTags#INCORRECT_FOR_IRON_TOOL}). Wrought iron is a touch more durable than iron, and
 * steel sits between iron and diamond on durability and damage.
 */
public enum ModToolMaterials implements ToolMaterial {
	// inverseTag, durability, miningSpeed, attackDamage, enchantability, repairIngredient
	WROUGHT_IRON(BlockTags.INCORRECT_FOR_IRON_TOOL, 320, 6.5F, 2.0F, 14,
			() -> Ingredient.ofItems(ModItems.WROUGHT_IRON_INGOT)),
	STEEL(BlockTags.INCORRECT_FOR_IRON_TOOL, 800, 7.0F, 2.5F, 12,
			() -> Ingredient.ofItems(ModItems.STEEL_INGOT));

	private final TagKey<Block> inverseTag;
	private final int durability;
	private final float miningSpeed;
	private final float attackDamage;
	private final int enchantability;
	private final Supplier<Ingredient> repairIngredient;

	ModToolMaterials(TagKey<Block> inverseTag, int durability, float miningSpeed, float attackDamage,
			int enchantability, Supplier<Ingredient> repairIngredient) {
		this.inverseTag = inverseTag;
		this.durability = durability;
		this.miningSpeed = miningSpeed;
		this.attackDamage = attackDamage;
		this.enchantability = enchantability;
		this.repairIngredient = repairIngredient;
	}

	@Override
	public int getDurability() {
		return this.durability;
	}

	@Override
	public float getMiningSpeedMultiplier() {
		return this.miningSpeed;
	}

	@Override
	public float getAttackDamage() {
		return this.attackDamage;
	}

	@Override
	public TagKey<Block> getInverseTag() {
		return this.inverseTag;
	}

	@Override
	public int getEnchantability() {
		return this.enchantability;
	}

	@Override
	public Ingredient getRepairIngredient() {
		return this.repairIngredient.get();
	}
}
