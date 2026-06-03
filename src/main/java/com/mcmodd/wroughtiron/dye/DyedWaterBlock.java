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
 * A translucent, glass-like "water" block whose color is stored per-placement so it can be dyed to
 * any shade with the vanilla dye-mixing recipe.
 *
 * <p>Note: this is a solid decorative block, not a flowing fluid. Minecraft fluids have no per-block
 * storage, so an arbitrarily-colored <i>flowing</i> water isn't representable &mdash; a colored
 * block is what makes the "every shade" mechanic possible.
 */
public class DyedWaterBlock extends Block implements BlockEntityProvider {
	public DyedWaterBlock(Settings settings) {
		super(settings);
	}

	@Override
	public BlockEntity createBlockEntity(BlockPos pos, BlockState state) {
		return new DyedWaterBlockEntity(pos, state);
	}

	@Override
	public void onPlaced(World world, BlockPos pos, BlockState state, LivingEntity placer, ItemStack stack) {
		super.onPlaced(world, pos, state, placer, stack);
		if (!world.isClient && world.getBlockEntity(pos) instanceof DyedWaterBlockEntity be) {
			be.setColor(DyedColorComponent.getColor(stack, DyedWaterBlockEntity.DEFAULT_COLOR));
		}
	}
}
