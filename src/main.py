from pathlib import Path
from feed_loader import load_feeds
from feed_validator import validate_feeds
from article_fetcher import fetch_articles
from html_builder import build_index_html

feeds_path = Path(__file__).resolve().parent.parent / "feeds"
output_file = Path(__file__).resolve().parent.parent / "index.html"

def main():
    feeds, source_map = load_feeds(feeds_path)
    validate_feeds(feeds, source_map)
    articles = fetch_articles(feeds)
    html = build_index_html(articles, feeds)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ {output_file} generated successfully with {len(articles)} articles.")

if __name__ == "__main__":
    main()
