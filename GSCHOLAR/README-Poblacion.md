
# Pipeline de Datos Académicos

## Introducción

Este proyecto es un pipeline de datos diseñado para extraer, transformar y cargar (ETL) datos académicos en Google BigQuery. Los datos se almacenan en Google Cloud Storage en formato JSON e incluyen información sobre autores, publicaciones y coautores. El script procesa los datos en paralelo, los valida y los carga en tablas de BigQuery.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Características](#características)
- [Dependencias](#dependencias)
- [Configuración](#configuración)
- [Documentación](#documentación)
- [Ejemplos](#ejemplos)
- [Solución de Problemas](#solución-de-problemas)
- [Contribuidores](#contribuidores)
- [Licencia](#licencia)

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/yourusername/scholarly-data-pipeline.git
   cd scholarly-data-pipeline
   ```

2. **Configurar un entorno virtual e instalar dependencias:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configurar las credenciales de Google Cloud:**
   Asegúrate de tener un archivo de clave de cuenta de servicio de Google Cloud y configura la variable de entorno `GOOGLE_APPLICATION_CREDENTIALS`:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"
   ```

## Uso

Ejecuta el script para iniciar el proceso ETL:
```bash
python Script_poblacion.py
```

## Características

- **Procesamiento en Paralelo:** Utiliza `ThreadPoolExecutor` para el procesamiento concurrente de archivos JSON.
- **Validación de Datos:** Verifica que los archivos JSON sean válidos antes de procesarlos.
- **Integración con BigQuery:** Crea las tablas necesarias y carga los datos en BigQuery.
- **Actualizaciones Incrementales:** Solo se procesan y cargan los registros nuevos.

## Dependencias

- `google-cloud-bigquery`
- `google-cloud-storage`
- `concurrent.futures`
- `threading`
- `os`
- `json`

## Configuración

### Configuración de BigQuery y Cloud Storage

- **ID del Proyecto:** Configurado en el script como `project_id = 'ripa-1022'`.
- **ID del Dataset:** Configurado en el script como `dataset_id = 'scholarly'`.
- **Bucket de Almacenamiento:** Configurado en el script como `bucket_name = 'scholarly_data'`.

### Esquemas de Tablas de BigQuery

El script define esquemas para tres tablas: `Info_Autores`, `Info_Publicaciones` y `Info_Coautores`. Estos esquemas se utilizan para configurar las tablas si no existen.

## Documentación

Los componentes principales del script son:

- **Inicialización:** Configuración de clientes de BigQuery y Storage.
- **Definiciones de Esquemas:** Esquemas para las tablas de BigQuery.
- **Creación de Tablas:** Asegura que las tablas necesarias se creen si no existen.
- **Extracción y Validación de Datos:** Descarga y valida archivos JSON desde Cloud Storage.
- **Transformación de Datos:** Extrae información relevante de los archivos JSON.
- **Carga de Datos:** Carga datos en las tablas de BigQuery en lotes.
- **Procesamiento Concurrente:** Utiliza hilos para procesar múltiples archivos simultáneamente.

## Ejemplos

Ejemplo de ejecución del script:
```bash
python Script_poblacion.py
```

## Solución de Problemas

### Problemas Comunes

1. **Error de JSON Inválido:** Asegúrate de que todos los archivos JSON en el bucket de Cloud Storage estén correctamente formateados.
2. **Permisos de BigQuery:** Asegúrate de que tu cuenta de servicio tenga los permisos necesarios para crear tablas y cargar datos en BigQuery.
3. **Problemas de Red:** Asegúrate de tener una conexión a internet estable para interactuar con los servicios de Google Cloud.

### Registros

El script imprime registros en la consola para varias etapas del procesamiento, como la creación de tablas, validación de datos y carga. Revisa la salida de la consola para cualquier mensaje de error o actualizaciones de estado.

