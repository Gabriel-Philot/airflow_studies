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
