from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
from airflow.operators.python import PythonOperator

import sys

sys.path.insert(0, "/usr/local/airflow")

from v2.src.load_db_cloud_job import save_db_postgress_silver


def load_silver_data_cloud():

    with TaskGroup("silver_persist", tooltip="silver data upload") as group:

        wait_a = BashOperator(
            task_id='wait_a',
            bash_command='sleep 10'
        )

        ingestion = PythonOperator(
            task_id='persist_cloud_silver', 
            python_callable=save_db_postgress_silver,
            provide_context=True,
        )

        wait_b = BashOperator(
            task_id='wait_b',
            bash_command='sleep 10'
        )

        return group