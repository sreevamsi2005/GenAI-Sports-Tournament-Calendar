# app.py
from flask import Flask, jsonify, request, g, send_from_directory, render_template
import sqlite3
import json
from pathlib import Path
import csv
import io

DB_FILE = "tournaments.db"
app = Flask(__name__, static_folder="static", template_folder="templates")

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DB_FILE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

def row_to_dict(row):
    d = dict(row)
    # parse streaming_links JSON string to Python list
    try:
        d["streaming_links"] = json.loads(d["streaming_links"] or "[]")
    except:
        d["streaming_links"] = []
    return d

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/tournaments", methods=["GET"])
def get_tournaments():
    sport = request.args.get("sport")
    level = request.args.get("level")
    limit = request.args.get("limit", type=int)
    q = "SELECT * FROM tournaments WHERE 1=1"
    params = []
    if sport:
        q += " AND sport = ?"
        params.append(sport)
    if level:
        q += " AND level = ?"
        params.append(level)
    q += " ORDER BY start_date ASC"
    if limit:
        q += " LIMIT ?"
        params.append(limit)
    cur = get_db().execute(q, params)
    rows = cur.fetchall()
    data = [row_to_dict(r) for r in rows]
    return jsonify({"count": len(data), "results": data})

@app.route("/api/tournaments/csv", methods=["GET"])
def download_csv():
    cur = get_db().execute("SELECT * FROM tournaments ORDER BY start_date ASC")
    rows = cur.fetchall()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["sport","name","level","start_date","end_date","official_url","streaming_links","image_url","summary"])
    for r in rows:
        writer.writerow([
            r["sport"],
            r["name"],
            r["level"],
            r["start_date"],
            r["end_date"],
            r["official_url"],
            r["streaming_links"],
            r["image_url"],
            r["summary"]
        ])
    output.seek(0)
    return app.response_class(output.getvalue(), mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=tournaments.csv"})

if __name__ == "__main__":
    # Ensure DB file exists (create empty if not)
    Path(DB_FILE).touch(exist_ok=True)
    app.run(host="0.0.0.0", port=5000, debug=True) 