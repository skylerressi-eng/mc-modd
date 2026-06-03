#!/usr/bin/env python3
"""
Asset/data generator for the dye-rework content (dyeable wool + dyeable/glowing name tags).

Run from the repo root:  python3 tools/generate_dye_assets.py
(Depends on Pillow.  Run tools/generate_assets.py first; this script merges into its lang file.)
"""

import json
import os
import random
from PIL import Image, ImageDraw

MOD_ID = "wroughtiron"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "src", "main", "resources", "assets", MOD_ID)
DATA = os.path.join(ROOT, "src", "main", "resources", "data")


def ensure(path):
    os.makedirs(path, exist_ok=True)


def write_json(path, obj):
    ensure(os.path.dirname(path))
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)
        f.write("\n")


# ---------------------------------------------------------------------------
# Grayscale textures (tinted at runtime by the colour providers)
# ---------------------------------------------------------------------------

def wool_texture():
    """A light, faintly noisy wool weave that multiplies cleanly with any tint."""
    rng = random.Random(42)
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    px = img.load()
    for y in range(16):
        for x in range(16):
            base = 226
            # subtle woven checker + noise
            if (x + y) % 2 == 0:
                base += 8
            base += rng.randint(-10, 10)
            base = max(150, min(245, base))
            px[x, y] = (base, base, base, 255)
    save(img, "block", "dyeable_wool.png")


def name_tag_texture():
    """A pale paper tag on a string; grayscale so the dyed colour shows through."""
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # string
    d.line([(11, 1), (8, 5)], fill=(120, 120, 120, 255))
    # tag body
    d.polygon([(3, 5), (12, 5), (14, 9), (12, 13), (3, 13)], fill=(232, 232, 232, 255),
              outline=(150, 150, 150, 255))
    # eyelet
    d.ellipse([10, 7, 12, 9], outline=(120, 120, 120, 255))
    # a couple of "text" ticks
    d.line([(5, 8), (8, 8)], fill=(170, 170, 170, 255))
    d.line([(5, 10), (9, 10)], fill=(170, 170, 170, 255))
    save(img, "item", "dyeable_name_tag.png")


def water_texture():
    """A light, translucent ripple texture; tinted + rendered translucent at runtime."""
    rng = random.Random(7)
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    px = img.load()
    for y in range(16):
        for x in range(16):
            base = 235 + rng.randint(-8, 8)
            # faint horizontal ripples
            if y % 4 == 0:
                base -= 18
            base = max(180, min(245, base))
            px[x, y] = (base, base, base, 190)
    save(img, "block", "dyed_water.png")


def horse_armor_texture():
    """A grayscale barding icon, tinted by the item colour provider."""
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # saddle/barding silhouette
    d.polygon([(3, 6), (12, 6), (13, 10), (8, 13), (3, 11)], fill=(225, 225, 225, 255),
              outline=(150, 150, 150, 255))
    d.line([(6, 3), (9, 3)], fill=(160, 160, 160, 255))  # strap
    d.line([(7, 3), (7, 6)], fill=(160, 160, 160, 255))
    d.line([(5, 8), (11, 8)], fill=(180, 180, 180, 255))
    d.ellipse([6, 9, 9, 11], outline=(160, 160, 160, 255))
    save(img, "item", "dyeable_horse_armor.png")


def save(img, *parts):
    path = os.path.join(ASSETS, "textures", *parts)
    ensure(os.path.dirname(path))
    img.save(path)


# ---------------------------------------------------------------------------
# Models / blockstates
# ---------------------------------------------------------------------------

def tinted_cube_faces():
    faces = {}
    for face, cull in [("down", "down"), ("up", "up"), ("north", "north"),
                       ("south", "south"), ("west", "west"), ("east", "east")]:
        faces[face] = {"texture": "#all", "cullface": cull, "tintindex": 0}
    return faces


def gen_models():
    # dyeable wool block model (all faces tinted)
    write_json(os.path.join(ASSETS, "models", "block", "dyeable_wool.json"), {
        "parent": "minecraft:block/block",
        "textures": {
            "all": f"{MOD_ID}:block/dyeable_wool",
            "particle": f"{MOD_ID}:block/dyeable_wool",
        },
        "elements": [{
            "from": [0, 0, 0],
            "to": [16, 16, 16],
            "faces": tinted_cube_faces(),
        }],
    })
    # block item model -> the block model (so the inventory icon is tinted too)
    write_json(os.path.join(ASSETS, "models", "item", "dyeable_wool.json"),
               {"parent": f"{MOD_ID}:block/dyeable_wool"})
    # name tag item model (layer0 tinted by the item colour provider)
    write_json(os.path.join(ASSETS, "models", "item", "dyeable_name_tag.json"),
               {"parent": "minecraft:item/generated",
                "textures": {"layer0": f"{MOD_ID}:item/dyeable_name_tag"}})
    # horse armor item model
    write_json(os.path.join(ASSETS, "models", "item", "dyeable_horse_armor.json"),
               {"parent": "minecraft:item/generated",
                "textures": {"layer0": f"{MOD_ID}:item/dyeable_horse_armor"}})
    # dyed water block model (all faces tinted, translucent texture)
    write_json(os.path.join(ASSETS, "models", "block", "dyed_water.json"), {
        "parent": "minecraft:block/block",
        "textures": {
            "all": f"{MOD_ID}:block/dyed_water",
            "particle": f"{MOD_ID}:block/dyed_water",
        },
        "elements": [{
            "from": [0, 0, 0],
            "to": [16, 16, 16],
            "faces": tinted_cube_faces(),
        }],
    })
    write_json(os.path.join(ASSETS, "models", "item", "dyed_water.json"),
               {"parent": f"{MOD_ID}:block/dyed_water"})
    # blockstates
    write_json(os.path.join(ASSETS, "blockstates", "dyeable_wool.json"),
               {"variants": {"": {"model": f"{MOD_ID}:block/dyeable_wool"}}})
    write_json(os.path.join(ASSETS, "blockstates", "dyed_water.json"),
               {"variants": {"": {"model": f"{MOD_ID}:block/dyed_water"}}})


# ---------------------------------------------------------------------------
# Loot / recipes / tags
# ---------------------------------------------------------------------------

def _copy_color_loot(block_id):
    return {
        "type": "minecraft:block",
        "pools": [{
            "rolls": 1.0,
            "bonus_rolls": 0.0,
            "entries": [{
                "type": "minecraft:item",
                "name": block_id,
                "functions": [{
                    "function": "minecraft:copy_components",
                    "source": "block_entity",
                    "include": ["minecraft:dyed_color"],
                }],
            }],
            "conditions": [{"condition": "minecraft:survives_explosion"}],
        }],
    }


def gen_loot():
    # Drop the block and copy the stored colour back onto the item.
    write_json(os.path.join(DATA, MOD_ID, "loot_table", "blocks", "dyeable_wool.json"),
               _copy_color_loot(f"{MOD_ID}:dyeable_wool"))
    write_json(os.path.join(DATA, MOD_ID, "loot_table", "blocks", "dyed_water.json"),
               _copy_color_loot(f"{MOD_ID}:dyed_water"))


def gen_recipes():
    rdir = os.path.join(DATA, MOD_ID, "recipe")
    # Craft a dyeable wool base from plain white wool.
    write_json(os.path.join(rdir, "dyeable_wool.json"), {
        "type": "minecraft:crafting_shapeless",
        "category": "building",
        "ingredients": ["minecraft:white_wool"],
        "result": {"id": f"{MOD_ID}:dyeable_wool", "count": 1},
    })
    # Craft a dyed water block from glass + a starter dye.
    write_json(os.path.join(rdir, "dyed_water.json"), {
        "type": "minecraft:crafting_shapeless",
        "category": "building",
        "ingredients": ["minecraft:glass", "minecraft:light_blue_dye"],
        "result": {"id": f"{MOD_ID}:dyed_water", "count": 1},
    })
    # Convert a leather horse armor into the dyeable variant.
    write_json(os.path.join(rdir, "dyeable_horse_armor.json"), {
        "type": "minecraft:crafting_shapeless",
        "category": "equipment",
        "ingredients": ["minecraft:leather_horse_armor"],
        "result": {"id": f"{MOD_ID}:dyeable_horse_armor", "count": 1},
    })
    # Craft a dyeable name tag from a vanilla name tag.
    write_json(os.path.join(rdir, "dyeable_name_tag.json"), {
        "type": "minecraft:crafting_shapeless",
        "category": "misc",
        "ingredients": ["minecraft:name_tag"],
        "result": {"id": f"{MOD_ID}:dyeable_name_tag", "count": 1},
    })
    # Apply glow ink to a name tag -> glowing name tag (sets the glowing component).
    write_json(os.path.join(rdir, "glow_name_tag.json"), {
        "type": "minecraft:crafting_shapeless",
        "category": "misc",
        "ingredients": [f"{MOD_ID}:dyeable_name_tag", "minecraft:glow_ink_sac"],
        "result": {
            "id": f"{MOD_ID}:dyeable_name_tag",
            "count": 1,
            "components": {f"{MOD_ID}:glowing": True},
        },
    })


def gen_tags():
    # The vanilla dye-mixing recipe applies to everything in #minecraft:dyeable.
    write_json(os.path.join(DATA, "minecraft", "tags", "item", "dyeable.json"),
               {"replace": False, "values": [
                   f"{MOD_ID}:dyeable_wool",
                   f"{MOD_ID}:dyed_water",
                   f"{MOD_ID}:dyeable_name_tag",
                   f"{MOD_ID}:dyeable_horse_armor",
               ]})


def merge_lang():
    path = os.path.join(ASSETS, "lang", "en_us.json")
    lang = {}
    if os.path.exists(path):
        lang = json.load(open(path))
    lang[f"block.{MOD_ID}.dyeable_wool"] = "Dyeable Wool"
    lang[f"block.{MOD_ID}.dyed_water"] = "Dyed Water"
    lang[f"item.{MOD_ID}.dyeable_name_tag"] = "Dyeable Name Tag"
    lang[f"item.{MOD_ID}.dyeable_horse_armor"] = "Dyeable Horse Armor"
    write_json(path, lang)


def main():
    wool_texture()
    name_tag_texture()
    water_texture()
    horse_armor_texture()
    gen_models()
    gen_loot()
    gen_recipes()
    gen_tags()
    merge_lang()
    print("Generated dye assets and data for", MOD_ID)


if __name__ == "__main__":
    main()
