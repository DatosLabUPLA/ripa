
# Proyecto de Scraping y Análisis de Datos Académicos

Este proyecto contiene dos scripts en Python para realizar scraping de datos académicos y procesar información poblacional. A continuación se explica el funcionamiento de cada uno de estos scripts.

## Scraper_Organiza.py

Este script extrae y procesa información sobre instituciones académicas y autores asociados utilizando la biblioteca scholarly para interactuar con Google Scholar.

### Dependencias

- `csv`
- `json`
- `os`
- `time`
- `datetime`
- `scholarly`
- `ProxyGenerator`

### Funcionalidades Principales

#### Extracción de Instituciones

- `get_instituciones()`: Lee un archivo CSV para obtener una lista de instituciones a extraer.
- `get_instituciones_completas()`: Lee un archivo CSV para obtener una lista de instituciones ya procesadas.

#### Manejo de Autores

- `get_autores_completados(dominio)`: Obtiene una lista de autores ya procesados para una institución específica.
- `get_autores(org_number)`: Busca autores en Google Scholar asociados a una organización específica.

#### Procesamiento de Datos

- `add_inst_completas(org_number)`: Agrega una institución al archivo de instituciones completadas.
- `agregar_datos_autor(autor)`: Agrega información detallada sobre un autor a los datos procesados.
- `guardar_datos(autor, datos)`: Guarda los datos de un autor en un archivo JSON.
- `guardar_publicaciones(publicaciones, autor)`: Guarda las publicaciones de un autor en un archivo JSON.

#### Integración con Google Cloud Storage y BigQuery

- `transform_and_accumulate(data, authors, publications, coauthors)`: Transforma y acumula datos de autores, publicaciones y coautores.
- `load_data_to_bigquery(table_name, rows)`: Carga datos en BigQuery en lotes.

#### Procesamiento Concurrente

- Uso de `concurrent.futures.ThreadPoolExecutor` para procesar múltiples archivos simultáneamente.

### Ejecución

Para ejecutar el script, asegúrate de tener configuradas las credenciales necesarias para acceder a Google Cloud y tener los archivos CSV requeridos en la misma carpeta que el script.

```sh
python Scraper_Organiza.py
```