"""
BUSINESS RULES JOB
"""

import json
import pandas as pd
import os


from src.resources.config import gold_path, file_name_gold, silver_file_path


def save_gold_data(df):
    path_zone = gold_path
    file_name = file_name_gold
    print(f"---------- Saving file: {path_zone}/{file_name}")
    os.makedirs(path_zone, exist_ok=True)
    dest_path = f"{path_zone}/{file_name}.csv"
    df.to_csv(dest_path, index=False)


def trasform_silver_data():
    df = pd.read_parquet(silver_file_path)
    grupocols = ["name_artist", "album_name"]
    df_agregate = (
        df.groupby(grupocols).size().reset_index().rename(columns={0: "kpi_songs"})
    )
    save_gold_data(df_agregate)
