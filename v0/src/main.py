from src.resources.spotify_api import SpotifyAPI, client_id, client_secret
from src.resources.process import transform_json_top10, transform_types
import pandas as pd


artist_name = 'Gojira'

def extract_api(artist_name):
    spotifyApi = SpotifyAPI(client_id, client_secret)
    artist = spotifyApi.search_for_artist(artist_name)
    if artist:
        songs = spotifyApi.get_songs_by_artist(artist['id'], "BR")
        print(f"Songs found: {len(songs)}")
        return artist, songs

    else:
        print(f"No artist found with name {artist_name}")
        return None


def transform_api(**kwargs):
    ti = kwargs['ti']
    artist, songs = ti.xcom_pull(task_ids='extract_data')
    top10 = transform_json_top10(artist, songs)
    top10_df = transform_types(top10)
    print(top10_df.head())
    return top10_df

