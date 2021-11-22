import feedparser
import requests

def get_link(url, today, list_link):
    rss = requests.get(url).text
    parsed_rss = feedparser.parse(rss)
    entry_rss = parsed_rss['entries']
    for entry in entry_rss:
        pubDate = str(entry['updated_parsed'][0]) + str(entry['updated_parsed'][1]) + str(entry['updated_parsed'][2])
        if today == pubDate:
            list_link.append(entry['link'])        

