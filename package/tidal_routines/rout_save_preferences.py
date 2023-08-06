import tidalapi

from .login import read_login_credentials, store_login_credentials
from .store import store_favorite_tracks, store_favorite_artists, store_favorite_albums, store_playlists
from ..common.logger import logErr, logInfo

def run() -> None:
    logInfo("Begin Tidal routine")

    try:
        session = tidalapi.Session()
        credentials = read_login_credentials()

        if len(credentials) == 4 and session.load_oauth_session(credentials[0], credentials[1], credentials[2], credentials[3]):
                logInfo('Login successful for user  ' + session.user.email)
        else:
            # Will run until you visit the printed url and link your account
            session.login_oauth_simple()
            store_login_credentials(session)

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
