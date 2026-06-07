---
name: wiki
description: Maintain a Karpathy-style LLM-synthesized knowledge base in `brain/knowledge/raw/` and `brain/knowledge/wiki/`. Use when the user says "/wiki ingest", "/wiki query", "/wiki lint", "/wiki tags", "ingest this into the wiki", "add to knowledge", "what do we know about X", or drops source material (articles, PDFs, transcripts, meeting notes) that should enter the wiki. Trigger proactively when the user drops a new document in `brain/knowledge/raw/` and asks the agent to absorb, synthesize, or remember it.
---

# Wiki Knowledge Skill

Maintain a living knowledge base in `brain/knowledge/`. Raw sources go in, cross-linked wiki pages come out. Unlike RAG, synthesis happens once at ingest time and accumulates. Every later query reads a pre-synthesized page, not raw chunks.

## Folders

- `brain/knowledge/raw/`: immutable source documents. Articles, PDFs, transcripts, meeting notes, exported threads. Never edit these.
- `brain/knowledge/wiki/`: LLM-generated markdown pages. One file per concept, person, project, or entity.
- `brain/knowledge/TAGS.md`: the approved tag taxonomy. **Always check this file before applying or proposing tags.** If it doesn't exist or is a placeholder, ask the user to define their taxonomy before tagging anything.

On first invocation, if either folder is missing: create it and add a `.gitkeep`.

## How this fits with the rest of the workspace

| Surface | Purpose |
|---|---|
| `context/` | Static facts about user/team/work. Slow-changing ground truth. |
| `brain/working/decisions.md` | Append-only decisions timeline. |
| Auto-memory | Cross-session user preferences. |
| **`brain/knowledge/wiki/`** | **Synthesized knowledge from external source material.** |

The wiki is for *external* material the agent ingests. Don't duplicate context files or decision entries inside the wiki, link out to them instead.

## Page Schema

Every wiki page is a kebab-case markdown file at `brain/knowledge/wiki/<concept>.md`.

**Frontmatter fields:**

~~~markdown
---
title: <Canonical Name>
type: <person | company | product | concept | client | playbook | moc>
tags: [<status>, <scope>, <optional domain tags>]
aliases: [<other names this entity is known by>]
people: [<wiki person-page ids — only pages that exist in wiki/>]
related: [<wiki page ids>]
sources: [<raw source filenames without extension>]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
~~~

**Body structure:**
1. **H1 title** matching the canonical name.
2. **Summary** — 2–3 sentences. Plain English.
3. **H2 sections** as needed (Overview, Key Facts, In Practice, Platform Role, etc.).
4. **## Related** — `[[wikilinks]]` to other pages.
5. **## Sources** — every `raw/` file that contributed, linked with `[[raw/filename|Label]]: "excerpt"` format.

**Example:**

~~~markdown
---
title: Acme Corp
type: client
tags: [active, client, data-ops]
aliases: [Acme, Acme Corporation]
people: [jane-doe]
related: [agentic-data-cleaning, novolink]
sources: [acme-discovery-call-2026-03]
created: 2026-03-15
updated: 2026-05-29
---

# Acme Corp

Acme Corp is a mid-market logistics company engaged for data integration work. Introduced through [[jane-doe]].

## Key Facts
- 400 employees across 6 facilities
- Running 5 disparate systems; no unified data layer

## In Practice
Lead with [[agentic-data-cleaning]] — their pain is identical to [[qsc]].

## Related
- [[jane-doe]]
- [[agentic-data-cleaning]]
- [[novolink]]

## Sources
- [[raw/acme-discovery-call-2026-03|Acme discovery call (March 2026)]]: "We can't get our systems to talk to each other."
~~~

### Tag convention

- Tags are defined in `brain/knowledge/TAGS.md`. That file is the single source of truth.
- The `type:` field is NOT a tag — it is a separate frontmatter field with fixed values.
- People and technologies are pages referenced via `people:` and `related:`, never tags.
- `tags:` contains only: status values, scope values, and optional domain values from TAGS.md.
- Never invent a tag just for one page. If a concept applies to only one place, skip the tag.
- To add a new tag: propose it to the user with a one-line description. If approved, add it to `brain/knowledge/TAGS.md` first, then apply it to pages. Never apply an unapproved tag.

## Operations

### Ingest

Triggered by "/wiki ingest <file>", "ingest raw/<file>", or "absorb this".

1. Read the source file end to end.
2. Identify distinct concepts, people, projects, or entities worth a page.
3. For each, before creating: list existing filenames in `brain/knowledge/wiki/` and check for variant spellings, acronyms, or synonyms. If an existing page matches, update it. Never duplicate.
4. **Tag the page.** Read `brain/knowledge/TAGS.md` first. Only apply tags from the approved taxonomy. If a file clearly needs a tag that doesn't exist yet, propose it to the user with a one-line description. If approved, add it to `TAGS.md` first, then apply.
5. Add the source file to the Sources section of every page it contributed to, using `[[raw/filename|Label]]: "excerpt"` format.
6. Add `[[wiki-links]]` to related pages wherever those concepts are mentioned in the body.
7. Do not create a page for entities mentioned only once across all sources. Drop those into `brain/knowledge/wiki/_mentions.md` instead (create it if missing).
8. Report: pages created, pages updated, tags applied, any orphaned links created.

If asked to "ingest everything in raw", process files one at a time and report after each batch of five.

### First ingest (bulk seeding)

When the user is seeding the wiki for the first time with a batch of documents:

1. Check `brain/knowledge/TAGS.md`. If a taxonomy already exists (set up during workspace init), use it. Skip to step 4.
2. If `TAGS.md` is empty or a placeholder, ask the user: "How do you naturally organize your information? By client? Document type? Topic? Status? Just describe the groupings that feel natural." Build the taxonomy from their answer.
3. Propose 5 to 15 tags grouped into the facets they described. Show each tag with a one-line description. Wait for approval. Save the approved taxonomy to `brain/knowledge/TAGS.md`.
4. Scan all files in `brain/knowledge/raw/` without writing anything yet. Identify entities and themes.
5. Run ingest across all files and apply only tags from the approved taxonomy. Don't invent new tags mid-ingest without asking.
6. Update `brain/knowledge/TAGS.md` with the "Last updated" date.

### Query

Triggered by "/wiki query <topic>", "what do we know about X", or "search the wiki".

1. Search `brain/knowledge/wiki/` by filename, tag, and content. **Read only `wiki/`, not `raw/`.** Falling back to `raw/` defeats the point of the system.
2. Answer using what the wiki pages say.
3. Cite the specific wiki pages used by filename.
4. If the wiki doesn't cover it, say so directly and name which `raw/` files look relevant, or say nothing in `raw/` covers it either.

### Lint

Triggered by "/wiki lint" or "audit the wiki".

1. Find broken `[[links]]` (targets that don't exist as files).
2. Find pages covering the same concept under different names.
3. Find pages with no Sources section or empty sources.
4. Find pages with fewer than two sources and no updates in the last month. Consolidation candidates.
5. Find orphan tags (tags applied to only one page). Pruning candidates.
6. Find pages with no tags.
7. **Report findings. Propose fixes. Do not auto-apply.** Wait for explicit approval on each fix. Auto-merging is how wikis rot.

### Tags

Triggered by "/wiki tags" or "show the tag system".

1. Read `brain/knowledge/TAGS.md` for the approved taxonomy.
2. Scan all pages in `brain/knowledge/wiki/` for actual tag usage.
3. Compare: show which approved tags are in use, which are unused (candidates for removal from `TAGS.md`), and which tags appear on pages but aren't in `TAGS.md` (unapproved, need to be added or removed).
4. For each tag in use, show the count of pages and a few examples.
5. Flag tags used on only one page (pruning candidates).
6. Do not modify anything. Report only.

## House rules

- Preserve exact numbers, dates, and quotes from sources.
- When sources disagree, note the disagreement explicitly rather than picking one silently.
- Follow `.claude/rules/communication-style.md` for voice.
- Cross-link to the rest of the workspace where it makes sense. Reference `brain/working/decisions.md` by date. Reference `context/team.md` people by name. Don't copy-paste content that already lives elsewhere.
- Never create pages inside `brain/knowledge/wiki/` that duplicate `context/` files.

## Obsidian compatibility

The `[[wiki-link]]` syntax, YAML frontmatter tags, and folder layout are all Obsidian-native. **Recommended: point Obsidian directly at `brain/knowledge/` as the vault root** (File, Open Vault, select `brain/knowledge/`), not the workspace root. That way the graph view is scoped to wiki pages and their sources, not every markdown file in the workspace.

With `brain/knowledge/` as the vault:
- Graph view shows wiki pages as nodes, `[[links]]` as edges, and `raw/` source files as connected leaf nodes.
- Tag pane (sidebar) filters pages by tag.
- Backlinks panel shows every page that links to the one you're reading.

No extra config required.

## First-run setup

If `brain/knowledge/raw/` or `brain/knowledge/wiki/` don't exist when first invoked:

1. Create both folders.
2. Add `.gitkeep` to each.
3. Tell the user: "Drop source files in `brain/knowledge/raw/`, then say `/wiki ingest <filename>` or `ingest everything in raw`. For best results, point Obsidian at `brain/knowledge/` as the vault root."

### Synthesize

Triggered by "/wiki synthesize", "push decisions to wiki", or "synthesize working memory into wiki".

Reads `brain/working/decisions.md` and identifies decisions with durable implications — strategic calls, positioning shifts, tooling choices — that should be reflected in wiki pages. Does NOT touch decisions.md (append-only; never rewrite).

1. Read `brain/working/decisions.md` end to end.
2. For each entry, identify which wiki pages are affected by that decision (by entity, concept, or product mentioned).
3. For each affected page: propose a specific addition — a `## Strategic Decisions` section entry, or an update to an existing section — quoting the decision date and plain-language summary.
4. Present all proposed changes. Wait for explicit approval on each before writing.
5. After approval: update the affected pages. Add `updated: YYYY-MM-DD` to their frontmatter.
6. Do not synthesize every decision — only ones with durable implications. Operational calls, task-level notes, and transient preferences do not belong in the wiki.

## What not to ingest

- `context/`, `decisions/`, `projects/`, `templates/`. Those are workspace surfaces, not source material.
- Raw exports of the agent's own memory or past conversations.
- Anything with secrets (API keys, credentials).
