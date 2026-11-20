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
| 29 | — | 3 | Home refined, services hub, first 10 service pages | Planned | After plan approval |
