from airflow import DAG
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import os
import pandas as pd

# Lista de archivos y bucket en GCS
BUCKET = 'etl_prueba_4-11'
# Carpeta en el bucket
base_gcs_path = 'data/carga_inicial/'  
#nombre de nuestro archivo
file_name = 'business.pkl'
#ruta donde vamos a tener nuestro archivo descargado temporalmente
local_path = f'/tmp/{file_name}'
#ruta temporal de nuestro archivo convertido
transformed_path = '/tmp/business.csv'

#lista de ciudades para filtrar
list_city = ['Houston','New York','Chicago','Los Angeles','Brooklyn','San Antonio','Dallas','Las Vegas','Miami','Philadelphia']
#quitamos la terminacion pkl y agregamos csv
#transformed_path = os.path.splitext(local_path)[0] + '.csv'

def verificar_archivo_en_gcs(file):
            gcs_hook = GCSHook()
            if gcs_hook.exists(bucket_name=BUCKET, object_name=f'{base_gcs_path}{file}'):
                print(f"El archivo {file} existe en GCS.")
            else:
                raise FileNotFoundError(f"El archivo {file} no existe en GCS.")
            
def download():
    gcs_hook = GCSHook()
    #metodo download- parametros (1 = bucket donde bajamos el archivo, 2 = la ruta dentro del bucket, 3 = y el destino donde lo vamos a descargar)
    gcs_hook.download(bucket_name=BUCKET, object_name=f'{base_gcs_path}{file_name}', filename=local_path)      

def transform(**context):
    df = pd.read_pickle(local_path)
    print("DATOS SIN PROCESAR: ", df.shape)
    # eliminamos columnas duplicadas, ya que fue revisado en el analisis preliminar y no contienen filas con datos de valor
    df = df.loc[:, ~df.columns.duplicated()]
    #filtramos solo los comercios por las ciudades objetivos del proyecto
    df = df[df['city'].isin(list_city)]
    #convertimos el archivo_filtrado a csv
    print("DATOS PROCESADOS: ", df.shape)
    df.to_csv(transformed_path, index=False)

def upload_data():
    gcs_hook = GCSHook()
    #metodo upload- parametros (1 = bucket donde subimos el archivo, 2 = la ruta donde quedara el archivo transformado, 3 = y la ruta de donde vamos a cargar el archivo)
    gcs_hook.upload(bucket_name=BUCKET, object_name='data/data_city_filter/business_filtered.csv', filename=transformed_path) 
    
def remove_temp():
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
    'filtra_ciudades_business_v2',
    default_args=default_args,
    description='Procesa secuencialmente: descarga, quita columnas duplicadas y filtra por las ciudades que elegimos en el analisis preliminar para finalmente transformar a CSV y subir a GCS',
    # Todos los lunes, jamas un viernes! jamas!
    schedule_interval='0 2 * * 1',  # Expresión cron para 2 AM todos los lunes
    start_date=days_ago(1),
    catchup=False,
) as dag:

    # Sensor que espera a que dag1 finalice exitosamente
    espera_dag1 = ExternalTaskSensor(
        task_id='espera_upload_to_gcs',
        external_dag_id='upload_to_gcs',
        external_task_id='upload_file_review',
        mode='poke',
        timeout=600,
        poke_interval=60,
    )
    # Verificación de archivo en GCS
    verificar_archivo = PythonOperator(
        task_id=f'verificar_archivo_en_gcs_business',
        python_callable=verificar_archivo_en_gcs,
        op_args=['business.pkl']
    )
    download_task = PythonOperator(
        task_id=f'download',
        python_callable=download
    )
    # Transformar el archivo a CSV
    transform_task = PythonOperator(
        task_id=f'filter_upload_business',
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

    # Definir la secuencia para el archivo actual
    espera_dag1>>verificar_archivo >> download_task >> transform_task >> upload_data_task >> remove_temp_task
