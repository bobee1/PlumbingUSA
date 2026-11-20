# PipeMend — Build Status

Nationwide plumbing services site. Brand **PipeMend**, domain **pipemend.us** (no DNS records on 2026-11-19, so very likely unregistered; not yet purchased).
Plan: "Nationwide Plumber Lead-Gen Site — Master Plan" (Claude doc, https://claude.ai/artifact/TmMBuMtsxGkkjk7koFm5BK). Rules: "Local Service Site SEO Criteria & AI Prompt" and "Blog Post Criteria & SEO Writing Prompt".
Full step log: [docs/RECORD-REGISTER.md](docs/RECORD-REGISTER.md).

Last updated: 2026-11-20 (Build 4)

## Previous
- Master plan written (2026-11-16): one national brand, metro hubs and city pages, Semrush keyword table for 20 plumbing services, state licensing-advertising risks, Cloudflare hosting.
- Build 1 (2026-11-19): engine, Deep Water + Copper design, logo set, 8 Pexels photos as WebP, 9 pages (home with system diagram, About, Contact form, Privacy, Terms, Disclaimer, Editorial, Accessibility, 404); audit 0 issues.
- Build 2 (2026-11-20): Semrush research (~4,700 units), competitor reads, site plan doc https://claude.ai/artifact/Lnvtnd4rBMx8H6m4StHfiB, approved by the owner on 2026-11-20 ("Build 3").
- Build 3 (2026-11-20): services hub and first 10 service pages (emergency, drain cleaning, hydro jetting, water heater repair and installation, tankless, sewer line, leak detection, slab leak, repiping); home trimmed to 1,771 words; audit 0 issues.
- Build 3b (2026-11-20): remaining 9 service pages (water line, toilet, faucet, garbage disposal, sump pump, gas line, water softener, backflow, commercial); all 19 services live; audit 0 issues.
- Owner decisions (2026-11-19): target plumbing and every sub-service in all states and cities; brand PipeMend; domain pipemend.us; own-business call routing like SootMend (24/7, 10+ years); legal owner Anjam Javed; toll-free 1-800-555-0199 until after deployment; repo github.com/bobee1/PlumbingUSA; Pexels photos as WebP or illustrations.

## Current — Build 4: Locations hub and 51 state pages (done)
- **Locations hub** `/locations/`: state cards grouped by Census region, a "how plumbing differs across the country" table computed from the data (oldest/newest housing, most FEMA water disasters, most gas/electric heat), 4 FAQs. 917 words.
- **51 state pages** (`/locations/<state>/`, 50 states + DC), 948–1,140 words each, built by `states.py` from:
  - `research/07-state-data.json` (Census ACS 2020–2024 housing, largest places, OpenFEMA water-related declarations since 2000) and `research/08-heating-fuel.json` (ACS 2024 heating fuel), both reused from SootMend's verified pulls;
  - `src/states/meta.json`: names, slugs, neighbors and the **plumbing licensing authority for every state**, checked against two state-by-state guides plus searches for Texas (board still active in 2026), Arkansas (Department of Health) and DC (Board of Industrial Trades). Six states license locally: KS, MO, NE, NY, PA, WY;
  - `src/states/content/<AB>.json`: hand-written local copy per state (lead, two "why" paragraphs, 4-row problems table, tips, areas, a local FAQ).
- **Each state page has:** quick answer, at-a-glance facts table, housing-age bar chart, pipes and housing age, common problems → service links, water heaters and gas lines (from heating fuel), storms and sewer backups (from FEMA), tips, licenses and permits, areas served, 4 FAQs, all 19 services, neighboring states, sources; Service schema with `areaServed`.
- **Service pages:** the "near you" block now shows "<service> near you" with links to all 51 state pages.
- **Home:** the all-50-states section links to the locations hub.
- **Checks:** audit PASS 0 issues; reading grade 6.7–9.0; no duplicate paragraphs; site audit clean; no overflow or console errors on all 52 location pages at 360/768/1280.

## Coming
| Build | Scope | Needs from owner |
| --- | --- | --- |
| 5 (next) | Guides hub, 12 guides, 50+ term glossary | — |
| 6, 6b | Wave 1 cities, 25 per build | — |
| 7, 7b | Wave 2 cities, 25 per build | — |
| 8+ | Wave 3 towns (50+ searches/mo) 25 per build; next guides; Search Console refreshes | Search Console access once live |
| Launch | Buy pipemend.us, Cloudflare Pages project, real toll-free number, email, Resend keys | Domain, number, email, Resend key |

## Open items
- **Phone number:** 1-800-555-0199 is in the 555-01xx range reserved for fiction and cannot receive calls. Swap after deployment: change `phone_display` / `phone_e164` in `src/site.json`, rebuild and push.
- **Domain:** buy pipemend.us soon (pipemend.com also had no DNS records on 2026-11-19).
- **Email:** add to `src/site.json` once the domain is bought.
- **Resend env vars** for the contact form: `RESEND_API_KEY`, `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL`.
- **Licensing-ad risk (owner aware):** Georgia, Texas, Illinois, Maryland, California and Minnesota limit plumbing ads to licensed plumbers. Pages say work is done by licensed local plumbers; each state page now names its licensing authority.
- **Deferred:** "helpful guides" links on service and state pages appear automatically in Build 5; city links on state pages in Builds 6–7.
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
