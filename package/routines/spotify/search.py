import spotipy as sp

import os
import os.path as path
import json

from ...common.logger import logErr, logInfo
from ...common.config import TIDAL_OUTPUT_DIR, TIDAL_FAVORITE_TRACKS_FILE, TIDAL_FAVORITE_ARTISTS_FILE, TIDAL_FAVORITE_ALBUMS_FILE
from ...common.config import SPOTIFY_SEARCH_OUTPUT_DIR, SPOTIFY_NOT_FOUND_FILE


kArtist: str = 'artist'
kArtists: str = 'artists'
kAlbum: str = 'album'
kAlbums: str = 'albums'
kTrack: str = 'track'
kTracks: str = 'tracks'
kName: str = 'name'

kItems: str = 'items'
kId: str = 'id'

def _store_not_found_queries(queries: list[str]) -> None:
    if not path.exists(SPOTIFY_SEARCH_OUTPUT_DIR):
        os.makedirs(SPOTIFY_SEARCH_OUTPUT_DIR)
        
    with open(path.join(SPOTIFY_SEARCH_OUTPUT_DIR, SPOTIFY_NOT_FOUND_FILE), 'a', encoding='utf-8') as oFile:
        for query in queries:
            oFile.write(f"{query}\n")


def _build_queries(inputFile: str, query_builder) -> list[str]:
    if not path.exists(inputFile):
        logErr(f'File {inputFile} not found')
        raise FileNotFoundError(f'File {inputFile} not found')
    
    queries = []
    with open(inputFile, 'r') as iFile:
        for item in iFile.readlines():
            parsed = json.loads(item.strip())
            queries.append(query_builder(parsed))
    
    return queries

def _search(spotify: sp.Spotify, input_tidal_file, query_builder, spotify_search_type, result_validator, id_accessor) -> list[str]:
    ids = []
    not_found = []
    queries = _build_queries(input_tidal_file, query_builder)
    for query in queries:
        result = spotify.search(query, limit=1, type=spotify_search_type)
        if result_validator(result):
            ids.append(id_accessor(result))
        else:
            logInfo(f'Nothing found for query "{query}" and type "{spotify_search_type}"')
            not_found.append(query)

    _store_not_found_queries(not_found)
    return ids

def search_artists_ids(spotify: sp.Spotify) -> list[str]:
    logInfo('Searching for artists on Spotify ...')
    return _search(spotify, 
                  input_tidal_file=path.join(TIDAL_OUTPUT_DIR, TIDAL_FAVORITE_ARTISTS_FILE), 
                  query_builder=lambda x:x[kArtist],
                  spotify_search_type=kArtist,
                  result_validator=lambda x:len(x[kArtists][kItems]) > 0,
                  id_accessor=lambda x:x[kArtists][kItems][0][kId])

def search_albums_ids(spotify: sp.Spotify) -> list[str]:
    logInfo('Searching for albums on Spotify ...')
    return _search(spotify, 
                  input_tidal_file=path.join(TIDAL_OUTPUT_DIR, TIDAL_FAVORITE_ALBUMS_FILE), 
                  query_builder=lambda x:f'artist:{x[kArtist]} album:{x[kName]}',
                  spotify_search_type=kAlbum,
                  result_validator=lambda x:len(x[kAlbums][kItems]) > 0,
                  id_accessor=lambda x:x[kAlbums][kItems][0][kId])

def search_tracks_ids(spotify: sp.Spotify) -> list[str]:
    logInfo('Searching for tracks on Spotify ...')
    return _search(spotify, 
                  input_tidal_file=path.join(TIDAL_OUTPUT_DIR, TIDAL_FAVORITE_TRACKS_FILE), 
                  query_builder=lambda x:f'artist:{x[kArtist]} track:{x[kName]}',
                  spotify_search_type=kTrack,
                  result_validator=lambda x:len(x[kTracks][kItems]) > 0,
                  id_accessor=lambda x:x[kTracks][kItems][0][kId])