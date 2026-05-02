"""Module to handle Spotify API connections and data pulls

Note that this module is essentially deprecated. It can be used but is not
needed for core functionality.
"""

import datetime
import json
import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

_config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")


def connect(client_id: str = "", client_secret: str = "") -> spotipy.Spotify:
    if len(client_id) == 0:
        client_id = _default_client_id()
    if len(client_secret) == 0:
        client_secret = _default_client_secret()

    redirect_uri = "http://127.0.0.1:9090"
    scope = "user-library-read"

    client = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
        )
    )
    return client


def extract_playlist_id(url: str) -> str:
    """Returns playlist ID given URL to playlist."""
    return url.split("/")[-1]


def read_playlist(client: spotipy.Spotify, playlist_id: str):
    playlist_data = client.playlist(playlist_id)
    return playlist_data


def playlist_date(playlist_data: dict):
    """Infer playlist creation date based on track dates"""
    return min(
        [track["added_at"] for track in playlist_data["items"]["items"]]
    )


def playlist_date_from_url(
    url: str, client_id: str = "", client_secret: str = ""
) -> datetime.datetime:
    """Gets playlist creation date given a URL to the playlist

    Returns
    -------
    Date song was first added to playlist. If the playlist cannot be found,
    default date of 1/1/1900 will be given instead of error.
    """
    client = connect(client_id, client_secret)
    try:
        playlist_data = read_playlist(client, extract_playlist_id(url))
    except spotipy.SpotifyException:
        return datetime.datetime(1900, 1, 1)
    first_track = playlist_date(playlist_data)
    return datetime.datetime.fromisoformat(first_track[:-1]).astimezone(
        datetime.timezone.utc
    )


def _default_client_id() -> str:
    with open(_config_path, "r") as file:
        data = json.load(file)
    return data["spotify_client_id"]


def _default_client_secret() -> str:
    with open(_config_path, "r") as file:
        data = json.load(file)
    return data["spotify_client_secret"]
