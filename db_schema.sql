-- db_schema.sql
CREATE TABLE IF NOT EXISTS tournaments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sport TEXT NOT NULL,
    name TEXT NOT NULL,
    level TEXT,
    start_date TEXT,        -- ISO format YYYY-MM-DD
    end_date TEXT,          -- ISO format YYYY-MM-DD
    official_url TEXT,
    streaming_links TEXT,   -- JSON array string
    image_url TEXT,
    summary TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_sport ON tournaments (sport);
CREATE INDEX IF NOT EXISTS idx_start_date ON tournaments (start_date); 