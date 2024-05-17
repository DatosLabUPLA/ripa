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
    max_bad_records=10,  # Permitir hasta 10 errores
    ignore_unknown_values=True  # Ignorar valores desconocidos
)

# Obtener todos los blobs (archivos) del bucket
bucket = storage_client.bucket(bucket_name)
blobs = bucket.list_blobs()

def is_valid_json(json_text):
    try:
        json.loads(json_text)
        return True
    except json.JSONDecodeError as e:
        print(f'Error al validar JSON: {e}')
        return False

def transform_to_ndjson(json_text):
    try:
        data = json.loads(json_text)
        if isinstance(data, list):
            # Si el JSON es una lista, conviértelo a NDJSON
            ndjson = '\n'.join(json.dumps(record) for record in data)
        else:
            # Si el JSON es un solo objeto, no es necesario transformar
            ndjson = json.dumps(data)
        return ndjson
    except json.JSONDecodeError as e:
        print(f'Error al transformar JSON: {e}')
        return None

# Descargar, validar y cargar archivos desde GCS a BigQuery
for blob in blobs:
    json_text = blob.download_as_text()
    if is_valid_json(json_text):
        ndjson_text = transform_to_ndjson(json_text)
        if ndjson_text:
            temp_file_path = '/tmp/temp_ndjson.json'
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write(ndjson_text)
            
            # Subir el archivo transformado a un nuevo blob en GCS
            transformed_blob_name = f'transformed/{blob.name}'
            transformed_blob = bucket.blob(transformed_blob_name)
            transformed_blob.upload_from_filename(temp_file_path)

            gcs_uri = f'gs://{bucket_name}/{transformed_blob_name}'
            try:
                load_job = bigquery_client.load_table_from_uri(
                    gcs_uri,
                    table_ref,
                    job_config=job_config
                )
                load_job.result()  # Espera a que el job de carga se complete
                print(f'Archivo {gcs_uri} cargado correctamente en BigQuery')
            except Exception as e:
                print(f'Error al cargar el archivo {gcs_uri}: {e}')
        else:
            print(f'Error al transformar el archivo: gs://{bucket_name}/{blob.name}')
    else:
        print(f'Omitido el archivo inválido: gs://{bucket_name}/{blob.name}')
    break  # Solo cargar un archivo para probar el código