#!/usr/bin/env python3
"""
Asset/data generator for the Wrought Iron & Steel mod (Fabric 1.21.1).

This script writes every texture (PNG, via Pillow) and every resource/data JSON
(blockstates, models, lang, loot tables, recipes, tags) into src/main/resources.

It is committed for transparency/reproducibility. Running it again regenerates the
exact same files, so the generated assets are also committed so the mod builds
without needing Python.

Run from the repo root:  python3 tools/generate_assets.py
"""

import json
import os
from PIL import Image, ImageDraw

MOD_ID = "wroughtiron"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "src", "main", "resources", "assets", MOD_ID)
DATA = os.path.join(ROOT, "src", "main", "resources", "data")

MATERIALS = ["wrought_iron", "steel"]

# ---------------------------------------------------------------------------
# Palettes
# ---------------------------------------------------------------------------
PALETTES = {
    "wrought_iron": {
        "L": (95, 101, 110, 255),
        "B": (64, 69, 75, 255),
        "D": (42, 46, 51, 255),
        "E": (24, 26, 29, 255),
    },
    "steel": {
        "L": (201, 211, 219, 255),
        "B": (150, 161, 171, 255),
        "D": (99, 110, 120, 255),
        "E": (58, 66, 74, 255),
    },
}
WOOD = {"W": (122, 82, 47, 255), "K": (86, 57, 33, 255)}
GLOW = (255, 226, 150, 255)
GLOW_D = (224, 168, 86, 255)
T = (0, 0, 0, 0)

PRETTY = {
    "wrought_iron": "Wrought Iron",
    "steel": "Steel",
}

# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

def ensure(path):
    os.makedirs(path, exist_ok=True)


def write_json(path, obj):
    ensure(os.path.dirname(path))
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)
        f.write("\n")


def save_png(img, *parts):
    path = os.path.join(ASSETS, "textures", *parts)
    ensure(os.path.dirname(path))
    img.save(path)


def new_img(w=16, h=16):
    return Image.new("RGBA", (w, h), T)


def from_ascii(rows, palette):
    """Build a 16x16 image from ASCII art. '.' is transparent."""
    codes = {".": T}
    codes.update(palette)
    codes.update(WOOD)
    codes["G"] = GLOW
    codes["g"] = GLOW_D
    img = new_img()
    px = img.load()
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            px[x, y] = codes[ch]
    return img


# ---------------------------------------------------------------------------
# Item textures
# ---------------------------------------------------------------------------
INGOT = [
    "................",
    "................",
    "................",
    "................",
    "................",
    ".....LLLLLLL....",
    "....LBBBBBBBD...",
    "...EBBBBBBBBBE..",
    "...EBBBBBBBBBE..",
    "...EDBBBBBBBDE..",
    "....EDDDDDDDE...",
    ".....EEEEEEE....",
    "................",
    "................",
    "................",
    "................",
]

NUGGET = [
    "................",
    "................",
    "................",
    "................",
    "......LLLL......",
    ".....LBBBBD.....",
    ".....EBBBBE.....",
    ".....EDBBDE.....",
    "......EDDE......",
    ".......EE.......",
    "................",
    "................",
    "................",
    "................",
    "................",
    "................",
]


def tool_sword(p):
    img = new_img()
    d = ImageDraw.Draw(img)
    # blade
    d.rectangle([7, 1, 8, 9], fill=p["L"])
    d.line([(7, 1), (7, 9)], fill=p["L"])
    d.line([(8, 1), (8, 9)], fill=p["D"])
    img.load()[7, 1] = p["E"]
    # crossguard
    d.rectangle([5, 10, 10, 10], fill=p["D"])
    img.load()[5, 10] = p["E"]
    img.load()[10, 10] = p["E"]
    # handle
    d.rectangle([7, 11, 8, 14], fill=WOOD["W"])
    img.load()[8, 14] = WOOD["K"]
    return img


def tool_pickaxe(p):
    img = new_img()
    d = ImageDraw.Draw(img)
    # head: arched bar
    d.line([(2, 4), (13, 4)], fill=p["B"])
    d.line([(2, 3), (13, 3)], fill=p["L"])
    d.line([(2, 5), (13, 5)], fill=p["D"])
    img.load()[2, 4] = p["E"]
    img.load()[13, 4] = p["E"]
    img.load()[2, 3] = p["E"]
    img.load()[13, 3] = p["E"]
    # handle
    d.rectangle([7, 5, 8, 15], fill=WOOD["W"])
    d.line([(8, 5), (8, 15)], fill=WOOD["K"])
    return img


def tool_axe(p):
    img = new_img()
    d = ImageDraw.Draw(img)
    # head wedge on the left
    d.polygon([(5, 2), (10, 3), (10, 8), (5, 9)], fill=p["B"])
    d.line([(5, 2), (5, 9)], fill=p["L"])
    d.line([(10, 3), (10, 8)], fill=p["D"])
    d.line([(5, 2), (10, 3)], fill=p["L"])
    d.line([(5, 9), (10, 8)], fill=p["E"])
    # handle
    d.rectangle([9, 3, 10, 15], fill=WOOD["W"])
    d.line([(10, 3), (10, 15)], fill=WOOD["K"])
    return img


def tool_shovel(p):
    img = new_img()
    d = ImageDraw.Draw(img)
    # spade head
    d.rectangle([6, 10, 9, 14], fill=p["B"])
    d.line([(6, 10), (6, 14)], fill=p["L"])
    d.line([(9, 10), (9, 14)], fill=p["D"])
    d.line([(6, 14), (9, 14)], fill=p["E"])
    img.load()[7, 14] = p["E"]
    img.load()[8, 14] = p["E"]
    # handle
    d.rectangle([7, 1, 8, 10], fill=WOOD["W"])
    d.line([(8, 1), (8, 10)], fill=WOOD["K"])
    return img


def tool_hoe(p):
    img = new_img()
    d = ImageDraw.Draw(img)
    # head: short horizontal bar with a downward tooth on the left
    d.line([(6, 3), (12, 3)], fill=p["B"])
    d.line([(6, 2), (12, 2)], fill=p["L"])
    d.rectangle([6, 3, 7, 5], fill=p["D"])
    img.load()[6, 2] = p["E"]
    img.load()[12, 2] = p["E"]
    # handle
    d.rectangle([10, 3, 11, 15], fill=WOOD["W"])
    d.line([(11, 3), (11, 15)], fill=WOOD["K"])
    return img


def armor_helmet(p):
    img = new_img()
    d = ImageDraw.Draw(img)
    d.rectangle([4, 4, 11, 9], fill=p["B"])
    d.rectangle([4, 3, 11, 3], fill=p["L"])
    d.line([(4, 4), (4, 9)], fill=p["L"])
    d.line([(11, 4), (11, 9)], fill=p["D"])
    # face gap
    d.rectangle([6, 7, 9, 9], fill=T)
    d.rectangle([4, 9, 5, 11], fill=p["D"])
    d.rectangle([10, 9, 11, 11], fill=p["D"])
    return img


def armor_chest(p):
    img = new_img()
    d = ImageDraw.Draw(img)
    # shoulders
    d.rectangle([3, 3, 12, 4], fill=p["L"])
    # body
    d.rectangle([4, 5, 11, 12], fill=p["B"])
    d.line([(4, 5), (4, 12)], fill=p["L"])
    d.line([(11, 5), (11, 12)], fill=p["D"])
    d.line([(4, 12), (11, 12)], fill=p["E"])
    # neck
    d.rectangle([7, 3, 8, 4], fill=T)
    d.line([(6, 5), (9, 5)], fill=p["D"])
    return img


def armor_legs(p):
    img = new_img()
    d = ImageDraw.Draw(img)
    d.rectangle([4, 3, 11, 5], fill=p["B"])
    d.line([(4, 3), (11, 3)], fill=p["L"])
    # legs
    d.rectangle([4, 6, 6, 13], fill=p["B"])
    d.rectangle([9, 6, 11, 13], fill=p["B"])
    d.line([(4, 6), (4, 13)], fill=p["L"])
    d.line([(11, 6), (11, 13)], fill=p["D"])
    d.line([(4, 13), (6, 13)], fill=p["E"])
    d.line([(9, 13), (11, 13)], fill=p["E"])
    return img


def armor_boots(p):
    img = new_img()
    d = ImageDraw.Draw(img)
    d.rectangle([3, 9, 6, 13], fill=p["B"])
    d.rectangle([9, 9, 12, 13], fill=p["B"])
    d.line([(3, 9), (6, 9)], fill=p["L"])
    d.line([(9, 9), (12, 9)], fill=p["L"])
    d.line([(3, 13), (6, 13)], fill=p["E"])
    d.line([(9, 13), (12, 13)], fill=p["E"])
    return img


def chain_item(p):
    img = new_img()
    px = img.load()
    pat = [".X.", "X.X", "X.X", "X.X", ".X."]
    for y in range(16):
        row = pat[y % 5]
        for i, ch in enumerate(row):
            if ch == "X":
                x = 6 + i
                if i == 0:
                    px[x, y] = p["L"]
                elif i == 2:
                    px[x, y] = p["D"]
                else:
                    px[x, y] = p["B"]
    return img


def door_item(p):
    img = new_img()
    d = ImageDraw.Draw(img)
    d.rectangle([4, 0, 11, 15], fill=p["B"])
    d.rectangle([4, 0, 11, 15], outline=p["E"])
    d.line([(5, 1), (5, 14)], fill=p["L"])
    d.line([(10, 1), (10, 14)], fill=p["D"])
    # panels
    d.rectangle([6, 2, 9, 6], outline=p["D"])
    d.rectangle([6, 9, 9, 13], outline=p["D"])
    # handle
    img.load()[9, 8] = p["L"]
    return img


# ---------------------------------------------------------------------------
# Block textures
# ---------------------------------------------------------------------------

def block_storage(p):
    rows = [
        "EEEEEEEEEEEEEEEE",
        "ELLLLLLLLLLLLLLE",
        "ELBBBBBBBBBBBBLE",
        "ELBDBBBBBBBBDBLE",
        "ELBBBBBBBBBBBBLE",
        "ELBBBBLLLLBBBBLE",
        "ELBBBBLBBLBBBBLE",
        "ELBBBBLBBLBBBBLE",
        "ELBBBBLLLLBBBBLE",
        "ELBBBBBBBBBBBBLE",
        "ELBDBBBBBBBBDBLE",
        "ELBBBBBBBBBBBBLE",
        "ELBBBBBBBBBBBBLE",
        "ELBBBBBBBBBBBBLE",
        "ELLLLLLLLLLLLLLE",
        "EEEEEEEEEEEEEEEE",
    ]
    return from_ascii(rows, p)


def block_bars(p):
    img = new_img()
    px = img.load()
    for (c0, c1) in [(1, 2), (7, 8), (13, 14)]:
        for y in range(16):
            px[c0, y] = p["L"]
            px[c1, y] = p["D"]
        px[c0, 0] = p["E"]
        px[c1, 0] = p["E"]
        px[c0, 15] = p["E"]
        px[c1, 15] = p["E"]
    return img


def block_chain(p):
    img = new_img()
    px = img.load()
    pat = [".X.", "X.X", "X.X", "X.X", ".X."]
    for strip in (0, 3):
        for y in range(16):
            row = pat[y % 5]
            for i, ch in enumerate(row):
                if ch == "X":
                    x = strip + i
                    if i == 0:
                        px[x, y] = p["L"]
                    elif i == 2:
                        px[x, y] = p["D"]
                    else:
                        px[x, y] = p["B"]
    return img


def block_lantern(p):
    img = Image.new("RGBA", (16, 16), p["B"])
    d = ImageDraw.Draw(img)
    # glowing interior
    d.rectangle([4, 4, 11, 11], fill=GLOW)
    # cage bars over the glow
    for x in (4, 7, 10):
        d.line([(x, 4), (x, 11)], fill=p["E"])
    d.line([(4, 4), (11, 4)], fill=p["D"])
    d.line([(4, 11), (11, 11)], fill=p["D"])
    # frame
    d.rectangle([3, 3, 12, 12], outline=p["E"])
    # top cap / loop
    d.rectangle([5, 1, 10, 3], fill=p["L"])
    d.rectangle([6, 0, 9, 0], fill=p["D"])
    # bottom
    d.rectangle([4, 13, 11, 14], fill=p["D"])
    d.rectangle([5, 15, 10, 15], fill=p["E"])
    return img


def block_door_half(p, top):
    img = Image.new("RGBA", (16, 16), p["B"])
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 15, 15], outline=p["E"])
    d.line([(1, 1), (1, 14)], fill=p["L"])
    d.line([(14, 1), (14, 14)], fill=p["D"])
    if top:
        d.line([(1, 1), (14, 1)], fill=p["L"])
        # barred window
        d.rectangle([5, 3, 10, 8], fill=p["D"])
        for x in (6, 8, 10):
            d.line([(x, 3), (x, 8)], fill=p["E"])
        d.rectangle([5, 3, 10, 8], outline=p["E"])
    else:
        d.line([(1, 14), (14, 14)], fill=p["E"])
        # recessed panel
        d.rectangle([4, 3, 11, 12], outline=p["D"])
        d.line([(5, 4), (5, 11)], fill=p["L"])
        # handle
        d.rectangle([11, 7, 12, 8], fill=p["L"])
    return img


def block_trapdoor(p):
    img = Image.new("RGBA", (16, 16), p["B"])
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 15, 15], outline=p["E"])
    # frame
    d.rectangle([1, 1, 14, 14], outline=p["D"])
    d.line([(1, 1), (14, 1)], fill=p["L"])
    # cross braces
    d.line([(1, 1), (14, 14)], fill=p["D"])
    d.line([(14, 1), (1, 14)], fill=p["D"])
    # rivets
    for (x, y) in [(2, 2), (13, 2), (2, 13), (13, 13), (7, 7)]:
        img.load()[x, y] = p["L"]
    return img


def armor_layer(p, two):
    """Worn-armor texture (64x32). Tinted plates; the game maps it onto the body."""
    img = Image.new("RGBA", (64, 32), p["B"])
    d = ImageDraw.Draw(img)
    # subtle top-down shading
    for y in range(32):
        if y < 4:
            shade = p["L"]
        elif y > 26:
            shade = p["D"]
        else:
            continue
        d.line([(0, y), (63, y)], fill=shade)
    # a few rivets / seams for texture
    for x in range(2, 64, 9):
        for y in range(3, 32, 8):
            img.load()[x % 64, y % 32] = p["E"]
    if two:
        d.line([(0, 16), (63, 16)], fill=p["D"])
    return img


def mod_icon():
    img = Image.new("RGBA", (128, 128), (28, 30, 34, 255))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 127, 127], outline=(70, 76, 84, 255), width=3)

    def ingot(cx, cy, p, scale=7):
        pts = [
            (cx - 4 * scale, cy - 2 * scale),
            (cx + 4 * scale, cy - 2 * scale),
            (cx + 5 * scale, cy + 2 * scale),
            (cx - 5 * scale, cy + 2 * scale),
        ]
        d.polygon(pts, fill=p["B"], outline=p["E"])
        d.line([pts[0], pts[1]], fill=p["L"], width=3)

    ingot(64, 46, PALETTES["steel"], 8)
    ingot(64, 86, PALETTES["wrought_iron"], 8)
    path = os.path.join(ASSETS, "icon.png")
    ensure(os.path.dirname(path))
    img.save(path)


# ---------------------------------------------------------------------------
# Texture generation driver
# ---------------------------------------------------------------------------

def gen_textures():
    for m in MATERIALS:
        p = PALETTES[m]
        save_png(from_ascii(INGOT, p), "item", f"{m}_ingot.png")
        save_png(from_ascii(NUGGET, p), "item", f"{m}_nugget.png")
        save_png(tool_sword(p), "item", f"{m}_sword.png")
        save_png(tool_pickaxe(p), "item", f"{m}_pickaxe.png")
        save_png(tool_axe(p), "item", f"{m}_axe.png")
        save_png(tool_shovel(p), "item", f"{m}_shovel.png")
        save_png(tool_hoe(p), "item", f"{m}_hoe.png")
        save_png(armor_helmet(p), "item", f"{m}_helmet.png")
        save_png(armor_chest(p), "item", f"{m}_chestplate.png")
        save_png(armor_legs(p), "item", f"{m}_leggings.png")
        save_png(armor_boots(p), "item", f"{m}_boots.png")
        save_png(chain_item(p), "item", f"{m}_chain.png")
        save_png(door_item(p), "item", f"{m}_door.png")

        save_png(block_storage(p), "block", f"{m}_block.png")
        save_png(block_bars(p), "block", f"{m}_bars.png")
        save_png(block_chain(p), "block", f"{m}_chain.png")
        save_png(block_lantern(p), "block", f"{m}_lantern.png")
        save_png(block_door_half(p, True), "block", f"{m}_door_top.png")
        save_png(block_door_half(p, False), "block", f"{m}_door_bottom.png")
        save_png(block_trapdoor(p), "block", f"{m}_trapdoor.png")

        save_png(armor_layer(p, False), "models", "armor", f"{m}_layer_1.png")
        save_png(armor_layer(p, True), "models", "armor", f"{m}_layer_2.png")
    mod_icon()


# ---------------------------------------------------------------------------
# Item models
# ---------------------------------------------------------------------------

def model_path(*parts):
    return os.path.join(ASSETS, "models", *parts)


def generated_item(layer0):
    return {"parent": "minecraft:item/generated", "textures": {"layer0": layer0}}


def handheld_item(layer0):
    return {"parent": "minecraft:item/handheld", "textures": {"layer0": layer0}}


def gen_item_models():
    for m in MATERIALS:
        ns = f"{MOD_ID}:item/{m}"
        bns = f"{MOD_ID}:block/{m}"
        # materials
        write_json(model_path("item", f"{m}_ingot.json"), generated_item(f"{ns}_ingot"))
        write_json(model_path("item", f"{m}_nugget.json"), generated_item(f"{ns}_nugget"))
        # tools (handheld)
        for tool in ["sword", "pickaxe", "axe", "shovel", "hoe"]:
            write_json(model_path("item", f"{m}_{tool}.json"), handheld_item(f"{ns}_{tool}"))
        # armor
        for piece in ["helmet", "chestplate", "leggings", "boots"]:
            write_json(model_path("item", f"{m}_{piece}.json"), generated_item(f"{ns}_{piece}"))
        # block items
        write_json(model_path("item", f"{m}_block.json"), {"parent": f"{bns}_block"})
        write_json(model_path("item", f"{m}_bars.json"), generated_item(f"{bns}_bars"))
        write_json(model_path("item", f"{m}_lantern.json"), {"parent": f"{bns}_lantern"})
        write_json(model_path("item", f"{m}_chain.json"), generated_item(f"{ns}_chain"))
        write_json(model_path("item", f"{m}_door.json"), generated_item(f"{ns}_door"))
        write_json(model_path("item", f"{m}_trapdoor.json"), {"parent": f"{bns}_trapdoor_bottom"})


# ---------------------------------------------------------------------------
# Block models
# ---------------------------------------------------------------------------

def gen_block_models():
    for m in MATERIALS:
        bt = f"{MOD_ID}:block/{m}"
        # storage block
        write_json(model_path("block", f"{m}_block.json"),
                   {"parent": "minecraft:block/cube_all", "textures": {"all": f"{bt}_block"}})

        # bars (glass-pane templates, single texture for pane + edge)
        pane_tex = {"pane": f"{bt}_bars", "edge": f"{bt}_bars"}
        write_json(model_path("block", f"{m}_bars_post.json"),
                   {"parent": "minecraft:block/template_glass_pane_post", "textures": pane_tex})
        write_json(model_path("block", f"{m}_bars_side.json"),
                   {"parent": "minecraft:block/template_glass_pane_side", "textures": pane_tex})
        write_json(model_path("block", f"{m}_bars_side_alt.json"),
                   {"parent": "minecraft:block/template_glass_pane_side_alt", "textures": pane_tex})
        write_json(model_path("block", f"{m}_bars_noside.json"),
                   {"parent": "minecraft:block/template_glass_pane_noside", "textures": pane_tex})
        write_json(model_path("block", f"{m}_bars_noside_alt.json"),
                   {"parent": "minecraft:block/template_glass_pane_noside_alt", "textures": pane_tex})

        # lantern
        write_json(model_path("block", f"{m}_lantern.json"),
                   {"parent": "minecraft:block/template_lantern", "textures": {"lantern": f"{bt}_lantern"}})
        write_json(model_path("block", f"{m}_lantern_hanging.json"),
                   {"parent": "minecraft:block/template_hanging_lantern", "textures": {"lantern": f"{bt}_lantern"}})

        # chain
        write_json(model_path("block", f"{m}_chain.json"),
                   {"parent": "minecraft:block/chain",
                    "textures": {"all": f"{bt}_chain", "particle": f"{bt}_chain"}})

        # door (8 template variants)
        door_tex = {"top": f"{bt}_door_top", "bottom": f"{bt}_door_bottom"}
        for variant in ["bottom_left", "bottom_left_open", "bottom_right", "bottom_right_open",
                        "top_left", "top_left_open", "top_right", "top_right_open"]:
            write_json(model_path("block", f"{m}_door_{variant}.json"),
                       {"parent": f"minecraft:block/door_{variant}", "textures": door_tex})

        # trapdoor (orientable templates)
        tt = {"texture": f"{bt}_trapdoor"}
        write_json(model_path("block", f"{m}_trapdoor_bottom.json"),
                   {"parent": "minecraft:block/template_orientable_trapdoor_bottom", "textures": tt})
        write_json(model_path("block", f"{m}_trapdoor_top.json"),
                   {"parent": "minecraft:block/template_orientable_trapdoor_top", "textures": tt})
        write_json(model_path("block", f"{m}_trapdoor_open.json"),
                   {"parent": "minecraft:block/template_orientable_trapdoor_open", "textures": tt})


# ---------------------------------------------------------------------------
# Blockstates
# ---------------------------------------------------------------------------

def bs_path(name):
    return os.path.join(ASSETS, "blockstates", f"{name}.json")


def gen_blockstates():
    for m in MATERIALS:
        b = f"{MOD_ID}:block/{m}"

        # storage block
        write_json(bs_path(f"{m}_block"), {"variants": {"": {"model": f"{b}_block"}}})

        # bars (glass-pane multipart)
        write_json(bs_path(f"{m}_bars"), {"multipart": [
            {"apply": {"model": f"{b}_bars_post"}},
            {"when": {"north": "true"}, "apply": {"model": f"{b}_bars_side"}},
            {"when": {"east": "true"}, "apply": {"model": f"{b}_bars_side", "y": 90}},
            {"when": {"south": "true"}, "apply": {"model": f"{b}_bars_side_alt"}},
            {"when": {"west": "true"}, "apply": {"model": f"{b}_bars_side_alt", "y": 90}},
            {"when": {"north": "false"}, "apply": {"model": f"{b}_bars_noside"}},
            {"when": {"east": "false"}, "apply": {"model": f"{b}_bars_noside_alt"}},
            {"when": {"south": "false"}, "apply": {"model": f"{b}_bars_noside_alt", "y": 90}},
            {"when": {"west": "false"}, "apply": {"model": f"{b}_bars_noside", "y": 270}},
        ]})

        # lantern
        write_json(bs_path(f"{m}_lantern"), {"variants": {
            "hanging=false": {"model": f"{b}_lantern"},
            "hanging=true": {"model": f"{b}_lantern_hanging"},
        }})

        # chain
        write_json(bs_path(f"{m}_chain"), {"variants": {
            "axis=x": {"model": f"{b}_chain", "x": 90, "y": 90},
            "axis=y": {"model": f"{b}_chain"},
            "axis=z": {"model": f"{b}_chain", "x": 90},
        }})

        # door
        write_json(bs_path(f"{m}_door"), {"variants": door_variants(b, m)})

        # trapdoor
        write_json(bs_path(f"{m}_trapdoor"), {"variants": trapdoor_variants(b, m)})


def door_variants(b, m):
    facing_y = {"east": 0, "south": 90, "west": 180, "north": 270}
    out = {}
    for facing, base in facing_y.items():
        for half in ["lower", "upper"]:
            for hinge in ["left", "right"]:
                for open_ in ["false", "true"]:
                    key = f"facing={facing},half={half},hinge={hinge},open={open_}"
                    h = "top" if half == "upper" else "bottom"
                    if open_ == "false":
                        model = f"{b}_door_{h}_{hinge}"
                        y = base
                    else:
                        model = f"{b}_door_{h}_{hinge}_open"
                        if hinge == "left":
                            y = (base + 90) % 360
                        else:
                            y = (base + 270) % 360
                    entry = {"model": model}
                    if y:
                        entry["y"] = y
                    out[key] = entry
    return out


def trapdoor_variants(b, m):
    facing_y = {"north": 0, "east": 90, "south": 180, "west": 270}
    out = {}
    for facing, base in facing_y.items():
        for half in ["bottom", "top"]:
            for open_ in ["false", "true"]:
                key = f"facing={facing},half={half},open={open_}"
                if open_ == "true":
                    entry = {"model": f"{b}_trapdoor_open"}
                    if half == "top":
                        entry["x"] = 180
                        y = (base + 180) % 360
                    else:
                        y = base
                    if y:
                        entry["y"] = y
                else:
                    entry = {"model": f"{b}_trapdoor_{'top' if half == 'top' else 'bottom'}"}
                    if base:
                        entry["y"] = base
                out[key] = entry
    return out


# ---------------------------------------------------------------------------
# Loot tables
# ---------------------------------------------------------------------------

def loot_path(name):
    return os.path.join(DATA, MOD_ID, "loot_table", "blocks", f"{name}.json")


def simple_drop(block_id):
    return {
        "type": "minecraft:block",
        "pools": [{
            "rolls": 1.0,
            "bonus_rolls": 0.0,
            "entries": [{"type": "minecraft:item", "name": block_id}],
            "conditions": [{"condition": "minecraft:survives_explosion"}],
        }],
    }


def door_drop(block_id):
    return {
        "type": "minecraft:block",
        "pools": [{
            "rolls": 1.0,
            "bonus_rolls": 0.0,
            "entries": [{"type": "minecraft:item", "name": block_id}],
            "conditions": [{
                "condition": "minecraft:block_state_property",
                "block": block_id,
                "properties": {"half": "lower"},
            }],
        }],
    }


def gen_loot_tables():
    for m in MATERIALS:
        for name in ["block", "bars", "lantern", "chain", "trapdoor"]:
            bid = f"{MOD_ID}:{m}_{name}"
            write_json(loot_path(f"{m}_{name}"), simple_drop(bid))
        did = f"{MOD_ID}:{m}_door"
        write_json(loot_path(f"{m}_door"), door_drop(did))


# ---------------------------------------------------------------------------
# Recipes
# ---------------------------------------------------------------------------

def recipe_path(name):
    return os.path.join(DATA, MOD_ID, "recipe", f"{name}.json")


def item(idv):
    return idv


def shaped(pattern, key, result_id, count=1, category="misc", group=None):
    r = {
        "type": "minecraft:crafting_shaped",
        "category": category,
        "pattern": pattern,
        "key": key,
        "result": {"id": result_id, "count": count},
    }
    if group:
        r["group"] = group
    return r


def shapeless(ingredients, result_id, count=1, category="misc", group=None):
    r = {
        "type": "minecraft:crafting_shapeless",
        "category": category,
        "ingredients": ingredients,
        "result": {"id": result_id, "count": count},
    }
    if group:
        r["group"] = group
    return r


def cooking(rtype, ingredient, result_id, exp, time, category="misc", group=None):
    r = {
        "type": rtype,
        "category": category,
        "ingredient": ingredient,
        "result": {"id": result_id},
        "experience": exp,
        "cookingtime": time,
    }
    if group:
        r["group"] = group
    return r


def gen_recipes():
    iron = "minecraft:iron_ingot"
    stick = "minecraft:stick"

    # --- Wrought iron from smelting iron ---
    wi = f"{MOD_ID}:wrought_iron_ingot"
    write_json(recipe_path("wrought_iron_ingot_from_smelting"),
               cooking("minecraft:smelting", iron, wi, 0.1, 200, group="wrought_iron_ingot"))
    write_json(recipe_path("wrought_iron_ingot_from_blasting"),
               cooking("minecraft:blasting", iron, wi, 0.1, 100, group="wrought_iron_ingot"))

    # --- Steel from combining iron + charcoal ---
    steel = f"{MOD_ID}:steel_ingot"
    write_json(recipe_path("steel_ingot"),
               shapeless([iron, "minecraft:charcoal", "minecraft:charcoal"], steel, 1))

    for m in MATERIALS:
        ingot_id = f"{MOD_ID}:{m}_ingot"
        nugget_id = f"{MOD_ID}:{m}_nugget"
        block_id = f"{MOD_ID}:{m}_block"

        # storage block <-> ingots
        write_json(recipe_path(f"{m}_block"),
                   shaped(["XXX", "XXX", "XXX"], {"X": ingot_id}, block_id, 1, "building"))
        write_json(recipe_path(f"{m}_ingot_from_block"),
                   shapeless([block_id], ingot_id, 9))

        # ingot <-> nuggets
        write_json(recipe_path(f"{m}_nugget"),
                   shapeless([ingot_id], nugget_id, 9))
        write_json(recipe_path(f"{m}_ingot_from_nuggets"),
                   shaped(["XXX", "XXX", "XXX"], {"X": nugget_id}, ingot_id, 1))

        # decorative
        write_json(recipe_path(f"{m}_bars"),
                   shaped(["XXX", "XXX"], {"X": ingot_id}, f"{MOD_ID}:{m}_bars", 16, "building"))
        write_json(recipe_path(f"{m}_lantern"),
                   shaped(["NNN", "NTN", "NNN"], {"N": nugget_id, "T": "minecraft:torch"},
                          f"{MOD_ID}:{m}_lantern", 1, "building"))
        write_json(recipe_path(f"{m}_chain"),
                   shaped(["N", "I", "N"], {"N": nugget_id, "I": ingot_id},
                          f"{MOD_ID}:{m}_chain", 1, "building"))
        write_json(recipe_path(f"{m}_door"),
                   shaped(["XX", "XX", "XX"], {"X": ingot_id}, f"{MOD_ID}:{m}_door", 3, "redstone"))
        write_json(recipe_path(f"{m}_trapdoor"),
                   shaped(["XX", "XX"], {"X": ingot_id}, f"{MOD_ID}:{m}_trapdoor", 1, "redstone"))

        # tools
        write_json(recipe_path(f"{m}_sword"),
                   shaped(["X", "X", "#"], {"X": ingot_id, "#": stick}, f"{MOD_ID}:{m}_sword", 1, "equipment"))
        write_json(recipe_path(f"{m}_pickaxe"),
                   shaped(["XXX", " # ", " # "], {"X": ingot_id, "#": stick}, f"{MOD_ID}:{m}_pickaxe", 1, "equipment"))
        write_json(recipe_path(f"{m}_axe"),
                   shaped(["XX", "X#", " #"], {"X": ingot_id, "#": stick}, f"{MOD_ID}:{m}_axe", 1, "equipment"))
        write_json(recipe_path(f"{m}_shovel"),
                   shaped(["X", "#", "#"], {"X": ingot_id, "#": stick}, f"{MOD_ID}:{m}_shovel", 1, "equipment"))
        write_json(recipe_path(f"{m}_hoe"),
                   shaped(["XX", " #", " #"], {"X": ingot_id, "#": stick}, f"{MOD_ID}:{m}_hoe", 1, "equipment"))

        # armor
        write_json(recipe_path(f"{m}_helmet"),
                   shaped(["XXX", "X X"], {"X": ingot_id}, f"{MOD_ID}:{m}_helmet", 1, "equipment"))
        write_json(recipe_path(f"{m}_chestplate"),
                   shaped(["X X", "XXX", "XXX"], {"X": ingot_id}, f"{MOD_ID}:{m}_chestplate", 1, "equipment"))
        write_json(recipe_path(f"{m}_leggings"),
                   shaped(["XXX", "X X", "X X"], {"X": ingot_id}, f"{MOD_ID}:{m}_leggings", 1, "equipment"))
        write_json(recipe_path(f"{m}_boots"),
                   shaped(["X X", "X X"], {"X": ingot_id}, f"{MOD_ID}:{m}_boots", 1, "equipment"))


# ---------------------------------------------------------------------------
# Tags
# ---------------------------------------------------------------------------

def tag_block(*name):
    return os.path.join(DATA, "minecraft", "tags", "block", *name) + ".json"


def gen_tags():
    all_blocks = []
    storage_blocks = []
    for m in MATERIALS:
        for name in ["block", "bars", "lantern", "chain", "door", "trapdoor"]:
            all_blocks.append(f"{MOD_ID}:{m}_{name}")
        storage_blocks.append(f"{MOD_ID}:{m}_block")

    write_json(tag_block("mineable", "pickaxe"), {"replace": False, "values": all_blocks})
    write_json(tag_block("needs_stone_tool"), {"replace": False, "values": storage_blocks})
    write_json(tag_block("beacon_base_blocks"), {"replace": False, "values": storage_blocks})

    # Fabric common tags for cross-mod compatibility
    c_item = os.path.join(DATA, "c", "tags", "item")
    write_json(os.path.join(c_item, "ingots.json"),
               {"replace": False, "values": [f"{MOD_ID}:wrought_iron_ingot", f"{MOD_ID}:steel_ingot"]})
    write_json(os.path.join(c_item, "nuggets.json"),
               {"replace": False, "values": [f"{MOD_ID}:wrought_iron_nugget", f"{MOD_ID}:steel_nugget"]})
    write_json(os.path.join(c_item, "storage_blocks.json"),
               {"replace": False, "values": [f"{MOD_ID}:wrought_iron_block", f"{MOD_ID}:steel_block"]})


# ---------------------------------------------------------------------------
# Lang
# ---------------------------------------------------------------------------

def gen_lang():
    lang = {"itemgroup.wroughtiron.general": "Wrought Iron & Steel"}
    for m in MATERIALS:
        pretty = PRETTY[m]
        lang[f"item.{MOD_ID}.{m}_ingot"] = f"{pretty} Ingot"
        lang[f"item.{MOD_ID}.{m}_nugget"] = f"{pretty} Nugget"
        for tool, label in [("sword", "Sword"), ("pickaxe", "Pickaxe"), ("axe", "Axe"),
                            ("shovel", "Shovel"), ("hoe", "Hoe")]:
            lang[f"item.{MOD_ID}.{m}_{tool}"] = f"{pretty} {label}"
        for piece, label in [("helmet", "Helmet"), ("chestplate", "Chestplate"),
                            ("leggings", "Leggings"), ("boots", "Boots")]:
            lang[f"item.{MOD_ID}.{m}_{piece}"] = f"{pretty} {label}"
        lang[f"block.{MOD_ID}.{m}_block"] = f"Block of {pretty}"
        lang[f"block.{MOD_ID}.{m}_bars"] = f"{pretty} Bars"
        lang[f"block.{MOD_ID}.{m}_lantern"] = f"{pretty} Lantern"
        lang[f"block.{MOD_ID}.{m}_chain"] = f"{pretty} Chain"
        lang[f"block.{MOD_ID}.{m}_door"] = f"{pretty} Door"
        lang[f"block.{MOD_ID}.{m}_trapdoor"] = f"{pretty} Trapdoor"
    write_json(os.path.join(ASSETS, "lang", "en_us.json"), lang)


# ---------------------------------------------------------------------------
def main():
    gen_textures()
    gen_item_models()
    gen_block_models()
    gen_blockstates()
    gen_loot_tables()
    gen_recipes()
    gen_tags()
    gen_lang()
    print("Generated assets and data for", MOD_ID)


if __name__ == "__main__":
    main()
