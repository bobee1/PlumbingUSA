"""Renders PNG icons and the default social image from the brand SVGs (needs Chrome + Playwright)."""
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent.parent
S = ROOT / "src" / "static"
B = S / "img" / "brand"
jobs = [("pipemend-app-icon-small.svg", 32, S / "favicon-32.png"), ("pipemend-app-icon.svg", 180, S / "apple-touch-icon.png"),
        ("pipemend-app-icon.svg", 192, S / "img" / "logo-192.png"), ("pipemend-app-icon.svg", 512, S / "img" / "logo-512.png")]
og = """<html><body style="margin:0;width:1200px;height:630px;background:radial-gradient(120% 140% at 100% 0,#17506a 0,#0f2d3d 58%);font-family:'Inter Display',sans-serif;position:relative;overflow:hidden">
<img src="pipemend-logo-reversed.svg" style="position:absolute;left:96px;top:150px;height:120px">
<p style="position:absolute;left:100px;top:330px;margin:0;color:#e6eef2;font-size:52px;font-weight:700;line-height:1.15">Plumbing repairs, drains and<br>water heaters across the U.S.</p>
<div style="position:absolute;left:0;right:0;bottom:0;height:22px;background:#a84b18"></div>
</body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    tmp = B / "_render.html"
    for svg, size, out in jobs:
        pg = b.new_page(viewport={"width": size, "height": size})
        tmp.write_text(f'<html><body style="margin:0;background:transparent"><img src="{svg}" width="{size}" height="{size}"></body></html>')
        pg.goto(tmp.as_uri())
        pg.wait_for_timeout(100)
        pg.screenshot(path=str(out), omit_background=True)
    pg = b.new_page(viewport={"width": 1200, "height": 630})
    tmp.write_text(og)
    pg.goto(tmp.as_uri()); pg.wait_for_timeout(200)
    pg.screenshot(path=str(S / "img" / "og-default.jpg"), type="jpeg", quality=88)
    b.close()
    tmp.unlink()
print("done")
