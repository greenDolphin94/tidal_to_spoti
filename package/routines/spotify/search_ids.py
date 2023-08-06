import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import os

from .search import search_artists_ids, search_albums_ids, search_tracks_ids
from .store import storeIds
from ...common.logger import logInfo, logErr
from ...common.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_TRACKS_IDS_FILE, SPOTIFY_ARTISTS_IDS_FILE, SPOTIFY_ALBUMS_IDS_FILE

from ..routine import Routine

class SearchIdsRoutine(Routine):
    def __init__(self, id: str) -> None:
        super().__init__(id)

    def run(self) -> bool:
        try:
            auth_manager = SpotifyClientCredentials(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
            sp = spotipy.Spotify(auth_manager=auth_manager)

            artists_ids = search_artists_ids(sp)
            storeIds(artists_ids, SPOTIFY_ARTISTS_IDS_FILE)
            albums_ids = search_albums_ids(sp)
            storeIds(albums_ids, SPOTIFY_ALBUMS_IDS_FILE)
            tracks_ids = search_tracks_ids(sp)
            storeIds(tracks_ids, SPOTIFY_TRACKS_IDS_FILE)

        except Exception as err:
            logErr(f"Exception occurred: {type(err)}")
            logErr(err)
            return False

        return True
