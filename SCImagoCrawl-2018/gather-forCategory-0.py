# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Miguel Guevara <miguel.guevara@postgrado.usm.cl, mguevara@mit.edu>
# Oct 5 2013


def get_soup(data):
    """Returns a BeautifulSoup (HTML-parsed input)"""

    return __import__('BeautifulSoup').BeautifulSoup(data)


def get_countries(data):
    """Parses the HTML link and returns the table rows where there are countries
    """
    import re

    def table_row_checker(tag):
        if tag.name == 'td' and tag.get('class') == 'tit':
            return True
        return False

    countries_html = get_soup(data).findAll(
        table_row_checker)  # returns a list
    # print countries_html
    #countries_id = []
    countries = {}

    for country_html in countries_html:
        try:
            # print label.text
            # countries_id.append(re.search('country=(.+?)&',country_html.a.get('href')).group(1))
            countries[re.search(
                'country=(.+?)&', country_html.a.get('href')).group(1)] = country_html.a.text
            # countries.append(country_html.a.text)
        except AttributeError:
            break
    return countries


def get_indicators(data):
    """Parses the HTML to get indicators scientifics
    """
    import re

    def table_div_checker(tag):
        if tag.name == 'div' and tag.get('class') == 'dentro_td':
            return True
        return False

    def table_row_checker(tag):
        if tag.name == 'td' and tag.get('class') == 'tit':
            return True
        return False

    countries_html = get_soup(data).findAll(
        table_row_checker)  # returns a list
    countries_indicators = {}
    indicators_html = get_soup(data).findAll(table_div_checker)
    country_number = 0

    for country_html in countries_html:

        #indicators = {}
        country_indicators = []

        for indicator in indicators_html[country_number:country_number + 6]:
            indicator_value = indicator.span.text
            if indicator_value.find('.') != -1:
                indicator_value = indicator_value.replace(".", '')
            if indicator_value.find(',') != -1:
                indicator_value = indicator_value.replace(",", '.')
            country_indicators.append(indicator_value)

            # print indicator_value

        id_country = re.search(
            'country=(.+?)&', country_html.a.get('href')).group(1)
        countries_indicators[id_country] = country_indicators
        print countries_indicators[id_country]
        country_number += 6

    # print countries_indicators
    return countries_indicators


def get_journals_indicators(data):
    """Parses the HTML to get indicators for Journals
    """
    import re

    def table_div_checker(tag):
        if tag.name == 'td':
            return True
        return False

    def table_row_checker(tag):
        if tag.name == 'td' and tag.get('class') == 'tit':
            return True
        return False

    # returns a list with class == tit
    journals_html = get_soup(data).findAll(table_row_checker)
    journals_indicators = {}  # list with results
    indicators_html = get_soup(data).findAll(table_div_checker)  # whole TD!

    # indicators begin at TD number 3 in each tr. 19 for another table at the
    # begining
    journal_number = 2 + 18

    # recorring throw the number of rows according journals
    for journal_html in journals_html:

        #indicators = {}
        # print journal_html
        journal_indicators = []
        print indicators_html[journal_number:journal_number + 10]
        # print indicators_html[journal_number + 9]
        for indicator in indicators_html[journal_number:journal_number + 10]:
            # we have an array with all TDs, each 13 we have a new Journal
            indicator_value = indicator.text
            # print indicator_value
            if indicator_value.find('.') != -1:
                indicator_value = indicator_value.replace(".", '')
            if indicator_value.find(',') != -1:
                indicator_value = indicator_value.replace(",", '.')
            journal_indicators.append(indicator_value)

            # print indicator_value

        id_journal = re.search('q=(.+?)&', journal_html.a.get('href')).group(1)
        journal = journal_html.text
        # print journal
        # print indicators_html[journal_number + 9]

        id_country = indicators_html[
            journal_number + 9].img.get('alt')  # image bander country
        # print id_country

        # adding country to array or indicators
        journal_indicators.append(id_country)
        journal_indicators.append(journal)

        # add to dictionaries of results
        journals_indicators[id_journal] = journal_indicators

        # print journals_indicators[id_journal]
        journal_number += 12  # forwarding the array with td data

    # print countries_indicators
    return journals_indicators
