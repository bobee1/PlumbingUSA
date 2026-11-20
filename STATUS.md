# PipeMend — Build Status

Nationwide plumbing services site. Brand **PipeMend**, domain **pipemend.us** (no DNS records on 2026-11-19, so very likely unregistered; not yet purchased).
Plan: "Nationwide Plumber Lead-Gen Site — Master Plan" (Claude doc, https://claude.ai/artifact/TmMBuMtsxGkkjk7koFm5BK). Rules: "Local Service Site SEO Criteria & AI Prompt" and "Blog Post Criteria & SEO Writing Prompt".
Full step log: [docs/RECORD-REGISTER.md](docs/RECORD-REGISTER.md).

Last updated: 2026-11-19

## Previous
- Master plan written (2026-11-16): one national brand, metro hubs and city pages, Semrush keyword table for 20 plumbing services, state licensing-advertising risks, Cloudflare hosting.
- Owner decisions (2026-11-19): target plumbing and every sub-service in all states and cities; brand PipeMend; domain pipemend.us; own-business call routing like SootMend (24/7, 10+ years); legal owner Anjam Javed; toll-free 1-800-555-0199 until after deployment; repo github.com/bobee1/PlumbingUSA; Pexels photos as WebP or illustrations.

## Current — Build 1: Foundation, home, trust and legal pages (done)
- **Engine:** `build.py` forked from the SootMend engine and rebranded; schema business type `Plumber`; offer catalog lists all 13 services (URLs added as each page goes live); sidebar and footer list only pages that exist.
- **Design system "Deep Water + Copper":** deep water #0f2d3d, copper #a84b18 (call buttons, 5.7:1 with white), link #0a5c72 (7.5:1), aqua #1d8fb0 and teal #1d7f78 accents. Contrast checked.
- **Logo set:** house + water drop + copper pipe band and sparkle; standard, reversed, mono lockups, marks, app icons, favicon, PNG icons and 1200×630 social image (`scripts/make_logo.py`, `scripts/make_brand_png.py`).
- **Photos:** 8 Pexels photos cropped 3:2, WebP at 1200 and 800 px, 9–164 KB (`scripts/make_photos.py`, `src/photos.json`). 4 used, 4 held for service pages. No photo repeats.
- **Pages (9):** home (1,795 words, 7 FAQs, "how water moves through a house" diagram with numbered legend), About (with "how a call works" illustration), Contact (safety steps + form → Pages Function → Resend), Privacy, Terms, Disclaimer, Editorial policy, Accessibility, 404.
- **Sources opened and cited:** EPA WaterSense (leaks), EPA mold guide (24–48 h drying), American Red Cross (frozen pipes), PHMSA (gas leaks), Insurance Information Institute (burst pipes vs. sewer backups).
- **Checks:** audit PASS 0 issues; reading grade 5.4–6.0 on content pages (legal exempt); site audit clean; no overflow or console errors at 360/768/1280.

## Coming
| Build | Scope | Needs from owner |
| --- | --- | --- |
| 2 | Keyword research and site plan: Semrush pull for ~60 service keywords, city demand for the top 100+ cities, question keywords, top-10 competitor benchmark; keyword map for home + 13 services; Wave 1 city list; 12-guide blog map. Plan doc for approval. | Approve the plan |
| 3 | Services hub and 13 service pages (1,000–1,500+ words each, sources, FAQs, competitor term coverage), Pexels photos. | — |
| 4 | Locations hub, 50 state pages + DC (licensing board, permit notes, climate risks such as freezes and slab leaks, hard water data). | — |
| 5 | Guides hub, 12 guides and a 50+ term plumbing glossary. | — |
| 6+ | City pages in batches of 25 (unique local data each), then suburbs scored from Semrush, until every city with demand is covered. | Search Console access once live |
| Launch | Buy pipemend.us, Cloudflare Pages project, real toll-free number, email, Resend keys, Search Console + analytics. | Domain, number, email, Resend key |

## Open items
- **Phone number:** 1-800-555-0199 is in the 555-01xx range reserved for fiction and cannot receive calls. Swap after deployment: change `phone_display` / `phone_e164` in `src/site.json`, rebuild and push.
- **Domain:** buy pipemend.us soon (pipemend.com also had no DNS records on 2026-11-19).
- **Email:** add to `src/site.json` once the domain is bought.
- **Resend env vars** for the contact form: `RESEND_API_KEY`, `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL`.
- **Licensing-ad risk (owner aware):** Georgia, Texas, Illinois, Maryland, California and Minnesota limit plumbing ads to licensed plumbers. Pages say work is done by licensed local plumbers; state pages in Build 4 will name each licensing board.
- **Process claims to confirm:** written estimates before work, permits pulled when required, photo records after each job.

## Deployment
- Cloudflare Pages: connect `bobee1/PlumbingUSA`, branch `main`, framework preset None, no build command, build output directory `public`. `functions/` is picked up automatically for the contact form.
- Staging address `*.pages.dev` sends `X-Robots-Tag: noindex` (set in `_headers`) until pipemend.us is connected.

## How to build
```
python3 -I scripts/make_photos.py <download_dir>   # after adding photos to src/photos.json
python3 build.py                 # writes public/
python3 scripts/audit.py         # must print "PASS: 0 issues"
python3 scripts/readability.py   # reading grade <= 9, no repeated paragraphs
python3 scripts/siteaudit.py     # whole-site link, title, canonical, sitemap check
python3 scripts/make_logo.py src/static/img/brand && python3 scripts/make_brand_png.py   # after a logo change
```
