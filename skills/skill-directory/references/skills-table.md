# FPOV Skill Inventory

The authoritative table of every skill in the FPOV library. Source of truth for routing decisions made by `skill-directory`.

**Last updated:** April 21, 2026
**Total skills:** 12

---

## How to Read This Table

- **Skill** — exact folder/frontmatter name
- **Category** — voice-content / thinking / cleanup / meta
- **Scope** — one sentence of what it actually does
- **Fires on (triggers)** — phrases and request patterns that should activate it
- **Does NOT handle** — explicit scope boundaries, to prevent over-triggering
- **Chains with** — skills commonly run before or after this one

---

## Voice & Content Skills

### fpov-voice
| Field | Value |
|---|---|
| **Category** | voice-content (MASTER) |
| **Scope** | Master FPOV voice/tone/messaging system. Owns voice rules (confident, visionary, human), tone rules (urgent, empowering, grounded), messaging pillars, signature hooks, and writing rules (no em dashes, no emojis, no fear-based framing). Single source of truth for how FPOV sounds. |
| **Fires on** | "write this in FPOV voice," "make this sound like FPOV," "brand voice check," "rewrite for the website," "draft in our voice," ad-hoc external copy that doesn't fit a specialist format |
| **Does NOT handle** | Blog post shape (→ fpov-blog-voice), newsletter structure (→ idea-stream-newsletter), Update page structure (→ update-page-copywriter), LinkedIn/multi-format output (→ fpov-content-ideation), AI-pattern cleanup (→ humanizer) |
| **Chains with** | → humanizer (final AI-pattern cleanup after voice application) |

### fpov-blog-voice
| Field | Value |
|---|---|
| **Category** | voice-content (specialist) |
| **Scope** | Transforms raw input (teaser, bullets, notes) into a full 800–1,200 word FPOV blog post. Owns blog-post SHAPE — one continuous argument, invisible structure, opening reframe to closing punch. Applies fpov-voice rules internally. |
| **Fires on** | "write this as a blog," "turn this into a post," "expand into a blog," "full blog post about X," "make this flow better" as long-form |
| **Does NOT handle** | Short-form LinkedIn posts, newsletter sections, Update page copy, non-FPOV blog work |
| **Chains with** | ← fpov-content-ideation (if user requested Big Idea first, expand to full blog). → humanizer (optional final cleanup) |

### idea-stream-newsletter
| Field | Value |
|---|---|
| **Category** | voice-content (specialist) |
| **Scope** | Drafts the monthly FPOV "Idea Stream" newsletter email. 80%-complete first draft, full skeleton (Opening Block, Big Idea, Water Cooler, FPOV HQ, Monthly Highlight, reminders). 5-minute target read. Applies fpov-voice rules internally. |
| **Fires on** | "draft the newsletter," "write this month's Idea Stream," "Idea Stream draft," "monthly email for FPOV," user provides sections in "Big Idea + Water Cooler + FPOV HQ + Monthly Highlight" format |
| **Does NOT handle** | Standalone Big Idea teasers (→ fpov-content-ideation), standalone Water Cooler blurbs (→ fpov-content-ideation), full blog post expansion (→ fpov-blog-voice) |
| **Chains with** | ↔ fpov-blog-voice (newsletter Big Idea often links to a full blog post). → humanizer (optional final cleanup) |

### update-page-copywriter
| Field | Value |
|---|---|
| **Category** | voice-content (specialist) |
| **Scope** | Produces full FPOV Update page copy for upcoming webinar/event — headline, presenter line, opening provocation, session invitation, 4-bullet section, CTA. Applies fpov-voice rules internally. |
| **Fires on** | "write the Update page," "write the webinar description," "FPOV Update copy for [speaker]," "event page for the next Update," "Update landing page" |
| **Does NOT handle** | LinkedIn event promo (→ fpov-content-ideation), newsletter FPOV Update reminder block (→ idea-stream-newsletter), post-event recap content |
| **Chains with** | → fpov-content-ideation (Update page + LinkedIn amplification posts). → humanizer (optional final cleanup) |

### fpov-content-ideation
| Field | Value |
|---|---|
| **Category** | voice-content (specialist) |
| **Scope** | Generates FPOV LinkedIn posts, short-form teasers, Water Cooler blurbs, and quick multi-format combos from a set topic. The topic stays active for the whole conversation. Applies fpov-voice rules internally. |
| **Fires on** | "topic this month is X," "give me 10 LinkedIn posts," "repurpose this into social," "give me 5 LinkedIn posts and a Big Idea teaser," "Water Cooler blurb" |
| **Does NOT handle** | Full blog posts (→ fpov-blog-voice), full monthly newsletter (→ idea-stream-newsletter), Update page copy (→ update-page-copywriter) |
| **Chains with** | ↔ fpov-blog-voice (Big Idea teaser → full blog post). → humanizer (optional final cleanup) |

---

## Cleanup Skill

### humanizer
| Field | Value |
|---|---|
| **Category** | cleanup |
| **Scope** | General-purpose AI-pattern cleanup. Removes inflated symbolism, promotional language, superficial -ing analyses, vague attributions, em dash overuse, rule of three, AI vocabulary words, negative parallelisms, excessive conjunctive phrases. Brand-agnostic — does not enforce FPOV or any specific voice. |
| **Fires on** | "humanize this," "make this sound less AI," "this sounds robotic," "clean up the AI voice," "de-AI this," user pastes draft and asks for rewrite |
| **Does NOT handle** | Applying FPOV voice (→ fpov-voice), writing content from scratch, brand-specific voice rules |
| **Chains with** | ← any voice-content specialist (optional final cleanup pass). ← fpov-voice (voice application first, then cleanup) |

---

## Thinking & Strategy Skills

### research
| Field | Value |
|---|---|
| **Category** | thinking |
| **Scope** | Multi-angle research with confidence tiers (HIGH/MEDIUM/LOW), cross-source verification to separate real signal from vendor echo-chamber. Forces build-not-buy framing on any tool or vendor research. |
| **Fires on** | "research [topic]," "deep dive on X," "verify this," "fact-check," "before we commit build hours," "before we recommend a buy" (when the user needs to UNDERSTAND the landscape) |
| **Does NOT handle** | Pressure-testing a recommendation that already exists (→ devils-advocate), multi-exec perspective review (→ board-of-executives) |
| **Chains with** | → devils-advocate (pressure-test the recommendation that comes out of research). → board-of-executives (multi-lens review of the research output) |

### devils-advocate
| Field | Value |
|---|---|
| **Category** | thinking |
| **Scope** | Single-lens stress test of a POC scope, UCH hypothesis, client recommendation, or "buy this tool" pitch. Surfaces hidden assumptions, counter-arguments, blind spots, biases. Bakes in build-not-buy recheck. |
| **Fires on** | "poke holes in this," "stress test," "before I send this," "challenge this," "what am I missing," about to commit a POC scope or client deliverable |
| **Does NOT handle** | Multi-perspective review (→ board-of-executives), initial research to understand a topic (→ research) |
| **Chains with** | ← research (pressure-test research findings). → board-of-executives (if single-lens isn't enough) |

### board-of-executives
| Field | Value |
|---|---|
| **Category** | thinking |
| **Scope** | Multi-lens review simulating FPOV-relevant exec archetypes (Futurist, Revenue Operator, Systems Operator, Financial Strategist, Battle-Tested CEO). Scores relevance, activates ≥3, forces explicit conflict detection so the hardest decision surfaces. |
| **Fires on** | "what would my board say," "pressure-test from the top," "multiple exec perspectives," "what would [role] think," 360 review of POC/capability/client recommendation |
| **Does NOT handle** | Single-lens quick critique (→ devils-advocate), initial research (→ research) |
| **Chains with** | ← research. ← devils-advocate (when single-lens wasn't enough) |

---

## Meta Skills

### skill-directory
| Field | Value |
|---|---|
| **Category** | meta |
| **Scope** | The master router and overlap guard. Routes ambiguous requests to the right skill, resolves known collisions, prevents double-firing. Does NOT produce end-user content. |
| **Fires on** | Ambiguous requests, multi-skill requests, "what skills do I have," "which skill should I use," "show me the skill inventory" |
| **Does NOT handle** | Actually doing the routed work (routes and hands off), recursing into itself |
| **Chains with** | → any skill in the library |

### skill-reviewer
| Field | Value |
|---|---|
| **Category** | meta |
| **Scope** | Audits a SKILL.md file against 5 Skill Killer checks (trigger clarity, description fit, structural completeness, output template discipline, scope discipline). Produces a report with top 3 fixes. Reports only, never edits. |
| **Fires on** | "review this skill," "audit my skill," "check my SKILL.md," "is this skill any good," user drops a SKILL.md path for critique |
| **Does NOT handle** | Building a new skill (→ skillsmd-interview-and-build), editing/fixing a skill (report only) |
| **Chains with** | ← skillsmd-interview-and-build (audit a newly-built skill before shipping) |

### skillsmd-interview-and-build
| Field | Value |
|---|---|
| **Category** | meta |
| **Scope** | Structured 9-question interview with capped branches to extract everything needed to build a new skill. Ends with readback, confirmation, name, handoff to skill-creator for the actual build, and MANDATORY Phase 4 registration in this directory (adds row to skills-table.md, adds collision rules if needed). |
| **Fires on** | "help me make a skill," "I want to build a skill for X," "interview me about a skill," "create a new skill" |
| **Does NOT handle** | Auditing an existing skill (→ skill-reviewer), routing between existing skills (→ skill-directory) |
| **Chains with** | → skill-creator (at /mnt/skills/examples/skill-creator/ — produces the actual files). → skill-directory (Phase 4 registration, MANDATORY). → skill-reviewer (optional audit before shipping) |

---

## Maintenance Notes

The skill directory is only useful if it stays current. Three rules keep it from drifting:

### 1. New skills must be registered by `skillsmd-interview-and-build`

When a new skill is built via the interview-and-build flow, Phase 4 of that skill is **mandatory** — it adds the new skill's row to this table and, if needed, adds a Collision Resolution Rule to the directory's SKILL.md. A new skill that exists on disk but is not in this table is invisible to the router.

If a skill is ever added outside the interview flow (hand-authored, pasted from somewhere), the operator is responsible for manually running the same Phase 4 steps — add the row here, check for collisions, update "Last updated" and "Total skills."

### 2. Edited skills require a same-day table update

When any skill's description, trigger phrases, or scope changes materially, the matching row in this table must be updated the same day. Run `skill-reviewer` against the edited skill first, then reflect the changes here.

### 3. Removed skills require same-day row deletion

When a skill is deleted from `/mnt/skills/user/`, delete its row here. Also scan the directory's Collision Resolution Rules for references to the removed skill and delete or rewrite those rules. A collision rule that routes to a skill that no longer exists is worse than no rule.

### Checklist for any skill change

- [ ] Row added/edited/deleted in this table
- [ ] Collision Resolution Rules in `SKILL.md` checked for impact
- [ ] Chain Rules in `SKILL.md` checked for impact
- [ ] "Last updated" date refreshed at top of this file
- [ ] "Total skills" count refreshed at top of this file
- [ ] `skill-reviewer` run on the new or edited skill
