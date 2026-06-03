package com.mcmodd.wroughtiron.dye;

import net.minecraft.component.DataComponentTypes;
import net.minecraft.entity.LivingEntity;
import net.minecraft.entity.effect.StatusEffectInstance;
import net.minecraft.entity.effect.StatusEffects;
import net.minecraft.entity.mob.MobEntity;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.component.type.DyedColorComponent;
import net.minecraft.text.Text;
import net.minecraft.text.TextColor;
import net.minecraft.util.ActionResult;
import net.minecraft.util.Hand;

/**
 * A name tag that names a mob with a <b>dyed colour</b> (the item is in {@code #minecraft:dyeable},
 * so its colour is mixed exactly like leather armour). If glow ink has been applied
 * ({@link ModDye#GLOWING} component), the named mob also gains a permanent glowing outline.
 */
public class DyeableNameTagItem extends Item {
	public DyeableNameTagItem(Settings settings) {
		super(settings);
	}

	@Override
	public ActionResult useOnEntity(ItemStack stack, PlayerEntity user, LivingEntity entity, Hand hand) {
		// Behaves like a vanilla name tag: only works if the tag has been renamed, and only on mobs.
		if (!stack.contains(DataComponentTypes.CUSTOM_NAME)) {
			return ActionResult.PASS;
		}
		if (!(entity instanceof MobEntity mob) || !mob.isAttackable()) {
			return ActionResult.PASS;
		}

		if (!user.getWorld().isClient) {
			int color = DyedColorComponent.getColor(stack, 0xFFFFFF);
			Text name = stack.get(DataComponentTypes.CUSTOM_NAME);
			mob.setCustomName(name.copy().styled(style -> style.withColor(TextColor.fromRgb(color))));
			mob.setCustomNameVisible(true);

			if (Boolean.TRUE.equals(stack.get(ModDye.GLOWING))) {
				// Infinite, hidden-particle glowing effect persists across reloads.
				mob.addStatusEffect(new StatusEffectInstance(StatusEffects.GLOWING,
						StatusEffectInstance.INFINITE, 0, false, false, false));
			}

			if (!user.getAbilities().creativeMode) {
				stack.decrement(1);
			}
		}
		return ActionResult.SUCCESS;
	}
}
