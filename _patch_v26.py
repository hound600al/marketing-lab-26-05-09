"""Patch v26 (portfolio.html + 이도형_포트폴리오_v26.html) Web2App slide with v27 실측 numbers.

v26의 9번 슬라이드(id=p10) Web2App 본문에 옛 수치(AOS CVR 19.47%, 매출 +187%, 7,534건 등)가
남아 있어, v27의 실측 본문(CPA -51.8%, CVR 2배, ROAS 2.1배)으로 교체.

v27 본문을 그대로 가져와 v26 페이지 번호로 변환:
- slide-num: 04 / 16 → 09 / 16
- chrome <b>04</b> → <b>09</b>
- cat-meta 01 / 03 (퍼포먼스 trio) → 01 / 02 (v26은 퍼포먼스 듀오)
"""
from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).parent

# 1) v27 build script에서 WEB2APP_SLIDE 본문 추출
src = (HERE / "_build_v27.py").read_text(encoding="utf-8")
m = re.search(r"WEB2APP_SLIDE = '''(.*?)'''", src, re.DOTALL)
if not m:
    raise SystemExit("WEB2APP_SLIDE constant not found in _build_v27.py")
new_block = m.group(1)

# 2) v26 페이지 번호 / sub-counter로 조정
new_block = new_block.replace(
    "<b>01 / 03</b> · Web2App", "<b>01 / 02</b> · Web2App"
)
new_block = new_block.replace(
    '<span class="slide-num">04 / 16</span>',
    '<span class="slide-num">09 / 16</span>',
)
new_block = new_block.replace(
    "<span><b>04</b> / 16</span>", "<span><b>09</b> / 16</span>"
)


def find_block_end(text: str, start: int) -> int:
    depth = 0
    i = start
    while i < len(text):
        if text.startswith("<div", i):
            depth += 1
            i += 4
        elif text.startswith("</div>", i):
            depth -= 1
            i += 6
            if depth == 0:
                return i
        else:
            i += 1
    raise RuntimeError(f"Unbalanced <div> from offset {start}")


# 3) 대상 파일들에 패치 적용
TARGETS = ["portfolio.html", "이도형_포트폴리오_v26.html"]
for fn in TARGETS:
    p = HERE / fn
    text = p.read_text(encoding="utf-8")
    open_match = re.search(r'<div class="slide" id="p10">', text)
    if not open_match:
        raise SystemExit(f"p10 not found in {fn}")
    start = open_match.start()
    end = find_block_end(text, start)
    text = text[:start] + new_block + text[end:]
    p.write_text(text, encoding="utf-8")
    print(f"patched {fn}: {len(text):,} bytes")
