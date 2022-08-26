from airflow import DAG
from airflow.operators.python_operator import PythonOperator
# from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from etl_pipe import _extract, _transform, _load 
# import os

# cwd = os.getcwd()

default_args = {
    "owner": "airflow",
    "start_date": datetime.today() - timedelta(days=1)
              }
with DAG(
    "dag_nyc_covid",
    default_args=default_args,
    schedule_interval = "0 1 * * *",
    ) as dag:
    
    extractData = PythonOperator(
            task_id="extract_data",
            python_callable =_extract,
            dag=dag)
    transformData = PythonOperator(
            task_id="transform_data",
            python_callable =_transform,
            dag=dag)
    loadData = PythonOperator(
            task_id="load_data",
            python_callable =_load,
            dag=dag)

    extractData >> transformData >> loadData