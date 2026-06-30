# Idea Queue — GitHub CLI for Copilot Cost Optimization

> **Candidate source material** for this topic workspace.
> Run `@feed-curator` in this workspace to synthesize and rank candidates into content ideas.

Last seeded: 2026-06-30 (manually, autonomous pipeline run).

---

## Candidate source material

### From web research

- [GitHub Copilot seat assignment docs](https://docs.github.com/en/copilot/reference/copilot-billing/seat-assignment) — official seat management, assignment/revocation
- [GitHub Copilot metrics API](https://docs.github.com/en/rest/copilot/copilot-metrics) — org-level usage metrics, acceptance rates, active users
- [Administering Copilot CLI for enterprise](https://docs.github.com/en/copilot/how-tos/copilot-cli/administer-copilot-cli-for-your-enterprise) — policy controls
- [AutoKitteh seat management automation](https://autokitteh.com/technical-blog/practical-automation-managing-your-teams-github-copilot-seats/) — real automation workflow, saves 15-25%
- [Visualize ROI of Copilot usage](https://devblogs.microsoft.com/all-things-azure/visualize-roi-of-your-github-copilot-usage-how-it-works/) — ROI measurement, acceptance rates, code churn reduction
- [50% cost savings case study](https://completeaitraining.com/news/how-cli-achieved-50-cost-savings-and-faster-product/) — before/after metrics

---

## Queued Ideas

### IDEA-001 — Prioritized (Score: high)

**Title:** Chronicle of GitHub CLI: 5 Scenarios That Cut Copilot Costs by Up to 50%

**One-liner:** A scenario-by-scenario walkthrough of `gh` commands that give engineering leaders
visibility, control, and accountability over GitHub Copilot spend — without killing developer productivity.

**Thesis:** Most organizations are over-provisioning GitHub Copilot by 15-30% because they manage
seats manually. A few targeted `gh` CLI automation patterns — covering discovery, provisioning,
monitoring, and deprovisioning — can eliminate this waste while improving adoption quality.

**Scenarios to cover:**
1. **Inactive seat discovery** — `gh api` to find seats with 0 acceptance events in 30 days → auto-deprovision
2. **Usage-gated provisioning** — `gh copilot` + `gh api` to provision seats only after onboarding completion
3. **Repository-scoped policy enforcement** — CLI-driven exclusion of sensitive/OSS repos from Copilot
4. **Usage metrics pipeline** — `gh api copilot/metrics` to build a cost-per-team dashboard
5. **Auto-reclaim on offboarding** — `gh api` in CI/CD offboarding workflow to revoke seats immediately

**Audience:** Platform engineers, engineering managers, FinOps practitioners managing GitHub Enterprise
**Format:** Single post, scenario-driven, CLI commands as concrete proof points
**Status:** `queued`
