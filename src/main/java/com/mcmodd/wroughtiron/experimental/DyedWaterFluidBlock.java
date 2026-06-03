package com.mcmodd.wroughtiron.experimental;

import net.minecraft.block.FluidBlock;
import net.minecraft.fluid.FlowableFluid;

/**
 * EXPERIMENTAL / UNVERIFIED.
 *
 * <p>Trivial subclass so we can construct a {@link FluidBlock} (its constructor is protected).
 */
public class DyedWaterFluidBlock extends FluidBlock {
	public DyedWaterFluidBlock(FlowableFluid fluid, Settings settings) {
		super(fluid, settings);
	}
}
