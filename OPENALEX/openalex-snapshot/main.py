import os
import glob
import time
from multiprocessing import Pool, Manager
from google.cloud import bigquery
from google.oauth2 import service_account

def load_credentials(json_path):
    try:
        credentials = service_account.Credentials.from_service_account_file(json_path)
        return credentials
    except Exception as e:
        print(f"Error loading credentials: {e}")
        raise

def load_data(file_schema, timings, credentials):
    data_file, schema, table = file_schema
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)

    start_time = time.time()

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        field_delimiter='\t',
        schema=[
            bigquery.SchemaField("work", "STRING") if "works" in table else
            bigquery.SchemaField("author", "STRING") if "authors" in table else
            bigquery.SchemaField("source", "STRING") if "sources" in table else
            bigquery.SchemaField("institution", "STRING") if "institutions" in table else
            bigquery.SchemaField("concept", "STRING") if "concepts" in table else
            bigquery.SchemaField("publisher", "STRING")
        ]
    )

    with open(data_file, "rb") as source_file:
        load_job = client.load_table_from_file(source_file, table, job_config=job_config)

    load_job.result()  # Waits for the job to complete.

    end_time = time.time()
    duration = end_time - start_time
    timings[data_file] = duration

def get_files_and_schemas(base_dir, table_name, schema):
    files = glob.glob(os.path.join(base_dir, '**', '*.gz'), recursive=True)
    return [(file, schema, table_name) for file in files]

if __name__ == '__main__':
    start_time = time.time()
    manager = Manager()
    timings = manager.dict()

    # Cargar credenciales desde el archivo JSON
    json_path = "credentials.json"
    credentials = load_credentials(json_path)

    tasks = []
    tasks.extend(get_files_and_schemas('openalex-snapshot/data/works', 'openalex.works', 'work:string'))
    tasks.extend(get_files_and_schemas('openalex-snapshot/data/authors', 'openalex.authors', 'author:string'))
    tasks.extend(get_files_and_schemas('openalex-snapshot/data/sources', 'openalex.sources', 'source:string'))
    tasks.extend(get_files_and_schemas('openalex-snapshot/data/institutions', 'openalex.institutions', 'institution:string'))
    tasks.extend(get_files_and_schemas('openalex-snapshot/data/concepts', 'openalex.concepts', 'concept:string'))
    tasks.extend(get_files_and_schemas('openalex-snapshot/data/publishers', 'openalex.publishers', 'publisher:string'))

    with Pool(processes=os.cpu_count()) as pool:
        pool.starmap(load_data, [(task, timings, credentials) for task in tasks])

    end_time = time.time()
    total_duration = end_time - start_time

    for file, duration in timings.items():
        print(f"File {file} took {duration:.2f} seconds")

    print(f"Total execution time: {total_duration:.2f} seconds")
