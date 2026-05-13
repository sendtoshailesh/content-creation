# Visual  Part 1 Practitioner Pack (Round 2)Review 
**Date**: 2026-05-13 | ** FAIL (14 critical, 17 important, 5 minor)Result**: 

## Summary Table

| Asset | Result |
|-------|--------|
| slide-01-hook.png | FAIL (1 important) |
| slide-02-promise.png | FAIL (2 critical) |
| slide-03-problem.png | FAIL (1 critical, 1 minor) |
| slide-04-framework.png | PASS (1 minor) |
| slide-05-step1.png | FAIL (2 critical) |
| slide-06-step2.png | FAIL (1 important) |
| slide-07-step3.png | FAIL (1 critical) |
| slide-08-pattern-interrupt.png | FAIL (2 important) |
| slide-09-recap.png | PASS (1 minor) |
| slide-10-cta.png | FAIL (3 important) |
| x-card-01.png | FAIL (1 important) |
| x-card-02.png | FAIL (3 issues) |
| x-card-03.png | PASS (1 minor) |
| x-card-04.png | FAIL (1 important) |
| medium-hero.png | FAIL (2 important) |
| medium-inline-01.png | FAIL (2 critical) |
| medium-inline-02.png | FAIL (2 critical) |
| substack-hero.png | FAIL (1 important) |
| linkedin-article-exhibit-01.png | FAIL (2 issues) |
| linkedin-article-exhibit-02.png | FAIL (4 issues) |

## Systemic Root Causes

| # | Issue | Fix |
|---|-------|-----|
| S1 | Off-spec dark bg `#1e293b` on 5 hero/hook assets | Approved or switch to `#ffffff` |
| S2 | Callout/box text overflows canvas edges | Clamp box coordinates to canvas bounds |
| S3 | Long title strings not wrapped at right edge | Use `textwrap.fill()` or explicit `\n` breaks |
| S4 | LinkedIn banner title too large for 1200px | Reduce fontsize ~30% or split to 2 lines |
| S5 | "TDS" attribution still in x-card-02, linkedin-02 | Remove all TDS/Towards Data Science strings |
bash init-workspace.sh `v` |
| S7 | Missing `$` in monetary values | Fix f-string formatting |
| S8 | Excessive whitespace in x-card-02, x-card-04, slide-10 | Centre content vertically |
