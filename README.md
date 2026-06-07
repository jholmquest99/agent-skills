# Agent Skills

A collection of 28 [Claude Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) — reusable, model-invoked capabilities for Claude Code and the Claude apps. Most are design/frontend focused, plus a set of general research & thinking utilities.

## Installation

Each skill is a folder containing a `SKILL.md`. To use them, copy any skill folder into one of your skills directories:

```bash
# Clone
git clone https://github.com/jholmquest99/agent-skills.git
cd agent-skills

# Install ALL skills globally (loads in every session)
cp -R skills/* ~/.claude/skills/

# …or install just one
cp -R skills/design-master ~/.claude/skills/

# …or per-project
cp -R skills/design-master /path/to/project/.claude/skills/
```

Then invoke by asking for the task (skills trigger automatically from their description) or with `/<skill-name>` for user-invocable ones.

## Design package (20)

Orchestrated by **`design-master`** — a director skill that classifies a design brief and stacks the right skills below it in the correct order.

| Skill | What it does |
|---|---|
| `brandkit` | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. |
| `industrial-brutalist-ui` | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog degradation effects. |
| `decision` | Log a meaningful decision to brain/working/decisions.md. Use when the user says "/decision ... |
| `design-master` | Master design orchestrator. Use when asked to design, build, redesign, polish, or change the look and feel of anything. |
| `emil-design-eng` | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. |
| `gpt-taste` | Elite UX/UI & Advanced GSAP Motion Engineer. |
| `html-to-pdf` | Render an HTML file into a print-ready PDF using headless Chrome, with a fallback for splicing high-resolution screenshots into specific pages when the print pipeline renders them differently from the browser preview. |
| `humanizer` | Remove signs of AI-generated writing from text. Use when editing or reviewing text to make it sound more natural and human-written. Based on Wikipedia's comprehensive "Signs of AI writing" guide. |
| `image-to-code` | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then implement the website to match them as closely as possible. |
| `imagegen-frontend-mobile` | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile products. |
| `imagegen-frontend-web` | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal image FOR EVERY section. A landing page with 8 sections produces 8 images. |
| `impeccable` | Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, extract, or otherwise improve a frontend interface. |
| `minimalist-ui` | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows. |
| `full-output-enforcement` | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any task requiring exhaustive, unabridged output. |
| `redesign-existing-projects` | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality. Works with any CSS framework or vanilla CSS. |
| `high-end-visual-design` | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. Blocks all the common defaults that make AI designs look cheap or generic. |
| `stitch-design-taste` | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN. |
| `design-taste-frontend` | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. |
| `ui-ux-pro-max` | UI/UX design intelligence for web and mobile. Includes 50+ styles, 161 color palettes, 57 font pairings, 161 product types, 99 UX guidelines, and 25 chart types across 10 stacks (React, Next. |
| `wiki` | Maintain a Karpathy-style LLM-synthesized knowledge base in `brain/knowledge/raw/` and `brain/knowledge/wiki/`. |

## Utilities (8)

General research, analysis, and skill-authoring helpers.

| Skill | What it does |
|---|---|
| `ai-impact-analysis` | Use when the user provides a company website URL or company name and asks for an AI impact analysis, says "what would AI do to this business," "run an impact read on [URL]," "AI impact for [company]," or wants a board-grade view of how AI i |
| `ai-news-briefing` | Use when an operator says "/ai-news," "AI news briefing," "AI news today," "what's new in AI," "catch me up on AI," "AI update," "daily AI brief," "/morning-brief," or any variant asking for a rundown of recent AI developments. |
| `board-of-executives` | Use when the user says "what would my board say," "pressure-test from the top," "multiple exec perspectives," "what would [role] think," or needs a 360 review of a POC scope, capability idea, client recommendation, or strategic call. |
| `devils-advocate` | Use when the user says "poke holes in this," "stress test," "before I send this," "challenge this," "what am I missing," or is about to commit a POC scope, recommend a tool buy, or ship a client deliverable. |
| `research` | Use when the user says "research [topic]," "deep dive," "verify this," "fact-check," "before we recommend a buy," or "before we commit build hours. |
| `skill-directory` | The master router and overlap guard for the FPOV skill library. Use this skill whenever a request is ambiguous, could match multiple skills, or contains multi-skill signals (e.g. |
| `skill-reviewer` | Use when the user says "review this skill," "audit my skill," "check my SKILL.md," "is this skill any good," or drops a path to a SKILL.md file for critique. |
| `skillsmd-interview-and-build` | Use this skill whenever a user wants to create, design, or build a new AI skill, or says things like "help me make a skill," "I want to build a skill for X," or "interview me about a skill. |

---

*Shared as-is. Each skill's full instructions live in its `SKILL.md`.*
