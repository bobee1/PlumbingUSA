"""State pages for PipeMend: one page per state and DC at /locations/<slug>/.

Inputs:
  research/07-state-data.json    Census ACS housing (2020-2024), largest places, OpenFEMA water-related declarations
  research/08-heating-fuel.json  Census ACS house heating fuel (2024)
  src/states/meta.json           names, slugs, neighbors, plumbing licensing authority [name, url, kind]
  src/states/content/<AB>.json   hand-written copy: lead, risk, why, problems, tips, areas, FAQ, optional notes
The functions below stitch verified facts together; each page's narrative comes from its own content file.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parent
R = ROOT / "research"
DATA = json.loads((R / "07-state-data.json").read_text())
FUEL = json.loads((R / "08-heating-fuel.json").read_text())["rows"]
META = json.loads((ROOT / "src" / "states" / "meta.json").read_text())
CONTENT_DIR = ROOT / "src" / "states" / "content"

WIKI = {"GA": "Georgia_(U.S._state)", "WA": "Washington_(state)", "NY": "New_York_(state)", "DC": "Washington,_D.C."}
FUEL_LABELS = ["Utility gas", "Propane or bottled gas", "Electricity", "Fuel oil or kerosene", "Coal", "Wood", "No heating fuel"]


def pick(ab, options, salt=""):
    """Deterministic choice so each state keeps the same wording between builds."""
    h = int(hashlib.md5((ab + salt).encode()).hexdigest(), 16)
    return options[h % len(options)]


def join_list(items):
    items = list(items)
    if not items:
        return ""
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def fmt(n):
    return f"{n:,}"


def state_path(ab):
    return f"/locations/{META[ab]['slug']}/"


def the(ab):
    return "the District of Columbia" if ab == "DC" else META[ab]["name"]


def short(ab):
    return "Washington, DC" if ab == "DC" else META[ab]["name"]


def load_content(ab):
    f = CONTENT_DIR / f"{ab}.json"
    return json.loads(f.read_text()) if f.exists() else None


def acs(ab):
    pop, med, own, pre80, pre40, mobile, units = DATA["acs"][ab]
    return dict(pop=pop, med=med, own=own, pre80=pre80, pre40=pre40, mobile=mobile, units=units)


def fuel(ab):
    return dict(zip(FUEL_LABELS, FUEL[META[ab]["name"]]))


def fema(ab):
    major, water, types, recent = DATA["fema"][ab]
    return dict(major=major, water=water, types=types, recent=recent)


def lic(ab):
    n, u, kind = META[ab]["lic"]
    return dict(name=n, url=u, kind=kind)


def lic_link(ab):
    L = lic(ab)
    return f'<a href="{L["url"]}">{L["name"]}</a>' if L["url"] else ""


# ---------------------------------------------------------------- page pieces

def quick_answer(ab, c):
    name = the(ab)
    a = acs(ab)
    lead = pick(ab, [
        f"PipeMend plumbers in {name} handle leaks, clogged drains, water heaters, sewer lines and gas lines, around the clock.",
        f"Plumbing services in {name} cover emergency leaks, drain and sewer clogs, water heater repair and replacement, and gas lines.",
        f"In {name}, PipeMend sends licensed local plumbers for burst pipes, drain clogs, water heaters, sewer problems and gas lines.",
    ], "q")
    if a["pre80"] >= 45:
        fact = f"{a['pre80']:g}% of homes here were built before 1980, so aging pipes and drains are a big part of the work."
    else:
        fact = f"The typical home here was built in {a['med']}, so water heaters, fixtures and fittings wear out before the pipes do."
    return f"{lead} The main local issues are {c['risk']}. {fact}"


def glance_table(ab):
    a, f, fe, L = acs(ab), fuel(ab), fema(ab), lic(ab)
    if L["kind"] == "local":
        lic_txt = "Cities and counties (no statewide plumber license)"
    elif L["kind"] == "contractor":
        lic_txt = f"{L['name']} (contractor license)"
    else:
        lic_txt = L["name"]
    rows = [
        ("Population", fmt(a["pop"])),
        ("Housing units", fmt(a["units"])),
        ("Median year homes were built", str(a["med"])),
        ("Homes built before 1980", f"{a['pre80']:g}%"),
        ("Homes built before 1940", f"{a['pre40']:g}%"),
        ("Homes heated with natural gas", f"{f['Utility gas']:g}%"),
        ("Homes heated with electricity", f"{f['Electricity']:g}%"),
        ("FEMA water-related disasters since 2000", f"{fe['water']} of {fe['major']} major disasters"),
        ("Plumbing license issued by", lic_txt),
    ]
    trs = "".join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in rows)
    return f'<div class="table-scroll"><table class="facts"><tbody>{trs}</tbody></table></div>'


def age_chart(ab):
    a = acs(ab)
    old, mid = a["pre40"], round(a["pre80"] - a["pre40"], 1)
    new = round(100 - a["pre80"], 1)
    rows = [("Before 1940", old), ("1940 to 1979", mid), ("1980 or later", new)]
    bars = "".join(
        f'<li><span class="bar-label">{k}</span><span class="bar-track"><span class="bar-fill" style="width:{max(v, 1):g}%"></span></span>'
        f'<span class="bar-val">{v:g}%</span></li>' for k, v in rows)
    return (f'<figure class="bars" aria-label="When homes in {short(ab)} were built">'
            f'<figcaption><strong>When homes in {short(ab)} were built</strong> (share of housing units, Census ACS 2020–2024)</figcaption>'
            f'<ul>{bars}</ul></figure>')


def housing_text(ab):
    a = acs(ab)
    name = the(ab)
    parts = []
    if a["pre40"] >= 15:
        parts.append(pick(ab, [
            f"{a['pre40']:g}% of homes in {name} were built before 1940. Many still have galvanized steel supply pipes, cast-iron drains or clay sewer laterals, which rust, crack and let roots in.",
            f"Old houses are common in {name}: {a['pre40']:g}% date from before 1940. Original galvanized water pipes and cast-iron or clay drains are often near the end of their life.",
        ], "p40"))
    elif a["pre80"] >= 45:
        parts.append(pick(ab, [
            f"With {a['pre80']:g}% of homes built before 1980, many {short(ab)} houses still have cast-iron drains and some galvanized supply lines.",
            f"{a['pre80']:g}% of the housing in {name} is more than 45 years old. Cast-iron drain stacks and older copper with lead solder are common in these homes.",
        ], "p80"))
    else:
        parts.append(pick(ab, [
            f"Housing in {name} is fairly young; the median home was built in {a['med']}. Most calls involve fixtures, water heaters, drain clogs and fittings rather than failing pipe.",
            f"The median home in {name} dates from {a['med']}, so most homes have copper, CPVC or PEX supply lines and plastic drains.",
        ], "new"))
    parts.append(pick(ab, [
        "The EPA says homes built before 1986 are more likely to have lead pipes, fixtures and solder; a water test and your utility's service line records tell you for sure.",
        "Homes built before 1986 are more likely to have lead pipes, fixtures or solder, according to the EPA. If yours is that old, test the water and ask your utility what your service line is made of.",
    ], "lead"))
    if 1974 <= a["med"] <= 1996:
        parts.append("Homes built from the late 1970s to the mid-1990s may also have gray polybutylene supply pipe, which has a history of failures.")
    links = ('See <a href="/services/repiping/">pipe repair and repiping</a>, <a href="/services/sewer-line-repair/">sewer line repair</a> '
             'and <a href="/services/water-line-repair/">water line repair</a>.')
    return f"<p>{' '.join(parts)} {links}</p>"


def heater_text(ab):
    f = fuel(ab)
    name = the(ab)
    s = []
    gas, el, prop, oil = f["Utility gas"], f["Electricity"], f["Propane or bottled gas"], f["Fuel oil or kerosene"]
    if gas >= 45:
        s.append(pick(ab, [
            f"Natural gas heats {gas:g}% of homes in {name}, and gas homes usually have gas water heaters too. That means burners, venting and <a href=\"/services/gas-line-repair/\">gas lines</a> to keep safe.",
            f"{gas:g}% of homes here heat with natural gas, so gas water heaters and <a href=\"/services/gas-line-repair/\">gas line</a> work are a large share of plumbing calls.",
        ], "gas"))
    elif el >= 55:
        s.append(pick(ab, [
            f"Electricity heats {el:g}% of homes in {name}, so electric tank water heaters are common. Burned-out elements and thermostats are frequent repairs, and <a href=\"/services/water-heater-installation/\">heat pump water heaters</a> cut running costs.",
            f"Most homes here ({el:g}%) heat with electricity. Electric water heaters dominate, and a <a href=\"/services/water-heater-installation/\">heat pump model</a> can lower bills when the old tank fails.",
        ], "el"))
    else:
        s.append(f"Homes in {name} split between natural gas ({gas:g}%) and electric heat ({el:g}%), so plumbers here service both gas and electric water heaters.")
    if prop >= 8:
        s.append(f"Propane heats {prop:g}% of homes, mostly in rural areas, and propane water heaters and lines need the same care as natural gas.")
    if oil >= 8:
        s.append(f"{oil:g}% of homes burn heating oil; many of them heat water with a boiler coil or an indirect tank.")
    s.append(pick(ab, [
        "The Department of Energy says most tank water heaters last 10 to 15 years.",
        "Most storage water heaters last 10 to 15 years, according to the Department of Energy.",
    ], "life") + ' See <a href="/services/water-heater-repair/">water heater repair</a> and <a href="/services/tankless-water-heaters/">tankless water heaters</a>.')
    return f"<p>{' '.join(s)}</p>"


def flood_text(ab):
    fe = fema(ab)
    name = the(ab)
    if fe["water"] == 0:
        return (f"<p>{name} has had no water-related FEMA major disaster declarations since 2000. "
                f"Most water damage here starts inside: burst supply lines, failed water heaters and overflowing toilets.</p>")
    recent = fe["recent"]
    rec = ""
    if recent:
        y, n = recent[0]
        first = n.split()[0]
        proper = first in ("Hurricane", "Tropical", "Typhoon", "Potential") or (len(n.split()) > 1 and n.split()[1][0].isupper())
        rec = f" The most recent was in {y} ({n if proper else n[0].lower() + n[1:]})."
    lead = pick(ab, [
        f"Since 2000, FEMA has declared {fe['water']} water-related major disasters in {name}, from floods, hurricanes and severe storms.",
        f"{name} has had {fe['water']} water-related federal disaster declarations since 2000.",
    ], "f")
    tail = pick(ab, [
        ' Heavy rain overloads sewers and fills basements, so <a href="/services/sump-pump-installation/">sump pumps</a>, backwater valves and <a href="/services/sewer-line-repair/">sewer line</a> repairs matter here.',
        ' Storms push sewage back up floor drains and flood low areas; a working <a href="/services/sump-pump-installation/">sump pump</a> and a backwater valve on the <a href="/services/sewer-line-repair/">sewer line</a> help.',
    ], "ft")
    return f"<p>{lead}{rec}{tail}</p>"


def problems_table(c):
    rows = "".join(f"<tr><td>{p}</td><td>{w}</td><td>{h}</td></tr>" for p, w, h in c["problems"])
    return ('<table><thead><tr><th>Problem</th><th>Where it shows up</th><th>Service that fixes it</th></tr></thead>'
            f'<tbody>{rows}</tbody></table>')


def licensing_section(ab, c):
    L = lic(ab)
    name, sh = the(ab), short(ab)
    if L["kind"] == "local":
        p1 = pick(ab, [
            f"{name} has no statewide plumber license. Cities and counties license plumbers and issue permits, so the rules in one town can differ from the next.",
            f"There is no statewide plumbing license in {name}; local governments license plumbers and run plumbing inspections.",
        ], "l1")
    elif L["kind"] == "contractor":
        p1 = pick(ab, [
            f"Plumbing contractors in {name} are licensed through the {lic_link(ab)}. Look up a company's license number there before work starts.",
            f"In {name}, the {lic_link(ab)} licenses plumbing contractors. Its online lookup shows whether a license is active.",
        ], "l1")
    else:
        p1 = pick(ab, [
            f"Plumbers in {name} are licensed by the {lic_link(ab)}. You can check a plumber's license there before work begins.",
            f"The {lic_link(ab)} licenses plumbers in {name}. Ask for the license number and look it up.",
        ], "l1")
    if c.get("licensing"):
        p1 += " " + c["licensing"]
    p2 = pick(ab, [
        f"Most {sh} cities and counties require a permit for water heater replacement, gas line work, sewer and water line replacement and new piping. The plumber usually pulls it and schedules the inspection.",
        f"Permits in {name} come from the city or county building department. Water heaters, gas piping, sewer laterals and repipes usually need one; simple fixture repairs usually do not.",
        f"In {name}, local building departments issue plumbing permits. Expect one for gas lines, water heaters, sewer or water service work and repiping.",
    ], "l2")
    p3 = pick(ab, [f"Every PipeMend job in {sh} goes to a plumber who holds the license that work requires there, and you get a written estimate before work starts.",
                   f"In {sh}, PipeMend sends plumbers licensed for the job where you live, and the price is in writing before any work begins."], "l3")
    return f"<p>{p1}</p>\n<p>{p2}</p>\n<p>{p3}</p>"


def faq(ab, c):
    name = the(ab)
    L = lic(ab)
    cities = DATA["cities"][ab]
    if ab == "DC":
        cover = ("Yes. PipeMend takes plumbing calls from every ward of the District, around the clock, "
                 "and from nearby Maryland and Virginia suburbs.")
    else:
        cover = (f"Yes. PipeMend takes plumbing calls from all of {name}, including {join_list(cities[:5])}, "
                 f"plus small towns and rural areas, 24 hours a day.")
    if L["kind"] == "local":
        lic_a = (f"{name} has no statewide plumber license, so cities and counties set the rules. "
                 f"Ask your local building department which license a plumber needs where you live.")
    elif L["kind"] == "contractor":
        lic_a = (f"Plumbing contractors are licensed by the {L['name']}, and some cities add their own rules. "
                 f"Check the license number before work starts.")
    else:
        lic_a = (f"Yes. The {L['name']} licenses plumbers in {name}. "
                 f"Gas line work may need its own license or endorsement.")
    permit_a = pick(ab, [
        f"Often, yes. Most local building departments in {name} require permits for water heaters, gas lines, sewer and water service lines and repiping. Small repairs such as a faucet or toilet usually do not need one.",
        f"For bigger jobs, yes. Water heater swaps, gas piping, sewer or water line replacement and repipes usually need a permit and inspection in {name}. Your plumber can pull it.",
    ], "pa")
    return [
        {"q": f"Do you have plumbers in all of {name}?", "a": cover},
        {"q": f"Do plumbers need a license in {name}?", "a": lic_a},
        {"q": f"Do I need a permit for plumbing work in {name}?", "a": permit_a},
        c["faq"],
    ]


SERVICES = json.loads((ROOT / "src" / "services.json").read_text())


def service_pills(sh):
    pills = "".join(f'<li><a href="/services/{x["slug"]}/">{x["name"]}</a></li>' for x in SERVICES)
    return f'<ul class="pills pills-sm">{pills}</ul>'


def nearby(ab):
    pills = "".join(f'<li><a href="{state_path(n)}">Plumbers in {short(n)}</a></li>' for n in META[ab]["neighbors"])
    pills += '<li><a href="/locations/">All states</a></li>'
    return f'<ul class="pills">{pills}</ul>'


GUIDE_RULES = [  # (slug, keywords in the state's own copy)
    ("how-to-keep-pipes-from-freezing", ("freez", "frozen", "ice storm", "cold snap")),
    ("water-heater-leaking", ("water heater",)),
    ("how-to-unclog-a-drain", ("root", "clog", "drain")),
    ("sewer-smell-in-house", ("sewer", "septic", "backup")),
    ("low-water-pressure-in-house", ("pressure", "galvanized", "hard water", "well")),
    ("polybutylene-pipes", ("polybutylene", "galvanized", "lead")),
    ("does-homeowners-insurance-cover-plumbing", ("flood", "hurricane", "insur")),
    ("tankless-vs-tank-water-heater", ("tankless", "scale")),
]


def guide_slugs(c):
    blob = json.dumps(c).lower()
    scored = sorted(((-sum(blob.count(k) for k in kws), i, slug) for i, (slug, kws) in enumerate(GUIDE_RULES)))
    return [s for _, _, s in scored[:3]]


def state_page(ab):
    c = load_content(ab)
    if not c:
        return None
    m = META[ab]
    L = lic(ab)
    name, sh = the(ab), short(ab)
    cities = DATA["cities"][ab]
    h1 = f"Plumbers and Plumbing Services in {sh}"
    title = f"Plumbers in {sh}: 24/7 Plumbing Services | PipeMend"
    if len(title) > 60:
        title = f"Plumbers in {sh}: 24/7 Plumbing | PipeMend"
    if len(title) > 60:
        title = f"Plumbers in {sh} | PipeMend"
    desc = f"Plumbers in {sh} for {c['risk_short']}. Leaks, drains, water heaters and sewer lines. Call PipeMend 24/7 at 1-800-555-0199."
    if len(desc) > 155:
        desc = f"Plumbers in {sh} for {c['risk_short']}. Call PipeMend 24/7 at 1-800-555-0199."
    if len(desc) > 155:
        desc = f"Plumbers in {sh} for {c['risk_short']}. Call 1-800-555-0199."
    tips_h = pick(ab, [f"Plumbing tips for {sh} homes", f"How to protect your plumbing in {sh}", f"Practical plumbing tips for {sh}"], "t")
    cta1 = pick(ab, [f"Plumbing problem in {sh}? Call PipeMend {{{{availability}}}}.",
                     f"Need a plumber in {sh}? Call PipeMend at {{{{phone}}}}."], "cta")
    cta2 = f"Leak, clog or no hot water anywhere in {sh}? Call {{{{phone}}}}."
    nb = [f'<a href="{state_path(n)}">{short(n)}</a>' for n in m["neighbors"]]
    nb_line = pick(ab, [f" Calls from neighboring {join_list(nb)} are covered too." if nb else "",
                        f" PipeMend also serves homes next door in {join_list(nb)}." if nb else "",
                        f" Plumbers are also available across the line in {join_list(nb)}." if nb else ""], "nb")
    if ab == "DC":
        areas_h = "Neighborhoods served in Washington, DC"
        areas_p = c["areas"] + nb_line
    else:
        areas_h = f"Areas served in {sh}"
        areas_p = (f"PipeMend takes plumbing calls across {name}. The largest communities are {join_list(cities)}. "
                   + c.get("areas", "") + nb_line)
    why_h = pick(ab, [f"Why plumbing in {sh} is different", f"What makes {sh} plumbing different", f"Local plumbing conditions in {sh}"], "w")
    body = f"""<p class="quick"><strong>Quick answer:</strong> {quick_answer(ab, c)}</p>

<h2>{sh} plumbing at a glance</h2>
{glance_table(ab)}
<p class="small-note">{sh} figures: Census ACS 2020–2024 (housing) and 2024 (heating fuel), and OpenFEMA disaster declarations from 2000 to November 2026.</p>

<h2>{why_h}</h2>
{''.join(f'<p>{p}</p>' for p in c['why'])}

<h2>Pipes, drains and housing age in {sh}</h2>
{age_chart(ab)}
{housing_text(ab)}

<h2>Common plumbing problems in {sh}</h2>
{problems_table(c)}
{{{{cta:{cta1}}}}}

<h2>Water heaters and gas lines in {sh}</h2>
{heater_text(ab)}

<h2>Storms, flooding and sewer backups in {sh}</h2>
{flood_text(ab)}

<h2>{tips_h}</h2>
<ul>{''.join(f'<li>{t}</li>' for t in c['tips'])}</ul>

<h2>Plumbing licenses and permits in {sh}</h2>
{licensing_section(ab, c)}
{{{{cta:{cta2}}}}}

<h2>{areas_h}</h2>
<p>{areas_p}</p>

{{{{faq}}}}

<h2>Plumbing services in {sh}</h2>
{service_pills(sh)}

<h2>Plumbers in nearby states</h2>
{nearby(ab)}

{{{{helpful_guides:{','.join(guide_slugs(c))}}}}}

{{{{sources}}}}
"""
    wiki = "https://en.wikipedia.org/wiki/" + WIKI.get(ab, m["name"].replace(" ", "_"))
    sources = [
        ["U.S. Census Bureau: American Community Survey", "https://www.census.gov/programs-surveys/acs"],
        ["FEMA: Disaster declarations", "https://www.fema.gov/disaster/declarations"],
        ["EPA: How can lead get into my drinking water?", "https://www.epa.gov/lead/how-can-lead-get-my-drinking-water"],
        ["U.S. Department of Energy: Energy Saver guide (water heating)", "https://www.energy.gov/sites/default/files/2022-08/energy-saver-guide-2022.pdf"],
    ]
    if L["url"]:
        sources.append([L["name"], L["url"]])
    sources += c.get("sources", [])
    return {
        "path": state_path(ab), "type": "state", "parents": [["Locations", "/locations/"]],
        "title": title, "description": desc, "h1": h1, "crumb": sh, "priority": "0.8",
        "lead": c["lead"],
        "chips": [f"All of {sh}" if ab != "DC" else "Every DC ward", "Homes, rentals and businesses", "24/7 plumbing calls"],
        "service": {"name": f"Plumbing services in {sh}", "serviceType": "Plumbing",
                    "areaServed": {"@type": "State" if ab != "DC" else "City", "name": sh, "sameAs": wiki}},
        "about": [[sh, wiki]],
        "mentions": [["Plumbing", "https://en.wikipedia.org/wiki/Plumbing"], ["Plumber", "https://en.wikipedia.org/wiki/Plumber"]],
        "faq_title": f"Plumbing questions in {sh}",
        "faq": faq(ab, c), "sources": sources,
        "body": body, "source": f"src/states/content/{ab}.json", "state": ab,
    }


def all_state_pages():
    return [p for p in (state_page(ab) for ab in sorted(META, key=lambda a: META[a]["name"])) if p]


REGIONS = {
    "Northeast": ["CT", "ME", "MA", "NH", "NJ", "NY", "PA", "RI", "VT"],
    "Midwest": ["IL", "IN", "IA", "KS", "MI", "MN", "MO", "NE", "ND", "OH", "SD", "WI"],
    "South": ["AL", "AR", "DE", "DC", "FL", "GA", "KY", "LA", "MD", "MS", "NC", "OK", "SC", "TN", "TX", "VA", "WV"],
    "West": ["AK", "AZ", "CA", "CO", "HI", "ID", "MT", "NV", "NM", "OR", "UT", "WA", "WY"],
}


def states_grid():
    """Cards for the locations hub, grouped by Census region."""
    out = []
    for reg, abs_ in REGIONS.items():
        cards = "".join(
            f'<li><a class="state-card" href="{state_path(a)}"><span class="state-name">{short(a)}</span>'
            f'<span class="state-cities">{", ".join(DATA["cities"][a][:3]) if a != "DC" else "All eight wards"}</span></a></li>'
            for a in sorted(abs_, key=lambda x: META[x]["name"]) if load_content(a))
        out.append(f'<h3>{reg}</h3><ul class="state-grid">{cards}</ul>')
    return "\n".join(out)


def state_pills():
    pills = "".join(f'<li><a href="{state_path(a)}">{short(a)}</a></li>'
                    for a in sorted(META, key=lambda x: META[x]["name"]) if load_content(a))
    return f'<ul class="pills pills-sm">{pills}</ul>'


def state_patterns():
    """National patterns table for the locations hub, computed from the same data as the state pages."""
    def link(a):
        return f'<a href="{state_path(a)}">{short(a)}</a>'
    al = [a for a in META if load_content(a)]
    top = lambda key, n=5: [link(a) for a in sorted(al, key=key)[:n]]
    rows = [
        ("Oldest housing (most homes built before 1940)", top(lambda a: -acs(a)["pre40"]),
         "Galvanized pipe, cast-iron and clay drains; repiping and sewer work"),
        ("Newest housing (latest median year built)", top(lambda a: -acs(a)["med"]),
         "Fixture, water heater and fitting repairs; slab leaks in slab-built areas"),
        ("Most FEMA water-related disasters since 2000", top(lambda a: -fema(a)["water"]),
         "Flooded basements, sewer backups and sump pumps"),
        ("Most homes heated with natural gas", top(lambda a: -fuel(a)["Utility gas"]),
         "Gas water heaters, venting and gas line work"),
        ("Most homes heated with electricity", top(lambda a: -fuel(a)["Electricity"]),
         "Electric and heat pump water heaters"),
    ]
    trs = "".join(f"<tr><td>{p}</td><td>{', '.join(s)}</td><td>{w}</td></tr>" for p, s, w in rows)
    return ('<table><thead><tr><th>Pattern</th><th>States where it stands out</th><th>What it means for plumbing</th></tr></thead>'
            f'<tbody>{trs}</tbody></table>')
