"""Builds PipeMend logo SVGs. Wordmark: Inter Display ExtraBold (SIL OFL) converted to outlines.

Mark: a house (the home) holding a water drop, crossed by a copper pipe band with a
coupling, plus a small four-point copper sparkle for "fixed and mended".
Colors: deep water #0f2d3d, aqua #3fb3cf, copper #a84b18 / #d9824a, white.
Run: python3 scripts/make_logo.py src/static/img/brand
"""
import os
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

WATER, AQUA, COPPER, COPPER_SOFT, WHITE = "#0f2d3d", "#3fb3cf", "#a84b18", "#e39a64", "#ffffff"
font = TTFont("/usr/share/fonts/opentype/inter/InterDisplay-ExtraBold.otf")
gs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
upm = font["head"].unitsPerEm


def text_paths(text, size, x0, baseline, tracking=-0.02):
    s = size / upm
    out, x = [], x0
    for ch in text:
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, baseline)))
        out.append(pen.getCommands())
        x += hmtx[g][0] * s + tracking * size
    return out, x - tracking * size


# ---- the mark (viewBox 64x64)
HOUSE = "M32 4.5 4.5 27.2c-1.7 1.4-.7 4.1 1.5 4.1H10V56a3.5 3.5 0 0 0 3.5 3.5h37A3.5 3.5 0 0 0 54 56V31.3h4c2.2 0 3.2-2.7 1.5-4.1L32 4.5z"
DROP = "M32 17.5c-1.3 5.2-10.5 13.2-10.5 21.3a10.5 10.5 0 0 0 21 0c0-8.1-9.2-16.1-10.5-21.3z"
SHINE = "M26.6 39.6c.2 2.6 1.6 4.7 3.9 5.7.8.3.4 1.5-.4 1.3-3.1-.8-5.1-3.6-5.2-6.8 0-.9 1.6-1.1 1.7-.2z"
PIPE = "M10 50.5h44v5H10z"
COUPLING = "M27 48.5h10v9H27z"
SPARK = "M48.5 9.5c.5 3 1.5 4 4.5 4.5-3 .5-4 1.5-4.5 4.5-.5-3-1.5-4-4.5-4.5 3-.5 4-1.5 4.5-4.5z"


def mark(house, drop, pipe, coupling, spark, small=False):
    sp = "" if small else f'<path d="{SPARK}" fill="{spark}"/>'
    sh = "" if small else f'<path d="{SHINE}" fill="{WHITE}" fill-opacity=".85"/>'
    return (f'<path d="{HOUSE}" fill="{house}"/><path d="{PIPE}" fill="{pipe}"/><path d="{COUPLING}" fill="{coupling}"/>'
            f'<path d="{DROP}" fill="{drop}"/>{sh}{sp}')


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{body}</svg>\n')


OUT = sys.argv[1] if len(sys.argv) > 1 else "."
files = {}
std = (WATER, AQUA, COPPER, COPPER_SOFT, COPPER)
files["pipemend-mark.svg"] = svg(64, 64, mark(*std), "PipeMend")
files["pipemend-mark-small.svg"] = svg(64, 64, mark(*std, small=True), "PipeMend")
files["pipemend-mark-mono.svg"] = svg(64, 64, mark(WATER, WHITE, WATER, WATER, WATER), "PipeMend")
app = (WHITE, AQUA, COPPER_SOFT, COPPER, COPPER_SOFT)
files["pipemend-app-icon.svg"] = svg(64, 64,
    f'<rect width="64" height="64" rx="14" fill="{WATER}"/><g transform="translate(8 7) scale(.75)">{mark(*app)}</g>', "PipeMend")
files["pipemend-app-icon-small.svg"] = svg(64, 64,
    f'<rect width="64" height="64" rx="14" fill="{WATER}"/><g transform="translate(6.4 5.6) scale(.8)">{mark(*app, small=True)}</g>', "PipeMend")


def lockup(pipe_c, mend_c, m):
    size, base = 46, 48
    a, x = text_paths("Pipe", size, 76, base)
    b, x2 = text_paths("Mend", size, x + 0.5, base)
    w = int(x2 + 4)
    body = (mark(*m) + f'<g fill="{pipe_c}">' + "".join(f'<path d="{d}"/>' for d in a)
            + f'</g><g fill="{mend_c}">' + "".join(f'<path d="{d}"/>' for d in b) + "</g>")
    return svg(w, 64, body, "PipeMend"), w


files["pipemend-logo.svg"], W = lockup(WATER, COPPER, std)
files["pipemend-logo-reversed.svg"], _ = lockup(WHITE, COPPER_SOFT, app)
files["pipemend-logo-mono.svg"], _ = lockup(WATER, WATER, (WATER, WHITE, WATER, WATER, WATER))

for name, data in files.items():
    with open(os.path.join(OUT, name), "w") as fh:
        fh.write(data)
print("lockup width", W)
