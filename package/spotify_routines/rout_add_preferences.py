import spotipy
from spotipy.oauth2 import SpotifyOAuth

from .add import add_artists_from_file, add_albums_from_file, add_tracks_from_file
from ..common.logger import logInfo, logErr
from ..common.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, SPOTIFY_SCOPE_LIB_MODIFY, SPOTIFY_SCOPE_FOLL_MODIFY

def run() -> None:
    logInfo("Begin Spotify add routine")

    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            SPOTIFY_CLIENT_ID, 
            SPOTIFY_CLIENT_SECRET, 
            SPOTIFY_REDIRECT_URI, 
            scope=f'{SPOTIFY_SCOPE_LIB_MODIFY},{SPOTIFY_SCOPE_FOLL_MODIFY}'))

        add_tracks_from_file(sp)
        add_albums_from_file(sp)
        add_artists_from_file(sp)

    except Exception as err:
        logErr(f"Exception occurred: {type(err)}")
        logErr(err)

    logInfo("End Spotify add routine")
