import os
import json

from ..common.logger import logInfo
from ..common.config import ROUTINES_CONFIG_FILE_PATH

from .tidal.store_all_preferences import StoreAllPreferencesRoutine
from .spotify.search_ids import SearchIdsRoutine
from .spotify.add_ids_to_favorites import AddIdsToFavoritesRoutine

from .routine import Routine

_RoutinesMap : dict[str, Routine] = {
    'StoreAllPreferences' : StoreAllPreferencesRoutine('TidalRoutine_StoreAllPreferences'),
    'SearchIds' : SearchIdsRoutine('SpotifyRoutine_SearchIds'),
    'AddIdsToFavorites' : AddIdsToFavoritesRoutine('SpotifyRoutine_AddIdsToFavorites')
}

def _append_if_valid(key: str, collection: list[Routine]) -> None:
    if (selected := _RoutinesMap.get(key)) is not None:
            collection.append(selected)
    else:
        logInfo(f'Unknown routine {key}, skipping')

def _load_routines_from_file(fileName: str) -> dict[str, object]:
    if not os.path.exists(fileName):
        raise RuntimeError(f'Missing "{fileName}". Please specify the routines to be executed. Abort')
    
    selected_routines = dict()
    with open(fileName, 'r') as iFile:
        selected_routines = json.loads(iFile.read())

    return selected_routines
     
def init_routines() -> list[Routine]:
    requested_routines = _load_routines_from_file(ROUTINES_CONFIG_FILE_PATH)
    valid_routines: list[Routine] = []
    for r in requested_routines['tidal']:
        _append_if_valid(r, valid_routines)
    for r in requested_routines['spotify']:
        _append_if_valid(r, valid_routines)

    return valid_routines