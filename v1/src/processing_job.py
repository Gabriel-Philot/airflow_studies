"""
PROCESSING JOB
"""
import json
import pandas as pd
import os


from src.resources.process import transform_json_top10, transform_types
from src.resources.config import silver_path, file_name_silver, bronze_file_path


def save_parquet_from_json(df):
  
    path_zone = silver_path
    file_name = file_name_silver
    print(f"---------- Saving file: {path_zone}/{file_name}")
    os.makedirs(path_zone, exist_ok=True)
    dest_path = f"{path_zone}/{file_name}.parquet"
    df.to_parquet(dest_path)

    # print(f"File created at: {path_zone}")






def transform_api():
    with open(bronze_file_path, encoding='utf-8') as f:
        songs = json.load(f)
    top10 = transform_json_top10(songs)
    top10_df = transform_types(top10)
    print(top10_df.head())
    save_parquet_from_json(top10_df)
