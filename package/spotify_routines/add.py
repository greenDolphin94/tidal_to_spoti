import spotipy as sp

import os.path as path
import math

from ..common.config import SPOTIFY_SEARCH_OUTPUT_DIR, SPOTIFY_TRACKS_IDS_FILE, SPOTIFY_ARTISTS_IDS_FILE, SPOTIFY_ALBUMS_IDS_FILE
from ..common.logger import logInfo

def _read_from_file(inputFile: str) -> list[str]:
    if not path.exists(inputFile):
        raise FileNotFoundError(f'File {inputFile} not found')
    items = []
    with open(inputFile, 'r', encoding='utf-8') as iFile:
        items = iFile.read().splitlines()

    return items

def _group(collection: list[str], batch_size: int) -> list[list[str]]:
    return [[item for item in collection[i*batch_size: i*batch_size + batch_size]] for i in range(0, math.ceil(len(collection)/batch_size))]

def add_artists_from_file(spotify: sp.Spotify):
    logInfo('Following new artists on Spotify ...')
    artists = _read_from_file(path.join(SPOTIFY_SEARCH_OUTPUT_DIR, SPOTIFY_ARTISTS_IDS_FILE))
    for batch in _group(artists, 20):
        response = spotify.user_follow_artists(batch)

def add_albums_from_file(spotify: sp.Spotify):
    logInfo('Saving new albums on Spotify ...')
    albums = _read_from_file(path.join(SPOTIFY_SEARCH_OUTPUT_DIR, SPOTIFY_ALBUMS_IDS_FILE))
    for batch in _group(albums, 20):
        response = spotify.current_user_saved_albums_add(batch)

def add_tracks_from_file(spotify: sp.Spotify):
    logInfo('Saving new tracks on Spotify ...')
    tracks = _read_from_file(path.join(SPOTIFY_SEARCH_OUTPUT_DIR, SPOTIFY_TRACKS_IDS_FILE))
    for batch in _group(tracks, 20):
        response = spotify.current_user_saved_tracks_add(batch)
