# PipeMend — Record Register

A dated log of every step. Newest entries at the bottom. Status: Done / In progress / Planned.

| # | Date | Build | Step | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026-11-16 | Plan | Nationwide plumbing master plan written | Done | Claude doc https://claude.ai/artifact/TmMBuMtsxGkkjk7koFm5BK; Semrush: "plumber near me" 550,000/mo, "emergency plumber" 246,000/mo |
| 2 | 2026-11-19 | 1 | Read site criteria and blog criteria docs | Done | Rules applied to every page |
| 3 | 2026-11-19 | 1 | Brand names checked with DNS (Cloudflare DoH) | Done | No records: pipemend.us/.com, draincrest.us/.com, plumbora.us and others; no plumbing business found using "PipeMend" |
| 4 | 2026-11-19 | 1 | Owner chose brand PipeMend, domain pipemend.us | Done | Matches the SootMend naming family |
| 5 | 2026-11-19 | 1 | Owner decisions recorded | Done | Own-business routing like SootMend (24/7, 10+ years); owner Anjam Javed; toll-free 1-800-555-0199; all states and cities, no exception |
| 6 | 2026-11-19 | 1 | Repo named | Done | github.com/bobee1/PlumbingUSA |
| 7 | 2026-11-19 | 1 | Generator forked from SootMend Build 1 engine and rebranded | Done | `build.py`; Plumber schema type; live-only links in sidebar, footer and offer catalog |
| 8 | 2026-11-19 | 1 | Design system "Deep Water + Copper" | Done | #0f2d3d, #a84b18, #0a5c72, #1d7f78; contrast 5.7–14.4:1 |
| 9 | 2026-11-19 | 1 | Logo, app icons, favicon, social image | Done | `scripts/make_logo.py`, `scripts/make_brand_png.py` |
| 10 | 2026-11-19 | 1 | Pexels photos downloaded, cropped 3:2, converted to WebP | Done | IDs 6419128, 34295406, 39885416, 14953886 (used); 10847199, 4092030, 18274115, 9551366 (held); all < 170 KB |
| 11 | 2026-11-19 | 1 | Sources opened for safety and fact claims | Done | EPA WaterSense, EPA mold guide, American Red Cross frozen pipes, PHMSA gas leaks, Insurance Information Institute |
| 12 | 2026-11-19 | 1 | Entity links verified on Wikipedia | Done | Plumbing, Plumber, Drain-waste-vent system, Sanitary sewer, Water heating, Plumbing fixture |
| 13 | 2026-11-19 | 1 | Home page written (1,795 words, 7 FAQs, plumbing system diagram with legend) | Done | `src/pages/index.html` |
| 14 | 2026-11-19 | 1 | Trust and legal pages written | Done | About (call-flow illustration), Contact (form), Privacy, Terms, Disclaimer, Editorial policy, Accessibility, 404 |
| 15 | 2026-11-19 | 1 | Contact form endpoint | Done | `functions/api/lead.js` (Resend; needs env vars) |
| 16 | 2026-11-19 | 1 | Audit + readability + site audit | Done | 0 issues; FK 5.4–6.0 (legal exempt) |
| 17 | 2026-11-19 | 1 | Responsive check 360/768/1280 | Done | No overflow, no console errors, menu works |
| 18 | 2026-11-19 | 1 | STATUS.md + record register written; committed | Done | Branch `main` |
| 19 | 2026-11-20 | 2 | Read SootMend Build 2 layout to keep the same research files | Done | research/01–06 |
| 20 | 2026-11-20 | 2 | Semrush: 60 service keywords (volume, CPC, competition, KD, intent) | Done | `research/01-service-keywords.csv` (600 units) |
| 21 | 2026-11-20 | 2 | Semrush: "plumber + city" for the 100 largest cities | Done | `research/02-city-demand.csv` (1,000 units); all 100 have demand, 110–2,900/mo |
| 22 | 2026-11-20 | 2 | Semrush: suburbs, small cities, state terms, modifiers | Done | `research/03-state-and-town-terms.csv` (500 units); state terms only 70–210/mo |
| 23 | 2026-11-20 | 2 | Semrush: questions (water heater, drain, plumber, pipes) + 40 guide topics | Done | `research/04-guide-keywords.csv` (2,800 units) |
| 24 | 2026-11-20 | 2 | Semrush top-10 SERPs: emergency plumber, water heater repair, sewer line repair, plumber denver | Done | `research/05-competitors.csv` (400 units) |
| 25 | 2026-11-20 | 2 | Competitor pages read: Roto-Rooter Seattle emergency (~3,000), Roto-Rooter water heater (~1,050), HomeGuide sewer cost (~1,700) | Done | Term list in plan |
| 26 | 2026-11-20 | 2 | Cities scored (volume × (1 − KD/100)) and split into Wave 1 / Wave 2 | Done | `research/06-city-waves.csv`; Wave 1 = 74% of measured city demand |
| 27 | 2026-11-20 | 2 | Site plan doc written for owner approval | Done | https://claude.ai/artifact/Lnvtnd4rBMx8H6m4StHfiB |
| 28 | 2026-11-20 | 2 | STATUS.md and register updated; committed and pushed | Done | Branch `main` |
| 29 | 2026-11-20 | 3 | Owner approved the Build 2 plan ("Build 3") | Done | Plan doc unchanged |
| 30 | 2026-11-20 | 3 | services.json expanded to 19 services in plan order | Done | 6 new: tankless, slab leak, faucet, water softener, backflow, commercial |
| 31 | 2026-11-20 | 3 | 13 Pexels photos chosen; 10 converted to WebP for Build 3, 3 held for 3b | Done | `src/photos.json`; sewer trench re-encoded under 200 KB |
| 32 | 2026-11-20 | 3 | Engine: scrollable tables; near-you and helpful-guides placeholders render empty until their pages exist | Done | `build.py` |
| 33 | 2026-11-20 | 3 | Sources opened: EPA WaterSense, EPA SSO FAQ, EPA FOG, EPA lead, DOE Energy Saver guide, DOE Building America tankless pages, CPSC scalds, ENERGY STAR HPWH, Red Cross, PHMSA, III, EPA mold | Done | Cited per page |
| 34 | 2026-11-20 | 3 | Services hub written | Done | 735 words; scenario table, hiring checklist |
| 35 | 2026-11-20 | 3 | Service pages: emergency, drain cleaning, hydro jetting | Done | 1,278 / 1,239 / 1,095 words |
| 36 | 2026-11-20 | 3 | Service pages: water heater repair, water heater installation, tankless (SVG diagram) | Done | 1,303 / 1,209 / 1,377 words |
| 37 | 2026-11-20 | 3 | Service pages: sewer line, leak detection, slab leak (SVG diagram), repiping | Done | 1,206 / 1,156 / 1,157 / 1,115 words |
| 38 | 2026-11-20 | 3 | Home trimmed to 1,771 words; system legend links to 7 service pages | Done | Cap 1,800 |
| 39 | 2026-11-20 | 3 | Audit, readability, site audit, responsive check 360/768/1280 | Done | PASS 0 issues; FK 5.0–7.4; no overflow; diagram labels fixed |
| 40 | 2026-11-20 | 3 | STATUS.md and register updated; committed and pushed | Done | Branch `main` |
| 41 | 2026-11-20 | 3b | Owner asked for Build 3b | Done | — |
| 42 | 2026-11-20 | 3b | 4 new Pexels photos (faucet, gas meter, toilet tank, commercial kitchen) converted to WebP; 3 held photos assigned | Done | `src/photos.json`; sump pump and backflow get SVG diagrams |
| 43 | 2026-11-20 | 3b | Sources opened: EPA WaterSense toilets + faucets, EPA cross-connection manual + fact sheet, USGS hardness, FEMA basement flooding, CPSC CO | Done | Cited per page |
| 44 | 2026-11-20 | 3b | Service pages: water line, toilet, faucet | Done | 1,243 / 1,079 / 1,069 words |
| 45 | 2026-11-20 | 3b | Service pages: garbage disposal, sump pump (SVG), gas line (safety callout) | Done | 1,022 / 1,174 / 1,099 words |
| 46 | 2026-11-20 | 3b | Service pages: water softener, backflow testing (SVG), commercial | Done | 1,013 / ~1,060 / 1,050 words |
| 47 | 2026-11-20 | 3b | Hub table +9 rows; home legend links to water line, toilet, faucet; all 19 cards linked | Done | Hub 843 words, home 1,774 |
| 48 | 2026-11-20 | 3b | Audit, readability, site audit, responsive check 360/768/1280 | Done | PASS 0 issues; FK 5.5–8.7; no overflow; sump label overlap fixed |
| 49 | 2026-11-20 | 3b | STATUS.md and register updated; committed and pushed | Done | Branch `main` |
| 50 | 2026-11-20 | 4 | Owner asked for Build 4 | Done | — |
| 51 | 2026-11-20 | 4 | Reused SootMend's state data (ACS housing, places, FEMA water declarations, heating fuel) and meta (names, slugs, neighbors) | Done | `research/07-state-data.json`, `research/08-heating-fuel.json`, `src/states/meta.json` |
| 52 | 2026-11-20 | 4 | Plumbing licensing authority researched for all 51 | Done | Two state-by-state guides cross-checked; TX, AR, DC verified separately; 6 local-only states |
| 53 | 2026-11-20 | 4 | `states.py` template (facts table, housing-age chart, heater and flood text, licensing, FAQ, schema) and `{{state_patterns}}` component | Done | Service cards swapped for compact links to keep pages under 1,400 words |
| 54 | 2026-11-20 | 4 | Locations hub written | Done | 917 words |
| 55 | 2026-11-20 | 4 | 51 hand-written state content files (South, West, Northeast + Midwest batches) | Done | `src/states/content/` |
| 56 | 2026-11-20 | 4 | Fixes: banned word on WA, repeated paragraphs made state-specific, CT/TN/VA simplified, named storms keep capitals | Done | — |
| 57 | 2026-11-20 | 4 | Home links to locations hub; service pages show "near you" state links | Done | Home 1,781 words |
| 58 | 2026-11-20 | 4 | Audit, readability, site audit, responsive check on 52 location pages | Done | PASS 0 issues; FK 6.7–9.0; 948–1,140 words |
| 59 | 2026-11-20 | 4 | STATUS.md and register updated; committed and pushed | Done | Branch `main` |
| 60 | 2026-11-20 | 5 | Owner asked for Build 5; re-read blog rules doc and the approved 12-guide list | Done | — |
| 61 | 2026-11-20 | 5 | Semrush phrase_organic / phrase_questions attempted | Failed | ERROR 122 (wrong format or empty key) on every call; no units spent |
| 62 | 2026-11-20 | 5 | SERPs checked by web search; 1 competitor content page read per guide (word count + headings) | Done | `research/09-guide-briefs.csv` |
| 63 | 2026-11-20 | 5 | New sources opened: ATSDR hydrogen sulfide, BLS plumbers, III "Am I covered?", City of Bloomington water pressure, Red Cross (re-checked) | Done | — |
| 64 | 2026-11-20 | 5 | Blog engine, image script, CSS ported from SootMend and rebranded | Done | `blog.py`, `scripts/make_post_images.py` |
| 65 | 2026-11-20 | 5 | 12 guides written; 5 extended to meet benchmarks | Done | 1,389–1,996 words |
| 66 | 2026-11-20 | 5 | 12 branded featured images rendered | Done | `src/static/img/blog/` |
| 67 | 2026-11-20 | 5 | Guides hub and glossary (58 terms) | Done | `/blog/`, `/glossary/` |
| 68 | 2026-11-20 | 5 | Helpful guides on 19 service and 51 state pages; in-text guide links on 5 service pages; sidebar popular guides | Done | — |
| 69 | 2026-11-20 | 5 | Audit, readability, site audit, responsive check | Done | PASS 0 issues; FK 4.8–7.8 |
| 70 | 2026-11-20 | 5 | STATUS.md and register updated; committed and pushed | Done | Branch `main` |
| 71 | 2026-11-20 | 6 | Semrush retested: ERROR 122 again; used Nov 19–20 city data | Blocked | research/06 |
| 72 | 2026-11-20 | 6 | City Census data and 25-city meta (ACS housing, heating fuel, ZIPs, neighborhoods, Semrush volume/KD) | Done | `research/10`, `research/11`, `src/metros/meta.json` |
| 73 | 2026-11-20 | 6 | City page engine `metros.py`; city links on state pages, locations hub and home | Done | — |
| 74 | 2026-11-20 | 6 | 25 city pages written (water utility, problems, tips, permits, FAQ) | Done | 955–1,079 words |
| 75 | 2026-11-20 | 6 | DC kept on state page; Scottsdale, Chandler, Anaheim, San Francisco, New Orleans moved to 6b (no city Census data) | Decided | — |
| 76 | 2026-11-20 | 6 | Audit, readability, site audit, responsive check | Done | PASS 0 issues; FK ≤9 |
| 77 | 2026-11-20 | 6 | STATUS.md and register updated; committed and pushed | Done | Branch `main` |
| 78 | 2026-11-20 | 6b | Census data for held-back cities: Census and Census Reporter APIs unreachable; 5 cities stay deferred | Blocked | — |
| 79 | 2026-11-20 | 6b | 25 cities added to `src/metros/meta.json` (Semrush volume/KD, rank, wave) | Done | Ranks 32–99 |
| 80 | 2026-11-20 | 6b | 25 city pages written, including local licensing for NYC, KC, Omaha, Wichita, Pittsburgh, Nashville, Memphis, Louisville | Done | 942–1,089 words |
| 81 | 2026-11-20 | 6b | Home page switched to top-20 city pills + "All city pages" link; hub anchor `#city-pages` | Done | Home 1,8xx → under 1,800 |
| 82 | 2026-11-20 | 6b | Audit, readability, site audit, responsive check | Done | PASS 0 issues; FK ≤9 |
| 83 | 2026-11-20 | 6b | STATUS.md and register updated; committed and pushed | Done | Branch `main` |
| 84 | 2026-11-24 | SEO | Semrush retested: working (ERROR 122 cleared) | Done | 27,250 units at start |
| 85 | 2026-11-24 | SEO | Guide keyword difficulty refresh + question keywords for 12 guides | Done | `research/12-guide-questions-semrush.csv`; ~5,500 units |
| 86 | 2026-11-24 | SEO | 7 new guide sections, 6 heading rewrites, 9 new FAQs, 2 meta descriptions | Done | Audit PASS; FK ≤9 |
| 87 | 2026-11-24 | 6c | Census routes tested: Census API, Census Reporter API and BigQuery unreachable; secondary sites inconsistent | Blocked | — |
| 88 | 2026-11-24 | 6c | Owner decision: run `scripts/census_pull.py` locally | Decided | Script pushed |
| 89 | 2026-11-24 | 6c | 25 cities added to meta (ranks 14–71) + 25 copy files written | Done | Staged, hidden until data |
| 90 | 2026-11-24 | 6c | `metros.live()` waits for Census data; auto-merge of research/13 and 14; `indep` flag for independent cities | Done | — |
| 91 | 2026-11-24 | 6c | Stand-in data test: audit, readability, duplicates, site audit, responsive | Done | PASS; stand-in files deleted |
| 92 | — | 6c | Owner runs Census script; build and publish 25 pages | Waiting | Owner action |
| 93 | 2026-11-24 | 7 | 6c Census data not yet pushed; Build 7 staged alongside | Noted | — |
| 94 | 2026-11-24 | 7 | `census_pull.py` extended to batches 6c + 7 (research/15, 16) | Done | Dry-run tested |
| 95 | 2026-11-24 | 7 | 24 cities added to meta (ranks 72–100) + 24 copy files | Done | Top-100 list finished |
| 96 | 2026-11-24 | 7 | Stand-in test of 49 staged pages: audit, readability, duplicates, links, responsive | Done | PASS; stand-ins deleted |
| 97 | — | 7 | Owner runs Census script; publish 49 pages | Waiting | Owner action |
| 98 | 2026-11-24 | 8 | Semrush: volume for 102 candidate cities, KD for top 48 → research/17-city-wave3.csv | Done | ~3,430 units; 18,300 left |
| 99 | 2026-11-24 | 8 | San Jose found missing from all earlier lists; added to Build 8 | Done | 1,300/mo, KD 30 |
| 100 | 2026-11-24 | 8 | 26 cities added to meta (wave 3) + 26 copy files; Census script batch 8 | Done | Staged |
| 101 | 2026-11-24 | 8 | State pages: city links as pills; hub: top 40 cities + note | Done | Live now |
| 102 | 2026-11-24 | 8 | Stand-in test of 75 staged pages: all checks | Done | PASS; stand-ins deleted |
| 103 | — | 8 | Owner runs Census script; publish 75 pages | Waiting | Owner action |
| 104 | 2026-11-24 | 9 | Semrush KD for 13 state-coverage cities | Done | 650 units; 17,650 left |
| 105 | 2026-11-24 | 9 | Verified Birmingham utility rename (Central Alabama Water) | Done | Web search |
| 106 | 2026-11-24 | 9 | 25 cities to meta + copy; Census script batch 9 (research/20, 21) | Done | Every state now has a city page |
| 107 | 2026-11-24 | 9 | City template: shared-name cities, nearby pills (max 8), permit text de-duplication, local-licensing wording | Done | Live now |
| 108 | 2026-11-24 | 9 | Stand-in test of 100 staged pages: all checks | Done | PASS; stand-ins deleted |
| 109 | — | 9 | Owner runs Census script; publish 100 pages | Waiting | Owner action |
| 110 | 2026-11-24 | 10 | Semrush KD for 23 Wave 3 cities; research/17 re-scored | Done | 1,150 units; 16,500 left |
| 111 | 2026-11-24 | 10 | 25 cities to meta + copy; Census script batch 10 (research/22, 23) | Done | Staged |
| 112 | 2026-11-24 | 10 | Stand-in test of 125 staged pages: all checks | Done | PASS; stand-ins deleted |
| 113 | — | 10 | Owner runs Census script; publish 125 pages | Waiting | Owner action |
| 114 | — | 11 | Fact-check pass on staged city copy, or Wave 3 remainder | Planned | Owner's choice |
