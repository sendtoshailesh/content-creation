---
name: unicode-formatting
description: 'Format text with Unicode Mathematical Bold and Italic characters for LinkedIn and X/Twitter posts. Use when creating social media content that needs native bold/italic rendering without Markdown support.'
argument-hint: 'Paste text to format, or describe the social post to create'
---

# Unicode Formatting Skill

## When to Use

- Creating LinkedIn posts with native bold/italic (LinkedIn strips Markdown)
- Creating X/Twitter threads with visual emphasis
- Converting plain text social posts to Unicode-formatted versions

## Unicode Character Maps

### Bold (Mathematical Sans-Serif Bold)

Use for key phrases, section headers, and emphasis:

| Plain | Unicode | Codepoint Range |
|-------|---------|-----------------|
| A-Z | 𝗔-𝗭 | U+1D5D4 to U+1D5ED |
| a-z | 𝗮-𝘇 | U+1D5EE to U+1D607 |
| 0-9 | 𝟬-𝟵 | U+1D7EC to U+1D7F5 |

### Italic (Mathematical Sans-Serif Italic)

Use for contrast, counterpoints, and secondary emphasis:

| Plain | Unicode | Codepoint Range |
|-------|---------|-----------------|
| A-Z | 𝘈-𝘡 | U+1D608 to U+1D621 |
| a-z | 𝘢-𝘻 | U+1D622 to U+1D63B |

## Formatting Conventions

- **Separators**: ━━━ (U+2501, box drawing heavy horizontal)
- **Sub-bullets**: ▸ (U+25B8, right-pointing small triangle)
- **Emoji anchors** (sparingly): ⚠️ 📊 🎯 💡 🔑
- **Copy markers**: `── START COPY ──` / `── END COPY ──`

## Procedure

### 1. Write Plain Text First

Draft the full post in plain text with clear structure: hook, body sections, data points, CTA.

### 2. Apply Unicode Formatting

- Convert section headers and key phrases to 𝗕𝗼𝗹𝗱
- Convert counterpoints and nuance phrases to 𝘐𝘵𝘢𝘭𝘪𝘤
- Add ━━━ separators between major sections
- Replace bullet dashes with ▸
- Add 1-2 emoji anchors per section (max)

### 3. Verify Character Counts

- LinkedIn: no hard char limit, but keep under 3000 chars
- X/Twitter: each tweet ≤ 280 chars (Unicode chars count as 1)

### 4. Wrap in Copy Markers

```
── START COPY ──

[formatted content here]

── END COPY ──
```

## Platform Rules

| Platform | Bold | Italic | Markdown | Max Length |
|----------|------|--------|----------|-----------|
| LinkedIn | Unicode 𝗕𝗼𝗹𝗱 | Unicode 𝘐𝘵𝘢𝘭𝘪𝘤 | Not supported | ~3000 chars |
| X/Twitter | Unicode 𝗕𝗼𝗹𝗱 | Unicode 𝘐𝘵𝘢𝘭𝘪𝘤 | Not supported | 280/tweet |
| Reddit | **Markdown** | *Markdown* | Native | No practical limit |

## Anti-Patterns

- Do NOT use Unicode bold/italic on Reddit — it renders as plain text
- Do NOT overformat — bold every word defeats the purpose
- Do NOT use emoji as content; use as visual anchors only
