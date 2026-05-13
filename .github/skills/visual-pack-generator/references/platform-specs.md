# Platform Specs Reference

Per-platform visual specifications for distilled post distribution. Load this file in Step 4 of the Visual Pack Generator procedure to determine required asset dimensions, counts, and platform-specific constraints.

---

## Platform Specification Table

| Platform | Format | Dimensions (px) | Max Visuals | Copy Budget | CTA Location | File Format | Canonical Risk |
|----------|--------|-----------------|-------------|-------------|--------------|-------------|----------------|
| LinkedIn Post (carousel) | PDF document post | 1080×1080 (square) preferred; 1080×1350 (portrait) also supported | 10 slides optimal (300 max) | 20–50 words/slide | First comment — post within 60 sec of publishing | PNG slides → upload individually or assemble as PDF | None (link in comment, not body) |
| LinkedIn Article | Text + inline exhibits | 1200×627 (hero image); 1200×627 (inline exhibits) | 2–3 inline exhibits | 700–900 words | End of article body paragraph | PNG | HIGH — Google indexes without canonical protection; content must be UNIQUE ANGLE |
| X/Twitter | Image-anchored thread | 1600×900 (landscape) or 1080×1080 (square) | 4 per tweet max | 200–240 chars per tweet | Final tweet only | PNG | None (link in last tweet) |
| Medium | Hero + inline images | 1400 px wide minimum (auto height); 1400×800 recommended for hero | Unlimited inline | 700–900 words | End of article | PNG | LOW — Import tool sets rel=canonical to GitHub Pages |
| Substack Note | 1 hero + optional inline | 1200×630 | 1–3 images (6 max) | 150–300 chars | Inline link in text | PNG | None |

---

## Platform-Specific Critical Rules

### LinkedIn Post (Carousel)

```
LINK PENALTY: Place canonical URL as FIRST COMMENT only — never in the post body.
Post the first comment within 60 seconds of publishing the carousel.

UPLOAD METHOD: Upload slides as a PDF document post (not as image post) to enable
carousel swipe behavior. Until automated PDF assembly is available, upload PNGs
individually in slide order.

REACH MECHANICS: LinkedIn's algorithm rewards dwell time (swipes through slides).
A 10-slide carousel at 35-55 sec average dwell outperforms text posts by 1.56x
and link posts by 2.15x (SocialInsider 2026, 1.3M posts).
```

### X/Twitter

```
LINK PENALTY: Twitter/X deprioritizes tweets that contain links in the tweet body.
Place the canonical URL ONLY in the final tweet of the thread.

IMAGE LIMIT: Maximum 4 images per tweet. Use image slots for:
  - Tweet 1: Hook image card (most important visual)
  - Tweet 2-3: Key data visualization cards
  - Final tweet: Optional summary card + canonical URL

CHARACTER ACCOUNTING:
  - Unicode characters count as 1 character each
  - URLs are always wrapped to t.co (23 characters regardless of URL length)
  - Plan 200-240 chars per tweet to leave buffer
```

### Medium

```
CANONICAL PROTECTION: MUST use the Medium Import tool — do NOT copy-paste content.
Import preserves the rel=canonical attribute pointing to the GitHub Pages source.
Copy-paste creates a new canonical URL on Medium, competing with the original.

IMPORT URL: https://medium.com/p/import

IMAGE EMBEDDING: Images placed in Markdown using standard syntax render inline
after import. Place images at natural reading breakpoints in the article.

WORD COUNT: 700-900 words for distilled versions. Do not republish the full blog.
```

### Substack

```
POST AS NOTE (NOT NEWSLETTER):
  - Substack NOTES appear in the ambient discovery feed
  - Substack POSTS (newsletters) email all subscribers
  - Distilled content should always be a NOTE to avoid subscriber fatigue
    and duplicate-content risk with the base blog

IMAGE SUPPORT: Up to 6 images in a Note (use 1-3 for typical distillation).
Substack Note image dimensions: 1200×630 px recommended.
```

### LinkedIn Article

```
CANONICAL RISK — HIGH:
  Google indexes LinkedIn Articles directly with their own canonical URL.
  There is NO technical mechanism to set rel=canonical on a LinkedIn Article.
  This creates direct SEO competition with the GitHub Pages source.

MITIGATION REQUIREMENT: LinkedIn Article content MUST present a UNIQUE ANGLE
that is NOT found in the base blog. Requirements:
  - More than 30% new material or a genuinely different perspective
  - Different structure and narrative arc from the base blog
  - Cannot be a recap, summary, or rephrasing of the blog

ACCEPTABLE UNIQUE ANGLES:
  - "What I learned working with customers on [topic]"
  - "The [N] mistakes most teams make when [doing X]"
  - "Why [X] matters more than most people think"
  - "The hidden cost of [common practice]"
  - "A practitioner's take on [topic]: what the research misses"

WORD COUNT: 700-900 words. Include 2-3 inline exhibit images (1200×627 px).
```

---

## Asset Requirements by Persona Mode

### Practitioner Mode — Full Asset List

| Asset File | Dimensions (px) | DPI | Platform | Slide Type |
|-----------|----------------|-----|----------|-----------|
| slide-01-hook.png | 1080×1080 | 320 | LinkedIn carousel | Hook |
| slide-02-promise.png | 1080×1080 | 320 | LinkedIn carousel | Promise |
| slide-03-problem.png | 1080×1080 | 320 | LinkedIn carousel | Problem |
| slide-04-framework.png | 1080×1080 | 320 | LinkedIn carousel | Framework |
| slide-05-step1.png | 1080×1080 | 320 | LinkedIn carousel | Step 1 |
| slide-06-step2.png | 1080×1080 | 320 | LinkedIn carousel | Step 2 |
| slide-07-step3.png | 1080×1080 | 320 | LinkedIn carousel | Step 3 |
| slide-08-interrupt.png | 1080×1080 | 320 | LinkedIn carousel | Pattern Interrupt |
| slide-09-recap.png | 1080×1080 | 320 | LinkedIn carousel | Recap |
| slide-10-cta.png | 1080×1080 | 320 | LinkedIn carousel | CTA |
| x-card-01.png | 1600×900 | 320 | X/Twitter | Hook card |
| x-card-02.png | 1600×900 | 320 | X/Twitter | Data card |
| x-card-03.png | 1600×900 | 320 | X/Twitter | Framework card |
| x-card-04.png | 1600×900 | 320 | X/Twitter | Recap card |
| medium-hero.png | 1400×800 | 320 | Medium | Hero image |
| medium-inline-01.png | 1200×800 | 320 | Medium | Inline visual 1 |
| medium-inline-02.png | 1200×800 | 320 | Medium | Inline visual 2 |
| substack-hero.png | 1200×630 | 320 | Substack Note | Hero image |
| linkedin-exhibit-01.png | 1200×627 | 320 | LinkedIn Article | Inline exhibit 1 |
| linkedin-exhibit-02.png | 1200×627 | 320 | LinkedIn Article | Inline exhibit 2 |

**Total: 20 assets**

### Executive Mode — Full Asset List

| Asset File | Dimensions (px) | DPI | Platform | Exhibit Type |
|-----------|----------------|-----|----------|-------------|
| exhibit-01.png | 1200×627 | 320 | LinkedIn Article + Medium | Context Exhibit (required) |
| exhibit-02.png | 1200×627 | 320 | LinkedIn Article + Medium | Evidence Exhibit (required) |
| exhibit-03.png | 1200×627 | 320 | LinkedIn Article | Framework Exhibit (required) |
| exhibit-04.png | 1200×627 | 320 | LinkedIn Article | ROI Exhibit (optional) |
| exhibit-05.png | 1200×627 | 320 | LinkedIn Article | Action Exhibit (optional) |
| x-card-01.png | 1600×900 | 320 | X/Twitter | Context/Evidence exhibit card |
| x-card-02.png | 1600×900 | 320 | X/Twitter | Framework/ROI exhibit card |
| medium-hero.png | 1400×800 | 320 | Medium | Hero image |
| medium-inline-01.png | 1200×800 | 320 | Medium | Inline exhibit |
| substack-hero.png | 1200×630 | 320 | Substack Note | Hero image |

**Total: 10 assets (8 required + 2 optional exhibit variations)**

---

## Publish Cadence

Execute in this sequence to maximize reach and protect the GitHub Pages canonical URL:

```
Day 0 (publish day)
  1. GitHub Pages publish          -> Establishes canonical URL
  2. Medium Import                 -> Sets rel=canonical -> GitHub Pages (SEO protection)
  3. LinkedIn carousel post        -> Upload slides; post canonical URL as first comment
                                      within 60 seconds
  4. X/Twitter image thread        -> Image cards + text thread; canonical URL in last tweet only

Day 3-4
  5. Substack Note                 -> Hero image + excerpt + inline link to canonical URL
                                      (post as NOTE, not newsletter)

Day 7+
  6. LinkedIn Article              -> Unique angle content (>30% new material)
                                      + 2-3 inline exhibit images
```

**Rationale for Day 0 ordering**: Medium import must run before LinkedIn to ensure rel=canonical is in place before search engines index the social distributions. LinkedIn carousel distributes fastest (hours) so publish promptly after Medium import.

---

## Engagement Benchmarks

Use these data points to justify the visual-first approach in content strategy documents:

| Metric | Value | Source |
|--------|-------|--------|
| LinkedIn carousel vs text posts | 1.56× engagement | SocialInsider 2026, 1.3M posts |
| LinkedIn carousel vs link posts | 2.15× engagement | SocialInsider 2026, 1.3M posts |
| LinkedIn carousel average dwell time | 35–55 sec | Hootsuite 2026 |
| LinkedIn text post average dwell time | 8–12 sec | Hootsuite 2026 |
| X/Twitter image tweets vs text-only | +35% to +150% more retweets | Buffer + Twitter + Sotrender 2024–2026 |
| Text + illustrations vs text only | +323% comprehension | Springer academic study |

---

## FT Visual Vocabulary — Chart Type Mapping

Use this mapping in Step 3 (Executive mode) to select the correct chart type for the Framework Exhibit:

| Data Relationship | Recommended Chart Type |
|-------------------|----------------------|
| Deviation from norm or baseline | Diverging bar chart |
| Part-to-whole (composition) | Stacked bar or donut chart |
| Ranking or magnitude comparison | Horizontal bar chart with direct labels |
| Change over time | Line chart or slope chart |
| Correlation between two variables | Scatter plot |
| Distribution of values | Histogram or box plot |
| Flow or process | Sankey diagram or labeled flow |
| Geographic | Choropleth map (use only when geography is the point) |
| Connection or hierarchy | Network or tree diagram |
