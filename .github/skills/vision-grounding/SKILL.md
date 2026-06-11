---
name: vision-grounding
description: "Build grounded, consolidated prompts for AI image generation. Describe reference images with a vision model and assemble a single prompt from subject + creative brief + brand guidelines + constraints. Use before generating any hero/illustrative image."
argument-hint: "Provide the creative brief, brand tokens, and any reference image paths/URLs"
---

# Vision Grounding Skill

## When to Use

Use before `image-content-agent` generates any hero / backdrop / scene / conceptual-
illustration image. Scope is the **AI-generated imagery** visual family only — diagrams,
infographics, flows, comparison matrices, and executive exhibits stay deterministic.

> Methodology adapted from `microsoft/content-generation-solution-accelerator`
> (`docs/IMAGE_GENERATION.md`): a vision model describes a reference image, and that
> description plus the creative brief and brand guidelines is combined into one consolidated
> prompt with explicit safety/style constraints.

## Step 1 — Describe reference images (grounding)

**Prefer your own Copilot vision.** As the `image-content-agent`, open each reference image in
the creative brief (`§7 Visual guidelines → Reference images`) with the `viewImage` tool and
write the description yourself (dominant colors with approximate hex, materials, shapes,
composition, lighting, style). This needs **no external API key or network**.

Use the script only as a **non-interactive / CI fallback** when you cannot view images directly:

```
python -m scripts.visuals.generated.describe --image <path-or-url> \
    --append content/visuals/generated/reference-descriptions.md --label "<label>"
```

Skip this step only when there is no reference image (then ground on the brief alone).

## Step 2 — Assemble the consolidated prompt (the grammar)

Build **one** prompt with these blocks, in order:

```
Create a professional <deliverable> hero image for <topic>.

SUBJECT (maintain accuracy):
<reference description from Step 1, or the brief's subject description>

SCENE / COMPOSITION:
<creative brief §7 visual guidelines: mood, setting, framing; ~30% negative space for overlay>

BRAND STYLE:
- Primary color: ACCENT #1f6feb  (and ACCENT_2 #0d9488 / ACCENT_3 #7c3aed as accents)
- Aesthetic: <brief mood — e.g., clean modern technical, editorial>
- Lighting: professional, soft, high clarity

REQUIREMENTS (hard constraints):
- NO text, words, letters, numbers, logos, or watermarks anywhere in the image
- Honor the brand colors faithfully (no hue substitution)
- Leave ~30% clean negative space for programmatic text overlay
- Photoreal/editorial unless the brief asks for illustration
- Safe-for-work; no real person likeness; no sensitive or unsafe scenes
```

## Constraints (non-negotiable)

1. **No embedded text.** Text and labels are added later programmatically over the negative
   space. State the no-text constraint explicitly in every prompt.
2. **Brand-color fidelity.** Pass token hex values; do not let the model reinterpret them.
3. **Negative space.** Always reserve ~30% for overlay so the asset is usable as a hero.
4. **Safety.** No real-person likeness, no sensitive scenes; flag anything borderline for the
   compliance gate.

## Step 3 — Generate (ai mode)

Pass the consolidated prompt to:

```
python -m scripts.visuals.generated.generate --prompt "<consolidated prompt>" \
    --out content/visuals/generated/<slug>-hero.png
```

Each output carries a sidecar JSON (provider, model, prompt, size, quality, cache key, plus
`mode`, `license`, and `safety_reviewed` provenance fields).

> For the **`programmatic`** mode (the default), there is no prompt grammar — render the backdrop
> directly with `scripts.visuals.generated.programmatic` (see `image-content-agent`). It is
> license-clean by construction and cannot bake in text.

## Step 4 — Deterministic QA pre-screen (mandatory, both modes)

Before the manual/vision review, run the objective inspector:

```
python -m scripts.visuals.generated.inspect_image content/visuals/generated/<slug>-hero.png --theme <theme>
```

It checks **no embedded text** (OCR), **brand-color fidelity** (palette distance), and
**negative-space** ratio, and prints a `GATE: PASS/FAIL`. A FAIL (Error) must be fixed before
handoff.

## License & safety checklist (record in the sidecar)

- `license`: `programmatic` mode is `generated-own (no third-party assets)`; `ai` mode records
  the provider/model and must respect that provider's commercial-use terms.
- `safety_reviewed`: confirm no real-person likeness, no sensitive/unsafe scene. Flag borderline
  cases to the compliance gate rather than publishing.

## Handoff

After the deterministic pre-screen passes, generated images go to `visual-reviewer` for the
section-9 `image-no-text`, `image-fidelity`, and `safety` checks (see
`.github/instructions/shared/compliance-severity.md`). Any **Error** blocks publishing until
regenerated.
