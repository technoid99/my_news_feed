# Personal News Feed Generator

Create your own customisable news feed website using simple RSS sources — automatically updated every day — hosted on GitHub Pages!

This tool is designed for **anyone with a GitHub account**, no programming required beyond basic GitHub skills.

---

## 📌 What This Project Does

- Displays the latest articles from RSS feeds you choose.
- Lets you filter by:
  - **News source**
  - **Publication time** (past 24h, 48h, 7 days, or all time)
  - **Keyword search** (supports AND, OR, and "quoted phrases")
- Automatically updates itself **every morning**.
- Hosted for free on **GitHub Pages** — no servers needed.
- You stay in control: choose your sources, update anytime.

---

## 🚀 How to Set Up Your Own News Feed

1. **Fork or Copy This Repository**

   - Click the **Fork** button at the top right of this page, or
   - Create a new repository and copy the files manually.

2. **Rename Your Repository (Optional)**

   - You can name your repo anything you like, for example:  
     `my_news_feed` or `daily-news-reader`.

3. **Enable GitHub Pages**

   - Go to **Settings** → **Pages**.
   - Under \"Source\", select the branch (usually `main`) and root (`/`).
   - GitHub will generate a URL like:  
     `https://your-username.github.io/your-repository-name`

4. **Customise Your News Sources**

   - Open the `config.html` page in your repository.
   - Edit, add, or remove RSS feeds using the easy web editor.
   - Copy the updated `feeds.json` back into your GitHub repository (replace the old file).

5. **Automatic Daily Updates**

   - GitHub Actions will run every morning at **6AM AEST** (Australia Eastern Standard Time).
   - It will pull the latest articles and update your `index.html` automatically.

6. **View Your Personal News Feed**

   - Go to your GitHub Pages link and enjoy your customised news feed!

---

## 🛠 Requirements

- A GitHub account.

No servers.  
No coding beyond basic file editing.  
No installations.  
Just GitHub + RSS!

---

## ⚙️ How It Works (Under the Hood)

- `main.py` pulls articles from your selected RSS feeds using Python and `feedparser`.
- It generates an `index.html` page listing all articles.
- A GitHub Actions workflow (`update_feed.yml`) runs `main.py` automatically every day.
- Changes are committed back to your repository if anything new appears.
- GitHub Pages serves your latest news to the world.

---

## 💡 Tips

- Bookmark your feed and customise filters (source selection, keywords, time range) — they are saved in the URL!
- Add niche topics (e.g., science, regional news, personal interests).
- Remove or add feeds anytime by editing `feeds.json`.

---

## 🤔 Why This Project?

Today’s news feeds are cluttered and controlled by algorithms.  
**This project lets you take back control.**  
Select only the topics and sources you trust.  
No ads. No tracking. Just the news you want, updated daily.

---

## 📝 License

Free to use, copy, modify, or redistribute.

---
