# Agent Skills

A collection of 26 [Claude Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) — reusable, model-invoked capabilities for Claude Code and the Claude apps. Heavy on design/frontend, plus research, writing, and skill-authoring tools.

Each skill is a self-contained folder with a `SKILL.md` (its instructions) and any supporting scripts/data. Skills are grouped into categories below — open any category for details.

## Install

```bash
git clone https://github.com/jholmquest99/agent-skills.git
cd agent-skills

# Install EVERY skill globally (flattens categories — skills must sit
# directly inside the skills dir to load):
for s in skills/*/*/; do cp -R "$s" ~/.claude/skills/; done

# …or grab a single skill:
cp -R skills/design-foundations/design-master ~/.claude/skills/

# …or install per-project instead of globally:
for s in skills/*/*/; do cp -R "$s" /path/to/project/.claude/skills/; done
```

Skills trigger automatically from their description, or invoke a user-invocable one with `/<skill-name>`.

## Categories

### [Design Foundations](skills/design-foundations/) (4)
The intelligence layer — orchestration, design systems, and the craft details that make UI feel great. Start with `design-master`.

`design-master`, `emil-design-eng`, `impeccable`, `ui-ux-pro-max`

### [Visual Styles](skills/visual-styles/) (5)
Pick-an-aesthetic skills. Each enforces a distinct, opinionated look so output never feels templated.

`brutalist-skill`, `gpt-tasteskill`, `minimalist-skill`, `soft-skill`, `taste-skill`

### [Image Generation](skills/image-generation/) (3)
Generate premium visual references, screen concepts, and brand imagery before (or instead of) writing code.

`brandkit`, `imagegen-frontend-mobile`, `imagegen-frontend-web`

### [Build & Redesign](skills/build-and-redesign/) (4)
Turn designs into code, upgrade existing interfaces, and control generation output.

`image-to-code-skill`, `output-skill`, `redesign-skill`, `stitch-skill`

### [Content & Docs](skills/content-and-docs/) (2)
Writing, documents, and knowledge management.

`html-to-pdf`, `humanizer`

### [Research & Thinking](skills/research-and-thinking/) (5)
Multi-angle research, decision pressure-testing, and analysis utilities.

`ai-impact-analysis`, `ai-news-briefing`, `board-of-executives`, `devils-advocate`, `research`

### [Skill Authoring](skills/skill-authoring/) (3)
Meta-skills for building, routing, and reviewing other skills.

`skill-directory`, `skill-reviewer`, `skillsmd-interview-and-build`

---

*MIT licensed. Shared as-is — each skill's full instructions live in its `SKILL.md`.*
