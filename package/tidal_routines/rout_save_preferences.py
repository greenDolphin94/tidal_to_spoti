import tidalapi

from .login import tidal_login_session
from .store import store_favorite_tracks, store_favorite_artists, store_favorite_albums, store_playlists
from ..common.logger import logErr, logInfo

def run() -> None:
    logInfo("Begin Tidal routine")

    try:
        session = tidalapi.Session()
        tidal_login_session(session)

        favorite_tracks = session.user.favorites.tracks()
        store_favorite_tracks(favorite_tracks)
        favorite_artists = session.user.favorites.artists()
        store_favorite_artists(favorite_artists)
        favorite_albums = session.user.favorites.albums()
        store_favorite_albums(favorite_albums)
        playlists = session.user.favorites.playlists()
        store_playlists(playlists)

    except Exception as err:
        logErr(f"Exception occurred: {type(err)}")
        logErr(err)

    logInfo("End Tidal routine")
