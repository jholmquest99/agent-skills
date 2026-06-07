---
name: cinematic-video-hero
category: hero
dial_compatibility:
  variance: [6, 10]
  motion: [5, 10]
  density: [3, 6]
when_to_use: "Premium personal brand, speaker, founder, military/athlete, or luxury service page where identity IS the product. Works best when you have a looping video asset or full-bleed photography."
not_for: "SaaS product landing pages, B2B tool sites, editorial/manifesto launches."
stack: ["html", "css", "vanilla-js"]
source: "Dan Rooney Speaker site — hero section"
---

## Visual Sketch

```
┌─────────────────────────────────────────────────────────┐
│  [looping video — full bleed, 70% darkened left edge]   │
│                                                         │
│  [LOGO] TITLE / RANK              ┌─────────────────┐  │
│                                   │ Key Credentials │  │
│  DISPLAY NAME                     │ ─────────────── │  │
│  (massive, 900 weight, stacked)   │ ▸ Credential 1  │  │
│                                   │ ▸ Credential 2  │  │
│  ROLE · ROLE · ROLE               │ ▸ Credential 3  │  │
│                                   │ ▸ ...           │  │
│  [Primary CTA]  [Ghost CTA]       └─────────────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

Layout: full-viewport, flex row (space-between). Left: eyebrow + display name + subtitle + CTAs. Right: glassmorphism credential card.

## CSS

```css
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 0 48px;
  overflow: hidden;
}

/* Looping background video */
.hero-video-wrap {
  position: absolute;
  inset: 0;
  overflow: hidden;
  z-index: 0;
}
.hero-video-wrap::after {
  content: '';
  position: absolute;
  inset: 0;
  /* Darken hard on left where text lives, open up on right */
  background: linear-gradient(110deg, rgba(5,10,22,0.70) 28%, rgba(5,10,22,0.30) 100%);
  z-index: 1;
}
.hero-video-wrap iframe {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  /* Maintain 16:9 and cover the viewport */
  width: 177.78vh;
  height: 56.25vw;
  min-width: 100%;
  min-height: 100%;
  pointer-events: none;
  border: none;
}

/* Inner layout */
.hero-inner {
  position: relative;
  z-index: 2;
  max-width: 1360px;
  margin: 0 auto;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 60px;
  padding-top: 100px;
  padding-bottom: 80px;
}
.hero-left { flex: 1; max-width: 720px; }
.hero-right { flex-shrink: 0; }

/* Eyebrow (logo + rank/label) */
.hero-eyebrow {
  display: flex;
  align-items: center;
  gap: 3px;
  margin-bottom: 28px;
}
.hero-eyebrow span {
  font-size: 1.22rem;
  font-weight: 700;
  letter-spacing: 0.32em;
  text-transform: uppercase;
  color: var(--accent);         /* gold, electric blue, etc. */
  padding-left: 20px;
}

/* Display name — maximum cinematic weight */
.hero-name {
  font-weight: 900;
  font-size: clamp(3.8rem, 7.5vw, 7rem);
  line-height: 0.93;
  letter-spacing: 0.015em;
  text-transform: uppercase;
  color: #fff;
  margin-bottom: 28px;
  text-shadow: 0 2px 36px rgba(0,0,0,0.75), 0 1px 8px rgba(0,0,0,0.55);
}

/* Pipe-separated roles */
.hero-subtitle {
  font-size: 0.9rem;
  font-weight: 500;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.7);
  margin-bottom: 52px;
}
.hero-subtitle .sep { color: rgba(255,255,255,0.3); margin: 0 12px; }

.hero-ctas { display: flex; gap: 14px; align-items: center; flex-wrap: wrap; }

/* Glassmorphism credential card */
.cred-card {
  background: rgba(5,10,22,0.72);
  backdrop-filter: blur(22px);
  -webkit-backdrop-filter: blur(22px);
  border: 1px solid rgba(255,255,255,0.13);
  padding: 36px 40px;
  min-width: 290px;
}
.cred-card-head {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 20px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}
.cred-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 7px 0;
  font-size: 0.82rem;
  font-weight: 500;
  color: rgba(255,255,255,0.88);
  border-bottom: 1px solid rgba(255,255,255,0.05);
}
.cred-item:last-child { border-bottom: none; }
.cred-item::before { content: '▸'; color: var(--accent); flex-shrink: 0; margin-top: 3px; font-size: 0.6rem; }
```

## HTML

```html
<section class="hero" id="home">
  <div class="hero-video-wrap">
    <iframe
      src="https://player.vimeo.com/video/VIDEO_ID?background=1&autoplay=1&loop=1&muted=1&byline=0&title=0"
      frameborder="0"
      allow="autoplay; fullscreen; picture-in-picture"
      allowfullscreen>
    </iframe>
  </div>
  <div class="hero-inner">
    <div class="hero-left">
      <div class="hero-eyebrow">
        <img src="assets/logo-white.svg" alt="Organization Logo" style="height:44px; width:auto; opacity:0.9;">
        <span>Title / Rank</span>
      </div>
      <h1 class="hero-name">DISPLAY<br>NAME<br>HERE</h1>
      <p class="hero-subtitle">
        Role One <span class="sep">|</span> Role Two <span class="sep">|</span> Role Three
      </p>
      <div class="hero-ctas">
        <a href="#book" class="btn-primary">Primary CTA</a>
        <a href="#intro" class="btn-ghost">Secondary CTA</a>
      </div>
    </div>
    <div class="hero-right">
      <div class="cred-card">
        <div class="cred-card-head">Key Credentials</div>
        <div class="cred-item">Credential One</div>
        <div class="cred-item">Credential Two</div>
        <div class="cred-item">Credential Three</div>
        <!-- Add as many cred-items as needed -->
      </div>
    </div>
  </div>
</section>
```

## Mobile Fallback

At `< 768px`:
- Stack `.hero-inner` to `flex-direction: column`
- Hide `.hero-right` (credential card) — too much content for mobile hero
- Scale `.hero-name` down: `font-size: clamp(2.8rem, 12vw, 4rem)`
- Reduce padding: `padding: 0 24px`

```css
@media (max-width: 768px) {
  .hero { padding: 0 24px; }
  .hero-inner { flex-direction: column; padding-top: 120px; padding-bottom: 60px; gap: 32px; }
  .hero-right { display: none; }
  .hero-name { font-size: clamp(2.8rem, 12vw, 4rem); }
}
```

## Motion Variants

**Band 1–3 (Low):** Static. No animation. Just the video plays.

**Band 4–7 (Default):** Stagger children in `.hero-left` with a CSS class `.r` (reveal) + `animation-delay` utilities. Each child fades up 40px on load.

**Band 8–10 (Cinematic):** GSAP timeline on load. Name chars split and stagger in. Credential card slides in from right with slight overshoot. Video overlay pulses subtly on scroll.

## Dark-Mode Notes

This block is inherently dark — the gradient overlay keeps it dark regardless of system preference. No dark-mode token swap needed. If you implement a light-mode toggle, swap the gradient overlay opacity: `rgba(255,255,255,0.10) → rgba(255,255,255,0.80)` and invert all text colors.

## Anti-Patterns

- **Do not** remove the gradient overlay. Without it, text becomes illegible on bright video frames.
- **Do not** use an auto-playing video with audio. `muted=1` is non-negotiable.
- **Do not** use `pointer-events: auto` on the iframe — it will trap scroll/click events.
- **Do not** drop a third CTA into `.hero-ctas`. Two maximum. Three is noise.
- **Do not** put more than 10 items in the credential card — it becomes a resume, not a hero signal.

## References

- Original: Dan Rooney Speaker Site (`/private/tmp/dan-rooney-speaker/index.html`, lines 1562–1602)
- Comparable production examples: johnlasseter.com-style speaker sites, Draper hero on drapervc.com