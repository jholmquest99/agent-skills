#!/usr/bin/env bash
#
# Render an HTML file to PDF using headless Chrome.
#
# Usage:
#   ./render-pdf.sh input.html              # writes input.pdf next to the HTML
#   ./render-pdf.sh input.html output.pdf   # explicit output path
#
# Page size and margins are controlled by the HTML's own CSS via @page.
# This script intentionally passes --no-margins and disables Chrome's
# print headers/footers so your CSS is the sole source of truth.
#
# Override the browser binary via CHROME_BIN if auto-detection fails:
#   CHROME_BIN=/path/to/chrome ./render-pdf.sh input.html

set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <input.html> [output.pdf]"
  exit 1
fi

HTML_ARG="$1"
if [[ ! -f "$HTML_ARG" ]]; then
  echo "HTML file not found: $HTML_ARG"
  exit 1
fi

# Resolve to an absolute path so file:// works regardless of cwd.
HTML="$(cd "$(dirname "$HTML_ARG")" && pwd)/$(basename "$HTML_ARG")"

if [[ $# -ge 2 ]]; then
  OUT="$2"
else
  OUT="${HTML%.html}.pdf"
  OUT="${OUT%.htm}.pdf"
fi

# ---------------------------------------------------------------------------
# Locate a Chromium-based browser.
# ---------------------------------------------------------------------------
CHROME="${CHROME_BIN:-}"

if [[ -z "$CHROME" ]]; then
  for candidate in \
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
    "/Applications/Chromium.app/Contents/MacOS/Chromium" \
    "/Applications/Arc.app/Contents/MacOS/Arc"
  do
    if [[ -x "$candidate" ]]; then
      CHROME="$candidate"
      break
    fi
  done
fi

if [[ -z "$CHROME" ]]; then
  for name in google-chrome google-chrome-stable chromium chromium-browser chrome; do
    if command -v "$name" >/dev/null 2>&1; then
      CHROME="$(command -v "$name")"
      break
    fi
  done
fi

if [[ -z "$CHROME" ]]; then
  echo "Could not find a Chromium-based browser."
  echo "Install Chrome / Brave / Edge / Chromium, or set CHROME_BIN=/path/to/chrome."
  exit 1
fi

echo "Rendering with: $CHROME"
echo "Input:  $HTML"
echo "Output: $OUT"

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

echo ""
echo "Done. PDF saved to:"
echo "  $OUT"
