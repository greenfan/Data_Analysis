import feedparser
import time
from datetime import datetime

url = "https://zapier.com/engine/rss/7955983/OpenScienceDailyRSS"
dgtw = feedparser.parse(url)

print(len(dgtw.entries))


todays_date = format(datetime.today().day).zfill(2)
print(todays_date)


for i in range(5):

    entry = dgtw.entries[i]
    pdate = entry.published

    if todays_date in pdate:
        print(entry.author)
    time.sleep(2)

