# Carga de Organizaciones

Se realizó una descarga de las organizaciones que mantiene actualizada ROR (https://ror.org) que OpenAlex usa como ID. Para ello no se conecto directamente con la API si no que se realizo una descarga de una snapshot de los datos. La descarga mas reciente al escribir este documento fue la 1.49-2024-07-11.

Ademas se realizó csv mix entre las organizaciones existentes previamente con un identificador de Google Scholar y las de ROR para poder complementar la información.

Para descargar una version mas reciente de los datos se debe ingresar a (https://zenodo.org/records/12729557). Se utiliza el archivo del schema v2 en formato json, el nombre del archivo es temina en ¨data_schema_v2.json¨.

El script toma solo las organizaciones en chile, que sean del tipo educacion y su estatus sea activo.