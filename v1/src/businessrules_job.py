"""
BUSINESS RULES JOB
"""
import json
import pandas as pd
import os



path_praquet_file = '/opt/local/airflow/datalake/silver/top10_songs_artist_parquet.parquet'


def save_gold_data(df):
    path_datalake = '/opt/local/airflow/datalake'
    path_zone = f"{path_datalake}/gold"
    filename = "business_rules"
    print(f"---------- Saving file: {path_zone}/{filename}")
    os.makedirs(path_zone, exist_ok=True)
    dest_path = f"{path_zone}/{filename}.csv"
    df.to_csv(dest_path, index=False)



def trasform_silver_data():
    df = pd.read_parquet(path_praquet_file)
    grupocols = ['name_artist', 'album_name']
    df_agregate = df.groupby(grupocols).size().reset_index() \
        .rename(columns={0: 'kpi_songs'})
    save_gold_data(df_agregate)
    

