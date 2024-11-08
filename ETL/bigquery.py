from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.utils.dates import days_ago
from datetime import datetime

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 8),
    'retries': 1,
}

# Define the DAG
with DAG(
    'gcs_to_bigquery_dag',
    default_args=default_args,
    # Todos los lunes, jamas un viernes! jamas!
    schedule_interval='0 2 * * 1',  # Expresión cron para 2 AM todos los lunes
    start_date=days_ago(1),
    catchup=False,
) as dag:

    # Task to load data from GCS to BigQuery
    load_data_checkin = GCSToBigQueryOperator(
        task_id='load_gcs_to_bigquery',
        bucket='etl_prueba_4-11',  # Replace with your GCS bucket name
        source_objects=['data/data_city_filter/checkin_filtered.csv'],  # Replace with your file path in GCS
        destination_project_dataset_table='utopian-honor-438417-u7.Sociuslab.checkin',  # Replace with your BigQuery table
        write_disposition='WRITE_TRUNCATE',
        create_disposition= 'CREATE_IF_NEEDED',
        skip_leading_rows=1,
    )

    load_data_business = GCSToBigQueryOperator(
        task_id='load_gcs_to_bigquery',
        bucket='etl_prueba_4-11',  # Replace with your GCS bucket name
        source_objects=['data/data_city_filter/business_filtered.csv'],  # Replace with your file path in GCS
        destination_project_dataset_table='utopian-honor-438417-u7.Sociuslab.business',  # Replace with your BigQuery table
        write_disposition='WRITE_TRUNCATE',
        create_disposition= 'CREATE_IF_NEEDED',
        skip_leading_rows=1,
    )

    load_data_tip = GCSToBigQueryOperator(
        task_id='load_gcs_to_bigquery',
        bucket='etl_prueba_4-11',  # Replace with your GCS bucket name
        source_objects=['data/data_city_filter/tip_filtered.csv'],  # Replace with your file path in GCS
        destination_project_dataset_table='utopian-honor-438417-u7.Sociuslab.tip',  # Replace with your BigQuery table
        write_disposition='WRITE_TRUNCATE',
        create_disposition= 'CREATE_IF_NEEDED',
        skip_leading_rows=1,
    )

    load_data_review = GCSToBigQueryOperator(
        task_id='load_gcs_to_bigquery',
        bucket='etl_prueba_4-11',  # Replace with your GCS bucket name
        source_objects=['data/data_city_filter/review_filtered.csv'],  # Replace with your file path in GCS
        destination_project_dataset_table='utopian-honor-438417-u7.Sociuslab.review',  # Replace with your BigQuery table
        write_disposition='WRITE_TRUNCATE',
        create_disposition= 'CREATE_IF_NEEDED',
        skip_leading_rows=1,
    )

    load_data_user = GCSToBigQueryOperator(
        task_id='load_gcs_to_bigquery',
        bucket='etl_prueba_4-11',  # Replace with your GCS bucket name
        source_objects=['data/data_city_filter/users_filtered.csv'],  # Replace with your file path in GCS
        destination_project_dataset_table='utopian-honor-438417-u7.Sociuslab.users',  # Replace with your BigQuery table
        write_disposition='WRITE_TRUNCATE',
        create_disposition= 'CREATE_IF_NEEDED',
        skip_leading_rows=1,
    )


load_data_checkin>>load_data_business>>load_data_tip>>load_data_user>>load_data_review
#create_dataset >> transform_file >> load_bigquery