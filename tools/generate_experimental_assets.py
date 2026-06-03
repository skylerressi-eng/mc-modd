#!/usr/bin/env python3
"""
EXPERIMENTAL asset generator (claude/dye-experimental branch): assets for the flowing dyed water
bucket/fluid block and the dyeable item frame.  Run from the repo root after the other generators.
"""

import json
import os
from PIL import Image, ImageDraw

MOD_ID = "wroughtiron"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "src", "main", "resources", "assets", MOD_ID)
DATA = os.path.join(ROOT, "src", "main", "resources", "data")


def ensure(p):
    os.makedirs(p, exist_ok=True)


def write_json(path, obj):
    ensure(os.path.dirname(path))
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)
        f.write("\n")


def save(img, *parts):
    path = os.path.join(ASSETS, "textures", *parts)
    ensure(os.path.dirname(path))
    img.save(path)


def frame_texture():
    """A grayscale square frame ring (tintable); center is transparent."""
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rectangle([2, 2, 13, 13], fill=(210, 210, 210, 255), outline=(150, 150, 150, 255))
    d.rectangle([4, 4, 11, 11], fill=(0, 0, 0, 0))
    # corner pegs
    for (x, y) in [(3, 3), (12, 3), (3, 12), (12, 12)]:
        img.load()[x, y] = (170, 170, 170, 255)
    save(img, "item", "dyeable_item_frame.png")


def bucket_texture():
    """A plain bucket with purple liquid (the dyed-water bucket)."""
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # liquid
    d.rectangle([5, 6, 10, 8], fill=(138, 91, 224, 255))
    # bucket body
    d.polygon([(4, 8), (11, 8), (10, 14), (5, 14)], fill=(170, 175, 182, 255),
              outline=(90, 96, 104, 255))
    d.line([(4, 8), (11, 8)], fill=(120, 126, 134, 255))
    save(img, "item", "dyed_water_bucket.png")


def main():
    frame_texture()
    bucket_texture()

    # item models
    write_json(os.path.join(ASSETS, "models", "item", "dyeable_item_frame.json"),
               {"parent": "minecraft:item/generated",
                "textures": {"layer0": f"{MOD_ID}:item/dyeable_item_frame"}})
    write_json(os.path.join(ASSETS, "models", "item", "dyed_water_bucket.json"),
               {"parent": "minecraft:item/generated",
                "textures": {"layer0": f"{MOD_ID}:item/dyed_water_bucket"}})

    # fluid block: rendered by the fluid renderer, model just supplies a particle sprite
    write_json(os.path.join(ASSETS, "models", "block", "dyed_water_fluid.json"),
               {"textures": {"particle": "minecraft:block/water_still"}})
    write_json(os.path.join(ASSETS, "blockstates", "dyed_water_fluid.json"),
               {"variants": {"": {"model": f"{MOD_ID}:block/dyed_water_fluid"}}})

    # obtain the dyed water bucket from a water bucket + dye
    write_json(os.path.join(DATA, MOD_ID, "recipe", "dyed_water_bucket.json"), {
        "type": "minecraft:crafting_shapeless",
        "category": "misc",
        "ingredients": ["minecraft:water_bucket", "minecraft:purple_dye"],
        "result": {"id": f"{MOD_ID}:dyed_water_bucket", "count": 1},
    })

    # add the dyeable item frame to #minecraft:dyeable (keep the existing entries)
    write_json(os.path.join(DATA, "minecraft", "tags", "item", "dyeable.json"),
               {"replace": False, "values": [
                   f"{MOD_ID}:dyeable_wool",
                   f"{MOD_ID}:dyed_water",
                   f"{MOD_ID}:dyeable_name_tag",
                   f"{MOD_ID}:dyeable_horse_armor",
                   f"{MOD_ID}:dyeable_item_frame",
               ]})

    # lang
    lang_path = os.path.join(ASSETS, "lang", "en_us.json")
    lang = json.load(open(lang_path)) if os.path.exists(lang_path) else {}
    lang[f"item.{MOD_ID}.dyed_water_bucket"] = "Dyed Water Bucket"
    lang[f"item.{MOD_ID}.dyeable_item_frame"] = "Dyeable Item Frame"
    lang[f"entity.{MOD_ID}.dyeable_item_frame"] = "Dyeable Item Frame"
    lang[f"block.{MOD_ID}.dyed_water_fluid"] = "Dyed Water"
    write_json(lang_path, lang)

    print("Generated EXPERIMENTAL assets for", MOD_ID)


if __name__ == "__main__":
    main()
