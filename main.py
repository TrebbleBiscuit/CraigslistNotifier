import feedparser

terms = ["nintendo"]

for term in terms:
    craigslist_search_url = "https://cincinnati.craigslist.org/search/sss?format=rss&query=" + term
    rssfeed = feedparser.parse( craigslist_search_url )
    for x in rssfeed["entries"]:
    #    print x
        for y in x:
            if y == "summary" or y == "link":
    #            print "TITLE: " + y
                print x[y]
            elif y == "title":
                posttitle = x[y]
                print posttitle.replace('&#x0024;', '- Price: ')
            elif y == "updated":
                posttitle = x[y]
                posttitle = posttitle.replace('T', ' - ')
                posttitle = posttitle.replace('-05:00', '')
                print posttitle
        print ""


# This program just shoves all the listings on top of each other, I need to make them sort by time
