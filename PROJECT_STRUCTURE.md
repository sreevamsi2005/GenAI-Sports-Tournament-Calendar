# GenAI Sports Tournament Calendar - Project Structure

## Complete File Organization

```
GenAI Sports Tournament Calendar/
├── app.py                      # Main Flask application (API + UI routes)
├── db_schema.sql               # SQLite database schema
├── populate_db.py              # Script to load sample data into database
├── requirements.txt            # Python dependencies
├── README.md                   # Comprehensive setup and usage instructions
├── sample_output.csv           # Example CSV export
├── PROJECT_STRUCTURE.md        # This file - project overview
├── tournaments.db              # SQLite database (created by populate_db.py)
│
├── data/
│   └── sample_tournaments.json # Sample dataset with 12 tournaments
│
├── scripts/
│   └── live_scrape_template.py # Template for fetching live tournament data
│
├── templates/
│   └── index.html              # Main UI template
│
└── static/
    └── app.js                  # JavaScript for UI functionality
```

## Key Features Implemented

### 1. Database Layer
- **SQLite database** with tournaments table
- **Schema includes**: sport, name, level, start_date, end_date, official_url, streaming_links, image_url, summary
- **Indexes** for fast filtering by sport and start_date
- **JSON storage** for streaming_links array

### 2. API Endpoints
- `GET /api/tournaments` - JSON API with filtering (sport, level, limit)
- `GET /api/tournaments/csv` - CSV export download
- `GET /` - Web UI interface

### 3. User Interface
- **Simple HTML + jQuery** (no React as per requirements)
- **Filtering controls** for sport and level
- **Card-based layout** showing tournament details
- **CSV download link**
- **Responsive design** with placeholder images

### 4. Data Management
- **Sample dataset** with 12 diverse sports events
- **Easy data replacement** via JSON file
- **Database population script** for quick setup
- **Live data integration template** for production use

### 5. Sample Data Coverage
- **12 different sports**: Cricket, Football, Badminton, Running, Gym, Cycling, Swimming, Kabaddi, Yoga, Basketball, Chess, Table Tennis
- **Multiple levels**: College/University, State, Zonal/Regional, City/Club, Club/Academy, District, National
- **Realistic tournament names** and descriptions
- **Placeholder images** and streaming links

## Quick Start Commands

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Populate database with sample data
python populate_db.py

# 3. Start the application
python app.py

# 4. Access the application
# Web UI: http://127.0.0.1:5000/
# API: http://127.0.0.1:5000/api/tournaments
# CSV: http://127.0.0.1:5000/api/tournaments/csv
```

## API Usage Examples

```bash
# Get all tournaments
curl http://127.0.0.1:5000/api/tournaments

# Filter by sport
curl http://127.0.0.1:5000/api/tournaments?sport=Cricket

# Filter by level
curl http://127.0.0.1:5000/api/tournaments?level=State

# Combine filters
curl http://127.0.0.1:5000/api/tournaments?sport=Football&level=State

# Limit results
curl http://127.0.0.1:5000/api/tournaments?limit=5
```

## Production Readiness

The project is designed to be easily extended for production use:

1. **Replace sample data** with live tournament information
2. **Use the scraper template** in `scripts/live_scrape_template.py`
3. **Add authentication** if needed
4. **Scale database** to PostgreSQL/MySQL for larger datasets
5. **Add caching** with Redis for better performance
6. **Implement scheduled updates** for fresh tournament data

## Assignment Compliance

✅ **Local SQLite storage** - Single file database  
✅ **JSON API endpoint** - GET /api/tournaments with filtering  
✅ **CSV export** - Download functionality  
✅ **Simple HTML+JS UI** - No React, jQuery-based  
✅ **All required fields** - Tournament name, level, dates, URLs, images, summary  
✅ **Filtering capability** - By sport and level  
✅ **Sample data** - 12 diverse tournaments  
✅ **Documentation** - Comprehensive README and setup instructions  

The project is ready for immediate use and demonstration! 