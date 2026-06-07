---
name: five-col-photo-mosaic-thumbnail
category: gallery
dial_compatibility:
  variance: [5, 9]
  motion: [2, 7]
  density: [5, 8]
when_to_use: "Mission, foundation, or portfolio sections where you want to show a body of photographic work while keeping one slot as a primary video or CTA. Strong when the photos are documentary/editorial in quality. Works as a full-bleed top-of-section moment."
not_for: "Product screenshots, headshot grids, e-commerce product images."
stack: ["html", "css"]
source: "Dan Rooney Speaker site — Folds of Honor mosaic section"
---

## Visual Sketch

```
┌────────┬────────┬──────────────────────┬────────┬────────┐
│ img A  │ img C  │                      │ img E  │ img G  │
│        │        │   [VIDEO THUMBNAIL]  │        │        │
│ img B  │ img D  │   (clickable, fills  │ img F  │ img H  │
│        │        │    center column)    │        │        │
└────────┴────────┴──────────────────────┴────────┴────────┘
```

Grid: `1fr 1fr 6fr 1fr 1fr`. Outer 4 columns each hold 2 stacked images. Center column is a video thumbnail (6× wider). Fixed min-height ~480px. All cells stretch full height, no gaps.

## CSS

```css
.photo-mosaic {
  display: grid;
  grid-template-columns: 1fr 1fr 6fr 1fr 1fr;
  min-height: 480px;
  overflow: hidden;
  /* No gap — edges touch by design */
}

/* Photo columns — each holds 2 stacked images */
.photo-col {
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.photo-col img {
  flex: 1;
  width: 100%;
  object-fit: cover;
  display: block;
  min-height: 0;   /* Required for flex shrink to work in column direction */
}

/* Center column — video thumbnail or primary media */
.mosaic-center {
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background: var(--bg-dark);
  cursor: pointer;
}
.mosaic-center-media {
  flex: 1;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  position: relative;
}

/* Play button overlay (if video thumbnail) */
.mosaic-play-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0,0,0,0.25);
  transition: background 0.2s;
}
.mosaic-center:hover .mosaic-play-overlay { background: rgba(0,0,0,0.40); }
.mosaic-play-btn {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: rgba(255,255,255,0.12);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.25);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.2s, background 0.2s;
}
.mosaic-center:hover .mosaic-play-btn {
  transform: scale(1.08);
  background: rgba(255,255,255,0.20);
}
.mosaic-play-arrow {
  width: 0;
  height: 0;
  border-top: 10px solid transparent;
  border-bottom: 10px solid transparent;
  border-left: 18px solid #fff;
  margin-left: 4px;
}
```

## HTML

```html
<!-- The mosaic sits at the top of its parent section, full-bleed -->
<div class="photo-mosaic">

  <!-- Left outer column — 2 stacked images -->
  <div class="photo-col">
    <img src="assets/photo-1a.jpg" alt="">
    <img src="assets/photo-1b.jpg" alt="">
  </div>

  <!-- Left inner column — 2 stacked images -->
  <div class="photo-col">
    <img src="assets/photo-2a.jpg" alt="">
    <img src="assets/photo-2b.jpg" alt="">
  </div>

  <!-- Center — video thumbnail (or swap for a hero image) -->
  <div class="mosaic-center" onclick="openVideoModal()" style="position:relative;">
    <img class="mosaic-center-media"
         src="assets/video-thumbnail.jpg"
         alt="Watch: [Video Title]">
    <div class="mosaic-play-overlay">
      <div class="mosaic-play-btn">
        <span class="mosaic-play-arrow"></span>
      </div>
    </div>
  </div>

  <!-- Right inner column — 2 stacked images -->
  <div class="photo-col">
    <img src="assets/photo-3a.jpg" alt="">
    <img src="assets/photo-3b.jpg" alt="">
  </div>

  <!-- Right outer column — 2 stacked images -->
  <div class="photo-col">
    <img src="assets/photo-4a.jpg" alt="">
    <img src="assets/photo-4b.jpg" alt="">
  </div>

</div>
```

## Mobile Fallback

At `< 768px`, the outer columns are too narrow to read. Hide them and show only center + two inner columns (or just center alone at very small sizes):

```css
@media (max-width: 900px) {
  .photo-mosaic { grid-template-columns: 1fr 4fr 1fr; }
  /* Hide outer columns */
  .photo-col:first-child,
  .photo-col:last-child { display: none; }
}
@media (max-width: 560px) {
  .photo-mosaic { grid-template-columns: 1fr; }
  .photo-col { display: none; }
  .mosaic-center { min-height: 280px; }
}
```

## Motion Variants

**Band 1–3:** Static. Images load with natural browser behavior.

**Band 4–7 (Default):** Columns fade in on scroll with staggered delays — outermost columns last, center first.

**Band 8–10 (Cinematic):** GSAP ScrollTrigger. Columns scale from 0.95 to 1.0 and fade in, staggered outward from center. Photos get a subtle parallax within their columns (translate Y on scroll, clipped by overflow:hidden).

## Dark-Mode Notes

Images are editorial photography — they work in both themes. The mosaic wrapper has no background color itself; it takes the section's background. The center column uses `var(--bg-dark)` as a fallback for when the thumbnail hasn't loaded.

## Anti-Patterns

- **Do not** add gaps between columns. The flush edges are what make this feel like a print spread rather than a photo grid.
- **Do not** use portrait-orientation photos in the outer columns — they'll get heavily cropped. Square or landscape photos only.
- **Do not** put more than 2 images per photo column — 3 images creates slivers that lose their content.
- **Do not** swap the center for another photo grid cell. The center's 6fr weight anchors the whole composition. If you don't have a video, use a single high-drama photo with text overlay instead of shrinking it down.
- **Do not** add `gap` to the grid — even 1px ruins the continuous mosaic feel.

## References

- Original: Dan Rooney Speaker Site (`/private/tmp/dan-rooney-speaker/index.html`, lines 2159–2185)
- CSS: lines 996–1050 of the same file