from scholarly import scholarly
import time,json,csv,random

start_time = time.time()

urls = []
contador1 = 0
def autorID(id_autor):
    tiempo_espera = random.uniform(2,30)

    time.sleep(5)
    try:
        search_query = scholarly.search_author_id(id_autor)
        autor = scholarly.fill(search_query, sections=[])
        autores = []

        if not autor:
            print("Autor no esta: ",search_query)     

        for llave in autor:
            autores.append(autor[llave])
            
        with open('author2.json', 'a') as f:
            f.write(json.dumps(autor, indent=4, sort_keys=True))
            #f.write(",\n")  # Agregar coma después de cada objeto autor

    except Exception as e:
        print('Error', e)


with open("AUTORES_SCHOLARLY/CSV_AUTOR_PUCV.csv",encoding="utf8") as f:
    reader = csv.DictReader(f)
    
#authors = ['jxAEmjUAAAAJ','JIJW4BoAAAAJ']

    for row in reader:
        urls.append(row['Scholar_id'])

with open('author2.json', 'w') as f:  # Crear el archivo JSON inicialmente vacío
    f.write("[")

contador = 0

for i, ids in enumerate(urls):
    autorID(ids)
    contador +=1
    print("Vamos en el autor: ",contador)
    if i != len(urls) - 1:
        with open('author2.json', 'a') as f:
            f.write(",\n")  # Agregar coma después de cada objeto autor excepto el último
            contador1 +=1
            if contador1 == 5:
                break
with open('author2.json', 'a') as f:
    f.write("]")  # Agregar corchete de cierre al final del archivo JSON

end_time = time.time()

elapsed_time = end_time-start_time

print("Proceso de extraccion de datos finalizado. Tiempo transcurrido:",elapsed_time,"segundos.")