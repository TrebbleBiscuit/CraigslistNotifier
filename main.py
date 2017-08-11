import feedparser
import re

terms = ["nintendo", "microsoft"]
entries = []
allentries = []

for term in terms:
    craigslist_search_url = "https://cincinnati.craigslist.org/search/sss?format=rss&query=" + term
    rssfeed = feedparser.parse( craigslist_search_url )
    for x in rssfeed["entries"]:
        for y in x:
            if y == "summary" or y == "link":
                clean = re.sub('<a class=.*?</a>', '[Contact Info]',
                               x[y])
                entries.append(clean)
            elif y == "title":
                posttitle = x[y]
                entries.append(posttitle.replace('&#x0024;',
                                                 '- Price: '))
            elif y == "updated":
                posttitle = x[y]
                posttitle = posttitle.replace('T', ' - ')
                posttitle = posttitle.replace('-05:00', '')
                entries.append(posttitle)
        allentries.append(entries)
        entries = []

allentries.sort(key=lambda x: x[1], reverse=True)  # Sorts by time
for x in range(len(allentries)-1, -1, -1):
    for y in range(0, len(allentries[x])):
        try:
            print allentries[x][y]
        except UnicodeEncodeError:
            break  # I don't think passing these posts over is a problem
    print ""
