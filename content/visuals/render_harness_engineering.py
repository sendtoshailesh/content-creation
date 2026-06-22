from __future__ import annotations

from pathlib import Path

from scripts.visuals.html.design import esc, page
from scripts.visuals.html.inspect import inspect_files
from scripts.visuals.html.render import render_many

OUT_DIR = Path(__file__).resolve().parent / "harness-engineering"
WIDTH = 1600
HEIGHT = 760


def section_header(kicker: str, title: str, subtitle: str = "") -> str:
    subtitle_html = (
        f'<p data-role="subtitle">{esc(subtitle)}</p>' if subtitle else ""
    )
    return f"""
    <div style="display:flex; flex-direction:column; gap:10px;">
      <div class="eyebrow" data-role="caption">{esc(kicker)}</div>
      <h1 data-role="title">{esc(title)}</h1>
      {subtitle_html}
    </div>
    """


def source(text: str) -> str:
    return f'<div class="source" data-role="caption">{esc(text)}</div>'


def card(title: str, body: str, klass: str = "") -> str:
    return f"""
    <div class="card {klass}">
      <div data-role="label">{esc(title)}</div>
      <div data-role="body">{esc(body)}</div>
    </div>
    """


def v01_harness_quote() -> str:
    body = f"""
    {section_header('core reframe', 'The model was never the whole agent')}
    <div class="card accent" style="gap:24px; justify-content:center; flex:1;">
      <div class="quote" data-role="title">So far, the developer was the harness.</div>
      <div data-role="subtitle">Harness engineering moves that hidden scaffolding into versioned, reviewable workflow artifacts.</div>
    </div>
    {source('Source: InfoQ podcast with Birgitta Boeckeler, Jun 2026')}
    """
    return page(WIDTH, HEIGHT, body, theme="default")


def v02_maturity_arc() -> str:
    stages = [
        ("1", "Autocomplete", "Next line or function"),
        ("2", "Vibe coding", "Larger chunks, weak ownership"),
        ("3", "Context engineering", "Better input context"),
        ("4", "Harness engineering", "Context plus feedback loops"),
    ]
    stage_html = "".join(
        f"""
        <div class="card" style="min-height:300px; justify-content:center;">
          <div class="badge">{esc(num)}</div>
          <div data-role="label">{esc(title)}</div>
          <div data-role="body">{esc(desc)}</div>
        </div>
        """
        for num, title, desc in stages
    )
    body = f"""
    {section_header('maturity arc', 'From autocomplete to harness engineering', 'Each step makes more of the workflow explicit.')}
    <div class="grid" style="grid-template-columns: repeat(4, 1fr); gap:18px; flex:1; align-items:stretch;">
      {stage_html}
    </div>
    {source('Sources: InfoQ podcast, QCon London 2025 context, Jun 2025 context-engineering wave')}
    """
    return page(WIDTH, HEIGHT, body, theme="ocean")


def v03_harness_anatomy() -> str:
    body = f"""
    {section_header('anatomy', 'Agent = model + harness', 'Feed-forward improves the first move. Feedback improves correction.')}
    <div style="display:grid; grid-template-columns: 1fr 1.1fr 1fr; gap:24px; flex:1; align-items:center;">
      <div style="display:flex; flex-direction:column; justify-content:center;">
        {card('Feed-forward', 'Conventions, architecture context, specs, examples, and design systems.', 'accent')}
      </div>
      <div class="card" style="align-items:center; justify-content:center; min-height:380px; background:var(--blue-bg); border-color:var(--accent);">
        <div data-role="value" style="color:var(--accent);">Model</div>
        <div data-role="subtitle" style="text-align:center;">The generator is only the core.</div>
      </div>
      <div style="display:flex; flex-direction:column; justify-content:center;">
        {card('Feedback', 'Tests, compiler errors, static analysis, coverage, and adversarial review.', 'ok')}
      </div>
    </div>
    <div class="gap-callout">
      <div class="gap-num" data-role="value">Loop</div>
      <div data-role="body">The harness catches cheap failures before human review.</div>
    </div>
    {source('Source: InfoQ podcast, feed-forward and feedback framework')}
    """
    return page(WIDTH, HEIGHT, body, theme="default")


def v04_building_blocks() -> str:
    items = [
        ("Custom agents", ".agent.md workflows", "Reviewable"),
        ("Skills", "Lazy-loaded context", "Angular v20"),
        ("Routing", "HyDRA economics", "72.5% savings"),
        ("Orchestration", "Selective delegation", "23% fewer failures"),
    ]
    blocks = "".join(
        f"""
        <div class="metric accent">
          <div data-role="label">{esc(name)}</div>
          <div class="m-num" data-role="value">{esc(metric)}</div>
          <div data-role="body">{esc(desc)}</div>
        </div>
        """
        for name, desc, metric in items
    )
    body = f"""
    {section_header('building blocks', 'Four beams around the model', 'A harness is a system, not a longer prompt.')}
    <div style="display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:22px; flex:1;">
      {blocks}
    </div>
    {source('Sources: GitHub Blog Jun 9, Jun 12, Jun 17 2026; InfoQ Angular skills Jun 2026')}
    """
    return page(WIDTH, HEIGHT, body, theme="forest")


def v05_context_switch_cost() -> str:
    body = f"""
    {section_header('cost of ad-hoc work', 'Prompting does not scale when state stays in your head')}
    <div style="display:grid; grid-template-columns:0.9fr 1.1fr; gap:30px; flex:1; align-items:center;">
      <div class="card warn" style="justify-content:center; align-items:center; min-height:420px;">
        <div data-role="value" style="color:var(--warn);">40%</div>
        <div data-role="subtitle" style="text-align:center;">efficiency loss from context switching</div>
      </div>
      <div class="flow">
        {card('Private prompt', 'Context is reconstructed every session.')}
        <div class="connector"></div>
        {card('Versioned harness', 'Context, tools, checks, and gates become reusable.')}
      </div>
    </div>
    {source('Source: Towards Data Science citing APA multitasking research')}
    """
    return page(WIDTH, HEIGHT, body, theme="sunset")


def v06_pipeline_case_study() -> str:
    body = f"""
    {section_header('case study', 'This pipeline is a harness', 'The model can change. The workflow contract remains inspectable.')}
    <div style="display:grid; grid-template-columns:0.9fr 1.2fr; gap:28px; flex:1; align-items:stretch;">
      <div class="card accent" style="justify-content:center;">
        <div data-role="value" style="color:var(--accent);">pipeline-config.md</div>
        <div data-role="body">Topic, platforms, status, gates, and current step.</div>
      </div>
      <div class="grid two" style="gap:18px;">
        {card('Agents', 'Strategy, writing, visuals, review, social, publishing')}
        {card('Skills', 'Scope, dimensions, visual planning, rendering')}
        {card('Scripts', 'Rendering, publishing, validation helpers')}
        {card('Gates', 'Scope, blog approval, publishing approval')}
      </div>
    </div>
    {source('Source: this repository, current run, 2026-06-20')}
    """
    return page(WIDTH, HEIGHT, body, theme="default")


def v07_risk_limits() -> str:
    body = f"""
    {section_header('honest limits', 'Harnesses guide models. They do not prove correctness.')}
    <div style="display:grid; grid-template-columns:1.15fr 0.85fr; gap:28px; flex:1; align-items:center;">
      <div class="card" style="gap:20px; justify-content:center; min-height:420px;">
        <div data-role="title">Risk = probability x impact x detectability</div>
        <div class="bar-row"><div class="bar-label" data-role="label">Low impact</div><div class="bar-track"><div class="bar-fill ok" style="width:32%"></div></div><div class="bar-value" data-role="label">more automation</div></div>
        <div class="bar-row"><div class="bar-label" data-role="label">Hard to detect</div><div class="bar-track"><div class="bar-fill warn" style="width:86%"></div></div><div class="bar-value" data-role="label">more review</div></div>
      </div>
      <div class="metric warn">
        <div class="m-num" data-role="value">Gap</div>
        <div data-role="body">Behavior harnesses are still weak when agents write their own tests.</div>
      </div>
    </div>
    {source('Source: InfoQ podcast and Angular skills coverage critique')}
    """
    return page(WIDTH, HEIGHT, body, theme="midnight")


def v08_playbook_checklist() -> str:
    steps = [
        ("1", "Choose one repeated AI task"),
        ("2", "Move reusable context into an agent or skill"),
        ("3", "Add one automated feedback signal"),
        ("4", "Review the harness like production code"),
        ("5", "When it fails, improve the harness first"),
    ]
    flow = "".join(
        f"""
        <div class="card" style="padding:20px 24px;">
          <div style="display:flex; align-items:center; gap:16px;">
            <div class="badge">{esc(num)}</div>
            <div data-role="label">{esc(text)}</div>
          </div>
        </div>
        {('<div class="connector" style="height:18px;"></div>' if num != '5' else '')}
        """
        for num, text in steps
    )
    body = f"""
    {section_header('playbook', 'Start with one repeatable harness', 'The first win is narrow, reviewable, and easy to validate.')}
    <div class="flow" style="flex:1;">
      {flow}
    </div>
    {source('Source: InfoQ podcast and practitioner playbook from this run')}
    """
    return page(WIDTH, HEIGHT, body, theme="ocean", pad=42)


ASSETS = [
    ("v01-harness-quote", v01_harness_quote),
    ("v02-maturity-arc", v02_maturity_arc),
    ("v03-harness-anatomy", v03_harness_anatomy),
    ("v04-building-blocks", v04_building_blocks),
    ("v05-context-switch-cost", v05_context_switch_cost),
    ("v06-pipeline-case-study", v06_pipeline_case_study),
    ("v07-risk-limits", v07_risk_limits),
    ("v08-playbook-checklist", v08_playbook_checklist),
]


def stamp_dpi(path: Path) -> None:
    try:
        from PIL import Image
    except ImportError:
        return
    with Image.open(path) as image:
        image.save(path, dpi=(320, 320))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    html_paths: list[Path] = []
    render_items: list[tuple[str, Path]] = []

    for name, factory in ASSETS:
        doc = factory()
        html_path = OUT_DIR / f"{name}.html"
        png_path = OUT_DIR / f"{name}.png"
        html_path.write_text(doc, encoding="utf-8")
        html_paths.append(html_path)
        render_items.append((doc, png_path))

    if not inspect_files(html_paths):
        raise SystemExit(1)

    rendered = render_many(render_items, scale=2)
    for path in rendered:
        stamp_dpi(path)
        print(path.relative_to(Path.cwd()))


if __name__ == "__main__":
    main()