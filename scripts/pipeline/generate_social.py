#!/usr/bin/env python3
"""
Generate social media content from the reviewed blog post.

Environment variables:
  GITHUB_TOKEN  - GitHub PAT for Models API access
  CRITIC_MODEL  - Model identifier
  PLATFORMS     - Comma-separated list (linkedin,twitter,reddit,reel,youtube)
"""
import json
import os
import glob
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
CRITIC_MODEL = os.environ.get("CRITIC_MODEL", "openai/gpt-4.1")
PLATFORMS = os.environ.get("PLATFORMS", "linkedin").split(",")
API_URL = "https://models.inference.ai.azure.com/chat/completions"

PLATFORM_PROMPTS = {
    "linkedin": """Create a LinkedIn post from this blog. Requirements:
- Plain text version + Unicode bold/italic version
- Hook with surprising data point (NOT "I wrote a blog")
- Numbered takeaways with data
- Clear CTA
- Wrap each version in -- START COPY -- / -- END COPY -- markers
- Include hashtags. Under 3000 characters""",

    "twitter": """Create a 10-12 tweet X/Twitter thread from this blog. Requirements:
- Each tweet under 280 characters
- Tweet 1: hook with shocking stat
- Final tweet: CTA + link placeholder
- Unicode bold/italic for emphasis
- Include standalone single-tweet summary at top""",

    "reddit": """Create a Reddit post from this blog. Requirements:
- Standard Markdown ONLY (no Unicode bold/italic)
- TL;DR at the top (4 bullet points max)
- Conversational, anti-promotional tone
- Blog link at end, not as primary CTA
- Suggest 3 subreddit-specific title variants""",

    "reel": """Create a 60-second reel/short video script from this blog. Requirements:
- Shot list table: Time | Visual | Voiceover | Text Overlay
- Screen recording notes
- Full voiceover script (~120 words)
- Captions for Instagram Reels/YouTube Shorts + LinkedIn Video
- ONE core message only. Text overlays: max 6-8 words per screen
- Thumbnail/cover frame description""",

    "youtube": """Create an 8-12 minute YouTube script from this blog. Requirements:
- Timed segments: Timestamp | Segment | Format
- Cold open hook (first 30 seconds)
- Visual cue references to existing PNGs
- CTA at end. Thumbnail concept suggestion""",
}

PLATFORM_FILES = {
    "linkedin": "content/linkedin-post.md",
    "twitter": "content/x-twitter-thread.md",
    "reddit": "content/reddit-post.md",
    "reel": "content/reel-script.md",
    "youtube": "content/youtube-script.md",
}


def call_model(system_prompt, user_content):
    model_name = CRITIC_MODEL.split("/")[-1] if "/" in CRITIC_MODEL else CRITIC_MODEL
    payload = json.dumps({
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        "max_tokens": 4096,
        "temperature": 0.5,
    }).encode()

    req = Request(API_URL, data=payload, method="POST", headers={
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json",
    })
    try:
        with urlopen(req) as resp:
            data = json.loads(resp.read())
            return data["choices"][0]["message"]["content"]
    except HTTPError as e:
        body = e.read().decode() if e.fp else ""
        print(f"API error {e.code}: {body}", file=sys.stderr)
        return f"[ERROR] API call failed: {e.code}"


def find_blog_post():
    candidates = glob.glob("content/*part*.md") + glob.glob("content/*blog*.md")
    candidates = [c for c in candidates if "strategy" not in c and "pipeline" not in c
                  and "linkedin" not in c and "reel" not in c and "reddit" not in c
                  and "twitter" not in c and "youtube" not in c and "reference" not in c
                  and "critic" not in c]
    if not candidates:
        return None
    return max(candidates, key=os.path.getmtime)


def main():
    blog_path = find_blog_post()
    if not blog_path:
        print("No blog post found. Skipping social generation.")
        return

    blog_content = Path(blog_path).read_text()
    print(f"Source blog: {blog_path}")
    print(f"Platforms: {PLATFORMS}")

    for platform in PLATFORMS:
        platform = platform.strip()
        if platform not in PLATFORM_PROMPTS:
            print(f"Unknown platform: {platform}, skipping")
            continue

        print(f"\nGenerating {platform}...")
        system = PLATFORM_PROMPTS[platform]
        result = call_model(system, f"Create {platform} content from this blog:\n\n{blog_content}")

        out_path = PLATFORM_FILES.get(platform, f"content/{platform}-post.md")
        Path(out_path).write_text(result)
        print(f"  Saved to {out_path}")

    print("\nSocial content generation complete.")


if __name__ == "__main__":
    main()
