---
name: skill-reviewer
description: >
  Use when the user says "review this skill," "audit my skill," "check my SKILL.md,"
  "is this skill any good," or drops a path to a SKILL.md file for critique. Audits
  a skill against triggering, structure, and quality checks, then returns a short
  report with pass/fail per check and the top 3 fixes. Reports only, never edits.
---

# Skill Reviewer

A maintenance skill. Point it at any SKILL.md and get back a structured audit. Use it in three scenarios: before committing a new skill, when an existing skill misfires (wrong trigger, no trigger, overlaps another), or as a quarterly drift check across a growing library.

## Context required

- Target: path to the SKILL.md being reviewed, or the raw SKILL.md content pasted in
- Optional: sibling skills (other SKILL.md files in the same library) so the reviewer can flag description overlap and trigger collisions
- Optional: known failure the user is trying to fix (e.g., "this fires on unrelated prompts")

## Steps

1. **Read the target SKILL.md fully.** Frontmatter, body, output template, gotchas, constraints.
2. **Run the 5 Skill Killers audit:**
   - **Trigger clarity** — does the description name specific phrases, not vague intents?
   - **Description fit** — does the description match what the body actually does?
   - **Structural completeness** — does it have Context, Steps, Output, Gotchas, Constraints?
   - **Output template discipline** — is the output template literal (shows exact structure), not just prose?
   - **Scope discipline** — is it one topic, or is it trying to do three skills' work?
3. **Trigger test.** Generate 3 example prompts that should fire this skill and 3 that shouldn't. Judge whether the description would route them correctly.
4. **Collision check** (when sibling skills provided). Flag overlapping trigger phrases or vague descriptions that would cause dispatcher confusion.
5. **Top 3 fixes.** Prioritize the changes that would have the biggest impact, not a laundry list.

## Output

```
# Skill Review: [skill-name]

## 5 Skill Killers
| Check | Pass/Fail | Notes |
|---|---|---|
| Trigger clarity | Pass / Fail | [one line] |
| Description fit | Pass / Fail | [one line] |
| Structural completeness | Pass / Fail | [what's missing] |
| Output template discipline | Pass / Fail | [literal or prose?] |
| Scope discipline | Pass / Fail | [one topic or sprawling?] |

## Trigger Test
**Should fire:**
1. [Example prompt] — [Would fire? Yes/No and why]
2. [Example prompt] — [Would fire? Yes/No and why]
3. [Example prompt] — [Would fire? Yes/No and why]

**Should NOT fire:**
1. [Example prompt] — [Would it fire incorrectly? Yes/No and why]
2. [Example prompt] — [Would it fire incorrectly? Yes/No and why]
3. [Example prompt] — [Would it fire incorrectly? Yes/No and why]

## Collision Check
[If sibling skills provided: list any overlap. Otherwise: "Not run — no sibling skills provided."]

## Top 3 Fixes
1. **[Fix title]** — [Specific change: what to rewrite, add, or remove]
2. **[Fix title]** — [Specific change]
3. **[Fix title]** — [Specific change]

## Verdict: READY / NEEDS WORK / REBUILD
[1-2 sentence justification]
```

## Gotchas

- Audit the description first. If the description is broken, nothing else matters because the skill won't fire.
- Don't confuse "well-written" with "effective." A beautifully structured skill with a vague description is broken.
- Scope creep is the most common killer. If the body has three output templates, the skill is three skills.
- The trigger test is the real signal. If 3-of-3 "should fire" prompts wouldn't actually fire, the description needs a rewrite, not a polish.
- Don't edit the file. This skill reports, it doesn't fix.

## Constraints

- Every Skill Killer check gets an explicit Pass or Fail. No "Partial" or "Depends."
- Trigger test must include both directions: 3 should-fire and 3 shouldn't-fire examples.
- Top 3 Fixes are ordered by impact, not severity.
- Verdict is mandatory. No fence-sitting.
- Never modify the target SKILL.md. Output only.

## Related skills

- `devils-advocate` — when the fix list is large and you want to pressure-test whether the skill should exist at all before rewriting
