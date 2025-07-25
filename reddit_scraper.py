import requests
import pandas as pd
import time

SUBREDDIT = "stocks"            # Change this to any subreddit
TIME_FILTER = "day"             # 'hour', 'day', 'week', etc.
LIMIT = 50                      # Number of posts
OUTPUT_CSV = f"reddit_{SUBREDDIT}_trends.csv"

url = f"https://www.reddit.com/r/{SUBREDDIT}/top/.json?t={TIME_FILTER}&limit={LIMIT}"
headers = {'User-agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    raise Exception(f"Error: {response.status_code}")

data = response.json()
posts = data["data"]["children"]

records = []
for post in posts:
    post_data = post["data"]
    records.append({
        "title": post_data["title"],
        "upvotes": post_data["ups"],
        "comments": post_data["num_comments"],
        "author": post_data["author"],
        "permalink": f"https://www.reddit.com{post_data['permalink']}",
        "created_utc": time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(post_data["created_utc"]))
    })

df = pd.DataFrame(records)
df.to_csv(OUTPUT_CSV, index=False)
print(f"Saved {len(df)} posts to {OUTPUT_CSV}")
