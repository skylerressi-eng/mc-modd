package com.mcmodd.wroughtiron.dye;

import net.minecraft.block.BlockState;
import net.minecraft.block.entity.BlockEntity;
import net.minecraft.component.ComponentMap;
import net.minecraft.component.DataComponentTypes;
import net.minecraft.component.type.DyedColorComponent;
import net.minecraft.nbt.NbtCompound;
import net.minecraft.network.listener.ClientPlayPacketListener;
import net.minecraft.network.packet.Packet;
import net.minecraft.network.packet.s2c.play.BlockEntityUpdateS2C;
import net.minecraft.registry.RegistryWrapper;
import net.minecraft.util.math.BlockPos;

/**
 * Stores the dyed color of a {@link DyedWaterBlock}. Mirrors {@link DyeableWoolBlockEntity} so that
 * dyed water supports the exact same "any shade" dye-mixing mechanic.
 */
public class DyedWaterBlockEntity extends BlockEntity {
	public static final int DEFAULT_COLOR = 0x3F76E4; // vanilla-ish water blue

	private int color = DEFAULT_COLOR;

	public DyedWaterBlockEntity(BlockPos pos, BlockState state) {
		super(ModDye.DYED_WATER_BLOCK_ENTITY, pos, state);
	}

	public int getColor() {
		return this.color;
	}

	public void setColor(int color) {
		this.color = color;
		this.markDirty();
		if (this.world != null) {
			this.world.updateListeners(this.pos, this.getCachedState(), this.getCachedState(),
					net.minecraft.block.Block.NOTIFY_ALL);
		}
	}

	@Override
	protected void writeNbt(NbtCompound nbt, RegistryWrapper.WrapperLookup registries) {
		super.writeNbt(nbt, registries);
		nbt.putInt("color", this.color);
	}

	@Override
	protected void readNbt(NbtCompound nbt, RegistryWrapper.WrapperLookup registries) {
		super.readNbt(nbt, registries);
		if (nbt.contains("color")) {
			this.color = nbt.getInt("color");
		}
	}

	@Override
	protected void addComponents(ComponentMap.Builder builder) {
		super.addComponents(builder);
		builder.add(DataComponentTypes.DYED_COLOR, new DyedColorComponent(this.color, true));
	}

	@Override
	protected void readComponents(BlockEntity.ComponentsAccess components) {
		super.readComponents(components);
		DyedColorComponent dyed = components.get(DataComponentTypes.DYED_COLOR);
		if (dyed != null) {
			this.color = dyed.rgb();
		}
	}

	@Override
	public void removeFromCopiedStackNbt(NbtCompound nbt) {
		nbt.remove("color");
	}

	@Override
	public Packet<ClientPlayPacketListener> toUpdatePacket() {
		return BlockEntityUpdateS2C.create(this);
	}

	@Override
	public NbtCompound toInitialChunkDataNbt(RegistryWrapper.WrapperLookup registries) {
		return this.createNbt(registries);
	}
}
