# LinkedIn Post — Part 3: From PRUs to Tokens

## Plain Text Version

── START COPY ──

On June 1, 2026, GitHub Copilot retires Premium Request Units.

Token-metered AI Credits take over (1 credit = $0.01 USD).

A short chat reply on a Lightweight model costs ~$0.001. A deep agent-mode session on a Powerful model can cost $0.45. That's a ~450x per-request cost spread — and now it shows up on your bill as actual dollars.

This is not a "use cheap models" story. Apple ML Research found that reasoning models burn thousands of extra tokens on simple tasks — with zero quality improvement. The expensive model is not always the better choice.

GitHub now categorizes every model into three durable buckets:

Lightweight (60-70% of daily tasks)
Variable rename, boilerplate, test scaffold, docstrings, imports.
Examples (May 2026): GPT-5 mini, GPT-5.4 nano, Gemini 3.5 Flash.

Versatile (20-30%)
Code review, refactoring, debugging, architecture questions.
Examples (May 2026): Claude Sonnet 4.x, GPT-4.1, GPT-5.4, Claude Haiku 4.5.

Powerful (5-10%)
Multi-file refactoring, novel algorithms, system design.
Examples (May 2026): Claude Opus 4.x, GPT-5.5, Gemini 2.5 Pro.

The cost math for 100 daily requests (real dollars):
- 65 lightweight at ~$0.001 = $0.065
- 25 versatile at ~$0.04 = $1.00
- 10 powerful at ~$0.30 = $3.00
- Daily total: ~$4.07 — about 86% less than "Powerful for everything"

Apply Part 1 (context engineering) and Part 2 (caching) on top and a developer comfortably stays inside Pro's $10/month credit allowance.

RouteLLM proved this at scale: 95% of flagship-model quality using only 14% flagship calls. A production team dropped from $3,000/day to $970/day — 68% reduction ($740K/year) — through routing alone.

This is the final layer of a three-part stack:
1. Context engineering (50-85% token reduction) [Part 1]
2. Caching + workflow discipline (up to 90% on repeated context) [Part 2]
3. Model selection across Lightweight/Versatile/Powerful categories [Part 3]

Combined potential: ~90% effective cost reduction with better output quality.

Start with context. Everything else follows.

Full series: https://sendtoshailesh.github.io/blog/series/ai-code-assistant-optimization.html

Sources (paste URLs into a browser to verify):
- GitHub Blog (usage-based billing): https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
- GitHub Docs (models and pricing): https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing
- Apple ML Research: https://machinelearning.apple.com/research/illusion-of-thinking
- RouteLLM (LMSYS): https://lmsys.org/blog/2024-07-01-routellm/

#GitHubCopilot #AICredits #AIEngineering #DeveloperProductivity #ModelSelection

── END COPY ──

---

## Unicode Formatted Version

── START COPY ──

On 𝗝𝘂𝗻𝗲 𝟭, 𝟮𝟬𝟮𝟲, GitHub Copilot retires Premium Request Units.

Token-metered 𝗔𝗜 𝗖𝗿𝗲𝗱𝗶𝘁𝘀 take over (1 credit = $0.01 USD).

A short chat reply on a 𝗟𝗶𝗴𝗵𝘁𝘄𝗲𝗶𝗴𝗵𝘁 model costs ~$0.001. A deep agent session on a 𝗣𝗼𝘄𝗲𝗿𝗳𝘂𝗹 model can cost $0.45. That is a 𝗮 ~𝟰𝟱𝟬𝘅 𝗽𝗲𝗿-𝗿𝗲𝗾𝘂𝗲𝘀𝘁 𝗰𝗼𝘀𝘁 𝘀𝗽𝗿𝗲𝗮𝗱, now visible on your bill in real dollars.

But this is 𝘯𝘰𝘵 a "use cheap models" story.

Apple ML Research: reasoning models burn thousands of extra tokens on simple tasks — 𝘻𝘦𝘳𝘰 quality gain. Light models actually score better on low-complexity items.

━━━

GitHub's three durable model categories:

𝟭. 𝗟𝗶𝗴𝗵𝘁𝘄𝗲𝗶𝗴𝗵𝘁 (60-70%) — rename, boilerplate, scaffolding
▸ Examples (May 2026): GPT-5 mini, GPT-5.4 nano, Gemini 3.5 Flash

𝟮. 𝗩𝗲𝗿𝘀𝗮𝘁𝗶𝗹𝗲 (20-30%) — review, refactor, debug
▸ Examples (May 2026): Claude Sonnet 4.x, GPT-4.1, Claude Haiku 4.5

𝟯. 𝗣𝗼𝘄𝗲𝗿𝗳𝘂𝗹 (5-10%) — multi-file refactor, system design
▸ Examples (May 2026): Claude Opus 4.x, GPT-5.5, Gemini 2.5 Pro

━━━

📊 𝗖𝗼𝘀𝘁 𝗺𝗮𝘁𝗵 (100 requests/day, real dollars):

▸ 65 lightweight at ~$0.001 = $0.065
▸ 25 versatile at ~$0.04 = $1.00
▸ 10 powerful at ~$0.30 = $3.00
▸ 𝗗𝗮𝗶𝗹𝘆 𝘁𝗼𝘁𝗮𝗹: ~$𝟰.𝟬𝟳 (𝘃𝘀 ~$𝟯𝟬 𝗶𝗳 𝗮𝗹𝗹 𝗣𝗼𝘄𝗲𝗿𝗳𝘂𝗹)

RouteLLM: 95% flagship-tier quality using only 14% flagship calls (in the 2024 LMSYS paper, "flagship" = GPT-4 baseline).
Production team: $3K/day -> $970/day (68% reduction).

━━━

🎯 𝗧𝗵𝗲 𝗰𝗼𝗺𝗽𝗹𝗲𝘁𝗲 𝘀𝘁𝗮𝗰𝗸:

𝗟𝗮𝘆𝗲𝗿 𝟭: Context engineering (50-85% token reduction)
𝗟𝗮𝘆𝗲𝗿 𝟮: Caching + workflow discipline (up to 90% on repeated context)
𝗟𝗮𝘆𝗲𝗿 𝟯: Model selection across Lightweight/Versatile/Powerful

Combined: ~𝟵𝟬% effective cost reduction with 𝘣𝘦𝘵𝘵𝘦𝘳 output quality.

Start with context. Everything else follows.

Full 3-part series: https://sendtoshailesh.github.io/blog/series/ai-code-assistant-optimization.html

Sources (verify the ground rules):
• GitHub Blog (usage-based billing): https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
• GitHub Docs (models and pricing): https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing
• Apple ML Research: https://machinelearning.apple.com/research/illusion-of-thinking
• RouteLLM (LMSYS): https://lmsys.org/blog/2024-07-01-routellm/

#GitHubCopilot #AICredits #AIEngineering #DeveloperProductivity #ModelSelection

── END COPY ──
