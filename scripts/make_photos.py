"""Crops Pexels downloads to 3:2 and writes WebP at 1200 and 800 px wide (each under 200 KB).
Usage: python3 -I scripts/make_photos.py <download_dir>   (reads src/photos.json for ids, slugs and crop focus)"""
import json, sys
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "src" / "static" / "img" / "p"
dl = Path(sys.argv[1])
for p in json.loads((ROOT / "src" / "photos.json").read_text()):
    im = Image.open(dl / f"{p['id']}.jpg").convert("RGB")
    w, h = im.size
    fy = p.get("focus_y", 0.5)
    if w / h > 1.5:
        nw = int(h * 1.5); x0 = int((w - nw) * p.get("focus_x", 0.5)); im = im.crop((x0, 0, x0 + nw, h))
    else:
        nh = int(w / 1.5); y0 = int((h - nh) * fy); im = im.crop((0, y0, w, y0 + nh))
    for width, suffix in ((1200, "-1200"), (800, "")):
        r = im.resize((width, int(width / 1.5)), Image.LANCZOS)
        q = 80
        while True:
            f = OUT / f"{p['slug']}{suffix}.webp"
            r.save(f, "WEBP", quality=q, method=6)
            if f.stat().st_size < 190_000 or q < 50: break
            q -= 5
        print(f.name, f.stat().st_size // 1024, "KB q", q)
