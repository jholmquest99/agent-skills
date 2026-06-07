---
name: decision
description: Log a meaningful decision to brain/working/decisions.md. Use when the user says "/decision ...", "log this decision", "add to the decision log", or makes a clear strategic/tactical call that should be preserved across conversations (strategy, positioning, campaigns, tools, hires, scrapping an initiative). Also trigger proactively mid-conversation when the user makes a meaningful call ("we're going with X", "let's kill Y") by asking if they want it logged.
---

# Decision Log Skill

Append decisions to `brain/working/decisions.md` in the project root.

## Format

Every entry follows this exact structure, appended to the end of the file:

~~~
[YYYY-MM-DD] DECISION: <what was decided> | REASONING: <why> | CONTEXT: <what was going on that drove it>
~~~

- Date: today's date in YYYY-MM-DD (pulled from session context, not guessed)
- One line per decision. No multi-line entries.
- Pipe-separated fields. Always include all three.
- Write in past tense, third person or imperative -- pick whichever reads cleaner.

## What counts as a decision worth logging

- Strategy or positioning calls
- Campaign/initiative go/no-go
- Tooling choices (picking/dropping a tool, MCP, platform)
- Cadence or format changes
- Team/resourcing calls (who owns what)
- Process changes (new workflow, abandoning an old one)

## What does NOT belong in the log

- Task-level to-dos
- Transient preferences
- Things already captured as context updates or memory entries
- Exploratory thinking that wasn't actually decided

## How to run the skill

**The reasoning is mandatory. Never log a decision without it.**

1. Parse the user's input. Identify the decision itself.

2. **Always ask for the "why" before writing**, unless the user has already clearly stated the reasoning in the same message. Use a short, direct prompt:
   - "Got it. Why are we making this call?"
   - "What's driving this?"
   - "Before I log it -- what's the reasoning?"

   Do not fabricate, infer, or paraphrase reasoning from surrounding context. User's words only. If their answer is thin ("because it's better"), push once for specificity ("better how -- what's the actual driver?"), then accept whatever they give.

3. Context (what was going on that drove it) can be inferred from the conversation if obvious. If not obvious, ask briefly.

4. Read `brain/working/decisions.md`, append the new entry on a new line at the end of the file, save.

5. Confirm in one line: "Logged: [date] -- <decision summary>". Do not echo the full entry back.

## Proactive capture

When NOT invoked explicitly but the user says something that sounds like a real decision mid-conversation ("we're killing X", "let's go with Y", "I'm done with Z"), do this:

1. Ask: "Sounds like a decision -- want me to log it? If so, what's the reasoning?"
2. Only log if they confirm AND provide reasoning.
3. Don't nag. Ask once per decision.
