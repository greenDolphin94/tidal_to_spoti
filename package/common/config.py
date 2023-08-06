import os
import os.path as path

import json

root = os.getcwd()

# Routines
ROUTINES_CONFIG_FILE_PATH = path.join(root, 'routines.json')

# Tidal
TIDAL_AUTH_TOKENS_FILE_PATH = path.join(root, 'package', 'routines', 'tidal', 'tidal_secrets.txt')
TIDAL_OUTPUT_DIR = path.join(root, 'output', 'tidal')
TIDAL_FAVORITE_TRACKS_FILE = 'FavoriteTracks.txt'
TIDAL_FAVORITE_ARTISTS_FILE = 'FavoriteArtists.txt'
TIDAL_FAVORITE_ALBUMS_FILE = 'FavoriteAlbums.txt'
TIDAL_PLAYLIST_FILE = 'Playlists.txt'

# Spotify
SPOTIFY_SECRETS_FILE = path.join(root, 'secrets.json')
json_secrets = dict()
with open(SPOTIFY_SECRETS_FILE, 'r') as iFile:
    json_secrets = json.loads(iFile.read())

SPOTIFY_CLIENT_ID = json_secrets['spotify_client_id']
SPOTIFY_CLIENT_SECRET = json_secrets['spotify_client_secret']
SPOTIFY_REDIRECT_URI = json_secrets['spotify_redirect_uri']
SPOTIFY_SCOPE_LIB_MODIFY = 'user-library-modify'
SPOTIFY_SCOPE_FOLL_MODIFY = 'user-follow-modify'
SPOTIFY_SEARCH_OUTPUT_DIR = path.join(root, 'output', 'spotify')
SPOTIFY_TRACKS_IDS_FILE = 'SpotifyTracksIds.txt'
SPOTIFY_ARTISTS_IDS_FILE = 'SpotifyArtistsIds.txt'
SPOTIFY_ALBUMS_IDS_FILE = 'SpotifyAlbumsIds.txt'
SPOTIFY_NOT_FOUND_FILE = 'NotFoundItems.txt'

# Logging
LOG_DIR = path.join(root, 'output', 'log')
LOG_INFO_FILE = path.join(LOG_DIR, 'log.txt')
LOG_ERR_FILE = path.join(LOG_DIR, 'logErr.txt')