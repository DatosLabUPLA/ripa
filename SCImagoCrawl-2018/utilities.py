
def get_html(link):
    """Retrieves a given page HTML code"""
    #GOOGLE_SCHOLAR_URL = 'http://scholar.google.com'
    SCRAPE_SPACE_SECONDS = (1, 2)  # initial codes 20-40
    SCRAPE_SPACE_SECONDS_BIG = (400, 720)  # initial codes 20-40
    UA = [
        'Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.9.2.9) Gecko/20100913 Firefox/3.6.9',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0',
        'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))',
        'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
        'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02',
        'Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62',
    ]

    import urllib2
    import numpy
    import time
    resp = False
    agent = UA[numpy.random.randint(0, len(UA))]
    # Requests the HTML from Google Scholar
    wait = numpy.random.randint(*SCRAPE_SPACE_SECONDS)

    # print("## Waiting %d seconds before hitting link `%s'..." % (wait, link))
    # print("\t\t\t ## Waiting %d seconds before hitting link " % (wait))
    # time.sleep(wait)

    try:
        # print("## Using agent `%s' to request `%s'..." % (agent, link))
        req = urllib2.Request(url=link, headers={'User-Agent': agent})
        hdl = urllib2.urlopen(req)
        #ACCESS_COUNTER = ACCESS_COUNTER + 1
        # print ACCESS_COUNTER
        resp = hdl.read()
    except urllib2.HTTPError as e:
        print("**Error HTTP** while fetching `%s'. AccessCounter: " % (link))
        print e
        wait2 = numpy.random.randint(*SCRAPE_SPACE_SECONDS_BIG)
        print("++++++++++++++TAKING A LONG SLEEP (%d ) ============== " %
              wait2)
        time.sleep(wait)
        req = urllib2.Request(url=link, headers={'User-Agent': agent})
        hdl = urllib2.urlopen(req)
        #ACCESS_COUNTER = ACCESS_COUNTER + 1
        # print ACCESS_COUNTER
        resp = hdl.read()
    except urllib2.URLError as e:
        print("**Error URL** while fetching `%s'. AccessCounter: " % (link))
        print e
        wait2 = numpy.random.randint(*SCRAPE_SPACE_SECONDS_BIG)
        print("++++++++++++++TAKING A LONG SLEEP (%d ) ============== " %
              wait2)
        time.sleep(wait)
        req = urllib2.Request(url=link, headers={'User-Agent': agent})
        hdl = urllib2.urlopen(req)
        #ACCESS_COUNTER = ACCESS_COUNTER + 1
        # print ACCESS_COUNTER
        resp = hdl.read()
    return resp
