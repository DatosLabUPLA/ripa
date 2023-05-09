from scholarly import scholarly 
import csv
from fake_useragent import UserAgent

urls=[]

def autor(id_autor):
    print(id_autor)
    search_query = scholarly.search_author_id(id_autor)

with open("AUTORESPORINSTITUCION/autonoma.csv",encoding="utf8") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        #urls.append(row['ï»¿ids'])
        urls.append(row['id_autor_gs'])

for ids in urls:
    autor(ids)    

#codigo de prueba para revisar si la ID existia o estaba mal escrita
'''author = scholarly.search_author_id('fHT2L6gAAAAJ')
scholarly.pprint(author)'''
    
    