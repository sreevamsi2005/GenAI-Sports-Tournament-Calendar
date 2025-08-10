# scripts/live_scrape_template.py
# NOTE: requires an API key and CSE id for Google Custom Search
import requests
import json
from time import sleep
CSE_KEY = "YOUR_GOOGLE_CSE_API_KEY"
CSE_ID = "YOUR_CSE_ID"

SPORT_QUERIES = {
    "Cricket": ["upcoming cricket tournaments 2025 site:espncricinfo.com", "cricket tournament schedule 2025 site:icc-cricket.com"],
    "Badminton": ["BWF tournament calendar 2025"],
    # add queries for each sport
}

def search(query):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {"key": CSE_KEY, "cx": CSE_ID, "q": query}
    r = requests.get(url, params=params)
    r.raise_for_status()
    return r.json()

def simple_extract(item):
    # Extract title/link/snippet (manual verification recommended)
    return {"title": item.get("title"), "link": item.get("link"), "snippet": item.get("snippet")}

def main():
    out = []
    for sport, queries in SPORT_QUERIES.items():
        for q in queries:
            res = search(q)
            items = res.get("items", [])
            for it in items:
                out.append({"sport": sport, "name": it.get("title"), "official_url": it.get("link"), "summary": it.get("snippet")})
            sleep(1)
    with open("data/live_tournaments.json","w",encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print("Wrote data/live_tournaments.json (manual verification required)")

if __name__ == "__main__":
    main() 