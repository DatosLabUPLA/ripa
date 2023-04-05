#! /bin/bash

# Configuración de la cuenta de Google Cloud
echo "Configurando proyecto"
gcloud config set project ripa-1022

# Descarga de datos
echo "Revisando si el proyecto existe y/o actualizandolo"
git clone https://github.com/DatosLabUPLA/ripa
cd ripa
git pull

# Moviendo script
echo "Moviendo script a carpeta de nivel superior"
cp bq_ripa.sh ~/bq_ripa.sh
chmod +x ~/bq_ripa.sh
cd ~

#Autores
echo "Cargando datos a BigQuery - Autores"
cd ripa/GSCHOLAR/AUTORESPORINSTITUCION
for archivo in `ls .`; do bq load --replace=true --source_format=CSV --field_delimiter="," --skip_leading_rows=1 gscholar.authors ./$archivo id_institucion_gs:STRING,id_autor_gs:STRING,autor:STRING,cargo:STRING,id_institucion:STRING,email:STRING,citaciones:INT64,intereses:STRING; done
cd ~

#Publicaciones
echo "Cargando datos a BigQuery - Publicaciones"
cd ripa/GSCHOLAR/ARTICULOS/
for archivo in `ls .`; do bq load --replace=true --source_format=CSV --field_delimiter="," --skip_leading_rows=1 gscholar.pubs ./$archivo id_gs:STRING,id_insttitution:STRING,name:STRING,name_institution:STRING,email:STRING,description:STRING,title:STRING,authors:STRING,journal:STRING,cites:STRING,year:STRING; done
cd ~

#CoAutores
echo "Cargando datos a BigQuery - CoAutores"
cd ripa/GSCHOLAR/COAUTORES/
for archivo in `ls .`; do bq load --replace=true --source_format=CSV --field_delimiter="," --skip_leading_rows=1 gscholar.coauthors ./$archivo id_gs:STRING,idco:STRING,name_coautor:STRING,email:STRING,description:STRING; done
cd ~

# Scimago 
echo "Cargando datos a BigQuery - Scimago"
cd ripa/APP\ PROCESA\ DATOS/
bq load --replace=true --source_format=CSV --field_delimiter="tab" --skip_leading_rows=1 gscholar.scimago scimago_journals_categories.csv id_journal:STRING,journal:STRING,journal_short:STRING,id_journal2:STRING,id_area:STRING,area_name:STRING,id_category:STRING,categories:STRING;

# Tabla pubs_journal
echo "Creando tabla de publicaciones con el nombre del pubs_journal"
bq query --use_legacy_sql=false "
create or replace TABLE gscholar.pubs_journal as
SELECT id_gs, lower(
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
              replace(journal,' ',''),',',''
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
from gscholar.pubs
"

# Tabla authors_categories
echo "Creando tabla de autores con categorias"
bq query --use_legacy_sql=false "create or replace table gscholar.authors_categories as
SELECT p.id_gs, p.short_js,s.journal,s.id_area, s.area_name, s.id_category,s.categories  
FROM `ripa-1022.gscholar.pubs_journal` p, `ripa-1022.gscholar.scimago` s
where p.short_js = s.journal_short"

