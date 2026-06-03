package com.mcmodd.wroughtiron.experimental;

import net.minecraft.entity.EntityType;
import net.minecraft.entity.data.DataTracker;
import net.minecraft.entity.data.TrackedData;
import net.minecraft.entity.data.TrackedDataHandlerRegistry;
import net.minecraft.entity.decoration.ItemFrameEntity;
import net.minecraft.nbt.NbtCompound;
import net.minecraft.util.math.BlockPos;
import net.minecraft.util.math.Direction;
import net.minecraft.world.World;

/**
 * EXPERIMENTAL / UNVERIFIED (could not be compiled in this sandbox).
 *
 * <p>An item frame that stores a dye color (tracked + persisted). The color is shown on the
 * inventory item via a color provider. Two hooks remain to finish: (1) copying the placed item's
 * color onto the spawned entity, and (2) tinting the frame model in a custom renderer.
 */
public class DyeableItemFrameEntity extends ItemFrameEntity {
	public static final int DEFAULT_COLOR = 0xFFFFFF;

	private static final TrackedData<Integer> COLOR =
			DataTracker.registerData(DyeableItemFrameEntity.class, TrackedDataHandlerRegistry.INTEGER);

	public DyeableItemFrameEntity(EntityType<? extends ItemFrameEntity> type, World world) {
		super(type, world);
	}

	public DyeableItemFrameEntity(World world, BlockPos pos, Direction facing) {
		super(ModFrames.DYEABLE_ITEM_FRAME, world, pos, facing);
	}

	@Override
	protected void initDataTracker(DataTracker.Builder builder) {
		super.initDataTracker(builder);
		builder.add(COLOR, DEFAULT_COLOR);
	}

	public int getColor() {
		return this.getDataTracker().get(COLOR);
	}

	public void setColor(int color) {
		this.getDataTracker().set(COLOR, color);
	}

	@Override
	public void writeCustomDataToNbt(NbtCompound nbt) {
		super.writeCustomDataToNbt(nbt);
		nbt.putInt("Color", this.getColor());
	}

	@Override
	public void readCustomDataFromNbt(NbtCompound nbt) {
		super.readCustomDataFromNbt(nbt);
		if (nbt.contains("Color")) {
			this.setColor(nbt.getInt("Color"));
		}
	}
}
