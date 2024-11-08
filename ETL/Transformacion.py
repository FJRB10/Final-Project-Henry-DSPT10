#Transformacion

import logging
import pandas as pd
import pickle
import csv
import tempfile
from google.cloud import storage
import io

def transform_file(bucket_name, gcs_file_path, transformed_path, selected_columns, **kwargs):
    
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(gcs_file_path)
    
    logging.info(f"Reading file from GCS: gs://{bucket_name}/{gcs_file_path}")

    data = blob.download_as_bytes()
    if gcs_file_path.endswith('.parquet'):
        df = pd.read_parquet(io.BytesIO(data))
    elif gcs_file_path.endswith('.json'):
        df = pd.read_json(io.BytesIO(data), lines=True)
    elif gcs_file_path.endswith('.pkl') or gcs_file_path.endswith('.pickle'):
        df = pickle.loads(data)
    else:
        raise ValueError("Formato de archivo no soportado")

    df = df[selected_columns]
    logging.info("Primeras filas del DataFrame transformado:\n%s", df.head())

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df.to_csv(
        temp_file.name,
        index=False,
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        encoding='utf-8'
    )
    temp_file.close()
    
    
    transformed_blob = bucket.blob(transformed_path)
    transformed_blob.upload_from_filename(temp_file.name)
    logging.info(f"Archivo transformado guardado en GCS: gs://{bucket_name}/{transformed_path}")
