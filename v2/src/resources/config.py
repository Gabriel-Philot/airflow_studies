# Organization of the paths to datalake

data_path = "/opt/local/airflow/datalake"

bronze_path = f"{data_path}/bronze"
silver_path = f"{data_path}/silver"
gold_path = f"{data_path}/gold"

# Organization of name of files

file_name = "top10_songs_artist"

file_name_bronze = f"{file_name}_bronze"
file_name_silver = f"{file_name}_silver"
file_name_gold = f"{file_name}_gold"

# Organization combo

bronze_file_path = f"{bronze_path}/{file_name_bronze}.json"
silver_file_path = f"{silver_path}/{file_name_silver}.parquet"
gold_file_path = f"{gold_path}/{file_name_gold}.csv"




## Postegress confis

schema_name_airflow = "airflow_schema"

table_name_silver = "top10_songs_artist_airflow_silver"


columns_schema_silver = {
        "artist_id": "VARCHAR(255)",
        "name_artist": "VARCHAR(255)",
        "top10_rank": "INTEGER",
        "song_name": "VARCHAR(255)", 
        "song_id": "VARCHAR(255)",
        "album_name": "VARCHAR(255)",
        "album_id": "VARCHAR(255)",
        "release_date": "DATE"
    }

key_column_silver = "song_id"


table_name_gold = "top10_songs_artist_airflow_gold"


columns_schema_gold = {
        "key_test": "VARCHAR(255)",
        "name_artist": "VARCHAR(255)",
        "album_name": "VARCHAR(255)",
        "kpi_songs": "INTEGER"
    }

key_column_gold = "key_test"
