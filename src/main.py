from pathlib import Path
from feed_loader import load_feeds
from feed_validator import validate_feeds
from article_fetcher import fetch_articles
from html_builder import build_index_html

feeds_path = Path(__file__).resolve().parent.parent / "feeds"
output_file = Path(__file__).resolve().parent.parent / "index.html"

def write_index_file_txt(feeds_dir):
    index_path = Path(feeds_dir) / "index.txt"
    files = sorted(
        [str(f.relative_to(feeds_dir)) for f in Path(feeds_dir).glob("*.json")
         if f.is_file() and f.name not in {"index.json", "index.txt"}]
    )
    with open(index_path, "w", encoding="utf-8") as f:
        for filename in files:
            f.write(f"feeds/{filename}\n")
    print(f"✅ Wrote text index file: {index_path}")

def main():
    feeds, source_map = load_feeds(feeds_path)
    validate_feeds(feeds, source_map)
    write_index_file_txt(feeds_path)
    articles = fetch_articles(feeds)
    html = build_index_html(articles, feeds)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ {output_file} generated successfully with {len(articles)} articles.")

if __name__ == "__main__":
    main()
