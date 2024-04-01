"""
LOAD DB CLOUD job
"""

import json
import pandas as pd
import os


from src.resources.postgress import PostgresDb, user_postegress, pass_postegress, host_postegress, db_postegress, port
from src.resources.config import schema_name_airflow, table_name_silver, columns_schema_silver, key_column_silver, table_name_gold, columns_schema_gold, key_column_gold
from src.resources.config import silver_file_path, gold_file_path


def save_db_postgress_silver():
    df = pd.read_parquet(silver_file_path)
    db = PostgresDb(host_postegress, db_postegress, user_postegress, pass_postegress, port)
    db.connect()
    db.create_update_table(df, schema_name_airflow, table_name_silver, columns_schema_silver, key_column_silver)


def save_db_postgress_golden():
    df = pd.read_csv(gold_file_path)
    df["key_test"] = df["name_artist"] + df["album_name"] # Adjusting wil be done here sometimes
    db = PostgresDb(host_postegress, db_postegress, user_postegress, pass_postegress, port)
    db.connect()
    db.create_update_table(df, schema_name_airflow, table_name_gold, columns_schema_gold, key_column_gold)
