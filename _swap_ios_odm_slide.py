"""Replace IOS_ODM_SLIDE constant in _build_v27.py with new insight body.

New insight (Notion 3705e589dc9f80e1a0fcf9a8c5ec8f03):
- Pivot: ODM 도입 2026-03 (변곡점이 25.12 → 26.03으로 변경)
- 비교: ODM 전 3개월 (25.12~26.02) vs ODM 후 3개월 (26.03~26.05)
- 구글애즈 iOS 구매 유저 437 → 1,430명 (+227%)
- 구글애즈 iOS CPA ₩82,136 → ₩43,513 (-47%)
- iOS 전체 구매 유저 월평균 27,041 → 37,860명 (+40%)
- 구글애즈 iOS 집행액 ₩3,589만 → ₩6,222만 (+73%)
"""
from pathlib import Path

p = Path(__file__).parent / "_build_v27.py"
text = p.read_text(encoding="utf-8")

START = "IOS_ODM_SLIDE = '''"
END_MARK = "slide_blocks[\"p_ios_odm\"] = IOS_ODM_SLIDE"

start_i = text.index(START)
end_i = text.index(END_MARK, start_i)


NEW_SLIDE = '''IOS_ODM_SLIDE = \'\'\'<div class="slide" id="p_ios_odm">
  <div class="grid-bg light"></div>
  <div class="hd-tight">
    <div>
      <div class="cat-row">
        <span class="cat-chip" style="background:var(--ca-perf);"><span class="ko">퍼포먼스</span><span class="en">Performance · iOS UA</span></span>
        <span class="cat-meta"><b>03 / 04</b> · iOS ODM</span>
      </div>
      <div class="page-title">ODM 도입(26.03)으로 막혔던 구글애즈 iOS — 구매 유저 <em>+227%</em> · CPA <em>-47%</em>, iOS 전체 <em>+40%</em></div>
    </div>
    <span class="slide-num">06 / 16</span>
  </div>

  <div class="body2">
    <div class="col-l">
      <div class="tag-row">
        <span class="c-badge" style="background:var(--ca-perf);">Performance · Google Ads · iOS UA</span>
        <span class="c-badge outline">커버링 · 2026.03 ODM 정식 연동 · ±3개월 매칭 비교</span>
      </div>
      <div class="p-title">iOS는 AOS 대비 LTV 최대 <em>4.6배</em>인데<br>가장 큰 채널에서 한 명도 데려올 수 없었다</div>

      <div class="phase b1"><span class="ptag">병목</span>ATT 이후 IDFA 막힘 + 구글 ODM 미설정 — iOS 학습 신호 0</div>
      <div class="sec tight"><ul>
        <li>구글애즈 머신러닝이 학습할 <em>iOS 전환 신호</em>가 없어 <strong>iOS 모객 전면 불가</strong> · 매월 수천만원 기회손실</li>
        <li>마케팅 단독으로는 못 푸는 <strong>앱 단 개발 작업</strong>이라 백로그에 계속 밀림 → 손실 비용을 데이터로 제시해 개발·제품팀 설득 (26.02.23 #개발팀_협업요청)</li>
      </ul></div>

      <div class="phase b2"><span class="ptag">실행</span>① ODM 정식 연동 (26.03) + ② iOS 고효율 소재 핏 (25.09~)</div>
      <div class="sec tight"><ul>
        <li><strong>① 구글애즈 ODM 연동 (2026.03)</strong> — 개발·제품팀 협업으로 정식 연동, 막혔던 구글애즈 iOS 캠페인 가동</li>
        <li><strong>② iOS 고효율 소재 핏 (25.09~)</strong> — 대형폐기물·가구·가전·엄마 소구를 채널 간 이식 · 30초 숏폼 위주 <strong>2주 단위 교체</strong></li>
        <li>준비/진행 중인 다음 레버 — ③ 측정 인프라(딥링크 포스트백·SKAN) · ④ ATT 동의 프리보딩 · ⑤ 유튜브 직접 컨택</li>
      </ul></div>

      <div class="phase b3"><span class="ptag">결과</span>ODM 도입 전후 3개월 — 구글애즈 iOS <b>+227%</b> · CPA <b>-47%</b></div>
      <div class="sec tight"><ul>
        <li>구글애즈 iOS 구매 유저 <strong>437 → 1,430명 (+227%)</strong> · 신규 설치 <strong>1,651 → 5,418명 (+228%)</strong></li>
        <li>구글애즈 iOS 구매 CPA <strong>₩82,136 → ₩43,513 (-47%)</strong> — 집행액은 +73% 늘렸는데 구매는 +227% (구글이 iOS 가치를 학습)</li>
        <li>iOS 전체 구매 유저 월평균 <strong>27,041 → 37,860명 (+40%)</strong> · 신규 설치 +35.8% · 26.05 41,833명 최고치</li>
      </ul></div>

      <div class="result">
        <div class="kpi"><span class="kpi-num">+227%</span><span class="kpi-label">구글애즈 iOS 구매 유저 (437 → 1,430명)</span></div>
        <div class="kpi"><span class="kpi-num">-47%</span><span class="kpi-label">구글애즈 iOS 구매 CPA (₩82,136 → ₩43,513)</span></div>
        <div class="kpi"><span class="kpi-num">+40%</span><span class="kpi-label">iOS 전체 구매 유저 월평균 (27,041 → 37,860명)</span></div>
      </div>
    </div>

    <div class="col-r">
      <!-- 상단: 6개월 막대(iOS 전체 구매 유저) + 라인(구글애즈 iOS 집행액) -->
      <div class="chart-card" style="flex:none;display:flex;flex-direction:column;padding:14px 18px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
          <div class="chart-title" style="margin-bottom:0;">iOS 전체 구매 유저(막대) + 구글애즈 iOS 집행액(라인) — ODM 도입 26.03 전후 3개월</div>
          <span style="font-family:var(--font-mono);font-size:10px;color:var(--sub);letter-spacing:.06em;">25.12~26.05 · Airbridge 실측</span>
        </div>
        <svg viewBox="0 0 720 280" width="100%" style="display:block;">
          <defs>
            <linearGradient id="b_pre_v2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#5B9BD5"/><stop offset="100%" stop-color="#8FB8DC"/></linearGradient>
            <linearGradient id="b_post_v2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#27AE60"/><stop offset="100%" stop-color="#5BC785"/></linearGradient>
          </defs>
          <!-- left axis: iOS 구매 유저 (0 ~ 45K), y range 30~230 (200px) -->
          <line x1="60" y1="30" x2="650" y2="30" stroke="#F1F4F9"/><text x="55" y="34" font-size="10" fill="#8B95A6" text-anchor="end" font-family="JetBrains Mono">45K</text>
          <line x1="60" y1="80" x2="650" y2="80" stroke="#F1F4F9"/><text x="55" y="84" font-size="10" fill="#8B95A6" text-anchor="end" font-family="JetBrains Mono">34K</text>
          <line x1="60" y1="130" x2="650" y2="130" stroke="#F1F4F9"/><text x="55" y="134" font-size="10" fill="#8B95A6" text-anchor="end" font-family="JetBrains Mono">22K</text>
          <line x1="60" y1="180" x2="650" y2="180" stroke="#F1F4F9"/><text x="55" y="184" font-size="10" fill="#8B95A6" text-anchor="end" font-family="JetBrains Mono">11K</text>
          <line x1="60" y1="230" x2="650" y2="230" stroke="#E2E6EF" stroke-width="1.5"/>
          <!-- right axis: 구글애즈 iOS 집행액 (0 ~ 3,000만, 200px) -->
          <text x="655" y="34" font-size="10" fill="#E67E22" text-anchor="start" font-family="JetBrains Mono">3,000만</text>
          <text x="655" y="130" font-size="10" fill="#E67E22" text-anchor="start" font-family="JetBrains Mono">1,500만</text>
          <text x="655" y="230" font-size="10" fill="#E67E22" text-anchor="start" font-family="JetBrains Mono">0</text>

          <!-- bars: 6 months, width 60, gap 30 (60+30=90, 6*90=540, start at 80, end 620)
               y = 230 - val/45000 * 200
               25.12 25387 → 117.17
               26.01 26915 → 110.38
               26.02 28821 → 101.91
               26.03 33993 → 78.92  (ODM 도입)
               26.04 37755 → 62.20
               26.05 41833 → 44.07 -->
          <rect x="80"  y="117.17" width="60" height="112.83" rx="3" fill="url(#b_pre_v2)"/>
          <rect x="170" y="110.38" width="60" height="119.62" rx="3" fill="url(#b_pre_v2)"/>
          <rect x="260" y="101.91" width="60" height="128.09" rx="3" fill="url(#b_pre_v2)"/>
          <rect x="350" y="78.92"  width="60" height="151.08" rx="3" fill="url(#b_post_v2)"/>
          <rect x="440" y="62.20"  width="60" height="167.80" rx="3" fill="url(#b_post_v2)"/>
          <rect x="530" y="44.07"  width="60" height="185.93" rx="3" fill="#27AE60"/>

          <!-- bar value labels -->
          <text x="110" y="112" font-size="11" fill="#3E73A8" font-weight="700" text-anchor="middle" font-family="JetBrains Mono">25.4K</text>
          <text x="200" y="105" font-size="11" fill="#3E73A8" font-weight="700" text-anchor="middle" font-family="JetBrains Mono">26.9K</text>
          <text x="290" y="96"  font-size="11" fill="#3E73A8" font-weight="700" text-anchor="middle" font-family="JetBrains Mono">28.8K</text>
          <text x="380" y="73"  font-size="12" fill="#1E8449" font-weight="900" text-anchor="middle" font-family="JetBrains Mono">34.0K</text>
          <text x="470" y="56"  font-size="12" fill="#1E8449" font-weight="900" text-anchor="middle" font-family="JetBrains Mono">37.8K</text>
          <text x="560" y="38"  font-size="13" fill="#1E8449" font-weight="900" text-anchor="middle" font-family="JetBrains Mono">41.8K ★</text>

          <!-- spend line: right axis 0~3000만, y = 230 - val/3000 * 200
               25.12 1813 → 109.13
               26.01 1776 → 111.60
               26.02 0    → 230 (집행 중단)
               26.03 1400 → 136.67
               26.04 2517 → 62.20
               26.05 2305 → 76.33 -->
          <polyline points="110,109.13 200,111.60 290,230 380,136.67 470,62.20 560,76.33"
                    fill="none" stroke="#E67E22" stroke-width="2.5" stroke-linejoin="round"/>
          <circle cx="110" cy="109.13" r="4" fill="#E67E22"/>
          <circle cx="200" cy="111.60" r="4" fill="#E67E22"/>
          <circle cx="290" cy="230" r="4" fill="#E67E22"/>
          <circle cx="380" cy="136.67" r="4" fill="#E67E22"/>
          <circle cx="470" cy="62.20" r="4" fill="#E67E22"/>
          <circle cx="560" cy="76.33" r="4" fill="#E67E22"/>

          <!-- spend value labels (small) -->
          <text x="110" y="100" font-size="9" fill="#C2740F" text-anchor="middle" font-family="JetBrains Mono">1,813</text>
          <text x="200" y="103" font-size="9" fill="#C2740F" text-anchor="middle" font-family="JetBrains Mono">1,776</text>
          <text x="290" y="222" font-size="9" fill="#C2740F" text-anchor="middle" font-family="JetBrains Mono">0</text>
          <text x="380" y="128" font-size="9" fill="#C2740F" text-anchor="middle" font-family="JetBrains Mono">1,400</text>
          <text x="470" y="54"  font-size="9" fill="#C2740F" text-anchor="middle" font-family="JetBrains Mono">2,517</text>
          <text x="560" y="68"  font-size="9" fill="#C2740F" text-anchor="middle" font-family="JetBrains Mono">2,305</text>

          <!-- ODM 도입 26.03 vertical marker (between bar 3 and bar 4) -->
          <line x1="335" y1="26" x2="335" y2="230" stroke="#1E8449" stroke-width="1.5" stroke-dasharray="4,4"/>
          <rect x="280" y="9" width="110" height="16" rx="3" fill="#0A0F2E"/>
          <text x="335" y="21" font-size="10" fill="#D6FF3D" font-weight="800" text-anchor="middle" font-family="JetBrains Mono">★ 26.03 ODM 도입</text>

          <!-- X labels -->
          <text x="110" y="248" font-size="10" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">25.12</text>
          <text x="200" y="248" font-size="10" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">26.01</text>
          <text x="290" y="248" font-size="10" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">26.02</text>
          <text x="380" y="248" font-size="10" fill="#0F172A" font-weight="800" text-anchor="middle" font-family="JetBrains Mono">26.03</text>
          <text x="470" y="248" font-size="10" fill="#5B6675" text-anchor="middle" font-family="JetBrains Mono">26.04</text>
          <text x="560" y="248" font-size="10" fill="#1E8449" font-weight="800" text-anchor="middle" font-family="JetBrains Mono">26.05</text>

          <!-- Period averages annotation -->
          <line x1="80" y1="262" x2="320" y2="262" stroke="#5B9BD5" stroke-width="2"/>
          <text x="200" y="275" font-size="10" fill="#3E73A8" text-anchor="middle" font-family="JetBrains Mono" font-weight="700">ODM 전 3개월 · 월평균 27,041명</text>
          <line x1="350" y1="262" x2="590" y2="262" stroke="#27AE60" stroke-width="2"/>
          <text x="470" y="275" font-size="10" fill="#1E8449" text-anchor="middle" font-family="JetBrains Mono" font-weight="700">ODM 후 3개월 · 월평균 37,860명 (+40%)</text>
        </svg>
      </div>

      <!-- 하단: 구글애즈 iOS ODM 전후 비교 표 -->
      <div class="chart-card" style="flex:1;min-height:0;display:flex;flex-direction:column;padding:14px 18px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
          <div class="chart-title" style="margin-bottom:0;">구글애즈 iOS — ODM 전후 3개월 합계 비교 (Airbridge 실측)</div>
          <span style="font-family:var(--font-mono);font-size:10px;color:var(--sub);letter-spacing:.08em;">25.12~26.02 vs 26.03~26.05</span>
        </div>
        <table style="width:100%;border-collapse:separate;border-spacing:0;font-variant-numeric:tabular-nums;">
          <thead><tr>
            <th style="text-align:left;padding:8px 10px;background:var(--ink);font-family:var(--font-mono);font-size:11px;font-weight:700;color:#fff;border-radius:6px 0 0 0;">구글애즈 iOS (3개월 합)</th>
            <th style="text-align:right;padding:8px 10px;background:var(--ink);font-family:var(--font-mono);font-size:11px;font-weight:700;color:#fff;">ODM 전</th>
            <th style="text-align:right;padding:8px 10px;background:var(--ink);font-family:var(--font-mono);font-size:11px;font-weight:700;color:#fff;">ODM 후</th>
            <th style="text-align:right;padding:8px 10px;background:var(--ink);font-family:var(--font-mono);font-size:11px;font-weight:700;color:#fff;border-radius:0 6px 0 0;">개선</th>
          </tr></thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--line-lt);">
              <td style="padding:9px 10px;font-size:12.5px;color:var(--text);">집행액</td>
              <td style="text-align:right;padding:9px 10px;font-size:12px;font-family:var(--font-mono);color:var(--text2);">₩3,589만</td>
              <td style="text-align:right;padding:9px 10px;font-size:12px;font-family:var(--font-mono);color:var(--text2);">₩6,222만</td>
              <td style="text-align:right;padding:9px 10px;"><span style="display:inline-block;background:#FFF7ED;color:#92400E;font-family:var(--font-mono);font-size:11px;font-weight:800;padding:3px 8px;border-radius:11px;">+73%</span></td>
            </tr>
            <tr style="background:#F4FBF7;border-bottom:1px solid var(--line-lt);">
              <td style="padding:9px 10px;font-size:13px;font-weight:800;color:var(--text);">★ 구매 유저</td>
              <td style="text-align:right;padding:9px 10px;font-size:12px;font-family:var(--font-mono);color:var(--text2);">437명</td>
              <td style="text-align:right;padding:9px 10px;font-size:13px;font-family:var(--font-mono);font-weight:800;color:#0E9E76;">1,430명</td>
              <td style="text-align:right;padding:9px 10px;"><span style="display:inline-block;background:#E3F7ED;color:#0E9E76;font-family:var(--font-mono);font-size:11px;font-weight:800;padding:3px 8px;border-radius:11px;">+227%</span></td>
            </tr>
            <tr style="border-bottom:1px solid var(--line-lt);">
              <td style="padding:9px 10px;font-size:12.5px;color:var(--text);">신규 설치 유저</td>
              <td style="text-align:right;padding:9px 10px;font-size:12px;font-family:var(--font-mono);color:var(--text2);">1,651명</td>
              <td style="text-align:right;padding:9px 10px;font-size:12px;font-family:var(--font-mono);color:var(--text2);">5,418명</td>
              <td style="text-align:right;padding:9px 10px;"><span style="display:inline-block;background:#E3F7ED;color:#0E9E76;font-family:var(--font-mono);font-size:11px;font-weight:800;padding:3px 8px;border-radius:11px;">+228%</span></td>
            </tr>
            <tr style="background:#F4FBF7;">
              <td style="padding:9px 10px;font-size:13px;font-weight:800;color:var(--text);">★ 구매 CPA</td>
              <td style="text-align:right;padding:9px 10px;font-size:12px;font-family:var(--font-mono);color:var(--text2);">₩82,136</td>
              <td style="text-align:right;padding:9px 10px;font-size:13px;font-family:var(--font-mono);font-weight:800;color:#0E9E76;">₩43,513</td>
              <td style="text-align:right;padding:9px 10px;"><span style="display:inline-block;background:#E3F7ED;color:#0E9E76;font-family:var(--font-mono);font-size:11px;font-weight:800;padding:3px 8px;border-radius:11px;">-47%</span></td>
            </tr>
          </tbody>
        </table>
        <div style="margin-top:auto;padding-top:8px;font-family:var(--font-mono);font-size:11px;color:var(--text2);line-height:1.5;">
          ✅ <strong style="color:var(--text);">ODM은 "광고를 더 쓴 것"이 아니라 "쓸 수 없던 채널을 쓸 수 있게 만든" 액션.</strong> 집행액은 +73%만 늘었는데 구매 유저는 <strong style="color:#0E9E76;">+227%</strong> — 구글이 iOS 가치를 학습하며 CPA가 <strong style="color:#0E9E76;">절반(-47%)</strong>으로 떨어짐.
        </div>
      </div>
    </div>
  </div>
  <div class="chrome"><span><b>06</b> / 16</span><span>Performance · iOS UA · ODM · 구글애즈 iOS +227% · CPA -47%</span></div>
</div>\'\'\'

'''

text = text[:start_i] + NEW_SLIDE + text[end_i:]
p.write_text(text, encoding="utf-8")
print(f"swapped IOS_ODM_SLIDE in _build_v27.py (file now {len(text):,} chars)")
