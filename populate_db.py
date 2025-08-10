# populate_db.py
import sqlite3
import json
import sys
from pathlib import Path

DB_FILE = "tournaments.db"
DATA_FILE = Path("data/sample_tournaments.json")

def create_schema(conn):
    with open("db_schema.sql", "r") as f:
        conn.executescript(f.read())

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def insert_tournament(conn, t):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO tournaments
        (sport, name, level, start_date, end_date, official_url, streaming_links, image_url, summary)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        t.get("sport"),
        t.get("name"),
        t.get("level"),
        t.get("start_date"),
        t.get("end_date"),
        t.get("official_url"),
        json.dumps(t.get("streaming_links", [])),
        t.get("image_url"),
        t.get("summary")
    ))
    conn.commit()

def main():
    if not DATA_FILE.exists():
        print(f"Data file {DATA_FILE} not found. Exiting.")
        sys.exit(1)

    data = load_json(DATA_FILE)
    conn = sqlite3.connect(DB_FILE)
    create_schema(conn)
    for t in data:
        insert_tournament(conn, t)
    conn.close()
    print(f"Inserted {len(data)} tournament records into {DB_FILE}")

if __name__ == "__main__":
    main() 