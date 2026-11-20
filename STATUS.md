# PipeMend — Build Status

Nationwide plumbing services site. Brand **PipeMend**, domain **pipemend.us** (no DNS records on 2026-11-19, so very likely unregistered; not yet purchased).
Plan: "Nationwide Plumber Lead-Gen Site — Master Plan" (Claude doc, https://claude.ai/artifact/TmMBuMtsxGkkjk7koFm5BK). Rules: "Local Service Site SEO Criteria & AI Prompt" and "Blog Post Criteria & SEO Writing Prompt".
Full step log: [docs/RECORD-REGISTER.md](docs/RECORD-REGISTER.md).

Last updated: 2026-11-20 (Build 6)

## Previous
- Master plan written (2026-11-16): one national brand, metro hubs and city pages, Semrush keyword table for 20 plumbing services, state licensing-advertising risks, Cloudflare hosting.
- Build 1 (2026-11-19): engine, Deep Water + Copper design, logo set, 8 Pexels photos as WebP, 9 pages (home with system diagram, About, Contact form, Privacy, Terms, Disclaimer, Editorial, Accessibility, 404); audit 0 issues.
- Build 2 (2026-11-20): Semrush research (~4,700 units), competitor reads, site plan doc https://claude.ai/artifact/Lnvtnd4rBMx8H6m4StHfiB, approved by the owner on 2026-11-20 ("Build 3").
- Build 3 (2026-11-20): services hub and first 10 service pages (emergency, drain cleaning, hydro jetting, water heater repair and installation, tankless, sewer line, leak detection, slab leak, repiping); home trimmed to 1,771 words; audit 0 issues.
- Build 3b (2026-11-20): remaining 9 service pages (water line, toilet, faucet, garbage disposal, sump pump, gas line, water softener, backflow, commercial); all 19 services live; audit 0 issues.
- Build 4 (2026-11-20): locations hub and 51 state pages (housing age, heating fuel, FEMA water disasters, plumbing licensing authority per state, hand-written local copy); audit 0 issues.
- Build 5 (2026-11-20): guides hub, 12 guides (1,389–1,996 words, each at or above its competitor benchmark), branded featured images, glossary of 58 terms, helpful-guide links on every service and state page; audit 0 issues.
- Owner decisions (2026-11-19): target plumbing and every sub-service in all states and cities; brand PipeMend; doma## Current — Build 6: first 25 Wave 1 city pages (done)
- **25 city pages** at `/locations/<state>/<city>/`: Phoenix, Austin, Los Angeles, Las Vegas, Dallas, San Diego, Houston, Denver, Fort Worth, Salt Lake City, Portland, Chicago, Seattle, Sacramento, Mesa, San Antonio, Atlanta, Plano, Philadelphia, Charlotte, Minneapolis, Cincinnati, Baltimore, Tucson, Miami. Chosen as the top-ranked Wave 1 cities (Semrush "plumber <city>" volume and KD from research/06) with full Census data.
- **Each page (955–1,079 words):** quick answer, at-a-glance table (homes, owner share, median build year, pre-1980 and pre-1940 share, main heating fuel, water utility), housing-age chart, why plumbing differs there, water supply, top-4 problems table linked to services, water heater and gas notes, 4 local tips, neighborhoods, permit office and licensing body, 4 FAQs, service pills, nearby cities, 3 helpful guides, sources. LocalBusiness/Service + FAQPage + BreadcrumbList schema.
- **Data:** Census ACS 2020–2024 5-year city figures (`research/10-city-acs.json`, `research/11-city-heating-fuel.json`); city facts in `src/metros/meta.json` and hand-written copy in `src/metros/content/<slug>.json` (no invented hardness numbers or prices).
- **Internal links:** state pages list their city pages; locations hub has a "City pages" section; home page links all city pages; city pages link nearby cities, their state, services and guides.
- **Checks:** audit PASS 0 issues; reading grade ≤9 on every page; no duplicate paragraphs; site audit clean; no overflow at 360/768/1280.
- **Held back on purpose:** Washington, D.C. stays on its state page (a city page would compete with it). Scottsdale, Chandler, Anaheim, San Francisco and New Orleans are missing from the city Census file, so they move to Build 6b once their data is pulled.
- **Semrush:** still "ERROR 122 wrong format or empty key" on 2026-11-20; city keyword data comes from the Nov 19–20 pull.

nd SERPs were checked by web search with one competitor page read per guide.
- **Checks:** audit PASS 0 issues; reading grade 4.8–7.8; no duplicate paragraphs; site audit clean; no overflow or console errors at 360/768/1280.

## Coming
| Build | Scope | Needs from owner |
| --- | --- | --- |
| 6b (next) | Scottsdale, Chandler, Anaheim, San Francisco, New Orleans (after Census pull) + next Wave 1 cities from rank 26 (Orlando, Arlington, Colorado Springs, Raleigh, …) | — |
| 7, 7b | Wave 2 cities, 25 per build | — |
| 8+ | Wave 3 towns (50+ searches/mo) 25 per build; next guides; Search Console refreshes | Search Console access once live |
| Launch | Buy pipemend.us, Cloudflare Pages project, real toll-free number, email, Resend keys | Domain, number, email, Resend key |

## Open items
- **Phone number:** 1-800-555-0199 is in the 555-01xx range reserved for fiction and cannot receive calls. Swap after deployment: change `phone_display` / `phone_e164` in `src/site.json`, rebuild and push.
- **Domain:** buy pipemend.us soon (pipemend.com also had no DNS records on 2026-11-19).
- **Email:** add to `src/site.json` once the domain is bought.
- **Resend env vars** for the contact form: `RESEND_API_KEY`, `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL`.
- **Licensing-ad risk (owner aware):** Georgia, Texas, Illinois, Maryland, California and Minnesota limit plumbing ads to licensed plumbers. Pages say work is done by licensed local plumbers; each state page now names its licensing authority.
- **Low inbound links:** Miami and Cincinnati have no other live city nearby yet; Orlando/Tampa and Columbus/Cleveland in later builds will link them.
- **Semrush key:** the Semrush connector returned "wrong format or empty key" on 2026-11-20. Still failing in Build 6. Reconnect or check the API key so later city waves can use fresh SERP data.
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
