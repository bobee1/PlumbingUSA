# PipeMend — Build Status

Nationwide plumbing services site. Brand **PipeMend**, domain **pipemend.us** (no DNS records on 2026-11-19, so very likely unregistered; not yet purchased).
Plan: "Nationwide Plumber Lead-Gen Site — Master Plan" (Claude doc, https://claude.ai/artifact/TmMBuMtsxGkkjk7koFm5BK). Rules: "Local Service Site SEO Criteria & AI Prompt" and "Blog Post Criteria & SEO Writing Prompt".
Full step log: [docs/RECORD-REGISTER.md](docs/RECORD-REGISTER.md).

Last updated: 2026-11-20 (Build 5)

## Previous
- Master plan written (2026-11-16): one national brand, metro hubs and city pages, Semrush keyword table for 20 plumbing services, state licensing-advertising risks, Cloudflare hosting.
- Build 1 (2026-11-19): engine, Deep Water + Copper design, logo set, 8 Pexels photos as WebP, 9 pages (home with system diagram, About, Contact form, Privacy, Terms, Disclaimer, Editorial, Accessibility, 404); audit 0 issues.
- Build 2 (2026-11-20): Semrush research (~4,700 units), competitor reads, site plan doc https://claude.ai/artifact/Lnvtnd4rBMx8H6m4StHfiB, approved by the owner on 2026-11-20 ("Build 3").
- Build 3 (2026-11-20): services hub and first 10 service pages (emergency, drain cleaning, hydro jetting, water heater repair and installation, tankless, sewer line, leak detection, slab leak, repiping); home trimmed to 1,771 words; audit 0 issues.
- Build 3b (2026-11-20): remaining 9 service pages (water line, toilet, faucet, garbage disposal, sump pump, gas line, water softener, backflow, commercial); all 19 services live; audit 0 issues.
- Build 4 (2026-11-20): locations hub and 51 state pages (housing age, heating fuel, FEMA water disasters, plumbing licensing authority per state, hand-written local copy); audit 0 issues.
- Owner decisions (2026-11-19): target plumbing and every sub-service in all states and cities; brand PipeMend; domain pipemend.us; own-business call routing like SootMend (24/7, 10+ years); legal owner Anjam Javed; toll-free 1-800-555-0199 until after deployment; repo github.com/bobee1/PlumbingUSA; Pexels photos as WebP or illustrations.

## Current — Build 5: Guides hub, 12 guides and glossary (done)
- **12 guides** (`/blog/<slug>/`), the approved list from the Build 2 plan, 1,389–1,996 words each, every one at or above its competitor benchmark (`research/09-guide-briefs.csv`): running toilet, water heater leaking, water heater lifespan, unclog a drain, frozen pipes, turning off the water, tankless vs. tank, low water pressure, polybutylene/galvanized/PEX/copper pipes, sewer smell, homeowners insurance and plumbing, plumber cost (factors only, no invented prices).
- **Built to the blog rules doc:** short-answer box, money-page link in the first 150 words, comparison tables, numbered steps, prevention, "Local note" (2–5 state links), "Related reading", "When should you call a plumber?", 4–5 FAQs, 3–5 opened primary sources (EPA, DOE, CDC/ATSDR, BLS, Red Cross, FEMA, III, USGS, City of Bloomington), author box, 2 related cards, BlogPosting + FAQPage schema with citations.
- **Featured images:** branded 1200×630 graphics (WebP ~24 KB + JPG ~47 KB) from `scripts/make_post_images.py`.
- **Guides hub** `/blog/` grouped into 5 categories; **glossary** `/glossary/` with 58 terms, auto-linking up to 4 terms per service, state and guide page.
- **Internal links:** every service page and state page now shows 3 "Helpful guides"; service pages link guides in-text; sidebar shows 4 popular guides; every guide has 3+ in-text inbound links with varied anchors.
- **Research note:** Semrush returned "ERROR 122 wrong format or empty key" for every report on 2026-11-20, so keyword volumes come from the Nov 19–20 Semrush pull (research/04) and SERPs were checked by web search with one competitor page read per guide.
- **Checks:** audit PASS 0 issues; reading grade 4.8–7.8; no duplicate paragraphs; site audit clean; no overflow or console errors at 360/768/1280.

## Coming
| Build | Scope | Needs from owner |
| --- | --- | --- |
| 6, 6b (next) | Wave 1 cities, 25 per build | — |
| 7, 7b | Wave 2 cities, 25 per build | — |
| 8+ | Wave 3 towns (50+ searches/mo) 25 per build; next guides; Search Console refreshes | Search Console access once live |
| Launch | Buy pipemend.us, Cloudflare Pages project, real toll-free number, email, Resend keys | Domain, number, email, Resend key |

## Open items
- **Phone number:** 1-800-555-0199 is in the 555-01xx range reserved for fiction and cannot receive calls. Swap after deployment: change `phone_display` / `phone_e164` in `src/site.json`, rebuild and push.
- **Domain:** buy pipemend.us soon (pipemend.com also had no DNS records on 2026-11-19).
- **Email:** add to `src/site.json` once the domain is bought.
- **Resend env vars** for the contact form: `RESEND_API_KEY`, `LEAD_TO_EMAIL`, `LEAD_FROM_EMAIL`.
- **Licensing-ad risk (owner aware):** Georgia, Texas, Illinois, Maryland, California and Minnesota limit plumbing ads to licensed plumbers. Pages say work is done by licensed local plumbers; each state page now names its licensing authority.
- **Deferred:** city links on state pages arrive with the city waves (Builds 6–7).
- **Semrush key:** the Semrush connector returned "wrong format or empty key" on 2026-11-20. Reconnect or check the API key before the city builds, which need fresh city SERP data.
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
