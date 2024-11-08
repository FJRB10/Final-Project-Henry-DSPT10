from airflow import DAG
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.utils.dates import days_ago
import os
import pandas as pd

# Lista de archivos y bucket en GCS
BUCKET = 'etl_prueba_4-11'
# Carpeta en el bucket
base_gcs_path = 'data/carga_inicial/'
# ruta archivo para filtrar
path_filter = 'data/data_city_filter/'
#nombre del archivo para filtrar
file_filter = 'business_filtered.csv'
#ruta local para el archivo temporal del filtrador
local_filter = f'/tmp/{file_filter}'
#nombre de nuestro archivo
file_name = 'review-001.json'
#ruta temporal de nuestro archivo transformado
transformed_path = '/tmp/review.csv'
#ruta donde vamos a tener nuestro archivo descargado temporalmente
local_path = f'/tmp/{file_name}'
#ruta destino en Google Cloud
destiny_gcs = 'data/data_city_filter/review_filtered.csv'

#antes de proceder nos aseguramos de que el archivo este bien cargado en el storage
def verificar_archivo_en_gcs(file):
    gcs_hook = GCSHook()
    if gcs_hook.exists(bucket_name=BUCKET, object_name=f'{base_gcs_path}{file}'):
        print(f"El archivo {file} existe en GCS.")
    else:
        raise FileNotFoundError(f"El archivo {file} no existe en GCS.")

#antes de proceder nos aseguramos de que el archivo este bien cargado en el storage
def verificar_filtrador_en_gcs():
    gcs_hook = GCSHook()
    if gcs_hook.exists(bucket_name=BUCKET, object_name=f'{path_filter}{file_filter}'):
        print(f"El archivo {file_filter} existe en GCS.")
    else:
        raise FileNotFoundError(f"El archivo {file_filter} no existe en GCS.")
            
def get_filter():
    gsc_hook = GCSHook()
    #metodo download- parametros (1 = bucket donde bajamos el archivo, 2 = la ruta dentro del bucket, 3 = y el destino donde lo vamos a descargar)
    gsc_hook.download(bucket_name=BUCKET,object_name=f'{path_filter}{file_filter}',filename=local_filter)
    df = pd.read_csv(local_filter)
    df = df['business_id'].to_list()
    return df

def download_file_review():
    gsc_hook = GCSHook()
    #metodo download- parametros (1 = bucket donde bajamos el archivo, 2 = la ruta dentro del bucket, 3 = y el destino donde lo vamos a descargar)
    gsc_hook.download(bucket_name=BUCKET,object_name=f'{base_gcs_path}{file_name}',filename=local_path)

def filtrar_json_pandas(chunk_size=50000, **context):
    #recuperamos la variable lista almacenada en Xcom 
    list_business = context['ti'].xcom_pull(task_ids='get_filter')
    #indica si es el primer lote
    first_chunk = True
    # Leer el archivo en chunks
    for chunk in pd.read_json(local_path, lines=True, chunksize=chunk_size):
        # Filtrar basado en la lista que decidimos de ciudades
        chunk_filtrado = chunk[chunk['business_id'].isin(list_business)]
        # Guardar en CSV, usando append después del primer chunk
        chunk_filtrado.to_csv(transformed_path, mode='a', index=False, header=first_chunk)
        first_chunk = False

def transform(**context):
    #en este caso usamos la funcion para filtrar antes de convertir, ya que es un archivo muy grande para procesar y consume muchos recursos
    df = pd.read_csv(transformed_path)
    #convertimos el archivo_filtrado a csv
    df = df.drop_duplicates(subset='text', keep=False)
    print("DATOS PROCESADOS: ", df.shape)
    df.to_csv(transformed_path, index=False)

def upload_data():
    gcs_hook = GCSHook()
    #metodo upload- parametros (1 = bucket donde subimos el archivo, 2 = la ruta donde quedara el archivo transformado, 3 = y la ruta de donde vamos a cargar el archivo)
    gcs_hook.upload(bucket_name=BUCKET, object_name=destiny_gcs, filename=transformed_path) 
    
def remove_temp():
    os.remove(local_filter)
    os.remove(local_path)
    os.remove(transformed_path)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    'filtra_review',
    default_args=default_args,
    description='Procesa secuencialmente: descarga, quita columnas duplicadas y filtra por las ciudades que elegimos en el analisis preliminar para finalmente transformar a CSV y subir a GCS',
    # Todos los lunes, jamas un viernes! jamas!
    schedule_interval='0 2 * * 1',  # Expresión cron para 2 AM todos los lunes
    start_date=days_ago(1),
    catchup=False,
) as dag:
    #sensor para esperar la tarea de filter business
    espera_ciudades = ExternalTaskSensor(
        task_id='espera_tarea_tip',
        external_dag_id='filtra_tip',
        external_task_id='remove_temporary_files',
        mode='poke',
        timeout=600,
        poke_interval=60,
    )
    # Verificación de archivo en GCS
    verificar_archivo_task = PythonOperator(
        task_id=f'verificar_archivo_en_gcs_business',
        python_callable=verificar_archivo_en_gcs,
        op_args=['tip.json']
    )
    verificar_filtrador_task = PythonOperator(
        task_id=f'verificar_filtrador_en_gcs_business',
        python_callable=verificar_filtrador_en_gcs,
    )
    get_filter_task = PythonOperator(
        task_id=f'get_filter',
        python_callable=get_filter
    )
    download_task = PythonOperator(
        task_id=f'download',
        python_callable=download_file_review
    )
    # filtrar la lista por las ciudades
    filter_task = PythonOperator(
        task_id=f'filter_file',
        python_callable=filtrar_json_pandas,
        provide_context=True
    )
    # Transformar el archivo a CSV
    transform_task = PythonOperator(
        task_id=f'transform_file',
        python_callable=transform,
        provide_context=True
    )
    upload_data_task = PythonOperator(
        task_id=f'upload',
        python_callable=upload_data
    )
    remove_temp_task = PythonOperator(
        task_id=f'remove_temporary_files',
        python_callable=remove_temp
    )

    espera_ciudades>>verificar_archivo_task >> verificar_filtrador_task >> [get_filter_task, download_task ]>> filter_task >> transform_task >> upload_data_task >> remove_temp_task