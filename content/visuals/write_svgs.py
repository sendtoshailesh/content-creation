"""Generate upgraded SVG visuals for the blog."""
from pathlib import Path

DIR = Path(__file__).parent

# ── 1. Trade-off 2×2 ──────────────────────────────────────────────
tradeoff = """\
<svg width="960" height="840" viewBox="0 0 960 840" xmlns="http://www.w3.org/2000/svg">
  <defs><style>text{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif}</style></defs>
  <rect width="960" height="840" fill="#ffffff"/>
  <text x="480" y="50" font-size="22" fill="#1e293b" font-weight="bold" text-anchor="middle">Quality vs. Cost Trade-Off Matrix</text>
  <!-- quadrant fills -->
  <rect x="100" y="80" width="380" height="340" fill="#ccfbf1" opacity="0.3" rx="8"/>
  <rect x="480" y="80" width="380" height="340" fill="#dbeafe" opacity="0.3" rx="8"/>
  <rect x="100" y="420" width="380" height="340" fill="#f8fafc" opacity="0.5" rx="8"/>
  <rect x="480" y="420" width="380" height="340" fill="#fef2f2" opacity="0.3" rx="8"/>
  <!-- axes -->
  <line x1="100" y1="420" x2="860" y2="420" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="6,4"/>
  <line x1="480" y1="80" x2="480" y2="760" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="6,4"/>
  <!-- quadrant labels -->
  <text x="290" y="130" font-size="13" fill="#0d9488" text-anchor="middle" font-style="italic" opacity="0.8">High Quality / Low Cost</text>
  <text x="670" y="130" font-size="13" fill="#1f6feb" text-anchor="middle" font-style="italic" opacity="0.8">High Quality / High Cost</text>
  <text x="290" y="720" font-size="13" fill="#64748b" text-anchor="middle" font-style="italic" opacity="0.8">Lower Quality / Low Cost</text>
  <text x="670" y="720" font-size="13" fill="#dc2626" text-anchor="middle" font-style="italic" opacity="0.8">Danger Zone</text>
  <!-- Frontier dot -->
  <circle cx="680" cy="200" r="28" fill="#1f6feb" opacity="0.08"/>
  <circle cx="680" cy="200" r="12" fill="#1f6feb" stroke="#ffffff" stroke-width="3"/>
  <text x="680" y="248" font-size="14" fill="#1f6feb" font-weight="600" text-anchor="middle">Frontier</text>
  <text x="680" y="268" font-size="11" fill="#64748b" text-anchor="middle">(Opus, o3, Ultra)</text>
  <!-- Mid-tier dot -->
  <circle cx="460" cy="320" r="24" fill="#0d9488" opacity="0.08"/>
  <circle cx="460" cy="320" r="10" fill="#0d9488" stroke="#ffffff" stroke-width="3"/>
  <text x="460" y="360" font-size="14" fill="#0d9488" font-weight="600" text-anchor="middle">Mid-tier</text>
  <text x="460" y="380" font-size="11" fill="#64748b" text-anchor="middle">(Sonnet, GPT-4o)</text>
  <!-- Lightweight dot -->
  <circle cx="260" cy="490" r="22" fill="#475569" opacity="0.08"/>
  <circle cx="260" cy="490" r="9" fill="#475569" stroke="#ffffff" stroke-width="3"/>
  <text x="260" y="530" font-size="14" fill="#475569" font-weight="600" text-anchor="middle">Lightweight</text>
  <text x="260" y="550" font-size="11" fill="#64748b" text-anchor="middle">(Haiku, Flash)</text>
  <!-- axis labels -->
  <text x="480" y="795" font-size="15" fill="#475569" text-anchor="middle">Cost &#x2192;</text>
  <text x="60" y="420" font-size="15" fill="#475569" text-anchor="middle" transform="rotate(-90 60,420)">Quality &#x2192;</text>
</svg>"""

# ── 2. Decision Funnel ────────────────────────────────────────────
funnel = """\
<svg width="960" height="780" viewBox="0 0 960 780" xmlns="http://www.w3.org/2000/svg">
  <defs><style>text{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif}</style></defs>
  <rect width="960" height="780" fill="#ffffff"/>
  <text x="480" y="48" font-size="22" fill="#1e293b" font-weight="bold" text-anchor="middle">Model Selection Decision Funnel</text>
  <!-- funnel stages (trapezoids narrowing down) -->
  <polygon points="140,100 820,100 760,210 200,210" fill="#dbeafe" stroke="#1f6feb" stroke-width="1.5"/>
  <text x="480" y="145" font-size="16" fill="#1f6feb" font-weight="600" text-anchor="middle">1. Define Task Requirements</text>
  <text x="480" y="170" font-size="12" fill="#64748b" text-anchor="middle">Latency, accuracy, throughput, compliance constraints</text>
  <polygon points="200,220 760,220 710,330 250,330" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5"/>
  <text x="480" y="265" font-size="16" fill="#0d9488" font-weight="600" text-anchor="middle">2. Shortlist Candidate Models</text>
  <text x="480" y="290" font-size="12" fill="#64748b" text-anchor="middle">Benchmark scores, pricing, context window, modality</text>
  <polygon points="250,340 710,340 660,450 300,450" fill="#f1f5f9" stroke="#475569" stroke-width="1.5"/>
  <text x="480" y="385" font-size="16" fill="#475569" font-weight="600" text-anchor="middle">3. Prototype &amp; Evaluate</text>
  <text x="480" y="410" font-size="12" fill="#64748b" text-anchor="middle">A/B test with real prompts, measure cost per query</text>
  <polygon points="300,460 660,460 620,570 340,570" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
  <text x="480" y="505" font-size="16" fill="#dc2626" font-weight="600" text-anchor="middle">4. Validate in Production</text>
  <text x="480" y="530" font-size="12" fill="#64748b" text-anchor="middle">Shadow deploy, monitor latency/cost/quality drift</text>
  <polygon points="340,580 620,580 580,690 380,690" fill="#1f6feb" stroke="#1f6feb" stroke-width="1.5" opacity="0.15"/>
  <rect x="380" y="580" width="200" height="110" fill="#1f6feb" rx="8"/>
  <text x="480" y="630" font-size="16" fill="#ffffff" font-weight="700" text-anchor="middle">5. Ship &amp; Monitor</text>
  <text x="480" y="655" font-size="12" fill="#dbeafe" text-anchor="middle">Continuous eval, router fallback</text>
  <!-- side annotations -->
  <text x="115" y="160" font-size="11" fill="#1f6feb" text-anchor="end" font-style="italic">All models</text>
  <text x="845" y="160" font-size="11" fill="#1f6feb" font-style="italic">~100+</text>
  <text x="170" y="280" font-size="11" fill="#0d9488" text-anchor="end" font-style="italic">Filtered</text>
  <text x="790" y="280" font-size="11" fill="#0d9488" font-style="italic">5-8</text>
  <text x="220" y="400" font-size="11" fill="#475569" text-anchor="end" font-style="italic">Tested</text>
  <text x="740" y="400" font-size="11" fill="#475569" font-style="italic">2-3</text>
  <text x="270" y="520" font-size="11" fill="#dc2626" text-anchor="end" font-style="italic">Validated</text>
  <text x="690" y="520" font-size="11" fill="#dc2626" font-style="italic">1-2</text>
  <!-- arrow down -->
  <polygon points="470,710 490,710 480,740" fill="#1f6feb"/>
  <text x="480" y="765" font-size="14" fill="#1e293b" font-weight="600" text-anchor="middle">Production Model</text>
</svg>"""

# ── 3. Checklist Card ─────────────────────────────────────────────
checklist = """\
<svg width="640" height="720" viewBox="0 0 640 720" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>text{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif}</style>
    <filter id="shadow" x="-4%" y="-2%" width="108%" height="108%">
      <feDropShadow dx="0" dy="2" stdDeviation="6" flood-color="#000" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="640" height="720" fill="#f8fafc"/>
  <!-- card -->
  <rect x="40" y="30" width="560" height="660" rx="12" fill="#ffffff" filter="url(#shadow)" stroke="#e2e8f0" stroke-width="1"/>
  <!-- header bar -->
  <rect x="40" y="30" width="560" height="60" rx="12" fill="#1f6feb"/>
  <rect x="40" y="70" width="560" height="20" fill="#1f6feb"/>
  <text x="320" y="68" font-size="18" fill="#ffffff" font-weight="700" text-anchor="middle">Pre-Launch Model Checklist</text>
  <!-- items -->
  <rect x="70" y="112" width="22" height="22" rx="4" fill="#0d9488"/>
  <text x="78" y="129" font-size="14" fill="#ffffff" font-weight="bold">&#x2713;</text>
  <text x="106" y="129" font-size="15" fill="#1e293b">Task requirements documented with acceptance criteria</text>
  <rect x="70" y="156" width="22" height="22" rx="4" fill="#0d9488"/>
  <text x="78" y="173" font-size="14" fill="#ffffff" font-weight="bold">&#x2713;</text>
  <text x="106" y="173" font-size="15" fill="#1e293b">Candidate models benchmarked on real prompts</text>
  <rect x="70" y="200" width="22" height="22" rx="4" fill="#0d9488"/>
  <text x="78" y="217" font-size="14" fill="#ffffff" font-weight="bold">&#x2713;</text>
  <text x="106" y="217" font-size="15" fill="#1e293b">Cost model built: tokens &#xD7; price &#xD7; volume</text>
  <rect x="70" y="244" width="22" height="22" rx="4" fill="#0d9488"/>
  <text x="78" y="261" font-size="14" fill="#ffffff" font-weight="bold">&#x2713;</text>
  <text x="106" y="261" font-size="15" fill="#1e293b">Latency budget defined per endpoint</text>
  <rect x="70" y="296" width="22" height="22" rx="4" stroke="#cbd5e1" stroke-width="1.5" fill="#ffffff"/>
  <text x="106" y="313" font-size="15" fill="#1e293b">Eval suite automated with &#x2265; 200 test cases</text>
  <rect x="70" y="340" width="22" height="22" rx="4" stroke="#cbd5e1" stroke-width="1.5" fill="#ffffff"/>
  <text x="106" y="357" font-size="15" fill="#1e293b">Model router / fallback logic implemented</text>
  <rect x="70" y="384" width="22" height="22" rx="4" stroke="#cbd5e1" stroke-width="1.5" fill="#ffffff"/>
  <text x="106" y="401" font-size="15" fill="#1e293b">Shadow deployment validated for 48+ hours</text>
  <rect x="70" y="428" width="22" height="22" rx="4" stroke="#cbd5e1" stroke-width="1.5" fill="#ffffff"/>
  <text x="106" y="445" font-size="15" fill="#1e293b">Monitoring dashboards live (cost, latency, quality)</text>
  <!-- divider -->
  <line x1="70" y1="478" x2="570" y2="478" stroke="#e2e8f0" stroke-width="1"/>
  <!-- footer -->
  <text x="320" y="510" font-size="13" fill="#64748b" text-anchor="middle">Complete all items before promoting to production.</text>
  <text x="320" y="535" font-size="13" fill="#64748b" text-anchor="middle">Review weekly with engineering and product leads.</text>
  <!-- progress bar -->
  <rect x="70" y="570" width="500" height="12" rx="6" fill="#e2e8f0"/>
  <rect x="70" y="570" width="250" height="12" rx="6" fill="#0d9488"/>
  <text x="70" y="605" font-size="13" fill="#0d9488" font-weight="600">4 / 8 complete</text>
  <text x="570" y="605" font-size="13" fill="#64748b" text-anchor="end">50%</text>
</svg>"""

for name, content in [("tradeoff-2x2.svg", tradeoff),
                       ("decision-funnel.svg", funnel),
                       ("checklist-card.svg", checklist)]:
    (DIR / name).write_text(content)
    print(f"  ✓ {name}")

print("Done – all 3 SVGs written.")
