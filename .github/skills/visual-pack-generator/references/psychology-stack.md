# Psychology Stack Reference

Maps 12 psychology and marketing frameworks to slide positions, content patterns, and practical application rules. Load this file alongside slide-grammar.md to apply the correct persuasion layer to each slide/exhibit during generation.

---

## The 12 Frameworks — Quick Reference

| # | Framework | One-line Description | Primary Slide Position |
|---|-----------|---------------------|----------------------|
| 1 | Curiosity Gap | Open a question the reader must close to feel resolution | Hook (position 1) |
| 2 | Zeigarnik Effect | Incomplete information is more memorable and drives continued engagement | Hook, Promise (positions 1–2) |
| 3 | IKEA Effect | Engagement through co-creation and active participation increases perceived value | CTA (position 10) |
| 4 | Von Restorff Isolation | Visually distinct elements in a series are remembered disproportionately | Hook, Pattern Interrupt (positions 1, 8) |
| 5 | Processing Fluency | Easier-to-process content is judged more credible and more true | All slides (consistent visual style throughout) |
| 6 | AIDA | Attention -> Interest -> Desire -> Action — classic persuasion arc | Framework (4), Solution steps (5–7) |
| 7 | SUCCESs | Simple, Unexpected, Concrete, Credible, Emotional, Stories — Heath brothers' stickiness model | Problem (3), Solution (5–7) |
| 8 | Cialdini Influence | Authority, Social Proof, Reciprocity, Commitment, Scarcity, Liking — six persuasion levers | Solution steps (5–7), CTA (10) |
| 9 | Dual-Coding Theory | Text + visuals processed in parallel = 323% better comprehension vs text alone | Problem (3), Framework (4) |
| 10 | Peak-End Rule | Experiences are judged by their peak moment and their ending — not the average | Hook (1), CTA (10) |
| 11 | Concrete Language | Specific details ("$2,400/day" not "expensive") beat abstract claims ("significant cost") | All data-bearing slides |
| 12 | Big Idea | One memorable, ownable takeaway per piece — the thesis the audience retells | Hook (1), Recap (9) |

---

## Optimal Psychology Stack Per Slide Position

Apply these stacks when generating slide content in Step 5 of the procedure.

| Position | Primary Frameworks | Secondary | Practical Application |
|----------|-------------------|-----------|----------------------|
| **Slide 1 — Hook** | Curiosity Gap + Von Restorff + Peak-End (peak) | Processing Fluency | Giant number or bold claim that stops the scroll. Open the question — don't answer it. Example: "Your AI bill is 3× what it should be." Dark BG enforces Von Restorff isolation against white slides 2–9. |
| **Slide 2 — Promise** | Processing Fluency + Zeigarnik Effect | AIDA (Attention) | List what the reader will learn. Zeigarnik: they've started; now they need to finish to close the loop. Keep it scannable — 3 to 5 short bullet promises. |
| **Slide 3 — Problem** | SUCCESs (Unexpected + Concrete) + Dual-Coding | AIDA (Interest), Zeigarnik | Surprising quantified data point + supporting visualization. Don't resolve the curiosity — deepen it. "Most teams don't know this is happening." |
| **Slides 4–6 — Framework + Steps 1–3** | Cialdini (Authority + Social Proof) + SUCCESs (Credible) | AIDA (Desire), Dual-Coding | Named tools, named companies, verified benchmarks, team sizes. Credibility signals: "Google uses this", "RouteLLM reduced costs 68% in 90 days at Mistral". Diagram encodes authority. |
| **Slide 7 — Step 3** | SUCCESs (Credible + Concrete) | Cialdini (Social Proof) | Third step closes the "how-to" arc. Include the most concrete, actionable instruction. Specific tool name + specific outcome metric. |
| **Slide 8 — Pattern Interrupt** | Von Restorff + SUCCESs (Emotional) | Concrete Language | Dark background breaks the visual rhythm of slides 2–7. Large pull-quote with human stakes. Example: "That $2K/day waste? It's someone's engineering salary for a month." Emotional + concrete. |
| **Slide 9 — Recap** | Peak-End (approach end) + Big Idea | Processing Fluency | Checklist of 3–5 key points creates a completion urge (Zeigarnik closure). The final checklist is the Big Idea made memorable. Use `[x]` ASCII markers. |
| **Slide 10 — CTA** | Peak-End (end) + Cialdini (Commitment + Reciprocity) | Big Idea, IKEA Effect | Last slide = the "end" in Peak-End — make it strong. Reciprocity: "I shared this for free; save it if it helped." Commitment: "Save this -> Read the full guide -> Link in comments". IKEA Effect: invite action (save, share) so the reader becomes invested. |

### Psychology Arc Summary (Practitioner)

```
Curiosity Gap (1) -> Zeigarnik loop opened (2) -> Unexpected data deepens loop (3)
-> Authority + Credibility builds trust (4-7)
-> Emotional peak breaks pattern (8)
-> Zeigarnik loop closed via checklist (9)
-> Reciprocity + Commitment triggers action (10)
```

---

## Executive Mode Psychology Stack

Simpler stack — credibility and decision-support first. No emotional manipulation; senior audiences have high BS detection.

| Position | Framework | Application |
|----------|-----------|-------------|
| **Exhibit 1 — Context** | Concrete Language + Von Restorff | Lead with the cost or risk number. Conclusion-as-title states the finding directly: "AI inference costs vary 120× across model tiers — most teams default to the most expensive." The number is the Von Restorff element. |
| **Exhibit 2 — Evidence** | Cialdini (Authority) + Processing Fluency | Named sources — Anthropic, Google, Microsoft Research, peer-reviewed data. Clean data-ink ratio is a Processing Fluency signal: high data-ink ratio = expertise. Remove all chart chrome that doesn't carry data. |
| **Exhibit 3 — Framework** | Dual-Coding + AIDA (Interest -> Desire) | The framework visual does double duty: it encodes the recommendation AND implies the expertise behind it. A clean flow or decision tree with named components (RouteLLM, LiteLLM) = authority. |
| **Exhibit 4 — ROI** | Cialdini (Scarcity + Commitment) + Big Idea | Quantify the opportunity cost of inaction. Scarcity: "Every month without routing is $X in preventable spend." Commitment: showing the ROI invites the reader to mentally commit to the approach. |
| **Exhibit 5 — Action** | Concrete Language + Cialdini (Commitment) | One clear recommendation per exhibit. Action-oriented language. Specific tools, steps, owners, timelines. No hedging ("may potentially") — replaces every vague verb with a named action. |

---

## Anti-Patterns to Avoid (Both Modes)

These patterns actively undermine persuasion effectiveness. Flag and fix any occurrence during generation.

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Vague claims: "significantly better", "much faster", "greatly reduced" | Violates Concrete Language + SUCCESs (Concrete) | Replace with exact number: "68% reduction in 90 days" — source + year |
| Hedged language: "can potentially", "may help", "could possibly" | Signals low confidence; undermines Cialdini (Authority) | Replace with named case study + benchmark: "RouteLLM reduced Mistral's inference cost by 68% in 90 days" |
| Text-heavy slides: more than 50 words body text per slide | Violates Processing Fluency; reduces dwell quality | Split into two slides; move excess to body copy of the post |
| Multiple insights per slide | Violates Big Idea rule; dilutes Peak-End peak | One insight per slide — if two are needed, add a slide |
| Missing attribution | Violates SUCCESs (Credible); loses Cialdini (Authority) | Every statistic includes source name + year directly on the slide |
| Cross-reference language: "as we saw above", "from the previous slide" | Breaks standalone comprehension; confuses out-of-context shares | Rewrite every slide to be self-contained |
| CTA on Executive exhibits | Signals promotional intent to senior audience; undermines credibility | Remove CTA from exhibit visual entirely; place in post body copy and captions |
| Unattributed "data" without a named source | Senior audiences treat unattributed data as opinion | Requires: specific publication/researcher, year, methodology note if relevant |
| Abstract titles on exhibits: "Model Cost Analysis", "Performance Data" | Violates Conclusion-as-title convention; forces reader to do interpretive work | Rewrite as conclusion: "Model cost varies 120× — routing captures 68% of the savings" |
| Generic CTAs: "Click here", "Learn more", "Follow for more" | Violates Cialdini (Reciprocity) framing; feels transactional | Use value-framed CTAs: "Save this before your next model selection" / "Full cost calculator — link in comments" |

---

## Hook Quality Checklist

Before finalizing Slide 1 (Practitioner) or the Context Exhibit title (Executive), verify:

- [ ] Contains a specific number (not "many" or "significant")
- [ ] Opens a question the reader must continue to close (Curiosity Gap)
- [ ] Visually distinct from slides 2–9 (Von Restorff — dark background or giant number)
- [ ] Comprehensible in under 3 seconds of viewing time
- [ ] ≤15 words total on the slide (Practitioner) or ≤12 words in exhibit title (Executive)
- [ ] Does NOT give away the answer (that comes in slides 4–7 / exhibits 2–3)
- [ ] Passes the "thumb-stop test" — would a reader scrolling LinkedIn at 1.5× speed pause?

---

## Credibility Signal Checklist

Apply to all data-bearing slides (positions 3–7 Practitioner / exhibits 1–3 Executive):

- [ ] Named tool, company, or researcher (not "a major cloud provider")
- [ ] Specific metric with unit ("$2,400/day" not "high cost")
- [ ] Year of data ("2025 model pricing" not "recent data")
- [ ] Sample size or study scope when available ("1.3M posts" not "analyzed posts")
- [ ] Source attribution visible on the slide/exhibit (not just in caption)
