# main.py

import json
import feedparser
import hashlib
import base64
from datetime import datetime
from pathlib import Path
import sys
from html_builder import build_index_html

feeds_path = Path(__file__).resolve().parent.parent / "feeds"
# From inside src/main.py
output_file = Path(__file__).resolve().parent.parent / "index.html"

# --- Utility Functions ---

def generate_uniqueid(url):
    sha256_hash = hashlib.sha256(url.encode('utf-8')).digest()
    base64_hash = base64.urlsafe_b64encode(sha256_hash).decode('utf-8').rstrip('=')
    return base64_hash

# --- Core Functions ---

def load_feeds(feeds_dir):
    all_feeds = []
    source_map = {}

    for file in feeds_dir.glob("*.json"):
        if file.is_file():
            try:
                with open(file, "r", encoding="utf-8") as f:
                    feeds = json.load(f)
            except json.JSONDecodeError as e:
                print(f"❌ {file.name} is not a valid JSON file.")
                if "Expecting property name enclosed in double quotes" in str(e):
                    print(f"Hint: {file.name} has a key that’s missing double quotes. Wrap all property names in double quotes.")
                elif "Expecting value" in str(e):
                    print(f"Hint: {file.name} may have a trailing comma. Delete any commas at the end of the list or object.")
                else:
                    print(f"Details: {e}")
                sys.exit(1)
            except Exception as e:
                print(f"❌ Could not read {file.name}: {e}")
                sys.exit(1)

            if not isinstance(feeds, list):
                print(f"❌ {file.name} must contain a list of feed entries, but something else was found.")
                sys.exit(1)

            for feed in feeds:
                source_map[id(feed)] = file.name
            all_feeds.extend(feeds)

    if not all_feeds:
        print("❌ No valid feeds found. Make sure your files are in /feeds and contain lists of feed entries.")
        sys.exit(1)

    return all_feeds, source_map

def validate_feeds(feeds, source_map=None):
    """
    Validates a combined list of feed entries.
    Optionally accepts a source_map dict: {feed_id: filename} for error tracking.
    """
    errors_found = False

    for idx, feed in enumerate(feeds):
        if not isinstance(feed, dict):
            print(f"ERROR: Feed entry {idx} is not a JSON object.")
            errors_found = True
            continue

        source_file = source_map.get(id(feed), "unknown file") if source_map else "unknown source"

        missing_fields = [field for field in ("source", "url", "uniqueid") if field not in feed]
        if missing_fields:
            print(f"ERROR: Missing fields in entry {idx} from {source_file}: {', '.join(missing_fields)}")
            errors_found = True
            continue

        expected_uniqueid = generate_uniqueid(feed["url"])
        if feed["uniqueid"] != expected_uniqueid:
            print(f"ERROR: Incorrect uniqueid in '{feed['source']}' from {source_file}. Expected: {expected_uniqueid}")
            errors_found = True

    if errors_found:
        print("❌ Feed validation failed. Please fix the above issues (common cause: trailing comma).")
        sys.exit(1)
    else:
        print("✅ All feeds validated successfully.")

def fetch_articles(feeds):
    articles = []
    for feed in feeds:
        parsed_feed = feedparser.parse(feed["url"])
        for entry in parsed_feed.entries:
            published = ""
            if hasattr(entry, "published"):
                published = entry.published
            elif hasattr(entry, "updated"):
                published = entry.updated

            link = entry.link if hasattr(entry, "link") else ""
            title = entry.title if hasattr(entry, "title") else "No Title"

            articles.append({
                "date": published,
                "source": feed["source"],
                "source_id": feed["uniqueid"],
                "title": title,
                "link": link
            })
    return articles

# --- Main Execution ---

def main():
    feeds, source_map = load_feeds(feeds_path)
    validate_feeds(feeds, source_map)
    articles = fetch_articles(feeds)

    html_content = build_index_html(articles, feeds)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ {output_file} generated successfully with {len(articles)} articles.")

if __name__ == "__main__":
    main()
