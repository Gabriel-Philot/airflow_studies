"""
Ingestion JOB
"""
from pathlib import Path
import json
import os
os.chdir('..')


from src.resources.spotify_api import SpotifyAPI, client_id, client_secret

def json_save_file(name_file, json_data, zone):
    """
    This function creates a json file in the raw folder.
    """
    path_datalake = '/opt/local/airflow/datalake'
    path_zone = f"{path_datalake}/{zone}"
    print(f"---------- Saving file: {path_zone}/{name_file}")

    os.makedirs(path_zone, exist_ok=True)
    dest_path = f"{path_zone}/{name_file}.json"
    
    with open(dest_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)
    print(f"\nFile created at: {path_zone}")
    


artist_name = 'Gojira'
# file_name = f"top10_{artist_name}"
# zone = 'raw'

def extract_api():
    spotifyApi = SpotifyAPI(client_id, client_secret)
    artist = spotifyApi.search_for_artist(artist_name)
    if artist:
        songs = spotifyApi.get_songs_by_artist(artist, "BR")
        print(f"Songs found: {len(songs)}")
        file_name = "top10_songs_artist"
        zone = 'bronze'
        json_save_file(file_name, songs, zone)

    else:
        print(f"No artist found with name {artist_name}")
        return None


