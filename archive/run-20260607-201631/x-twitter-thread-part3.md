# X/Twitter Thread — Part 3: PRUs → AI Credits

## Standalone Summary Tweet

── START COPY ──

GitHub Copilot retires PRUs on June 1, 2026.

Token-metered AI Credits take over. A short Lightweight chat: ~$0.001. A deep Powerful agent session: ~$0.45.

A ~450x per-request spread — now in real dollars on your bill.

Part 3: how to route across Lightweight/Versatile/Powerful. 🧵

── END COPY ──

---

## Full Thread (10 tweets)

── START COPY ──

1/ 𝗝𝘂𝗻𝗲 𝟭, 𝟮𝟬𝟮𝟲: GitHub Copilot retires Premium Request Units.

Token-metered GitHub AI Credits take over.
1 credit = $0.01 USD.

The bill now reflects the actual tokens your request consumes. 🧵

2/ The new categories: 𝗟𝗶𝗴𝗵𝘁𝘄𝗲𝗶𝗴𝗵𝘁 / 𝗩𝗲𝗿𝘀𝗮𝘁𝗶𝗹𝗲 / 𝗣𝗼𝘄𝗲𝗿𝗳𝘂𝗹.

Short Lightweight chat: ~$0.001/request
Versatile review: ~$0.04/request
Powerful agent session: ~$0.45/request

A ~𝟰𝟱𝟬𝘅 𝗽𝗲𝗿-𝗿𝗲𝗾𝘂𝗲𝘀𝘁 𝘀𝗽𝗿𝗲𝗮𝗱.

3/ But "use the cheapest model" is bad advice.

Apple ML Research found reasoning models burn extra tokens on simple tasks — with 𝘻𝘦𝘳𝘰 quality improvement.

Standard models were actually 𝗯𝗲𝘁𝘁𝗲𝗿 on low-complexity items.

machinelearning.apple.com/research/illusion-of-thinking

4/ The 3-category taxonomy:

▸ 𝗟𝗶𝗴𝗵𝘁𝘄𝗲𝗶𝗴𝗵𝘁 (60-70%): rename, docs, boilerplate
▸ 𝗩𝗲𝗿𝘀𝗮𝘁𝗶𝗹𝗲 (20-30%): review, refactor, debug
▸ 𝗣𝗼𝘄𝗲𝗿𝗳𝘂𝗹 (5-10%): multi-file, system design, deep agent

5/ The cost math for 100 requests/day:

65 lightweight @ ~$0.001 = $0.065
25 versatile @ ~$0.04 = $1.00
10 powerful @ ~$0.30 = $3.00

𝗗𝗮𝗶𝗹𝘆: ~$𝟰.𝟬𝟳

vs ~$30 if you ran everything Powerful. ~86% reduction.

6/ Production validation:

▸ RouteLLM (LMSYS, 2024): 95% flagship quality using only 14% flagship calls — 75% cost cut. lmsys.org/blog/2024-07-01-routellm
▸ CascadeFlow: 69% savings, 96% quality retention
▸ Real team: $3,000/day → $970/day ($740K/yr saved)

7/ Plan allowances (matching subscription fee):

▸ Pro: $10 credits/mo
▸ Pro+: $39 credits/mo
▸ Business: $19/user/mo ($30 promo Jun–Aug)
▸ Enterprise: $39/user/mo ($70 promo Jun–Aug)

Code completions + Next Edit remain unmetered.

8/ For AI team leads and decision-makers — four actions before June 1:

1) Document a Lightweight/Versatile/Powerful task taxonomy
2) Set budget alerts at 50/75/90% of the 𝘴𝘵𝘢𝘯𝘥𝘢𝘳𝘥 allowance
3) Review top-consuming workflows monthly
4) Invest in context engineering training, not model restrictions

9/ The 3-layer optimization stack (full series):

𝗟𝗮𝘆𝗲𝗿 𝟭: Context engineering → 50-85% fewer tokens (Part 1)
𝗟𝗮𝘆𝗲𝗿 𝟮: Caching + workflow discipline (Part 2)
𝗟𝗮𝘆𝗲𝗿 𝟯: Category-based routing (Part 3)

Combined: ~𝟵𝟬% effective cost reduction with 𝘣𝘦𝘵𝘵𝘦𝘳 output.

10/ Part 3 published:
sendtoshailesh.github.io/blog/ai-code-assistant-model-selection-part-3.html

⚠ Edge case: annual Pro/Pro+ subscribers stay on PRU multipliers until plan expiry — and the multipliers *increase* for that group on June 1. Plan renewals accordingly.

11/ Sources (verify the ground rules):
• GitHub Blog (usage-based billing): github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing
• GitHub Docs (models and pricing): docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing
• Apple ML Research: machinelearning.apple.com/research/illusion-of-thinking
• RouteLLM (LMSYS, 2024): lmsys.org/blog/2024-07-01-routellm
• Specific model names are as of May 2026; the Lightweight/Versatile/Powerful taxonomy is what stays durable as models rotate.

#GitHubCopilot #AICredits #ModelRouting #AIEngineering #DeveloperProductivity

── END COPY ──

---

### Posting Notes

- **Best timing**: Tuesday-Thursday, 8-10am PT
- **Image**: Attach `content/visuals/task-model-alignment.png` to tweet 4
- **Cadence**: Post all tweets in rapid succession (thread)
- **Engagement**: Reply to responses within 4 hours of posting
