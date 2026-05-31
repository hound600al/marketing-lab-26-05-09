"""Generate V26 portfolio PDF (1920×1080 per page, 17 slides).

Strategy:
1. Copy portfolio.html (= v26 deck, 17 slides) → _v26_print.html
2. Inject @page + .slide page-break CSS so each slide = 1 PDF page
3. Disable responsive scale (transform: scale → none) so slide renders at 1920×1080 raw
4. Run Chrome headless with --print-to-pdf
"""
import re
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "portfolio.html"  # = v26 그로스 결과물, 17 슬라이드
PRINT_HTML = HERE / "_v26_print.html"
PDF_OUT = HERE / "이도형_그로스마케터_포트폴리오_v26.pdf"

text = SRC.read_text(encoding="utf-8")

# Print-only CSS: each slide = 1 PDF page, disable scale, white background
PRINT_CSS = """
<style>
@media print {
  @page { size: 1920px 1080px; margin: 0; }
  html, body {
    background: #fff !important;
    width: 1920px !important;
    overflow: visible !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  body {
    display: block !important;
    align-items: stretch !important;
    gap: 0 !important;
  }
  :root { --slide-scale: 1 !important; }
  .slide {
    transform: none !important;
    margin: 0 !important;
    width: 1920px !important;
    height: 1080px !important;
    page-break-after: always !important;
    break-after: page !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  .slide:last-child {
    page-break-after: auto !important;
    break-after: auto !important;
  }
  /* hide any non-slide chrome (none expected, defensive) */
  body > :not(.slide) { display: none !important; }
}
</style>
"""

# Inject print CSS right before </head>
text = text.replace("</head>", PRINT_CSS + "</head>", 1)
PRINT_HTML.write_text(text, encoding="utf-8")
print(f"wrote {PRINT_HTML}: {len(text):,} chars")

# Run Chrome headless --print-to-pdf
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
src_url = PRINT_HTML.resolve().as_uri()
out_path = str(PDF_OUT.resolve())

cmd = [
    CHROME,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--no-margins",
    "--virtual-time-budget=10000",  # let fonts/images load
    f"--print-to-pdf={out_path}",
    src_url,
]
print("running:", " ".join(cmd))
result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
print("STDOUT:", result.stdout[:500])
print("STDERR:", result.stderr[:500])

if PDF_OUT.exists():
    print(f"\nwrote PDF: {PDF_OUT}")
    print(f"size: {PDF_OUT.stat().st_size:,} bytes")
else:
    print("\nPDF generation FAILED")
