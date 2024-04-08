import csv
import json
import time
from scholarly import scholarly, ProxyGenerator

def search_authors_by_organization(org_number, last_author_id=None):
    pg = ProxyGenerator()
    success = pg.ScraperAPI('42ac9e6e09c190fa8705c964e9d187cc')
    scholarly.use_proxy(pg)
    authors = scholarly.search_author_by_organization(org_number)
    
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
        # Relleno de autor
        scholarly.fill(author)

        # Agregar autor a la lista
        authors_list.append(author)
        dominio = author["email_domain"].split("@")[1].split(".")[0]
        # Guardar el resultado en un archivo JSON separado para cada organización
        with open(f'{dominio}.json', 'w') as f:
            json.dump(authors_list, f, indent=4, default=lambda x: x.__dict__)

        # Calcular tiempo que tomó guardar este autor
        author_time_taken = time.time() - author_start_time

        # Registrar detalles en archivo de texto
        with open('registro_autores.txt', 'a', encoding='utf-8') as f:
            f.write(f'Institución: {org_number}, Autor: {author["name"]}, id: {author["scholar_id"]} Tiempo tomado: {author_time_taken} segundos\n')

def main():
    # Leer números de organización y último autor registrado desde archivo CSV
    last_authors = {}
    try:
        with open('registro_autores.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                org_number = line.split(', Autor')[0].split('Institución: ')[1].strip()
                last_author_id = line.split('id: ')[1].split(' Tiempo')[0].strip()
                last_authors[org_number] = last_author_id
    except FileNotFoundError:
        pass  # Si el archivo no existe, continúa como si no hubiera registros

    with open('organizaciones.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Ignorar encabezados si los hay
        for row in reader:
            org_number = row[0]
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
