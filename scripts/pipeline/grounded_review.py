#!/usr/bin/env python3
"""
Grounded fact-check for the content pipeline.
Extracts data claims from the blog and verifies each against the reference brief.

Environment variables:
  GITHUB_TOKEN  - GitHub PAT for Models API access
  CRITIC_MODEL  - Model identifier
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
API_URL = "https://models.inference.ai.azure.com/chat/completions"

SYSTEM_PROMPT = """You are a grounded content fact-checker. You will receive:
1. A blog post
2. A reference brief with verified source data

Your job:
- Extract every numerical claim, benchmark, percentage, and data point from the blog
- Cross-reference each claim against the reference brief
- Flag any claim NOT supported by the reference brief as [UNVERIFIED]
- Flag any claim that contradicts the reference brief as [CONTRADICTION]
- Check that [VOLATILE] data points have appropriate caveats
- Verify source attributions

Output format:
## Grounded Review

### Verified
- [claim]: matches [source in reference brief]

### Unverified
- [claim]: not found in reference brief

### Contradictions
- [claim]: blog says X, reference brief says Y

### Volatile Data Check
- [claim]: has caveat: yes/no

### Summary
- Claims checked: N
- Verified: N
- Unverified: N
- Contradictions: N
- Volatile without caveat: N
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
        "temperature": 0.2,
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
    ref_path = "content/reference-brief.md"

    if not blog_path:
        print("No blog post found. Skipping grounded review.")
        return

    blog_content = Path(blog_path).read_text()
    ref_content = Path(ref_path).read_text() if os.path.exists(ref_path) else "No reference brief available."

    print(f"Fact-checking: {blog_path}")
    user_msg = f"## Blog Post\n\n{blog_content}\n\n---\n\n## Reference Brief\n\n{ref_content}"

    review = call_model(SYSTEM_PROMPT, user_msg)
    print(review)

    summary_path = Path("content/critic-review-summary.md")
    existing = summary_path.read_text() if summary_path.exists() else ""
    summary_path.write_text(existing + "\n\n---\n\n" + review)
    print(f"\nGrounded review appended to content/critic-review-summary.md")


if __name__ == "__main__":
    main()
