"""City pages for PipeMend: /locations/<state>/<city>/ (Wave 1 = top cities by "plumber + city" search demand).

Inputs:
  research/10-city-acs.json            Census ACS 2020-2024 housing data for each city
  research/11-city-heating-fuel.json   Census ACS B25040 heating fuel for each city
  src/metros/meta.json                 city, state, county, ZIP codes, neighborhoods, nearby cities, Semrush figures
  src/metros/content/<slug>.json       hand-written copy: lead, risk, why, water, problems, tips, areas, permits, FAQ
A page is built only when its content file and Census data both exist, so cities go live batch by batch.
"""
import json
from pathlib import Path

import states as S

ROOT = Path(__file__).parent
ACS = json.loads((ROOT / "research" / "10-city-acs.json").read_text())["places"]
FUEL = json.loads((ROOT / "research" / "11-city-heating-fuel.json").read_text())["places"]
# Later city batches: extra Census files from scripts/census_pull.py, merged when present
for _a, _f in [("13-city-acs-6c.json", "14-city-heating-fuel-6c.json"),
               ("15-city-acs-7.json", "16-city-heating-fuel-7.json")]:
    if (ROOT / "research" / _a).exists() and (ROOT / "research" / _f).exists():
        ACS.update(json.loads((ROOT / "research" / _a).read_text())["places"])
        FUEL.update(json.loads((ROOT / "research" / _f).read_text())["places"])
MMETA = json.loads((ROOT / "src" / "metros" / "meta.json").read_text())
CDIR = ROOT / "src" / "metros" / "content"


def live(slug):
    # needs copy and Census data; a city waiting on its Census pull stays hidden
    return (slug in MMETA and (CDIR / f"{slug}.json").exists()
            and MMETA[slug]["acs"] in ACS and MMETA[slug]["fuel"] in FUEL)


def area_of(m):
    """' and <County>' for normal cities; nothing for independent cities and consolidated city-counties."""
    return "" if m.get("indep") else f" and {m['county']}"


def mpath(slug):
    m = MMETA[slug]
    return f"/locations/{S.META[m['st']]['slug']}/{m['url']}/"


def mlink(slug, text=None):
    return f'<a href="{mpath(slug)}">{text or MMETA[slug]["city"]}</a>'


def metros_in_state(ab):
    return sorted([k for k, v in MMETA.items() if v["st"] == ab and live(k)], key=lambda k: MMETA[k]["city"])


def acs(slug):
    pop, units, med, pre80, pre40, own, mobile = ACS[MMETA[slug]["acs"]]
    return dict(pop=pop, units=units, med=med, pre80=pre80, pre40=pre40, own=own, mobile=mobile)


def fuel(slug):
    return dict(zip(S.FUEL_LABELS, FUEL[MMETA[slug]["fuel"]][:7]))


def glance(slug, c):
    m, a, f = MMETA[slug], acs(slug), fuel(slug)
    rows = [("Population", S.fmt(a["pop"])), ("Housing units", S.fmt(a["units"])),
            ("Median year homes were built", str(a["med"])),
            ("Homes built before 1980", f"{a['pre80']:g}%"), ("Homes built before 1940", f"{a['pre40']:g}%"),
            ("Owner-occupied homes", f"{a['own']:g}%"),
            ("Homes heated with natural gas", f"{f['Utility gas']:g}%"),
            ("Homes heated with electricity", f"{f['Electricity']:g}%"),
            ("Water utility", c["utility"]), ("County", m["county"]),
            ("Sample ZIP codes", ", ".join(m["zips"]))]
    trs = "".join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in rows)
    return f'<div class="table-scroll"><table class="facts"><tbody>{trs}</tbody></table></div>'


def age_chart(slug):
    a = acs(slug)
    c = MMETA[slug]["city"]
    rows = [("Before 1940", a["pre40"]), ("1940 to 1979", round(a["pre80"] - a["pre40"], 1)), ("1980 or later", round(100 - a["pre80"], 1))]
    bars = "".join(f'<li><span class="bar-label">{k}</span><span class="bar-track"><span class="bar-fill" style="width:{max(v, 1):g}%"></span></span>'
                   f'<span class="bar-val">{v:g}%</span></li>' for k, v in rows)
    return (f'<figure class="bars" aria-label="When homes in {c} were built"><figcaption><strong>When homes in {c} were built</strong> '
            f'(share of housing units, Census ACS 2020–2024)</figcaption><ul>{bars}</ul></figure>')


def housing_line(slug):
    a, c = acs(slug), MMETA[slug]["city"]
    if a["pre40"] >= 20:
        s = S.pick(slug, [f"{a['pre40']:g}% of homes in {c} were built before 1940, so galvanized supply pipe, cast-iron stacks and clay sewer laterals are still common.",
                          f"{c} has a lot of old housing: {a['pre40']:g}% predates 1940. Original galvanized water lines and cast-iron or clay drains are often near the end of their life."], "hl")
    elif a["pre80"] >= 50:
        s = S.pick(slug, [f"About {a['pre80']:g}% of {c} homes were built before 1980, so cast-iron drains, older copper with lead solder and some galvanized lines come up often.",
                          f"More than half of {c}'s homes ({a['pre80']:g}%) went up before 1980. Cast-iron drains and aging supply lines are a big share of repair calls."], "hl")
    else:
        s = S.pick(slug, [f"Housing in {c} is newer, with a median build year of {a['med']}. Most calls are fixtures, water heaters, drain clogs and slab or fitting leaks rather than failing pipe.",
                          f"With a median build year of {a['med']}, most {c} homes have copper, CPVC or PEX lines. Water heaters, fixtures and fittings wear out first."], "hl")
    if 1974 <= a["med"] <= 1996:
        s += " Homes from the late 1970s to the mid-1990s may also have gray polybutylene pipe, which has a history of failures."
    if a["own"] < 45:
        s += f" Only {a['own']:g}% of homes are owner-occupied, so many calls come from renters, landlords and property managers."
    s += (' See <a href="/services/repiping/">pipe repair and repiping</a> and '
          '<a href="/blog/polybutylene-pipes/">our guide to pipe types</a>.')
    return f"<p>{s}</p>"


def heater_line(slug):
    f, c = fuel(slug), MMETA[slug]["city"]
    if f["Utility gas"] >= 50:
        s = S.pick(slug, [f"Natural gas heats {f['Utility gas']:g}% of {c} homes, and most of those have gas water heaters, so burners, venting and <a href=\"/services/gas-line-repair/\">gas lines</a> are routine work.",
                          f"{f['Utility gas']:g}% of homes in {c} heat with natural gas. Gas water heaters and <a href=\"/services/gas-line-repair/\">gas line repairs</a> are a large share of plumbing calls."], "h")
    elif f["Electricity"] >= 50:
        s = S.pick(slug, [f"Electricity heats {f['Electricity']:g}% of {c} homes, so electric tank water heaters are common, and a <a href=\"/services/water-heater-installation/\">heat pump model</a> can cut running costs when the old tank fails.",
                          f"Most {c} homes ({f['Electricity']:g}%) heat with electricity. Burned-out elements and thermostats are frequent water heater repairs, and heat pump tanks are a popular upgrade."], "h")
    else:
        s = f"{c} homes split between gas ({f['Utility gas']:g}%) and electric heat ({f['Electricity']:g}%), so plumbers here service both gas and electric water heaters."
    if f["No heating fuel"] >= 4:
        s += f" In the mild climate, {f['No heating fuel']:g}% of homes use no heating fuel at all."
    s += ' See <a href="/services/water-heater-repair/">water heater repair</a> and <a href="/blog/tankless-vs-tank-water-heater/">tankless vs. tank</a>.'
    return f"<p>{s}</p>"


def page(slug):
    if not live(slug):
        return None
    c = json.loads((CDIR / f"{slug}.json").read_text())
    m = MMETA[slug]
    city, ab = m["city"], m["st"]
    disp = f"{city}, {ab}"
    sp = S.state_path(ab)
    L = S.lic(ab)
    title = f"Plumber in {city}, {ab}: 24/7 Plumbing Services | PipeMend"
    if len(title) > 60:
        title = f"Plumber in {city}, {ab}: 24/7 Plumbing | PipeMend"
    if len(title) > 60:
        title = f"Plumber in {city}, {ab} | PipeMend"
    desc = f"Plumber in {disp} for {c['risk_short']}. Leaks, drains, water heaters and sewer lines. Call PipeMend 24/7 at 1-800-555-0199."
    if len(desc) > 155:
        desc = f"Plumber in {disp} for {c['risk_short']}. Call PipeMend 24/7 at 1-800-555-0199."
    if len(desc) > 155:
        desc = f"Plumber in {disp} for {c['risk_short']}. Call 1-800-555-0199."
    near = [n for n in m["nearby"] if live(n)]
    back = sorted(k for k, v in MMETA.items() if slug in v["nearby"] and k not in near and live(k))
    same = [k for k in metros_in_state(ab) if k != slug and k not in near and k not in back]
    near = (near + back + same)[:5]
    nb = S.pick(slug, [f"PipeMend also covers nearby {S.join_list([mlink(n) for n in near])}.",
                       f"Plumbers also work in {S.join_list([mlink(n) for n in near])}.",
                       f"Plumbing help is also available in {S.join_list([mlink(n) for n in near])}."], "nb") if near else ""
    quick = S.pick(slug, [f"PipeMend plumbers in {disp} handle leaks, clogged drains, water heaters, sewer lines and gas lines, day and night.",
                          f"Plumbing services in {city} cover emergency leaks, drain and sewer clogs, water heater repair and replacement, and gas lines.",
                          f"In {city}, PipeMend sends licensed local plumbers for burst pipes, drain clogs, water heaters, sewer problems and gas lines."], "q")
    quick += f" The main local issues are {c['risk']}. PipeMend covers all of {city}{area_of(m)}, including ZIP codes {', '.join(m['zips'][:3])}."
    if L["kind"] == "local":
        lic_p = f"{S.META[ab]['name']} has no statewide plumber license, so {city}{area_of(m)} set{'s' if m.get('indep') else ''} the licensing rules."
    elif L["kind"] == "contractor":
        lic_p = f'Plumbing contractors in {city} are licensed through the <a href="{L["url"]}">{L["name"]}</a>.'
    else:
        lic_p = f'Plumbers in {city} are licensed by the <a href="{L["url"]}">{L["name"]}</a>; you can look up a license number there.'
    permits = f"{lic_p} {c['permits']} More on state rules: <a href=\"{sp}\">plumbers in {S.short(ab)}</a>."
    cta1 = S.pick(slug, [f"Plumbing problem in {city}? Call PipeMend {{{{availability}}}}.",
                         f"Need a plumber in {city}? Call PipeMend at {{{{phone}}}}."], "c1")
    tips_h = S.pick(slug, [f"Plumbing tips for {city} homes", f"How {city} homeowners can prevent plumbing problems", f"Practical plumbing tips for {city}"], "t")
    faq = [
        {"q": f"Do you have plumbers in all of {city}?",
         "a": f"Yes. PipeMend takes plumbing calls from across {city}{area_of(m)}, including {S.join_list(m['hoods'][:5])}, and ZIP codes such as {', '.join(m['zips'][:4])}."},
        {"q": f"Do I need a permit for plumbing work in {city}?",
         "a": S.pick(slug, [f"For bigger jobs, usually yes. Water heater replacement, gas lines, sewer or water line work and repiping generally need a {city} permit and inspection. Simple repairs such as a faucet or toilet usually don't.",
                            f"Often. {city} typically requires permits for water heaters, gas piping, sewer and water service lines and repipes. Your plumber can pull the permit and schedule the inspection."], "pq")},
        {"q": f"How fast can a plumber get to me in {city}?",
         "a": S.pick(slug, [f"In {city}, it depends on traffic, the time of day and how many calls are open. You get an honest time window when you call. If water is spreading, shut off the main valve first.",
                            f"Arrival depends on where you are in {city}, the hour and current demand. Ask for a time window when you call, and close the main water valve if a pipe is leaking."], "aq")},
        c["faq"],
    ]
    body = f"""<p class="quick"><strong>Quick answer:</strong> {quick}</p>

<h2>{city} plumbing at a glance</h2>
{glance(slug, c)}
<p class="small-note">{city} housing and heating figures: Census ACS 2020–2024 5-year estimates.</p>

<h2>Why plumbing in {city} is different</h2>
{''.join(f'<p>{p}</p>' for p in c['why'])}

<h2>Pipes and housing age in {city}</h2>
{age_chart(slug)}
{housing_line(slug)}

<h2>Water quality and supply in {city}</h2>
<p>{c['water']}</p>

<h2>Common plumbing problems in {city}</h2>
{S.problems_table(c)}
{{{{cta:{cta1}}}}}

<h2>Water heaters and gas lines in {city}</h2>
{heater_line(slug)}

<h2>{tips_h}</h2>
<ul>{''.join(f'<li>{t}</li>' for t in c['tips'])}</ul>

<h2>Neighborhoods and areas served in {city}</h2>
<p>{c['areas']} {nb}</p>

<h2>Plumbing permits and licenses in {city}</h2>
<p>{permits}</p>
{{{{cta:Leak, clog or no hot water in {city}? Call {{{{phone}}}}.}}}}

{{{{faq}}}}

<h2>Plumbing services in {city}</h2>
{S.service_pills(city)}

<h2>More plumbers near {city}</h2>
<ul class="pills">{''.join(f'<li><a href="{mpath(n)}">Plumber in {MMETA[n]["city"]}</a></li>' for n in near)}<li><a href="{sp}">All of {S.short(ab)}</a></li><li><a href="/locations/">All locations</a></li></ul>

{{{{helpful_guides:{','.join(S.guide_slugs(c))}}}}}

{{{{sources}}}}
"""
    wiki = "https://en.wikipedia.org/wiki/" + m["wiki"]
    sources = [["U.S. Census Bureau: American Community Survey", "https://www.census.gov/programs-surveys/acs"],
               ["EPA: How can lead get into my drinking water?", "https://www.epa.gov/lead/how-can-lead-get-my-drinking-water"],
               ["U.S. Department of Energy: Energy Saver guide (water heating)", "https://www.energy.gov/sites/default/files/2022-08/energy-saver-guide-2022.pdf"]]
    if L["url"]:
        sources.append([L["name"], L["url"]])
    sources += c.get("sources", [])
    return {
        "path": mpath(slug), "type": "city", "parents": [["Locations", "/locations/"], [S.short(ab), sp]],
        "title": title, "description": desc, "h1": f"Plumber in {disp}", "crumb": city, "priority": "0.8",
        "lead": c["lead"], "chips": [m["county"], "Homes, rentals and businesses", "24/7 plumbing calls"],
        "service": {"name": f"Plumbing services in {disp}", "serviceType": "Plumbing",
                    "areaServed": {"@type": "City", "name": disp, "sameAs": wiki,
                                   "containedInPlace": {"@type": "AdministrativeArea", "name": m["county"]}}},
        "about": [[disp, wiki]],
        "mentions": [["Plumbing", "https://en.wikipedia.org/wiki/Plumbing"]] + c.get("mentions", []),
        "faq_title": f"Plumbing questions in {city}", "faq": faq, "sources": sources,
        "body": body, "source": f"src/metros/content/{slug}.json",
    }


def all_pages():
    return [p for p in (page(s) for s in sorted(MMETA)) if p]
