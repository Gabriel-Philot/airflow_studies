from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator



import sys
sys.path.insert(0, '/usr/local/airflow')

from src.resources.test_module import get_requests, get_beatiful


with DAG(
    dag_id = 'teste_dependencies',
    start_date=datetime(2023,10,16),
    # Intervalo de tempo que nossa orquestração irá rodar
    schedule_interval='0 13 * * *',
    # A partir da nossa start_date até hoje, o catchup caso seja True, todos os dags que não foram executados serão executados a partir da criação de uma nova dag
    catchup=False

) as dag:
    
    task_0 = PythonOperator(
        task_id = 'Requests',
        python_callable=get_requests

    )
    task_1 = PythonOperator(
        task_id = 'BeatifulSoup',
        python_callable=get_beatiful
    )

    task_0 >> task_1