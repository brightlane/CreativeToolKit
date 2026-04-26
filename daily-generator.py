from datetime import datetime
import random
import os

# YOUR AFFILIATE LINK (Wondershare LinkConnector)
affiliate_url = "https://www.linkconnector.com/ta.php?lc=007949048603004532&atid=WondershareWeb"

# SEO keyword bank (rotate daily)
keywords = [
    "best video editing software 2026",
    "easy video editing for beginners",
    "Wondershare Filmora review",
    "PDFelement PDF editor guide",
    "cheap alternative to Adobe Premiere",
    "video editing tools for YouTube",
    "AI video editing software",
    "creative software for content creators"
]

# Blog topics
topics = [
    "Why Wondershare is the Best Tool for Creators",
    "How to Edit Videos Faster Using Filmora",
    "Best Tools for YouTube Growth in 2026",
    "Wondershare vs Adobe: Full Breakdown",
    "Beginner Guide to Video Editing Software",
    "AI Tools Changing Content Creation"
]

def generate_blog():
    date = datetime.now().strftime("%Y-%m-%d")
    keyword = random.choice(keywords)
    topic = random.choice(topics)

    blog = f"""<!DOCTYPE html>
<html>
<head>
  <title>{topic} | Daily Creative Tools Guide</title>
  <meta name="description" content="{keyword} guide and tutorial. Learn tools and software for creators.">
</head>

<body style="font-family:Arial; max-width:900px; margin:auto;">

<h1>{topic}</h1>

<p>
Today’s focus keyword: <strong>{keyword}</strong>
</p>

<p>
Wondershare provides powerful tools for video editing, PDF management, and content creation.
</p>

<h2>Why This Matters</h2>
<p>
Creators need fast, simple tools to produce content efficiently. Wondershare helps reduce editing time and improves output quality.
</p>

<h2>Top Recommendation</h2>

<p>
👉 <a href="{affiliate_url}">Try Wondershare Tools Here</a>
</p>

<h2>Key Benefits</h2>
<ul>
  <li>Beginner-friendly editing tools</li>
  <li>AI-powered enhancements</li>
  <li>Fast export for social media</li>
</ul>

<p>
👉 <a href="{affiliate_url}">Start Using Wondershare Now</a>
</p>

</body>
</html>
"""

    os.makedirs("blog", exist_ok=True)

    file_path = f"blog/blog-{date}.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(blog)

    print("Generated:", file_path)

if __name__ == "__main__":
    generate_blog()
