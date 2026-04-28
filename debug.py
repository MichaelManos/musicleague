import musicleague as ml

league_data = ml.read_dir(r"C:\Users\Micha\OneDrive\Documents\2024\Music League")

database = ml.db.connect(":memory:")

ml.db.create_all(database)

database.sql("SELECT * FROM league")
database.sql("INSERT INTO league (name) VALUES ('league1')")
