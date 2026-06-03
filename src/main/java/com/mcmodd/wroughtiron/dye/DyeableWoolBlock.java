package com.mcmodd.wroughtiron.dye;

import net.minecraft.block.Block;
import net.minecraft.block.BlockEntityProvider;
import net.minecraft.block.BlockState;
import net.minecraft.block.entity.BlockEntity;
import net.minecraft.component.type.DyedColorComponent;
import net.minecraft.entity.LivingEntity;
import net.minecraft.item.ItemStack;
import net.minecraft.util.math.BlockPos;
import net.minecraft.world.World;

/**
 * A wool block whose color is stored per-placement in a {@link DyeableWoolBlockEntity}. Combined
 * with the vanilla dye-mixing recipe (the block item is in {@code #minecraft:dyeable}), this lets
 * players make wool in any shade imaginable, exactly like dyeing leather armor.
 */
public class DyeableWoolBlock extends Block implements BlockEntityProvider {
	public DyeableWoolBlock(Settings settings) {
		super(settings);
	}

	@Override
	public BlockEntity createBlockEntity(BlockPos pos, BlockState state) {
		return new DyeableWoolBlockEntity(pos, state);
	}

	@Override
	public void onPlaced(World world, BlockPos pos, BlockState state, LivingEntity placer, ItemStack stack) {
		super.onPlaced(world, pos, state, placer, stack);
		if (!world.isClient && world.getBlockEntity(pos) instanceof DyeableWoolBlockEntity be) {
			be.setColor(DyedColorComponent.getColor(stack, DyeableWoolBlockEntity.DEFAULT_COLOR));
		}
	}
}
