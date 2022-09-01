# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Miguel Guevara <mguevara@mit.edu>
# 6 Sep 2013

import sqlite3 as sqlite
import os
import utilities


def connect_database(name_db):
    """ Returns a connection object to database. If database does not
exist, the creates the new database.
    """
    DATABASE_NAME = name_db
    is_new_database = os.path.exists(DATABASE_NAME)
    connection = sqlite.connect(DATABASE_NAME)

  # if not is_new_database:
    cursor = connection.cursor()
    cursor.executescript("""
	  create table IF NOT EXISTS  areas(
		id_area primary key,
		name			
	   );
	   
	   create table IF NOT EXISTS  categories(
		id_category primary key, 
		id_area,
		categories
	   );
	   
	   create table IF NOT EXISTS  regions(
	    id_region primary key,
	    region
	   );
	   
	   create table IF NOT EXISTS  types(
	    id_type primary key,
	    type 
	   );
	   
	   create table IF NOT EXISTS  years(
	    id_year primary key,
	    year
	   );
	   
	   create table IF NOT EXISTS  countries(
	    id_country primary key,
	    id_region,
	    country
	   );

	   create table IF NOT EXISTS  indicators(
	   	id_category,
	   	id_country,
	   	id_year,
	   	documents,
	   	citable_documents,
	   	citations,
	   	self_citations,
	   	citations_per_document,
	   	h_index,
	   	PRIMARY KEY (id_category, id_country, id_year)

	   	);

		create table  IF NOT EXISTS  journals(
			id_journal,
			id_country,
			journal,
			PRIMARY KEY (id_journal)
			);

		create table  IF NOT EXISTS journals_categories(
			id_journal,
			id_category,
			PRIMARY KEY (id_journal, id_category)
			);

		create table IF NOT EXISTS journals_indicators(
			id_journal,
			id_year,
			sjr,
			h_index,
			total_documents,
			total_documents_3years,
			total_references,
			total_cites,
			citable_documents_3years,
			cites_per_documents_2years,
			references_per_document,
			PRIMARY KEY (id_journal,id_year)
			)
	   
		""")

    # insert_regions #not used
    # insert_countries(connection)
    # insert_maestro(connection,"areas") #not working done manually
    # insert_maestro(connection,"categories") # not working done manually
    #insert_maestro(connection,"years") #
    # insert_years()

    return connection


def insert_countries(connection):
    import gather
    cursor = connection.cursor()

    regions = {"Western+Europe": "Western Europe", "Eastern+Europe": "Eastern Europe", "Africa": "Africa", "Northern+America": "Northern America",
               "Latin+America": "Latin America", "Middle+East": "Middle East", "Asiatic+Region": "Asiatic Region", "Pacific+Region": "Pacific Region"}
    countries = {}

    for region, id_region in regions.iteritems():
        BASE = u'http://www.scimagojr.com/countryrank.php?&region=%s'
        link = (BASE % (region)).encode('utf8')
        print link
        data = utilities.get_html(link)
        # print data
        countries = gather.get_countries(data)
        # print countries
        for id_country, country in countries.iteritems():
            # print country_id
            print country
            cursor.execute(
                "insert or replace into countries(id_country, id_region, country) values(?,?,?)", (id_country, id_region, country))
            connection.commit()


def insert_maestro(connection, table):
    import os
    maestros = os.path.expanduser(
        "~/Dropbox/doctorado/MIT_PROJECT/Data/Symago/maestros")
    table_csv = table + ".csv"
    file_csv = os.path.join(maestros, table_csv)
    cursor = connection.cursor()
    cursor.executescript(""" separator ";" """)
    cursro.execute(""" .import %s %s %(file_csv, table)""")


def get_categories(connection):
    cursor = connection.cursor()
    cursor.execute("select id_category from categories")
    categories = cursor.fetchall()
    return categories


def get_countries(connection):
    cursor = connection.cursor()
    cursor.execute("select id_country from countries")
    countries = cursor.fetchall()
    return countries


def get_years(connection):
    cursor = connection.cursor()
    cursor.execute("select id_year from years order by year desc")
    years = cursor.fetchall()
    return years


def get_years_journals(connection):
    cursor = connection.cursor()
    # just data since 1999
    cursor.execute(
        "select id_year from years where cast(id_year as int) != 0  and cast(id_year as int) >= 1999 and cast(id_year as int) <= 2003 order by year desc")
    years = cursor.fetchall()
    return years


def get_categories_journals(connection):
    cursor = connection.cursor()
    cursor.execute(
        "select id_category from categories where id_category not like '0'")
    categories = cursor.fetchall()
    return categories
