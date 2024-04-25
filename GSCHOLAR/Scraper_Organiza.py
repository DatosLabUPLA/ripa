import csv  # Importación del módulo csv para trabajar con archivos CSV
import json  # Importación del módulo json para trabajar con archivos JSON
import os  # Importación del módulo os para operaciones de archivo y directorio
import time  # Importación del módulo time para medir el tiempo
from scholarly import scholarly, ProxyGenerator  # Importación de clases y funciones específicas de los módulos scholarly y ProxyGenerator

def search_authors_by_organization(org_number, last_author_id=None):
    # Configuración del proxy para evitar bloqueos por solicitudes excesivas
    pg = ProxyGenerator()  # Instanciación de ProxyGenerator
    success = pg.ScraperAPI('42ac9e6e09c190fa8705c964e9d187cc')  # Asignación de clave de API para el proxy
    scholarly.use_proxy(pg)  # Uso del proxy configurado con la biblioteca scholarly
    
    # Búsqueda de autores por número de organización
    authors = scholarly.search_author_by_organization(org_number)  # Búsqueda de autores utilizando la biblioteca scholarly
    
    # Si se proporciona el ID del último autor registrado, comenzar desde ese punto
    if last_author_id:
        found_last_author = False  # Bandera para indicar si se encontró el último autor registrado
        new_authors = []  # Lista para almacenar los nuevos autores
        for author in authors:
            if author['scholar_id'] == last_author_id:
                found_last_author = True  # Se encontró el último autor registrado
                continue  # Saltar el último autor registrado y continuar con la iteración
            if found_last_author:
                new_authors.append(author)  # Agregar autores después del último autor registrado a la lista de nuevos autores
        authors = new_authors  # Reemplazar la lista de autores con la lista de nuevos autores
    
    return authors  # Devolver la lista de autores

def save_authors(authors, institution_name,dominio):
    # Reemplazar caracteres no deseados en el nombre de la institución para el nombre de la carpeta
    institution_folder = f'DATOS_COMPLETOS/{dominio.replace(" ", "_")}'
    
    # Verificar si la carpeta de la institución existe, si no, crearla
    if not os.path.exists(institution_folder):
        os.makedirs(institution_folder)
    
    for author in authors:  # Iterar sobre la lista de autores
        author_start_time = time.time()  # Registrar el tiempo de inicio para guardar este autor
        
        # Rellenar detalles adicionales del autor utilizando la biblioteca scholarly
        scholarly.fill(author)
        
        # Obtener el identificador del autor
        dominio2 = author["scholar_id"]
        
        # Guardar el resultado en un archivo JSON separado para cada autor
        with open(f'{institution_folder}/{dominio2}.json', 'w') as f:
            json.dump(author, f, indent=4, default=lambda x: x.__dict__)  # Escribir los detalles del autor en un archivo JSON
        
        # Calcular el tiempo que tomó guardar este autor
        author_time_taken = time.time() - author_start_time
        
        # Convertir el tiempo de guardado del autor de segundos a horas/minutos/segundos
        m, s = divmod(author_time_taken, 60)
        h, m = divmod(m, 60)
        time_taken_str = "%d:%02d:%02d" % (h, m, s)
        
        # Registrar detalles en archivo de texto
        with open('registro_autores.txt', 'a', encoding='utf-8') as f:
            f.write(f'Institución: {institution_name}, Autor: {author["name"]}, id: {author["scholar_id"]} Tiempo tomado: {time_taken_str}\n')  # Registrar detalles del autor en el archivo de registro

def main():
    # Leer números de organización y último autor registrado desde archivo CSV
    last_authors = {}  # Diccionario para almacenar los últimos autores registrados
    try:
        with open('registro_autores.txt', 'r', encoding='utf-8') as f:  # Abrir el archivo de registro de autores en modo lectura
            lines = f.readlines()  # Leer todas las líneas del archivo
            for line in lines:  # Iterar sobre cada línea en el archivo
                org_number = line.split(', Autor')[0].split('Institución: ')[1].strip()  # Obtener el número de institución de la línea
                last_author_id = line.split('id: ')[1].split(' Tiempo')[0].strip()  # Obtener el ID del último autor registrado de la línea
                last_authors[org_number] = last_author_id  # Agregar el número de institución y el ID del último autor al diccionario
    except FileNotFoundError:
        pass  # Si el archivo no existe, continuar sin hacer nada
    
    # Leer instituciones desde archivo CSV
    institutions_to_extract = set()  # Conjunto para almacenar las instituciones a extraer
    with open('organizaciones.csv', newline='') as csvfile:  # Abrir el archivo de instituciones en modo lectura
        reader = csv.reader(csvfile)  # Crear un lector CSV
        for row in reader:  # Iterar sobre cada fila en el archivo CSV
            institutions_to_extract.add(row[0])  # Agregar la institución al conjunto
    
    # Comparar instituciones completadas con las faltantes
    completed_institutions = set()  # Conjunto para almacenar las instituciones completadas
    for filename in os.listdir('DATOS_COMPLETOS'):  # Iterar sobre los archivos en el directorio DATOS_COMPLETOS
        if filename.endswith('.json'):  # Verificar si el archivo es un archivo JSON
            completed_institution = filename.split('.')[0]  # Obtener el nombre de la institución del archivo
            completed_institutions.add(completed_institution)  # Agregar la institución al conjunto de instituciones completadas
    institutions_to_process = institutions_to_extract - completed_institutions  # Obtener las instituciones que aún no han sido procesadas
    #print(f'instituciones a procesar: {institutions_to_process}')
    for institution_name in institutions_to_process:  # Iterar sobre las instituciones a procesar
        print(f'Buscando autores para la institución: {institution_name}')  # Imprimir mensaje indicando la búsqueda de autores para la institución
        
        # Buscar autores por institución, comenzando desde el último autor registrado
        last_author_id = last_authors.get(institution_name)  # Obtener el ID del último autor registrado para esta institución
        authors = search_authors_by_organization(institution_name, last_author_id)  # Buscar autores para la institución
        for author in authors:
            dominio = author['email_domain'].split('@')[1].split('.')[-2]
            break
        save_authors(authors, institution_name,dominio)  # Guardar los autores en archivos JSON separados
        if dominio is not None:
            print(dominio)
        else :
            print("No se encontro dominio")
        # Guardar autores en archivos JSON separados
          # Guardar los autores en archivos JSON
main()  # Llamar a la función principal para iniciar el proceso de extracción de autores
