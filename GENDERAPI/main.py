import json
import requests
import csv
from google.cloud import bigquery
from google.oauth2 import service_account
from google.api_core.exceptions import NotFound
from datetime import datetime


def get_gender(name: str) -> dict:
    url = "https://gender-api.com/v2/gender/by-full-name"
    token = "e6735cad3911e4eededb09767bf47d28a252820d8b7b7489b9307b039202cffd"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "country": "CL",
        "locale": None,
        "ip": None,
        "full_name": name,
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error {response.status_code}")

def format_data(gender_data: dict, author_data: dict) -> dict:
    try:
        to_format = {
            'id_autor_gs': author_data['id_autor_gs'],
            'gender': gender_data['gender'],
            'probability': gender_data['probability'],
            'full_name': gender_data['input']['full_name'],
            'first_name': gender_data['first_name'],
            'last_name': gender_data['last_name'],
            'samples': gender_data['details']['samples'],
            'result_found': gender_data['result_found'],
            'country': gender_data['input']['country'],
        }
    except KeyError as e:
        print(f"KeyError: {e}")  # Mostrar el error para entender qué campo falta
        to_format = {
            'id_autor_gs': author_data['id_autor_gs'],
            'full_name': gender_data['input']['full_name'],
            'country': gender_data['input']['country'],
            'result_found': gender_data['result_found'],
            'first_name': None,
            'last_name': None,
            'probability': None,
            'gender': None,
            'samples': None,
        }
    return to_format

def get_authors() -> dict:
    # url_ripa = "https://ripa.datoslab.cl/gs/authors/"
    # response_ripa = requests.get(url_ripa)

    # leer desde json local
    with open("genero_input.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        return data

    if response_ripa.status_code == 200:
        data = response_ripa.json()
        return data
    else:
        print(f"Error {response_ripa.status_code}")
        return {}

def connect_to_bigquery():
    key_path = './ripa-1022-3be68cb6392e.json'
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

    return client

# inserta datos en bigquery en el nodo genero_gs que esta dentro del nodo gscholar que esta dentro del nodo ripa-1022, si no existe, crealo.
def insert_to_bigquery(data: dict):
    client = connect_to_bigquery()
    dataset_id = "ripa"
    table_id = "ripa_gs_genero"
    table_ref = client.dataset(dataset_id).table(table_id)

    # Check if the table exists and get it. If not, create it.
    try:
        table = client.get_table(table_ref)  # This verifies the table exists.
    except NotFound:
        # If the table does not exist, create it with the desired schema.
        schema = [
            bigquery.SchemaField("id_autor_gs", "STRING", mode="NULLABLE", ),
            bigquery.SchemaField("full_name", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("country", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("result_found", "BOOLEAN", mode="NULLABLE"),
            bigquery.SchemaField("first_name", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("last_name", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("probability", "FLOAT", mode="NULLABLE"),
            bigquery.SchemaField("gender", "STRING", mode="NULLABLE"),
            bigquery.SchemaField("samples", "INTEGER", mode="NULLABLE"),
        ]
        table = bigquery.Table(table_ref, schema=schema)
        table = client.create_table(table)  # Make an API request to create the table.

    # Insert rows into the table. Use `insert_rows_json` for better performance with large data sets.
    errors = client.insert_rows_json(table_ref, [data])  # Make an API request.

    if not errors:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

def save_to_file(data: dict):
    with open("genero.json", "a", encoding='utf-8') as file:
        # Escribe el diccionario como JSON, seguido de una coma y nueva línea si no es el último
        file.write(json.dumps(data, indent=4, ensure_ascii=False) + ",\n")

def finish_json_file():
    # Abrir el archivo en modo lectura y escritura binaria
    with open("genero.json", "rb+") as file:
        # Moverse al final del archivo
        file.seek(0, 2)  # Mover el indicador al final del archivo
        end_position = file.tell()  # Guardar la posición final del archivo
        # Retroceder desde el final hasta encontrar la última coma
        while file.tell() > 0:
            file.seek(-1, 1)  # Retroceder un byte
            if file.read(1) == b',':
                # Truncar el archivo justo antes de la última coma encontrada
                file.seek(-1, 1)  # Retroceder un byte nuevamente para estar justo antes de la coma
                file.truncate()
                break
            file.seek(-1, 1)  # Retroceder un byte nuevamente para continuar la búsqueda
        # Agregar el cierre de arreglo JSON
        file.write(b"\n]")

def save_to_csv(data: dict):
    with open("genero.csv", mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)

def init_files():
    # Simulación de datos de entrada basada en el ejemplo proporcionado
    author_data_example = {'id_autor_gs': 'BxT998AAAAAJ', 'autor': 'Zulay Giménez', 'id_institucion': 'uc', 'citaciones': 110}
    gender_data_example = {
        'input': {
            'full_name': 'Zulay Giménez',
            'country': 'CL'
        },
        'details': {
            'credits_used': 1,
            'duration': '42ms',
            'samples': 365,
            'country': None,
            'first_name_sanitized': 'zulay'
        },
        'result_found': True,
        'last_name': 'Giménez',
        'first_name': 'Zulay',
        'probability': 0.98,
        'gender': 'female'
    }

    formatted_data = format_data(gender_data_example, author_data_example)

    # Inicializar el archivo JSON
    with open("genero.json", "w", encoding='utf-8') as file:
        file.write("[\n")
    
    # Inicializar el archivo CSV con cabecera
    with open("genero.csv", mode='w', newline='', encoding='utf-8') as file:
        headers = formatted_data.keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

def save_to_log(data: str):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("log.txt", "a", encoding='utf-8') as file:
        file.write(f"{current_time}: {data}\n")

def main():
    # Guardar el tiempo de inicio
    save_to_log("Inicio del proceso")

    # Inicializar archivos
    init_files()

    authors = get_authors()
    save_to_log(f"Total de autores: {len(authors)}")
    print(f"Total de autores: {len(authors)}")

    save_to_log(f"Inicio iteración de autores")
    for author in authors:
        save_to_log(f"Procesado autor: {author['id_autor_gs']}")
        print(f"id_gs: {author['id_autor_gs']} - autor: {author['autor']}")
        gender_data = get_gender(author['autor'])
        formatted_data = format_data(gender_data, author)
        insert_to_bigquery(formatted_data)
        save_to_file(formatted_data)
        save_to_csv(formatted_data)
    save_to_log(f"Fin iteración de autores")

    # Finalizar correctamente el archivo JSON
    finish_json_file()
    
    # imprimir el tiempo de finalización
    save_to_log("Fin del proceso")

    autors = get_authors()

if __name__ == '__main__':
    main()
