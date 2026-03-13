import feedparser
import json
import time
from datetime import datetime

FEEDS = {
      'Technology': 'https://news.google.com/rss/search?q=technology&hl=en-US&gl=US&ceid=US:en',
      'AI': 'https://news.google.com/rss/search?q=artificial+intelligence&hl=en-US&gl=US&ceid=US:en',
      'World': 'https://news.google.com/rss/search?q=world&hl=en-US&gl=US&ceid=US:en'
}

def fetch_feeds():
      news_data = {}
      for category, url in FEEDS.items():
                print(f"[{datetime.now()}] Fetching {category}...")
                feed = feedparser.parse(url)
                news_data[category] = []
                for entry in feed.entries[:5]:
                              news_data[category].append({
                                                'title': entry.title,
                                                'link': entry.link,
                                                'published': entry.published
                              })

            with open('news_data.json', 'w', encoding='utf-8') as f:
                      json.dump(news_data, f, ensure_ascii=False, indent=4)
                  print(f"[{datetime.now()}] Synchronization complete.")

if __name__ == "__main__":
      fetch_feeds()
