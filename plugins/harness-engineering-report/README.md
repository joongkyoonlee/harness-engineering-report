# Harness Engineering Report Plugin

This Codex plugin helps create sourced PDF reports about Harness Engineering topics, including CI/CD, DevOps, platform engineering, software delivery, security, FinOps, internal developer platforms, and AI-assisted engineering workflows.

It also includes a Claude Code plugin manifest, so the same skill can be installed from a Claude Code marketplace.

## Contents

- `.codex-plugin/plugin.json`: Codex plugin manifest
- `.claude-plugin/plugin.json`: Claude Code plugin manifest
- `skills/harness-engineering-report/SKILL.md`: Harness Engineering research and report workflow
- `scripts/render_report.py`: Helper that converts Markdown to styled HTML and optionally prints PDF with Chrome or Edge

The skill guides Codex to search with varied Korean and English queries, compare sources, extract engineering insights, and produce a PDF-ready report.
