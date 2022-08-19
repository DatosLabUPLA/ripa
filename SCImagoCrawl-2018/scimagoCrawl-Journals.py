# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Miguel Guevara <mguevara@mit.edu, miguel.guevara@postgrado.usm.cl>
# created January 14th 2013
# crawl information fo Scimago Journal Rank for research proposses

import os
import sys
import sqlite3 as sqlite
import DB
import utilities
import gather
import datetime
import re
#from utilities import get_html
#from utilsParser import *

SCHIMAGO_COUNTRY_RANK = "http://schimagojr.com"
ROOT_DIRECTORY = os.path.expanduser(
    "~/Dropbox/doctorado/MIT_PROJECT/Data/Symago/DB")
DATABASE_NAME = "scimago-Apr3-2018.db"
DATABASE = os.path.join(ROOT_DIRECTORY, DATABASE_NAME)
print DATABASE
connection = DB.connect_database(DATABASE)
print("Database crea ted: %s" % DATABASE)
begin = datetime.datetime.today()
# regions = ["Western+Europe":"Western Europe","Eastern+Europe":"Eastern
# Europe","Africa":"Africa","Northern+America":"Northern
# America","Latin+America"]
years = DB.get_years_journals(connection)
# print years
categories = DB.get_categories_journals(connection)
# print categories
# min_documents = 0 #filter of number of documents for country
# years=[1996,1997]  			#test data
# categories = [1105, 1104]  	#test data

#BASE = u'http://www.scimagojr.com/countryrank.php?category=%s&year=%s&order=it&min=0&min_type=it'
#BASE = u'http://www.scimagojr.com/countryrank.php?area=0&category=%s&region=all&year=%s&order=it&min=0&min_type=it'
BASE = u'http://www.scimagojr.com/journalrank.php?category=%s&country=all&year=%s&order=sjr&page=%d'
cursor = connection.cursor()

print years

for year in years:
    print year
    for category in categories:
        # print category
        page = 0  # for pagination aka screen of 50 records
        max_page = 0

        while page <= max_page:
            # print 'PAGE:::::::'
            # print page
            link = (BASE % (category[0], year[0], page)).encode('utf8')
            #link = (BASE % (category,year))
            #link = 'http://www.scimagojr.com/countryrank.php?&category='+category+'&region=all&year='+year+'order=it&min=0&min_type=it'
            data = utilities.get_html(link)  # connect Symago JR
            print link
            if page == 0:
                # look for information of quantity of registers total
                registers = re.search('of ([0-9]+)', data)
                if registers is not None:
                    registers_numbers = int(registers.group(1))
                    # each page has 50 registers
                    max_page = int(registers_numbers / 50)
                    #print ("Max Page: %d" % max_page)

            journals_indicators = gather.get_journals_indicators(
                data)  # bottle neck!!
            # print journals_indicators

            for id_journal, indicators in journals_indicators.iteritems():
                #print("Year:%s |	Category: %s  |	Journal: %s %s" % (year[0],category[0], id_journal, indicators[11]))
                # print indicators
                # print indicators
                rank_position = indicators[0]
                journal = indicators[1]
                type_pub = indicators[2]
                sjr = indicators[4]
                h_index = indicators[5]
                total_documents = indicators[6]
                total_documents_3years = indicators[7]
                total_references = indicators[8]
                total_cites_3years = indicators[9]
                citable_documents_3years = indicators[10]
                cites_per_documents_2years = indicators[11]
                references_per_document = indicators[12]
                id_country = indicators[14]  # number 9 was missed for scimago
                quartile = indicators[16]

                cursor.execute("insert  or replace  into journals_indicators values (?,?,?,?,?,?,?,?,?,?,?)", (id_journal, year[
                               0], sjr, h_index, total_documents, total_documents_3years, total_references, total_cites_3years, citable_documents_3years, cites_per_documents_2years, references_per_document))
                id_category = category[0]
                cursor.execute("insert or replace into journals_categories values (?,?,?,?)", (
                    id_journal, id_category, year[0], quartile))
                # print id_journal
                cursor.execute(
                    "insert or replace into journals values (?,?,?,?)", (id_journal, id_country, journal, type_pub))

            connection.commit()
            page = page + 1

        # print country_indicators

print("Database created: %s" % DATABASE)
end = datetime.datetime.today()
print("Tiempo total: ")
print(end - begin)
