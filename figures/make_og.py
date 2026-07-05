#!/usr/bin/env python3
"""Generate the social preview image and favicon for the Drift-VLA page."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
IMAGES = HERE.parent / "static" / "images"
SCALE = 2
W, H = 1200 * SCALE, 630 * SCALE

BLUE = "#2a78d6"
AQUA = "#1baf7a"
INK = "#0b0b0b"
INK_2 = "#52514e"
HAIRLINE = "#e1e0d9"
PANEL = "#f8fbff"


def font(size, bold=False):
    root = Path("/opt/conda/envs/lerobot/fonts")
    name = "Ubuntu-B.ttf" if bold else "Ubuntu-R.ttf"
    return ImageFont.truetype(str(root / name), size * SCALE)


def xy(box):
    return tuple(int(v * SCALE) for v in box)


def center_text(draw, y, text, size, fill, bold=False):
    f = font(size, bold)
    bbox = draw.textbbox((0, 0), text, font=f)
    x = (W - (bbox[2] - bbox[0])) // 2
    draw.text((x, int(y * SCALE)), text, font=f, fill=fill)


def card(draw, x, y, w, h, title, value, note, accent):
    draw.rounded_rectangle(xy((x, y, x + w, y + h)), radius=18 * SCALE, fill="white", outline=accent, width=2 * SCALE)
    draw.ellipse(xy((x + 27, y + 29, x + 41, y + 43)), fill=accent)
    draw.text(xy((x + 54, y + 24)), title, font=font(22, True), fill=INK)
    draw.text(xy((x + 28, y + 77)), value, font=font(37, True), fill=accent)
    draw.text(xy((x + 28, y + 122)), note, font=font(19), fill=INK_2)


img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

draw.rounded_rectangle(xy((54, 50, 1146, 580)), radius=28 * SCALE, fill=PANEL, outline=HAIRLINE, width=1 * SCALE)
center_text(draw, 83, "Drift-VLA", 54, INK, True)
center_text(draw, 153, "One-step action generation with action-dimension drifting", 27, BLUE, True)
center_text(draw, 202, "SmolVLA backbone, 1-NFE inference, KeyStone self-consistency", 22, INK_2)

card(draw, 115, 285, 290, 170, "Best success", "92.3 ±0.6%", "LIBERO-Spatial", BLUE)
card(draw, 455, 285, 290, 170, "Latency", "53.5 ms", "per action chunk", AQUA)
card(draw, 795, 285, 290, 170, "Real robot", "LeKiwi", "shopping rollouts", BLUE)

draw.rounded_rectangle(xy((390, 500, 810, 506)), radius=3 * SCALE, fill=AQUA)
center_text(draw, 525, "Drift-VLA + KeyStone keeps one-step speed while improving robustness.", 21, INK, True)

img = img.resize((1200, 630), Image.Resampling.LANCZOS)
img.save(IMAGES / "og_preview.png", quality=95)
print(f"wrote {IMAGES / 'og_preview.png'}")

favicon = Image.new("RGB", (64, 64), BLUE)
fd = ImageDraw.Draw(favicon)
fd.rounded_rectangle((7, 7, 57, 57), radius=12, fill=BLUE)
fd.text((19, 11), "D", font=ImageFont.truetype("/opt/conda/envs/lerobot/fonts/Ubuntu-B.ttf", 40), fill="white")
favicon.save(IMAGES / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print(f"wrote {IMAGES / 'favicon.ico'}")
