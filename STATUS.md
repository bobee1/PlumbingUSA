# PipeMend — Build Status

Nationwide plumbing services site. Brand **PipeMend**, domain **pipemend.us** (no DNS records on 2026-11-19, so very likely unregistered; not yet purchased).
Plan: "Nationwide Plumber Lead-Gen Site — Master Plan" (Claude doc, https://claude.ai/artifact/TmMBuMtsxGkkjk7koFm5BK). Rules: "Local Service Site SEO Criteria & AI Prompt" and "Blog Post Criteria & SEO Writing Prompt".
Full step log: [docs/RECORD-REGISTER.md](docs/RECORD-REGISTER.md).

Last updated: 2026-11-20 (Build 6b)

## Previous
- Master plan written (2026-11-16): one national brand, metro hubs and city pages, Semrush keyword table for 20 plumbing services, state licensing-advertising risks, Cloudflare hosting.
- Build 1 (2026-11-19): engine, Deep Water + Copper design, logo set, 8 Pexels photos as WebP, 9 pages (home with system diagram, About, Contact form, Privacy, Terms, Disclaimer, Editorial, Accessibility, 404); audit 0 issues.
- Build 2 (2026-11-20): Semrush research (~4,700 units), competitor reads, site plan doc https://claude.ai/artifact/Lnvtnd4rBMx8H6m4StHfiB, approved by the owner on 2026-11-20 ("Build 3").
- Build 3 (2026-11-20): services hub and first 10 service pages (emergency, drain cleaning, hydro jetting, water heater repair and installation, tankless, sewer line, leak detection, slab leak, repiping); home trimmed to 1,771 words; audit 0 issues.
- Build 3b (2026-11-20): remaining 9 service pages (water line, toilet, faucet, garbage disposal, sump pump, gas line, water softener, backflow, commercial); all 19 services live; audit 0 issues.
- Build 4 (2026-11-20): locations hub and 51 state pages (housing age, heating fuel, FEMA water disasters, plumbing licensing authority per state, hand-written local copy); audit 0 issues.
- Build 5 (2026-11-20): guides hub, 12 guides (1,389–1,996 words, each at or above its competitor benchmark), branded featured images, glossary of 58 terms, helpful-guide links on every service and state page; audit 0 issues.
- Build 6 (2026-11-20): first 25 Wave 1 city pages (Phoenix to Miami), city links on state pages, locations hub and ## Current — Build 6b: next 25 city pages (done)
- **25 more city pages** (50 live in total): Orlando, Arlington, Colorado Springs, Raleigh, Baton Rouge, New York, Nashville, Boise, Gilbert, Aurora, Jacksonville, Memphis, Indianapolis, Durham, Kansas City, Tampa, Cleveland, Pittsburgh, Long Beach, Reno, Columbus, Omaha, Louisville, Madison, Wichita. These are every remaining city in the Census city file, ranked 32–99 in research/06 (all Wave 1 cities with data, then the strongest Wave 2 cities).
- **Same page model as Build 6** (942–1,089 words): Census at-a-glance table and housing-age chart, water utility and source, top-4 problems linked to services, tips, neighborhoods, permit office and licensing body, 4 FAQs, nearby cities, guides, sources.
- **Local licensing handled per city:** NYC (DOB master plumber), Kansas City, Omaha and Wichita (city/MABCD licenses; no state license), Pittsburgh (Allegheny County Health Department), Nashville and Memphis (local plus Tennessee contractor license), Louisville (Kentucky Division of Plumbing).
- **Home page** now shows the top 20 cities by search demand plus an "All city pages" link to the hub, so it stays under 1,800 words as cities grow.
- **Nearby links:** Miami and Cincinnati now get links from Orlando, Tampa, Jacksonville, Columbus, Indianapolis and Louisville.
- **Checks:** audit PASS 0 issues; reading grade ≤9 on every page; no duplicate paragraphs; site audit clean (lowest city inbound links: 6); no overflow or console errors at 360/768/1280.
- **Still held back:** Washington, D.C. (stays on its state page), and Scottsdale, Chandler, Anaheim, San Francisco, New Orleans, St. Petersburg, Chula Vista, Irvine, Boston, Garland, Albuquerque, Oakland and the other Wave 1–2 cities not in the Census city file. The Census API and Census Reporter API are not reachable from this workspace, so these need a data pull.
- **Semrush:** still failing (ERROR 122).

** audit PASS 0 issues; reading grade 4.8–7.8; no duplicate paragraphs; site audit clean; no overflow or console errors at 360/768/1280.

## Coming
| Build | Scope | Needs from owner |
| --- | --- | --- |
| 6c (next) | City Census data pull (ACS 5-year: B25034, B25035, B25003, B25024, B25001, B01003, B25040) for the next 25 cities by rank (Scottsdale, Chandler, Anaheim, San Francisco, New Orleans, St. Petersburg, Chula Vista, Irvine, Boston, Garland, Albuquerque, Oakland, Glendale, Lubbock, Fremont, Irving, Richmond, Greensboro, Santa Ana, Detroit, St. Louis, Henderson, Tulsa, Virginia Beach, Lexington), then their pages | Either run a short Census script locally, or approve using a secondary source (e.g. city-stats sites quoting ACS) |
| 7, 7b | Wave 2 cities, 25 per build | — |
| 8+ | Wave 3 towns (50+ searches/mo) 25 per build; next guides; Search Console refreshes | Search Console access once live |
| Launch | Buy pipemend.us, Cloudflare Pages project, real toll-free number, email, Resend keys | Domain, number, email, Resend key |

## Open items
- **Phone number:** 1-800-555-0199 is in the 555-01xx range reserved for fiction and cannot receive calls. Swap after deployment: change `phone_display` / `phone_e164` in `src/site.json`, rebuild and push.
- **Domain:** buy pipemend.us soon (pipemend.com also had no DNS records on 2026-11-19).
- **Email:** add to `src/site.json` once the domain is bought.
- **Resend env vars** for the contact form: `RESEND_API_KEY`, `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL`.
- **Licensing-ad risk (owner aware):** Georgia, Texas, Illinois, Maryland, California and Minnesota limit plumbing ads to licensed plumbers. Pages say work is done by licensed local plumbers; each state page now names its licensing authority.
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
