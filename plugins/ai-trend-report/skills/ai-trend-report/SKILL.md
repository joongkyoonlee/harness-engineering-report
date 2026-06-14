---
name: ai-trend-report
description: Research the latest seven days of AI news with varied web searches and create a sourced PDF trend report.
---

# AI Trend Report

Use this skill when the user asks for an AI trend report, weekly AI news briefing, recent AI industry analysis, or a PDF report based on current web research.

## Output

Create a concise PDF report in Korean unless the user asks for another language. Also keep the source Markdown and HTML files next to the PDF.

## Research Window

- Default to the latest seven calendar days.
- State the exact date range in the report.
- If the user says "today", "this week", or "latest", resolve it to concrete dates.
- Prefer articles published inside the date range. Use older sources only for background and label them as context.

## Search Strategy

Run multiple searches with varied wording. Mix Korean and English queries.

Use at least these query groups:

1. Model releases and benchmarks:
   - "AI model release last week"
   - "LLM benchmark new model this week"
   - "생성형 AI 모델 출시 이번 주"
2. Product and platform launches:
   - "AI product launch this week"
   - "agentic AI tools news last 7 days"
   - "AI 에이전트 제품 출시"
3. Big tech and startups:
   - "OpenAI Anthropic Google Meta AI news last week"
   - "AI startup funding acquisition this week"
   - "AI 스타트업 투자 인수 최근"
4. Policy, safety, copyright, regulation:
   - "AI regulation policy safety news last week"
   - "AI copyright lawsuit regulation this week"
   - "AI 규제 저작권 안전성 최근"
5. Enterprise adoption and market signals:
   - "enterprise AI adoption news this week"
   - "AI chip cloud datacenter demand last week"
   - "기업 AI 도입 반도체 데이터센터 뉴스"

Add domain-specific queries when useful, such as healthcare AI, education AI, robotics AI, coding agents, AI video, AI search, or open-source AI.

## Source Rules

- Use direct links to sources.
- Prioritize primary sources, official blogs, company announcements, regulator pages, research papers, and reputable news outlets.
- Cross-check important claims with at least two sources when possible.
- Do not overquote. Summarize in your own words and include links.
- Keep a source table with title, publisher, date, URL, and relevance.

## Report Structure

Use this structure:

1. Title page
2. Executive summary
3. Key trend bullets
4. Timeline of major events
5. Trend analysis by theme
6. Implications for Korean organizations
7. Watchlist for the next 1-4 weeks
8. Source table
9. Methodology and search queries

## Recommended Files

Create an output directory named `ai-trend-report-YYYY-MM-DD`.

Recommended filenames:

- `ai-trend-report.md`
- `ai-trend-report.html`
- `ai-trend-report.pdf`
- `sources.json`

## PDF Rendering

After writing Markdown, use the helper script when available:

```bash
python plugins/ai-trend-report/scripts/render_report.py ai-trend-report.md --pdf ai-trend-report.pdf --html ai-trend-report.html
```

If browser-based PDF export is unavailable, still provide the Markdown and HTML report and explain that PDF export could not run in the current environment.
