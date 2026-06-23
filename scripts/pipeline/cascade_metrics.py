#!/usr/bin/env python3
"""
Phase D observability for the content review cascade.

Reads the append-only run ledger (content/critique-metrics.md), aggregates the
cascade outcomes across runs, and reports the anti-over-trust metrics:

  - auto-approve rate   = auto_approved / artifacts
  - escalation rate     = escalated / artifacts
  - escalation precision = human_changed / escalated   (of escalated items, how many the human changed)
  - miss rate           = audit_flagged / audited      (sampled auto-approvals an audit later flagged)
  - judge-human agreement = (human_changed + audited - audit_flagged) / (escalated + audited)

Self-regulating stop condition (Section 8 of the proposal): when the miss rate rises
above the agreed threshold, the gate should tighten (lower auto-approve thresholds).
This is surfaced as a FAIL so the orchestrator can act on it.

Ledger row schema (one row per run, all counts non-negative integers):
  | run_id | artifacts | auto_approved | escalated | human_changed | audited | audit_flagged |

Exit codes: 0 = within thresholds, 1 = stop condition tripped (tighten the gate),
2 = configuration/usage/parse error.
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

EXIT_OK = 0
EXIT_TIGHTEN = 1
EXIT_ERROR = 2

DEFAULT_LEDGER = Path("content/critique-metrics.md")
DEFAULT_MAX_MISS_RATE = 0.10
COLUMNS = 7


@dataclass(frozen=True)
class Run:
    run_id: str
    artifacts: int
    auto_approved: int
    escalated: int
    human_changed: int
    audited: int
    audit_flagged: int


def parse_ledger(text: str) -> list[Run]:
    """Parse run rows from the ledger markdown table.

    A data row has exactly COLUMNS pipe-delimited cells, a non-numeric run_id, and
    six integer counts. Header, separator, and prose rows are skipped.
    """
    runs: list[Run] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != COLUMNS:
            continue
        run_id = cells[0]
        if not run_id or set(cells[1]) <= set("-: "):
            continue  # separator row
        try:
            counts = [int(c) for c in cells[1:]]
        except ValueError:
            continue  # header or prose row
        if any(n < 0 for n in counts):
            raise ValueError(f"negative count in run row: {line}")
        runs.append(Run(run_id, *counts))
    return runs


def _rate(numerator: int, denominator: int) -> float | None:
    return numerator / denominator if denominator else None


def _fmt(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.0%}"


def aggregate(runs: list[Run]) -> dict[str, float | None]:
    artifacts = sum(r.artifacts for r in runs)
    auto = sum(r.auto_approved for r in runs)
    escalated = sum(r.escalated for r in runs)
    changed = sum(r.human_changed for r in runs)
    audited = sum(r.audited for r in runs)
    flagged = sum(r.audit_flagged for r in runs)
    agreements = changed + (audited - flagged)
    labeled = escalated + audited
    return {
        "auto_approve_rate": _rate(auto, artifacts),
        "escalation_rate": _rate(escalated, artifacts),
        "escalation_precision": _rate(changed, escalated),
        "miss_rate": _rate(flagged, audited),
        "judge_human_agreement": _rate(agreements, labeled),
    }


def render_report(scope: str, runs: list[Run], metrics: dict[str, float | None],
                  max_miss_rate: float, tighten: bool) -> str:
    miss = metrics["miss_rate"]
    lines = [
        "## Cascade metrics (Phase D)",
        "",
        f"Scope: {scope} ({len(runs)} run(s))",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Auto-approve rate | {_fmt(metrics['auto_approve_rate'])} |",
        f"| Escalation rate | {_fmt(metrics['escalation_rate'])} |",
        f"| Escalation precision | {_fmt(metrics['escalation_precision'])} |",
        f"| Miss rate (sampled audit) | {_fmt(miss)} |",
        f"| Judge-human agreement | {_fmt(metrics['judge_human_agreement'])} |",
        "",
        f"Miss-rate threshold: {max_miss_rate:.0%}",
        "",
    ]
    if miss is None:
        lines.append(
            "GATE: PASS - no sampled audits yet; record audits to measure drift.")
    elif tighten:
        lines.append(
            "GATE: FAIL - miss rate exceeds threshold. Tighten the gate: lower the "
            "Tier 1/Tier 3 auto-approve bar and widen sampled audits until it recovers.")
    else:
        lines.append("GATE: PASS - miss rate within threshold.")
    return "\n".join(lines)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Phase D observability metrics for the content review cascade.")
    parser.add_argument("ledger", nargs="?", type=Path, default=DEFAULT_LEDGER,
                        help=f"Run ledger to read (default: {DEFAULT_LEDGER}).")
    parser.add_argument("--window", type=int, metavar="N",
                        help="Aggregate only the last N runs (drift view).")
    parser.add_argument("--max-miss-rate", type=float, default=DEFAULT_MAX_MISS_RATE,
                        help=f"Stop-condition threshold (default: {DEFAULT_MAX_MISS_RATE}).")
    parser.add_argument("-o", "--output", type=Path,
                        help="Write the report to this file as well as stdout.")
    return parser


def main() -> int:
    args = create_parser().parse_args()

    if not args.ledger.exists():
        print(f"Ledger not found: {args.ledger}", file=sys.stderr)
        return EXIT_ERROR
    if args.window is not None and args.window <= 0:
        print("--window must be a positive integer.", file=sys.stderr)
        return EXIT_ERROR

    try:
        runs = parse_ledger(args.ledger.read_text(encoding="utf-8"))
    except ValueError as exc:
        print(f"Cannot parse ledger: {exc}", file=sys.stderr)
        return EXIT_ERROR

    if not runs:
        print("No run rows recorded yet in the ledger.", file=sys.stderr)
        return EXIT_ERROR

    scope = "all runs"
    if args.window is not None and args.window < len(runs):
        runs = runs[-args.window:]
        scope = f"last {args.window} runs"

    metrics = aggregate(runs)
    miss = metrics["miss_rate"]
    tighten = miss is not None and miss > args.max_miss_rate

    report = render_report(scope, runs, metrics, args.max_miss_rate, tighten)
    print(report)

    if args.output:
        args.output.write_text(report + "\n", encoding="utf-8")

    return EXIT_TIGHTEN if tighten else EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
