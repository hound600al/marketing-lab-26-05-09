"""One-shot patch: v26.html source의 p11 (T-ROAS) 슬라이드를 새 인사이트로 교체.

새 인사이트 (Notion 36a5e589dc9f81de99b1c52e2f5718d9):
- 정적 가치 우회로 시도한 AOS 고가치 모객
- 25.04~26.04 12개월 운영 후 매출 미연동 한계로 OFF
- 집행액 정점: 26.01 ₩4,338만
- iOS 재주문 M+1 ~60% > AOS ~54% (4~6%p) → OS-수준 고가치 검증
- AOS M+1은 T-ROAS 집행 시기에도 54~57% 안정 (집행액과 약한 양의 관계)

cat-meta "02 / 02"는 그대로 유지 (build script SUBCOUNTER_REWRITES가 02/03·02/04로 변환).
"""
from __future__ import annotations
import re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "이도형_포트폴리오_v26.html"

NEW_TROAS_SLIDE = '''<!-- ══════ p11  PERFORMANCE ② T-ROAS 정적 가치 (매출 미연동 한계로 OFF) ══════ -->
<div class="slide" id="p11">
  <div class="grid-bg light"></div>
  <div class="hd-tight">
    <div>
      <div class="cat-row">
        <span class="cat-chip" style="background:var(--ca-perf);"><span class="ko">퍼포먼스</span><span class="en">Performance · Google Ads</span></span>
        <span class="cat-meta"><b>02 / 02</b> · T-ROAS</span>
      </div>
      <div class="page-title">구글애즈 T-ROAS — 매출 신호 빈 상태에서 <em>정적 가치로 우회</em>, 12개월 운영 후 OFF</div>
    </div>
    <span class="slide-num">10 / 16</span>
  </div>

  <div class="body2">
    <div class="col-l">
      <div class="tag-row">
        <span class="c-badge" style="background:var(--ca-perf);">Performance · Google Ads · T-ROAS</span>
        <span class="c-badge outline">커버링 · 2025.04~2026.04 · 12개월 운영</span>
      </div>
      <div class="p-title">CPA 최적화는 건수만 통제 —<br><em>누가 더 비싼 주문을 할지</em>는 가르지 못한다</div>

      <div class="phase b1"><span class="ptag">병목</span>매출 신호가 비어 '가치 기반 입찰'이 불가능</div>
      <div class="sec tight"><ul>
        <li>CPA 최적화는 전환 <em>건수</em>만 통제 → ARPU·리텐션 학습 불가. 구글 AE가 T-ROAS(전환가치 최적화) 제안</li>
        <li>그런데 자사 DB 매출이 <strong>Airbridge <code style="font-family:var(--font-mono);font-size:13px;background:var(--cobalt-soft);padding:1px 6px;border-radius:3px;">order_complete</code>로 미전달</strong> → 가치 신호 0원, 알고리즘이 학습할 게 없음</li>
      </ul></div>

      <div class="phase b2"><span class="ptag">실행</span>정적 가치(static value)로 상대적 가치 차이만이라도 학습시키기</div>
      <div class="sec tight"><ul>
        <li>회원가입 <strong>₩5,000</strong> · 구매 <strong>₩33,000</strong>(이후 ₩30,000) 정적 부여 — 가입과 구매의 <em>상대적 가치 차이</em>를 알고리즘이 학습</li>
        <li>캠페인 <code style="font-family:var(--font-mono);font-size:13px;background:var(--cobalt-soft);padding:1px 6px;border-radius:3px;">uac_aos_purchase_aim_(복합소구)_25.04.23</code>에 T-ROAS 입찰 적용, 타깃 ROAS 55% → 50%로 튜닝</li>
      </ul></div>

      <div class="phase b3"><span class="ptag">결과</span>OS-수준 고가치는 검증, 그러나 매출 미연동 벽을 못 넘고 26.04 OFF</div>
      <div class="sec tight"><ul>
        <li>집행액 정점 <strong>26.01 ₩4,338만</strong> → 26.02 ₩1,215만 → 26.03 ₩517만 → <strong>26.04 OFF</strong></li>
        <li>코호트 검증 — iOS 재주문 M+1 <strong>~60%</strong> > AOS <strong>~54%</strong> (4~6%p 일관 우위) · OS 단위로 iOS가 재구매에서도 고가치임을 데이터로 확인</li>
        <li>AOS M+1은 T-ROAS 집행 내내 <strong>54~57% 밴드 안정</strong> · 집행액과의 강한 양의 관계는 없음 (약한 양의 관계만)</li>
      </ul></div>

      <div class="result">
        <div class="kpi"><span class="kpi-num">₩4,338만</span><span class="kpi-label">집행 정점 (26.01 · 12개월 운영)</span></div>
        <div class="kpi"><span class="kpi-num">+4~6%p</span><span class="kpi-label">iOS 재주문 M+1, AOS 대비</span></div>
        <div class="kpi"><span class="kpi-num">OFF</span><span class="kpi-label">26.04 · 매출 미연동 한계로 종료</span></div>
      </div>
    </div>

    <div class="col-r">
      <!-- 상단: T-ROAS 집행액(막대) vs AOS·iOS 재주문 M+1(라인) -->
      <div class="chart-card" style="flex:none;display:flex;flex-direction:column;padding:14px 18px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
          <div class="chart-title" style="margin-bottom:0;">T-ROAS 집행액(막대) vs OS별 재주문 M+1(라인) — 25.06~26.04</div>
          <span style="font-family:var(--font-mono);font-size:10px;color:var(--sub);letter-spacing:.06em;">Airbridge · order_complete → order_complete · general</span>
        </div>
        <svg viewBox="0 0 720 280" width="100%" style="display:block;">
          <defs>
            <linearGradient id="bar_spend" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#5B9BD5" stop-opacity=".85"/><stop offset="100%" stop-color="#5B9BD5" stop-opacity=".4"/></linearGradient>
          </defs>
          <!-- y grid (left axis: 집행액, 0~5000만, 1cm=200px usable) -->
          <line x1="50" y1="40" x2="670" y2="40" stroke="#F1F4F9"/><text x="45" y="44" font-size="9" fill="#8B95A6" text-anchor="end" font-family="JetBrains Mono">5,000만</text>
          <line x1="50" y1="90" x2="670" y2="90" stroke="#F1F4F9"/><text x="45" y="94" font-size="9" fill="#8B95A6" text-anchor="end" font-family="JetBrains Mono">3,750만</text>
          <line x1="50" y1="140" x2="670" y2="140" stroke="#F1F4F9"/><text x="45" y="144" font-size="9" fill="#8B95A6" text-anchor="end" font-family="JetBrains Mono">2,500만</text>
          <line x1="50" y1="190" x2="670" y2="190" stroke="#F1F4F9"/><text x="45" y="194" font-size="9" fill="#8B95A6" text-anchor="end" font-family="JetBrains Mono">1,250만</text>
          <line x1="50" y1="240" x2="670" y2="240" stroke="#E2E6EF" stroke-width="1.5"/>
          <!-- right axis: 재주문 M+1, 40~80% -->
          <text x="675" y="44" font-size="9" fill="#C0392B" text-anchor="start" font-family="JetBrains Mono">80%</text>
          <text x="675" y="140" font-size="9" fill="#C0392B" text-anchor="start" font-family="JetBrains Mono">60%</text>
          <text x="675" y="240" font-size="9" fill="#C0392B" text-anchor="start" font-family="JetBrains Mono">40%</text>

          <!-- bars: 11 months, width 38, gap 16
               x range 60~660 (=600 / 11 = ~55), bar每 width 38, gap 16 → 11×(38+16) = 594
               spend max 5000만, y = 240 - val/5000 * 200
               25.06 1065→197.4
               25.07 3865→85.4
               25.08 3126→114.96
               25.09 2898→124.08
               25.10 4871→45.16 (peak)
               25.11 3312→107.52
               25.12 3334→106.64
               26.01 4338→66.48 (정점 ₩4,338만)
               26.02 1215→191.4
               26.03 517→219.32
               26.04 0→240 -->
          <rect x="60"  y="197.4" width="38" height="42.6"  rx="3" fill="url(#bar_spend)"/>
          <rect x="116" y="85.4"  width="38" height="154.6" rx="3" fill="url(#bar_spend)"/>
          <rect x="172" y="114.96" width="38" height="125.04" rx="3" fill="url(#bar_spend)"/>
          <rect x="228" y="124.08" width="38" height="115.92" rx="3" fill="url(#bar_spend)"/>
          <rect x="284" y="45.16" width="38" height="194.84" rx="3" fill="url(#bar_spend)"/>
          <rect x="340" y="107.52" width="38" height="132.48" rx="3" fill="url(#bar_spend)"/>
          <rect x="396" y="106.64" width="38" height="133.36" rx="3" fill="url(#bar_spend)"/>
          <rect x="452" y="66.48" width="38" height="173.52" rx="3" fill="#0F19D8"/>
          <rect x="508" y="191.4"  width="38" height="48.6"  rx="3" fill="url(#bar_spend)"/>
          <rect x="564" y="219.32" width="38" height="20.68" rx="3" fill="url(#bar_spend)"/>
          <rect x="620" y="238"    width="38" height="2"     rx="1" fill="#C7CBE3"/>

          <!-- spend value labels (key) -->
          <text x="303" y="40" font-size="10" fill="#0F19D8" font-weight="700" text-anchor="middle" font-family="JetBrains Mono">4,871</text>
          <text x="471" y="61" font-size="11" fill="#0F19D8" font-weight="900" text-anchor="middle" font-family="JetBrains Mono">4,338 ★</text>
          <text x="639" y="234" font-size="9" fill="#C0392B" font-weight="800" text-anchor="middle" font-family="JetBrains Mono">OFF</text>

          <!-- Right scale lines/area for retention (line chart layer) -->
          <!-- iOS M+1 (green): val 40-80% → y = 240 - (val-40)/40 * 200
               25.06 71.7 → 80.8 (high)
               25.07 60.8 → 136 → 136
               actually: y = 240 - (val-40)/40 * 200 = 240 - 5*(val-40)
               71.7: 240 - 5*31.7 = 240 - 158.5 = 81.5
               60.8: 240 - 5*20.8 = 240 - 104 = 136
               59.2: 240 - 5*19.2 = 240 - 96 = 144
               60.5: 240 - 5*20.5 = 240 - 102.5 = 137.5
               59.2: 144
               62.6: 240 - 5*22.6 = 240 - 113 = 127
               59.1: 240 - 5*19.1 = 240 - 95.5 = 144.5
               60.1: 240 - 5*20.1 = 240 - 100.5 = 139.5
               60.5: 137.5
               59.6: 240 - 5*19.6 = 240 - 98 = 142 -->
          <polyline points="79,81.5 135,136 191,144 247,137.5 303,144 359,127 415,144.5 471,139.5 527,137.5 583,142"
                    fill="none" stroke="#1A9054" stroke-width="2.5" stroke-linejoin="round"/>
          <!-- circles for iOS -->
          <circle cx="79" cy="81.5" r="3.5" fill="#1A9054"/>
          <circle cx="135" cy="136" r="3.5" fill="#1A9054"/>
          <circle cx="191" cy="144" r="3.5" fill="#1A9054"/>
          <circle cx="247" cy="137.5" r="3.5" fill="#1A9054"/>
          <circle cx="303" cy="144" r="3.5" fill="#1A9054"/>
          <circle cx="359" cy="127" r="3.5" fill="#1A9054"/>
          <circle cx="415" cy="144.5" r="3.5" fill="#1A9054"/>
          <circle cx="471" cy="139.5" r="4.5" fill="#1A9054" stroke="#fff" stroke-width="1.5"/>
          <circle cx="527" cy="137.5" r="3.5" fill="#1A9054"/>
          <circle cx="583" cy="142" r="3.5" fill="#1A9054"/>

          <!-- AOS M+1 (red):
               68.1 → 240 - 5*28.1 = 99.5
               53.7 → 240 - 5*13.7 = 171.5
               53.8 → 171
               57.1 → 154.5
               53.9 → 170.5
               56.1 → 159.5
               54.4 → 168
               56.5 → 157.5
               54.8 → 166
               51.7 → 181.5 -->
          <polyline points="79,99.5 135,171.5 191,171 247,154.5 303,170.5 359,159.5 415,168 471,157.5 527,166 583,181.5"
                    fill="none" stroke="#C0392B" stroke-width="2.5" stroke-linejoin="round"/>
          <circle cx="79" cy="99.5" r="3.5" fill="#C0392B"/>
          <circle cx="135" cy="171.5" r="3.5" fill="#C0392B"/>
          <circle cx="191" cy="171" r="3.5" fill="#C0392B"/>
          <circle cx="247" cy="154.5" r="3.5" fill="#C0392B"/>
          <circle cx="303" cy="170.5" r="3.5" fill="#C0392B"/>
          <circle cx="359" cy="159.5" r="3.5" fill="#C0392B"/>
          <circle cx="415" cy="168" r="3.5" fill="#C0392B"/>
          <circle cx="471" cy="157.5" r="4.5" fill="#C0392B" stroke="#fff" stroke-width="1.5"/>
          <circle cx="527" cy="166" r="3.5" fill="#C0392B"/>
          <circle cx="583" cy="181.5" r="3.5" fill="#C0392B"/>

          <!-- vertical: 26.01 정점 marker -->
          <line x1="471" y1="32" x2="471" y2="240" stroke="#B3DA1C" stroke-width="1.3" stroke-dasharray="3,4"/>
          <rect x="430" y="14" width="82" height="16" rx="3" fill="#0A0F2E"/>
          <text x="471" y="26" font-size="10" fill="#D6FF3D" font-weight="800" text-anchor="middle" font-family="JetBrains Mono">★ 26.01 집행 정점</text>
          <line x1="639" y1="32" x2="639" y2="240" stroke="#C0392B" stroke-width="1.3" stroke-dasharray="3,4"/>
          <rect x="603" y="14" width="72" height="16" rx="3" fill="#C0392B"/>
          <text x="639" y="26" font-size="10" fill="#fff" font-weight="800" text-anchor="middle" font-family="JetBrains Mono">26.04 OFF</text>

          <!-- X labels -->
          <text x="79"  y="258" font-size="9" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">25.06</text>
          <text x="135" y="258" font-size="9" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">07</text>
          <text x="191" y="258" font-size="9" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">08</text>
          <text x="247" y="258" font-size="9" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">09</text>
          <text x="303" y="258" font-size="9" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">10</text>
          <text x="359" y="258" font-size="9" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">11</text>
          <text x="415" y="258" font-size="9" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">12</text>
          <text x="471" y="258" font-size="9" fill="#0F172A" font-weight="800" text-anchor="middle" font-family="JetBrains Mono">26.01</text>
          <text x="527" y="258" font-size="9" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">02</text>
          <text x="583" y="258" font-size="9" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">03</text>
          <text x="639" y="258" font-size="9" fill="#C0392B" font-weight="800" text-anchor="middle" font-family="JetBrains Mono">04</text>

          <!-- Legend -->
          <rect x="60" y="266" width="14" height="8" fill="url(#bar_spend)"/>
          <text x="78" y="273" font-size="9" fill="#5B6675" font-family="JetBrains Mono">T-ROAS 집행액 (좌)</text>
          <rect x="200" y="269" width="14" height="2.5" fill="#1A9054"/>
          <text x="218" y="273" font-size="9" fill="#5B6675" font-family="JetBrains Mono">iOS 재주문 M+1 (우)</text>
          <rect x="350" y="269" width="14" height="2.5" fill="#C0392B"/>
          <text x="368" y="273" font-size="9" fill="#5B6675" font-family="JetBrains Mono">AOS 재주문 M+1 (우)</text>
          <text x="555" y="273" font-size="9" fill="#0F172A" font-weight="700" text-anchor="middle" font-family="JetBrains Mono">★ AOS 54~57% 밴드 안정</text>
        </svg>
      </div>

      <!-- 하단: 왜 OFF 했나 — 한계 3가지 -->
      <div class="chart-card" style="flex:1;min-height:0;display:flex;flex-direction:column;padding:14px 18px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
          <div class="chart-title" style="margin-bottom:0;">왜 T-ROAS를 지속하지 못하고 OFF했나 — 한계 3가지</div>
          <span style="font-family:var(--font-mono);font-size:10px;color:var(--sub);letter-spacing:.08em;">Retrospective · 2026.04</span>
        </div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;flex:1;min-height:0;">
          <div style="background:#fff;border:1px solid var(--line);border-radius:10px;padding:11px 13px;display:flex;flex-direction:column;gap:5px;position:relative;overflow:hidden;">
            <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--red,#EF4444);"></div>
            <div style="font-family:var(--font-mono);font-size:10px;font-weight:800;letter-spacing:.12em;color:#C0392B;text-transform:uppercase;">① 정적 가치 = 상수</div>
            <div style="font-size:12px;color:var(--text2);line-height:1.5;font-weight:600;">모든 유저에 동일한 고정값 → "누가 더 비싼 주문을 하는지"를 알고리즘이 학습 불가</div>
          </div>
          <div style="background:#fff;border:1px solid var(--line);border-radius:10px;padding:11px 13px;display:flex;flex-direction:column;gap:5px;position:relative;overflow:hidden;">
            <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--red,#EF4444);"></div>
            <div style="font-family:var(--font-mono);font-size:10px;font-weight:800;letter-spacing:.12em;color:#C0392B;text-transform:uppercase;">② 실제 매출 미연동</div>
            <div style="font-size:12px;color:var(--text2);line-height:1.5;font-weight:600;"><code style="font-family:var(--font-mono);font-size:11px;">order_complete</code> revenue가 비어 tROAS·SKAN이 0원 기반 동작. SDK value + S2S 개발팀 요청 중</div>
          </div>
          <div style="background:#fff;border:1px solid var(--line);border-radius:10px;padding:11px 13px;display:flex;flex-direction:column;gap:5px;position:relative;overflow:hidden;">
            <div style="position:absolute;top:0;left:0;right:0;height:2px;background:var(--red,#EF4444);"></div>
            <div style="font-family:var(--font-mono);font-size:10px;font-weight:800;letter-spacing:.12em;color:#C0392B;text-transform:uppercase;">③ 전환가치 입찰 실적 한계</div>
            <div style="font-size:12px;color:var(--text2);line-height:1.5;font-weight:600;">일부 캠페인은 25.11 tCPA로 전환, 복합소구 T-ROAS도 26.02부터 축소 → 26.04 OFF, 예산을 tCPA 엄마소구로 이전</div>
          </div>
        </div>
        <div style="margin-top:auto;padding-top:10px;font-family:var(--font-mono);font-size:11px;color:var(--text2);line-height:1.55;">
          💡 <strong style="color:var(--text);">레슨런 — 가치 기반 입찰은 실제 매출이 이벤트로 정확히 연동돼야 성립.</strong> 정적 가치는 그 전까지의 임시방편. <span style="color:var(--green-dark,#0E9E76);">다음 과제는 DB 매출을 Airbridge SDK value + S2S로 연동해 <strong>동적 가치(dynamic value)</strong> 전환.</span>
        </div>
      </div>
    </div>
  </div>
  <div class="chrome"><span><b>10</b> / 16</span><span>Performance · T-ROAS · 정적 가치 우회 · 12개월 운영 후 OFF</span></div>
</div>'''

text = SRC.read_text(encoding="utf-8")

# 기존 p11 슬라이드 블록의 시작/끝 위치 탐지
# 시작: <!-- ══════ p11 ... 코멘트가 있으면 그것부터, 없으면 <div ... id="p11">
start_marker = re.search(r'<!-- [═]+ p11 .*?-->\n<div class="slide" id="p11">', text)
if start_marker:
    start = start_marker.start()
else:
    m = re.search(r'<div class="slide" id="p11">', text)
    start = m.start()

# 끝: balanced <div>...</div>
i = text.find('<div class="slide" id="p11">', start)
depth = 0
while i < len(text):
    if text.startswith('<div', i):
        depth += 1; i += 4
    elif text.startswith('</div>', i):
        depth -= 1; i += 6
        if depth == 0:
            break
    else:
        i += 1
end = i

old_block_len = end - start
new_text = text[:start] + NEW_TROAS_SLIDE + text[end:]
SRC.write_text(new_text, encoding="utf-8")
print(f"replaced p11 block: {old_block_len:,} → {len(NEW_TROAS_SLIDE):,} chars")
print(f"file: {len(new_text):,} chars")
