---
name: skill-directory
description: The master router and overlap guard for the FPOV skill library. Use this skill whenever a request is ambiguous, could match multiple skills, or contains multi-skill signals (e.g., 'write a blog and make it sound like FPOV,' 'research this tool then stress-test it,' 'draft the newsletter with Water Cooler and Big Idea'). Also trigger when the user asks 'what skills do I have,' 'which skill should I use,' 'show me the skill inventory,' or 'what can you do.' DO NOT fire when the request clearly maps to exactly one skill (e.g., 'humanize this draft' → go straight to humanizer). This skill routes, disambiguates, and prevents double-firing — it does not produce end-user content itself.
---

# Skill Directory

This is the master router for the FPOV skill library. It does three things: (1) routes ambiguous requests to the right skill, (2) resolves known collisions between skills that could both fire on the same trigger, and (3) prevents double-firing by enforcing which skill owns what.

**The full skill inventory lives in `references/skills-table.md`** — that's the authoritative table of every skill, its scope, its trigger phrases, what it doesn't handle, and which skills it chains with. Read that file before making any routing decision.

---

## When to Use This Skill

**Fire this skill when:**
- The request could plausibly match two or more skills (e.g., "write a blog post" matches both `fpov-blog-voice` and `fpov-content-ideation`)
- The request contains multiple verbs or steps that span skills ("research this vendor then poke holes in the recommendation")
- The user asks what skills exist or which one to use
- A specialist skill is about to fire on a draft that's already passed through another specialist (double-fire risk)

**Do NOT fire this skill when:**
- The request maps cleanly to exactly one skill with no ambiguity (e.g., "humanize this," "audit my SKILL.md," "what would my board say about this plan")
- The user is clearly inside an active skill already (e.g., mid-way through a `skillsmd-interview-and-build` interview)

---

## How Routing Works

1. **Read the request.** Identify the verbs, artifacts, and output expectations.
2. **Consult `references/skills-table.md`.** Find every skill whose trigger phrases or scope could match.
3. **If only one skill matches → route there.** No directory needed.
4. **If multiple skills match → apply the Collision Resolution Rules below.**
5. **If no skill matches → say so plainly.** Don't force-fit. Suggest either creating a new skill (route to `skillsmd-interview-and-build`) or handling the request without a skill.
6. **Name the skill you're routing to.** Tell the user: "Routing to `[skill-name]` because [one-line reason]." This keeps routing visible and correctable.

---

## Collision Resolution Rules

These are the known overlap cases in the current library. When a request hits any of these patterns, follow the rule — don't re-litigate.

### Collision A — Blog post request
**Matches:** `fpov-blog-voice`, `fpov-content-ideation`, `fpov-voice`
**Rule:** Full blog post (800–1,200 words, long-form) → **`fpov-blog-voice`**. Short-form content including LinkedIn posts, teasers, or multi-format combos → **`fpov-content-ideation`**. Ad-hoc voice-only rewrite (not a blog-shape deliverable) → **`fpov-voice`**.

### Collision B — Newsletter content
**Matches:** `idea-stream-newsletter`, `fpov-content-ideation`
**Rule:** Full monthly newsletter (with Big Idea + Water Cooler + FPOV HQ + Monthly Highlight) → **`idea-stream-newsletter`**. Standalone Big Idea teaser or Water Cooler blurb outside the full newsletter context → **`fpov-content-ideation`**.

### Collision C — "Before we recommend a buy" / tool evaluation
**Matches:** `research`, `devils-advocate`
**Rule:** If the user wants to *understand* the tool or landscape → **`research`**. If the user already has a buy recommendation and wants to *pressure-test* it → **`devils-advocate`**. Chain both when the task is "research then stress-test."

### Collision D — Stress testing
**Matches:** `devils-advocate`, `board-of-executives`
**Rule:** Single-lens critique or quick pressure-test → **`devils-advocate`**. Multi-perspective review requiring different exec lenses (futurist, operator, CFO) → **`board-of-executives`**. If the user says "poke holes" → devils-advocate. If the user says "what would [role/persona] think" or "multiple perspectives" → board-of-executives.

### Collision E — FPOV voice application
**Matches:** `fpov-voice`, `fpov-blog-voice`, `idea-stream-newsletter`, `update-page-copywriter`, `fpov-content-ideation`
**Rule:** **`fpov-voice`** is the master voice skill. Specialist skills (blog-voice, newsletter, update-page, content-ideation) apply `fpov-voice` rules *internally*. **Never fire `fpov-voice` on top of a specialist's output** — that's double-processing. Fire `fpov-voice` directly only when the request doesn't fit a specialist format (e.g., "rewrite this homepage copy in FPOV voice").

### Collision F — AI-pattern cleanup vs. voice
**Matches:** `humanizer`, `fpov-voice`
**Rule:** **`humanizer`** is general AI-pattern cleanup — no brand voice opinions. **`fpov-voice`** applies FPOV's specific voice. For FPOV content: run the specialist skill (which includes fpov-voice), then optionally pass through `humanizer` for final AI-pattern cleanup. For non-FPOV content: `humanizer` alone. For FPOV voice on ad-hoc copy: `fpov-voice` then `humanizer`.

### Collision G — Skill meta-work
**Matches:** `skill-reviewer`, `skillsmd-interview-and-build`, `skill-directory`
**Rule:** Build a new skill → **`skillsmd-interview-and-build`**. Audit an existing skill → **`skill-reviewer`**. Route between skills or ask "what skills exist" → **`skill-directory`** (this one).

---

## Chain Rules (Which Skills Run Together)

Some tasks naturally call for two skills in sequence. When the user's request implies a chain, route through each in order and tell them what's happening.

- **Research → Devil's Advocate** — "research this tool then pressure-test the recommendation"
- **Research → Board of Executives** — "research this then give me the board's view"
- **Any FPOV specialist → Humanizer** — specialist produces the draft in-voice; humanizer does the final AI-pattern scrub
- **fpov-voice → Humanizer** — ad-hoc FPOV voice rewrite with final cleanup
- **skillsmd-interview-and-build → skill-creator → skill-directory (Phase 4)** — build a new skill, then automatically register it in this directory so the router knows it exists. This chain is enforced, not optional.
- **skillsmd-interview-and-build → skill-reviewer** — build a new skill, then audit it before shipping

---

## Double-Fire Prevention

The most common failure mode is two skills processing the same content when only one should. Rules to prevent this:

1. **Specialist owns voice.** When a request routes to `fpov-blog-voice`, `idea-stream-newsletter`, `update-page-copywriter`, or `fpov-content-ideation`, that skill applies `fpov-voice` rules internally. Do not fire `fpov-voice` separately on the output.

2. **Humanizer is opt-in, never automatic.** Specialists produce in-voice drafts. `humanizer` only runs if the user explicitly asks or if a draft is visibly AI-shaped after voice application.

3. **Thinking skills don't chain to themselves.** If `devils-advocate` just ran, don't immediately run `board-of-executives` on the same output unless the user explicitly asks. Redundant pressure-testing is noise.

4. **Skill-directory doesn't route to skill-directory.** If this skill fires, it routes *out* — it never recurses.

---

## Keeping the Directory Current

The directory is only useful if the inventory is accurate. Two contracts keep it from drifting:

### New skills are registered by `skillsmd-interview-and-build` (Phase 4)

When a new skill is built via the interview-and-build flow, that skill's Phase 4 is **required** to:
1. Add the new skill's row to `references/skills-table.md`
2. Check for new collisions with existing skills
3. If a collision exists, add a Collision Resolution Rule to this SKILL.md's "Collision Resolution Rules" section
4. Update the "Last updated" and "Total skills" fields at the top of the table

A new skill that isn't registered is invisible to the router. The build is not complete until registration is done.

### Edited or removed skills require manual updates

When a skill's description, triggers, or scope changes — or when a skill is deleted — the operator must update `references/skills-table.md` the same day and scan this SKILL.md's Collision Resolution Rules for references to the changed or removed skill. A stale rule (routing to a skill that no longer exists, or using old trigger phrases) breaks routing silently.

The full maintenance checklist lives in `references/skills-table.md`.

---

## Output

When this skill fires on an ambiguous request, produce exactly this:

```
# Routing Decision

**Request:** [One-line restatement of what the user asked for]

**Candidate skills:** [List of skills that matched, with one-line scope each]

**Routing to:** `[skill-name]`

**Why:** [One sentence citing the Collision Rule or the scope match]

**Chain:** [If multi-step, list the skills in order: skill-1 → skill-2. Otherwise: "Single skill."]
```

When the user asks "what skills do I have" or "which skill should I use for X":
- Read `references/skills-table.md`
- Answer directly with the relevant skill(s) and trigger phrases
- Do not produce the routing decision template unless they're committing to a task

---

## Gotchas

- **The directory is not the doer.** This skill routes. Once routed, the target skill takes over. Don't try to do the work inside this skill.
- **Stale inventory breaks routing.** When any skill is added, removed, or has its description changed, `references/skills-table.md` must be updated the same day. A directory with stale entries is worse than no directory.
- **Unknown requests are fine.** If no skill fits, say so. Force-fitting a request to a wrong skill is worse than handling it without one.
- **Respect the user's override.** If the user says "use fpov-blog-voice for this," route there even if the directory would have chosen differently. Then flag the override so the directory rules can be improved.
- **Don't narrate the routing process in depth.** Users want the answer, not a play-by-play. Keep routing statements to one or two lines.

---

## Constraints

- The skill-directory never produces end-user content (blog posts, newsletters, research, critiques). It only routes.
- Every routing decision must name the target skill explicitly, in backticks, so it's visible to both Claude and the user.
- When `references/skills-table.md` disagrees with this SKILL.md, the table wins — it's the single source of truth for what's in the library right now.
- Collision Resolution Rules are authoritative. If a rule says "blog post → fpov-blog-voice," do not override based on tone or preference.
- If a chain is required, announce it up front: "This needs [skill-1] then [skill-2]. Starting with [skill-1]."

---

## Related skills

- `skillsmd-interview-and-build` — when the request clearly needs a skill that doesn't exist yet
- `skill-reviewer` — when the user says a skill is misfiring and this directory alone can't fix it
