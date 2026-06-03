package com.mcmodd.wroughtiron.experimental;

import java.util.Optional;

import net.minecraft.block.Block;
import net.minecraft.block.BlockState;
import net.minecraft.block.FluidBlock;
import net.minecraft.block.entity.BlockEntity;
import net.minecraft.fluid.FlowableFluid;
import net.minecraft.fluid.Fluid;
import net.minecraft.fluid.FluidState;
import net.minecraft.item.Item;
import net.minecraft.sound.SoundEvent;
import net.minecraft.sound.SoundEvents;
import net.minecraft.state.StateManager;
import net.minecraft.util.math.BlockPos;
import net.minecraft.world.World;
import net.minecraft.world.WorldAccess;
import net.minecraft.world.WorldView;

/**
 * EXPERIMENTAL / UNVERIFIED (could not be compiled in this sandbox).
 *
 * <p>A custom flowing fluid for "flowing dyed water". Because fluids have no per-block storage, this
 * uses a single fixed tint (applied by the render handler) rather than an arbitrary mixed color.
 * Standard {@link FlowableFluid} implementation following the Fabric fluids tutorial; some method
 * signatures may need a tweak against the exact 1.21.1 mappings on first compile.
 */
public abstract class DyedFluid extends FlowableFluid {
	@Override
	public Fluid getStill() {
		return ModFluids.STILL_DYED_WATER;
	}

	@Override
	public Fluid getFlowing() {
		return ModFluids.FLOWING_DYED_WATER;
	}

	@Override
	public Item getBucketItem() {
		return ModFluids.DYED_WATER_BUCKET;
	}

	@Override
	protected boolean isInfinite(World world) {
		return false;
	}

	@Override
	protected void beforeReplacingBlock(WorldAccess world, BlockPos pos, BlockState state) {
		BlockEntity blockEntity = state.hasBlockEntity() ? world.getBlockEntity(pos) : null;
		Block.dropStacks(state, world, pos, blockEntity);
	}

	@Override
	protected int getFlowSpeed(WorldView world) {
		return 4;
	}

	@Override
	protected int getLevelDecreasePerBlock(WorldView world) {
		return 1;
	}

	@Override
	public int getTickRate(WorldView world) {
		return 5;
	}

	@Override
	protected float getBlastResistance() {
		return 100.0F;
	}

	@Override
	public Optional<SoundEvent> getBucketFillSound() {
		return Optional.of(SoundEvents.ITEM_BUCKET_FILL);
	}

	@Override
	protected BlockState toBlockState(FluidState state) {
		return ModFluids.DYED_WATER_FLUID_BLOCK.getDefaultState().with(FluidBlock.LEVEL, getBlockStateLevel(state));
	}

	@Override
	public boolean matchesType(Fluid fluid) {
		return fluid == ModFluids.STILL_DYED_WATER || fluid == ModFluids.FLOWING_DYED_WATER;
	}

	public static class Flowing extends DyedFluid {
		@Override
		protected void appendProperties(StateManager.Builder<Fluid, FluidState> builder) {
			super.appendProperties(builder);
			builder.add(LEVEL);
		}

		@Override
		public int getLevel(FluidState state) {
			return state.get(LEVEL);
		}

		@Override
		public boolean isStill(FluidState state) {
			return false;
		}
	}

	public static class Still extends DyedFluid {
		@Override
		public int getLevel(FluidState state) {
			return 8;
		}

		@Override
		public boolean isStill(FluidState state) {
			return true;
		}
	}
}
