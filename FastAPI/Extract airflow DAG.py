from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def execute_fastapi_task():
    # Aquí podrías hacer una solicitud HTTP a tu servicio en Cloud Run
    import requests
    response = requests.get("https://https://sociuslabextraction-150928410393.us-central1.run.app/fetch-places-data")
    if response.status_code != 200:
        raise Exception("Error al ejecutar el servicio de FastAPI")

with DAG(
    'upload_google_maps_data_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None
) as dag:
    upload_task = PythonOperator(
        task_id='upload_data',
        python_callable=execute_fastapi_task
    )
