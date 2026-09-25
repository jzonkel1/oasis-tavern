"""Resize the rendered share card to 1200x630, check the headline sits in the center safe box, and build QA contact sheets."""
import os, glob
from PIL import Image
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
im = Image.open("research/og-2x.png").convert("RGB").resize((1200, 630), Image.LANCZOS)
im.save("assets/img/og.jpg", quality=88, optimize=True)
g = im.crop((0, 330, 1200, 470)).convert("L")
cols = [x for x in range(1200) if max(g.getpixel((x, y)) for y in range(0, 140, 4)) > 200]
print("headline spans", min(cols), max(cols), "safe 285-915")
for name, ncols in (("mobile", 4), ("desktop", 2)):
    fs = sorted(glob.glob("research/shots/%s-0*.png" % name))
    ims = [Image.open(f) for f in fs]
    w, h = ims[0].size
    rows = (len(ims) + ncols - 1) // ncols
    sheet = Image.new("RGB", (ncols * w // 2, rows * h // 2), (0, 0, 0))
    for i, x in enumerate(ims):
        sheet.paste(x.resize((w // 2, h // 2)), ((i % ncols) * w // 2, (i // ncols) * h // 2))
    sheet.save("research/shots/_%s-sheet.jpg" % name, quality=70)
print("sheets ok")
