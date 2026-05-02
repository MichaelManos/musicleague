# musicleague
Scratchwork repository for reading and organizing Music League data

## Installation
To install using pip:
`pip install git+https://github.com/MichaelManos/musicleague`

## Suggested Use
```python
import musicleague as ml

leagues = {
    "Pilot - Grab Bag": r"C:\Users\Micha\OneDrive\Documents\2024\Music League",
    "2 Tracks 2 Curious": r"C:\Users\Micha\OneDrive\Documents\2025\Music League\2 - 2 Tracks 2 Curious",
    "A League of Our Own": r"C:\Users\Micha\OneDrive\Documents\2025\Music League\3 - A League of Our Own",
    "The League of Extraordinary Song Submissions": r"C:\Users\Micha\OneDrive\Documents\2026\Music League\4 - The League of Extraordinary Song Submissions",
}
# database = ml.connect(":memory:")  # For in memory version
database = ml.connect("musicleague.db")
for name in leagues:
    ml.insert_league(name, leagues[name], database)

df = ml.export(database)  # Export as pandas DataFrame
ml.export(database, "musicleague.xlsx")  # Export as Excel
ml.export(database, "musicleague.csv")  # Export as CSV

ml.start_ui(database)  # Exploratory analysis
```
