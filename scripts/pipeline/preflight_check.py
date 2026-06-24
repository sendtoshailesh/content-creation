#!/usr/bin/env python3
"""
Tier 0 deterministic preflight for the content pipeline.

Runs zero-cost, no-LLM checks over content artifacts and visual renderers, then
emits the shared compliance-severity findings table plus a GATE verdict. A FAIL
returns the artifact to its producer before any LLM-based critic tier runs.

Checks (deterministic only):
  Markdown content (.md)
    - broken local links / image paths (claim-citation, accessibility)
    - empty image alt text (accessibility)
    - source attributions without an inline link (claim-citation)
    - banned corporate phrases (voice)
    - heading hygiene: exactly one H1 (layout)
    - word-count band for blog posts (messaging)
  Visual renderers (.py under a visuals/ path)
    - non-token hex colors (design-token)
    - matplotlib savefig without dpi=320 (design-token)
    - Unicode glyphs in string literals that break matplotlib (typography)

Exit codes: 0 = GATE PASS, 1 = GATE FAIL, 2 = configuration/usage error.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

EXIT_PASS = 0
EXIT_FAIL = 1
EXIT_ERROR = 2

# --- Design tokens (mirror of visual-standards.instructions.md) ----------------
# Base tokens + every theme palette hex are valid; plus pure black/white.
ALLOWED_HEX: frozenset[str] = frozenset(
    h.lower()
    for h in {
        "#000000", "#ffffff",
        # base
        "#1e293b", "#475569", "#94a3b8", "#e5e7eb", "#f8fafc",
        # default
        "#1f6feb", "#0d9488", "#7c3aed", "#dc2626", "#16a34a",
        "#dbeafe", "#ccfbf1", "#ede9fe", "#fee2e2",
        # ocean
        "#0ea5e9", "#06b6d4", "#155e75", "#f97316", "#14b8a6",
        "#e0f2fe", "#cffafe", "#ffedd5",
        # sunset
        "#ef4444", "#b91c1c", "#eab308", "#fff7ed", "#fef3c7", "#fef2f2",
        # forest
        "#65a30d", "#a16207", "#ca8a04", "#15803d", "#f0fdf4",
        "#ecfccb", "#fefce8", "#fef9c3",
        # midnight
        "#6366f1", "#8b5cf6", "#ec4899", "#a78bfa", "#e0e7ff",
        "#fae8ff", "#fce7f3",
    }
)

REQUIRED_DPI = 320
BLOG_MIN_WORDS = 600

# Corporate / off-voice phrases (writing-style). Word-boundary, case-insensitive.
BANNED_PHRASES: tuple[str, ...] = (
    "leverage", "synergy", "synergies", "game-changer", "game changer",
    "revolutionize", "revolutionary", "seamless", "seamlessly", "cutting-edge",
    "delve", "in today's fast-paced world", "unlock the power",
    "harness the power", "elevate your", "best-in-class", "world-class",
    "paradigm shift", "low-hanging fruit", "move the needle", "boil the ocean",
)

# Unicode glyphs the visual standard bans in matplotlib (use ASCII equivalents).
# Scoped to arrows and check/cross marks; em-dash/bullet/ellipsis render fine.
BANNED_GLYPHS: tuple[str, ...] = ("→", "←", "↑", "↓", "✓", "✗", "✔", "✘", "☑", "☒")

HEX_RE = re.compile(r"#[0-9a-fA-F]{6}\b")
MD_LINK_RE = re.compile(r"!?\[(?P<text>[^\]]*)\]\((?P<target>[^)\s]+)(?:\s+\"[^\"]*\")?\)")
SAVEFIG_RE = re.compile(r"\.savefig\s*\(")
STRING_LITERAL_RE = re.compile(r"(['\"])(?P<body>(?:\\.|(?!\1).)*)\1")

# Source-attribution guard (claim-citation). Flags parenthetical citations that
# name a publisher/author + year but carry NO inline link to the primary source.
# Precise token list keeps false positives near zero; bare date parens like
# "(Jun 2026)" or "(2022-2024)" are intentionally allowed.
SOURCE_TOKENS: tuple[str, ...] = (
    "infoq", "stripe", "anthropic", "openai", "böckeler", "bockeler",
    "willison", "morris", "circleci", "swebench", "swe-bench", "fowler",
    "thoughtworks", "dropbox", "github", "arxiv", "deepmind", "google",
    "microsoft", "apple", "meta", "nvidia", "gartner", "mckinsey", "redmonk",
    "stack overflow", "stackoverflow", "techcrunch", "the verge", "wired",
)
CITATION_PAREN_RE = re.compile(r"\(([^()]*?\b(?:19|20)\d{2}\b[^()]*?)\)")

VISUAL_PATH_HINT = "visuals"


@dataclass(frozen=True)
class Finding:
    severity: str  # Error | Warning | Info
    category: str
    location: str
    finding: str
    fix: str


def _line_for(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def check_markdown(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")
    rel = path.as_posix()
    lower = text.lower()

    # Links and images.
    for m in MD_LINK_RE.finditer(text):
        target = m.group("target")
        is_image = m.group(0).startswith("!")
        line = _line_for(text, m.start())
        loc = f"{rel}:{line}"

        if is_image and not m.group("text").strip():
            findings.append(Finding(
                "Warning", "accessibility", loc,
                "Image has empty alt text",
                "Add descriptive alt text inside the [] brackets",
            ))

        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if target.startswith("<") or "{{" in target:
            continue  # templated / angle-bracket autolink, skip

        clean = target.split("#", 1)[0].split("?", 1)[0]
        if not clean:
            continue
        candidates = [path.parent / clean, Path.cwd() / clean]
        if not any(c.exists() for c in candidates):
            sev = "Error" if is_image else "Warning"
            kind = "Broken image path" if is_image else "Broken local link"
            findings.append(Finding(
                sev, "claim-citation", loc,
                f"{kind}: {target} not found",
                "Fix the path or generate the missing asset",
            ))

    # Banned phrases.
    for phrase in BANNED_PHRASES:
        for m in re.finditer(rf"\b{re.escape(phrase)}\b", lower):
            line = _line_for(text, m.start())
            findings.append(Finding(
                "Warning", "voice", f"{rel}:{line}",
                f"Off-voice phrase: \"{phrase}\"",
                "Reword to plain practitioner voice",
            ))

    # Heading hygiene: exactly one H1.
    h1_count = len(re.findall(r"^#\s+\S", text, flags=re.MULTILINE))
    if h1_count != 1:
        findings.append(Finding(
            "Warning", "layout", rel,
            f"Document has {h1_count} H1 headings (expected exactly 1)",
            "Use a single H1 title; demote extras to H2",
        ))

    # Word-count band for blog posts.
    if _looks_like_blog(path):
        words = len(re.findall(r"\b\w+\b", text))
        if words < BLOG_MIN_WORDS:
            findings.append(Finding(
                "Warning", "messaging", rel,
                f"Blog post is {words} words (< {BLOG_MIN_WORDS} minimum)",
                "Expand with concrete data, examples, or a case study",
            ))

    # Source attributions must carry an inline link to the primary source.
    for m in CITATION_PAREN_RE.finditer(text):
        start = m.start()
        if start > 0 and text[start - 1] == "]":
            continue  # this paren is a Markdown link target, e.g. [text](url)
        inner = m.group(1)
        if "](" in inner or "://" in inner:
            continue  # already wraps an inline link / is a URL
        low = inner.lower()
        if any(tok in low for tok in SOURCE_TOKENS) or " via " in low or "et al" in low:
            line = _line_for(text, start)
            findings.append(Finding(
                "Warning", "claim-citation", f"{rel}:{line}",
                f"Source attribution without inline link: ({inner.strip()})",
                "Wrap the citation in a Markdown link to the primary source URL",
            ))

    return findings


def _looks_like_blog(path: Path) -> bool:
    name = path.name.lower()
    if path.parent.name != "content":
        return False
    skip = ("strategy", "pipeline", "linkedin", "reel", "reddit", "twitter",
            "youtube", "reference", "brief", "map", "queue", "log", "config",
            "proposal", "feed-sources")
    return not any(s in name for s in skip)


def check_renderer(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8")
    rel = path.as_posix()

    for m in HEX_RE.finditer(text):
        hex_val = m.group(0).lower()
        if hex_val not in ALLOWED_HEX:
            line = _line_for(text, m.start())
            findings.append(Finding(
                "Warning", "design-token", f"{rel}:{line}",
                f"Non-token color {m.group(0)}",
                "Use a design-token hex from visual-standards, or justify",
            ))

    if SAVEFIG_RE.search(text) and f"dpi={REQUIRED_DPI}" not in text.replace(" ", ""):
        findings.append(Finding(
            "Warning", "design-token", rel,
            f"savefig() present without dpi={REQUIRED_DPI}",
            f"Pass dpi={REQUIRED_DPI} to every savefig call",
        ))

    for m in STRING_LITERAL_RE.finditer(text):
        body = m.group("body")
        for glyph in BANNED_GLYPHS:
            if glyph in body:
                line = _line_for(text, m.start())
                findings.append(Finding(
                    "Error", "typography", f"{rel}:{line}",
                    f"Unicode glyph '{glyph}' in a string literal",
                    "Replace with ASCII (-> , [x], [ ]); glyphs break matplotlib",
                ))
                break

    return findings


def _is_renderer(path: Path) -> bool:
    return path.suffix == ".py" and VISUAL_PATH_HINT in path.as_posix().lower()


def collect_targets(paths: list[Path]) -> list[Path]:
    if paths:
        out: list[Path] = []
        for p in paths:
            if p.is_dir():
                out.extend(sorted(p.rglob("*.md")))
                out.extend(sorted(p.rglob("*.py")))
            else:
                out.append(p)
        return out
    # Default discovery: content markdown + visual renderers.
    out = sorted(Path("content").glob("*.md")) if Path("content").exists() else []
    for base in (Path("content/visuals"), Path("scripts/visuals")):
        if base.exists():
            out.extend(sorted(base.rglob("*.py")))
    return out


def review(path: Path) -> list[Finding]:
    if not path.exists():
        return [Finding("Error", "config", path.as_posix(),
                        "File not found", "Provide a valid path")]
    if _is_renderer(path):
        return check_renderer(path)
    if path.suffix == ".md":
        return check_markdown(path)
    return []


def render_table(findings: list[Finding]) -> str:
    if not findings:
        return "_No findings._"
    rows = [
        "| Severity | Category | Asset / location | Finding | Required fix |",
        "|----------|----------|------------------|---------|--------------|",
    ]
    order = {"Error": 0, "Warning": 1, "Info": 2}
    for f in sorted(findings, key=lambda x: (order.get(x.severity, 9), x.location)):
        rows.append(
            f"| {f.severity} | {f.category} | {f.location} | {f.finding} | {f.fix} |"
        )
    return "\n".join(rows)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Tier 0 deterministic preflight for content artifacts.")
    parser.add_argument("paths", nargs="*", type=Path,
                        help="Files or directories to check (default: auto-discover).")
    parser.add_argument("--strict", action="store_true",
                        help="Treat Warnings as gate-blocking (default: only Errors block).")
    parser.add_argument("-o", "--output", type=Path,
                        help="Write the findings report to this file as well as stdout.")
    return parser


def main() -> int:
    args = create_parser().parse_args()

    targets = collect_targets(args.paths)
    if not targets:
        print("No content artifacts found to check.", file=sys.stderr)
        return EXIT_ERROR

    all_findings: list[Finding] = []
    for path in targets:
        all_findings.extend(review(path))

    errors = sum(1 for f in all_findings if f.severity == "Error")
    warnings = sum(1 for f in all_findings if f.severity == "Warning")
    infos = sum(1 for f in all_findings if f.severity == "Info")

    failed = errors > 0 or (args.strict and warnings > 0)
    verdict = "FAIL" if failed else "PASS"

    report_lines = [
        "## Tier 0 Preflight",
        "",
        f"Checked {len(targets)} artifact(s) - "
        f"Error: {errors}  Warning: {warnings}  Info: {infos}",
        "",
        render_table(all_findings),
        "",
        f"GATE: {verdict}",
    ]
    report = "\n".join(report_lines)
    print(report)

    if args.output:
        args.output.write_text(report + "\n", encoding="utf-8")

    return EXIT_FAIL if failed else EXIT_PASS


if __name__ == "__main__":
    sys.exit(main())
