# PipeMend — Build Status

Nationwide plumbing services site. Brand **PipeMend**, domain **pipemend.us** (no DNS records on 2026-11-19, so very likely unregistered; not yet purchased).
Plan: "Nationwide Plumber Lead-Gen Site — Master Plan" (Claude doc, https://claude.ai/artifact/TmMBuMtsxGkkjk7koFm5BK). Rules: "Local Service Site SEO Criteria & AI Prompt" and "Blog Post Criteria & SEO Writing Prompt".
Full step log: [docs/RECORD-REGISTER.md](docs/RECORD-REGISTER.md).

Last updated: 2026-11-20

## Previous
- Master plan written (2026-11-16): one national brand, metro hubs and city pages, Semrush keyword table for 20 plumbing services, state licensing-advertising risks, Cloudflare hosting.
- Build 1 (2026-11-19): engine, Deep Water + Copper design, logo set, 8 Pexels photos as WebP, 9 pages (home with system diagram, About, Contact form, Privacy, Terms, Disclaimer, Editorial, Accessibility, 404); audit 0 issues.
- Build 2 (2026-11-20): Semrush research (~4,700 units), competitor reads, site plan doc https://claude.ai/artifact/Lnvtnd4rBMx8H6m4StHfiB, approved by the owner on 2026-11-20 ("Build 3").
- Owner decisions (2026-11-19): target plumbing and every sub-service in all states and cities; brand PipeMend; domain pipemend.us; own-business call routing like SootMend (24/7, 10+ years); legal owner Anjam Javed; toll-free 1-800-555-0199 until after deployment; repo github.com/bobee1/PlumbingUSA; Pexels photos as WebP or illustrations.

## Current — Build 3: Services hub and first 10 service pages (done)
- **Services hub** `/services/`: 19 service cards (9 shown unlinked until Build 3b), "which service do I need" table, hiring checklist.
- **10 service pages:** emergency plumbing, drain cleaning, hydro jetting, water heater repair, water heater installation, tankless water heaters, sewer line repair, leak detection, slab leak repair, pipe repair and repiping. 1,095–1,377 words each, quick answer, checklist, comparison table, process steps, cost factors, DIY-or-pro, prevention, 5 FAQs, Service + FAQPage schema, Wikipedia entities, 3–4 opened government or industry sources.
- **Photos:** 10 more Pexels photos as WebP (1200 + 800 px, all under 200 KB); tankless and slab leak use new SVG diagrams with a separate mobile version. Three photos held for Build 3b (water softener, water line, garbage disposal).
- **Home:** trimmed to 1,771 words after the services grid grew to 19; the plumbing-system legend now links to 7 service pages.
- **Engine:** tables wrap in a scrollable region on small screens; `{{near_you}}` and `{{helpful_guides:...}}` placeholders render empty until state pages (Build 4) and guides (Build 5) exist, then fill in automatically.
- **Checks:** audit PASS 0 issues; reading grade 5.0–7.4; site audit clean; no horizontal overflow at 360/768/1280.

## Coming
| Build | Scope | Needs from owner |
| --- | --- | --- |
| 3b (next) | Remaining 9 service pages (water line, toilet, faucet, garbage disposal, sump pump, gas line, water softener, backflow testing, commercial), then the hub cards and related links go live | — |
| 4 | Locations hub and 51 state pages (licensing board, permits, freeze, slab and hard-water risks) | — |
| 5 | Guides hub, 12 guides, 50+ term glossary | — |
| 6, 6b | Wave 1 cities, 25 per build | — |
| 7, 7b | Wave 2 cities, 25 per build | — |
| 8+ | Wave 3 towns (50+ searches/mo) 25 per build; next guides; Search Console refreshes | Search Console access once live |
| Launch | Buy pipemend.us, Cloudflare Pages project, real toll-free number, email, Resend keys | Domain, number, email, Resend key |

## Open items
- **Phone number:** 1-800-555-0199 is in the 555-01xx range reserved for fiction and cannot receive calls. Swap after deployment: change `phone_display` / `phone_e164` in `src/site.json`, rebuild and push.
- **Domain:** buy pipemend.us soon (pipemend.com also had no DNS records on 2026-11-19).
- **Email:** add to `src/site.json` once the domain is bought.
- **Resend env vars** for the contact form: `RESEND_API_KEY`, `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL`.
- **Licensing-ad risk (owner aware):** Georgia, Texas, Illinois, Maryland, California and Minnesota limit plumbing ads to licensed plumbers. Pages say work is done by licensed local plumbers; state pages in Build 4 will name each licensing board.
- **Deferred on service pages:** the "Local note" paragraph and "plumbers near you" links return in Build 4; "helpful guides" links in Build 5.
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
