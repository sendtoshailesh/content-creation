"""Publish-time Playwright QA gate for rendered docs/blog pages.

Extends the original raw-HTML diagram check into a final publish gate:

- rejects raw diagram source that would render as literal text
- verifies key page sections render in Chromium
- checks images, stylesheets, scripts, and local links resolve
- runs responsive overflow checks at desktop / tablet / mobile widths
- performs lightweight accessibility checks (alt text, heading order, focus)
- optionally captures or compares full-page screenshots for regression gating

Usage:
    python3 -m scripts.visuals.html.check_published
    python3 -m scripts.visuals.html.check_published docs/index.html docs/blog/foo.html
    python3 -m scripts.visuals.html.check_published --snapshot-dir /tmp/site-snaps --update-snapshots
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

from PIL import Image, ImageChops, ImageStat
from playwright.sync_api import sync_playwright

# Languages that are *diagram* sources, not code samples: if these appear as a
# raw <code class="language-XXX"> block they were meant to be rendered to an
# image and will otherwise show as literal text.
_DIAGRAM_LANGS = ("mermaid", "graphviz", "dot", "plantuml")
_VIEWPORTS: tuple[tuple[str, int, int], ...] = (
    ("desktop", 1440, 1600),
    ("tablet", 1024, 1400),
    ("mobile", 390, 1200),
)
_DIAGRAM_RUNTIME_RE = re.compile(r"(mermaid|graphviz|plantuml|viz\.js)", re.I)
_HASH_RE = re.compile(r'href="(#.*?)"')
_PAGE_JS = r"""
() => {
  const text = (el) => (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 80);
  const focusableSelector = [
    'a[href]',
    'button',
    'input',
    'select',
    'textarea',
    '[tabindex]:not([tabindex="-1"])'
  ].join(',');
  const focusables = [...document.querySelectorAll(focusableSelector)]
    .filter((el) => {
      const rect = el.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0;
    })
    .slice(0, 12)
    .map((el) => {
      el.focus();
      const rect = el.getBoundingClientRect();
      const style = getComputedStyle(el);
      const outlineWidth = parseFloat(style.outlineWidth || '0');
      const borderWidth = parseFloat(style.borderWidth || '0');
      const hasFocusIndicator =
        ((style.outlineStyle && style.outlineStyle !== 'none') && outlineWidth > 0) ||
        style.boxShadow !== 'none' ||
        ((style.borderStyle && style.borderStyle !== 'none') && borderWidth > 0);
      return {
        tag: el.tagName.toLowerCase(),
        text: text(el),
        hasFocusIndicator,
        outlineStyle: style.outlineStyle || '',
        outlineWidth,
        boxShadow: style.boxShadow || '',
        x: rect.x,
        y: rect.y,
        w: rect.width,
        h: rect.height
      };
    });

  return {
    title: document.title,
    bodyTextLength: (document.body.innerText || '').trim().length,
    mainCount: document.querySelectorAll('main').length,
    articleCount: document.querySelectorAll('article').length,
    heroCount: document.querySelectorAll('.hero').length,
    blogCardCount: document.querySelectorAll('.blog-card').length,
    postContentCount: document.querySelectorAll('.post-content').length,
    h1Count: document.querySelectorAll('h1').length,
    headings: [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map((el) => Number(el.tagName.slice(1))),
    fragmentTargets: [...document.querySelectorAll('[id],[name]')]
      .map((el) => el.id || el.getAttribute('name') || '')
      .filter(Boolean),
    images: [...document.images].map((img) => ({
      src: img.getAttribute('src') || '',
      alt: img.getAttribute('alt') || '',
      complete: img.complete,
      naturalWidth: img.naturalWidth,
      naturalHeight: img.naturalHeight
    })),
    links: [...document.querySelectorAll('a[href]')].map((a) => ({
      href: a.getAttribute('href') || '',
      text: text(a)
    })),
    assets: [...document.querySelectorAll('link[href], script[src]')].map((el) => ({
      tag: el.tagName.toLowerCase(),
      rel: el.getAttribute('rel') || '',
      path: el.getAttribute(el.tagName.toLowerCase() === 'link' ? 'href' : 'src') || ''
    })),
    runtimeScripts: [...document.querySelectorAll('script')]
      .map((s) => [s.getAttribute('src') || '', s.textContent || ''].join(' '))
      .filter((txt) => txt),
    xOverflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
    yOverflow: document.documentElement.scrollHeight - document.documentElement.clientHeight,
    focusables
  };
}
"""


@dataclass(frozen=True)
class Finding:
    severity: str  # Error | Warning
    message: str


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def discover_pages() -> list[Path]:
    docs = _repo_root() / "docs"
    return sorted(p for p in docs.rglob("*.html") if p.is_file())


def _findings_for_raw_html(path: Path) -> list[Finding]:
    html = path.read_text(encoding="utf-8", errors="ignore")
    findings: list[Finding] = []

    for lang in _DIAGRAM_LANGS:
        if re.search(rf'class="[^"]*language-{lang}', html):
            has_runtime = re.search(rf'<script[^>]*{lang}', html, re.I)
            if not has_runtime:
                findings.append(Finding(
                    "Error",
                    f'raw <code class="language-{lang}"> block with no {lang} runtime <script>; pre-render it to PNG and embed as <img>',
                ))

    for lang in _DIAGRAM_LANGS:
        if f"```{lang}" in html:
            findings.append(Finding(
                "Error",
                f"literal ```{lang} fence found in published HTML; markdown conversion failed",
            ))

    for href in _HASH_RE.findall(html):
        if href == "#":
            findings.append(Finding("Warning", 'anchor href="#" provides no destination'))

    return findings


def _resolve_local_ref(page_path: Path, ref: str) -> Path | None:
    parsed = urlparse(ref)
    if parsed.scheme or ref.startswith("//"):
        return None
    if ref.startswith("#"):
        return None
    clean = ref.split("#", 1)[0].split("?", 1)[0]
    if not clean:
        return None
    return (page_path.parent / clean).resolve()


def _check_heading_order(levels: list[int]) -> list[Finding]:
    findings: list[Finding] = []
    if not levels:
        return [Finding("Error", "page has no headings")]
    if levels[0] != 1:
        findings.append(Finding("Error", f"heading sequence starts at h{levels[0]} instead of h1"))
    for prev, curr in zip(levels, levels[1:]):
        if curr > prev + 1:
            findings.append(Finding("Warning", f"heading level jumps from h{prev} to h{curr}"))
            break
    return findings


def _page_kind_findings(path: Path, data: dict) -> list[Finding]:
    findings: list[Finding] = []
    if data["mainCount"] == 0:
        findings.append(Finding("Error", "page is missing a <main> region"))
    if data["h1Count"] != 1:
        findings.append(Finding("Error", f'page has {data["h1Count"]} h1 headings; expected exactly 1'))
    if data["bodyTextLength"] == 0:
        findings.append(Finding("Error", "page rendered with no body text"))

    is_index = path.name == "index.html" and path.parent.name == "docs"
    if is_index:
        if data["heroCount"] == 0:
            findings.append(Finding("Error", "home page is missing the .hero section"))
        if data["blogCardCount"] == 0:
            findings.append(Finding("Error", "home page rendered no .blog-card entries"))
    else:
        if data["articleCount"] == 0:
            findings.append(Finding("Error", "post page is missing an <article>"))
        if data["postContentCount"] == 0:
            findings.append(Finding("Error", "post page is missing .post-content"))
    return findings


def _resource_findings(path: Path, data: dict) -> list[Finding]:
    findings: list[Finding] = []
    targets = set(data.get("fragmentTargets", []))

    for img in data["images"]:
        if not img["src"]:
            findings.append(Finding("Error", "image without src attribute"))
            continue
        if not img["complete"] or img["naturalWidth"] <= 0 or img["naturalHeight"] <= 0:
            findings.append(Finding("Error", f'broken image asset: {img["src"]}'))
        if not img["alt"].strip():
            findings.append(Finding("Error", f'image missing alt text: {img["src"]}'))
        resolved = _resolve_local_ref(path, img["src"])
        if resolved is not None and not resolved.exists():
            findings.append(Finding("Error", f'image path not found on disk: {img["src"]}'))

    for asset in data["assets"]:
        ref = asset["path"]
        if not ref:
            continue
        resolved = _resolve_local_ref(path, ref)
        if resolved is not None and not resolved.exists():
            findings.append(Finding(
                "Error",
                f'{asset["tag"]} asset not found on disk: {ref}',
            ))

    for link in data["links"]:
        href = link["href"].strip()
        if not href:
            findings.append(Finding("Warning", f'empty href on link "{link["text"]}"'))
            continue
        parsed = urlparse(href)
        if parsed.scheme in {"http", "https", "mailto", "tel"}:
            continue
        if href.startswith("#"):
            target = href[1:]
            if target and target not in targets:
                findings.append(Finding("Error", f'fragment target not found in page: {href}'))
            continue
        resolved = _resolve_local_ref(path, href)
        if resolved is None:
            continue
        if not resolved.exists():
            findings.append(Finding("Error", f'local link target not found: {href}'))

    if any(_DIAGRAM_RUNTIME_RE.search(s) for s in data["runtimeScripts"]):
        findings.append(Finding("Error", "published page loads a diagram runtime script; pre-render diagrams instead"))

    return findings


def _viewport_findings(viewport_name: str, data: dict) -> list[Finding]:
    findings: list[Finding] = []
    if data["xOverflow"] > 1:
        findings.append(Finding("Error", f"{viewport_name}: horizontal overflow detected (+{data['xOverflow']}px)"))
    focusables = data.get("focusables", [])
    if focusables and not any(f["hasFocusIndicator"] for f in focusables):
        findings.append(Finding("Warning", f"{viewport_name}: no visible keyboard focus indicator detected on sampled elements"))
    return findings


def _snapshot_name(path: Path, viewport_name: str) -> str:
    rel = path.relative_to(_repo_root() / "docs").as_posix()
    slug = rel.replace("/", "__").replace(".html", "")
    return f"{slug}.{viewport_name}.png"


def _compare_images(expected: Path, actual: Path, max_diff_mean: float) -> Finding | None:
    with Image.open(expected) as exp, Image.open(actual) as act:
        if exp.size != act.size:
            return Finding("Error", f"snapshot size changed {exp.size} -> {act.size}")
        diff = ImageChops.difference(exp.convert("RGBA"), act.convert("RGBA"))
        if diff.getbbox() is None:
            return None
        mean = sum(ImageStat.Stat(diff).mean) / len(ImageStat.Stat(diff).mean)
        if mean > max_diff_mean:
            return Finding("Error", f"snapshot drift mean={mean:.3f} exceeds threshold {max_diff_mean:.3f}")
    return None


def check_page(path: Path, snapshot_dir: Path | None, update_snapshots: bool, max_diff_mean: float) -> list[Finding]:
    findings = _findings_for_raw_html(path)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        try:
            for idx, (viewport_name, width, height) in enumerate(_VIEWPORTS):
                page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
                try:
                    page.goto(path.resolve().as_uri(), wait_until="load")
                    page.wait_for_load_state("networkidle")
                    page.evaluate("async () => { if (document.fonts) await document.fonts.ready; }")
                    data = page.evaluate(_PAGE_JS)

                    if idx == 0:
                        findings.extend(_check_heading_order(data["headings"]))
                        findings.extend(_page_kind_findings(path, data))
                        findings.extend(_resource_findings(path, data))
                    findings.extend(_viewport_findings(viewport_name, data))

                    if snapshot_dir is not None:
                        snapshot_dir.mkdir(parents=True, exist_ok=True)
                        baseline = snapshot_dir / _snapshot_name(path, viewport_name)
                        current = snapshot_dir / f".current-{_snapshot_name(path, viewport_name)}"
                        page.screenshot(path=str(current), full_page=True)
                        if update_snapshots:
                            current.replace(baseline)
                        else:
                            if not baseline.exists():
                                findings.append(Finding("Error", f"snapshot baseline missing: {baseline.name}"))
                            else:
                                diff_finding = _compare_images(baseline, current, max_diff_mean)
                                if diff_finding is not None:
                                    findings.append(Finding("Error", f"{viewport_name}: {diff_finding.message}"))
                            current.unlink(missing_ok=True)
                finally:
                    page.close()
        finally:
            browser.close()

    return findings


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Playwright publish QA gate for rendered docs/blog pages.")
    parser.add_argument("paths", nargs="*", help="Published HTML files to validate (default: all docs/**/*.html)")
    parser.add_argument("--snapshot-dir", type=Path, help="Directory containing baseline PNG snapshots")
    parser.add_argument("--update-snapshots", action="store_true", help="Write/update baseline snapshots instead of comparing")
    parser.add_argument("--max-diff-mean", type=float, default=0.0, help="Allowed mean pixel drift for snapshot compare")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    return parser


def main(argv: list[str]) -> int:
    args = create_parser().parse_args(argv)
    if args.update_snapshots and args.snapshot_dir is None:
        print("--update-snapshots requires --snapshot-dir", file=sys.stderr)
        return 2

    paths = [Path(p) for p in args.paths] if args.paths else discover_pages()
    if not paths:
        print("No published HTML pages found.", file=sys.stderr)
        return 2

    failed = False
    for path in paths:
        if not path.exists():
            print(f"[FAIL] {path}")
            print("   - Error: file not found")
            failed = True
            continue

        findings = check_page(
            path.resolve(),
            snapshot_dir=args.snapshot_dir.resolve() if args.snapshot_dir else None,
            update_snapshots=args.update_snapshots,
            max_diff_mean=args.max_diff_mean,
        )
        errors = [f for f in findings if f.severity == "Error"]
        warnings = [f for f in findings if f.severity == "Warning"]
        if errors or (args.strict and warnings):
            failed = True
            status = "FAIL"
        elif warnings:
            status = "WARN"
        else:
            status = "PASS"
        print(f"[{status}] {path}")
        for finding in findings:
            print(f"   - {finding.severity}: {finding.message}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
