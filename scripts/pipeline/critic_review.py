#!/usr/bin/env python3
"""
Cross-model critic review for the content pipeline.
Reads the blog post, sends it to a model from a DIFFERENT family than the one
that created it, and produces a structured review.

Environment variables:
  GITHUB_TOKEN    - GitHub PAT for Models API access
  CRITIC_MODEL    - Model identifier (e.g., openai/gpt-4.1)
  CRITIC_FAMILY   - Model family (openai, anthropic, google)
  CREATION_FAMILY - Family that created the content
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
CRITIC_FAMILY = os.environ.get("CRITIC_FAMILY", "openai")
CREATION_FAMILY = os.environ.get("CREATION_FAMILY", "unknown")
API_URL = "https://models.inference.ai.azure.com/chat/completions"

SYSTEM_PROMPT = """You are a cross-model content critic. The content you are reviewing was created by
a DIFFERENT AI model family ({creation_family}). You are from the {critic_family} family.

Your job is adversarial review - find what the creation model got wrong or missed:

1. CHALLENGE ASSUMPTIONS: Look for claims that sound plausible but may be pattern-matched, not verified.
2. DETECT HALLUCINATED SPECIFICITY: Flag suspiciously precise numbers with no source.
3. FIND LOGICAL GAPS: Where does the argument skip steps?
4. CHECK TONE DRIFT: Flag sections that shift to corporate or promotional tone.
5. VERIFY INTERNAL CONSISTENCY: Do data points match across sections?
6. VISUAL DENSITY: Flag any H2/H3 section >400 words with no image reference.

Produce a structured review in Markdown:

## Critic Review

### Issues Found
- [severity: high/medium/low] [section]: description

### Verified Claims
- [claim]: appears consistent with stated source

### Recommendations
- [suggestion]

### Visual Density Check
- [section]: word count, has visual: yes/no

### Summary
- Issues: N (high: N, medium: N, low: N)
- Sections checked: N
- Visual density gaps: N
"""


def call_model(system_prompt, user_content):
    model_name = CRITIC_MODEL.split("/")[-1] if "/" in CRITIC_MODEL else CRITIC_MODEL
    payload = json.dumps({
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        "max_tokens": 4096,
        "temperature": 0.3,
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
                  and "twitter" not in c and "youtube" not in c and "reference" not in c]
    if not candidates:
        return None
    return max(candidates, key=os.path.getmtime)


def main():
    blog_path = find_blog_post()
    if not blog_path:
        print("No blog post found in content/. Skipping critic review.")
        Path("content/critic-review-summary.md").write_text("No blog post found to review.\n")
        return

    blog_content = Path(blog_path).read_text()
    print(f"Reviewing: {blog_path} ({len(blog_content)} chars)")
    print(f"Creation family: {CREATION_FAMILY} | Critic family: {CRITIC_FAMILY}")

    system = SYSTEM_PROMPT.format(
        creation_family=CREATION_FAMILY,
        critic_family=CRITIC_FAMILY,
    )
    user_msg = f"Review this blog post:\n\n---\n\n{blog_content}"

    review = call_model(system, user_msg)
    print(review)

    Path("content/critic-review-summary.md").write_text(review)
    print(f"\nReview saved to content/critic-review-summary.md")


if __name__ == "__main__":
    main()
