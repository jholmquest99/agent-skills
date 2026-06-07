---
name: research
description: >
  Use when the user says "research [topic]," "deep dive," "verify this," "fact-check,"
  "before we recommend a buy," or "before we commit build hours." Runs multi-angle
  research with explicit confidence tiers (HIGH/MEDIUM/LOW) and cross-source verification
  to separate real signal from vendor-echo. Forces a build-not-buy framing on any tool
  or capability research.
---

# Research

Separates real signal from vendors repeating each other so FPOV's recommendations hold up under client scrutiny. Forces a build-not-buy framing on any research that touches a tool or vendor, because the default trap is collapsing "what's out there" into "what should we buy."

## Context required

- Topic: what's being researched
- Purpose: capability validation, vendor evaluation, market trend check, client discovery prep, fact-check
- Horizon: how current does the information need to be
- Stakes: exploratory vs client-facing deliverable
- If researching a tool or vendor: name it explicitly so the build-not-buy section has a target

## Steps

1. Decompose the topic into 3-5 distinct research angles (e.g., capability, market adoption, buyer perspective, technical feasibility, risk).
2. Run sources in parallel per angle.
3. Assign a confidence tier to each key finding:
   - **HIGH** — multiple independent sources, primary documentation, direct evidence
   - **MEDIUM** — secondary sources, agreement across non-independent sources, indirect evidence
   - **LOW** — single source, speculation, vendor marketing, recycled content
4. Cross-source verification. Flag echo-chamber effects: if 10 "sources" trace back to one vendor blog or one LinkedIn thought piece, that's LOW confidence, not HIGH.
5. Find dissenting views. If nothing dissents, that itself is a signal worth naming.
6. **Build-not-buy framing.** If the topic is a tool, vendor, or bought capability: include an explicit "What could FPOV build instead or build around this" section. If the research is not about buying, note why the section doesn't apply.
7. Name the gaps: what couldn't be verified, what's unknown, what would need more time.

## Output

```
# Research: [Topic]

## Executive Summary
[3-5 sentence answer to the actual question being asked]

## Key Findings
| # | Finding | Confidence | Sources |
|---|---|---|---|
| 1 | [Finding] | HIGH / MED / LOW | [Source names or links] |

## Dissenting Views
[Counter-narratives or contrarian takes found in sources. If none, say so and flag it as a potential echo-chamber signal.]

## Source Quality
| Source | Type | Independence | Notes |
|---|---|---|---|
| [Source] | Primary / Secondary / Vendor / Analyst | Yes / No | [If secondary: what primary does it cite] |

## Build-not-Buy Framing
[When applicable: what could FPOV build instead, or build around, this tool/vendor/capability?]
[If not applicable: one-line note on why.]

## Gaps and Unknowns
1. [What couldn't be verified and why]
2. [What would need more time or different access]
```

## Gotchas

- Echo-chamber detection matters more than source count. Five blog posts citing one vendor deck is one source, not five.
- Vendor marketing is LOW confidence by default, regardless of how authoritative it sounds.
- Recycled dates. Watch for "2024 trends" articles republished in 2026 with new dates.
- If you can't find dissent, that's data. Name it.
- Primary sources beat analyst summaries beat vendor blogs beat LinkedIn posts. Rank accordingly.

## Constraints

- Every key finding must carry a confidence tier.
- Source Quality table is mandatory. No assertions without sourcing.
- Build-not-Buy Framing is mandatory when the topic involves a tool, vendor, or bought capability.
- LOW findings can appear in the output but must be labeled so operators don't mistake them for signal.
- If the research can't reach HIGH confidence on the question asked, say so clearly in the Executive Summary.

## Related skills

- `devils-advocate` — pressure-test the recommendation that comes out of the research
