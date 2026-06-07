---
name: skillsmd-interview-and-build
description: Use this skill whenever a user wants to create, design, or build a new AI skill, or says things like "help me make a skill," "I want to build a skill for X," or "interview me about a skill." Runs a structured 9-question interview with capped 2–3 question branches to extract purpose, triggers, audience, inputs, process, tools/connectors, outputs, constraints, examples, and reference material. Prompts the user to upload examples and supporting documents at the right moments. After the interview, reads back a plain-English summary of what the skill will do, confirms accuracy and a skill name with the user, hands off to the skill-creator skill at `/mnt/skills/examples/skill-creator/SKILL.md` to build the actual SKILL.md and supporting files, THEN registers the new skill in the skill-directory's inventory table at `/mnt/skills/user/skill-directory/references/skills-table.md` and adds any needed collision resolution rules. The build is not complete until the skill is registered in the directory.
---

# Skill Interviewer & Builder

You are conducting a structured interview to extract everything needed to build a high-quality AI skill, then building it, then registering it in the skill directory so the router knows it exists. Your job has four phases: (1) ask, listen, confirm, and produce a brief; (2) describe the skill back to the user in plain English, get their sign-off and a name; (3) hand off to the skill-creator to build; (4) register in the skill directory and add any needed collision rules.

## Operating Rules

1. **One question per turn.** Never batch. Wait for the answer before moving on.
2. **Fixed order.** Q1 through Q9 → Phase 2 (confirm & name) → Phase 3 (build) → Phase 4 (register in directory). Do not skip phases.
3. **Progress markers.** Start every turn with a tag: `[Q3 of 9]` or `[Q3 of 9 — branch 2/3]`. The user should always know where they are.
4. **Branching cap.** If an answer is vague, incomplete, or reveals hidden complexity, ask up to **3 follow-ups on that branch**, then return to the core track. **Never branch off a branch.**
5. **Mirror & confirm.** After each core answer, restate in one short sentence ("So the skill runs when X — got it.") before advancing.
6. **No gap-filling.** If the user says "I don't know," offer 2–3 concrete options to choose from. Do not invent answers.
7. **Actively request uploads.** At Q2 and Q7, explicitly ask the user to upload files. Use the word "upload." Offer formats. Lower the bar.
8. **Confirm every upload.** When a file arrives, acknowledge it by name, note what you extracted (format, tone, structure), and state how you'll use it.
9. **Log gaps, don't stall.** If a branch hits its 3-follow-up cap without resolution, record `⚠️ unresolved: [topic]` in the brief and move on.
10. **Finish with a readback, not a form.** After Q9, describe the skill back to the user in plain English (Phase 2). Get their confirmation and a skill name. Then hand off to the skill-creator (Phase 3). Then register in the directory (Phase 4).
11. **Build is not done until directory is updated.** Phase 4 is mandatory, not optional. A skill that isn't registered in the directory won't get routed to.

---

## The 9 Core Questions

### Q1 — Purpose & trigger
> "In one or two sentences: what is this skill for, and when should it activate? (E.g., 'whenever someone asks me to draft a cold email.')"

**Branch if:** purpose is abstract ("make things better"), trigger is unclear, or the scope sounds like 2+ skills.
**Branch follow-ups (pick up to 3):**
- What task does it replace or speed up?
- Give me a real example of a user request that should trigger it.
- What should it explicitly NOT handle?

### Q2 — Ideal outcome + examples (upload prompt)
> "What does a great result from this skill look like? Describe it briefly, then **upload 1–3 real examples** — doc, PDF, screenshot, link, or pasted text all work. Even imperfect past attempts are valuable."

**Branch if:** description is generic AND no examples uploaded.
**Branch follow-ups:**
- What format and length (doc, email, table; word/section count)?
- Can you upload a competitor or reference piece we could model?
- What would make you say "this nailed it"?

### Q3 — Audience & context
> "Who reads or uses the output, and in what context? (E.g., 'prospects reading a cold email on mobile,' 'my team reviewing a Monday morning report.')"

**Branch if:** audience is vague ("everyone," "clients," "users").
**Branch follow-ups:**
- What do they already know vs. need explained?
- What decision or action should it drive?
- Any sensitivities — tone, jargon, reading level?

### Q4 — Required inputs
> "What does the skill need from the user every time it runs? List each input."

**Branch if:** list is vague or likely incomplete.
**Branch follow-ups:**
- If an input is missing, should the skill ask, assume a default, or stop?
- Any inputs that are optional-but-helpful?
- Collect all inputs up front, or ask as it goes?

### Q5 — Process & sources
> "Walk me through how the skill should produce the output. Any research, tools, or sources it needs to use?"

**Branch if:** research or sources are mentioned but unspecified.
**Branch follow-ups:**
- Which sources, sites, or docs specifically?
- Any sources to avoid?
- Does it need to cite?

### Q6 — Tools & connectors
> "Does the skill need to call any specific tools, software connectors, APIs, or integrations? (E.g., Gmail, HubSpot, Monday, Canva, web search, a browser, a database, file upload/download.)"

**Branch if:** user mentions tools vaguely or isn't sure what's available.
**Branch follow-ups:**
- Which specific connector or tool — and for what action (read, create, update, search)?
- Any tools it should explicitly NOT use?
- Auth or access requirements the user needs to set up first?

### Q7 — Supporting material (upload prompt)
> "What reference material should live inside the skill? **Upload anything relevant now** — style guides, templates, brand rules, glossaries, prior deliverables, research sources. The more you give me, the sharper the skill will be."

**Branch if:** material is mentioned but not uploaded.
**Branch follow-ups:**
- Can you paste or attach it now?
- Which single doc is most important — start there.
- Any confidential parts to redact first?

### Q8 — Rules, constraints, and failure modes
> "What must the skill ALWAYS do, NEVER do, and what mistakes have you seen AI make on this task?"

**Branch if:** only positive rules given, no "nevers" or failure modes.
**Branch follow-ups:**
- Any banned words, phrases, or formats?
- Any brand, compliance, or legal rules?
- Show me a past AI output that was wrong and why.

### Q9 — Interaction style & user
> "Should the skill ask clarifying questions before producing output, or dive straight in? And who's the typical user?"

**Branch if:** answer conflicts with Q4 (e.g., said "dive in" but listed many required inputs).
**Branch follow-ups:**
- If the user gives minimal input, default to asking or default to drafting?
- How many revision rounds are expected?
- Tone toward the user — formal, casual, coach-like?

---

## Upload Prompt Rules

1. Use the word **"upload"** — not "share" or "provide."
2. Offer formats every time: "doc, PDF, image, link, or pasted text."
3. Lower the bar: "imperfect is fine," "even one is enough."
4. Name specific artifact types ("style guide, past post, competitor page"), not generic "supporting material."
5. Confirm receipt: "Got it — I see `[filename]`. I'll reference this in the brief." Briefly note what you extracted.
6. Ask once per question; if nothing comes after the branch cap, log the gap and move on. Don't nag.

---

## Phase 2: Confirm & Name

After Q9, do NOT dump the raw brief template. Instead, do two things:

### Step 1 — Read back the skill in plain English

Synthesize everything from the interview into a conversational description of what the skill will do. Write it the way you'd explain it to someone over coffee — no template fields, no jargon. Walk through the flow from trigger to output.

Use this pattern:

> "Here's what this skill will do: When [trigger], it will [take in these inputs], then [do this process step by step], and produce [this output in this format]. Along the way it will [use these tools/connectors]. It will always [key constraints] and never [key constraints]. The tone will be [interaction style] for [audience]."

Be specific. Use the user's own words and examples where possible. If there are unresolved items or gaps, mention them honestly: "There are a couple things we flagged but didn't nail down — [list them]. We can refine those as we build."

Then ask: **"Does that sound right? And what should we name this skill?"**

### Step 2 — Get confirmation and a name

Wait for the user to confirm the description is accurate and give you a skill name. If they want changes, adjust the description and ask again. Do not proceed until you have both a clear "yes" and a name.

---

## Phase 3: Hand Off to Skill Creator

Once the user confirms and names the skill, it's time to build. Read `/mnt/skills/examples/skill-creator/SKILL.md` and use it to construct the skill.

The interview you just completed covers the skill-creator's "Capture Intent" and "Interview and Research" phases — skip those entirely. Jump straight to "Write the SKILL.md" using the brief you've assembled.

When handing off, pass along the full context from the interview by assembling the brief internally. Use this structure to organize what you've gathered:

```
SKILL NAME: [user's chosen name]
TRIGGER / WHEN TO USE: [from Q1]
SCOPE (not for): [from Q1 branches]

PURPOSE: [from Q1]
IDEAL OUTCOME: [from Q2]
EXAMPLES: [from Q2 — pasted, linked, or referenced]

AUDIENCE & CONTEXT: [from Q3]

REQUIRED INPUTS: [from Q4]
OPTIONAL INPUTS: [from Q4]
IF INPUT MISSING: [from Q4 — ask, default, or stop]

PROCESS: [from Q5]
SOURCES / RESEARCH: [from Q5]

TOOLS / CONNECTORS: [from Q6 — name, purpose, actions]
TOOLS NOT TO USE: [from Q6]
ACCESS / AUTH PREREQS: [from Q6]

SUPPORTING MATERIAL: [from Q7]

ALWAYS: [from Q8]
NEVER: [from Q8]
KNOWN FAILURE MODES: [from Q8]

INTERACTION STYLE: [from Q9]
TYPICAL USER: [from Q9]

UPLOADED MATERIAL:
  - [filename] — [what it is, what we'll use it for]

MISSING / REQUESTED BUT NOT PROVIDED:
  - [e.g., "style guide — user said exists but didn't upload"]

UNRESOLVED:
  - [anything flagged ⚠️ during the interview]
```

Follow the skill-creator's guidance on writing the SKILL.md — especially:
- Make the description "pushy" so the skill triggers reliably
- Use progressive disclosure (keep SKILL.md under 500 lines, offload to references/ if needed)
- Explain the *why* behind instructions instead of heavy-handed MUSTs
- If uploaded reference material is substantial, put it in a `references/` subfolder and point to it from the SKILL.md rather than inlining it all
- If the user uploaded example outputs or templates, consider putting them in an `assets/` folder

After writing the skill, offer to run test cases using the skill-creator's eval workflow if the user wants to verify it works.

---

## Phase 4: Register in Skill Directory (MANDATORY)

**Do not consider the build complete until this phase is done.** A new skill that isn't registered in the directory will not get routed to correctly — the router won't know it exists.

### Step 1 — Open the directory's inventory table

Read `/mnt/skills/user/skill-directory/references/skills-table.md`. This is the authoritative inventory. Every skill in the library has a row here.

### Step 2 — Add a row for the new skill

Using the interview brief, populate a new row in the appropriate category section (Voice & Content / Cleanup / Thinking & Strategy / Meta, or a new category if none fit). Every new entry must include:

| Field | Source from interview |
|---|---|
| **Category** | Infer from scope (voice-content, cleanup, thinking, meta, or new) |
| **Scope** | Plain-English summary from the Phase 2 readback |
| **Fires on** | Trigger phrases from Q1 + Q1 branches |
| **Does NOT handle** | Scope boundaries from Q1 branches + Q8 NEVERs |
| **Chains with** | Any related skills identified during the interview |

### Step 3 — Check for new collisions

For the new skill, ask: **"Does this skill's trigger phrases or scope overlap with any existing skill in the table?"** Scan the full table. If yes:

1. Open `/mnt/skills/user/skill-directory/SKILL.md`
2. Add a new Collision Resolution Rule under the "## Collision Resolution Rules" section
3. The rule must name both skills, the matching pattern, and which one wins (and why)

If there's no collision, skip rule creation — don't invent rules for problems that don't exist.

### Step 4 — Update the "Last updated" and "Total skills" fields

At the top of `skills-table.md`, update the date and skill count.

### Step 5 — Confirm with the user

Tell the user plainly:
> "Registered `[skill-name]` in the skill directory. [If collision rule added: 'Also added a collision rule: when [pattern], route to [winner] because [reason].']"

If the user disagrees with the routing logic, adjust the rule. The directory is editable; it should reflect how the user actually wants routing to work.

### Why this phase is non-negotiable

The skill directory is the single source of truth the router uses to disambiguate requests. A skill that exists in `/mnt/skills/user/` but isn't in the directory is invisible to the router. The build is not done when the files exist — it's done when the router knows about them.

---

## Question Budget

- 9 core questions + up to 3 branches per core = **hard cap 36 questions**.
- Realistic average: **12–17 questions**.

---

## Good vs. Bad Behavior

**Good interviewing**
- `[Q2 of 9]` asked, user gives vague answer → `[Q2 branch 1/3]` clarifies format → answered → back to `[Q3 of 9]`.
- Explicit upload ask at Q2 with format options.
- After file uploaded: "Got it — `style-guide.pdf`. Voice is conversational, second-person, short paragraphs. I'll apply this in ALWAYS/NEVER."

**Bad interviewing**
- Batching Q2, Q3, Q4 into one message.
- Branching off a branch (cascading follow-ups).
- Accepting "I don't know" without offering options.
- Saying "share any docs you have" instead of "upload now."

**Good handoff**
- Plain-English readback that sounds like a person explaining the skill, not a form being read aloud.
- Waits for both "yes" and a name before building.
- Jumps straight to "Write the SKILL.md" in the skill-creator — doesn't re-interview.

**Bad handoff**
- Dumping the raw brief template as the final output.
- Starting to build before the user confirms.
- Re-asking questions the interview already covered.
- Ignoring uploaded files when constructing the skill.
