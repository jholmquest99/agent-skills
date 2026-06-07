---
name: three-col-portrait-content-form
category: feature
dial_compatibility:
  variance: [5, 9]
  motion: [3, 8]
  density: [4, 7]
when_to_use: "Experience or offer sections on speaker, athlete, executive, or premium service pages. Best when you have a strong cut-out portrait asset. The three columns give the section weight without requiring a separate page."
not_for: "SaaS feature lists, product comparison tables, dashboard onboarding."
stack: ["html", "css"]
source: "Dan Rooney Speaker site — CAVU Experience section"
---

## Visual Sketch

```
┌──────────────────────────────────────────────────────────────────┐
│ [PORTRAIT CUT-OUT]  │  [ICON/GIF]                │ ┌──────────┐ │
│ (full-height,       │  [Body copy — centered]     │ │ PANEL    │ │
│  anchored bottom,   │                             │ │ HEADING  │ │
│  bleeds top & bot)  │  "Live Unlimited."          │ │          │ │
│                     │  (display tagline, italic)  │ │ [Form]   │ │
│                     │                             │ │          │ │
│                     │                             │ │ [Submit] │ │
│                     │                             │ └──────────┘ │
└──────────────────────────────────────────────────────────────────┘
```

Grid: `38fr 35fr 27fr`. Fixed height (815px). Col 1: portrait bleeds to edges. Col 2: centered editorial content. Col 3: dark panel with form.

## CSS

```css
/* ─── SECTION WRAPPER ─── */
.experience {
  background-color: #000;
  padding: 0;
}

.experience-inner {
  display: grid;
  grid-template-columns: 38fr 35fr 27fr;
  min-height: 815px;
  max-height: 815px;
  align-items: stretch;
  overflow: hidden;
}

/* ─── COL 1: PORTRAIT ─── */
.exp-portrait-col {
  position: relative;
  overflow: hidden;
  background: #000;
  min-height: 600px;
}
.exp-portrait-col > img {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  height: 99%;
  width: auto;
  max-width: none;
}

/* ─── COL 2: EDITORIAL CONTENT ─── */
.exp-content-col {
  padding: 12px 80px 92px 56px;
  height: 815px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  background: #000;
}
.exp-body {
  font-size: 1rem;
  line-height: 1.82;
  color: rgba(255,255,255,0.6);
  margin-bottom: 28px;
  max-width: 400px;
}
/* Italic display tagline — "Live Unlimited." style */
.exp-tagline {
  font-size: clamp(2.2rem, 3.6vw, 3.4rem);
  font-style: italic;
  font-weight: 500;
  color: var(--accent-light);   /* soft gold, warm cream, etc. */
  line-height: 1.2;
}

/* ─── COL 3: PANEL (form, booking, contact) ─── */
.exp-panel-col {
  padding: 36px 40px;
  background: var(--bg-mid);    /* slightly lighter than pure black */
  border-left: 1px solid rgba(255,255,255,0.06);
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.exp-panel-title {
  font-weight: 900;
  font-size: clamp(1.3rem, 1.7vw, 1.9rem);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  line-height: 1.1;
  color: #fff;
  margin-bottom: 8px;
}
.exp-panel-sub {
  font-size: 0.88rem;
  color: rgba(255,255,255,0.5);
  line-height: 1.72;
  margin-bottom: 14px;
  padding-bottom: 14px;
  border-bottom: 1px solid rgba(255,255,255,0.07);
}

/* Form fields — tight variant for panel column */
.f-field { margin-bottom: 10px; }
.f-field label {
  display: block;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.55);
  margin-bottom: 5px;
}
.f-field input,
.f-field select,
.f-field textarea {
  width: 100%;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.12);
  color: #fff;
  font-size: 0.9rem;
  padding: 9px 14px;
  border-radius: 0;
  outline: none;
  transition: border-color 0.15s;
}
.f-field input:focus,
.f-field textarea:focus { border-color: var(--accent); }
.f-field textarea { height: 72px; resize: none; }
.f-submit {
  width: 100%;
  padding: 13px;
  background: var(--accent);
  color: #000;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  border: none;
  cursor: pointer;
  margin-top: 4px;
  transition: opacity 0.15s;
}
.f-submit:hover { opacity: 0.88; }
.f-alt {
  font-size: 0.78rem;
  color: rgba(255,255,255,0.4);
  text-align: center;
  margin-top: 8px;
}
.f-alt a { color: var(--accent); }
```

## HTML

```html
<section class="experience" id="experience">
  <div class="experience-inner">

    <!-- Col 1 — Portrait, full-height cut-out, anchored to bottom -->
    <div class="exp-portrait-col">
      <img src="assets/subject-nobg.png" alt="[Name] — no background portrait">
    </div>

    <!-- Col 2 — Editorial content, centered -->
    <div class="exp-content-col">
      <img src="assets/icon-or-animation.gif" alt="Icon" style="height:200px; margin:0 auto 28px; opacity:0.9;">
      <p class="exp-body">
        Body copy explaining the offer or experience. Keep to 2–3 sentences.
        This is not a feature list — it is a single compelling thought.
      </p>
      <div class="exp-tagline">Your Tagline Here.</div>
    </div>

    <!-- Col 3 — Booking / contact panel -->
    <div class="exp-panel-col">
      <img src="assets/small-icon.png" alt="" style="display:block;height:100px;width:auto;margin:0 auto 15px;opacity:0.75;">
      <div class="exp-panel-title">Book the<br>Experience</div>
      <p class="exp-panel-sub">Supporting sentence for social proof or context — who else has done this.</p>
      <form onsubmit="handleSubmit(event)">
        <div class="f-field">
          <label>Full Name</label>
          <input type="text" placeholder="Your full name" required>
        </div>
        <div class="f-field">
          <label>Email</label>
          <input type="email" placeholder="you@company.com" required>
        </div>
        <div class="f-field">
          <label>Phone</label>
          <input type="tel" placeholder="+1 (555) 000-0000">
        </div>
        <div class="f-field">
          <label>Event Details</label>
          <textarea placeholder="Date, location, audience size, context."></textarea>
        </div>
        <button type="submit" class="f-submit">Request the Experience</button>
      </form>
      <p class="f-alt">Or email: <a href="mailto:contact@domain.com">contact@domain.com</a></p>
    </div>

  </div>
</section>
```

## Mobile Fallback

At `< 900px`:
- Drop to single column. Stack: panel first (the action), then content, hide portrait.
- Remove fixed heights.

```css
@media (max-width: 900px) {
  .experience-inner {
    grid-template-columns: 1fr;
    max-height: none;
    min-height: auto;
  }
  .exp-portrait-col { display: none; }
  .exp-content-col {
    padding: 60px 32px;
    height: auto;
    order: 2;
  }
  .exp-panel-col {
    border-left: none;
    border-top: 1px solid rgba(255,255,255,0.06);
    order: 1;
    padding: 48px 32px;
  }
}
```

## Motion Variants

**Band 1–3:** Static. No animation.

**Band 4–7 (Default):** Panel column reveals on scroll with a `.r` class (fade-up 30px, 0.6s ease). Portrait fades in from left edge.

**Band 8–10 (Cinematic):** Portrait slides up from below-fold on scroll (GSAP ScrollTrigger). Content col chars stagger in. Panel slides in from right with subtle depth.

## Dark-Mode Notes

This block is black by design. No system dark-mode swap. The panel column uses `var(--bg-mid)` — set this to `#090f1e` or similar for a dark navy that reads as "separate" from the black background, without going light.

## Anti-Patterns

- **Do not** use a portrait with a background — the cut-out anchored to the bottom edge is the whole point. Always use a no-background PNG.
- **Do not** add more than 4 form fields. More than 4 and the panel becomes a full-page form; build a dedicated form page instead.
- **Do not** center the text in the panel column — left-align reads as a card, centered reads as a modal.
- **Do not** use equal-width columns (`1fr 1fr 1fr`). The asymmetric `38fr 35fr 27fr` ratio is intentional — it creates visual hierarchy before the eye reads a word.

## References

- Original: Dan Rooney Speaker Site (`/private/tmp/dan-rooney-speaker/index.html`, lines 1711–1756)
- CSS: lines 558–720 of the same file