"""profile/resume.md 를 제출용 A4 PDF(profile/resume.pdf)로 만든다.

  python tools/build-resume-pdf.py        # Playwright(Python) 가 깔린 환경에서

md 가 원본이고 PDF 는 산출물이다 — 이력서를 고치면 이 스크립트를 다시 돌린다.
"""

from __future__ import annotations

import pathlib
import re

from playwright.sync_api import sync_playwright

REPO = pathlib.Path(__file__).resolve().parent.parent
SOURCE = REPO / "profile" / "resume.md"
TARGET = REPO / "profile" / "resume.pdf"
MARKED = "https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"
FONT = "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css"

# 인쇄용 — 화면 장식 없이 위계만. 표는 쪽을 넘어 쪼개지지 않게 한다.
PRINT_CSS = """
@page { size: A4; margin: 11mm 14mm 12mm 14mm; }
* { box-sizing: border-box; }
body { font: 8.9pt/1.5 'Pretendard Variable', Pretendard, sans-serif; color: #151515; word-break: keep-all; margin: 0; }
h1 { font-size: 20pt; letter-spacing: -0.03em; margin: 0 0 4pt; }
h2 { font-size: 11.5pt; margin: 9pt 0 3pt; padding-bottom: 3pt; border-bottom: 1.2pt solid #151515; break-after: avoid; }
h3 { font-size: 10.2pt; margin: 8pt 0 2pt; break-after: avoid; }
h4 { font-size: 9.6pt; margin: 7pt 0 2pt; color: #2c4ee6; break-after: avoid; }
p { margin: 3pt 0; }
blockquote { margin: 0 0 5pt; padding: 0; color: #555; }
blockquote p { margin: 1pt 0; }
ul { margin: 2pt 0 4pt; padding-left: 13pt; }
li { margin: 0.6pt 0; }
table { width: 100%; border-collapse: collapse; margin: 2pt 0 4pt; break-inside: avoid; font-size: 8.6pt; }
th, td { text-align: left; vertical-align: top; padding: 1.6pt 5pt; border-bottom: 0.5pt solid #ddd; }
thead { display: none; }  /* md 표의 「항목 · 내용」 머리는 인쇄에서 뺀다 */
td:first-child { width: 22%; color: #555; white-space: nowrap; }
a { color: inherit; text-decoration: none; }
code { font-family: ui-monospace, Menlo, monospace; font-size: 0.9em; }
ul.facts { columns: 2; column-gap: 18pt; list-style: none; padding-left: 0; }
ul.facts li { break-inside: avoid; }
ul.facts span { display: inline-block; min-width: 46pt; color: #555; }
"""

# 인쇄에서 두 단 목록으로 접는 절
COMPACT_SECTIONS = ["학력", "자격 · 어학", "기타"]


def printable_markdown(markdown: str) -> str:
    """PDF 에만 맞는 손질 — 자기 자신을 가리키는 「이력서 PDF」 줄은 뺀다."""
    return re.sub(r"^\| 이력서 PDF \|.*\n", "", markdown, flags=re.MULTILINE)


def main() -> None:
    markdown = printable_markdown(SOURCE.read_text(encoding="utf-8"))
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.set_content(
            f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><link rel="stylesheet" href="{FONT}">'
            f"<style>{PRINT_CSS}</style></head><body><main id=doc></main><script src='{MARKED}'></script></body></html>",
            wait_until="networkidle",
        )
        page.evaluate("md => { document.getElementById('doc').innerHTML = marked.parse(md) }", markdown)
        # 종이에서는 링크를 누를 수 없다 — 「repo」 같은 링크 글은 실제 주소로 보여 준다.
        page.evaluate("""() => document.querySelectorAll('a[href^="http"]').forEach(a => {
            if (!a.textContent.includes('.')) a.textContent = a.href.replace(/^https?:\\/\\//, '').replace(/\\/$/, '')
        })""")
        # 짧은 사실 표(자격 · 기타)는 인쇄에서 두 단 목록으로 접는다 — 한 줄에 한 항목이면 종이를 낭비한다.
        page.evaluate("""titles => document.querySelectorAll('h2').forEach(h2 => {
            const table = h2.nextElementSibling
            if (!titles.includes(h2.textContent.trim()) || table?.tagName !== 'TABLE') return
            const list = document.createElement('ul')
            list.className = 'facts'
            table.querySelectorAll('tbody tr').forEach(tr => {
                const [key, value] = [...tr.children].map(td => td.innerHTML)
                list.insertAdjacentHTML('beforeend', `<li><span>${key}</span> ${value}</li>`)
            })
            table.replaceWith(list)
        })""", COMPACT_SECTIONS)
        page.evaluate("document.fonts.ready")
        page.pdf(path=str(TARGET), format="A4", print_background=True, prefer_css_page_size=True,
                 display_header_footer=True, header_template="<span></span>",
                 footer_template="<div style='width:100%;font-size:7pt;color:#999;text-align:center'>"
                                 "이현도 · 이력서 · <span class='pageNumber'></span> / <span class='totalPages'></span></div>")
        browser.close()
    print(TARGET)


if __name__ == "__main__":
    main()
