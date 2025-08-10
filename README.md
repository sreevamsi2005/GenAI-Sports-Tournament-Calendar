# GenAI Intern Assignment — Tournament Calendar (MVP)


---

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
I attempted to fetch live up-to-date tournaments automatically for you but my web-fetching tool failed during preparation.Beacause of failure of fetching realtime updates but able to fetch from sample data used for this project .The code is intentionally designed so that swapping the JSON is trivial.

