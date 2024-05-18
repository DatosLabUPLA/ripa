
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

## Script_poblacion.py

Este repositorio contiene un script en Python diseñado para automatizar el proceso de carga de datos de Google Scholar en BigQuery. El script recupera datos desde Google Cloud Storage, los procesa y los carga en tablas predefinidas en BigQuery.

### Características

- **Integración con BigQuery**: Crea automáticamente tablas en BigQuery si no existen.
- **Integración con Google Cloud Storage**: Recupera archivos JSON que contienen datos de Google Scholar desde un bucket especificado de Google Cloud Storage.
- **Transformación de Datos**: Transforma y agrega datos para autores, publicaciones y coautores.
- **Procesamiento Concurrente**: Utiliza multithreading para procesar múltiples archivos simultáneamente y cargar datos de manera eficiente.
- **Procesamiento por Lotes**: Inserta datos en BigQuery en lotes para un rendimiento optimizado.

### Configuración

#### Prerrequisitos

- **Google Cloud SDK**: Asegúrate de tener instalado y configurado Google Cloud SDK.
- **Cuenta de Servicio**: Crea una cuenta de servicio con permisos para acceder a BigQuery y Cloud Storage. Descarga el archivo de clave JSON.
- **Paquetes de Python**: Instala los paquetes de Python requeridos usando el siguiente comando:

```sh
pip install google-cloud-bigquery google-cloud-storage
```

#### Configuración

Establece la ruta a tu archivo de credenciales de Google Cloud descomentando y actualizando la siguiente línea en el script:

```python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ruta/a/tu/archivo-de-cuenta-de-servicio.json"
```

Actualiza las variables `project_id`, `dataset_id` y `bucket_name` en el script para que coincidan con tu proyecto y recursos de Google Cloud:

```python
project_id = 'tu-id-de-proyecto'
dataset_id = 'tu-id-de-dataset'
bucket_name = 'tu-nombre-de-bucket'
```

### Uso

1. Asegúrate de que tus credenciales de Google Cloud estén configuradas correctamente.
2. Ejecuta el script:

```sh
python Script_poblacion.py
```

### Descripción del Script

El script realiza las siguientes funciones principales:

- **Creación de Tablas**: Define esquemas para las tablas `Info_Autores`, `Info_Publicaciones` e `Info_Coautores` y las crea en BigQuery si no existen.
- **Recuperación de Datos**: Lista y lee archivos JSON del bucket especificado de Cloud Storage.
- **Transformación de Datos**: Extrae la información relevante de cada archivo JSON y la prepara para su carga en BigQuery.
- **Carga por Lotes**: Inserta datos en las tablas de BigQuery en lotes de 100 registros utilizando el método `insert_rows_json`.
- **Procesamiento Concurrente**: Utiliza `ThreadPoolExecutor` para procesar múltiples archivos JSON concurrentemente.

### Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

```sh
python Script_poblacion.py
```
