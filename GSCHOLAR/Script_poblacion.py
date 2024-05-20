import os
import json
from google.cloud import bigquery, storage
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configura la ruta a las credenciales de Google Cloud (solo si no estás usando Cloud Shell)
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-file.json"

# Inicializa los clientes de BigQuery y Storage
bigquery_client = bigquery.Client()
storage_client = storage.Client()

# Define el ID del proyecto y los datasets de BigQuery
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

    # Extraer información del autor
    autor = {
        "container_type": data.get("container_type"),
        "scholar_id": data.get("scholar_id"),
        "source": data.get("source"),
        "name": data.get("name"),
        "url_picture": data.get("url_picture"),
        "affiliation": data.get("affiliation"),
        "organization": data.get("organization"),
        "email_domain": data.get("email_domain"),
        "citedby": data.get("citedby"),
        "citedby5y": data.get("citedby5y"),
        "hindex": data.get("hindex"),
        "hindex5y": data.get("hindex5y"),
        "i10index": data.get("i10index"),
        "i10index5y": data.get("i10index5y")
    }
    info_autores.append(autor)

    # Extraer información de las publicaciones
    for pub in data.get("publications", []):
        publicacion = {
            "scholar_id": data.get("scholar_id"),
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
    for coauthor in data.get("coauthors", []):
        coautor = {
            "scholar_id": data.get("scholar_id"),
            "coauthor_scholar_id": coauthor.get("scholar_id"),
            "name": coauthor.get("name"),
            "affiliation": coauthor.get("affiliation"),
        }
        info_coautores.append(coautor)
    
    return info_autores, info_publicaciones, info_coautores

def process_blob(blob):
    try:
        json_text = blob.download_as_text()
        if is_valid_json(json_text):
            data = json.loads(json_text)
            return extract_info(data)
        else:
            print(f'Omitido el archivo inválido: gs://{bucket_name}/{blob.name}')
            return [], [], []
    except Exception as e:
        print(f'Error al procesar el archivo gs://{bucket_name}/{blob.name}: {e}')
        return [], [], []

def load_data_to_bigquery(data, table_ref, job_config):
    if data:
        json_data = '\n'.join(json.dumps(record) for record in data)
        temp_file_path = f'/tmp/{table_ref.table_id}.json'
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

# Obtener los IDs ya existentes en las tablas de BigQuery
def get_existing_ids(table_ref, id_column):
    query = f"SELECT {id_column} FROM `{project_id}.{dataset_id}.{table_ref.table_id}`"
    results = bigquery_client.query(query)
    return {row[id_column] for row in results}

# Descargar, validar y extraer información de los archivos JSON
all_info_autores = []
all_info_publicaciones = []
all_info_coautores = []

# Obtener los IDs ya existentes
existing_scholar_ids = get_existing_ids(table_refs["Info_Autores"], "scholar_id")
existing_publication_ids = get_existing_ids(table_refs["Info_Publicaciones"], "author_pub_id")
existing_coauthor_ids = get_existing_ids(table_refs["Info_Coautores"], "coauthor_scholar_id")

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(process_blob, blob) for blob in blobs]
    for future in as_completed(futures):
        info_autores, info_publicaciones, info_coautores = future.result()
        # Filtrar información ya existente
        info_autores = [autor for autor in info_autores if autor["scholar_id"] not in existing_scholar_ids]
        info_publicaciones = [pub for pub in info_publicaciones if pub["author_pub_id"] not in existing_publication_ids]
        info_coautores = [coauthor for coauthor in info_coautores if coauthor["coauthor_scholar_id"] not in existing_coauthor_ids]

        all_info_autores.extend(info_autores)
        all_info_publicaciones.extend(info_publicaciones)
        all_info_coautores.extend(info_coautores)

# Agrupar datos en lotes y cargar en BigQuery
def batch_and_load_data(data, table_ref, job_config):
    batch_size = 1000
    batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
    for batch in batches:
        load_data_to_bigquery(batch, table_ref, job_config)

# Cargar datos en las tablas de BigQuery en paralelo
with ThreadPoolExecutor(max_workers=3) as executor:
    future_to_table = {
        executor.submit(batch_and_load_data, all_info_autores, table_refs["Info_Autores"], load_job_configs["Info_Autores"]): "Info_Autores",
        executor.submit(batch_and_load_data, all_info_publicaciones, table_refs["Info_Publicaciones"], load_job_configs["Info_Publicaciones"]): "Info_Publicaciones",
        executor.submit(batch_and_load_data, all_info_coautores, table_refs["Info_Coautores"], load_job_configs["Info_Coautores"]): "Info_Coautores"
    }
    for future in as_completed(future_to_table):
        table_name = future_to_table[future]
        try:
            future.result()
            print(f'Datos cargados correctamente en la tabla {table_name}')
        except Exception as exc:
            print(f'Error al cargar datos en la tabla {table_name}: {exc}')