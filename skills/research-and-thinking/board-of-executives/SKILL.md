---
name: board-of-executives
description: >
  Use when the user says "what would my board say," "pressure-test from the top,"
  "multiple exec perspectives," "what would [role] think," or needs a 360 review of
  a POC scope, capability idea, client recommendation, or strategic call. Simulates
  FPOV-relevant elite exec archetypes, activates only the relevant ones (minimum 3),
  and forces explicit conflict detection between them so the hardest decision surfaces
  instead of getting papered over in synthesis.
---

# Board of Executives

Simulates elite exec archetypes that matter at FPOV's scale (9-person boutique consulting firm, owner-operated, IP-driven). Not all advisors activate every time. The skill scores relevance first, runs only the voices that apply, and builds an explicit conflict map so the real decision isn't buried.

## Context required

- Target: plan, POC scope, capability brief, client recommendation, or decision
- Stakes: internal exploration, team commitment, or client-facing commit
- Optional: one custom advisor override (e.g., a named client persona for pitch rehearsal)

## Advisor archetypes

### The Futurist
- **Modeled on:** Scott Klososky (FPOV founder)
- **Lens:** Practical-applied futurism, human-technology symbiosis, digital maturity curve, high-beams vs low-beams
- **Bias:** Overweights horizon implications; may push positioning that feels premature to quarter-focused operators
- **Asks:** "What happens to this capability when AI doubles again?" / "Are we building for today's org or the one that's coming?" / "High-beams or low-beams?"

### The Revenue Operator
- **Modeled on:** Hormozi corporate-CRO composite
- **Lens:** Unit economics, pipeline velocity, offer construction
- **Bias:** Kills anything not tied to a deal in 90 days; misses long-cycle IP plays
- **Asks:** "What's the payback? Does this close a deal?" / "If I can't sell it, why are we building it?"

### The Systems Operator
- **Modeled on:** Leila Hormozi / elite COO composite
- **Lens:** Process rigor, role clarity, scaling people without breaking them
- **Bias:** Over-engineers rollout; process-heavy on small experiments
- **Asks:** "Who owns this? What's the SOP?" / "What breaks at 10x volume?"

### The Financial Strategist
- **Modeled on:** Karlton Dennis corporate-advisor composite
- **Lens:** Owner-operator cashflow, tax efficiency, keep-more-of-what-you-make
- **Bias:** Frames everything through cash and deductibility; short-term-cash biased
- **Asks:** "Billable or R&D-credit eligible?" / "Cash impact this quarter?" / "Recurring or one-time?"

### The Battle-Tested CEO
- **Modeled on:** Dimon-style enterprise operator
- **Lens:** Skeptical buyer lens, wants proof not promise
- **Bias:** Burden of proof on change; misses real innovation in favor of proven plays
- **Asks:** "I've seen this pitch. What's different?" / "Show me the proof, not the deck." / "What's the failure case?"

## Steps

1. **Score relevance.** For each advisor, rate 1-5 how much their lens applies to the input.
2. **Activate advisors.** Pull in every advisor scoring 3+. If fewer than 3 score 3+, activate the 3 highest-scoring regardless.
3. **Run each activated advisor independently.** Stay in character. Embody the bias, don't hedge toward balance.
4. **Each advisor gives a clear verdict** (Support / Concern / Oppose) with 2-3 sentences of bias-driven reasoning.
5. **Build the conflict map.** For every pair of activated advisors, identify any dimension they split on. Not all pairs need to conflict, but every real split must be named.
6. **Pick the decision-critical conflict.** The one split that must be resolved before proceeding.
7. **Synthesize.** Propose a recommended action that navigates the decision-critical conflict, not one that papers over it.
8. **Consensus check.** If all activated advisors agree, flag it as suspicious and run a devil's-advocate override on the synthesis.

## Output

```
# Board Review: [Title]

## Activation
| Advisor | Relevance | Status | Why |
|---|---|---|---|
| Futurist | 5/5 | Active | [One-line reason] |
| Revenue Operator | 2/5 | Skipped | [One-line reason] |
| Systems Operator | 4/5 | Active | [One-line reason] |
| Financial Strategist | 3/5 | Active | [One-line reason] |
| Battle-Tested CEO | 4/5 | Active | [One-line reason] |

## Active Advisor Verdicts

### The Futurist
**Verdict:** Support / Concern / Oppose
[2-3 sentences in character]

[Repeat for each active advisor]

## Conflict Map
| # | Advisor A | Advisor B | Split on | Forces the call on |
|---|---|---|---|---|
| 1 | Futurist | Financial Strategist | Horizon vs cash | Fund this quarter or park it |
| 2 | Systems Operator | Battle-Tested CEO | Process vs proof | Build SOP first or ship to a reference client |

## Decision-Critical Conflict
[The single conflict that must be resolved before proceeding, and why it's the one that matters.]

## Recommended Action
[Synthesis that navigates the decision-critical conflict. Does not paper over the tension.]

## Consensus Check
[If all advisors aligned: flag it and name what a skeptic would push back on. Otherwise omit.]
```

## Gotchas

- Make advisors genuinely disagree. If the Revenue Operator and the Futurist are saying the same thing, you're not in character.
- Activation matters. Don't pull in advisors who don't have a stake; their voices dilute the real ones.
- Stay in character including the bias. The Revenue Operator should genuinely dismiss unmonetizable capability plays. The Battle-Tested CEO should genuinely demand proof.
- The decision-critical conflict must be a real fork in the road. If it's a nuance, go back and find the real one.
- Custom advisor slot is one per run. Don't dilute the board with too many voices.

## Constraints

- Minimum 3 activated advisors per run.
- Every activated advisor must give a clear verdict (Support / Concern / Oppose). No fence-sitting.
- The Conflict Map must include at least one real split when 3+ advisors are active. If none exist, the run is suspicious and should be re-run with harder critique.
- The Decision-Critical Conflict is mandatory and must name both advisors and the dimension.
- The Recommended Action cannot be "do more research" unless the Conflict Map explicitly identifies an information gap.

## Related skills

- `devils-advocate` — single-lens pressure test when a full board is overkill
