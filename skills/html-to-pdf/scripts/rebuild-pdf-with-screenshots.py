#!/usr/bin/env python3
"""
Rebuild a PDF with selected pages replaced by high-res screenshots of the
HTML (as Chrome renders it in a real browser). All other pages stay as the
original vector-rendered PDF pages.

Use this as a fallback for pages where the headless print pipeline renders
something different from the live browser (mix-blend-mode, certain gradient
compositions, position:absolute children inside overflow:hidden flex parents,
very tall children, etc.).

Two ways to configure:
  1. Edit the CONFIG block below, then: python3 rebuild-pdf-with-screenshots.py
  2. Pass CLI args (each overrides the corresponding CONFIG value):

     python3 rebuild-pdf-with-screenshots.py \
       --html input.html \
       --pdf  input.pdf  \
       --slides 1,2,9    \
       --total 17        \
       --width 1280      \
       --height 720      \
       --gap 24          \
       --scale 2

WIDTH and HEIGHT are the CSS pixel dimensions of one page (96 CSS DPI). For
@page size 13.333in x 7.5in -> 1280 x 720. For Letter portrait -> 816 x 1056.
GAP is the on-screen vertical margin between pages (use 0 if pages are flush).
SCALE is the device scale factor for the screenshot; 2 yields ~192 DPI in the
final PDF and prints crisply.

CHROME_BIN env var overrides browser auto-detection.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

# ============================================================================
# CONFIG (edit these defaults, or override via CLI)
# ============================================================================
HTML_NAME       = "index.html"
PDF_NAME        = "index.pdf"
SCREENSHOT_PAGES: list[int] = []   # 1-indexed page numbers to replace
TOTAL_PAGES     = 0                # total pages in the PDF (must match!)
WIDTH_LOGICAL   = 1280             # CSS pixel width of one page
HEIGHT_LOGICAL  = 720              # CSS pixel height of one page
GAP_LOGICAL     = 24               # screen-only margin between pages (0 if flush)
SCALE           = 2                # device scale factor (2 = retina ~192 DPI)
# ============================================================================


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--html",   default=None, help="Path to source HTML")
    p.add_argument("--pdf",    default=None, help="Path to existing PDF (will be replaced)")
    p.add_argument("--slides", default=None, help="Comma-separated 1-indexed page numbers to replace, e.g. 1,2,9")
    p.add_argument("--total",  type=int, default=None, help="Total page count of the PDF")
    p.add_argument("--width",  type=int, default=None, help="CSS pixel width of one page")
    p.add_argument("--height", type=int, default=None, help="CSS pixel height of one page")
    p.add_argument("--gap",    type=int, default=None, help="Screen-only margin between pages (CSS px)")
    p.add_argument("--scale",  type=int, default=None, help="Device scale factor (2 recommended)")
    return p.parse_args()


def ensure(pkg: str, import_name: str | None = None) -> None:
    """Install a pip package on first run if missing."""
    import_name = import_name or pkg
    try:
        __import__(import_name)
    except ImportError:
        print(f"Installing {pkg}...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "--user", "--quiet", pkg]
        )
        import site
        site.main()


def find_chrome() -> str:
    env = os.environ.get("CHROME_BIN")
    if env and Path(env).exists():
        return env

    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Arc.app/Contents/MacOS/Arc",
    ]
    for c in candidates:
        if Path(c).exists():
            return c

    from shutil import which
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        path = which(name)
        if path:
            return path

    sys.exit(
        "No Chromium-based browser found. "
        "Install Chrome/Brave/Edge/Chromium or set CHROME_BIN=/path/to/chrome."
    )


def main() -> None:
    args = parse_args()
    here = Path(__file__).parent.resolve()

    html_name        = args.html   or HTML_NAME
    pdf_name         = args.pdf    or PDF_NAME
    width_logical    = args.width  or WIDTH_LOGICAL
    height_logical   = args.height or HEIGHT_LOGICAL
    gap_logical      = GAP_LOGICAL if args.gap is None else args.gap
    scale            = args.scale  or SCALE
    total_pages      = args.total  or TOTAL_PAGES

    if args.slides is not None:
        screenshot_pages = [int(x) for x in args.slides.split(",") if x.strip()]
    else:
        screenshot_pages = list(SCREENSHOT_PAGES)

    if not screenshot_pages:
        sys.exit("No pages to replace. Set SCREENSHOT_PAGES in the CONFIG block or pass --slides.")
    if total_pages <= 0:
        sys.exit("TOTAL_PAGES is unset. Set it in the CONFIG block or pass --total.")

    # Resolve files (allow absolute or relative to script directory).
    html_path = Path(html_name)
    if not html_path.is_absolute():
        html_path = here / html_path
    pdf_path = Path(pdf_name)
    if not pdf_path.is_absolute():
        pdf_path = here / pdf_path

    if not html_path.exists():
        sys.exit(f"HTML not found: {html_path}")
    if not pdf_path.exists():
        sys.exit(f"Existing PDF not found: {pdf_path}. Run render-pdf.sh first.")

    tmp = pdf_path.parent / ".pdf-build"
    tmp.mkdir(exist_ok=True)

    # ----- Dependencies (lazy) ----------------------------------------------
    ensure("Pillow", "PIL")
    ensure("pypdf", "pypdf")

    from PIL import Image
    from pypdf import PdfReader, PdfWriter

    chrome = find_chrome()

    # ----- Step 1: Full-page screenshot of the HTML ------------------------
    page_h = height_logical
    page_gap = gap_logical
    # Total scroll height that contains every page + gaps + safety margin.
    full_height = total_pages * (page_h + page_gap) + 200
    full_png = tmp / "full.png"

    print(f"Step 1: Full-page screenshot via headless Chrome ({chrome})...")
    subprocess.run(
        [
            chrome,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--force-device-scale-factor={scale}",
            f"--window-size={width_logical},{full_height}",
            "--virtual-time-budget=10000",
            f"--screenshot={full_png}",
            f"file://{html_path}",
        ],
        check=True,
    )

    full = Image.open(full_png)
    print(f"  Full screenshot size: {full.size}")

    # ----- Step 2: Crop each requested page out of the tall screenshot ------
    print(f"Step 2: Cropping pages {screenshot_pages}...")
    slide_w_px = width_logical * scale
    slide_h_px = height_logical * scale
    gap_px     = gap_logical * scale

    page_pngs: dict[int, Path] = {}
    for n in screenshot_pages:
        if n < 1 or n > total_pages:
            sys.exit(f"Page {n} out of range (1..{total_pages})")
        idx = n - 1
        top = idx * (slide_h_px + gap_px)
        bottom = top + slide_h_px
        crop = full.crop((0, top, slide_w_px, bottom))
        out = tmp / f"page-{n}.png"
        crop.save(out, "PNG")
        page_pngs[n] = out
        print(f"  Saved page {n}: {out.name}")

    # ----- Step 3: Convert each PNG to a single-page PDF at correct DPI -----
    # Page width in inches = slide_w_px / dpi  ==>  dpi = scale * 96
    dpi = float(scale * 96)
    print(f"Step 3: Converting screenshots to single-page PDFs at {dpi:.0f} DPI...")
    page_pdfs: dict[int, Path] = {}
    for n, png in page_pngs.items():
        out = tmp / f"page-{n}.pdf"
        Image.open(png).convert("RGB").save(out, "PDF", resolution=dpi)
        page_pdfs[n] = out

    # ----- Step 4: Splice screenshot pages into the existing PDF ------------
    print("Step 4: Splicing screenshots into the existing PDF...")
    existing = PdfReader(str(pdf_path))
    if len(existing.pages) != total_pages:
        print(
            f"  WARNING: existing PDF has {len(existing.pages)} pages but "
            f"--total={total_pages}. Continuing, verify the output."
        )

    writer = PdfWriter()
    screenshot_readers = {n: PdfReader(str(p)) for n, p in page_pdfs.items()}

    for n in range(1, total_pages + 1):
        if n in screenshot_pages:
            writer.add_page(screenshot_readers[n].pages[0])
        else:
            # Existing PDF is 0-indexed; page N is at index N-1
            if n - 1 < len(existing.pages):
                writer.add_page(existing.pages[n - 1])

    final_tmp = tmp / "final.pdf"
    with open(final_tmp, "wb") as f:
        writer.write(f)
    final_tmp.replace(pdf_path)

    vector_pages = [n for n in range(1, total_pages + 1) if n not in screenshot_pages]
    print(f"\nDone. Final PDF: {pdf_path}")
    print(f"Total pages: {len(writer.pages)}")
    print(f"  Screenshot pages: {screenshot_pages}")
    print(f"  Vector pages:     {vector_pages}")


if __name__ == "__main__":
    main()
