# GenAI Intern Assignment — Tournament Calendar (MVP)


---

## What this repo contains
- `app.py` — Flask app exposing:
  - `GET /api/tournaments` — JSON API (query params: `sport`, `level`, `limit`)
  - `GET /api/tournaments/csv` — Download CSV
  - A basic UI at `/` (index.html)
- `db_schema.sql` — SQLite schema
- `populate_db.py` — Load sample JSON into `tournaments.db`
- `data/sample_tournaments.json` — Sample dataset (12 events)
- `templates/index.html`, `static/app.js` — Simple UI
- `sample_output.csv` — Example CSV export (you can re-generate)

---

## Sample Output
![Sample Output](SampleOutput.png)
### Web UI Interface
The application provides a clean, responsive web interface for browsing tournaments:

```
┌─────────────────────────────────────────────────────────────────┐
│                    GenAI Tournament Calendar — Demo              │
├─────────────────────────────────────────────────────────────────┤
│ Sport: [All ▼]  Level: [All ▼]  [Filter]  [Download CSV]        │
├─────────────────────────────────────────────────────────────────┤
│ ┌─────────────┐ ┌─────────────────────────────────────────────┐ │
│ │             │ │ Cricket — Inter-University Cricket          │ │
│ │   [Image]   │ │ Championship 2025                           │ │
│ │             │ │ College/University | 2025-08-20 → 2025-08-28│ │
│ └─────────────┘ │                                             │ │
│                 │ A multi-university cricket tournament       │ │
│                 │ featuring 16 teams across the region...     │ │
│                 │                                             │ │
│                 │ Official | Watch                            │ │
│ └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│ ┌─────────────┐ ┌─────────────────────────────────────────────┐ │
│ │             │ │ Football — State Youth Football Cup 2025    │ │
│ │   [Image]   │ │ State | 2025-09-05 → 2025-09-12             │ │
│ │             │ │                                             │ │
│ └─────────────┘ │ State-level youth football cup with district│ │
│                 │ winners from across the state...            │ │
│                 │                                             │ │
│                 │ Official | Watch                            │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Quick setup
1. Clone or copy files into a folder.
2. Create Python venv and install Flask:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install flask
   ```
3. Populate DB with sample data:
   ```bash
   python populate_db.py
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open UI: http://127.0.0.1:5000/
   API: http://127.0.0.1:5000/api/tournaments


## Limitations 
I attempted to fetch live up-to-date tournaments automatically for you but my web-fetching tool failed during preparation. Because the assignment requires upcoming real tournaments, please replace `data/sample_tournaments.json` with a verified dataset (either run the live_scrape_template.py with your API keys and then manually verify or use federation APIs). The code is intentionally designed so that swapping the JSON is trivial.

If you'd like, I can re-run live collection for you now (fetch and produce a verified dataset) once I have the ability to access the web or if you provide API keys. Until then, the submission includes a realistic sample dataset and a reproducible pipeline for live updating.

