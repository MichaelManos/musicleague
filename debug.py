import musicleague as ml

leagues = {
    "Pilot - Grab Bag": r"C:\Users\Micha\OneDrive\Documents\2024\Music League",
    "2 Tracks 2 Curious": r"C:\Users\Micha\OneDrive\Documents\2025\Music League\2 - 2 Tracks 2 Curious",
    "A League of Our Own": r"C:\Users\Micha\OneDrive\Documents\2025\Music League\3 - A League of Our Own",
    "The League of Extraordinary Song Submissions": r"C:\Users\Micha\OneDrive\Documents\2026\Music League\4 - The League of Extraordinary Song Submissions",
}
database = ml.connect(":memory:")
ml.create_all(database)
for name in leagues:
    ml.insert_league(name, leagues[name], database)

ml.start_ui(database)


# TODO: View, data export
