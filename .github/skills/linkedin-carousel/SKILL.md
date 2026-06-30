---
name: linkedin-carousel
description: Build one consolidated LinkedIn document carousel (PDF) that stitches a blog's publish-ready visuals into a single swipeable story — cover + one captioned slide per visual + CTA. Use after the blog and its visuals are finalized and REVR-passed, when the user wants a single deck-like file to upload as a LinkedIn document post. Optional distribution output, never a publishing gate.
---

# LinkedIn Carousel (Consolidated Visual-Story PDF)

Deterministic, manifest-driven carousel generation. This skill consolidates a
blog's already-rendered visuals into **one** portrait PDF that tells the blog's
story end to end. Uploaded to LinkedIn as a **document post**, the PDF renders as
a native swipeable carousel — the highest-reach format on the platform.

It is **optional** — skipping it never blocks publishing. It is distinct from
`deck-builder` (a full PPTX/PDF speaker deck): this skill produces a single
social-ready carousel from the existing visual assets, with no new claims.

## When to use

- **Auto-built with every LinkedIn post.** Whenever the pipeline generates a LinkedIn
  post and the blog's visuals are finalized (REVR-passed), build the carousel as that
  post's document-post attachment — it is the asset the post exists to carry. This is a
  standing step (orchestrator Step 4b-carousel), not a user-opt-in.
- **Only after** the blog (`content/<topic>.md`) and its visuals are finalized and
  every visual carries a PASS REVR record under `content/visuals/revr/`.
- Also runnable on demand when the user asks for a single deck-like file / carousel to
  share on LinkedIn (e.g. "consolidate all visuals as one story I can post").

## Inputs (read, do not modify)

| Input | Path | Use |
|-------|------|-----|
| Finalized blog | `content/<topic>.md` | Narrative order of visuals + alt text → captions |
| Visuals | `content/visuals/*.png` | The slides; reuse as-is, never re-render here. SVG visuals must be rasterized to PNG first (see Phase A0) — the renderer composites raster images via PIL. |
| Canonical URL | `content/publishing-log.md` | CTA slide + first-comment link |
| Creative brief | `content/creative-brief.md` | Title, subtitle, voice for cover + CTA |
| Design tokens | `.github/copilot-instructions.md` | Palette + Helvetica Neue |

## Output files

| File | Purpose |
|------|---------|
| `content/visuals/<topic>-carousel.manifest.json` | Curated slide spine (cover, ordered slides, CTA) |
| `content/visuals/<topic>-carousel.pdf` | The carousel PDF for LinkedIn document upload |

## Procedure

### Phase A0 — Rasterize any SVG visuals to PNG (only if needed)

0. The renderer opens each slide image with PIL, so **SVG visuals cannot be used directly**.
   Walk the finalized blog's image embeds; for every `![alt](visuals/<name>.svg)`, produce a
   PNG sibling before curating the manifest:

   ```bash
   rsvg-convert -w 3200 --background-color=white content/visuals/<name>.svg -o content/visuals/<name>.png
   ```

   (`rsvg-convert` is preferred; `magick`/`inkscape`/`cairosvg` also work.) Reference the
   `.png` name in the manifest. Blogs whose visuals are already all PNG skip this phase.

### Phase A — Curate the manifest (gate before render)

1. Walk the finalized blog top to bottom and list every `![alt](visuals/<name>.png)`
   marker **in order** — this is the story order. Do not reorder by filename.
2. For each visual, write a one-line `caption` (distill the alt text / its section's
   point) and a short uppercase `kicker` (2–4 words naming the beat, e.g. `WHY NOW`).
3. Fill the cover (`title_lines`, `subtitle`, `tagline`, `cover_note`), `handle`,
   `canonical` (from `content/publishing-log.md`), and the CTA (`cta_headline`,
   `cta_body`). Keep captions terse; the visual carries the detail. The `handle`
   is the author name/personal handle only — never include the repo name in it
   (it renders in every slide footer).
4. Write the manifest to `content/visuals/<topic>-carousel.manifest.json` using the
   schema in the loop-engineering example. Use ASCII only in caption/kicker/cover
   text (no Unicode arrows or glyphs — write `->`, `[x]`); this matches the visual
   rendering standard.

### Phase B — Render the PDF

5. Run the renderer:

   ```bash
   python scripts/visuals/build_carousel.py content/visuals/<topic>-carousel.manifest.json
   ```

   It builds a 1080×1350 (4:5) PDF: a cover slide, one captioned slide per visual
   (image contain-fit under a kicker + caption band, with a slide-number footer),
   and a closing CTA slide carrying the canonical URL. The renderer fails fast if
   any manifest visual is missing.
6. Verify the result by rasterizing a few pages (`qlmanage -t -s 700 -o /tmp <pdf>`
   renders page 1; for inner pages import the module and `savefig(..., dpi=100)` —
   `dpi=100` is required because `figimage` places pixels for the 1080×1350 canvas).
   Confirm: caption bands don't overlap the image, images are fully inside the frame,
   and the CTA URL is complete.

## Output handoff (how the user posts it)

Tell the user, do not auto-post:

1. New LinkedIn post → **Add a document** → upload `content/visuals/<topic>-carousel.pdf`.
2. Give it a short document title (becomes the carousel title).
3. Put the hook in the post body; put the **canonical URL in the FIRST COMMENT**, not
   the body, to avoid the outbound-link reach penalty.
4. Publish — LinkedIn renders the PDF as a swipeable carousel.

## Pipeline hygiene

- This is **Step 6d** (optional, post-content). It runs after visuals are finalized
  and REVR-passed; it never gates publishing.
- After building, record the asset in `content/pipeline-config.md` (a one-line note
  under Current Step is enough): renderer path, manifest path, and output PDF path.
- If a visual is re-rendered later, the carousel is **stale** — rerun Phase B to refresh.

## Renderer reference

- Generic, manifest-driven: `scripts/visuals/build_carousel.py`.
- It strips its own directory from `sys.path` before importing matplotlib (a local
  `scripts/visuals/html/` dir would otherwise shadow the stdlib `html` package).
- Tokens, font, and 4:5 canvas are fixed in the renderer; per-blog content lives in
  the manifest. To restyle, edit the renderer; to re-content, edit the manifest.
