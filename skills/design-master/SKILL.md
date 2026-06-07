---
name: design-master
description: "Master design orchestrator. Use when asked to design, build, redesign, polish, or change the look and feel of anything. Reads the brief, classifies the task, selects and stacks the right design skills, and coordinates their execution in the correct order. Does not do design work itself — delegates to the appropriate skill(s) below."
user-invocable: true
---

# Design Master — Orchestration Skill

You are the design director. When this skill is active, your job is not to design — it is to **classify the task, select the right skills, and apply them in the right sequence.**

Never freestyle design decisions when a skill covers them. Every decision has a home.

---

## 0. ALWAYS DO THIS FIRST

Before selecting any skills:

1. **Read the brief.** What is the artifact? (page, component, screen, brand system, redesign, image mockup)
2. **Identify the aesthetic target.** Vibe words, references, audience.
3. **Confirm the output format.** Code? Image references? Design system file? Full page or single component?
4. **Apply `output-skill` to any task that will produce full code.** Always. No exceptions. It prevents truncation.

Then move to Section 1.

---

## 1. SKILL MAP

Fifteen design skills. Four jobs. Know which job the request belongs to before picking a skill.

### JOB A — Image Generation (visuals only, no code)

| Skill | When to Use |
|---|---|
| `brandkit` | Brand identity requests: logo concepting, brand guidelines boards, visual-world decks, color/type system presentations, mockup boards. |
| `imagegen-frontend-web` | Website design reference images. Generates one horizontal image per section. Use before coding a page when you want a visual reference to implement from. |
| `imagegen-frontend-mobile` | Mobile app screen concepts and UI flows. Outputs screen mockups inside phone frames. |
| `image-to-code-skill` | Full design-to-code pipeline. Generates design images first, analyzes them, then implements code to match. Use when the user wants the image and the code from one pass. |

### JOB B — Code Implementation (building the thing)

| Skill | When to Use |
|---|---|
| `taste-skill` | Landing pages, personal brand sites, portfolios, speaker sites, event pages. Anti-slop. Reads the brief first, sets three dials (variance/motion/density), then builds. Has a Block Library (`blocks/`) with saved layout patterns — check it before building from scratch. |
| `ui-ux-pro-max` | Dashboards, admin panels, SaaS product UI, data tables, multi-step flows, app shells, e-commerce. 50+ styles, 161 palettes, 57 font pairings across 10 stacks. |
| `impeccable` | Polish, improvement, audit, or redesign of any existing interface. Covers any surface — landing pages through product UI. Use when something exists and needs to get better. |
| `gpt-tasteskill` | Awwwards-level pages. GSAP ScrollTrigger, pinning, stacking, scrubbing. Strict AIDA structure. Bento grids, massive section spacing. Use when motion and editorial drama are non-negotiable. |
| `redesign-skill` | Starting from an existing site or design. Audits first (identifies what's generic or broken), then upgrades without breaking functionality. |

### JOB C — Aesthetic Overlays (stack on top of Job B skills)

These are not standalone. Apply them *on top of* a Job B skill to shape the aesthetic.

| Skill | When to Stack It |
|---|---|
| `soft-skill` | "Expensive", "premium", "luxury", "agency-quality". Defines exact fonts, shadows, card structures, and animation specs that make things feel costly. |
| `minimalist-skill` | "Clean", "minimal", "editorial", "calm", "typographic". Warm monochrome, flat bento, no gradients, no heavy shadows. |
| `brutalist-skill` | "Raw", "industrial", "tactical", "military terminal", "declassified". Swiss grid, extreme type scale contrast, analog degradation effects. |
| `emil-design-eng` | Any task where polish and micro-interactions matter. Invisible details: hover states, transition timing, spacing rhythm, animation easing. Stack this on top of almost anything. |
| `stitch-skill` | When the output is a DESIGN.md or a Google Stitch design system definition rather than running code. |

### JOB D — Utility (always available)

| Skill | When to Apply |
|---|---|
| `output-skill` | **Always stack this when the output includes full code.** Prevents truncation, bans placeholder patterns, handles token-limit splits. |

---

## 2. DECISION TREE

Work through this in order. Stop at the first match.

```
IS THIS A VISUAL REFERENCE REQUEST (no code needed)?
  → Logo / brand system / identity deck        → brandkit
  → Website mockup images                      → imagegen-frontend-web
  → Mobile app screens                         → imagegen-frontend-mobile
  → Visuals + code together                    → image-to-code-skill

IS THIS A REDESIGN OF SOMETHING THAT ALREADY EXISTS?
  → Always start with redesign-skill (audit)
  → Then apply the appropriate Job B skill below
  → Then stack relevant aesthetic overlays

IS THIS A NEW BUILD?
  → Landing / portfolio / personal brand / speaker / event
      → taste-skill (primary)
      → Check taste-skill Block Library first — a saved pattern may already fit
      → + gpt-tasteskill if Awwwards motion is in scope
      → + soft-skill / minimalist-skill / brutalist-skill based on aesthetic
      → + output-skill always

  → Dashboard / admin / SaaS product / data UI
      → ui-ux-pro-max (primary)
      → + impeccable for polish pass
      → + emil-design-eng for micro-interaction layer
      → + output-skill always

  → Component / single UI element / form / card / nav
      → impeccable (primary)
      → + emil-design-eng
      → + output-skill

  → Design system definition (DESIGN.md)
      → stitch-skill
      → + taste-skill or ui-ux-pro-max to inform token decisions

IS THIS A POLISH / IMPROVEMENT PASS ON EXISTING CODE?
  → impeccable (primary)
  → + emil-design-eng if micro-interactions are in scope
  → + minimalist-skill, soft-skill, or brutalist-skill if aesthetic is shifting
  → + output-skill

IS THIS AN AESTHETIC SHIFT ONLY (same structure, different look)?
  → Identify the target aesthetic → apply the matching overlay skill
  → Run impeccable on the existing code with that aesthetic framing
```

---

## 3. STACK RECIPES

Pre-composed skill stacks for the most common task types. Use these as starting configurations, then adjust based on the brief.

### Personal Brand / Speaker / Athlete Site
```
taste-skill           ← primary layout + anti-slop discipline
soft-skill            ← expensive feel, premium typography
emil-design-eng       ← micro-interactions, invisible polish
output-skill          ← full code, no truncation
```
Check `taste-skill/blocks/` first — `cinematic-video-hero`, `three-col-portrait-content-form`, and `five-col-photo-mosaic-thumbnail` are saved patterns for exactly this type of page.

### Awwwards / Agency / Experimental Page
```
gpt-tasteskill        ← AIDA structure, GSAP motion, bento discipline
soft-skill            ← expensive foundations
imagegen-frontend-web ← visual reference images first (optional but recommended)
output-skill          ← full code
```

### SaaS Product Landing Page
```
taste-skill           ← landing page discipline
ui-ux-pro-max         ← component and pattern reference
emil-design-eng       ← interaction polish
output-skill          ← full code
```

### Dashboard / Admin Panel
```
ui-ux-pro-max         ← layout, data hierarchy, component standards
impeccable            ← polish and audit
emil-design-eng       ← interaction states, hover, focus, loading
output-skill          ← full code
```

### Minimalist Editorial Site
```
minimalist-skill      ← primary aesthetic
taste-skill           ← layout discipline and anti-slop
emil-design-eng       ← typographic rhythm, invisible polish
output-skill          ← full code
```

### Industrial / Tactical / Military Site
```
brutalist-skill       ← primary aesthetic
taste-skill           ← layout structure
output-skill          ← full code
```

### Mobile App UI
```
imagegen-frontend-mobile ← screen concepts first
ui-ux-pro-max            ← implementation standards
emil-design-eng          ← gesture states, micro-interactions
output-skill             ← full code
```

### Brand Identity / Visual System
```
brandkit              ← image generation for boards, logos, identity decks
stitch-skill          ← DESIGN.md if a design system definition is also needed
```

### Redesign of Existing Site
```
redesign-skill        ← audit first — identify what to keep, what to kill
[relevant Job B skill] ← implement the upgrade
[relevant overlays]   ← apply target aesthetic
output-skill          ← full code
```

---

## 4. THE BLOCK LIBRARY

Before building any layout from scratch, check `taste-skill/blocks/`. Saved patterns are production-grade and skip the invention step.

Current blocks:

| Block | Category | File |
|---|---|---|
| `cinematic-video-hero` | hero | `blocks/hero/cinematic-video-hero.md` |
| `three-col-portrait-content-form` | feature | `blocks/feature/three-col-portrait-content-form.md` |
| `five-col-photo-mosaic-thumbnail` | gallery | `blocks/gallery/five-col-photo-mosaic-thumbnail.md` |

When a saved block fits the brief, load it and adapt. Do not rebuild what is already built.

---

## 5. EXECUTION ORDER

When multiple skills are in the stack, execute in this sequence:

1. **Image generation** (if in scope) — `imagegen-frontend-web`, `brandkit`, or `imagegen-frontend-mobile`. Get visuals settled before writing code.
2. **Audit** (if redesign) — `redesign-skill`. Understand what exists before changing it.
3. **Primary implementation skill** — `taste-skill`, `ui-ux-pro-max`, or `impeccable`. This is the structural pass.
4. **Aesthetic overlays** — `soft-skill`, `minimalist-skill`, `brutalist-skill`, `gpt-tasteskill`. These refine the feel.
5. **Micro-interaction polish** — `emil-design-eng`. Last layer before output.
6. **Output enforcement** — `output-skill`. Always runs last, on every code output.

Never run aesthetic overlays before the structural pass. Never run output enforcement before the code is complete.

---

## 6. WHAT THIS SKILL DOES NOT DO

This skill does not write design code, generate images, or make aesthetic decisions. It selects skills. If you find yourself making a layout decision inside this skill, stop and route it through the appropriate Job B or overlay skill instead.

If the brief is unclear — ask one question. Not a multi-question dump. One question that resolves the most consequential ambiguity. Then proceed.