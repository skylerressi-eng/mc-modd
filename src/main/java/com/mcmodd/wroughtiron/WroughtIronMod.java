package com.mcmodd.wroughtiron;

import net.fabricmc.api.ModInitializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Main entrypoint for the Wrought Iron &amp; Steel mod.
 *
 * <p>The mod adds a small metallurgy progression on top of vanilla iron:
 * <ul>
 *     <li>Smelt an iron ingot to refine it into a <b>wrought iron ingot</b>.</li>
 *     <li>Combine iron and charcoal to forge a <b>steel ingot</b>.</li>
 *     <li>Use either metal to craft a full set of tools, armor and decorative blocks.</li>
 * </ul>
 */
public class WroughtIronMod implements ModInitializer {
	public static final String MOD_ID = "wroughtiron";
	public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

	@Override
	public void onInitialize() {
		// Order matters only in that blocks must exist before block items / item group entries
		// reference them. Each initialize() call simply forces the holder class to load so its
		// static registration runs.
		ModBlocks.initialize();
		ModItems.initialize();
		ModItemGroups.initialize();
		com.mcmodd.wroughtiron.dye.ModDye.initialize();

		LOGGER.info("[{}] Wrought iron and steel are ready for the forge.", MOD_ID);
	}
}
