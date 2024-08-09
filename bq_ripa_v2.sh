#! /bin/bash

# Configuración de la cuenta de Google Cloud
echo "Configurando proyecto"
gcloud config set project ripa-1022

# Definir variable de tiempo de inicio
start_time=`date +%s`

# Actualizar repositorio
echo "Revisando si el proyecto existe y/o actualizandolo"
git clone https://github.com/DatosLabUPLA/ripa
cd ripa
git pull
cd ~

# Instrucciones previas
echo "--------------------------"
echo "INSTRUCCIONES PREVIAS V2"
echo "1) Antes de continuar, asegurese de haber creado el dataset ripa en BigQuery"
echo "2) Asegurese de haber eliminado las tablas pubs, authors y coauthors en el dataset ripa"
echo "--------------------------"

# Pregunta si desea actualizar los datos
echo "Desea actualizar los datos? (y/n)"
read actualizar

# Si la respuesta es "y" se actualizan los datos
if [ $actualizar = "y" ]; then
    echo "Actualizando datos"

    # Scimago 
    echo "Cargando datos a BigQuery - Scimago"
    cd ripa/APP\ PROCESA\ DATOS/
    bq load --source_format=CSV --field_delimiter="tab" --skip_leading_rows=1 ripa.ripa_scimago scimago_journals_categories.csv id_journal:STRING,journal:STRING,journal_short:STRING,id_journal2:STRING,id_area:STRING,area_name:STRING,id_category:STRING,categories:STRING;

    # Tabla pubs_journal
    echo "Creando tabla de publicaciones con el nombre del ripa_pubs_journal"
    bq query --use_legacy_sql=false \
    "create or replace TABLE ripa.ripa_pubs_journal as
    SELECT scholar_id, lower(
      regexp_replace(
        replace(
        replace(
        replace(
        replace(
        replace(
        replace(
          replace(
            replace(
              replace(
                replace(
                  replace(citation,' ',''),',',''
                ), '(',''
              ), ')',''
            ),'-',''
          ), 'á','a'
        ),'é', 'e'
        ),'í','i'
        ),'ó','o'
        ),'ú','u'
        ), 'ñ','n'

          ),r'([0-9]+)',''
        )
      ) as short_js
    from ripa.gs_publications
    "

    # Tabla authors_categories
    echo "Creando tabla de autores con categorias"
    bq query --use_legacy_sql=false \
    "create or replace table ripa.ripa_authors_categories as
    SELECT p.scholar_id, p.short_js,s.journal,s.id_area, s.area_name, s.id_category,s.categories  
    FROM ripa-1022.ripa.ripa_pubs_journal p, ripa-1022.ripa.ripa_scimago s
    where p.short_js = s.journal_short"
else
    echo "No se actualizarán los datos"
fi

# Definir variable de tiempo de finalización
end_time=`date +%s`

# Mostrar tiempo de ejecución
echo "Tiempo de ejecución: $((end_time-start_time)) segundos"
