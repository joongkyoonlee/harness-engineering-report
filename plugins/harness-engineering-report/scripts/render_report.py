#!/usr/bin/env python3
"""Render a simple Markdown report to HTML and optionally PDF via Chrome/Edge."""

from __future__ import annotations

import argparse
import html
import os
import shutil
import subprocess
import sys
from pathlib import Path


STYLE = """
body {
  font-family: "Noto Sans KR", "Malgun Gothic", "Apple SD Gothic Neo", Arial, sans-serif;
  color: #172033;
  line-height: 1.62;
  margin: 48px;
  max-width: 920px;
}
h1, h2, h3 { color: #0f172a; line-height: 1.25; }
h1 { font-size: 30px; border-bottom: 3px solid #2563eb; padding-bottom: 12px; }
h2 { font-size: 22px; margin-top: 32px; border-bottom: 1px solid #dbe3ef; padding-bottom: 6px; }
h3 { font-size: 17px; margin-top: 24px; }
p, li { font-size: 11.5pt; }
a { color: #1d4ed8; }
code { background: #f1f5f9; padding: 2px 5px; border-radius: 4px; }
pre { background: #0f172a; color: #e2e8f0; padding: 14px; border-radius: 8px; overflow-x: auto; }
blockquote { border-left: 4px solid #93c5fd; margin-left: 0; padding-left: 16px; color: #334155; }
table { width: 100%; border-collapse: collapse; margin: 18px 0; font-size: 10pt; }
th, td { border: 1px solid #dbe3ef; padding: 8px; vertical-align: top; }
th { background: #eff6ff; }
@page { size: A4; margin: 16mm; }
"""


def render_inline(text: str) -> str:
    escaped = html.escape(text)
    return escaped.replace("**", "")


def markdown_to_html(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    in_list = False
    in_code = False
    code_lines: list[str] = []

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_code:
                out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
                code_lines = []
                in_code = False
            else:
                if in_list:
                    out.append("</ul>")
                    in_list = False
                in_code = True
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not stripped:
            if in_list:
                out.append("</ul>")
                in_list = False
            continue

        if stripped.startswith("# "):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<h1>{render_inline(stripped[2:])}</h1>")
        elif stripped.startswith("## "):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<h2>{render_inline(stripped[3:])}</h2>")
        elif stripped.startswith("### "):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<h3>{render_inline(stripped[4:])}</h3>")
        elif stripped.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{render_inline(stripped[2:])}</li>")
        elif stripped.startswith("> "):
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<blockquote>{render_inline(stripped[2:])}</blockquote>")
        else:
            if in_list:
                out.append("</ul>")
                in_list = False
            out.append(f"<p>{render_inline(stripped)}</p>")

    if in_list:
        out.append("</ul>")
    if in_code:
        out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")

    return "<!doctype html><html><head><meta charset=\"utf-8\"><style>" + STYLE + "</style></head><body>" + "\n".join(out) + "</body></html>"


def find_browser() -> str | None:
    candidates = [
        os.environ.get("CHROME_PATH"),
        shutil.which("msedge"),
        shutil.which("chrome"),
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return str(candidate)
    return None


def print_pdf(html_path: Path, pdf_path: Path) -> None:
    browser = find_browser()
    if not browser:
        raise RuntimeError("Chrome or Edge was not found for PDF export.")
    cmd = [
        browser,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path.resolve()}",
        html_path.resolve().as_uri(),
    ]
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--html", type=Path)
    parser.add_argument("--pdf", type=Path)
    args = parser.parse_args()

    markdown_path = args.markdown
    html_path = args.html or markdown_path.with_suffix(".html")
    pdf_path = args.pdf

    content = markdown_path.read_text(encoding="utf-8")
    html_content = markdown_to_html(content)
    html_path.write_text(html_content, encoding="utf-8")
    print(f"Wrote HTML: {html_path}")

    if pdf_path:
        print_pdf(html_path, pdf_path)
        print(f"Wrote PDF: {pdf_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
