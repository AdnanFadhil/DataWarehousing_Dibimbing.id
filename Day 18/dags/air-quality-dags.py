from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from my_custom_module import retrieve_data, transform_data, store_data_in_postgresql

default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'openaq_data_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['openaq'],
)

ingest_data_task = PythonOperator(
    task_id='ingest_data_task',
    python_callable=retrieve_data,
    dag=dag,
)

transform_data_task = PythonOperator(
    task_id='transform_data_task',
    python_callable=transform_data,
    dag=dag,
)

store_data_task = PythonOperator(
    task_id='store_data_task',
    python_callable=store_data_in_postgresql,
    provide_context=True,
    dag=dag,
)

ingest_data_task >> transform_data_task >> store_data_task
