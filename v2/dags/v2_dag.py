from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from groups.silver_load import load_silver_data_cloud
from groups.gold_load import load_gold_data_cloud

import sys

sys.path.insert(0, "/usr/local/airflow")

from src.ingestion_job import extract_api
from src.processing_job import transform_api
from src.businessrules_job import trasform_silver_data



with DAG(
    dag_id="dag_v2_group",
    start_date=datetime(2023, 10, 16),
    # Intervalo de tempo que nossa orquestração irá rodar
    schedule_interval="0 13 * * *",
    # A partir da nossa start_date até hoje, o catchup caso seja True, todos os dags que não foram executados serão executados a partir da criação de uma nova dag
    catchup=False,
) as dag:
     
    args = {'start_date': dag.start_date, 'schedule_interval': dag.schedule_interval, 'catchup': dag.catchup}


    extract_task = PythonOperator(
        task_id="ingestion_data",
        python_callable=extract_api,
        provide_context=True,
    )

    process_task = PythonOperator(
        task_id="processing_data",
        python_callable=transform_api,
        provide_context=True,
    )

    transform_task = PythonOperator(
        task_id="apply_business_rules",
        python_callable=trasform_silver_data,
        provide_context=True,
    )

    silver_group = load_silver_data_cloud()

    golden_group = load_gold_data_cloud()




extract_task >> process_task >> transform_task >> silver_group  >> golden_group
