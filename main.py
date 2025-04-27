import json
import feedparser
import hashlib
import base64
from datetime import datetime
from pathlib import Path
import sys

# --- CONFIGURATION ---
FEEDS_FILE = "feeds.json"
OUTPUT_FILE = "index.html"
MAX_ARTICLES_PER_FEED = None  # None = unlimited

# --- FUNCTIONS ---

def generate_uniqueid(url):
    sha256_hash = hashlib.sha256(url.encode('utf-8')).digest()
    base64_hash = base64.urlsafe_b64encode(sha256_hash).decode('utf-8').rstrip('=')
    return base64_hash

def validate_feeds(feeds):
    for feed in feeds:
        if "source" not in feed or "url" not in feed or "uniqueid" not in feed:
            print(f"ERROR: Feed entry missing required fields: {feed}")
            sys.exit(1)
        expected_uniqueid = generate_uniqueid(feed["url"])
        if feed["uniqueid"] != expected_uniqueid:
            print(f"ERROR: uniqueid mismatch for feed '{feed['source']}'. Expected {expected_uniqueid}.")
            sys.exit(1)

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
                "title": title,
                "link": link,
                "source_id": feed["uniqueid"]
            })
            if MAX_ARTICLES_PER_FEED and len(articles) >= MAX_ARTICLES_PER_FEED:
                break
    return articles

def build_html(articles):
    now_utc = datetime.utcnow().strftime("%d %b %Y, %H:%M UTC")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>My News Feed</title>
<style>
  body {{ font-family: Arial, sans-serif; margin: 40px; }}
  table {{ border-collapse: collapse; width: 100%; }}
  th, td {{ text-align: left; padding: 8px; border-bottom: 1px solid #ddd; }}
  th {{ background-color: #f2f2f2; cursor: pointer; }}
  .missing-date td:first-child {{ color: gray; }}
  .date-filter, .filter-row {{ margin-bottom: 20px; }}
  a {{ color: #1a0dab; text-decoration: none; }}
</style>
<script>
let currentSort = {{ col: 0, asc: false }};
function sortTable(colIndex) {{
    const tbody = document.querySelector('#newsTable tbody');
    let asc = currentSort.col === colIndex ? !currentSort.asc : false;
    currentSort = {{ col: colIndex, asc: asc }};
    const rows = Array.from(tbody.rows);
    rows.sort((a, b) => {{
        let valA = a.cells[colIndex].textContent.trim();
        let valB = b.cells[colIndex].textContent.trim();
        if (colIndex === 0) return asc ? new Date(valA) - new Date(valB) : new Date(valB) - new Date(valA);
        return asc ? valA.localeCompare(valB) : valB.localeCompare(valA);
    }});
    tbody.innerHTML = '';
    rows.forEach(r => tbody.appendChild(r));
}}
document.addEventListener('DOMContentLoaded', () => {{
    sortTable(0);
}});
</script>
</head>
<body>
<h2>My News Feed</h2>
<p><em>Page generated on {now_utc}</em></p>
<table id="newsTable">
<thead>
<tr>
  <th onclick="sortTable(0)">Date ▲▼</th>
  <th onclick="sortTable(1)">Source ▲▼</th>
  <th>Title</th>
</tr>
</thead>
<tbody>
"""

    for article in articles:
        date = article["date"]
        date_display = date if date else ""
        row_class = " class='missing-date'" if not date else ""
        html += f"<tr{row_class}><td>{date_display}</td><td>{article['source']}</td><td><a href='{article['link']}' target='_blank'>{article['title']}</a></td></tr>\n"

    html += """
</tbody>
</table>
</body>
</html>"""

    return html

# --- MAIN EXECUTION ---

def main():
    if not Path(FEEDS_FILE).exists():
        print(f"ERROR: {FEEDS_FILE} not found.")
        sys.exit(1)

    with open(FEEDS_FILE, "r", encoding="utf-8") as f:
        feeds = json.load(f)

    validate_feeds(feeds)
    articles = fetch_articles(feeds)
    html = build_html(articles)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ {OUTPUT_FILE} generated successfully with {len(articles)} articles.")

if __name__ == "__main__":
    main()
