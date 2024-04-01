from psycopg2.extras import execute_values
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
# from dataclasses import dataclass

load_dotenv()

user_postegress = os.getenv("POSTGRES_USER")
pass_postegress = os.getenv("POSTGRES_PASSWORD")
host_postegress = os.getenv("PGHOST")
db_postegress = os.getenv("POSTGRES_DB")
port = 5432

class PostgresDb:

  def __init__(self, host, database, user,  password, port):
    self.host = host
    self.database = database
    self.user = user  
    self.password = password
    self.port = port

  def connect(self):
    self.conn = psycopg2.connect(
        host=self.host,
        database=self.database, 
        user=self.user,
        password=self.password,
        port = self.port
    )

  def create_update_table(self, df, dbschema_name, table_name, columns_schema,  key_column):
    
    try:
      cursor = self.conn.cursor()
      # Create Schema
      cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {dbschema_name}")
      # Create table
      cols_str_sql = ','.join([f'"{col}" {data_type}' for col, data_type in columns_schema.items()])
      create_table_sql = f"CREATE TABLE IF NOT EXISTS {dbschema_name}.{table_name} ({cols_str_sql})"
      cursor.execute(create_table_sql)

      # INSERT/UPDATE INTO TABLE
      for _, row in df.iterrows():

        select_sql = f"SELECT {key_column} FROM {dbschema_name}.{table_name} WHERE {key_column} = '{row[key_column]}'"

        cursor.execute(select_sql)
        result = cursor.fetchone()

        if result:
          update_table = f"""
             UPDATE {dbschema_name}.{table_name} SET
             """
          for col, value in columns_schema.items():
             update_table += f"{col} = '{row[col]}',"
          update_table = update_table[:-1] # Remove última vírgula
          update_table += f"WHERE {key_column} = '{row[key_column]}'"
          print(update_table)
          cursor.execute(update_table)

        else:
           # Formating values
            values = [tuple(row[col] for col in columns_schema)]
            value_rows = [str(tuple(x)) for x in values]

            # Query INSERT
            insert_sql = f"INSERT INTO {dbschema_name}.{table_name} ({', '.join(columns_schema)}) VALUES {', '.join(value_rows)}"
            cursor.execute(insert_sql)

     
      self.conn.commit()
      cursor.close()
      self.conn.close()

    except:
      self.conn.rollback()
      cursor.close()
      self.conn.close()
      raise Exception("Error into create or insert data into PostgreSQL.")
    
    
  def run_query(self, query):
    cursor = self.conn.cursor() 
    cursor.execute(query)
    records = cursor.fetchall()
    cols = [desc[0] for desc in cursor.description]
    cursor.close()

    return records, cols