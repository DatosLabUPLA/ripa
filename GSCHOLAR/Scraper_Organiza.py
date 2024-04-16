import csv
import json
import os  # Para operaciones de archivo y directorio
import time
from scholarly import scholarly, ProxyGenerator

def search_authors_by_organization(org_number, last_author_id=None):
    # Configuración del proxy para evitar bloqueos por solicitudes excesivas
    pg = ProxyGenerator()
    success = pg.ScraperAPI('42ac9e6e09c190fa8705c964e9d187cc')
    scholarly.use_proxy(pg)
    
    # Búsqueda de autores por número de organización
    authors = scholarly.search_author_by_organization(org_number)
    
    # Si se proporciona el ID del último autor registrado, comenzar desde ese punto
    if last_author_id:
        found_last_author = False
        new_authors = []
        for author in authors:
            if author['scholar_id'] == last_author_id:
                found_last_author = True
                continue  # Saltar el último autor registrado
            if found_last_author:
                new_authors.append(author)
        authors = new_authors
    
    return authors

def save_authors(authors, org_number):
    authors_list = []
    for index, author in enumerate(authors):
        author_start_time = time.time()
        
        # Rellenar detalles adicionales del autor
        scholarly.fill(author)

        # Agregar autor a la lista
        authors_list.append(author)
        # Extraer el dominio del correo electrónico para el nombre de archivo JSON
        dominio = author["email_domain"].split("@")[1].split(".")[-2]
        
        # Guardar el resultado en un archivo JSON separado para cada organización
        with open(f'{dominio}.json', 'w') as f:
            json.dump(authors_list, f, indent=4, default=lambda x: x.__dict__)
        
        # Mover el archivo JSON a la carpeta ARCHIVOS_COMPLETOS
        os.rename(f'{dominio}.json', f'ARCHIVOS_COMPLETOS/{dominio}.json')

        # Calcular tiempo que tomó guardar este autor
        author_time_taken = time.time() - author_start_time

        # Convertir segundos a horas/minutos/segundos
        m, s = divmod(author_time_taken, 60)
        h, m = divmod(m, 60)
        time_taken_str = "%d:%02d:%02d" % (h, m, s)

        # Registrar detalles en archivo de texto
        with open('registro_autores.txt', 'a', encoding='utf-8') as f:
            f.write(f'Institución: {org_number}, Autor: {author["name"]}, id: {author["scholar_id"]} Tiempo tomado: {time_taken_str}\n')

def main():
    # Leer números de organización y último autor registrado desde archivo CSV
    last_authors = {}
    try:
        with open('registro_autores.log', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                org_number = line.split(', Autor')[0].split('Institución: ')[1].strip()
                last_author_id = line.split('id: ')[1].split(' Tiempo')[0].strip()
                last_authors[org_number] = last_author_id
    except FileNotFoundError:
        pass  # Si el archivo no existe, continúa como si no hubiera registros

    # Leer instituciones desde archivo CSV
    institutions_to_extract = set()
    with open('instituciones.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            institutions_to_extract.add(row[0])

    # Comparar instituciones completadas con las faltantes
    completed_institutions = set()
    for filename in os.listdir('DATOS_COMPLETOS'):
        if filename.endswith('.json'):
            completed_institution = filename.split('.')[0]
            completed_institutions.add(completed_institution)
    institutions_to_process = institutions_to_extract - completed_institutions

    for org_number in institutions_to_process:
        print(f'Buscando autores para la organización con número: {org_number}')
        
        # Buscar autores por organización, comenzando desde el último autor registrado
        last_author_id = last_authors.get(org_number)
        authors = search_authors_by_organization(org_number, last_author_id)
        
        # Guardar autores en archivo JSON
        save_authors(authors, org_number)

if __name__ == "__main__":
    start_time = time.time()
    main()
    total_time_taken = time.time() - start_time
    print(f'Tiempo total tomado para buscar y guardar autores: {total_time_taken} segundos')
