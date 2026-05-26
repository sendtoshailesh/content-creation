# Marp Deck Build Playbook — Lessons from Git-Ape Workshop Decks

> **Source project**: `git-ape-private/workshops/` (Tracks 1–4 customer-presentation decks)
> **Captured**: 2026-05-26
> **Purpose**: Reference playbook for any future Markdown → HTML/PDF/PPTX deck generation work. Every gotcha below cost time to debug — read this before starting a new deck.

This document carries forward two things from the Git-Ape workshop deck build:

1. **15 lessons learned (L1–L15)** — surgical, reusable rules for building presentation-quality decks with Marp CLI.
2. **Open follow-up: marketing-assets workstream** — what's still pending from the original workshop program plan, to be picked up here.

---

## Part 1 — Lessons Learned (L1–L15)

### Asset & rendering pipeline

**L1 — Externalise SVGs; never inline.**
Inline `<svg>` in Marp Markdown breaks PPTX rendering — raw XML leaks into the slide as text. ALWAYS write SVGs to a separate file (e.g., `shared/img/diagram.svg`) and reference via:
```html
<img src="../shared/img/diagram.svg" alt="..." style="width:100%;height:auto;display:block;" />
```
This works correctly in HTML, PDF (Chromium), and PPTX (LibreOffice).

**L2 — Blank lines inside inline HTML blocks break CommonMark.**
If you must inline HTML, strip ALL blank lines inside the block. A blank line ends the HTML block in CommonMark and the rest gets rendered as text. This is what causes "raw SVG XML appearing on a slide" in failed renders.

**L8 — Always re-render all three formats after any change.**
HTML, PDF (Chromium), and PPTX (LibreOffice) use different rendering paths. A fix that lands in HTML can still break in PPTX. Run the full triple-render every iteration:
```bash
npx --yes -p @marp-team/marp-cli marp deck.md --html --allow-local-files -o deck.html
npx --yes -p @marp-team/marp-cli marp deck.md --pdf  --allow-local-files -o deck.pdf
npx --yes -p @marp-team/marp-cli marp deck.md --pptx --allow-local-files -o deck.pptx
```

**L9 — Verify visually, not by file size.**
File size is NOT a quality signal. Rasterize and inspect every slide:
- PDF: `magick -density 130 deck.pdf slide-%02d.png` (requires Ghostscript: `brew install ghostscript`)
- PPTX: `soffice --headless --convert-to pdf --outdir /tmp/x deck.pptx && magick -density 110 /tmp/x/deck.pdf /tmp/x/slide-%02d.png` (requires LibreOffice: `brew install --cask libreoffice`)

### Marp + CommonMark pitfalls

**L3 — Speaker notes must be single-line prose.**
Marp converts HTML comments inside slides to PPTX speaker notes, but its parser eats bullet-list lines (`- foo`) inside comments. Write notes as a single-line prose paragraph, no leading dashes. Verify by unzipping the PPTX and reading `ppt/notesSlides/notesSlide{N}.xml`.

**L11 — Separate Marp directives from speaker-note comments.**
Marp directives like `<!-- _class: lead -->` and speaker-note comments `<!-- speaker notes... -->` MUST be in separate `<!-- ... -->` blocks. If they share a comment block, the directive gets eaten.

**L15 — Strip trailing `---` after slide generation.**
A trailing slide separator at end-of-file creates an empty extra slide. After programmatically generating slides, always:
```python
text = text.rstrip()
if text.endswith('---'):
    text = text[:-3].rstrip() + '\n'
```

### CSS specificity & theming

**L4 — Light-theme overrides are mandatory for these classes.**
On `section.light` slides the following classes WILL render invisibly without explicit overrides: `.badge`, `.pill`, `.note`, `code`, `.panel pre code`, `.hero-card pre code`. Always pair every dark-theme rule with a `section.light` counterpart.

**L13 — Override Marp's built-in code styling with `!important`.**
Marp's default theme uses an extremely specific selector:
```css
div#\:\$p > svg > foreignObject > section > code { ... }
```
A plain `code` or even `section code` will lose. Use `!important` on `background` and `color`:
```css
code {
  background: rgba(48, 64, 110, 0.55) !important;
  color: #e8efff !important;
  ...
}
section.light code {
  background: rgba(20, 30, 50, 0.07) !important;
  color: #20324f !important;
}
```

### Layout & content discipline

**L5 — Don't wrap headings in `<strong>` inside `.metric` blocks.**
`.metric strong` is sized at 1.6em (intended for stat numbers like "73%" or "$4.35M"). Wrapping a heading in `<strong>` inside a `.metric` overflows the card. For titles, use `### h3` and style via `.metric h3 { font-size: 0.95em }`.

**L6 — Narrow flow boxes need single-word labels.**
A `.flow-tight` 4-column grid inside a half-width `.panel` produces ~140px-wide boxes — multi-word descriptions wrap mid-word. Use single-word labels (Say / Plan / Gate / Ship) and drop the `<p>` description entirely for boxes under ~150px wide.

**L7 — Slide-count pills must match actual slide count.**
A hero pill that says "5 slides" while the deck has 6 is a tell-tale "agent slop" signal in a customer-facing deck. Count slides after every structural edit and update the pill.

**L14 — SVG label clearance.**
Labels inside an SVG viewBox need clearance above (y < 35) or below (y > viewBoxHeight − 5) the diagram boxes. Putting text at y=100/200 inside a 280-tall viewBox with boxes at y=110–180 overlaps the row.

### Workflow

**L10 — Anchor shared theme CSS in one canonical deck.**
For multi-deck programs, pick one deck as the canonical source of shared front-matter (theme tokens + utility classes). Re-extract the front-matter (`sed -n '1,N p'`) when generating sibling decks so theme fixes propagate automatically.

**L12 — Logo paths must be relative from the deck file, not the repo root.**
For a deck at `workshops/track-1-zero-to-deploy/deck.md`, the logo at `website/static/img/logo.png` is at `../../website/static/img/logo.png`. Don't paste repo-relative paths.

---

## Part 2 — Open Follow-up: Marketing Assets

The Git-Ape workshop program plan originally listed marketing/distribution assets that were **deferred out of scope** during the workshop deck build. They're parked here for future content work.

### What's pending

From `workshops/internal-review/program-summary.md` (in the git-ape repo), the marketing surfaces called out were:

1. **One-page program flyer** (PDF) — 4-track program at a glance, target audience per track, prerequisites, outcomes. Source for sales / pre-event collateral.

2. **LinkedIn launch posts** — three variants:
   - Executive (audience: VPs of Eng, CTOs) — focus on ROI, risk reduction, governance
   - Practitioner (audience: senior engineers, platform leads) — focus on the security gate + IaC quality
   - Beginner (audience: developers new to Azure/IaC) — focus on "deploy without writing ARM"

3. **Reel / short-form video** (60–90 seconds) — screen-capture of the Track 1 demo, hook in the first 3 seconds, call-to-action to the workshop signup link.

4. **Twitter/X thread** — 8–10 tweets, one per "wow moment" from Track 1 + Track 2 demos. Lead with the security-gate-blocked-deploy moment.

5. **Conference talk abstract** — 200-word abstract + 5-bullet outline pitching a 30-min "Git-Ape: AI-assisted Azure deployments with a security gate that actually blocks" talk.

6. **Internal Microsoft channel post** — Teams/Yammer launch announcement for internal field readiness teams.

### Source material to draw on

- **Track decks** at `git-ape-private/workshops/track-{1,2,3,4}-*/`*`_deck.{pdf,pptx}` — copy hero stats, security-gate language, cost-transparency numbers directly.
- **Guided demo scripts** at `git-ape-private/workshops/track-{1,2,3}-*/guided-demo-script.md` — the talking points are pre-written and audience-tested.
- **FACILITATOR-GUIDE.md** — timing tables and per-audience talking points.

### Recommended content sequence

1. Start with the **LinkedIn practitioner post** — highest-signal audience, fastest to write from existing demo-script copy.
2. Cut a **60-second reel** from a Track 1 demo recording (when one exists at `workshops/shared/recordings/track-1-demo.mp4`).
3. Use the practitioner post + reel as the basis for the **executive post** and the **flyer**.
4. **Conference abstract** is a derivative of the practitioner post — write last.

### Pipeline integration

This repo's existing `content/` workflow (medium-post-* / linkedin-post-* / pipeline-config.md) is the natural place to draft these. Suggested file names:

```
content/linkedin-post-git-ape-practitioner.md
content/linkedin-post-git-ape-executive.md
content/reel-script-git-ape-track1-demo.md
content/twitter-thread-git-ape-launch.md
content/flyer-git-ape-program.md
content/conference-abstract-git-ape.md
```

Follow the same structure as the existing `linkedin-post-part1.md` and `medium-post-part1.md` files for tone and formatting consistency.

---

## Quick-reference build commands

```bash
# Render one deck (all three formats)
cd path/to/deck-folder
npx --yes -p @marp-team/marp-cli marp deck.md --html --allow-local-files -o deck.html
npx --yes -p @marp-team/marp-cli marp deck.md --pdf  --allow-local-files -o deck.pdf
npx --yes -p @marp-team/marp-cli marp deck.md --pptx --allow-local-files -o deck.pptx

# Visually verify PDF
magick -density 130 deck.pdf /tmp/review/slide-%02d.png

# Visually verify PPTX
soffice --headless --convert-to pdf --outdir /tmp/review deck.pptx
magick -density 110 /tmp/review/deck.pdf /tmp/review/pptx-slide-%02d.png

# Confirm speaker notes captured
unzip -p deck.pptx ppt/notesSlides/notesSlide1.xml | grep -oE '<a:t>[^<]+' | head
```

### Required tooling

- Node.js (for `npx` + Marp CLI v4.x)
- ImageMagick (`brew install imagemagick`)
- Ghostscript (`brew install ghostscript`) — required by ImageMagick for PDF rasterization
- LibreOffice (`brew install --cask libreoffice`) — for headless PPTX → PDF conversion

---

_End of playbook._
