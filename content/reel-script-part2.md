# Reel Script: Invisible Compound Savings

**Duration**: 60 seconds (Reels/Shorts) / 75 seconds (LinkedIn Video)
**Format**: A — "Did You Know?" (Data Shock)
**Platforms**: Instagram Reels, YouTube Shorts, LinkedIn Video
**Aspect ratio**: 9:16 (1080x1920)
**Source**: `content/ai-code-assistant-cost-part-2.md`

---

## Shot List

| Time | Visual | Voiceover | Text Overlay |
|------|--------|-----------|--------------|
| 0:00-0:05 | Dark screen with a repeating animation: same block of text sent 10 times, each with a price tag | "Ninety percent of the context you send your AI is the same every time. And you're paying full price for all of it." | **Same context. Full price. Every time.** |
| 0:05-0:12 | Cut to `caching-flow.png` visual, zoom into the cost comparison between Request 1 and Request 10 | "OpenAI and Anthropic offer ninety percent off for cached tokens. Your system prompt, instructions, file context — they repeat across every prompt in a session." | **90% off cached tokens** |
| 0:12-0:20 | Animated counter: 1,000,000 tokens counting down to 109,000 | "A ten-thousand token prefix across one hundred requests? Without caching: a million tokens. With caching: a hundred and nine thousand. By request ten, the prefix is free." | **1M -> 109K tokens** |
| 0:20-0:28 | Screen recording: developer typing "try again" in Copilot Chat, then "that's not what I meant", then another retry | "But there's a hidden cost nobody talks about. The retry tax. If forty percent of your prompts need a follow-up, you're paying one-point-four x baseline." | **The Retry Tax: 1.4x** |
| 0:28-0:38 | Cut to `retry-tax-calculator.png` visual, highlight the 30-50% danger zone | "Most developers live in the thirty to fifty percent retry range without knowing it. Every vague prompt, every 'try again' — full-price tokens for zero output." | **30-50% retry rate = hidden cost** |
| 0:38-0:48 | Screen recording: developer closing files, starting fresh thread, typing a specific prompt with #file reference | "The fix is structural. Stable instructions enable caching. Fresh threads maximize cache hits. Specific prompts eliminate retries." | **Set once. Compounds forever.** |
| 0:48-0:55 | Split screen: left shows "Before" with retry loop, right shows "After" with single clean request | "Same model. Same task. Better habits. Lower cost." | **Better habits = less waste** |
| 0:55-0:60 | End card: series title + "Part 2 of 3" + follow prompt | "Part two of three. Part three covers the one-twenty-x model spread — when expensive models help and when they don't. Follow for that." | **Part 2 of 3 | Follow** |

---

## Screen Recording Notes

- **App**: VS Code with GitHub Copilot extension active
- **Theme**: Dark theme
- **Setup for retry tax shot (0:20-0:28)**:
  - Open Copilot Chat with some history
  - Type a vague prompt: "fix the login issue"
  - Show confused response
  - Type: "try again"
  - Show another mediocre response
  - Type: "that's not what I meant, the session timeout is wrong"
  - Point: 3 requests for 1 task = 3x the cost
- **Setup for fix shot (0:38-0:48)**:
  - Close all unrelated files
  - Open fresh Copilot Chat thread
  - Type: `#file:src/auth/session.ts The session timeout logic at line 23 should use a 30-minute window instead of 60. Update the TTL constant and the expiration check.`
  - Show clean, correct response on first attempt
- **Zoom**: 150-200% on relevant UI area

---

## Voiceover Script (Full)

> Ninety percent of the context you send your AI is the same every time. And you're paying full price for all of it.
>
> OpenAI and Anthropic offer ninety percent off for cached tokens. Your system prompt, instructions, file context — they repeat across every prompt in a session.
>
> A ten-thousand token prefix across one hundred requests? Without caching: a million tokens. With caching: a hundred and nine thousand. By request ten, the prefix is free.
>
> But there's a hidden cost nobody talks about. The retry tax. If forty percent of your prompts need a follow-up, you're paying one-point-four x baseline.
>
> Most developers live in the thirty to fifty percent retry range without knowing it. Every vague prompt, every "try again" — full-price tokens for zero output.
>
> The fix is structural. Stable instructions enable caching. Fresh threads maximize cache hits. Specific prompts eliminate retries.
>
> Same model. Same task. Better habits. Lower cost.
>
> Part two of three. Part three covers the one-twenty-x model spread — when expensive models help and when they don't. Follow for that.

**Word count**: ~145 words (~58-62 seconds at conversational pace)

---

## Captions & Hashtags

### Instagram Reels / YouTube Shorts

90% of your AI prompt context repeats every request.
You're paying full price for it.

Caching = 90% off. Retry elimination = 1.4x savings.

Set once. Compounds forever. Part 2 of 3.

#PromptCaching #GitHubCopilot #AIEngineering #CodingTips #DeveloperTools

### LinkedIn Video

90% of your AI code assistant context is identical across requests. OpenAI and Anthropic cache repeated prefixes at 90% off.

The other hidden cost: the retry tax. If 40% of requests need follow-ups, effective spend = 1.4x baseline.

The fix: stable instructions (auto-caching) + specific prompts (no retries). Set once, compounds forever.

Part 2 of 3. Full breakdown in comments.

#PromptCaching #GitHubCopilot #AIEngineering #DeveloperProductivity

---

## Thumbnail / Cover Frame

**Visual**: Dark background with split composition.
- Left side: Repeating text blocks with dollar signs, red-tinted. "Full price x100"
- Right side: Same blocks but grayed out (cached), one active. "90% off x99"
- Center: Large "90%" with discount tag
- Bottom: "Prompt Caching" in white text
- Top corner: "Part 2/3" badge
