import hashlib
import base64
import sys

def generate_uniqueid(url):
    sha256_hash = hashlib.sha256(url.encode('utf-8')).digest()
    return base64.urlsafe_b64encode(sha256_hash).decode('utf-8').rstrip('=')

def validate_feeds(feeds, source_map=None):
    errors_found = False

    for idx, feed in enumerate(feeds):
        source_file = source_map.get(id(feed), "unknown file") if source_map else "unknown source"

        if not isinstance(feed, dict):
            print(f"ERROR: Feed entry {idx} in {source_file} is not a JSON object.")
            errors_found = True
            continue

        missing_fields = [k for k in ("source", "url", "uniqueid") if k not in feed]
        if missing_fields:
            print(f"ERROR: Entry {idx} in {source_file} is missing fields: {', '.join(missing_fields)}")
            errors_found = True
            continue

        expected = generate_uniqueid(feed["url"])
        if feed["uniqueid"] != expected:
            print(f"ERROR: Incorrect uniqueid in '{feed['source']}' from {source_file}. Expected: {expected}")
            errors_found = True

    if errors_found:
        print("❌ Feed validation failed.")
        sys.exit(1)
    else:
        print("✅ All feeds validated successfully.")
