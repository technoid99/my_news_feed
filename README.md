# Personal News Feed Generator

This template allows you to create your own customisable news feed website from simple RSS sources.
After setting up your sources and activating your Github Pages page (your news feed website), your news feed website will update every day.

This tool is designed for **anyone with a GitHub account**, no programming required.

Click here to see a sample feed: [My news feed](https://technoid99.github.io/my_news_feed/index.html)
This is the location of the original Github repository [template](https://github.com/technoid99/my_news_feed/).

This repo is currently under construction. Don't copy it if the following status is not a green 'passing'

[![Update News Feed Daily](https://github.com/technoid99/my_news_feed/actions/workflows/update_feed.yml/badge.svg?branch=main)](https://github.com/technoid99/my_news_feed/actions/workflows/update_feed.yml)

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

## 🛠 Requirements

- A GitHub account.

No servers.  
No coding beyond basic file editing.  
No installations.  
Just GitHub + RSS!

---

# ✅ Quick Setup Instructions:

| Step | Action |
|:-----|:-------|
| 1 | Click **"Use this template"** |
| 2 | Create your own repository |
| 3 | Enable **GitHub Pages** (repository Settings > Pages (left menu) > Source: GitHub Actions) |
| 4 | Go make yourself a coffee ☕ or tea 🫖
| 5 | Go to your new news feed webpage `https://yourusername.github.io/your-repository-name/config.html`
| 6 | Use the Config tool (top right hand corner) to customise your RSS feed sources content
| 7 | Paste the content into your `feeds.json` or relevant file. (Click < > Code in the top left corner to get back to your repository file system)
| 8 | Once you modify a json file in the feeds/ directory, it will automatically update the website. Within 1-2 minutes.
| 9 | Drink your beverage ☕ 🫖
| 10 | Enjoy your personal news feed!  🚀 

---

# 🚀 Detailed Setup Instructions

### 1. Make Your Own Copy

- Click the green **"Use this template"** button at the top of this page.
- Choose **"Create a new repository"**.
- Give your repository a name (e.g., `my_news_feed`).
- Click **Create repository**.

✅ You now have your own personal copy!

---

### 2. Enable GitHub Pages

- In your new repository, go to **Settings**.
- Click **Pages**. (left menu)
- Under **"Build and deployment Source"**, select:
  - **Github Actions**
- Click **Save**.

✅ After a few seconds, GitHub will give you a live web link to your personal news feed!

---

### 3. Setup Your News Sources

- Go to your newly published Github Pages page (`https://your-username.github.io/your-repository-name`)
- Click Config in the top right hand corner.
- Use the simple web form to add or remove RSS feeds.
- After making changes, **copy** the updated JSON text by clicking the copy JSON button
- Then:
  - Go to your Gitub repository
  - Click <>Code to get back to your file system
  - Click `feeds.json` or the corresponding json file you were editing in your repository file listing
  - Click the ✏️ **edit button**.
  - Delete all content in that file
  - Paste your updated feeds.json
  - Click `Commit changes...` green button.

✅ Now you control exactly what news you see!

---

💡 Looking for RSS sources?
* use advance search keyword `feeds:` in Bing Search [example](https://www.bing.com/search?q=feed%3A+%22technology), or Yahoo or DuckDuckGo
* [Google News](https://news.google.com). Run your search then in the URL add `rss/` after the google.com. Use that URL as your RSS source URL.
* run a basic Google search for 'RSS news feeds'
* Create your own through [RSSEverything](https://rsseverything.com), [PolitePol](https://politepol.com)

## 💡 Tips for Google News

### Add a Google News search as an RSS feed

1. Create a bookmarklet
a. Copy this javascript code that obtains the exact search query and makes it an RSS feed ```javascript:(function(){let url=window.location.href;if(url.includes('news.google.com/')){url=url.replace('news.google.com/','news.google.com/rss/');navigator.clipboard.writeText(url).then(()=>alert('RSS URL copied to clipboard!')).catch(err=>console.error('Copy failed',err));}else{alert('Not a Google News page.');}})();```
b. Create a new bookmark in your browser. (I like to save it to Bookmarks bar for easy access)
c. Paste it into the URL field of the bookmark.
d. Name it something like "Get Google News RSS".

2. Manually search using Google News
a. Go to [https://news.google.com/](https://news.google.com/)
b. Run your news search query or click on a Topic heading.
c. While on your resulting Google News search page, click the bookmarklet. It will copy the RSS feed URL to your clipboard.

3. Go to your my_news_feed Config file or use [this one](https://technoid99.github.io/my_news_feed/config.html) from the template and use the copied URL as your RSS URL.
   
---

### 4. How Updates Work

- Every day 8pm UTC GitHub Actions will automatically update your news feed.
- You don't need to do anything — it refreshes itself!
- Note: if you wish to update outside of this schedule got to Actions (top menu) > "Update News Feed Daily" (left menu) > Run workflow dropdown (right side) > Run workflow.

---

### 5. View Your Personal News Feed

- Visit your GitHub Pages link (found in **Settings → Pages**).
- Use the source filter, time filter and keyword filter to your liking.
- Bookmark it for quick access! (yes, even with the filters!)

✅ You can filter articles by:
- Source
- Time range (24h, 48h, 7d, or all time)
- Keyword search (supports **AND**, **OR**, and **"quoted phrases"**) eg. (grapes OR berries) AND apples -bananas

💡 Tips
- Bookmark your feed with customised filters (source selection, keywords, time range) — they are saved in the URL!

---

## ⚙️ How It Works (Under the Hood)

- `main.py` pulls articles from your configured RSS feed sources in the /feeds folder using Python and `feedparser`.
- It generates an `index.html` page listing all articles.
- A GitHub Actions workflow (`update_feed.yml`) runs `main.py` automatically every day.
- Instead of committing changes to your repository, the site is built into a /public folder and uploaded as a GitHub Pages artifact.
- Deployment uses actions/deploy-pages@v4 and actions/upload-pages-artifact@v3, following GitHub’s modern deployment method.
- GitHub Pages serves your latest news to the world
  
---

## Troubleshooting

### The website doesn't update

1. Check Actions.
2. If `Update News Feed Daily` fails, click into it and see why.
3. Scroll to the end of the error message. If it says:
```json.decoder.JSONDecodeError: Illegal trailing comma before end of array: line 146 column 4 (char 5393) Error: Process completed with exit code 1.```
Then you've probably manually edited your feeds.json and left a comma at the end of the json file. Delete it and run the workflow again.

---

## 💡 Use Cases

### Individual

#### Researcher wanting to be up to date on the latest on various topics
1. put all interests in one feeds.json
2. publish the repository
3. visit the corresponding Github page
4. selectively check RSS feed source based on topic of interest and the time and keyword filter as desired.
5. Bookmark that exact URL.
6. Comeback daily (or per your scheduling) for updates

### Small enterprise with multiple users

1. Admin manages all the feeds.json and individuals run a search based on their desires sources and filters.
2. Individual user bookmarks the URL to receive updates next time with their customised settings
3. Each individual user can use Config to add a new entry.
4. Paste the new entry Issues ticket for Admin to add to feeds.json

---

## 📚 Need Help?

- Open an Issue in this repository if you get stuck.
- Explore GitHub documentation if you're completely new!

---

## 🤔 Why This Project?

Getting news feeds via email clutters my inbox.
Select only the topics and sources you trust.  
No ads. No tracking. Just the news you want, updated daily.

---

## 📝 License

Free to use, copy, modify, or redistribute.

---
