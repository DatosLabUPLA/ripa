import csv
import re

def obtener_numero_org(enlace):
    match = re.search(r'org=(\d+)', enlace)
    if match:
        return match.group(1)
    else:
        return None

archivo_csv = 'instituciones.csv'
archivo_organizaciones = 'organizaciones.csv'

with open(archivo_csv, 'r') as csvfile, open(archivo_organizaciones, 'w', newline='') as orgfile:
    lector_csv = csv.DictReader(csvfile)
    escritor_csv = csv.writer(orgfile)
    escritor_csv.writerow(['Numero de org'])
    for fila in lector_csv:
        enlace = fila['enlace']
        numero_org = obtener_numero_org(enlace)
        if numero_org:
            print("Número de org para", enlace, ":", numero_org)
            escritor_csv.writerow([numero_org])
        else:
            print("No se pudo encontrar el número de org para", enlace)
