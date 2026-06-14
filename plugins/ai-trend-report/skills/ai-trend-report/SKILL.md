---
name: ai-trend-report
description: Research Harness Engineering topics with varied web searches and create a sourced PDF report.
---

# Harness Engineering Report

Use this skill when the user asks for a Harness Engineering report, Harness.io research, DevOps/platform engineering analysis, CI/CD comparison, software delivery trend report, or a PDF report based on current web research.

## Output

Create a concise PDF report in Korean unless the user asks for another language. Also keep the source Markdown and HTML files next to the PDF.

## Research Window

- Default to the latest seven calendar days when the user asks for "latest", "recent", "이번 주", or time-sensitive updates.
- For strategic or evergreen Harness Engineering reports, combine current web research with official background sources.
- State the exact date range in the report.
- If the user says "today", "this week", or "latest", resolve it to concrete dates.
- Prefer articles published inside the date range. Use older sources only for background and label them as context.

## Search Strategy

Run multiple searches with varied wording. Mix Korean and English queries. Include official Harness sources when possible.

Use at least these query groups:

1. Harness platform and engineering:
   - "Harness engineering blog CI/CD platform engineering"
   - "Harness software delivery platform latest"
   - "Harness 엔지니어링 DevOps 플랫폼"
2. CI/CD and software delivery:
   - "Harness CI CD pipeline governance deployment automation"
   - "continuous delivery platform engineering Harness"
   - "Harness CI/CD 배포 자동화 파이프라인"
3. Internal developer platform and developer experience:
   - "Harness IDP internal developer portal Backstage"
   - "developer experience platform engineering Harness"
   - "내부 개발자 플랫폼 Harness IDP"
4. Security, governance, and compliance:
   - "Harness security testing software supply chain governance"
   - "Harness SLSA SBOM DevSecOps"
   - "Harness 보안 거버넌스 DevSecOps"
5. FinOps, cloud cost, and efficiency:
   - "Harness cloud cost management FinOps engineering"
   - "software engineering efficiency metrics Harness"
   - "Harness FinOps 클라우드 비용 최적화"
6. AI-assisted engineering:
   - "Harness AI software delivery engineering"
   - "AI for DevOps CI/CD Harness"
   - "Harness AI 개발 생산성"

Add domain-specific queries when useful, such as DORA metrics, feature flags, chaos engineering, service reliability, Kubernetes delivery, code quality, developer productivity, and software engineering intelligence.

## Source Rules

- Use direct links to sources.
- Prioritize primary sources, official blogs, company announcements, regulator pages, research papers, and reputable news outlets.
- For Harness product claims, prefer official Harness documentation, engineering blogs, release notes, and product pages, then corroborate with analyst or practitioner sources.
- Cross-check important claims with at least two sources when possible.
- Do not overquote. Summarize in your own words and include links.
- Keep a source table with title, publisher, date, URL, and relevance.

## Report Structure

Use this structure:

1. Title page
2. Executive summary
3. Key findings
4. Harness Engineering landscape
5. Analysis by theme: CI/CD, IDP, security, FinOps, AI-assisted engineering
6. Architecture and operating model implications
7. Implications for Korean engineering organizations
8. Adoption roadmap and risks
9. Watchlist for the next 1-4 weeks when researching recent news
10. Source table
11. Methodology and search queries

## Recommended Files

Create an output directory named `harness-engineering-report-YYYY-MM-DD`.

Recommended filenames:

- `harness-engineering-report.md`
- `harness-engineering-report.html`
- `harness-engineering-report.pdf`
- `sources.json`

## PDF Rendering

After writing Markdown, use the helper script when available:

```bash
python plugins/ai-trend-report/scripts/render_report.py harness-engineering-report.md --pdf harness-engineering-report.pdf --html harness-engineering-report.html
```

If browser-based PDF export is unavailable, still provide the Markdown and HTML report and explain that PDF export could not run in the current environment.
