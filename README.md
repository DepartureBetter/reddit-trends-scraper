# 🔍 Reddit Trends Scraper

This project is a lightweight tool to extract daily trend data from any subreddit using Reddit’s public JSON endpoints — ideal for surfacing insights, feeding LLMs, or automating topic discovery.

---

## 🚀 Use Case

Reddit contains real-time conversations around emerging tools, AI breakthroughs, and niche communities — but manually scrolling through threads is slow and inconsistent.

This tool helps:
- Growth teams discover what's trending in user conversations
- AI engineers feed contextual prompts into LLMs
- Founders and researchers analyze what people *actually care about*

---

## 🧠 What It Does

- Connects to any subreddit’s `/top/.json` endpoint (e.g., `r/stocks`, `r/technology`)
- Extracts:
  - Post titles  
  - Upvote counts  
  - Comment counts  
  - Post URLs
- Stores results in a clean `pandas` DataFrame
- Exports to `.csv` for downstream use (analytics, LLMs, dashboards, etc.)

---

## 🛠 Stack

- `requests` — to fetch the subreddit feed  
- `pandas` — for structuring and cleaning data  
- `json` — to parse the Reddit response  
- `time` — for polite delay handling  
- `argparse` *(optional)* — to allow CLI control for subreddit + time range

---

## 📦 Example Output

```csv
Title,Upvotes,Comments,URL
"New open-source LLM beats GPT-3.5", 1234, 211, https://reddit.com/r/LocalLLaMA/post/xyz
"Is fine-tuning dead?", 985, 100, https://reddit.com/r/LocalLLaMA/post/abc
...
