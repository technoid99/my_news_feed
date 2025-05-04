# 📰 Personal News Feed Generator

Create your own daily news reader from any public RSS feeds — no coding or servers required.

---

## TL;DR

- ✅ Pick your sources  
- 🛠 Paste them into a config file  
- 🌐 GitHub Pages builds your feed  
- 🔁 Feed updates daily via GitHub Actions  
- 📱 Works on mobile  

See it in action: [News Feed Demo](https://technoid99.github.io/my_news_feed/index.html) 
[![](https://github.com/technoid99/my_news_feed/actions/workflows/update_feed.yml/badge.svg?branch=main)](https://technoid99.github.io/my_news_feed/index.html)

Source: [Template Repo](https://github.com/technoid99/my_news_feed)

---

## 👥 Who This Is For

This tool is designed for individuals who:

- Want to stay up to date on news, research, or niche topics  
- Prefer to choose their own sources  
- Want to avoid email newsletters, ad tracking, or social media platforms  
- Don’t know what RSS is (yet) :)

---

## ❓What’s RSS? 

RSS is a simple way to get new articles from your favourite websites.
- It stands for *Really Simple Syndication*
- Many news and research sites quietly offer RSS feeds
- This project uses those feeds to build your own personal news site

Examples:
- A Google News search result like `https://news.google.com/rss/search?q=cybersecurity`
- A blog like `https://example.com/rss`
- A WordPress website `https://example.com/feed`

No ads, no login, just headlines and links — all under your control.

---

## 🔍 What This Project Does

- Displays the latest articles from the feeds you choose
- Lets you filter by:
  - **News source**
  - **Time range** (24h, 48h, 7d, or all time)
  - **Keywords** (with AND, OR, and phrase support)
- Automatically updates **once per day** (8pm UTC)
- Fully hosted on **GitHub Pages**
- Mobile-friendly

---

## 🛠 Requirements

- A GitHub account
- Comfort with editing text files in GitHub’s web interface
- Public RSS feeds (not login-protected unless you want to reveal your password to the world!)

No installs. No backend. Just GitHub + a web browser.

---

## ✅ Quick Setup Guide

| Step | Action |
|------|--------|
| 1 | Click **"Use this template"** in GitHub (top right of this page) |
| 2 | Create your own repository (repo) |
| 3 | Enable **GitHub Pages** (Settings > Pages > Source: GitHub Actions) |
| 4 | Visit your feed: `https://yourusername.github.io/your-repo-name/config.html` |
| 5 | Use the Config form to build your feed list |
| 6 | Paste the JSON into your file (e.g. `feeds/feeds.json`) |
| 7 | Site updates automatically in 1–2 mins |
| 8 | Bookmark your filtered feed URL for reuse |

The [Detailed Setup Guide](https://github.com/technoid99/my_news_feed/wiki/Detailed-Setup-Guide) is located in the wiki.

---

## 📂 You Can Use Multiple Feed Files

You can keep several feed files in `/feeds/`. For example:

- `feeds/soccer.json`
- `feeds/cybersecurity.json`
- `feeds/recipes.json`

The config tool (`config.html`) helps you generate valid content for each one.

---

## 📊 System Overview

```text
+--------------+        +------------------+       +-------------------------+
| feeds/*.json | ----> | GitHub Actions   | --->  | index.html (Static Feed) |
+--------------+        | Runs daily       |       +-------------------------+
                        | Runs main.py     |
                        | Outputs HTML     |
                        +------------------+
```
---

---

## 💡 Advanced Tips (Moved to Wiki)

- [Finding RSS feeds using Google or Bing](https://github.com/technoid99/my_news_feed/wiki/Finding-RSS-Feeds)
- [How to convert Google News searches into RSS](https://github.com/technoid99/my_news_feed/wiki/Google-News-RSS-Bookmarklet)
- [Example feeds.json snippets](https://github.com/technoid99/my_news_feed/wiki/Example-Configs)

---

## ⚙️ How It Works (Under the Hood)

- `main.py` reads all JSON files in `/feeds/`
- It uses `feedparser` to pull latest articles
- Generates a single `index.html` listing articles
- GitHub Actions (`update_feed.yml`) runs daily
- GitHub Pages serves the result

---

## 🛠 Troubleshooting

### Site isn’t updating?

1. Go to the **Actions** tab  
2. Open the `Update News Feed Daily` run  
3. Check the error. Most common issue:

   ```
   JSONDecodeError: Illegal trailing comma
   ```

→ Remove the trailing comma in your `.json` config

---

## ✨ Use Cases

### 👩‍🎓 Researcher
- Track multiple sources on the same topic
- Filter results by time or keyword

### 👩‍💻 Curious Reader
- Stay updated without distractions
- Check once a day, just the headlines

---

## 📚 Need Help?

- Open an [Issue](https://github.com/technoid99/my_news_feed/issues)
- Explore the [Wiki](https://github.com/technoid99/my_news_feed/wiki)

---

## 📝 License

Free to use, modify, or share.
