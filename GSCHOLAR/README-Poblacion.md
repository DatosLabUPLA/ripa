# README-Poblacion.md

## Descripción del Código

Este script tiene como objetivo cargar datos de archivos JSON almacenados en Google Cloud Storage (GCS) a tablas en Google BigQuery. Los datos corresponden a información de autores, publicaciones y coautores relacionados con la universidad.

## Requisitos Previos

1. **Credenciales de Google Cloud**: Asegúrese de tener configuradas las credenciales de Google Cloud. Si no está utilizando Cloud Shell, configure la ruta a sus credenciales:
    ```python
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-file.json"
    ```

2. **Clientes de BigQuery y Storage**: El script utiliza los clientes de BigQuery y Storage de Google Cloud.

3. **Configuración del Proyecto**: Asegúrese de tener los IDs del proyecto, dataset y bucket configurados correctamente:
    ```python
    project_id = 'ripa-1022'
    dataset_id = 'universidad'
    bucket_name = 'scholarly_data'
    ```

## Funcionalidad

### Inicialización

1. **Clientes de BigQuery y Storage**: Inicializa los clientes necesarios.
2. **Referencias a Tablas y Esquemas**: Define las referencias y esquemas de las tablas de BigQuery.

### Creación de Tablas

Las tablas `Info_Autores`, `Info_Publicaciones` y `Info_Coautores` se crean en BigQuery si no existen.

### Procesamiento de Archivos JSON

1. **Descargar Blobs**: Se listan y descargan todos los blobs del bucket de GCS.
2. **Validación y Extracción de Datos**: Se validan y extraen datos de los archivos JSON descargados.
3. **Filtrado de Datos Existentes**: Se obtienen los IDs ya existentes en las tablas de BigQuery para evitar duplicados.

### Carga de Datos a BigQuery

1. **Agrupar Datos en Lotes**: Los datos extraídos se agrupan en lotes de tamaño fijo.
2. **Cargar Datos en Paralelo**: Se cargan los datos en BigQuery en paralelo utilizando un `ThreadPoolExecutor`.

## Detalles del Código

### Funciones Clave

- **create_table_if_not_exists**: Crea una tabla en BigQuery si no existe.
- **is_valid_json**: Verifica si un texto es un JSON válido.
- **extract_info**: Extrae información de autores, publicaciones y coautores de los datos JSON.
- **process_blob**: Procesa un blob (archivo JSON) descargado de GCS.
- **load_data_to_bigquery**: Carga datos a una tabla de BigQuery desde un archivo temporal.
- **get_existing_ids**: Obtiene los IDs existentes de una tabla de BigQuery.
- **batch_and_load_data**: Agrupa datos en lotes y los carga a BigQuery.

### Estructura del Script

1. **Configuración Inicial**: Inicializa clientes y define configuraciones.
2. **Creación de Tablas**: Verifica y crea tablas en BigQuery.
3. **Procesamiento de Datos**: Descarga, valida, extrae y filtra datos JSON.
4. **Carga de Datos**: Agrupa y carga datos en BigQuery en paralelo.

## Ejecución

Para ejecutar el script, simplemente asegúrese de tener las dependencias necesarias instaladas y ejecute el script en su entorno Python configurado con las credenciales y permisos adecuados para acceder a Google Cloud Storage y Google BigQuery.

```bash
python script.py
