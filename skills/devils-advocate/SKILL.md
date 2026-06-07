---
name: devils-advocate
description: >
  Use when the user says "poke holes in this," "stress test," "before I send this,"
  "challenge this," "what am I missing," or is about to commit a POC scope, recommend
  a tool buy, or ship a client deliverable. Systematically surfaces hidden assumptions,
  counter-arguments, blind spots, biases, and forces a build-not-buy recheck on any
  recommendation that ends in "buy X."
---

# Devil's Advocate

FPOV's R&D recommendations land in front of execs who poke holes fast. This skill stress-tests a POC scope, UCH hypothesis, client recommendation, or "buy this tool" pitch before it ships. Bakes in a build-not-buy recheck because the fastest way to dilute an R&D output is to default to a vendor pick when the team could build instead.

## Context required

- Target: document, plan, argument, recommendation, POC scope, client deck, or decision
- Stakes: internal brainstorm, team decision, client-facing deliverable, or board-level commitment
- Known constraints: budget, timeline, non-negotiables to skip critiquing
- If the target recommends buying a tool: name the vendor explicitly so the build-not-buy recheck has a target

## Steps

1. Read the target fully before critiquing anything.
2. Identify 3-5 hidden assumptions. What must be true for this to work that isn't stated?
3. Construct the strongest counter-arguments. Steel-man the opposition. No strawmen.
4. Find the biggest blind spot: the perspective or scenario completely overlooked.
5. Bias check:
   - Anchoring (over-relying on first framing)
   - Confirmation (seeking only supportive evidence)
   - Sunk cost (continuing because of past investment)
   - Survivorship (looking only at the wins)
   - Optimism (underestimating risk, inflating upside)
6. **Build-not-buy recheck.** If the recommendation ends in "buy X," ask explicitly: what could FPOV build that creates leverage around this buy, or replaces it entirely? If the answer is strong, call it out.
7. Deliver verdict: SOLID / SHAKY / RED FLAG.

## Output

```
# Stress Test: [Title of Target]

## Hidden Assumptions
| # | Assumption | Risk if wrong | Severity |
|---|-----------|---------------|----------|
| 1 |           |               | High/Med/Low |

## Strongest Counter-Arguments
1. [Counter-argument with supporting reasoning]
2. [Counter-argument with supporting reasoning]

## Biggest Blind Spot
[Perspective or scenario completely overlooked]

## Bias Check
- Anchoring: Found / Clear
- Confirmation: Found / Clear
- Sunk Cost: Found / Clear
- Survivorship: Found / Clear
- Optimism: Found / Clear

## Build-not-Buy Recheck
[If recommendation involves buying: what could the team build instead, or build around it? If not applicable, one-line note on why.]

## Verdict: SOLID / SHAKY / RED FLAG
[1-2 sentence justification]

## Recommended Mitigations
1. [Action to address top risk]
2. [Action to address second risk]
3. [Pre-mortem question to ask before proceeding]
```

## Gotchas

- Challenge constructively. Goal is to strengthen the argument, not destroy confidence.
- Prioritize 2-3 critiques that could actually derail. No laundry lists.
- Flag your own model bias. LLMs hedge toward balance. If the argument is genuinely strong, say so.
- Respect non-negotiables. If the operator says the budget is fixed, don't argue the budget.
- Match intensity to stakes. A sandbox brainstorm doesn't need board-level rigor.

## Constraints

- Never soften a RED FLAG to avoid discomfort.
- At least one actionable mitigation per identified risk.
- The build-not-buy recheck is mandatory when the recommendation involves buying a tool, service, or vendor.
- Stay inside the material. Flag speculation as speculative.

## Related skills

- `board-of-executives` — for multi-lens pressure when a single devil's-advocate pass isn't enough
