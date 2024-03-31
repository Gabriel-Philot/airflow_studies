"""
Ingestion JOB
"""
from pathlib import Path
import json
import os
os.chdir('..')


from src.resources.spotify_api import SpotifyAPI, client_id, client_secret
from src.resources.config import bronze_path, file_name_bronze


def json_save_file_bronze(json_data):
    """
    This function creates a json file in the raw folder.
    """
    path_datalake_zone = bronze_path
    file_name = file_name_bronze
    print(f"---------- Saving file: {path_datalake_zone}/{file_name}")

    os.makedirs(path_datalake_zone, exist_ok=True)
    dest_path = f"{bronze_path}/{file_name}.json"
    
    with open(dest_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
    print(f"\nFile created at: {path_datalake_zone}")
    


artist_name = 'Gojira'

def extract_api():
    spotifyApi = SpotifyAPI(client_id, client_secret)
    artist = spotifyApi.search_for_artist(artist_name)
    if artist:
        songs = spotifyApi.get_songs_by_artist(artist, "BR")
        print(f"Songs found: {len(songs)}")
        json_save_file_bronze(songs)

    else:
        print(f"No artist found with name {artist_name}")
        return None


