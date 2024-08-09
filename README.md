# ripa
RIPA Chile

## Instalar dependencias
Para instalar las dependencias del proyecto se debe contar con un ambiente virtual como `virtualenv` o `conda`. En este caso se usará `conda`.

```bash
conda create -n ripa python=3.12 -y
conda activate ripa
pip install -r requirements.txt
```

## Configuración de Google BigQuery
Para configurar la terminal de Google BigQuery con el proyecto se debe descargar el repositorio ya que hay pasos para actualizar las tablas que requieren de esta configuración inicial.

```bash
gcloud config set project ripa-1022

cd ~
git clone https://github.com/DatosLabUPLA/ripa

```

## Actualizar tablas

El proyecto utiliza `Google BigQuery` para almacenar los datos en el proyecto `ripa-1022` y en el dataset `ripa`.

### Tablas ANID
Tablas involucradas:
- anid_colaboracion
- anid_curriculo
- anid_difusion_y_transferencia
- anid_educacion
- anid_experiencia_academica
- anid_experiencia_profesional
- anid_formacion_de_capital_humano
- anid_investigador
- anid_produccion

### Tablas Google Scholar
Tablas involucradas:
- gs_authors
- gs_coauthors
- gs_publications

#### Atualizar datos
Para actualizar estos datos se debe contar con una API_KEY de `ScraperAPI` e incluirla en el codigo `GSCHOLAR\Scraper_Organiza.py`. Además se debe borrar el contenido del archivo `GSCHOLAR\organizaciones_completas.csv`. 

El script tomará los id de las organizaciones de Google Scholar almacenadas en `GSCHOLAR\organizaciones.csv` y mediante el paquete de `scholarly` se obtendrán los datos de los autores y se almacenarán en formato JSON de forma **local** en la carpeta `GSCHOLAR\DATOS_COMPLETOS`. El script tiene en cuenta los datos previemente descargados y no los vuelve a descargar. Este proceso puede tardar varias horas.

#### Poblar las tablas **(NO RECUERDO SI TIENE QUE HACERSE DESDE LA TERMINAL DE BIGQUERY O LOCAL)**
Una vez actualizados los datos de manera local, se debe ejecutar el script `GSCHOLAR\gs_upload_data.py` para poder subir los datos a BigQuery. Este script debe ejecutarse desde la terminal de BigQuery y solicitará permisos al usuario.

```bash
cd ~/ripa
git pull
cd GSCHOLAR
python gs_upload_data.py
```

### Tablas Scimago
Tablas involucradas:
- ripa_authors_categories
- ripa_pubs_journal
- ripa_scimago

#### Atualizar datos
Para recrear estas tablas se debe ejecutar en la terminal de BigQuery el archivo `bq_ripa_v2.sh`, esto solicitará permisos al usuario y luego empezará a ejecutarse. Si se quieren actualizar los datos teniendo ya las creadas, estas deben ser eliminadas antes de ejecutar el script.

```bash
cd ~/ripa
git pull
cp bq_ripa_v2.sh ~
cd ~
chmod +x bq_ripa_v2.sh
./bq_ripa_v2.sh
```

### Tabla API Gender
Tablas involucradas:


### Tablas RIPA
Tablas involucradas:
- ripa_organizations

#### Atualizar datos

## Tablas Openalex
Esta es una base de datos completa que pesa 3TB, por lo que se decidió subirla a dataset distinto llamado `openalex`. 

Se siguieron los pasos que ofrece [Openalex](https://docs.openalex.org/download-all-data/upload-to-your-database/load-to-a-data-warehouse) para subir los datos, por lo cual se subieron en formato de JSON uno por registro.

Para hacer la carga inicial de los datos se debe considerar que el proceso demorará en el rango de horas. En las pruebas realizadas demoró ~3 horas en cargar los 3TB a una velocidad de ~900Mbps y ~24 horas a una velocidad de ~100Mbps. Dada la cantidad de datos se realizo un cobre de ~40USD para la subida de datos y ~2USD cada día que se mantenga la base de datos. Adicionalmente las consultas cuesta dinero, por lo que se debe tener cuidado con las consultas que se realicen.

Tablas involucradas:
- authors
- concepts
- institutions
- publishers
- sources
- works

#### Recrear tablas
Para recrear la base de datos desde cero, se debe crear el dataset y luego generar las tablas. Esto debe realizarse desde la terminal de BigQuery, pero tambien puede realizarce desde una terminal local con el [SDK de Google Cloud](https://cloud.google.com/sdk/docs/install?hl=es-419) instalado.

Pasos para crear el dataset y las tablas:
```bash
# Crear dataset
bq mk ripa-1022:openalex

# Crear tablas
bq mk --table ripa-1022:openalex.works work:string
bq mk --table ripa-1022:openalex.authors author:string
bq mk --table ripa-1022:openalex.sources source:string
bq mk --table ripa-1022:openalex.institutions institution:string
bq mk --table ripa-1022:openalex.concepts concept:string
bq mk --table ripa-1022:openalex.publishers publisher:string
```

Se debe descargar el repositorio de Openalex para luego subirlo, no hay forma de hacerlo directamente con el dataset completo. El proceso completo aqui [Openalex](https://docs.openalex.org/download-all-data/download-to-your-machine). Además se requiere de utilizar la [AWS CLI](https://aws.amazon.com/cli/). 


Dado que se descarga una gran cantidad de datos y archivos se recomienda ejecutarlo fuera del repositorio para que Github no intente subirlos.

Vamos a simular que dentro de la carpeta de `openalex` tenemos los archivos `OPENALEX\openalex-snapshot\main.py` y `credentials.json`, ejecutamos lo siguiente para empezar a descargar los datos:

```bash
# Conocer el tamaño de la base de datos comprimida
aws s3 ls --summarize --human-readable --no-sign-request --recursive "s3://openalex/"

# Descargar la base de datos
aws s3 sync "s3://openalex" "openalex-snapshot" --no-sign-request

```

Ahora tendremos una nueva carpeta llamada `openalex-snapshot`, que contiene la base de datos. Ahora ejecutaremos el script de python que se encargará de subir los datos a BigQuery.

```bash
# Estando en el directorio de openalex
python main.py
```




