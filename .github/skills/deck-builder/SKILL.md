---
name: deck-builder
description: Build an optional presentation deck from finalized blog + LinkedIn content. Generates a Marp Markdown deck with per-slide speaker notes written in a humor + intellectual voice and tagged by topic, lets the user finalize the deck, then exports both PPTX and PDF. Use only after the blog and LinkedIn post are finalized; this is an optional distribution output, never a gate.
---

# Deck Builder (Optional PPTX + PDF)

STORM-free, deterministic deck generation. This skill turns finalized written content
into a slide deck with rich speaker notes, then exports it to **both** PPTX and PDF using
the Marp CLI. It is an **optional** step — skipping it never blocks publishing.

> Read `docs/marp-deck-playbook-and-git-ape-marketing-followup.md` (lessons L1–L15) before
> running. Every Marp gotcha below was learned the hard way; follow the rules literally.

## When to use

- **Only after** the blog post (`content/<topic>.md`) **and** the LinkedIn post are finalized
  and have passed the quality gate. The deck distills finished work; it does not create new claims.
- When the user explicitly opts in (it is offered in the orchestrator's platform-selection menu).

## Inputs (read, do not modify)

| Input | Path | Use |
|-------|------|-----|
| Finalized blog | `content/<topic>.md` | Primary narrative, section structure, data points |
| LinkedIn post | `content/linkedin-post*.md` | Hook, framing, one-liners for the title/closing slides |
| Creative brief | `content/creative-brief.md` | Audience, tone, key message, guardrails |
| Visuals | `content/visuals/*.png` (and `*.svg`) | Reuse existing rendered assets on slides |
| Design tokens | `.github/copilot-instructions.md` | Palette + Helvetica Neue for theme CSS |

## Output files

Write everything under `content/deck/`:

| File | Purpose |
|------|---------|
| `content/deck/<topic>-deck.md` | Marp Markdown source (slides + speaker notes) |
| `content/deck/<topic>-deck.pdf` | Exported PDF deck |
| `content/deck/<topic>-deck.pptx` | Exported PPTX deck (speaker notes land in notes pane) |
| `content/deck/_verify/slide-*.png` | Rasterized slides for visual verification (L9) |

## Procedure

### Phase A — Build and finalize the deck Markdown (gate before export)

1. Derive a slide spine from the blog's H2/H3 structure: title slide, agenda/topics,
   one slide per major section, a data/exhibit slide reusing an existing visual where one
   fits, and a closing/CTA slide. Target 8–14 slides; never pad with filler (L7: the slide
   count must match any "N slides" pill).
2. Pull slide bodies from the finalized blog — distill, do not rewrite the argument. Keep
   on-slide text terse (headline + 3–5 bullets or one metric block). Detail belongs in the
   speaker notes, not on the slide.
3. Reference existing visuals as **external files** only — never inline `<svg>` (L1, L2).
   Use `![alt](../visuals/<name>.png)` or an `<img src="../visuals/<name>.svg" .../>` tag.
4. Add **per-slide speaker notes** following the Speaker Notes Style below.
5. Apply the Marp rules (next section).
6. **Present the deck Markdown to the user and ask them to finalize/approve.** Do not export
   until the user confirms the deck content and speaker notes. This finalize step is mandatory.

### Phase B — Export to PPTX + PDF (after user finalizes)

7. Run the full triple-render every time (L8 — a fix that lands in one format can break another):

   ```bash
   npx --yes -p @marp-team/marp-cli marp content/deck/<topic>-deck.md --html --allow-local-files -o content/deck/<topic>-deck.html
   npx --yes -p @marp-team/marp-cli marp content/deck/<topic>-deck.md --pdf  --allow-local-files -o content/deck/<topic>-deck.pdf
   npx --yes -p @marp-team/marp-cli marp content/deck/<topic>-deck.md --pptx --allow-local-files -o content/deck/<topic>-deck.pptx
   ```

8. **Verify visually, not by file size (L9).** Rasterize and inspect:

   ```bash
   magick -density 130 content/deck/<topic>-deck.pdf content/deck/_verify/slide-%02d.png
   ```

9. **Verify speaker notes landed in the PPTX.** Unzip and confirm `ppt/notesSlides/notesSlide*.xml`
   contain the note text (L3). If notes are missing, they were written with leading dashes or a
   blank line — rewrite as single-line prose and re-export.
10. Report the file inventory and any tooling that was missing (see Tooling), then update
    `content/pipeline-config.md` (mark the optional deck step done; record slide count + formats).

## Speaker Notes Style (humor + intellectual, topic-tagged)

Every slide gets one speaker-note comment. The note must:

- Open with a **topic tag**, then deliver the substance in a **humor + intellectual** voice —
  a sharp, well-reasoned point delivered with a wry, self-aware aside. Smart first, funny second;
  never slapstick, never at the audience's expense.
- Be **single-line prose** — no bullet lists, no leading `-`, no blank lines inside the comment
  (L3: Marp's parser eats dashed lines and blank lines inside note comments).
- Keep Marp directive comments (`<!-- _class: lead -->`) in a **separate** comment block from the
  speaker-note comment (L11), or the directive gets swallowed.

Format per slide:

```markdown
<!-- _class: lead -->

<!-- Topic: Cold-start cost — Reviewers love to blame the model for slow pipelines, but the meter
runs on context you forgot to trim; the punchline is that the cheapest optimization is usually the
one you were too busy to make. -->
```

Tone calibration: think "a senior engineer narrating their own war story" — precise on the
technical claim, dry on the human one. One witty turn per note is plenty; if a note has two jokes,
cut one and keep the insight.

## Marp rules (from the playbook — apply literally)

- **L1 / L2** — Externalize all SVGs; strip blank lines inside any inline HTML block.
- **L3** — Speaker notes are single-line prose (verified in `ppt/notesSlides/`).
- **L8** — Re-render HTML + PDF + PPTX after every change.
- **L9** — Inspect rasterized slides; file size is not a quality signal.
- **L11** — Directive comments and note comments live in separate `<!-- -->` blocks.
- **L12** — Image/logo paths are relative to the deck file (`../visuals/...`), not the repo root.
- **L15** — Strip a trailing `---` so no empty final slide is created.
- Theme: use the design-token palette and Helvetica Neue; pair every dark rule with a
  `section.light` counterpart (L4) and override Marp code styling with `!important` (L13).

## Tooling

The export needs Node (for `npx @marp-team/marp-cli`). Rasterizing the PDF needs ImageMagick +
Ghostscript; rasterizing the PPTX path needs LibreOffice. If any are missing, report the exact
install command and still deliver the deck Markdown + whichever formats succeeded:

```bash
brew install ghostscript
brew install --cask libreoffice
```

## Constraints

- This step is **optional** and runs **after** the blog and LinkedIn post are finalized. Never
  treat it as a publishing gate; skipping it must not block any other step.
- Do **not** invent data, claims, or examples. The deck only distills finalized content.
- Do **not** export until the user finalizes the deck Markdown and speaker notes (Phase A gate).
- Always produce **both** PPTX and PDF when export tooling is available.
