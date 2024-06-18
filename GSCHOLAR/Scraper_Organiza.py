import csv  # Importación del módulo csv para trabajar con archivos CSV
import json  # Importación del módulo json para trabajar con archivos JSON
import os  # Importación del módulo os para operaciones de archivo y directorio
import time  # Importación del módulo time para medir el tiempo
from datetime import datetime
from scholarly import scholarly, ProxyGenerator  # Importación de clases y funciones específicas de los módulos scholarly y ProxyGenerator

def get_instituciones():
    institutions_to_extract = set()  # Conjunto para almacenar las instituciones a extraer
    with open('organizaciones.csv', newline='') as csvfile:  # Abrir el archivo de instituciones en modo lectura
        reader = csv.reader(csvfile)  # Crear un lector CSV
        for row in reader:  # Iterar sobre cada fila en el archivo CSV
            institutions_to_extract.add(row[0])
    return institutions_to_extract

def get_instituciones_completas():
    completed_institutions = set()
    with open('organizaciones_completas.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            completed_institutions.add(row[0])
    return completed_institutions

def get_autores_completados(dominio):
    autores = set()
    institution_folder = os.path.join('DATOS_COMPLETOS', dominio)
    if not os.path.exists(institution_folder):
        os.makedirs(institution_folder)
    for filename in os.listdir(institution_folder):
    
    
        if filename.endswith('.json'):
            autor = filename.split('.')[0]
            autores.add(autor)
    return autores

def get_autores(org_number):
    pg = ProxyGenerator()
    success = pg.ScraperAPI('a04593990d15c798a5477e1f7804a66b') #cambiar por una cuenta con creditos
    scholarly.use_proxy(pg)
    authors_id = set()
    authors = scholarly.search_author_by_organization(org_number)
    authors_id = {author['scholar_id'] for author in authors}
    return authors_id

def add_inst_completas(org_number):
    with open('organizaciones_completas.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([org_number])
        
def get_domino(org_number):
    author = scholarly.search_author_id(org_number)
    dominio = author['email_domain'].split('@')[1].split('.')[-2]
    return dominio
 # Devolver la lista de autores

def save_authors(authors, institution_name,dominio):
    # Reemplazar caracteres no deseados en el nombre de la institución para el nombre de la carpeta
    institution_folder = os.path.join('DATOS_COMPLETOS', dominio.replace(" ", "_"))
    
    # Verificar si la carpeta de la institución existe, si no, crearla
    if not os.path.exists(institution_folder):
        os.makedirs(institution_folder)
    
    for author in authors:  # Iterar sobre la lista de autores
        author_start_time = time.time()  # Registrar el tiempo de inicio para guardar este autor
        
        # Rellenar detalles adicionales del autor utilizando la biblioteca scholarly
        author_info=scholarly.search_author_id(author, filled=True)
        
        # Obtener el identificador del autor
        id_gs = author_info["scholar_id"] # ID google Schorar 
        json_file = f'{id_gs}.json'
        archivo = os.path.join(institution_folder, json_file)
        # Guardar el resultado en un archivo JSON separado para cada autor
        with open(archivo, 'w') as f:
            json.dump(author_info, f, indent=4, default=lambda x: x.__dict__)  # Escribir los detalles del autor en un archivo JSON
        
        # Calcular el tiempo que tomó guardar este autor
        author_time_taken = time.time() - author_start_time
        
        # Convertir el tiempo de guardado del autor de segundos a horas/minutos/segundos
        m, s = divmod(author_time_taken, 60)
        h, m = divmod(m, 60)
        time_taken_str = "%d:%02d:%02d" % (h, m, s)
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Registrar detalles en archivo de texto
        with open('registro_autores.txt', 'a', encoding='utf-8') as f:
            
            f.write(f'Institución: {institution_name}, Autor: {author_info["name"]}, id: {author_info["scholar_id"]} Tiempo tomado: {time_taken_str}, fecha de extraccion: {current_date}\n')  # Registrar detalles del autor en el archivo de registro

def main():
    institutions_to_extract = get_instituciones()  # Obtener las instituciones a extraer
    completed_institutions = get_instituciones_completas()  # Agregar la institución al conjunto de instituciones completadas
    institutions_to_process = institutions_to_extract - completed_institutions  # Obtener las instituciones que aún no han sido procesadas
    #print(f'instituciones a procesar: {institutions_to_process}')
    for institution_name in institutions_to_process:
        try:  # Iterar sobre las instituciones a procesar
            print(f'Buscando autores para la institución: {institution_name}')  # Imprimir mensaje indicando la búsqueda de autores para la institución
            A0= get_autores(institution_name)
            dominio = get_domino(list(A0)[0])
            A1 = get_autores_completados(dominio)
            authors = A0 - A1
            if len(authors) == 0:
                add_inst_completas(institution_name)
                print(f'Institución completada: {institution_name}')
                continue
            
            save_authors(authors, institution_name,dominio)  # Guardar los autores en archivos JSON separados
            if dominio is not None:
                print(dominio)
            else :
                print("No se encontro dominio")
        except Exception as e:
            print(f'Error al extraer autores de la institución: {e}')
            # Guardar autores en archivos JSON separados
            # Guardar los autores en archivos JSON
main()
