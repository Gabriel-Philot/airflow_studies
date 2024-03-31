"""
PROCESSING JOB
"""
import json
import pandas as pd
import os
from src.resources.process import transform_json_top10, transform_types


def save_parquet_from_json(df):
    path_datalake = '/opt/local/airflow/datalake'
    path_zone = f"{path_datalake}/silver"
    filename = "top10_songs_artist_parquet"
    print(f"---------- Saving file: {path_zone}/{filename}")
    os.makedirs(path_zone, exist_ok=True)
    dest_path = f"{path_zone}/{filename}.parquet"
    df.to_parquet(dest_path)

    # print(f"File created at: {path_zone}")



path_json_file = '/opt/local/airflow/datalake/bronze/top10_songs_artist.json'


def transform_api():
    with open(path_json_file, encoding='utf-8') as f:
        songs = json.load(f)
    top10 = transform_json_top10(songs)
    top10_df = transform_types(top10)
    print(top10_df.head())
    save_parquet_from_json(top10_df)
