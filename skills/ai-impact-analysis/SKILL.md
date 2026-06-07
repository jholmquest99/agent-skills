---
name: ai-impact-analysis
description: >
  Use when the user provides a company website URL or company name and asks for an
  AI impact analysis, says "what would AI do to this business," "run an impact read
  on [URL]," "AI impact for [company]," or wants a board-grade view of how AI is
  likely to reshape a target business. Produces a narrative report with supporting
  tables covering five domains (Financial, Market, Workforce, Brand, Product &
  Services) with a build-before-buy strategic lens, an AI moat thesis, and an
  honest accounting of what is known versus inferred. Activate Deep Research when
  available for the strongest output.
---

# AI Impact Analysis

A consulting tool for executive strategic conversations. Given a company's public website (and any other public sources research can surface), produces a written report on how AI is likely to reshape that business across five domains. The output is a doc-style narrative report with supporting tables, designed to be read by a CEO or shared with a leadership team.

The report holds up under executive scrutiny: defensible, specific, free of generic AI commentary, honest about what is known versus inferred, and grounded in named sources.

## Voice and tone

If a separate voice or style skill is loaded in this Project (FPOV's voice skill, for example), defer to it. Do not duplicate or override its guidance. If no voice skill is active, write executive-grade prose: direct, plain English, no jargon, no filler, no emojis, no em dashes, full sentences, paragraphs over bullet lists where the content supports it.

## Use Deep Research when available

The research phase should pull from more than the homepage. Activate Deep Research mode if it is on. Otherwise, instruct the assistant to research broadly across the company's site, leadership LinkedIn, recent press, podcasts and interviews, industry analyst commentary, named competitors, and sub-niche signals. The depth of sourcing is what separates this report from a generic AI-strategy template.

If the user has not enabled Deep Research and the report would benefit from it, say so once at the start of the analysis and offer to re-run with it on.

## Context to confirm before running

If the user has not provided these, ask:

- **Target URL or company name** (required)
- **Purpose**: strategic planning, board preparation, M&A diligence, internal AI roadmap, capability assessment, advisory conversation, other
- **Audience**: CEO, full board, leadership team, working group. This shapes register, not structure.

If only a URL is provided, default to purpose "strategic planning," audience "leadership team," and proceed.

---

## Methodology

### Step 1 — Research the company

Pull a complete picture from public sources:

- The company's site, end to end (positioning, services, product lines, customer logos, case studies, leadership, careers, blog, methodology pages, trust signals)
- Founder and leadership signals (LinkedIn, interviews, podcasts, conference talks, op-eds)
- Recent press, funding, M&A, layoffs or hiring waves, regulatory or legal hits
- Named competitors and how they are positioning around AI
- Industry analyst commentary and trade press for the sub-niche
- Any visible AI, automation, or technology language the company uses about itself

If Deep Research is on, use it. If it is off, search broadly anyway.

### Step 2 — Classify the business

Internally lock the following classifiers before writing the report. They do not appear as a bullet list in the output. They shape the narrative.

| Classifier | Options |
|---|---|
| Industry / sub-niche | Specific (descriptive, not "tech" or "services") |
| B2B / B2C / B2G | Pick one; note hybrids |
| Service / product / hybrid | Service-heavy, product-heavy, balanced |
| Recurring vs project revenue | Best read from public sources |
| Knowledge work intensity | High, medium, low |
| Customization spectrum | Templated, configured, fully bespoke |
| Regulatory pressure | High, medium, low |
| Apparent size band | Best read of revenue or headcount |
| AI maturity | Stated vs actual (often divergent) |
| Brand differentiator | One line, in their own positioning |
| Proprietary data and IP visible | Named where possible |

Mark anything inferred as a guess in the narrative.

### Step 3 — Develop the central thesis

Before writing, identify the single most important sentence the report needs to deliver. The thesis usually answers one of three questions:

1. Where does AI compress this business's economics fastest?
2. Where does AI most plausibly create durable advantage they could build?
3. Where does AI most directly threaten their differentiator?

The whole report should pull toward that thesis. Generic "AI will change everything" framing fails the test.

### Step 4 — Write the report

Five domains. Prose for the body, supplemented with tables where they earn their place (see "When to use tables" below). Risks woven into each domain narrative, not segregated into a list. Confidence handled in the language ("the public record makes this clear," "this is inferred from the team page and should be confirmed," "without revenue visibility this is a band, not a number"), with one explicit confidence note per domain.

### Step 5 — Close with the strategic call

End the report with a build-before-buy reading and an AI moat thesis specific to this company.

---

## When to use tables

Tables earn their place when they make scannable comparisons that prose buries. The narrative is still the spine of the report; tables sit alongside it, never replace it.

The following six tables are the standard pattern. Include all six unless the research genuinely does not support one (in which case omit it rather than padding).

1. **At a glance** (Executive Summary) — 2-column, 6 rows. Surface-level read: tells a CEO scanning the first page what they are about to read. Columns: Dimension | Reading. Rows include central thesis, highest exposure, largest opportunity, competitive position, strategic urgency.

2. **Competitive AI scorecard** (Business Context) — wide multi-column. Operators across the rows, AI capability dimensions across the columns. Highlight the target company's row visually (soft yellow fill, bold text) so the comparison reads at a glance. This is usually the most damning visual in the report.

3. **Financial impact heat map** (Financial Impact) — 5 columns. P&L lever | AI impact direction | Magnitude | Time horizon | Top risk if unaddressed. Ranks 6-10 levers.

4. **Workforce exposure by function** (Workforce Impact) — 5 columns. Function | Headcount band | AI exposure | Direction | Time horizon. Covers 6-10 functions ranging from frontline to HQ knowledge work.

5. **Product line AI ranking** (Product & Services Impact) — 5 columns. Product line | AI upside | Defensibility of moat | Build-vs-buy default | Sequencing priority. Ranks the company's actual product or service lines.

6. **Build-before-buy roadmap** (Strategic Recommendation) — 4 columns. Horizon | Move | Type (Build / Buy / Build + Buy) | Strategic purpose. Sequenced over 24 months in three horizons (0-6, 6-12, 12-24 months).

A seventh table — **Confidence by section** — is optional and goes in the Confidence section. 4 columns: Section | Confidence | Primary basis | What would raise it. Use it when the report is long enough that the per-section confidence statements are hard to find by scanning.

Keep prose around every table. Each table should be introduced (one line setting up what it shows) and followed by the synthesis the table itself cannot give (one paragraph naming the pattern). Do not let tables float without context.

---

## Output structure

The report is written as a document. Use Title Case for section headers throughout. Target length 4-7 pages (roughly 3,000 to 5,500 words including tables). Tables count toward usefulness, not toward length.

```
# AI Impact Analysis: [Company Name]

[Optional subtitle: a single line capturing the thesis in plain English. Italicized.]

**Prepared:** [YYYY-MM-DD]
**Purpose:** [Strategic planning / Board preparation / M&A diligence / etc.]

## Executive Summary

[3-5 paragraphs. Open with the thesis sentence. Name the company in plain English (they sell X to Y). State the single biggest AI exposure and the single biggest AI opportunity in clear terms. Preview the strategic call (build-before-buy thesis) without burying the lede. An executive reading only this section should walk away with the report's argument.]

### At a glance

[Standard 2-column table. 6 rows. Use this anywhere the executive summary runs longer than 3 paragraphs. Skip it only if the summary is genuinely short.]

## Business Context

[2-3 paragraphs. Plain-English description of what they actually do, who they serve, what their differentiator is in their own words versus what the market makes of it, where they sit on the size and maturity spectrum. Weave in the relevant classifiers (B2B/B2C/B2G, service vs product, regulatory pressure, customization, AI maturity guess) as prose, not a table. Name the brand DNA in one or two lines because Brand impact downstream depends on it.]

[Confidence statement.]

### Competitive AI Scorecard

[Wide multi-column table comparing the target company to its named competitors across 5-7 AI capability dimensions. Highlight the target company's row. Follow with one paragraph naming the pattern.]

## Financial Impact

[2-4 paragraphs. Where AI hits the P&L. Investment posture sized to the company's apparent scale. The top 2-3 ROI levers specific to this business model. Where margin expands if AI works. Where margin compresses if competitors move first. Risks named in the narrative, not bulleted: cost overruns, vendor lock-in, AI-driven price compression, capital allocation traps.]

### Financial Impact Heat Map

[5-column table ranking 6-10 P&L levers. Follow with one synthesis paragraph if the table reveals a pattern that prose did not already cover.]

[Confidence statement.]

## Market Impact

[2-4 paragraphs. How AI is changing the rules in this specific niche. Named competitor moves where they are visible. Cycle time compression both internally and as a client expectation. Disintermediation risk, commoditization risk, new-entrant risk specific to their segment. If supply chain is relevant to their model, address it; if not, do not pad.]

[Confidence statement.]

## Workforce Impact

[2-4 paragraphs. Which roles in their likely org are most exposed to AI augmentation or replacement, by name and function, not by abstraction. Skill shifts the team needs. Realistic throughput gains and where they land. Quality dynamics in both directions. Risks: senior talent retention, junior pipeline collapse, skill atrophy, brand exposure when AI-drafted output reaches clients.]

### Workforce Exposure by Function

[5-column table covering 6-10 functions. Follow with one paragraph if needed.]

[Confidence statement.]

## Brand Impact

[2-4 paragraphs. Does AI reinforce or erode their differentiator? Anchor this section in the brand DNA from Business Context. How customer relationships and trust dynamics shift. Public perception exposure specific to their industry. Founder dependency or thought-leadership concentration if applicable. Risks: brand dilution from generic AI output, trust loss from undisclosed AI use, regulatory or PR fallout.]

[Confidence statement.]

## Product and Services Impact

[3-5 paragraphs. The longest section in most reports. Existing service or product lines, ranked by AI upside, with reasoning. Plausible new offerings the company could realistically launch given current capabilities and customer base. Proprietary data and IP assets visible from the public record, named specifically. The AI moat question in narrative form: what could only this company build that competitors could not replicate by writing a check? Risks: cannibalization, IP leakage through third-party AI tools, undifferentiated features that do not compound.]

### Product Line AI Ranking

[5-column table ranking the company's actual product or service lines.]

[Confidence statement.]

## Strategic Recommendation: Build Before Buy

[3-5 paragraphs. The strategic call. Top 3 capabilities they could build, each anchored to a specific signal from the research. Where buying genuinely makes sense and what to build around it to preserve leverage. The AI moat thesis: a clear sentence on what only this company could build. End with a recommendation on sequencing: which build comes first, and why. This section is the report's payoff. It should be specific enough that the executive could hand it to their leadership team as a starting brief.]

### 24-Month Build-Before-Buy Roadmap

[4-column table sequenced across 0-6, 6-12, and 12-24 month horizons. Each row is a discrete move with Build / Buy / Build + Buy classification.]

## Confidence and Upgrade Path

[1-2 paragraphs. Honest accounting of what is HIGH, MEDIUM, and LOW confidence across the report. Specific list of what additional information would most improve the analysis (typically: revenue mix disclosure, named vendor stack, organizational signals, leadership statements not yet in the public record). Explicit note on what was inferred versus verified. If the public record was thin, say so plainly.]

### Confidence by Section

[Optional 4-column table. Use when the report is long enough that scanning for confidence statements is hard.]

## Sources

[Numbered list of every source actually used. Distinguish primary (the company's own site, leadership statements, filings) from secondary (press, analyst commentary, competitor sites). Include URLs. If Deep Research was used, note it.]
```

---

## Output format

Default to a single markdown report (rendered inline or as an artifact) unless the user requests otherwise.

If the user asks for a Word doc, .docx, "something I can share," or a deliverable for a board or client, use the docx skill and produce a polished Word document. Apply executive-typography defaults: Arial throughout, 11pt body, justified prose, navy or near-black headers, soft-yellow row highlight on the target company in the competitive scorecard, running header with the report title, and "Page X of Y" footer pagination. Make all source URLs live hyperlinks.

If the user asks for a PDF, generate the docx first, then convert.

---

## Gotchas

- Generic AI commentary is a fail. Every paragraph must be anchored to a classifier or a research signal. "AI will change how they work" is not a sentence the report should ever contain.
- Do not invent leadership, financials, or customers. If something is not in the public record, write that it is not, and proceed. Bands beat false precision.
- Do not soft-pedal risk. Risks are not a separate section; they are woven into each domain. Name them concretely.
- The Strategic Recommendation section is mandatory. The report fails if it ends without a build-before-buy thesis and a named AI moat.
- A bare "they should buy a tool" recommendation is not a strategic call. Always name what to build around any purchase.
- B2C and B2B businesses read very differently. Brand and customer relationship analysis shifts hard. Do not apply a generic template across them.
- Regulated industries (HIPAA, FINRA, FERPA, GDPR, SOC2 environments) downstream-affect every domain. Re-check Financial, Workforce, and Brand specifically when regulation is high.
- A company's stated AI strategy is a signal, not a fact. "AI-powered" usually means "we use someone else's API." Treat as MEDIUM confidence at best.
- An AI moat claim needs a specific, verifiable signal (a named dataset, a trademarked methodology, a customer interaction archive). Do not assert a moat the public record does not support.
- If the public record is genuinely thin (fewer than 5 substantive sources), say so in the Confidence section and limit the report's claims accordingly. Do not pad to length.
- Tables should not float. Every table needs a one-line introduction and a follow-on paragraph that names the pattern. A table without surrounding prose is a deck slide, not a report.
- Do not duplicate prose content in tables or vice versa. The table's job is comparison and density; the prose's job is argument and synthesis. They serve different reads of the same content.

## Constraints

- Output is a written report, not a fill-in-the-blank template. Prose for the body of every domain section, with tables supporting where comparison or ranking is the natural read.
- Length target: 4-7 pages (3,000 to 5,500 words). Do not pad to hit length; trim if the analysis is genuinely shorter.
- Every domain section ends with one explicit confidence statement.
- Strategic Recommendation section is mandatory and contains a named AI moat thesis.
- Sources section is mandatory. No assertions without traceability.
- Defer to a loaded voice skill for tone and style. Do not duplicate its rules here.
- If the user has not enabled Deep Research and the analysis would meaningfully benefit, say so once and offer to re-run.
- If the user requests a Word doc, use the docx skill and apply the executive typography defaults specified in Output Format.
