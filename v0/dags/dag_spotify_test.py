from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

import sys

sys.path.insert(0, "/usr/local/airflow")

# from src.resources.test_addnewmodule import sum_print
from src.main import extract_api, transform_api, artist_name

# artist_name = 'Gojira'


with DAG(
    dag_id="spotify_test00",
    start_date=datetime(2023, 10, 16),
    # Intervalo de tempo que nossa orquestração irá rodar
    schedule_interval="0 13 * * *",
    # A partir da nossa start_date até hoje, o catchup caso seja True, todos os dags que não foram executados serão executados a partir da criação de uma nova dag
    catchup=False,
) as dag:

    # Defina a tarefa de extração
    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract_api,
        op_args=[artist_name],
        provide_context=True,
    )

    # Defina a tarefa de transformação
    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_api,
        provide_context=True,
    )

# Defina as dependências entre as tarefas
extract_task >> transform_task
