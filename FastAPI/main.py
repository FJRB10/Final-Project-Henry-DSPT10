from fastapi import FastAPI
from google.cloud import bigquery
import requests
import os
from datetime import datetime

app = FastAPI()

# Configuración de Google Cloud
PROJECT_ID = 'utopian-honor-438417-u7'
API_KEY = 'AIzaSyDDt1fiH2cTopWMX_qfg50nm0taKg4egV4'
PLACE_IDS = [
    'ChIJOwg_06VPwokRYv534QaPC8g', 'ChIJ7cv00DwsDogRAMDACa2m4K8',
    'ChIJE9on3F3HwoAR9AhGJW_fL-I', 'ChIJ60u11Ni3xokRwVg-jNgU9Yk',
    'ChIJrw7QBK9YXIYRvBagEDvhVgg', 'ChIJS5dFe_cZTIYRj2dH9qSb7Lk',
    'ChIJ0X31pIK3voARo3mz1ebVzDo', 'ChIJEcHIDqKw2YgRZU-t3XHylv8'
]

# Inicializa el cliente de BigQuery
bigquery_client = bigquery.Client()

@app.get("/fetch-places-data")
def fetch_places_data():
    results = []
    for place_id in PLACE_IDS:
        response = requests.get(
            f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={API_KEY}"
        )
        if response.status_code == 200:
            place_data = response.json().get("result", {})
            results.append(place_data)
            save_to_bigquery(place_data)
        else:
            return {"error": f"Failed to fetch data for place_id: {place_id}"}

    return {"status": "Data fetched and uploaded to BigQuery", "data": results}

def save_to_bigquery(data):
    table_id = f"{PROJECT_ID}.dataset_name.table_name"  # Cambia a tu dataset y tabla
    rows_to_insert = [data]
    errors = bigquery_client.insert_rows_json(table_id, rows_to_insert)
    if errors:
        print(f"Error inserting rows: {errors}")
    else:
        print("Data inserted successfully")
