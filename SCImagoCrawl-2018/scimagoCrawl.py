# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Miguel Guevara <mguevara@mit.edu, miguel.guevara@postgrado.usm.cl>
# created 4 Oct 2013
# crawl information fo Scimago Country Rank for research proposses

import os
import sys
import sqlite3 as sqlite
import DB
import utilities
import gather
import datetime
# from bs4 import BeautifulSoup   #added 10 sep 2014
#from utilities import get_html
#from utilsParser import *

SCHIMAGO_COUNTRY_RANK = "http://schimagojr.com"
ROOT_DIRECTORY = os.path.expanduser(
    "~/Dropbox/UPLA/DOCENCIA/CIF9159\ TALLER\ INTEGRADO/TALLER\ INTEGRADO\ BASE/CODES/SCImagoCrawl-2018")
DATABASE_NAME = "scimago-Apr3-2018.db"
print os.path.join(DATABASE_NAME)
#DATABASE = os.path.join(ROOT_DIRECTORY, DATABASE_NAME)
DATABASE = os.path.join(DATABASE_NAME)
# you have to create manually tables categories, areas, year, countries
print DATABASE
connection = DB.connect_database(DATABASE)
print("Database created: %s" % DATABASE)
begin = datetime.datetime.today()

# for the first time


# regions = ["Western+Europe":"Western Europe","Eastern+Europe":"Eastern
# Europe","Africa":"Africa","Northern+America":"Northern
# America","Latin+America"]
years = DB.get_years(connection)
years = map(lambda x: int(x[0]), years)
print years
categories = DB.get_categories(connection)
categories = map(lambda x: int(x[0]), categories)
print categories

## min_documents = 0 #filter of number of documents for country
#years=[1996,2015]  			#test data
#categories = [1105, 1104]  	#test data

#BASE = u'http://www.scimagojr.com/countryrank.php?category=%s&year=%s&order=it&min=0&min_type=it'
BASE = u'http://www.scimagojr.com/countryrank.php?area=0&category=%s&region=all&year=%s&order=it&min=0&min_type=it'
cursor = connection.cursor()
page = 0  # number of page AKA screen with 50 rows.

for year in years:
    print year
    for category in categories:
        print category
        #print(BASE % (category[0],year[0]))
        #link = (BASE % (category[0], year[0])).encode('utf8') #official
        link = (BASE % (category,year)).encode('utf8')  #test
        #link = 'http://www.scimagojr.com/countryrank.php?&category='+category+'&region=all&year='+year+'order=it&min=0&min_type=it'

        data = utilities.get_html(link)  # connect Symago JR

        #data1 = data0.split('<tbody>')[1]
        #data = data1.split('</tbody>')[0]
        print link
        # print data
        countries_indicators = gather.get_indicators(data)  # bottle neck!!
        # print("indicators")
        # print(countries_indicators)

        for id_country, indicators in countries_indicators.iteritems():
            #print("Year:%s |	Category: %s  |	Country: %s" %
                  #(year[0], category[0], id_country))  #real
            print("Year:%s |    Category: %s  | Country: %s" %  #testing
                  (year, category, id_country))
            # print indicators
            documents = indicators[0]
            citable_documents = indicators[1]
            citations = indicators[2]
            self_citations = indicators[3]
            citations_per_document = indicators[4]
            h_index = indicators[5]

            cursor.execute("insert  or replace  into indicators values (?,?,?,?,?,?,?,?,?)", (category, id_country, year, documents, citable_documents,  citations, self_citations, citations_per_document, h_index))

        connection.commit()

        # print country_indicators

print("Database created: %s" % DATABASE)
end = datetime.datetime.today()
#print("Tiempo total: %d" %(int(end-begin)))
