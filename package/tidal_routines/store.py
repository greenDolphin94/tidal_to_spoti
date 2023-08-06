import tidalapi

import os
import json

from ..common.logger import logErr, logInfo
from ..common.config import TIDAL_OUTPUT_DIR, TIDAL_FAVORITE_TRACKS_FILE, TIDAL_FAVORITE_ARTISTS_FILE, TIDAL_FAVORITE_ALBUMS_FILE, TIDAL_PLAYLIST_FILE

kName: str = 'name'
kArtist: str = 'artist'
kAlbum: str = 'album'

def _write_to_file(collection, entry_builder, filename, mode = 'w', encoding = 'utf-8') -> None:
    # Create reuslts folder if it does not exists
    if not os.path.exists(TIDAL_OUTPUT_DIR):
        os.makedirs(TIDAL_OUTPUT_DIR)
    
    with open(os.path.join(TIDAL_OUTPUT_DIR,filename), mode=mode, encoding=encoding) as oFile:
      for item in collection:
            try:
                oFile.write(f'{entry_builder(item)}\n')
            except Exception as err:
                logErr('Failed to write item ' + str(item.id))
                raise err

def store_favorite_tracks(collection) -> None:
    logInfo("Saving favorite tracks")
    def track_entry_builder(e: tidalapi.Track) -> str:
        # Use json dumps to automatically escape characters
        return json.dumps({
            kArtist:e.artist.name,
            kName:e.full_name,
            kAlbum:e.album.name
            })
    
    _write_to_file(collection, track_entry_builder, TIDAL_FAVORITE_TRACKS_FILE)

def store_favorite_artists(collection) -> None:
    logInfo("Saving favorite artists")
    def artist_entry_builder(e: tidalapi.Artist) -> str:
        return json.dumps({
            kArtist:e.name
        })
    
    _write_to_file(collection, artist_entry_builder, TIDAL_FAVORITE_ARTISTS_FILE)

def store_favorite_albums(collection) -> None:
    logInfo("Saving favorite albums")
    def album_entry_builder(e: tidalapi.Album) -> str:
        return json.dumps({
            kArtist:e.artist.name,
            kName:e.name
        })
    
    _write_to_file(collection, album_entry_builder, TIDAL_FAVORITE_ALBUMS_FILE)

def store_playlists(collection: list[tidalapi.Playlist]) -> None:
    logInfo("Saving playlists")
    def playlist_entry_builder(e: tidalapi.Track) -> str:
        return json.dumps({
            kArtist:e.artist.name,
            kName:e.full_name
        })
    for pl in collection:
        _write_to_file([f">>> {pl.name}\n"], lambda x:x, TIDAL_PLAYLIST_FILE, 'a')
        _write_to_file(pl.tracks(), playlist_entry_builder, TIDAL_PLAYLIST_FILE, 'a')
        _write_to_file(['\n'], lambda x:x, TIDAL_PLAYLIST_FILE, 'a')