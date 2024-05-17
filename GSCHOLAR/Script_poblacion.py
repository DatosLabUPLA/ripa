import os
import json
from google.cloud import bigquery, storage

# Configura la ruta a las credenciales de Google Cloud (solo si no estás usando Cloud Shell)
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-file.json"

# Inicializa los clientes de BigQuery y Storage
bigquery_client = bigquery.Client()
storage_client = storage.Client()

# Define el ID del proyecto, el dataset, la tabla y el nombre del bucket
project_id = 'ripa-1022'
dataset_id = 'universidad'
table_id = 'academicos'
bucket_name = 'scholarly_data'

# Ruta de la carpeta que contiene las subcarpetas con los archivos JSON
base_folder_path = 'DATOS_COMPLETOS'

# Crear el bucket en GCS si no existe
bucket = storage_client.bucket(bucket_name)
if not bucket.exists():
    bucket = storage_client.create_bucket(bucket_name)
    print(f'Bucket {bucket_name} creado.')
else:
    print(f'Bucket {bucket_name} ya existe.')

# Subir archivos JSON a GCS
for subfolder in os.listdir(base_folder_path):
    subfolder_path = os.path.join(base_folder_path, subfolder)
    
    if os.path.isdir(subfolder_path):
        for json_file in os.listdir(subfolder_path):
            json_file_path = os.path.join(subfolder_path, json_file)
            blob_name = f'{subfolder}/{json_file}'

            # Subir archivo a GCS
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(json_file_path)
            print(f'Archivo {json_file_path} subido a gs://{bucket_name}/{blob_name}')

# Define la referencia a la tabla
table_ref = bigquery_client.dataset(dataset_id).table(table_id)

# Configura el job de carga
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    schema=[
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
    ],
)

# Cargar archivos desde GCS a BigQuery
for subfolder in os.listdir(base_folder_path):
    subfolder_path = os.path.join(base_folder_path, subfolder)
    
    if os.path.isdir(subfolder_path):
        for json_file in os.listdir(subfolder_path):
            blob_name = f'{subfolder}/{json_file}'
            gcs_uri = f'gs://{bucket_name}/{blob_name}'
            
            load_job = bigquery_client.load_table_from_uri(
                gcs_uri,
                table_ref,
                job_config=job_config
            )
            load_job.result()  # Espera a que el job de carga se complete
            print(f'Archivo {gcs_uri} cargado correctamente en BigQuery')
