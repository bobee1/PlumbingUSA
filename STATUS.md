# PipeMend — Build Status

Nationwide plumbing services site. Brand **PipeMend**, domain **pipemend.us** (no DNS records on 2026-11-19, so very likely unregistered; not yet purchased).
Plan: "Nationwide Plumber Lead-Gen Site — Master Plan" (Claude doc, https://claude.ai/artifact/TmMBuMtsxGkkjk7koFm5BK). Rules: "Local Service Site SEO Criteria & AI Prompt" and "Blog Post Criteria & SEO Writing Prompt".
Full step log: [docs/RECORD-REGISTER.md](docs/RECORD-REGISTER.md).

Last updated: 2026-11-24 (Build 7 — staged with 6c, waiting on Census data)

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
- **Semrush:** working again as of 2026-11-24.

** audit PASS 0 issues; reading grade 4.8–7.8; no duplicate paragraphs; site audit clean; no overflow or console errors at 360/768/1280.

## Also done — Guide SEO pass with Semrush (2026-11-24)
- **Semrush is working again** (21,730 API units left). Pulled fresh keyword difficulty for all 12 guide keywords and the top 10 question keywords for each topic: `research/12-guide-questions-semrush.csv` (about 5,500 units used).
- **New sections:** unclog guide now covers shower (9,900/mo, KD 20), bathtub, sink and dishwasher drains; sewer-smell guide covers toilet, bathroom sink and washer/laundry smells.
- **Headings matched to easy questions:** "Why is my water pressure low?" (KD 6), "What size tankless water heater do I need?", "What to do if pipes freeze", "How to fix a leaking water heater", "What does sewer gas smell like?".
- **9 new FAQs** (in FAQ schema): stop a running toilet now, who to call for a leaking water heater, outside shut-off valve, flushing and cost of tankless, buying a house with polybutylene and repipe cost, plumber cost to unclog a drain. Prices stay off the site, as before.
- **Descriptions** for the running-toilet and unclog guides now include "toilet that keeps running" (9,900/mo, KD 19) and the drain types.
- **Not changed:** service and city pages already use Semrush data from Nov 19–20. Note: Semrush reports 673,000/mo for "how to fix a running toilet" with a one-month spike in its trend; treat that number as unreliable.
- Checks: audit PASS 0 issues; reading grade ≤9; FAQ schema valid; no overflow.

## In progress — Build 6c: 25 more city pages (staged; waiting on Census data)
- **Cities (ranks 14–71):** Scottsdale, Chandler, Glendale (AZ), Anaheim, San Francisco, Chula Vista, Irvine, Oakland, Fremont, Santa Ana, New Orleans, St. Petersburg, Boston, Garland, Lubbock, Irving, Albuquerque, Richmond (VA), Virginia Beach, Greensboro, Detroit, St. Louis, Henderson, Tulsa, Lexington.
- **Done:** city details in `src/metros/meta.json` (batch "6c": county, ZIPs, neighborhoods, nearby cities, Semrush volume/KD) and all 25 copy files in `src/metros/content/` (water utility, problems, tips, permit office, state licensing, FAQ). Independent cities (Richmond, Virginia Beach, St. Louis) and San Francisco's city-county use the `indep` flag so wording doesn't name a county twice.
- **Build change:** `metros.live()` now needs both copy and Census data, and `metros.py` merges `research/13-city-acs-6c.json` and `research/14-city-heating-fuel-6c.json` when present. Until then these 25 pages stay hidden; the live site is unchanged (145 pages).
- **Tested with stand-in figures:** all 25 pages built (945–1,094 words), audit PASS 0 issues, reading grade ≤9, no duplicate paragraphs, no overflow; then the stand-in files were deleted.
- **Owner action:** `git pull`, then `python3 scripts/census_pull.py` (Python 3, internet, no API key). It writes the two research files above. Commit and push them (or send them), and the pages go live on the next build.
- **Data route:** the Census API, Census Reporter API and BigQuery (no Google sign-in) can't be reached from the build workspace; the owner chose to run the script.

## In progress — Build 7: last 24 cities of the top-100 list (staged; waiting on Census data)
- **Cities (ranks 72–100):** Spokane, Winston-Salem, Riverside, Stockton, Fresno, Bakersfield, Fort Wayne, El Paso, Corpus Christi, Laredo, Toledo, Jersey City, Newark, Anchorage, Chesapeake, Norfolk, Hialeah, Lincoln, Honolulu, Milwaukee, North Las Vegas, Buffalo, Oklahoma City, St. Paul. This finishes every city in research/06 (Washington, D.C. stays on its state page).
- **Done:** meta (batch "7") and 24 copy files. Local licensing covered: Lincoln and Buffalo (city licenses), New Jersey master plumber board, Alaska and Hawaii state boards. Anchorage, Honolulu, Chesapeake and Norfolk use the `indep` flag.
- **Script:** `scripts/census_pull.py` now pulls 6c and 7 in one run (or one batch: `python3 scripts/census_pull.py 7`) and writes research/15 and 16 for Build 7; `metros.py` merges them when present.
- **Tested with stand-in figures (all 49 staged pages):** 194 pages built, audit PASS 0 issues, reading grade ≤9, no duplicates, lowest city inbound links 6, no overflow or console errors. Stand-in files deleted; live site stays at 145 pages.
- **Owner action:** `git pull`, then `python3 scripts/census_pull.py`, then commit and push research/13–16. 49 city pages go live on the next build.

## Coming
| Build | Scope | Needs from owner |
| --- | --- | --- |
| 6c (finish) | Owner runs `scripts/census_pull.py`; then build, audit and publish the 25 staged cities | Census files |
| 7 (finish) | Census data in → publish 6c + 7 (49 cities, 194 pages) | Owner runs script |
| 8 (next) | Wave 3 city research with Semrush (now working): next 50–100 cities by \"plumber + city\" demand, then staged pages | — |
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
