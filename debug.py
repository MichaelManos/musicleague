import os
os.chdir(r"C:\Users\Micha\OneDrive\Projects\musicleague")

import musicleague as ml

league_data = ml.read_dir(r"C:\Users\Micha\OneDrive\Documents\2024\Music League")

client = ml.spotify.connect()
data = ml.spotify.read_playlist(client, ml.spotify.extract_playlist_id("https://open.spotify.com/playlist/6YgZUdiz8yEtupEGCOJVkM"))
ml.spotify.playlist_date(data)
