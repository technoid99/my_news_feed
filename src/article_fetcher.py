import feedparser

def fetch_articles(feeds):
    articles = []
    for feed in feeds:
        parsed = feedparser.parse(feed["url"])
        for entry in parsed.entries:
            published = getattr(entry, "published", getattr(entry, "updated", ""))
            title = getattr(entry, "title", "No Title")
            link = getattr(entry, "link", "")

            articles.append({
                "date": published,
                "source": feed["source"],
                "source_id": feed["uniqueid"],
                "title": title,
                "link": link
            })
    return articles
