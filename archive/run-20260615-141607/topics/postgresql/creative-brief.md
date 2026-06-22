# Creative Brief — PostgreSQL × AI performance

| Field | Value |
|-------|-------|
| **Topic** | How AI actually helps solve PostgreSQL performance problems (with real examples) |
| **Status** | `approved` |
| **Author voice** | First-person practitioner — "sharing what I've seen work with customers' Postgres fleets" |

## 1. Overview
A field guide for DBAs and data engineers on where AI genuinely shortens the Postgres
performance loop — triage, root-cause from `EXPLAIN`/stats, query rewriting, index advice,
and anomaly detection — and, just as importantly, where it confidently lies. Grounded in real
Postgres mechanics and real tools, not hype.

## 2. Objectives
- Primary: give DBAs a concrete, trustworthy mental model for using LLMs/AI tools in the
  diagnose → root-cause → fix → validate performance workflow.
- Secondary: show real before/after examples; call out failure modes (hallucinated internals,
  stale defaults, unvalidated index advice).

## 3. Target audience
- **Primary:** DBAs and data engineers running Postgres in production (RDS/Aurora/self-managed).
- **Secondary:** backend tech leads who own database performance.

## 4. Key message
AI won't replace your `EXPLAIN ANALYZE` skills — but pointed at the right steps (triage, query
rewriting, index suggestions, anomaly detection), and *grounded in your real stats*, it cuts the
diagnose-to-fix loop from hours to minutes. Here's where it works, where it lies, and how to
keep a human in the loop.

## 5. Tone & style
Practitioner field guide. Conversational, data-driven, honest about limits. No vendor hype, no
"AI replaces DBAs" framing.

## 6. Deliverables
Single ~2,800–3,200-word blog · LinkedIn post · Reel/Short script · programmatic hero image.

## 7. Visual guidelines
- **Mood:** clean, technical, editorial; brand palette (ACCENT `#1f6feb`, ACCENT_2 `#0d9488`).
- **Hero:** programmatic backdrop (`scripts.visuals.generated.programmatic`) + CSS title overlay.
- **Deterministic diagrams/charts:** the diagnose→fix loop, a "where AI helps vs hurts" matrix,
  and a before/after latency chart. matplotlib for the chart; HTML/CSS for the diagram/matrix.
- No embedded text in the hero backdrop; brand-color fidelity.

## 8. Call to action
Try one AI-assisted step on a real slow query this week (feed it `EXPLAIN (ANALYZE, BUFFERS)`),
validate the suggestion, and keep your stats grounded. Follow for the next deep-dive.

## 9. Constraints & guardrails
- Every claim needs a concrete number, tool name, or mechanism; case study metrics may be
  clearly labelled illustrative/composite but must be mechanically realistic.
- Cite real tools/mechanisms: `EXPLAIN (ANALYZE, BUFFERS)`, `pg_stat_statements`, `auto_explain`,
  `pg_stat_activity`, autovacuum, HNSW/IVFFlat (pgvector), pganalyze, AWS DevOps Guru for RDS,
  RDS Performance Insights, Postgres MCP servers, Amazon Q.
- Be explicit about LLM failure modes on Postgres internals (the "teach an LLM what it doesn't
  know about Postgres" problem).
