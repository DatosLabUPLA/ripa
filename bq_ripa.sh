#! /bin/bash

# Configuración de la cuenta de Google Cloud
gcloud config set project ripa-1022

# Descarga de datos
git clone https://github.com/DatosLabUPLA/ripa
cd ripa
git pull
cd ~

#Autores
cd ripa/GSCHOLAR/AUTORESPORINSTITUCION
for archivo in `ls .`; do bq load --replace=true --source_format=CSV --field_delimiter="," --skip_leading_rows=1 gscholar.authors ./$archivo id_institucion_gs:STRING,id_autor_gs:STRING,autor:STRING,cargo:STRING,id_institucion:STRING,email:STRING,citaciones:INT64,intereses:STRING; done
cd ~

#Publicaciones
cd ripa/GSCHOLAR/ARTICULOS/
for archivo in `ls .`; do bq load --replace=true --source_format=CSV --field_delimiter="," --skip_leading_rows=1 gscholar.pubs ./$archivo id_gs:STRING,id_insttitution:STRING,name:STRING,name_institution:STRING,email:STRING,description:STRING,title:STRING,authors:STRING,journal:STRING,cites:STRING,year:STRING; done
cd ~

#CoAutores
cd ripa/GSCHOLAR/COAUTORES/
for archivo in `ls .`; do bq load --replace=true --source_format=CSV --field_delimiter="," --skip_leading_rows=1 gscholar.coauthors ./$archivo id_gs:STRING,idco:STRING,name_coautor:STRING,email:STRING,description:STRING; done
cd ~

# Scimago 
cd ripa/APP\ PROCESA\ DATOS/
bq load --replace=true --source_format=CSV --field_delimiter="tab" --skip_leading_rows=1 gscholar.scimago scimago_journals_categories.csv id_journal:STRING,journal:STRING,journal_short:STRING,id_journal2:STRING,id_area:STRING,area_name:STRING,id_category:STRING,categories:STRING;

# Tabla pubs_journal
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
bq query --use_legacy_sql=false "create or replace table gscholar.authors_categories as
SELECT p.id_gs, p.short_js,s.journal,s.id_area, s.area_name, s.id_category,s.categories  
FROM `ripa-1022.gscholar.pubs_journal` p, `ripa-1022.gscholar.scimago` s
where p.short_js = s.journal_short"

