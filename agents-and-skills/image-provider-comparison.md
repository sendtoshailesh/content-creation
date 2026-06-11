# AI Image Provider Comparison & Decision

> Decision input for the **`ai` mode** of the hero/illustrative imagery capability (hero /
> backdrop / scene / conceptual-illustration assets only). Diagrams, infographics, flows,
> comparison matrices, and executive exhibits remain deterministic/programmatic and are out of
> scope for image generation.
>
> **You only need this doc if you opt into `ai` mode.** The **default** is
> `mode: programmatic` — deterministic backdrops rendered by
> `scripts.visuals.generated.programmatic` with no API key, no network, and no cost. Choose `ai`
> only when you need a true photoreal/illustrative look that CSS backdrops cannot deliver.
>
> **Methodology source:** adapted from
> [`microsoft/content-generation-solution-accelerator`](https://github.com/microsoft/content-generation-solution-accelerator)
> (`docs/IMAGE_GENERATION.md`), which generates marketing imagery via Azure OpenAI
> `gpt-image-1.5` / `gpt-image-1-mini`.

## Candidates

| Provider / model | SDK | Best for | Text-in-image | Commercial use |
|------------------|-----|----------|---------------|----------------|
| **Azure OpenAI** `gpt-image-1` | `openai` (Azure config) | Enterprise compliance, same path as reference repo | Good (we forbid it anyway) | Yes |
| **Azure OpenAI** `gpt-image-1-mini` | `openai` (Azure config) | Cheaper/faster budget tier | Adequate | Yes |
| **OpenAI** `gpt-image-1` | `openai` | Lowest setup friction, transparent pricing | Good | Yes |
| **Stability AI** (SD 3.5 / Core) | `requests` / `stability-sdk` | Stylized/artistic illustration, lowest cost | Weak | Yes (check plan) |
| **Google** `imagen-3` (Gemini API) | `google-genai` | Photoreal, strong prompt adherence | Good | Yes |

## Pricing (verify before committing — rates change)

**OpenAI `gpt-image-1` (per image, authoritative as of mid-2025):**

| Size | Low | Medium | High |
|------|-----|--------|------|
| 1024×1024 | $0.011 | $0.042 | $0.167 |
| 1024×1536 / 1536×1024 | $0.016 | $0.063 | $0.250 |

Token-based alternative billing: input $10 / 1M, cached input $2.50 / 1M, output $40 / 1M.

**Azure OpenAI `gpt-image-1` / `gpt-image-1-mini`:** per-image rates were not separately
published at the time of writing; Azure typically matches or runs ~10–25% above OpenAI's
direct rates, and `-mini` is the budget tier. **Verify on the
[Azure OpenAI pricing page](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/)
and your subscription/region.**

**Stability AI:** credit-based, typically <$0.01–0.04/image depending on model.
**Google Imagen 3:** see the [Gemini API pricing page](https://ai.google.dev/pricing).

## Selection criteria for this pipeline

1. **Reproducibility** — does the API accept/return a seed? (We store it in the sidecar.)
2. **No-text fidelity** — we forbid embedded text; any model works, but cleaner is better.
3. **Brand-color fidelity** — how well it honors hex/color guidance in the prompt.
4. **Setup friction** — keys, endpoint, API version, region availability.
5. **Cost at our volume** — typically 1–3 hero images per run; default to the cheaper tier.
6. **Content safety** — built-in moderation + our no-human-likeness/sensitive-scene flag.

## Recommendation

- **Default:** **OpenAI `gpt-image-1`** at **medium** quality, **1024×1024** — lowest setup
  friction (single `OPENAI_API_KEY`), transparent per-image pricing (~$0.04/image), and the
  same `openai` SDK Azure uses, so switching to Azure later is a config change only.
- **Enterprise / reference-parity fallback:** **Azure OpenAI `gpt-image-1-mini`** when an
  Azure subscription + compliance posture is required.
- **Stylized-illustration alternative:** **Stability** for non-photoreal, low-cost art.

The provider is selected via `IMAGE_PROVIDER` / `IMAGE_MODEL_NAME` in `.env` and recorded in
`content/pipeline-config.md` → **Image Generation** block. The adapter
(`scripts/visuals/generated/provider.py`) keeps OpenAI and Azure OpenAI behind one interface.

## User decision

| Field | Value |
|-------|-------|
| **Chosen provider** | _(fill in: openai / azure_openai / stability / google)_ |
| **Chosen model** | _(e.g. gpt-image-1, gpt-image-1-mini)_ |
| **Default size / quality** | _(e.g. 1024×1024 / medium)_ |
| **Decided on** | _(date)_ |
