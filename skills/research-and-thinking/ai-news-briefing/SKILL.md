---
name: ai-news-briefing
description: >
  Use when an operator says "/ai-news," "AI news briefing," "AI news today," "what's new in AI,"
  "catch me up on AI," "AI update," "daily AI brief," "/morning-brief," or any variant asking for
  a rundown of recent AI developments. Produces a comprehensive catchup covering the last 24 hours
  (default) across frontier model releases, enterprise product launches, research breakthroughs,
  funding and M&A, regulation, and consumer/creative tools — plus a 2-3 sentence summary of the
  latest AI Daily Brief episode (Nathaniel Whittemore). Neutral scope by default; operator can
  narrow the lens (e.g., "focus on enterprise," "just frontier models," "only regulation"). Fire
  this skill any time the user wants to know what happened in AI recently, even if they don't use
  the word "briefing." Defaults to the current date unless another date is specified.
---

# AI News Briefing

 daily AI catchup: everything that happened in AI in the last 24 hours, in one brief. Built so anyone on the team can log in, run this, and walk away caught up — whether they're prepping a client call, writing, or just staying current.

## Scope

**Default: neutral and broad.** Cover anything meaningfully new across AI in the window. Don't pre-filter for audience. Categories to sweep:

- **Frontier models & labs** — OpenAI, Anthropic, Google DeepMind, Meta, xAI, Mistral, DeepSeek, Alibaba/Qwen, and any new lab with a credible release
- **Enterprise & hyperscaler launches** — Microsoft, Google Cloud, AWS, Oracle, Salesforce, ServiceNow, SAP, NVIDIA, Databricks, Snowflake
- **Consumer & creative tools** — ChatGPT/Claude/Gemini app updates, image/video/audio generation (Midjourney, Runway, ElevenLabs, Suno), dev tools (Cursor, Windsurf, Replit, GitHub)
- **Research** — new architectures, agentic capabilities, reasoning, context, benchmarks, notable papers
- **Funding, M&A, and business moves** — rounds over $25M, acquisitions, strategic partnerships, named deployments
- **Policy & regulation** — US, EU, UK, China — executive orders, court rulings, major legislative moves
- **Competitive dynamics** — lab vs lab, hyperscaler vs hyperscaler, platform shifts

**Operator can narrow the lens.** If the operator says "just enterprise," "focus on research," "skip consumer," "only policy" — honor it and trim accordingly. If they don't specify, stay broad.

**What to deprioritize (but don't silently drop):**
- Random Hugging Face uploads, minor fine-tunes, trivial version bumps
- Prompt engineering tips, "10 hacks" content, influencer hot takes unless they break news
- Single-source rumors without corroboration (label as rumor, don't promote to fact)
- Vendor echo (five outlets covering one OpenAI post is one source, not five)

If the operator's angle suggests they'd want the hobbyist/creator side surfaced more (e.g., "catch me up on the AI art scene"), flex accordingly.

## Sources (priority order)

1. **Primary (HIGH trust)** — lab and hyperscaler blogs directly
   - openai.com/blog, anthropic.com/news, deepmind.google/discover/blog, ai.meta.com/blog
   - blogs.microsoft.com/ai, cloud.google.com/blog/products/ai-machine-learning, aws.amazon.com/blogs/machine-learning
   - nvidia.com/en-us/ai/, databricks.com/blog, huggingface.co/blog (for major HF announcements)
2. **AI Daily Brief** — Nathaniel Whittemore's podcast. Find the latest episode via WebSearch ("AI Daily Brief Nathaniel Whittemore latest episode" + today's date). Usable surfaces: Spotify show page, YouTube channel, the podcast's show-notes site, or his Substack.
3. **Business press (MEDIUM-HIGH trust)** — Bloomberg, Reuters, The Information, WSJ, FT, Axios AI+, Semafor Technology
4. **Trade press (MEDIUM trust)** — TechCrunch, The Verge, Wired, Ars Technica, VentureBeat, 404 Media
5. **Analyst/newsletter (MEDIUM trust, cross-verify)** — Stratechery, Platformer, Import AI, The Rundown, Ben's Bites

If a story only appears on a single low-trust source, label it LOW and note it — don't drop it silently, and don't elevate it to fact.

## Steps

1. **Confirm the date window.** Default: last 24 hours from today (the date shown in system context). If operator specifies a different window ("last week," "since Friday"), use that.
2. **Check for lens narrowing.** If the operator specified a focus area (enterprise, research, policy, consumer, etc.), weight the sweep accordingly. Otherwise cover everything.
3. **Sweep primary sources first** — lab and hyperscaler blogs for announcements in the window. Highest signal.
4. **Sweep business and trade press** for deployments, funding, regulation, M&A, and stories the labs didn't self-announce.
   - **Fresh reporting on an older story counts.** If a major outlet breaks new details about an event from outside the window (e.g., Bloomberg reveals previously-unreported specifics of a deal announced two weeks ago), include it — but frame it around the new reporting, not the old event. State the report date clearly and credit the outlet. Do not include stories where the "new" coverage is just a recycled summary with no new information.
5. **Locate the latest AI Daily Brief episode.** Get the episode title, publish date, and enough content (show notes, description, transcript snippet) to write a 2-3 sentence summary. **If the latest episode is older than 48 hours, skip the AI Daily Brief section entirely** and note it under "Notable by Absence" instead (e.g., "No new AI Daily Brief episode in the last 48 hours — latest is from [date]"). If it's within 48 hours but older than 24, include it and lead with "Latest episode (published [date], [N] days ago):".
6. **Consolidate vendor echo.** If ten outlets covered one announcement, link the primary source and note briefly that it got wide coverage.
8. **Check for notable absences.** If a major lab has been silent for a week, a rumored announcement didn't land, or an expected launch slipped — that's signal worth flagging.
9. **Write the brief.** Short and honest beats long and padded. If the window was quiet, say so.

## Output

```
# AI News Briefing — [YYYY-MM-DD]

## TL;DR
[2-4 bullets. The stuff someone needs before their next client call or meeting.]

## Frontier Models & Labs
### [Product/Model Name] — [Lab]
- **What:** [1-2 sentences]
- **Why it matters:** [1 sentence]
- **Source:** [Primary link only]

[Repeat per release. Omit section if nothing in window.]

## Enterprise & Hyperscaler
### [Product/Launch] — [Vendor]
- **What:** [1-2 sentences]
- **Why it matters:** [1 sentence]
- **Source:** [Primary link only]

[Omit section if empty.]

## Consumer & Creative
- **[Product]:** [1-2 sentences.] — [Primary link only]
[Omit section if empty.]

## Research
- **[Paper/finding]:** [1-2 sentences. Why it matters.] — [Primary link only]
[Omit section if empty.]

## Funding, M&A & Deployments
- **[Company]:** [1-2 sentences. Amount, lead, deal.] — [Primary link only]
[Omit section if empty.]

## Policy & Regulation
- **[Jurisdiction/Topic]:** [1-2 sentences.] — [Primary link only]
[Omit section if empty.]

## AI Daily Brief — [Episode Title]
**Published:** [Date] | **Host:** Nathaniel Whittemore
[2-3 sentence summary. If episode is 24-48h old, lead with: "Latest episode (published [date], [N] days ago):"]
**Link:** [URL]

[OMIT this entire section if the latest episode is older than 48 hours. Instead, surface the absence under "Notable by Absence" below.]

## Notable by Absence
[Anything conspicuously quiet — major lab silent, expected launch missed, rumored announcement didn't land, pattern break. Omit section if nothing applies.]

## Gaps
[What couldn't be verified in the time available — paywalled sources, single-source claims, rumors not yet corroborated. Omit section if nothing applies.]
```

## Gotchas

- **Date discipline.** "Last 24 hours" means published in the last 24 hours, not "recently discussed." Check publish timestamps, not article dates that get refreshed.
- **Vendor echo.** If five outlets cover an OpenAI release, that's one source (OpenAI's blog) echoed five times, not five independent signals. Link the primary.
- **Rumor vs announcement.** "Sources familiar with the matter" is not an announcement. Label rumors as rumors.
- **Recycled news.** Watch for "explainer" pieces republished without new information.
- **AI Daily Brief frequency.** Usually weekdays. No new episode on weekends or holidays is normal — don't invent one. Say "most recent episode is from [date]."
- **Paywalls.** The Information and WSJ often have the best scoops. If paywalled, cite the headline and the fact of the paywall, don't fabricate the content.
- **Time zones.** Default is CDT (per `context/me.md`). "Last 24 hours" is relative to CDT unless specified.
- **Scope creep.** Neutral default doesn't mean dump everything. Still apply judgment — skip the noise, keep the signal. If you're including an item, you should be able to say in one sentence why it matters.

## Constraints

- **Every item must include a working source URL.** No unsourced assertions, no "per reports," no naked citations. If a story was found via WebSearch, capture the actual article URL, not the search results page. If a story is paywalled, still include the link and label `(paywall)`.
- **One source link per item.** Always the primary — the lab's own blog post, the company's own press release, or (for reporting-driven stories) the outlet that broke it. Do not stack multiple links per item. If the primary source is paywalled, link it anyway and label `(paywall)`; only fall back to a secondary source if no primary exists.
- If OpenAI announces something and TechCrunch covers it, link OpenAI's post — not both.
- Format every source as a clickable markdown link: `[Publisher or Source Name](https://...)`. Never output a bare domain or "source: TechCrunch" without the URL.
- The AI Daily Brief section must include the direct episode link (Spotify, YouTube, or Substack — whichever surface the episode was found on), not just the show's homepage.
- The AI Daily Brief summary must be 2-3 sentences. Not 1. Not 5.
- Honor the operator's lens narrowing when specified. Default is broad; "focus on X" means trim the rest.
- If the window is quiet, say so. A short honest brief beats a padded one.

