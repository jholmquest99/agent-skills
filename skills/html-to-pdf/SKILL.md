---
name: html-to-pdf
description: >
  Render an HTML file into a print-ready PDF using headless Chrome, with a
  fallback for splicing high-resolution screenshots into specific pages when
  the print pipeline renders them differently from the browser preview.
  Produces vector-quality PDFs by default; switches individual pages to raster
  only when needed. Use when the user says "render this HTML to PDF," "make
  a PDF of this page," "the PDF looks wrong on slide N," "fix the broken
  page in the PDF," or asks to convert any standalone HTML artifact into a
  shareable PDF (decks, one-pagers, posters, reports, certificates,
  print-styled web pages). Works for any page size. Letter, A4, 16:9 deck,
  custom, controlled by the `@page` rule in the HTML's CSS.
---

# HTML to PDF

A two-stage rendering pipeline that turns a self-contained HTML file into a clean PDF.

1. **Vector pass**, headless Chrome prints the HTML to PDF. Text stays selectable, lines stay sharp at any zoom.
2. **Raster fallback (optional)**, for any specific page where the print engine renders the page differently from the live browser, replace just that page with a high-resolution screenshot. The rest of the PDF stays vector.

The combination is important. Vector-only fails on pages that use `mix-blend-mode`, certain gradient compositions, or absolutely-positioned children inside `overflow: hidden` flex parents. Screenshot-only loses crispness everywhere. The hybrid keeps quality high and only pays the raster cost where it has to.

---

## When to use

Trigger on language like:
- "render this HTML to PDF"
- "build a PDF from [file].html"
- "make a print version of this page"
- "the PDF looks wrong on slide N"
- "fix the broken page in the PDF"
- "convert this deck/one-pager/poster to PDF"

If the user has only a Markdown source or a description, this skill is downstream, they need to produce the HTML first (via whatever skill or hand-authoring fits the artifact).

---

## What you need

- A Chromium-based browser installed locally. The script auto-detects Chrome, Brave, Edge, Chromium, or Arc on macOS. On Linux/Windows it falls back to `google-chrome` / `chromium` / `chrome.exe` on `PATH`.
- Python 3 (only if you need the screenshot-replacement step). Pillow and pypdf get auto-installed on first run via `pip install --user`.
- A self-contained HTML file. External CDN fonts and images are fine; relative paths resolve against the HTML's own folder.

---

## Files in this skill

```
.claude/skills/html-to-pdf/
├── SKILL.md                           ← this file
└── scripts/
    ├── render-pdf.sh                  ← Stage 1: vector render
    ├── rebuild-pdf-with-screenshots.py ← Stage 2: hybrid raster fix-up
    └── page-template.html             ← minimal HTML scaffold with @page CSS
```

When you start work on a new artifact, copy the two scripts into the project folder alongside the HTML. They're designed to live next to the file they render so anyone in the repo can rebuild the PDF without touching the skill folder.

```bash
cp .claude/skills/html-to-pdf/scripts/render-pdf.sh path/to/project/
cp .claude/skills/html-to-pdf/scripts/rebuild-pdf-with-screenshots.py path/to/project/
chmod +x path/to/project/render-pdf.sh
```

---

## The HTML contract

For the PDF to come out at the right size, the HTML must declare the page size in CSS:

```css
@page {
  size: 13.333in 7.5in;   /* 16:9 landscape deck. Use 8.5in 11in for Letter, etc. */
  margin: 0;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

.page {
  width: 13.333in;
  height: 7.5in;
  page-break-after: always;
}
.page:last-child { page-break-after: auto; }

@media print {
  body { background: white; }
  .page { box-shadow: none; margin: 0; }
}
```

Each top-level page or slide should be a `.page` (or equivalent) sized to match `@page`. `page-break-after: always` forces the print engine to paginate cleanly.

`scripts/page-template.html` in this skill is a minimal copy of this scaffold. Use it as a starting point if you're authoring a brand-new artifact.

### Common page sizes

| Format | `@page size` |
|---|---|
| US Letter portrait | `8.5in 11in` |
| US Letter landscape | `11in 8.5in` |
| A4 portrait | `210mm 297mm` |
| 16:9 deck (1280×720 logical) | `13.333in 7.5in` |
| 16:9 deck (1920×1080 logical) | `20in 11.25in` |
| Square social post | `1080px 1080px` |

---

## Stage 1. Vector render

```bash
./render-pdf.sh input.html              # writes input.pdf next to it
./render-pdf.sh input.html output.pdf   # explicit output path
```

What the script does under the hood:

```bash
"$CHROME" \
  --headless \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf="$OUT" \
  --print-to-pdf-no-header \
  --no-margins \
  --hide-scrollbars \
  --virtual-time-budget=10000 \
  "file://$HTML"
```

The flag that matters most is `--virtual-time-budget=10000`. It tells Chrome to wait up to 10 seconds for fonts, images, and CSS to settle before snapshotting. Without it, web fonts often fall back to system fonts in the PDF even when they look fine in the browser.

`--no-margins` and `--no-pdf-header-footer` keep Chrome from injecting its own page chrome on top of your `@page` rule.

### Verifying the vector pass

Open the PDF, then open the HTML in the browser side by side. Compare each page. Look for:

- Fonts swapping to system fallbacks (a sign `--virtual-time-budget` wasn't long enough)
- Gradients flattening or shifting tone
- Elements with `mix-blend-mode` rendering as solid blocks
- Tall content getting clipped at a page boundary
- Background images shifting position
- Any `position: absolute` element appearing in the wrong place inside an `overflow: hidden` parent

If everything matches, you're done. Skip Stage 2.

---

## Stage 2. Screenshot replacement (only if needed)

When specific pages render wrong in the PDF but right in the browser, swap just those pages for high-res screenshots. The rest stay vector.

```bash
# Edit the config block at the top of the script first, then:
python3 rebuild-pdf-with-screenshots.py
```

The script accepts CLI args too:

```bash
python3 rebuild-pdf-with-screenshots.py \
  --html input.html \
  --pdf input.pdf \
  --slides 1,2,9 \
  --total 17 \
  --width 1280 \
  --height 720
```

### What the script does

1. Headless Chrome takes a single tall screenshot of the whole HTML at 2x device scale (so a 1280×720 logical page becomes 2560×1440 pixels, print-grade resolution).
2. It crops out each requested page from the tall screenshot using the page width/height plus the inter-page gap.
3. Each crop becomes a single-page PDF at 192 DPI (= 2x scale → matches the original page dimensions in inches).
4. It walks through every page slot in the existing PDF. For pages in `--slides`, it pulls in the screenshot version. For everything else, it keeps the vector page.
5. The output replaces the original PDF.

The result: pages you didn't flag stay sharp, selectable vectors. Pages you flagged are pixel-perfect to the browser at the cost of being raster (slightly soft at extreme zoom, not selectable text).

### Configuring the script

Open `rebuild-pdf-with-screenshots.py` and edit the constants at the top:

```python
SCREENSHOT_PAGES = [1, 2, 9]   # 1-indexed page numbers to replace
TOTAL_PAGES      = 17           # total page count of the PDF
HTML_NAME         = "your-file.html"
PDF_NAME          = "your-file.pdf"
WIDTH_LOGICAL     = 1280         # CSS pixel width of one page
HEIGHT_LOGICAL    = 720          # CSS pixel height of one page
GAP_LOGICAL       = 24           # screen-only margin between pages, 0 for print-style flow
SCALE             = 2            # device scale factor (2 = retina, ~192 DPI)
```

The CLI args override these, so you can leave the defaults pointing at the most common case for a project and pass overrides when needed.

### Picking the right WIDTH/HEIGHT/GAP

- WIDTH_LOGICAL × HEIGHT_LOGICAL must equal the CSS pixel size of one page in the browser. For an `@page` size of `13.333in × 7.5in` rendered at 96 CSS DPI, that's `1280 × 720`. For Letter portrait (`8.5in × 11in`) at 96 DPI, it's `816 × 1056`.
- GAP_LOGICAL is whatever vertical margin you use between pages on screen (`margin: 0 auto 24px auto` → `GAP = 24`). If pages are flush, set to 0.
- If the crops come out misaligned, the most common cause is a mismatch between the CSS page height and HEIGHT_LOGICAL. Measure a single page in DevTools (Computed → height) and use that exact value.

---

## End-to-end workflow

1. Author the HTML with the `@page` rule and per-page wrappers.
2. Open it in the browser. Scroll through. Confirm the design looks right.
3. Run `./render-pdf.sh input.html` to produce the vector PDF.
4. Open the PDF. Spot-check every page against the browser.
5. If everything matches: ship it.
6. If a few pages drifted: edit `SCREENSHOT_PAGES` in the Python script (or pass `--slides`), then run `python3 rebuild-pdf-with-screenshots.py`.
7. Open the rebuilt PDF. Confirm the previously-broken pages now match the browser.
8. Report: total page count, which pages got screenshot replacement and why, final file size.

---

## Gotchas

- **Web fonts not loading in the PDF.** Bump `--virtual-time-budget` higher (try 20000) or self-host the font files instead of relying on Google Fonts. Slow networks during `headless` mode can starve the font fetch.
- **`mix-blend-mode` always breaks the print engine.** If you need the effect, plan to use the screenshot replacement on those pages from the start. Don't fight it.
- **Tall content getting cut off.** The print engine paginates strictly at the `@page` size. Anything spilling past the page height clips. Make page wrappers fixed-height with `overflow: hidden` so the design fails loudly in the browser too, not silently in the PDF.
- **Header injection at the top of the page.** If you see Chrome's URL/timestamp printed on the PDF, you're missing one of `--no-pdf-header-footer` / `--print-to-pdf-no-header` / `--no-margins`.
- **Wrong page count after Stage 2.** The screenshot script trusts `TOTAL_SLIDES`. If you add or remove pages from the HTML, update that constant or the rebuild silently drops/duplicates pages.
- **Linux: Chrome path not found.** The script tries `google-chrome`, `chromium`, and `chromium-browser` on `PATH`. Install whichever your distro uses or set `CHROME_BIN=/path/to/chrome` before calling.
- **Windows: untested under WSL.** The macOS app paths obviously don't apply. Set `CHROME_BIN` to the Windows Chrome executable or run from a Linux/Mac machine.

---

## Output contract

When the skill completes there should be:

- `<project>/<name>.html`, the source HTML (untouched)
- `<project>/<name>.pdf`, the rendered PDF (vector, with optional raster pages spliced in)
- `<project>/render-pdf.sh`, copy of the render script
- `<project>/rebuild-pdf-with-screenshots.py`, copy of the screenshot-replacement script

Report back to the user with:
- Path to the final PDF
- Total page count
- Which pages (if any) got screenshot replacement and why
- Final file size
