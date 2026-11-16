"""Render version-separated public means to PNG. Requires Pillow; no hardware tests."""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "benchmarks.json").read_text(encoding="utf-8"))
SCALE = 2
W, H = 1260, 1110
image = Image.new("RGB", (W*SCALE, H*SCALE), "#f7f9fc")
draw = ImageDraw.Draw(image)


def font(size, bold=False):
    names = (["C:/Windows/Fonts/arialbd.ttf", "DejaVuSans-Bold.ttf"] if bold
             else ["C:/Windows/Fonts/arial.ttf", "DejaVuSans.ttf"])
    for name in names:
        try:
            return ImageFont.truetype(name, int(size*SCALE))
        except OSError:
            pass
    return ImageFont.load_default(size=int(size*SCALE))


def text(x, y, label, size=17, bold=False, color="#14213d", anchor=None):
    draw.text((x*SCALE, y*SCALE), label, font=font(size, bold), fill=color, anchor=anchor)


def line(points, color="#d5dde8", width=1):
    draw.line([(int(x*SCALE), int(y*SCALE)) for x, y in points], fill=color, width=width*SCALE)


text(38, 25, "Workload and version determine the comparison", 29, True)
text(38, 68, "Public aggregate means | benchmark snapshot: 13 November 2026", 18)
text(38, 97, "Unmatched submissions; no causal attribution. Apple and PassMark results excluded.", 16)

panels = [
    ("stockfish_17_1", 160, "Stockfish 17.1", "Million nodes/s | HIGHER is better", 45, 1e6),
    ("llvm_16_ninja", 465, "LLVM 16.0 / Ninja", "Seconds | LOWER is better", 360, 1),
    ("llvm_21_1_ninja", 770, "LLVM 21.1 / Ninja", "Seconds | LOWER is better", 360, 1),
]
# The recorded key names are checked rather than silently replacing one version.
for key, top, title, unit, limit, divisor in panels:
    rows = DATA[key]
    text(38, top, title, 23, True)
    text(38, top+32, unit, 17)
    left, right = 320, 1120
    for tick in range(5):
        x = left + (right-left)*tick/4
        line([(x, top+73), (x, top+247)])
        text(x, top+257, f"{limit*tick/4:g}", 15, anchor="mt")
    for index, row in enumerate(rows):
        y = top+91+index*44
        value = row["value"]/divisor
        text(left-18, y, row["cpu"], 17, anchor="rm")
        width = (right-left)*value/limit
        color = "#6941b8" if "Ryzen" in row["cpu"] else "#176da7"
        draw.rounded_rectangle(
            (left*SCALE, (y-13)*SCALE, (left+width)*SCALE, (y+13)*SCALE),
            radius=4*SCALE, fill=color)
        label = f"{value:.3f}" if divisor != 1 else f"{value:g}"
        text(left+width+12, y, label, 17, True, anchor="lm")

text(38, 1080, "Exact values, source cutoffs, published spread fields and result counts appear in README.md.", 16)
image.save(ROOT / "verified-results.png", optimize=True)
print(f"Rendered verified-results.png: {image.width} x {image.height}")
