# X/Twitter Thread — Part 2: Prompt Caching + Retry Tax

## Standalone Summary Tweet

── START COPY ──

90% of your AI coding prompt context repeats across requests.

If you’re paying full price each time, you’re overspending.

Part 2: prompt caching + retry-tax discipline to cut waste without sacrificing output quality. 🧵

── END COPY ──

---

## Full Thread (10 tweets)

── START COPY ──

1/ 90% of your AI coding context is often repeated across requests:

▸ system prompt  
▸ project instructions  
▸ active file context

That repeated prefix can be cached. 🧵

2/ Under usage-based billing, cached input is significantly cheaper than fresh input.

Typical range: 75–90% lower cost for repeated prefix tokens (model-dependent).

3/ Simple example:

10K stable prefix × 100 requests/day

Without caching: 1,000,000 full-price prefix tokens  
With caching: ~109,000 effective prefix tokens

That’s ~89% savings on prefix spend.

4/ Caching only works when your prefix stays stable.

If you constantly churn context, you reset cache benefits.

5/ Three habits that improve cache hit rate:

▸ keep instructions stable  
▸ stay in one thread for one feature  
▸ avoid unnecessary file/context churn

Clean context = cacheable context.

6/ Now the hidden leak: retry tax.

If 40% of requests need follow-ups, effective spend becomes ~1.4x baseline.

7/ Every vague “try again” is usually:

▸ full-price request  
▸ low-value output  
▸ more stale context added to history

Retries compound cost + confusion.

8/ Reduce retries with workflow discipline:

1) one task per prompt  
2) diagnose failure before retry  
3) specify file + constraint + expected output

9/ Real optimization is multiplicative:

Caching lowers cost per good request.  
Prompt quality lowers number of bad requests.

Do both together.

10/ Part 2 of 3 in the series:

Part 1: context engineering foundations  
Part 3: model routing and when expensive models are worth it

Published canonical URL: https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html

#PromptCaching #ContextEngineering #GitHubCopilot #AIEngineering #DeveloperProductivity

── END COPY ──
