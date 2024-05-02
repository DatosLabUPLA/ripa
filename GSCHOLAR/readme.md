(TITULO)Sistema de extraccion de datos
Modulo de extraccion de datos para modelo ETL utilizando la libreria scholarly. 

Dicha libreria extrae los datos desde google scholar con  funciones predefinidas para la facilitar su uso.

Dentro de este proyecto se utilizan las siguientes funciones de scholarly:

1.-search_author_by_organization(id_universidad): dicha funcion en base el id de una univeridad entrega una lista de objetos del tipo autor. Esta funcion se utiliza para realizar una extraccion de todos los autores de cada universidad, sin embargo solo traen la informacion especifica de cada uno

2.- fill(author:Author object): funcion que rellena un objeto del tipo Author para que contenga completa cantidad de su informacion

Dentro del codigo principal se encuentran 3 funciones principales

1.-search_authors_by_organitzation(org_number,last_author_id=None): esta funcion parte el codigo ya que es la que busca los autores desde el ultimo obtenido desde el log de uso del codigo

2.- save_authors(authors, institution_name,dominio): funcion que guarda la informacion completa de los autores para luego dicha informacion guardarla en un archivo de tipo json en especifico por cada autor

3.- main(): funcion principal que compara las universidades terminadas con las que estan por terminar y en base a las universidades restantes se corre el codigo para guardar informacion faltante

guardar la info en dos log nuevo uno de autor y otro de universidades

resta conjuntos 

