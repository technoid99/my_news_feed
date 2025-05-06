from datetime import datetime
from email.utils import parsedate_to_datetime
from jinja2 import Environment, FileSystemLoader

def build_index_html(articles, feeds):
    now_utc = datetime.utcnow().strftime("%d %b %Y, %H:%M UTC")

    # Preprocess articles to format display date
    for article in articles:
        try:
            dt = parsedate_to_datetime(article["date"])
            article["display_date"] = dt.strftime("%a %d %b %y")
        except Exception:
            article["display_date"] = article["date"] or ""

        article["row_class"] = "missing-date" if not article["date"] else ""

    # Set up Jinja2 environment (assuming template file is in the same directory)
    env = Environment(loader=FileSystemLoader("./src"))
    template = env.get_template("index_template.html")

    # Render and return HTML
    return template.render(
        generated_time=now_utc,
        articles=articles,
        feeds=feeds
    )
