# dag_carga
from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator

default_args = ''
file_config = []

with DAG(
    'load_data_dag',
    default_args=default_args,
    schedule_interval=None
) as dag:

    for folder, config in file_config.items():

        transformed_file_path = f"carga_incremental/{folder}_transformed.csv" 
        table_name = config['table']

     
        load_to_bigquery = GCSToBigQueryOperator(
            task_id=f'load_to_bigquery_{folder}',
            bucket='etl_agu',
            source_objects=[transformed_file_path],
            destination_project_dataset_table=table_name,
            source_format='CSV',
            write_disposition='WRITE_TRUNCATE',
            create_disposition='CREATE_IF_NEEDED',
            skip_leading_rows=1,
            max_bad_records=5,
            allow_quoted_newlines=True
        )
