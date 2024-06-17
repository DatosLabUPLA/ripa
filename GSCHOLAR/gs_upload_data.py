import os
import csv
import json
import tempfile
from google.cloud import bigquery
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

# Configura la ruta a las credenciales de Google Cloud (solo si no estás usando Cloud Shell)
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-file.json"

# Inicializa los clientes de BigQuery y Storage
bigquery_client = bigquery.Client()

# Define el ID del proyecto y los datasets de BigQuery
project_id = 'ripa-1022'
dataset_id = 'ripa'

# Define las referencias a las tablas
table_refs = {
    "gs_authors": bigquery_client.dataset(dataset_id).table("gs_authors"),
    "gs_publications": bigquery_client.dataset(dataset_id).table("gs_publications"),
    "gs_coauthors": bigquery_client.dataset(dataset_id).table("gs_coauthors")
}

# Configura los esquemas de las tablas
schemas = {
    "gs_authors": [
        bigquery.SchemaField("container_type", "STRING"),
        bigquery.SchemaField("scholar_id", "STRING"),
        bigquery.SchemaField("source", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("url_picture", "STRING"),
        bigquery.SchemaField("affiliation", "STRING"),
        bigquery.SchemaField("organization", "STRING"),
        bigquery.SchemaField("email_domain", "STRING"),
        bigquery.SchemaField("citedby", "INTEGER"),
        bigquery.SchemaField("citedby5y", "INTEGER"),
        bigquery.SchemaField("hindex", "INTEGER"),
        bigquery.SchemaField("hindex5y", "INTEGER"),
        bigquery.SchemaField("i10index", "INTEGER"),
        bigquery.SchemaField("i10index5y", "INTEGER"),
    ],
    "gs_publications": [
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
    "gs_coauthors": [
        bigquery.SchemaField("scholar_id", "STRING"),
        bigquery.SchemaField("coauthor_scholar_id", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("affiliation", "STRING"),
    ]
}

# Configura los jobs de carga
load_job_configs = {
    "gs_authors": bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, schema=schemas["gs_authors"]),
    "gs_publications": bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, schema=schemas["gs_publications"]),
    "gs_coauthors": bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, schema=schemas["gs_coauthors"])
}

# Crear tablas si no existen
def create_table_if_not_exists(table_ref, schema):
    try:
        bigquery_client.get_table(table_ref)
        print(f"Table {table_ref.table_id} already exists.")
    except Exception:
        table = bigquery.Table(table_ref, schema=schema)
        bigquery_client.create_table(table)
        print(f"Created table {table_ref.table_id}.")

# Crear todas las tablas necesarias
for table_name, table_ref in table_refs.items():
    create_table_if_not_exists(table_ref, schemas[table_name])

# Obtener todos los blobs (archivos) del bucket
bucket = storage_client.bucket(bucket_name)
blobs = list(bucket.list_blobs())

# Validar si el texto es un JSON válido
def is_valid_json(json_text):
    try:
        json.loads(json_text)
        return True
    except json.JSONDecodeError as e:
        print(f'Error al validar JSON: {e}')
        return False

# Extraer información del JSON y convertirlo en los registros necesarios
def extract_info(data):
    gs_authors = []
    gs_publications = []
    gs_coauthors = []

    # Extraer información del autor
    autor = {
        "container_type": data.get("container_type"),
        "scholar_id": data.get("scholar_id"),
        "source": data.get("source"),
        "name": data.get("name"),
        "url_picture": data.get("url_picture"),
        "affiliation": data.get("affiliation"),
        "organization": str(data.get("organization")),
        "email_domain": data.get("email_domain"),
        "citedby": data.get("citedby"),
        "citedby5y": data.get("citedby5y"),
        "hindex": data.get("hindex"),
        "hindex5y": data.get("hindex5y"),
        "i10index": data.get("i10index"),
        "i10index5y": data.get("i10index5y")
    }
    gs_authors.append(autor)

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
        gs_publications.append(publicacion)

    # Extraer información de los coautores
    for coauthor in data.get("coauthors", []):
        coautor = {
            "scholar_id": data.get("scholar_id"),
            "coauthor_scholar_id": coauthor.get("scholar_id"),
            "name": coauthor.get("name"),
            "affiliation": coauthor.get("affiliation"),
        }
        gs_coauthors.append(coautor)
    
    return gs_authors, gs_publications, gs_coauthors

# Procesar cada blob y extraer la información
def process_blob(blob, existing_scholar_ids, existing_publication_ids, existing_coauthor_ids, lock):
    try:
        json_text = blob.download_as_text()
        if is_valid_json(json_text):
            data = json.loads(json_text)
            gs_authors, gs_publications, gs_coauthors = extract_info(data)

            # Filtrar información ya existente
            with lock:
                gs_authors = [autor for autor in gs_authors if autor["scholar_id"] not in existing_scholar_ids]
                gs_publications = [pub for pub in gs_publications if pub["author_pub_id"] not in existing_publication_ids]
                gs_coauthors = [coauthor for coauthor in gs_coauthors if coauthor["coauthor_scholar_id"] not in existing_coauthor_ids]

                # Actualizar los sets de IDs existentes para evitar duplicaciones en futuros hilos
                existing_scholar_ids.update(autor["scholar_id"] for autor in gs_authors)
                existing_publication_ids.update(pub["author_pub_id"] for pub in gs_publications)
                existing_coauthor_ids.update(coauthor["coauthor_scholar_id"] for coauthor in gs_coauthors)

            return gs_authors, gs_publications, gs_coauthors
        else:
            print(f'Omitido el archivo inválido: gs://{bucket_name}/{blob.name}')
            return [], [], []
    except Exception as e:
        print(f'Error al procesar el archivo gs://{bucket_name}/{blob.name}: {e}')
        return [], [], []

# Cargar datos a BigQuery en lotes
def load_data_to_bigquery(data, table_ref, job_config):
    if data:
        with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='') as temp_file:
            writer = csv.DictWriter(temp_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            temp_file_path = temp_file.name
        
        try:
            with open(temp_file_path, 'rb') as temp_file:
                load_job = bigquery_client.load_table_from_file(temp_file, table_ref, job_config=job_config)
                load_job.result()  # Espera a que el job de carga se complete
            print(f'Archivo {temp_file_path} cargado correctamente en BigQuery')
        except Exception as e:
            print(f'Error al cargar el archivo {temp_file_path}: {e}')
        finally:
            os.remove(temp_file_path)

# Obtener los IDs ya existentes en las tablas de BigQuery
def get_existing_ids(table_ref, id_column):
    query = f"SELECT {id_column} FROM `{project_id}.{dataset_id}.{table_ref.table_id}`"
    results = bigquery_client.query(query)
    return {row[id_column] for row in results}

# Descargar, validar y extraer información de los archivos JSON
all_gs_authors = []
all_gs_publications = []
all_gs_coauthors = []

# Obtener los IDs ya existentes
existing_scholar_ids = get_existing_ids(table_refs["gs_authors"], "scholar_id")
existing_publication_ids = get_existing_ids(table_refs["gs_publications"], "author_pub_id")
existing_coauthor_ids = get_existing_ids(table_refs["gs_coauthors"], "coauthor_scholar_id")

# Lock para sincronizar el acceso a los IDs existentes
lock = Lock()

# Procesar blobs en paralelo y extraer información
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(process_blob, blob, existing_scholar_ids, existing_publication_ids, existing_coauthor_ids, lock) for blob in blobs]
    for future in as_completed(futures):
        gs_authors, gs_publications, gs_coauthors = future.result()
        all_gs_authors.extend(gs_authors)
        all_gs_publications.extend(gs_publications)
        all_gs_coauthors.extend(gs_coauthors)

# Agrupar datos en lotes y cargar en BigQuery
def batch_and_load_data(data, table_ref, job_config):
    batch_size = 1000
    batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
    for batch in batches:
        load_data_to_bigquery(batch, table_ref, job_config)

# Cargar datos en las tablas de BigQuery en paralelo
with ThreadPoolExecutor(max_workers=3) as executor:
    future_to_table = {
        executor.submit(batch_and_load_data, all_gs_authors, table_refs["gs_authors"], load_job_configs["gs_authors"]): "gs_authors",
        executor.submit(batch_and_load_data, all_gs_publications, table_refs["gs_publications"], load_job_configs["gs_publications"]): "gs_publications",
        executor.submit(batch_and_load_data, all_gs_coauthors, table_refs["gs_coauthors"], load_job_configs["gs_coauthors"]): "gs_coauthors"
    }
    for future in as_completed(future_to_table):
        table_name = future_to_table[future]
        try:
            future.result()
            print(f'Datos cargados correctamente en la tabla {table_name}')
        except Exception as exc:
            print(f'Error al cargar datos en la tabla {table_name}: {exc}')
