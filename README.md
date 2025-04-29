# Personal News Feed Generator

Create your own customisable news feed website using simple RSS sources — automatically updated every day — hosted on GitHub Pages!

This tool is designed for **anyone with a GitHub account**, no programming required beyond basic GitHub skills.

Click here to see a sample feed: [My news feed](https://technoid99.github.io/my_news_feed/index.html)
This is the location of the original Github repository [template](https://github.com/technoid99/my_news_feed/).

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

# ✅ Quick Setup Instructions:

| Step | Action |
|:-----|:-------|
| 1 | Click **"Use this template"** |
| 2 | Create your own repository |
| 3 | Enable **GitHub Pages** (repository Settings > Pages (left menu) > branch: main, root folder > Save button) |
| 4 | Customize your `feeds.json` | [feeds.json Config tool](https://technoid99.github.io/my_news_feed/config.html)
| 5 | Enjoy your personal news feed! 🚀 |

---

# 🚀 Detailed Setup Instructions

### 1. Make Your Own Copy

- Click the green **"Use this template"** button at the top of this page.
- Choose **"Create a new repository"**.
- Give your repository a name (e.g., `my_news_feed`).
- Click **Create repository**.

✅ You now have your own personal copy!

---

### 2. Customize Your News Sources

- Before you first publish, you can use this [feeds.json config tool](https://technoid99.github.io/my_news_feed/config.html) to build your ```feeds.json``` file content. After you publish use your own config tool (```https://your-username.github.io/your-repository-name/config.html```) as it'll pull in your existing feeds.json file so you can better edit it.
- Use the simple web form to edit, add, or remove RSS feeds.
- After making changes, **copy** the updated JSON text.
- Then:
  - Click `feeds.json` in your repository file listing
  - Click the ✏️ **edit button**.
  - Paste your updated feeds.json.
  - Save the changes.

✅ Now you control exactly what news you see!

---

### 3. Enable GitHub Pages / Publish!

- In your new repository, go to **Settings**.
- Scroll down to **Pages**.
- Under **"Source"**, select:
  - **Branch:** `main`
  - **Folder:** `/ (root)`
- Click **Save**.

✅ After a few seconds, GitHub will give you a live web link to your personal news feed!

---

### 4. How Updates Work

- Every morning at **6AM AEST (Australia Eastern Standard Time)**,
  GitHub Actions will automatically update your news feed.
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

- Bookmark your feed with customised filters (source selection, keywords, time range) — they are saved in the URL!
- Add niche topics (e.g., science, regional news, personal interests).
- Remove or add feeds anytime by editing `feeds.json`.

---

## 💡 Advanced Tips

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

- Check the About page on your news feed site.
- Open an Issue in this repository if you get stuck.
- Explore GitHub documentation if you're completely new!

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
