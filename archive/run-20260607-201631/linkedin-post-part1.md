# LinkedIn Post — Part 1: Spend Fewer Tokens, Get Better Code

## Plain Text Version

── START COPY ──

Anthropic cut tool context by 85%.

Accuracy improved from 49% to 74%.

They removed information and the AI got better.

Your AI code assistant has the same problem. Most developers assume more context helps. The data says the opposite.

Here's what the research shows:

▸ 30-70% of typical AI prompt context is noise that actively degrades output (TDS analysis)
▸ Anthropic's Tool Search: 85% fewer tokens, accuracy jumped 25 percentage points
▸ SWEzze paper: 6x context compression delivered 5-9.2% BETTER issue resolution with 51-71% fewer tokens
▸ Programmatic Tool Calling: 37% fewer tokens AND accuracy improved from 25.6% to 28.5%

The pattern is unambiguous: less noise = better output.

I've been applying this as "context engineering" — five practices that improve what your AI code assistant produces:

1. Close irrelevant files before prompting (reduces conflicting signals)
2. One thread per task (eliminates stale context steering output wrong)
3. Use #file references for targeted context (focuses model attention)
4. Front-load intent in prompts (state what you want first, then details)
5. Maintain a copilot-instructions.md file (stable, cacheable project context)

Every practice passes one test: "Would I do this even if AI were free?"

The answer is yes for all five. They make you more effective. The token reduction is a bonus.

And starting June 1, that bonus matters more — GitHub Copilot moves to usage-based billing where every junk token shows up on the bill.

But the advice is durable regardless of billing model. Better input produces better output whether you pay per token or nothing at all.

This is Part 1 of 3. Part 2 covers caching (90% savings with zero quality trade-off) and workflow discipline. Part 3: when expensive models genuinely help.

Full post with before/after data from Anthropic, SWEzze, and GitHub: https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html

#ContextEngineering #GitHubCopilot #AIEngineering #DeveloperProductivity #PromptEngineering

── END COPY ──

---

## Unicode Formatted Version

── START COPY ──

Anthropic cut tool context by 85%.

Accuracy improved from 49% to 74%.

𝗧𝗵𝗲𝘆 𝗿𝗲𝗺𝗼𝘃𝗲𝗱 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗮𝗻𝗱 𝘁𝗵𝗲 𝗔𝗜 𝗴𝗼𝘁 𝗯𝗲𝘁𝘁𝗲𝗿.

Your AI code assistant has the same problem. Most developers assume more context helps. The data says the opposite.

━━━

𝗧𝗵𝗲 𝗿𝗲𝘀𝗲𝗮𝗿𝗰𝗵:

▸ 30-70% of AI prompt context is noise that 𝘢𝘤𝘵𝘪𝘷𝘦𝘭𝘺 𝘥𝘦𝘨𝘳𝘢𝘥𝘦𝘴 output
▸ Anthropic Tool Search: 85% fewer tokens, accuracy 49% -> 𝟳𝟰%
▸ SWEzze: 6x compression = 5-9.2% 𝗕𝗘𝗧𝗧𝗘𝗥 issue resolution + 51-71% fewer tokens
▸ Programmatic Tool Calling: 37% fewer tokens AND accuracy improved

𝘓𝘦𝘴𝘴 𝘯𝘰𝘪𝘴𝘦 = 𝘣𝘦𝘵𝘵𝘦𝘳 𝘰𝘶𝘵𝘱𝘶𝘵. Every time.

━━━

𝗙𝗶𝘃𝗲 𝗰𝗼𝗻𝘁𝗲𝘅𝘁 𝗲𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴 𝗽𝗿𝗮𝗰𝘁𝗶𝗰𝗲𝘀 that improve AI code assistant output:

𝟭. Close irrelevant files before prompting
𝟮. One thread per task (fresh context, clean slate)
𝟯. Use #file references for targeted context
𝟰. Front-load intent (state goal first, then details)
𝟱. Maintain a copilot-instructions.md file

Every practice passes this test: 𝘞𝘰𝘶𝘭𝘥 𝘐 𝘥𝘰 𝘵𝘩𝘪𝘴 𝘦𝘷𝘦𝘯 𝘪𝘧 𝘈𝘐 𝘸𝘦𝘳𝘦 𝘧𝘳𝘦𝘦?

Yes. All five. They make you more effective. The token reduction is a bonus.

━━━

📊 𝗧𝗵𝗲 𝘁𝗶𝗺𝗶𝗻𝗴:

Starting June 1, GitHub Copilot moves to usage-based billing. Every junk token now shows up on the bill.

But the advice is durable 𝘳𝘦𝘨𝘢𝘳𝘥𝘭𝘦𝘴𝘴 of billing model. Better input produces better output whether you pay per token or nothing at all.

━━━

🎯 𝗬𝗼𝘂𝗿 𝗳𝗶𝗿𝘀𝘁 𝗮𝗰𝘁𝗶𝗼𝗻:

Close every irrelevant file before your next Copilot prompt. Note whether the output improves. For most developers, it will.

Part 1 of 3. Next: caching (90% savings, zero quality trade-off) + workflow discipline.

Full post with before/after data: https://sendtoshailesh.github.io/blog/ai-code-assistant-context-engineering-part-1.html

#ContextEngineering #GitHubCopilot #AIEngineering #DeveloperProductivity #PromptEngineering

── END COPY ──
