import os

from ...common.config import SPOTIFY_SEARCH_OUTPUT_DIR

def storeIds(resultIds: list, fileName: str):
    # Create results folder if it does not exists
    if not os.path.exists(SPOTIFY_SEARCH_OUTPUT_DIR):
        os.makedirs(SPOTIFY_SEARCH_OUTPUT_DIR)
    with open(os.path.join(SPOTIFY_SEARCH_OUTPUT_DIR, fileName), mode='w', encoding='utf-8') as oFile:
        for id in resultIds:
            oFile.write(f"{id}\n")