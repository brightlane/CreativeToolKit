from datetime import datetime
import random
import os

affiliate_url = "https://www.linkconnector.com/ta.php?lc=007949048603004532&atid=WondershareWeb"

hashtags = [
    "#Wondershare",
    "#Filmora",
    "#VideoEditing",
    "#ContentCreator",
    "#YouTubeGrowth",
    "#PDFTools",
    "#AItools",
    "#CreatorEconomy"
]

twitter_messages = [
    "🔥 Create professional videos in minutes with Wondershare Filmora",
    "🎬 The easiest way to edit YouTube videos in 2026 is here",
    "🚀 Stop overcomplicating editing — try Wondershare tools today",
    "💡 Beginners are growing fast using Filmora video editor",
    "📈 Level up your content creation workflow instantly"
]

facebook_messages = [
    "Create stunning videos and documents with Wondershare tools designed for creators.",
    "Wondershare makes video editing and PDF management simple for everyone.",
    "Grow your content faster using beginner-friendly creative software.",
    "Professional results without professional complexity — that’s Wondershare."
]

pinterest_titles = [
    "Best Video Editing Software for Beginners (2026 Guide)",
    "Easy Tools for YouTube Growth and Content Creation",
    "Wondershare Filmora Editing Workflow Explained",
    "Simple PDF Editing Tools for Students and Creators"
]

def generate_posts():
    date = datetime.now().strftime("%Y-%m-%d")

    tagset = " ".join(random.sample(hashtags, 3))

    twitter = f"""
{random.choice(twitter_messages)}

👉 {affiliate_url}

{tagset}
"""

    facebook = f"""
🔥 Wondershare Creative Tools Update

{random.choice(facebook_messages)}

👉 Start here: {affiliate_url}

{tagset}
"""

    pinterest = f"""
Title: {random.choice(pinterest_titles)}

Description:
Learn how Wondershare tools simplify video editing, PDF work, and content creation.

👉 {affiliate_url}
"""

    os.makedirs("social", exist_ok=True)

    with open(f"social/{date}-twitter.txt", "w", encoding="utf-8") as f:
        f.write(twitter)

    with open(f"social/{date}-facebook.txt", "w", encoding="utf-8") as f:
        f.write(facebook)

    with open(f"social/{date}-pinterest.txt", "w", encoding="utf-8") as f:
        f.write(pinterest)

    print("Social posts generated:", date)

if __name__ == "__main__":
    generate_posts()
