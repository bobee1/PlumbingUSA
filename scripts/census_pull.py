#!/usr/bin/env python3
"""Pull Census ACS 5-year housing data for the next PipeMend city pages.

Run on any computer with internet access (no API key needed):
    python3 scripts/census_pull.py
It writes one pair of files per city batch, in the same format as research/10 and 11:
  Build 6c: research/13-city-acs-6c.json, research/14-city-heating-fuel-6c.json
  Build 7:  research/15-city-acs-7.json,  research/16-city-heating-fuel-7.json
Commit and push them (or send them back) and the city pages can be built.
Run one batch only with:  python3 scripts/census_pull.py 7
Standard library only.
"""
import json, sys, urllib.request, urllib.parse
from pathlib import Path

# (city label used in meta, state FIPS, exact Census place name)
CITIES = [
    ("Scottsdale", "04", "Scottsdale city, Arizona"),
    ("Chandler", "04", "Chandler city, Arizona"),
    ("Glendale", "04", "Glendale city, Arizona"),
    ("Anaheim", "06", "Anaheim city, California"),
    ("San Francisco", "06", "San Francisco city, California"),
    ("Chula Vista", "06", "Chula Vista city, California"),
    ("Irvine", "06", "Irvine city, California"),
    ("Oakland", "06", "Oakland city, California"),
    ("Fremont", "06", "Fremont city, California"),
    ("Santa Ana", "06", "Santa Ana city, California"),
    ("New Orleans", "22", "New Orleans city, Louisiana"),
    ("St. Petersburg", "12", "St. Petersburg city, Florida"),
    ("Boston", "25", "Boston city, Massachusetts"),
    ("Garland", "48", "Garland city, Texas"),
    ("Lubbock", "48", "Lubbock city, Texas"),
    ("Irving", "48", "Irving city, Texas"),
    ("Albuquerque", "35", "Albuquerque city, New Mexico"),
    ("Richmond", "51", "Richmond city, Virginia"),
    ("Virginia Beach", "51", "Virginia Beach city, Virginia"),
    ("Greensboro", "37", "Greensboro city, North Carolina"),
    ("Detroit", "26", "Detroit city, Michigan"),
    ("St. Louis", "29", "St. Louis city, Missouri"),
    ("Henderson", "32", "Henderson city, Nevada"),
    ("Tulsa", "40", "Tulsa city, Oklahoma"),
    ("Lexington", "21", "Lexington-Fayette urban county, Kentucky"),
]

CITIES_7 = [
    ("Spokane", "53", "Spokane city, Washington"),
    ("Winston-Salem", "37", "Winston-Salem city, North Carolina"),
    ("Riverside", "06", "Riverside city, California"),
    ("Stockton", "06", "Stockton city, California"),
    ("Fresno", "06", "Fresno city, California"),
    ("Bakersfield", "06", "Bakersfield city, California"),
    ("Fort Wayne", "18", "Fort Wayne city, Indiana"),
    ("El Paso", "48", "El Paso city, Texas"),
    ("Corpus Christi", "48", "Corpus Christi city, Texas"),
    ("Laredo", "48", "Laredo city, Texas"),
    ("Toledo", "39", "Toledo city, Ohio"),
    ("Jersey City", "34", "Jersey City city, New Jersey"),
    ("Newark", "34", "Newark city, New Jersey"),
    ("Anchorage", "02", "Anchorage municipality, Alaska"),
    ("Chesapeake", "51", "Chesapeake city, Virginia"),
    ("Norfolk", "51", "Norfolk city, Virginia"),
    ("Hialeah", "12", "Hialeah city, Florida"),
    ("Lincoln", "31", "Lincoln city, Nebraska"),
    ("Honolulu", "15", "Urban Honolulu CDP, Hawaii"),
    ("Milwaukee", "55", "Milwaukee city, Wisconsin"),
    ("North Las Vegas", "32", "North Las Vegas city, Nevada"),
    ("Buffalo", "36", "Buffalo city, New York"),
    ("Oklahoma City", "40", "Oklahoma City city, Oklahoma"),
    ("St. Paul", "27", "St. Paul city, Minnesota"),
]

BATCHES = {
    "6c": (CITIES, "13-city-acs-6c.json", "14-city-heating-fuel-6c.json"),
    "7": (CITIES_7, "15-city-acs-7.json", "16-city-heating-fuel-7.json"),
}

YB = [f"B25034_{i:03d}E" for i in range(1, 12)]   # year built: total, 2020+, ... 1939 or earlier
FUEL = [f"B25040_{i:03d}E" for i in range(1, 11)]  # heating fuel: total, gas, LP, elec, oil, coal, wood, solar, other, none
VARS = ["NAME", "B01003_001E", "B25001_001E", "B25035_001E", "B25003_001E", "B25003_002E",
        "B25024_001E", "B25024_010E"] + YB + FUEL


def fetch(year, state):
    q = urllib.parse.urlencode({"get": ",".join(VARS), "for": "place:*", "in": f"state:{state}"})
    url = f"https://api.census.gov/data/{year}/acs/acs5?{q}"
    with urllib.request.urlopen(url, timeout=60) as r:
        rows = json.load(r)
    head = rows[0]
    return {row[0]: dict(zip(head, row)) for row in rows[1:]}


def pct(a, b):
    return round(100.0 * a / b, 1) if b else 0.0


def find(cache, year, st, name):
    if st not in cache:
        cache[st] = fetch(year, st)
    d = cache[st].get(name)
    if d:
        return d
    # fall back to a case-insensitive match on the part before the comma
    short = name.split(",")[0].lower()
    hits = [v for k, v in cache[st].items() if k.lower().startswith(short)]
    return hits[0] if len(hits) == 1 else None


def run_batch(batch, year, cache, out):
    cities, acs_file, fuel_file = BATCHES[batch]
    acs, fuel = {}, {}
    print(f"\nBatch {batch}:")
    for label, st, name in cities:
        d = find(cache, year, st, name)
        if not d:
            print("NOT FOUND:", name); continue
        n = {k: int(float(v)) for k, v in d.items() if k.endswith("E") and k != "NAME" and v not in (None, "")}
        yb_total = n["B25034_001E"]
        pre80 = sum(n[f"B25034_{i:03d}E"] for i in range(7, 12))
        pre40 = n["B25034_011E"]
        key = f"{label}|{st}"
        acs[key] = [n["B01003_001E"], n["B25001_001E"], n["B25035_001E"], pct(pre80, yb_total),
                    pct(pre40, yb_total), pct(n["B25003_002E"], n["B25003_001E"]),
                    pct(n["B25024_010E"], n["B25024_001E"])]
        t = n["B25040_001E"]
        fuel[key] = [pct(n["B25040_002E"], t), pct(n["B25040_003E"], t), pct(n["B25040_004E"], t),
                     pct(n["B25040_005E"], t), pct(n["B25040_006E"], t), pct(n["B25040_007E"], t),
                     pct(n["B25040_010E"], t), t]
        print(f"ok  {label}, {st}: built {acs[key][2]}, pre-1980 {acs[key][3]}%")
    src = f"U.S. Census Bureau ACS {year - 4}-{year} 5-year via api.census.gov"
    (out / acs_file).write_text(json.dumps({
        "_source": f"{src} (B01003, B25001, B25035, B25034, B25003, B25024)",
        "fields": ["population", "housing_units", "median_year_built", "built_before_1980_pct",
                   "built_before_1940_pct", "owner_occupied_pct", "mobile_home_pct"],
        "places": acs}, indent=1))
    (out / fuel_file).write_text(json.dumps({
        "_source": f"{src}, table B25040 House Heating Fuel (occupied housing units)",
        "fields": ["utility_gas_pct", "propane_pct", "electricity_pct", "fuel_oil_pct", "coal_pct",
                   "wood_pct", "no_fuel_pct", "occupied_units"],
        "places": fuel}, indent=1))
    print(f"Wrote {len(acs)} cities to research/{acs_file} and research/{fuel_file}")


def main():
    batches = sys.argv[1:] or list(BATCHES)
    year = None
    for y in (2024, 2023):
        try:
            fetch(y, "04"); year = y; break
        except Exception as e:
            print(f"ACS {y} 5-year not available ({e}); trying older year")
    if not year:
        sys.exit("Could not reach api.census.gov")
    out = Path(__file__).resolve().parent.parent / "research"
    cache = {}
    for b in batches:
        run_batch(b, year, cache, out)


if __name__ == "__main__":
    main()
