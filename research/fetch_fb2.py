"""Download the harvested Oasis Tavern Facebook photos (research/fb-harvest.json),
dedupe by average hash, and build a contact sheet so the keepers can be picked by eye."""
import json, os, sys, urllib.request, concurrent.futures
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "fb2-harvest.json")
OUT = os.path.join(HERE, "fb2")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"


def load():
    data = json.load(open(SRC, encoding="utf-8"))
    if isinstance(data, dict):
        data = list(data.values())
    return [d for d in data if d.get("src")]


def grab(rec):
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "%s.jpg" % rec["fbid"])
    if os.path.exists(path) and os.path.getsize(path) > 2000:
        return path
    try:
        req = urllib.request.Request(rec["src"], headers={"User-Agent": UA})
        blob = urllib.request.urlopen(req, timeout=45).read()
        open(path, "wb").write(blob)
        return path
    except Exception as e:
        print("FAIL", rec["fbid"], e)
        return None


def ahash(im, n=12):
    g = im.convert("L").resize((n, n), Image.LANCZOS)
    px = list(g.getdata())
    avg = sum(px) / len(px)
    return "".join("1" if p > avg else "0" for p in px)


def ham(a, b):
    return sum(x != y for x, y in zip(a, b))


def main():
    recs = load()
    print("records", len(recs))
    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        paths = [p for p in ex.map(grab, recs) if p]
    print("downloaded", len(paths))
    # dedupe: keep the largest of each near-duplicate group
    items = []
    for p in paths:
        try:
            im = Image.open(p)
            items.append((p, ahash(im), im.size[0] * im.size[1], im.size))
        except Exception as e:
            print("bad", p, e)
    items.sort(key=lambda t: -t[2])
    keep = []
    for p, h, area, size in items:
        if any(ham(h, k[1]) <= 4 for k in keep):
            continue
        keep.append((p, h, area, size))
    print("unique", len(keep))
    # contact sheet
    cols, tw, th = 6, 260, 260
    rows = (len(keep) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * (th + 20)), (18, 18, 18))
    d = ImageDraw.Draw(sheet)
    for i, (p, h, area, size) in enumerate(keep):
        im = Image.open(p).convert("RGB")
        im.thumbnail((tw, th))
        x, y = (i % cols) * tw, (i // cols) * (th + 20)
        sheet.paste(im, (x + (tw - im.width) // 2, y))
        d.text((x + 4, y + th + 3), "%s %dx%d" % (os.path.basename(p)[:-4], size[0], size[1]), fill=(230, 230, 230))
    sheet.save(os.path.join(HERE, "fb2-sheet.jpg"), quality=78)
    json.dump([os.path.basename(k[0]) for k in keep], open(os.path.join(HERE, "fb2-keep.json"), "w"))
    print("sheet written")


if __name__ == "__main__":
    main()
