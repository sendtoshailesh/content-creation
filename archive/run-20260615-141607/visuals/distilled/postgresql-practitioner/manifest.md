# Visual Pack Manifest: postgresql-practitioner

Generated: 2026-06-12
Blog source: `content/topics/postgresql/blog.md`
Persona mode: **practitioner** (LinkedIn carousel)
Canonical URL: https://sendtoshailesh.github.io/blog/ai-postgresql-performance.html

Title: *How AI Actually Helps You Fix PostgreSQL Performance Problems (and Where It Lies)*
Audience: DBAs and data engineers running PostgreSQL in production.

## Format

- **Carousel**: 9 square slides, hook → framework → steps → CTA grammar.
- **Format dimensions**: 1080×1080 px (square — fits LinkedIn document post / Instagram).
- **Rendered output**: 2160×2160 px PNGs — the 1080×1080 layout rasterized via
  Chromium at `device_scale_factor=2` (repo standard) for retina-crisp text.
- **Engine**: HTML/CSS authored with `scripts/visuals/html/design.py` (`page()` /
  `css()`), `components.py`, gated by `scripts/visuals/html/inspect.py`, rasterized
  by `render.py`. Type scale rendered at `scale = 1.55` for full-screen social.
- **Renderer**: `render_distilled.py` (in this folder). Re-run with:
  `.venv/bin/python content/visuals/distilled/postgresql-practitioner/render_distilled.py`

## Asset Inventory

| # | File | Dimensions | Slide type | Layout pattern | One-line purpose |
|---|------|-----------|------------|----------------|------------------|
| 1 | `slide-01-hook.png` | 1080×1080 | Hook | Hero stat | "AI won't fix your Postgres performance — it makes you 10x faster at finding the fix." |
| 2 | `slide-02-trap.png` | 1080×1080 | Problem | Comparison bars + gap callout | An LLM can't see your DB: GPT-4 54.89% vs human 92.96% text-to-SQL accuracy (BIRD); grounding is everything. |
| 3 | `slide-03-rule.png` | 1080×1080 | Rule | Numbered card list | Ground every prompt — feed real EXPLAIN (ANALYZE, BUFFERS) + pg_stat_statements + version()/settings. |
| 4 | `slide-04-matrix.png` | 1080×1080 | Framework | Scorecard rows + rating tags | Where AI helps: triage HIGH · read plans HIGH · index advice MEDIUM · anomaly detection HIGH · internals/DDL LOW. |
| 5 | `slide-05-example.png` | 1080×1080 | Step / proof | Before/after bars + gap callout | A missing composite index: 4,200 ms → 38 ms (~110x), validated with hypopg before CREATE INDEX CONCURRENTLY. |
| 6 | `slide-06-autovacuum.png` | 1080×1080 | Step | Two metric tiles (before/after knob) | Autovacuum starvation: AI names the knob (scale_factor 0.2 too high); you set the value (0.02) and watch. |
| 7 | `slide-07-safe-wiring.png` | 1080×1080 | Step | Checklist (ok / warn states) | Safe wiring: read-only role + Postgres MCP for live stats; never auto-apply DDL; validate with hypopg + staging replica. |
| 8 | `slide-08-playbook.png` | 1080×1080 | Recap | Vertical numbered flow + connectors | The playbook: Ground → Triage → Hypothesize → Validate → Apply → Measure. |
| 9 | `slide-09-cta.png` | 1080×1080 | CTA | Title + URL card + follow line | Read the full field guide (canonical URL) + follow for the next one. |

## Theme Assignment

One cohesive theme across the entire deck (overrides the default round-robin per
the brief: "one cohesive theme across the deck"). Brand design tokens only.

| Asset | Theme |
|-------|-------|
| slide-01 … slide-09 | `ocean` (ACCENT `#0ea5e9`, SUCCESS/teal `#14b8a6`, WARN/orange `#f97316`) |

Base tokens (BG, TEXT, TEXT_2, MUTED, GRID, LIGHT_BG) are constant across the deck.

## Quality gates (all passed)

- **DOM inspector** (`python3 -m scripts.visuals.html.inspect`): **PASS** on all 9
  slides — no off-scale type, ≤1 focal "display" number per slide, no text
  overflow/clipping, no canvas overflow, no stray internal labels, flow has visible
  connectors.
- **Uniform TYPE_SCALE**: every slide rendered at `scale = 1.55`; type roles are the
  shared design-system roles (display/title/value/subtitle/label/body/caption).
- **No gauges/arcs**: all magnitude shown with horizontal bars (slides 2, 5) or
  metric tiles (slide 6).
- **Focal number discipline**: exactly one `display` hero number where applicable
  (slide 1 = "10x"); bar/metric/gap values use the `value` role.
- **No baked-in slide counters**: footers are source/brand lines only.
- **Visual review**: every PNG opened and confirmed — crisp arrows on the playbook
  flow, uniform type, no clipping or overflow.

## Source attribution (on-slide)

- Slide 2: BIRD text-to-SQL benchmark (bird-bench.github.io), 2024 — GPT-4 54.89%
  (with knowledge) / human 92.96% execution accuracy.
- Slide 5: illustrative composite-index win; mechanism, SQL and tooling (hypopg,
  CREATE INDEX CONCURRENTLY) are real and cited in the blog.
- Slide 6: PostgreSQL docs — routine vacuuming (autovacuum_vacuum_scale_factor).

## Usage Notes

- **LinkedIn**: upload the 9 slides as a PDF document post (carousel). Place the
  canonical URL in the first comment within ~60 sec of posting.
- **Instagram / square feeds**: 1080×1080 native; the 2160 px files downscale cleanly.
- **Order**: slides are numbered 01→09 in narrative order (hook → trap → rule →
  framework → example → autovacuum → safe wiring → playbook → CTA).
- **Pipeline note**: this is a *net-new* social distribution asset (supports
  topic Step 11 — social publishing). It does not modify or invalidate the
  published blog's inline visuals (`content/topics/postgresql/visuals/`), so no
  Step 3b status reset was required.
