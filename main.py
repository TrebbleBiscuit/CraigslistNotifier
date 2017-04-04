#term = raw_input("Enter Search Term: ")
term = "nintendo"

import feedparser
craigslist_nintendo_url = "https://cincinnati.craigslist.org/search/sss?format=rss&query=" + term

rssfeed = feedparser.parse( craigslist_nintendo_url )

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
