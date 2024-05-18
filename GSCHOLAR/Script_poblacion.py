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
project_id = 'your-project-id'
dataset_id = 'your-dataset-id'
bucket_name = 'your-bucket-name'

# Definición de las tablas y sus esquemas
tables_schemas = {
    'Info_Autores': [
        bigquery.SchemaField("scholar_id", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("affiliation", "STRING"),
        bigquery.SchemaField("hindex", "INTEGER"),
        bigquery.SchemaField("interests", "STRING", mode="REPEATED"),
    ],
    'Info_Publicaciones': [
        bigquery.SchemaField("scholar_id", "STRING"),
        bigquery.SchemaField("title", "STRING"),
        bigquery.SchemaField("pub_year", "STRING"),
        bigquery.SchemaField("citation", "STRING"),
        bigquery.SchemaField("num_citations", "INTEGER"),
    ],
    'Info_Coautores': [
        bigquery.SchemaField("scholar_id", "STRING"),
        bigquery.SchemaField("coauthor_id", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("affiliation", "STRING"),
    ],
}

# Crear tablas en BigQuery si no existen
for table_name, schema in tables_schemas.items():
    table_ref = bigquery_client.dataset(dataset_id).table(table_name)
    try:
        bigquery_client.get_table(table_ref)
        print(f"Tabla {table_name} ya existe.")
    except:
        table = bigquery.Table(table_ref, schema=schema)
        bigquery_client.create_table(table)
        print(f"Tabla {table_name} creada.")

# Obtener todos los blobs (archivos) del bucket
bucket = storage_client.bucket(bucket_name)
blobs = list(bucket.list_blobs())

def is_valid_json(json_text):
    try:
        json.loads(json_text)
        return True
    except json.JSONDecodeError as e:
        print(f'Error al validar JSON: {e}')
        return False

def transform_and_accumulate(blob, authors, publications, coauthors):
    json_text = blob.download_as_text()
    if not is_valid_json(json_text):
        print(f'Omitido el archivo inválido: gs://{bucket_name}/{blob.name}')
        return

    data = json.loads(json_text)
    
    # Agregar información del autor
    author_info = {
        "scholar_id": data["scholar_id"],
        "name": data["name"],
        "affiliation": data["affiliation"],
        "hindex": data["hindex"],
        "interests": data["interests"]
    }
    authors.append(author_info)
    
    # Agregar información de las publicaciones
    for pub in data.get("publications", []):
        publication_info = {
            "scholar_id": data["scholar_id"],
            "title": pub["bib"]["title"],
            "pub_year": pub["bib"].get("pub_year", None),
            "citation": pub["bib"].get("citation", None),
            "num_citations": pub.get("num_citations", None)
        }
        publications.append(publication_info)
    
    # Agregar información de los coautores
    for coauthor in data.get("coauthors", []):
        coauthor_info = {
            "scholar_id": data["scholar_id"],
            "coauthor_id": coauthor["scholar_id"],
            "name": coauthor["name"],
            "affiliation": coauthor["affiliation"]
        }
        coauthors.append(coauthor_info)

def load_data_to_bigquery(table_name, rows):
    table_ref = bigquery_client.dataset(dataset_id).table(table_name)
    errors = bigquery_client.insert_rows_json(table_ref, rows)
    if errors:
        print(f'Error al insertar en {table_name}: {errors}')
    else:
        print(f'{len(rows)} registros insertados en {table_name}')

# Procesar y cargar datos en lotes
batch_size = 100
authors = []
publications = []
coauthors = []

def process_blob(blob):
    global authors, publications, coauthors
    transform_and_accumulate(blob, authors, publications, coauthors)
    
    if len(authors) >= batch_size:
        load_data_to_bigquery('Info_Autores', authors)
        authors = []
    if len(publications) >= batch_size:
        load_data_to_bigquery('Info_Publicaciones', publications)
        publications = []
    if len(coauthors) >= batch_size:
        load_data_to_bigquery('Info_Coautores', coauthors)
        coauthors = []

# Usar procesamiento concurrente para manejar múltiples archivos simultáneamente
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process_blob, blobs)

# Cargar cualquier dato restante
if authors:
    load_data_to_bigquery('Info_Autores', authors)
if publications:
    load_data_to_bigquery('Info_Publicaciones', publications)
if coauthors:
    load_data_to_bigquery('Info_Coautores', coauthors)
