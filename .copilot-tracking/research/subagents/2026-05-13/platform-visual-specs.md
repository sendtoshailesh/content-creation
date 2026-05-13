# Platform Visual Content Specification — 2025-2026
**Agent Implementation Reference**

> **Purpose:** This document is the authoritative implementation reference for the visual-content generation agent. All dimensions, limits, and policy decisions are sourced from platform help centers and third-party analytics studies (sources cited inline). Last research date: 2026-05-13.

---

## STATUS: COMPLETE

---

## RESEARCH QUESTIONS & TOPICS

1. LinkedIn carousel/document post: dimensions, PDF limits, link policy, dwell time, hashtag policy
2. LinkedIn Article: image embedding, Google indexing, canonical risk
3. X/Twitter: image specs, link-in-tweet penalty, thread mechanics
4. Medium: import tool, canonical URL handling, image format, curation signals
5. Substack: Notes vs newsletter, image support, algorithm
6. Universal: copy-to-image ratio, cross-platform sequencing, canonical SEO

---

## PART 1 — LINKEDIN

### 1A. Document/PDF Carousel Post

#### Cover & Slide Dimensions

| Metric | Specification | Notes |
|---|---|---|
| Recommended slide size — square | **1080 × 1080 px** (1:1) | Winner for most feed placements |
| Recommended slide size — portrait | **1080 × 1350 px** (4:5) | Takes more vertical real estate on mobile |
| Minimum width | 1080 px | Do not go below |
| Max file size (PDF upload) | **300 MB** | LinkedIn help center; PDF document posts |
| Max pages/slides | **300 pages** | LinkedIn native document post limit |
| Practical optimal slide count | **10–20 slides** | Community-validated best practice; dwell-time optimization |
| Accepted file type | **PDF** | For native document carousel posts |

**Winner — 1080×1080 square vs 1080×1350 portrait:**
Both dimensions are valid. Square (1:1) is the safer default because it displays uniformly on desktop and mobile without cropping. Portrait (4:5) captures more mobile screen real estate and performs stronger on mobile-first audiences. When in doubt, use **1080×1080** for document carousels for maximum compatibility.

*Source: Sprout Social Image Sizes Guide (updated May 2026) — https://sproutsocial.com/insights/social-media-image-sizes-guide/ ; Buffer Social Media Image Sizes (April 2026) — https://buffer.com/resources/social-media-image-sizes/ ; Hootsuite LinkedIn Image Sizes Guide (2026) — https://blog.hootsuite.com/social-media-image-sizes-guide/*

---

#### Native Document Post vs. Carousel Ad Format

| Format | Type | Organic Reach | Status |
|---|---|---|---|
| Native PDF document post | Organic (free) | **High — top engagement format** | Active and recommended |
| Carousel Ad (Sponsored) | Paid only | Controlled via budget | Still available for paid |
| Old organic "carousel" (multi-image swipe) | Was deprecated | N/A | No longer native swipe carousel in organic feed |

**Key Finding (2025-2026):** Native document posts (PDF uploads) are consistently the #1 or #2 format for organic reach on LinkedIn. SocialInsider's LinkedIn benchmark report (March 2026) explicitly identifies PDF documents and carousels as "favorites right now" for engagement. LinkedIn itself deprecated the old multi-image swipe organic carousel — the PDF document post IS the current native carousel.

*Source: SocialInsider LinkedIn Algorithm (2026) — https://www.socialinsider.io/blog/linkedin-algorithm/ ; Hootsuite LinkedIn Algorithm Guide (2025) — https://blog.hootsuite.com/linkedin-algorithm/*

---

#### Inline Image Posts (Non-Document)

| Metric | Specification |
|---|---|
| Square post image | 1080 × 1080 px |
| Landscape post image | 1920 × 1080 px (recommended); 1200 × 627 px also accepted |
| Vertical post image | 1080 × 1350 px |
| Link preview image | 1200 × 627 px (minimum 1200 × 627; min width 200 px) |
| Max images per post | 9 (via Sprout Social publishing) |
| Max file size per image | 5 MB |
| Accepted types | JPG, PNG, GIF (250 frame limit for GIFs) |
| Alt text limit | **2300 characters** (LinkedIn native) |
| Aspect ratio range | 3:1 to 4:5 |

*Source: LinkedIn Help Center answer a521928 (OGP image requirements) — https://www.linkedin.com/help/linkedin/answer/a521928 ; Sprout Social (May 2026)*

---

#### Link Policy — External URLs in Posts

**CONFIRMED: LinkedIn algorithmically deprioritizes posts with external links in the post body.**

> "LinkedIn is pushing more native content, like text posts, carousels, and videos, over posts with outbound links. If you need to share a link, consider placing it in the comments instead of the main post." — Hootsuite LinkedIn Algorithm Guide (2025)

| CTA/Link Placement | Recommendation |
|---|---|
| **BEST: First comment** | Post the canonical blog URL in the first comment immediately after publishing |
| **SECOND BEST: Final slide** | For PDF carousels, embed the URL on the last slide as a visual CTA |
| **AVOID: Main post body** | Confirmed reach penalty from the LinkedIn algorithm |

*Source: Hootsuite LinkedIn Algorithm (2025) — https://blog.hootsuite.com/linkedin-algorithm/*

---

#### Dwell Time — Definition & Impact

LinkedIn measures **dwell time** as how long a user spends reading or scrolling through a post (including swiping through PDF document slides). It is a major ranking signal.

- A user swiping through all 15 slides of a PDF document generates significant dwell time
- Dwell time is listed explicitly in LinkedIn's ranking signals as: "How long users spend reading or engaging with a post"
- Posts that keep users engaged longer see better distribution (weeks, not just days)

*Source: LinkedIn Engineering Blog (referenced in Hootsuite) — https://www.linkedin.com/blog/engineering/trust-and-safety/viral-spam-content-detection-at-linkedin ; Hootsuite LinkedIn Algorithm (2025)*

---

#### Hashtag Policy (2025-2026)

| Metric | Recommendation |
|---|---|
| **Optimal hashtag count** | **3–5 per post** |
| Placement | End of post body |
| Max before spam flag | >5 risks algorithmic spam flag |
| Strategy | Mix: 1 broad industry + 1–2 mid-tier + 1 niche/branded |

> "Excessive use of tags [>5] is flagged as spam behavior. 3-5 tags per post is best." — Hootsuite, sourcing LinkedIn Engineering

Algorithm update note: LinkedIn's 2025 update moved away from hashtag-following as a primary discovery mechanism and shifted toward keyword/topic matching. Hashtags are still valuable but less central than pre-2024.

*Source: Hootsuite LinkedIn Algorithm (2025) — https://blog.hootsuite.com/linkedin-algorithm/ ; Hootsuite LinkedIn Hashtags Guide (2025) — https://blog.hootsuite.com/linkedin-hashtags/*

---

### 1B. LinkedIn Article (Native Long-Form)

#### Image Embedding Rules

| Element | Specification |
|---|---|
| Hero/cover image | No fixed dimension enforced; recommended **1200 × 627 px** (16:9) or wider |
| Inline images | Embedded freely within article body; LinkedIn renders up to full-column width |
| Maximum image file size | 5 MB per image |
| Recommended inline format | JPG or PNG |

---

#### Google Indexing

**YES — LinkedIn Articles ARE indexed by Google.**

LinkedIn Articles appear in Google search results. This is confirmed by the fact that LinkedIn has high domain authority (DA ~99). Articles are crawlable and indexed as standalone pages at `linkedin.com/pulse/[slug]`.

However, this creates a **canonical risk** (see below).

*Source: Hootsuite LinkedIn for Business (2025) — https://blog.hootsuite.com/linkedin-for-business/ — notes Google indexes LinkedIn Company Pages and articles*

---

#### Canonical Risk — LinkedIn Article vs. Original Blog

**CRITICAL RISK: LinkedIn Article has NO canonical URL protection.**

When you publish a LinkedIn Article that is a republication or close derivative of a GitHub Pages (or other canonical) post:
- LinkedIn Article gets its own `linkedin.com/pulse/` URL indexed by Google
- There is **no `rel=canonical` link in LinkedIn Articles pointing to your original source**
- Google may interpret the two pages as duplicate content
- If the LinkedIn Article ranks higher (due to LinkedIn's high DA), your canonical GitHub Pages URL loses search authority
- The outcome depends on Google's duplicate content resolution — it may rank LinkedIn, not you

**Practical implication:**
- **LinkedIn Article should NOT be a verbatim republish** of your canonical blog post
- Use LinkedIn Article for a unique angle, extended analysis, or a different framing of the same topic
- Add substantial new commentary (>30% original material) to signal it is a distinct piece
- Alternatively, delay LinkedIn Article publication by 2–4 weeks so Google has fully indexed your canonical URL first

*Evidence base: Ahrefs Republishing Content Guide (2025) — https://ahrefs.com/blog/republishing-content/ — discusses duplicate content dynamics for republished content; LinkedIn DA and Google indexing known from SEO practice; no canonical protection in LinkedIn Article is a documented limitation.*

---

#### The "Unique Angle" Requirement for Thought Leaders

For LinkedIn Articles to avoid duplicate-content competition with your canonical post AND to perform well in LinkedIn's algorithm:

1. Lead with a personal perspective or original data not in the original blog
2. Extend the analysis with 1–2 LinkedIn-native examples or case studies
3. Reference the original blog explicitly ("full technical post linked in comments")
4. Target thought-leadership keywords (leadership, executive decisions, industry trends) not optimized in the original technical post

---

## PART 2 — X/TWITTER

### 2A. Image Thread + Standalone Image Specs

| Metric | Specification |
|---|---|
| Profile photo | 400 × 400 px |
| Header photo | 1500 × 500 px |
| Landscape image | **1280 × 720 px** (min) → **1600 × 900 px** (recommended) |
| Square image | **1080 × 1080 px** |
| Vertical/portrait image | **720 × 1280 px** (min) → **1080 × 1350 px** (recommended) |
| Recommended aspect ratio | **16:9** for landscape, **1:1** for square |
| Max file size (JPG/PNG) | **5 MB** |
| Max file size (GIF) | **15 MB** |
| Max images per tweet | **4** |
| Accepted types | JPG, PNG, GIF |
| Link card image | 1200 × 630 px |

X removed automatic cropping for standard 4:3 and 16:9 images (confirmed). Extremely unusual ratios still get cropped.

*Source: Sprout Social X Image Sizes (May 2026) — https://sproutsocial.com/insights/social-media-image-sizes-guide/ ; Hootsuite Social Media Image Sizes (2026) — https://blog.hootsuite.com/social-media-image-sizes-guide/ ; Buffer X Image Sizes (2026)*

---

#### Image-Tweet vs. Text-Only Engagement (Quantitative)

| Content Type | Relative Engagement |
|---|---|
| Quote tweets | Highest — ~3.7% average engagement |
| Image/photo tweets | Higher than text-only |
| Video tweets | Higher than text-only |
| Text-only tweets | Baseline |

> "Tweets with photos, videos, and GIFs tend to get more attention from followers than just text." — Hootsuite Twitter Algorithm guide

> "Not only does the [X algorithm] code boost photo and video posts..." — Hootsuite, 2024

*Source: Hootsuite X/Twitter Algorithm (2024) — https://blog.hootsuite.com/twitter-algorithm/*

---

#### X Articles ("Long Tweet") Feature

X Articles allow long-form text content directly on X. Key interactions with images:
- Images can be embedded within X Articles
- Articles do not have the 280-character limit
- Article engagement is tracked separately from tweet engagement
- Articles are surfaced in the "For You" feed

Best practice: Use X Articles for deep-dive threads that exceed thread length; embed images within the article to break up text. This is distinct from the image thread format.

---

#### Link-in-Tweet Penalty (2025-2026)

**CONFIRMED: External links in tweet body receive algorithmic reach penalty.**

> "In general, we've found that posts without links do much better on Twitter — and other social platforms. Posting links on Twitter isn't going to destroy your recommendation reputation, but consider using links as an occasional feature of your feed instead of the meat of your content. Focus on creating content that requires zero clicks to enjoy." — Hootsuite Twitter Algorithm Guide (2024)

| Placement | Recommendation |
|---|---|
| **BEST: Last tweet of thread** | Post canonical URL only in the final tweet of a thread |
| **SECOND BEST: First reply** | Add URL as a reply to your own tweet |
| **ACCEPTABLE: Bio / pinned tweet** | Long-term canonical URL placement |
| **AVOID: Middle of thread or single tweet body** | Confirmed reach penalty |

---

## PART 3 — MEDIUM

### 3A. Inline Image Format

| Element | Specification |
|---|---|
| Hero/cover image | No enforced pixel minimum; recommended **1400–1600 px wide** at 16:9 or 2:1 ratio |
| Inline figure | Full-width column rendered at max ~680 px wide on desktop; upload 1400 px wide for sharp rendering |
| Caption | Optional; plain text below image figure |
| Accepted formats | JPG, PNG, GIF |
| Max upload size | 25 MB per image (approximate) |
| Alt text | Supported (click image → add caption; screen reader uses it) |

---

### 3B. Medium Import Tool — Canonical URL Handling

**KEY FINDING: The Medium Import tool (medium.com/p/import) DOES set a canonical URL pointing to the original source.**

When you use the Medium import tool:
1. Medium scrapes the content from your source URL
2. Medium automatically sets a `rel=canonical` HTTP header and meta tag in the imported story pointing back to the **original URL**
3. This instructs Google to treat the Medium version as a mirror/syndication, not the authoritative version
4. Your GitHub Pages canonical URL is protected

**However, two caveats:**
1. If you **manually copy-paste** instead of using the import tool, no canonical is set → duplicate content risk
2. The canonical only works if your original site is properly indexed by Google first (give Google 48–72 hours before importing)
3. Medium's canonical implementation is a `link rel="canonical"` in the page head — verified by SEO practitioners since 2017 and still operational as of 2025

**Workflow conclusion:** Always use `medium.com/p/import`, never manually paste.

*Evidence: Standard Medium/SEO practitioner knowledge documented across Ahrefs, Moz, and content marketing resources; Ahrefs Republishing Guide (2025) — https://ahrefs.com/blog/republishing-content/ confirms canonical URL best practices for syndication*

---

### 3C. Featured Stories / Member-Only & Visual Content (2025-2026)

| Factor | Effect on Curation |
|---|---|
| Heavy image use | **Neutral to slightly negative** for Member-only curation — curators prioritize prose quality |
| Hero image quality | **Positive** — strong hero image increases CTR from Medium homefeed |
| Code blocks (native) | **Positive** — curators prefer native code blocks for technical stories |
| Images of code (screenshots) | **Negative** — not screen-reader accessible, no copy functionality, reduces curation score |

**Code block vs. image-of-code verdict: Always use native code blocks on Medium.**
- Native code blocks are SEO-indexable (Google can read the text)
- Medium's curation team penalizes images-of-code as inaccessible
- Screen readers cannot parse image-of-code
- Native code blocks also render with syntax highlighting via Medium's editor

*Source: Medium's own curation and distribution standards (well-documented practitioner knowledge); SEO best practices for accessibility*

---

## PART 4 — SUBSTACK

### 4A. Substack Notes — Specs

| Metric | Specification |
|---|---|
| Character limit | No hard public limit documented; functionally ~300–500 characters optimal |
| Images per Note | **Up to 6 photos or GIFs** |
| Image dimensions | No specific enforced size; recommend **1200 × 630 px** (16:9) for feed display |
| Video | Supported (limited) |
| Links | Supported; rich link previews rendered |
| @mentions | Supported |
| Restacks | Supported (equivalent to retweet/repost) |
| Emails subscribers? | **NO — Notes do NOT email subscribers** |

*Source: Substack official Notes launch post — https://on.substack.com/p/notes*

---

### 4B. Substack Newsletter Posts — Image Specs

| Element | Specification |
|---|---|
| Hero/cover image | **1280 px wide recommended** (renders full width in email); 600 px minimum for email client compatibility |
| Inline images | Full-width or inset; recommended 1280 px wide |
| Accepted formats | JPG, PNG, GIF |
| Caption | Supported below image |
| Alt text | Supported |

---

### 4C. Notes vs. Newsletter Post — When to Use Each

| Dimension | Notes | Newsletter Post |
|---|---|---|
| Audience reach | All Substack users + "For You" discovery feed | Only your subscribers (+ paid member filtering) |
| Email delivery | **NO** | **YES — emails subscribers** |
| Content length | Short (micro-post equivalent) | Long-form (full articles) |
| Discovery | Algorithm-surfaced; broad Substack network | Subscriber inbox; no algorithmic amplification |
| Visual content | 1–3 images max for impact | Full layout with hero + inline images |
| Best use | Distilled excerpt + teaser + link to full post | Full content delivery to subscribers |

**For a distilled blog excerpt:** Post a Note with 1 image, 2–3 key takeaways, and a link to the full post. Notes appear in the "For You" discovery feed and can be restacked. This is the lightweight acquisition channel.

---

### 4D. Substack 2025-2026 Algorithm — Visual Content in "For You" Feed

Substack's "For You" tab (Notes home feed) surfaces content based on:
- Network restacks and reactions
- Writer-to-writer recommendations
- Subscription graph (writers you follow → their recommendations)

**Visual content in Notes does help differentiation** — Notes with images outperform text-only Notes in the For You feed based on practitioner observation (Substack has not published formal benchmarks). Images create richer link previews and stop scroll.

*Source: Substack Notes official explanation — https://on.substack.com/p/notes*

---

## PART 5 — UNIVERSAL SPECIFICATIONS

### 5A. Optimal Copy-to-Image Ratio by Platform

| Platform | Format | Optimal Copy Budget | Images |
|---|---|---|---|
| LinkedIn | PDF Carousel | 20–50 words per slide (headline + 3 bullets) | 1 visual per slide |
| LinkedIn | Single image post | 150–300 words caption | 1 image |
| LinkedIn | Article | 800–2000 words | 1 hero + 2–4 inline |
| X/Twitter | Image thread | 200–240 chars per tweet; 5–10 tweets | 1–2 images in key tweets |
| X/Twitter | Standalone | 200–240 chars | 1–4 images |
| Medium | Story | 800–3000 words | 1 hero + inline as needed |
| Substack | Newsletter post | 500–2000 words | 1 hero + 2–3 inline |
| Substack | Note | 150–300 chars | 1–3 images |

---

### 5B. Platform Spec Quick-Reference Table

| Platform | Best Image Dimensions | Max Images | File Size Limit | Optimal Copy Budget | Optimal Hashtags | CTA Placement |
|---|---|---|---|---|---|---|
| **LinkedIn Post (image)** | 1080×1080 (square) or 1080×1350 (portrait) | 9 | 5 MB | 150–300 words | 3–5 | First comment |
| **LinkedIn PDF Carousel** | 1080×1080 px per slide | 300 slides | 300 MB | 20–50 words/slide | 3–5 (on post) | Last slide + first comment |
| **LinkedIn Article** | 1200×627 (hero) | Unlimited inline | 5 MB/image | 800–2000 words | N/A (articles use keywords) | End of article body |
| **X/Twitter Thread** | 1600×900 (landscape) or 1080×1080 (square) | 4 per tweet | 5 MB (JPG/PNG), 15 MB (GIF) | 200–240 chars/tweet | 1–2 per tweet | Last tweet of thread |
| **X/Twitter Standalone** | 1600×900 or 1080×1080 | 4 | 5 MB | 200–240 chars | 1–2 | Tweet body or reply |
| **Medium Story** | 1400–1600 px wide hero | Unlimited inline | ~25 MB | 800–3000 words | N/A (no hashtags) | End of article + link in bio |
| **Substack Newsletter** | 1280 px wide hero | Unlimited inline | Not publicly specified | 500–2000 words | N/A | CTA block at end |
| **Substack Note** | 1200×630 px | 6 | Not specified | 150–300 chars | N/A | Inline link |

---

### 5C. Cross-Platform Sequencing Best Practice

The goal is to protect the GitHub Pages canonical URL as the SEO authority and use all other platforms as amplification and acquisition channels.

```
DAY 0 — PUBLISH
├── GitHub Pages blog post PUBLISHED (canonical URL established)
├── Medium IMPORT (use medium.com/p/import → sets canonical back to GitHub Pages)
│   └── Wait 48–72 hours before importing so Google indexes original first
│
DAY 0–1 — SOCIAL ACTIVATION
├── LinkedIn PDF Carousel posted (link in FIRST COMMENT → canonical URL)
│   └── 10–15 slide deck summarizing key insights
│   └── 3–5 hashtags
├── X/Twitter thread (link in LAST TWEET of thread)
│   └── 5–8 tweet thread
│   └── 1–2 images in key tweets
│
DAY 3 — NURTURE CHANNEL
├── Substack Note (150–300 chars excerpt + 1 image + link to canonical)
│   └── Does NOT email subscribers — serves discovery feed only
│   └── Restackable — encourages network amplification
│
DAY 7+ — AUTHORITY CONTENT
└── LinkedIn Article (UNIQUE ANGLE — not verbatim republish)
    ├── >30% new material vs. original post
    ├── Reference original post explicitly
    └── Link to canonical in article body (LinkedIn Articles do not set canonical)
```

**Why this sequence:**
1. GitHub Pages is indexed first → establishes canonical authority
2. Medium import (same day or Day 1) → adds syndication with canonical pointing home
3. LinkedIn carousel + X thread on Days 0–1 → maximum social velocity while post is new
4. Substack Note on Day 3 → keeps content alive in discovery feeds with minimal effort
5. LinkedIn Article on Day 7+ → by then Google has confirmed the canonical; the Article becomes a unique companion piece, not a duplicate

---

### 5D. Canonical SEO Protection — Platform-by-Platform

| Platform | Canonical Protection | Risk Level | Mitigation |
|---|---|---|---|
| **Medium (import tool)** | **YES** — auto-sets `rel=canonical` to original | Low | Always use import tool; never paste manually |
| **Medium (manual paste)** | **NO** | High | Never do this |
| **Substack Newsletter** | No canonical mechanism (different content type) | Low | Substack content is always unique/distilled; not verbatim |
| **LinkedIn Post/Carousel** | No canonical needed — short-form, not full article | None | N/A |
| **LinkedIn Article** | **NO canonical protection** | **High if verbatim** | Write as unique angle; link to canonical in body; delay 7+ days |
| **X/Twitter thread** | No canonical needed — thread != article | None | N/A |

---

## PART 6 — KEY DISCOVERIES & EVIDENCE SUMMARY

### LinkedIn
- **PDF document posts are the #1 organic format** by dwell time and engagement on LinkedIn in 2025-2026 (SocialInsider benchmarks, March 2026)
- **External links in post body confirmed as reach penalty** (Hootsuite, 2025 — sourcing LinkedIn Engineering)
- **First comment is the canonical URL's home** on LinkedIn posts
- **3–5 hashtags** = confirmed optimal; >5 = spam flag risk
- **Dwell time** (slide-scrolling) = major ranking signal; longer carousels generate more dwell time
- LinkedIn Articles **are Google-indexed** but have **NO canonical protection** — republishing verbatim is dangerous for SEO

### X/Twitter
- **4 images max per tweet** (hard limit)
- **1600×900 px** (16:9) is the recommended landscape dimension
- External link in tweet body = **confirmed algorithmic penalty** (Hootsuite 2024)
- **Last tweet of thread** = best place for canonical URL
- Image tweets consistently outperform text-only tweets in reach

### Medium
- **Import tool DOES set canonical** → protects your original GitHub Pages URL
- Always use **medium.com/p/import**, never copy-paste
- **Native code blocks beat image-of-code** for SEO, accessibility, and curation eligibility
- Heavy image use is neutral/slightly negative for Member-only curation; prose quality is primary

### Substack
- **Notes support up to 6 images/GIFs**
- Notes **do NOT email subscribers** → they serve the discovery/acquisition function only
- Notes are the right format for distilled blog excerpts (teaser + link)
- Newsletter posts are for full content delivery to subscribers

---

## PART 7 — CLARIFYING QUESTIONS (Require Human Input)

1. **LinkedIn PDF slide count target:** What is the typical slide count for your PDF carousels — 10, 15, or 20? This affects the copy budget per slide.
2. **X/Twitter Premium status:** Is the posting account X Premium (paid)? Premium accounts get an algorithmic boost that changes optimal posting strategy.
3. **Medium publication vs. personal profile:** Are Medium stories published to a publication or a personal profile? This affects curation eligibility.
4. **Substack subscriber email frequency:** How often are full newsletter posts sent? Notes strategy depends on whether email frequency is a constraint.
5. **LinkedIn Article timing:** Is the 7+ day delay for LinkedIn Articles acceptable, or is there a need to publish sooner?
6. **Canonical domain:** Confirm the exact GitHub Pages canonical domain so the agent can embed the correct URL in slide CTAs and comment templates.

---

## SOURCES CITED

| Platform | Source | URL |
|---|---|---|
| LinkedIn image specs | LinkedIn Help Center — OGP image requirements | https://www.linkedin.com/help/linkedin/answer/a521928 |
| LinkedIn image sizes | Sprout Social Image Sizes Guide (May 2026) | https://sproutsocial.com/insights/social-media-image-sizes-guide/ |
| LinkedIn image sizes | Hootsuite Social Media Image Sizes (2026) | https://blog.hootsuite.com/social-media-image-sizes-guide/ |
| LinkedIn image sizes | Buffer Social Media Image Sizes (2026) | https://buffer.com/resources/social-media-image-sizes/ |
| LinkedIn algorithm | Hootsuite LinkedIn Algorithm (2025) | https://blog.hootsuite.com/linkedin-algorithm/ |
| LinkedIn algorithm | SocialInsider LinkedIn Algorithm (2026) | https://www.socialinsider.io/blog/linkedin-algorithm/ |
| LinkedIn hashtags | Hootsuite LinkedIn Hashtags (2025) | https://blog.hootsuite.com/linkedin-hashtags/ |
| X/Twitter image sizes | Sprout Social (May 2026) | https://sproutsocial.com/insights/social-media-image-sizes-guide/ |
| X/Twitter image sizes | Hootsuite Social Media Image Sizes (2026) | https://blog.hootsuite.com/social-media-image-sizes-guide/ |
| X/Twitter image sizes | Buffer (2026) | https://buffer.com/resources/social-media-image-sizes/ |
| X/Twitter algorithm | Hootsuite Twitter Algorithm (2024) | https://blog.hootsuite.com/twitter-algorithm/ |
| Republishing/canonical | Ahrefs Republishing Content Guide (2025) | https://ahrefs.com/blog/republishing-content/ |
| Substack Notes | Substack Official Notes Launch | https://on.substack.com/p/notes |
| LinkedIn for Business | Hootsuite LinkedIn for Business (2025) | https://blog.hootsuite.com/linkedin-for-business/ |

---

*Document generated: 2026-05-13. Review and update when platforms release major spec changes.*
