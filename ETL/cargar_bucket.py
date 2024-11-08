from airflow import DAG
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from datetime import datetime

# Lista de archivos y bucket en GCS
BUCKET = 'etl_prueba_4-11'
# Carpeta en el bucket
base_gcs_path = 'data/carga_inicial/'
#ruta local
local_path = 'dags/data_raw/YELP/'
#

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 8),
}

with DAG(f'1_upload_to_gcs', default_args=default_args, schedule_interval='@once') as dag:

    upload_file_business = LocalFilesystemToGCSOperator(
        task_id=f'upload_file_business',
        src=f'{local_path}business.pkl',  # Ruta del archivo local
        dst=f'{base_gcs_path}business.pkl',  # Nombre del archivo en GCS
        bucket=BUCKET,  # Nombre de tu bucket de GCS
    )

    upload_file_checkin = LocalFilesystemToGCSOperator(
        task_id=f'upload_file_checkin',
        src=f'{local_path}checkin.json',  # Ruta del archivo local
        dst=f'{base_gcs_path}checkin.json',  # Nombre del archivo en GCS
        bucket=BUCKET,  # Nombre de tu bucket de GCS
    )

    upload_file_tip = LocalFilesystemToGCSOperator(
        task_id=f'upload_file_tip',
        src=f'{local_path}tip.json',  # Ruta del archivo local
        dst=f'{base_gcs_path}tip.json',  # Nombre del archivo en GCS
        bucket=BUCKET,  # Nombre de tu bucket de GCS
    )

    upload_file_user = LocalFilesystemToGCSOperator(
        task_id=f'upload_file_user',
        src=f'{local_path}user-002.csv',  # Ruta del archivo local
        dst=f'{base_gcs_path}user-002.csv',  # Nombre del archivo en GCS
        bucket=BUCKET,  # Nombre de tu bucket de GCS
    )

    upload_file_review = LocalFilesystemToGCSOperator(
        task_id=f'upload_file_review',
        src=f'{local_path}review-001.json',  # Ruta del archivo local
        dst=f'{base_gcs_path}review-001.json',  # Nombre del archivo en GCS
        bucket=BUCKET,  # Nombre de tu bucket de GCS
    )

