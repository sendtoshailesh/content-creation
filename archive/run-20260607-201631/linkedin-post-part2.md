# LinkedIn Post — Part 2: Invisible Compound Savings

## Plain Text Version

── START COPY ──

90% of your AI prompt context is the same across every request.

You are paying full price for it every time.

OpenAI and Anthropic both offer a 90% discount on cached input tokens via their APIs — and under GitHub Copilot's new usage-based billing (June 1), cached tokens consume credits at 75-90% less than regular input tokens. If your system prompt, copilot-instructions file, and active file context repeat across prompts in a session — and they do — caching kicks in and charges a fraction of the cost.

Here's the math for a 10K token prefix across 100 daily requests:

▸ Without caching: 1,000,000 tokens at full price
▸ With caching: ~109,000 effective tokens (89% savings on prefix)
▸ By request 10, the prefix is essentially free

But caching is only half the story. The other half is the retry tax.

If 40% of your AI code assistant requests need a follow-up or correction, your effective spend is 1.4x baseline. At 50%, it's 1.5x. Every "try again" is a full-price request that produced zero value.

Five workflow disciplines that eliminate retries:

1. One task per prompt (don't bundle unrelated asks)
2. Diagnose before retrying (was the context wrong? the prompt ambiguous?)
3. Structured commit messages (clean metadata = better future AI context)
4. Clean project structure (meaningful directories and file patterns)
5. Measure cost per successful task, not cost per request

The connection to Part 1: context engineering enables caching. When you close irrelevant files and maintain stable instructions, you create a consistent prefix that caches automatically. Clean context is cacheable context.

These are set-and-forget optimizations. One-time setup, compounding returns across every AI interaction.

Part 2 of 3. Part 1 covered context engineering (85% token reduction, better output). Part 3 covers model selection (the 120x multiplier spread).

Full post: https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html

#ContextEngineering #GitHubCopilot #AIEngineering #DeveloperProductivity #PromptCaching

── END COPY ──

---

## Unicode Formatted Version

── START COPY ──

90% of your AI prompt context is the same across every request.

𝗬𝗼𝘂 𝗮𝗿𝗲 𝗽𝗮𝘆𝗶𝗻𝗴 𝗳𝘂𝗹𝗹 𝗽𝗿𝗶𝗰𝗲 𝗳𝗼𝗿 𝗶𝘁 𝗲𝘃𝗲𝗿𝘆 𝘁𝗶𝗺𝗲.

OpenAI and Anthropic both offer a 90% discount on cached input tokens via their APIs — and under GitHub Copilot's new usage-based billing, cached tokens consume credits at 75-90% less than regular input. If your system prompt, copilot-instructions, and file context repeat across prompts — and they do — caching charges a 𝗳𝗿𝗲𝗰𝘁𝗶𝗼𝗻 of the cost.

━━━

📊 𝗧𝗵𝗲 𝗺𝗮𝘁𝗵 (10K token prefix, 100 requests/day):

▸ Without caching: 1,000,000 tokens at full price
▸ With caching: ~109,000 effective tokens
▸ 𝟴𝟵% 𝘀𝗮𝘃𝗶𝗻𝗴𝘀 on prefix tokens
▸ By request 10, the prefix is essentially free

━━━

⚠️ 𝗧𝗵𝗲 𝗿𝗲𝘁𝗿𝘆 𝘁𝗮𝘅:

If 40% of your requests need a follow-up, effective spend = 1.4x baseline.

Every "try again" is a full-price request that produced 𝘻𝘦𝘳𝘰 value.

Five disciplines that eliminate it:

𝟭. One task per prompt (don't bundle)
𝟮. Diagnose before retrying (fix the root cause)
𝟯. Structured commit messages (better future AI context)
𝟰. Clean project structure (AI reads your file tree)
𝟱. Measure cost per 𝘴𝘶𝘤𝘤𝘦𝘴𝘴𝘧𝘶𝘭 task, not cost per request

━━━

🎯 𝗧𝗵𝗲 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻:

Context engineering (Part 1) 𝘦𝘯𝘢𝘣𝘭𝘦𝘴 caching. Clean context = consistent prefix = automatic cache hits.

These are set-and-forget optimizations. One-time setup, compounding returns across every interaction.

Part 2 of 3. Part 1: context engineering (85% fewer tokens, better output). Part 3: model selection (the 120x spread).

Full post: https://sendtoshailesh.github.io/blog/ai-code-assistant-caching-workflow-part-2.html

#ContextEngineering #GitHubCopilot #AIEngineering #DeveloperProductivity #PromptCaching

── END COPY ──
