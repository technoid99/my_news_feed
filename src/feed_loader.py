import json
import sys
from pathlib import Path

def load_feeds(feeds_dir):
    all_feeds = []
    source_map = {}

    for file in Path(feeds_dir).glob("*.json"):
        if file.is_file():
            try:
                with open(file, "r", encoding="utf-8") as f:
                    feeds = json.load(f)
            except json.JSONDecodeError as e:
                print(f"❌ {file.name} is not a valid JSON file.")
                if "Expecting property name enclosed in double quotes" in str(e):
                    print(f"Hint: {file.name} has a key that’s missing double quotes.")
                elif "Expecting value" in str(e):
                    print(f"Hint: {file.name} may have a trailing comma.")
                else:
                    print(f"Details: {e}")
                sys.exit(1)
            except Exception as e:
                print(f"❌ Could not read {file.name}: {e}")
                sys.exit(1)

            if not isinstance(feeds, list):
                print(f"❌ {file.name} must contain a list of feed entries.")
                sys.exit(1)

            for feed in feeds:
                source_map[id(feed)] = file.name
            all_feeds.extend(feeds)

    if not all_feeds:
        print("❌ No valid feeds found in /feeds.")
        sys.exit(1)

    return all_feeds, source_map
