(TITULO)Sistema de extraccion de datos
Modulo de extraccion de datos para modelo ETL utilizando la libreria scholarly. 

Dicha libreria extrae los datos desde google scholar con  funciones predefinidas para la facilitar su uso.

Dentro de este proyecto se utilizan las siguientes funciones de scholarly:

1.-search_author_by_organization(id_universidad): dicha funcion en base el id de una univeridad entrega una lista de objetos del tipo autor. Esta funcion se utiliza para realizar una extraccion de todos los autores de cada universidad, sin embargo solo traen la informacion especifica de cada uno

2.- fill(author:Author object): funcion que rellena un objeto del tipo Author para que contenga completa cantidad de su informacion

Dentro del codigo principal se encuentran las siguientes funciones principales

1.-get_instituciones(): Esta funcion obtiene las ID de instituciones del archivo semilla en formato csv (vease 'organizaciones.csv') donde se obtienen todas las instituciones para analizar

2.- get_instituciones_completas(): Esta funcion obtiene las ID de las universidades ya completadas en el archivo, donde retorna un conjunto con las instituciones completas. De manera que se resta con el conjunto retornado en get_instituciones, y asi analizar las intituciones que faltan analizar

3.- get_autores_completados(dominio):Obtiene todos los ID de autores guardados de una institucion que devuelve un arreglo con esas ID's

4.- get_autores(org_number): obtiene todos los ID's de autores de una institucion, lo que devuelve es un conjunto con los id's de autores

5.- add_inst_completas(org_number): Funcion que agrega en un archivo CSV las instituciones que ya se encuentran con todos sus autores extraidos.

6.- get_dominio(org_number):

7.- save_authors(authors, institution_name,dominio): funcion que guarda la informacion completa de los autores para luego dicha informacion guardarla en un archivo de tipo json en especifico por cada autor

8.- main(): funcion principal que compara las universidades terminadas con las que estan por terminar y en base a las universidades restantes se corre el codigo para guardar informacion faltante
