import os
import json
import concurrent.futures
from google.cloud import bigquery, storage

# Configura la ruta a las credenciales de Google Cloud (solo si no estás usando Cloud Shell)
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-file.json"

# Inicializa los clientes de BigQuery y Storage
bigquery_client = bigquery.Client()
storage_client = storage.Client()

# Define el ID del proyecto, el dataset y el nombre del bucket
project_id = 'ripa-1022'
dataset_id = 'universidad'
bucket_name = 'scholarly_data'

# Define las referencias a las tablas
table_refs = {
    "Info_Autores": bigquery_client.dataset(dataset_id).table("Info_Autores"),
    "Info_Publicaciones": bigquery_client.dataset(dataset_id).table("Info_Publicaciones"),
    "Info_Coautores": bigquery_client.dataset(dataset_id).table("Info_Coautores")
}

# Configura los esquemas de las tablas
schemas = {
    "Info_Autores": [
        bigquery.SchemaField("container_type", "STRING"),
        bigquery.SchemaField("scholar_id", "STRING"),
        bigquery.SchemaField("source", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("url_picture", "STRING"),
        bigquery.SchemaField("affiliation", "STRING"),
        bigquery.SchemaField("organization", "INTEGER"),
        bigquery.SchemaField("email_domain", "STRING"),
        bigquery.SchemaField("citedby", "INTEGER"),
        bigquery.SchemaField("citedby5y", "INTEGER"),
        bigquery.SchemaField("hindex", "INTEGER"),
        bigquery.SchemaField("hindex5y", "INTEGER"),
        bigquery.SchemaField("i10index", "INTEGER"),
        bigquery.SchemaField("i10index5y", "INTEGER"),
    ],
    "Info_Publicaciones": [
        bigquery.SchemaField("scholar_id", "STRING"),
        bigquery.SchemaField("container_type", "STRING"),
        bigquery.SchemaField("source", "STRING"),
        bigquery.SchemaField("title", "STRING"),
        bigquery.SchemaField("pub_year", "STRING"),
        bigquery.SchemaField("citation", "STRING"),
        bigquery.SchemaField("author_pub_id", "STRING"),
        bigquery.SchemaField("num_citations", "INTEGER"),
        bigquery.SchemaField("citedby_url", "STRING"),
    ],
    "Info_Coautores": [
        bigquery.SchemaField("scholar_id", "STRING"),
        bigquery.SchemaField("coauthor_scholar_id", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("affiliation", "STRING"),
    ]
}

# Configura los jobs de carga
load_job_configs = {
    "Info_Autores": bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON, schema=schemas["Info_Autores"]),
    "Info_Publicaciones": bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON, schema=schemas["Info_Publicaciones"]),
    "Info_Coautores": bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON, schema=schemas["Info_Coautores"])
}

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

def extract_info(data):
    info_autores = []
    info_publicaciones = []
    info_coautores = []

    for item in data:
        # Extraer información del autor
        autor = {
            "container_type": item.get("container_type"),
            "scholar_id": item.get("scholar_id"),
            "source": item.get("source"),
            "name": item.get("name"),
            "url_picture": item.get("url_picture"),
            "affiliation": item.get("affiliation"),
            "organization": item.get("organization"),
            "email_domain": item.get("email_domain"),
            "citedby": item.get("citedby"),
            "citedby5y": item.get("citedby5y"),
            "hindex": item.get("hindex"),
            "hindex5y": item.get("hindex5y"),
            "i10index": item.get("i10index"),
            "i10index5y": item.get("i10index5y")
        }
        info_autores.append(autor)

        # Extraer información de las publicaciones
        for pub in item.get("publications", []):
            publicacion = {
                "scholar_id": item.get("scholar_id"),
                "container_type": pub.get("container_type"),
                "source": pub.get("source"),
                "title": pub.get("bib", {}).get("title"),
                "pub_year": pub.get("bib", {}).get("pub_year"),
                "citation": pub.get("bib", {}).get("citation"),
                "author_pub_id": pub.get("author_pub_id"),
                "num_citations": pub.get("num_citations"),
                "citedby_url": pub.get("citedby_url"),
            }
            info_publicaciones.append(publicacion)

        # Extraer información de los coautores
        for coauthor in item.get("coauthors", []):
            coautor = {
                "scholar_id": item.get("scholar_id"),
                "coauthor_scholar_id": coauthor.get("scholar_id"),
                "name": coauthor.get("name"),
                "affiliation": coauthor.get("affiliation"),
            }
            info_coautores.append(coautor)
    
    return info_autores, info_publicaciones, info_coautores

# Descargar, validar y extraer información de los archivos JSON
all_info_autores = []
all_info_publicaciones = []
all_info_coautores = []

batch_size = 1000  # Tamaño del lote para cargar los datos

for blob in blobs:
    json_text = blob.download_as_text()
    if is_valid_json(json_text):
        data = json.loads(json_text)
        if isinstance(data, list):
            info_autores, info_publicaciones, info_coautores = extract_info(data)
            all_info_autores.extend(info_autores)
            all_info_publicaciones.extend(info_publicaciones)
            all_info_coautores.extend(info_coautores)
        else:
            print(f'Formato inesperado en archivo: gs://{bucket_name}/{blob.name}')
    else:
        print(f'Omitido el archivo inválido: gs://{bucket_name}/{blob.name}')

def load_data_to_bigquery(data, table_ref, job_config):
    if data:
        batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
        for batch in batches:
            json_data = '\n'.join(json.dumps(record) for record in batch)
            temp_file_path = '/tmp/temp_ndjson.json'
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write(json_data)
            
            transformed_blob_name = f'transformed/{table_ref.table_id}.json'
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

# Función para paralelizar la carga de datos
def parallel_load_data(table_name, data):
    load_data_to_bigquery(data, table_refs[table_name], load_job_configs[table_name])

# Cargar datos en las tablas de BigQuery en paralelo
with ThreadPoolExecutor(max_workers=3) as executor:
    future_to_table = {
        executor.submit(parallel_load_data, "Info_Autores", all_info_autores): "Info_Autores",
        executor.submit(parallel_load_data, "Info_Publicaciones", all_info_publicaciones): "Info_Publicaciones",
        executor.submit(parallel_load_data, "Info_Coautores", all_info_coautores): "Info_Coautores"
    }
    for future in as_completed(future_to_table):
        table_name = future_to_table[future]
        try:
            future.result()
            print(f'Datos cargados correctamente en la tabla {table_name}')
        except Exception as exc:
            print(f'Error al cargar datos en la tabla {table_name}: {exc}')