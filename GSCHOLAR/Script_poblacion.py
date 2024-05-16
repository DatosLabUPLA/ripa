import os
import json
from google.cloud import bigquery

# Configura la ruta a las credenciales de Google Cloud

# Inicializa el cliente de BigQuery
client = bigquery.Client()

# Define el ID del proyecto y el dataset de BigQuery
project_id = 'ripa-1022'
dataset_id = 'universidad'
table_id = 'academico'

# Definir el esquema de la tabla en BigQuery
schema = [
    bigquery.SchemaField("container_type", "STRING"),
    bigquery.SchemaField("filled", "STRING", mode="REPEATED"),
    bigquery.SchemaField("scholar_id", "STRING"),
    bigquery.SchemaField("source", "STRING"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("url_picture", "STRING"),
    bigquery.SchemaField("affiliation", "STRING"),
    bigquery.SchemaField("organization", "INTEGER"),
    bigquery.SchemaField("interests", "STRING", mode="REPEATED"),
    bigquery.SchemaField("email_domain", "STRING"),
    bigquery.SchemaField("citedby", "INTEGER"),
    bigquery.SchemaField("citedby5y", "INTEGER"),
    bigquery.SchemaField("hindex", "INTEGER"),
    bigquery.SchemaField("hindex5y", "INTEGER"),
    bigquery.SchemaField("i10index", "INTEGER"),
    bigquery.SchemaField("i10index5y", "INTEGER"),
    bigquery.SchemaField("cites_per_year", "RECORD", mode="REPEATED", fields=[
        bigquery.SchemaField("year", "INTEGER"),
        bigquery.SchemaField("citations", "INTEGER"),
    ]),
    bigquery.SchemaField("coauthors", "RECORD", mode="REPEATED", fields=[
        bigquery.SchemaField("container_type", "STRING"),
        bigquery.SchemaField("filled", "STRING", mode="REPEATED"),
        bigquery.SchemaField("scholar_id", "STRING"),
        bigquery.SchemaField("source", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("affiliation", "STRING"),
    ]),
    bigquery.SchemaField("publications", "RECORD", mode="REPEATED", fields=[
        bigquery.SchemaField("container_type", "STRING"),
        bigquery.SchemaField("source", "STRING"),
        bigquery.SchemaField("bib", "RECORD", fields=[
            bigquery.SchemaField("title", "STRING"),
            bigquery.SchemaField("pub_year", "STRING"),
            bigquery.SchemaField("citation", "STRING"),
        ]),
        bigquery.SchemaField("filled", "BOOLEAN"),
        bigquery.SchemaField("author_pub_id", "STRING"),
        bigquery.SchemaField("num_citations", "INTEGER"),
        bigquery.SchemaField("citedby_url", "STRING"),
        bigquery.SchemaField("cites_id", "STRING", mode="REPEATED"),
    ]),
    bigquery.SchemaField("public_access", "RECORD", fields=[
        bigquery.SchemaField("available", "INTEGER"),
        bigquery.SchemaField("not_available", "INTEGER"),
    ]),
]

# Crea la tabla en BigQuery si no existe
table_ref = client.dataset(dataset_id).table(table_id)
try:
    table = client.get_table(table_ref)
    print(f"Tabla {table_id} ya existe.")
except Exception:
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table)
    print(f"Tabla {table_id} creada.")

# Ruta de la carpeta que contiene las subcarpetas con los archivos JSON
base_folder_path = 'DATOS_COMPLETOS'

# Itera sobre cada subcarpeta
for subfolder in os.listdir(base_folder_path):
    subfolder_path = os.path.join(base_folder_path, subfolder)
    
    if os.path.isdir(subfolder_path):
        # Itera sobre cada archivo JSON en la subcarpeta
        for json_file in os.listdir(subfolder_path):
            json_file_path = os.path.join(subfolder_path, json_file)
            
            # Carga el contenido del archivo JSON
            with open(json_file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                
                # Prepara los datos para la inserción
                rows_to_insert = [json_data]
                
                # Inserta los datos en la tabla de BigQuery
                errors = client.insert_rows_json(table, rows_to_insert)
                
                if errors:
                    print(f'Error al insertar el archivo {json_file}: {errors}')
                else:
                    print(f'Archivo {json_file} insertado correctamente en BigQuery')
