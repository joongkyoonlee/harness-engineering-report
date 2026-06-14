# AI Trend Report

This repository publishes a Codex marketplace plugin that researches the latest seven days of AI news and creates a sourced PDF trend report.

## Repository Layout

```text
.
|-- .agents/
|   `-- plugins/
|       `-- marketplace.json
`-- plugins/
    `-- ai-trend-report/
        |-- .codex-plugin/
        |   `-- plugin.json
        |-- scripts/
        |   `-- render_report.py
        `-- skills/
            `-- ai-trend-report/
                `-- SKILL.md
```

## How It Works

- `.agents/plugins/marketplace.json` is the marketplace catalog.
- `plugins/ai-trend-report/.codex-plugin/plugin.json` is the plugin manifest.
- `plugins/ai-trend-report/skills/` contains the AI trend report workflow.
- `plugins/ai-trend-report/scripts/render_report.py` renders Markdown to HTML and optionally PDF.

## Publish To GitHub

Create a new GitHub repository, then push this folder:

```bash
git init
git add .
git commit -m "Create AI trend report plugin"
git branch -M main
git remote add origin https://github.com/YOUR_ORG/ai-trend-report.git
git push -u origin main
```

## Register In Codex

After publishing, another user can register this marketplace by adding the repository's marketplace root.

```bash
codex plugin marketplace add https://github.com/YOUR_ORG/ai-trend-report
codex plugin add ai-trend-report@ai-trend-report
```

If your installed marketplace name differs, check the name in `.agents/plugins/marketplace.json` and use:

```bash
codex plugin add ai-trend-report@<marketplace-name>
```

## Adapting This Starter

For multi-host distribution, keep the core logic portable:

- Codex: ship `.codex-plugin/plugin.json`, `skills/`, optional MCP/app config.
- Claude Code: expose shared logic through MCP or Claude-specific commands/config.
- Other harnesses: expose the same tools through MCP or an HTTP API when possible.

MCP is the best cross-agent compatibility layer because many hosts can consume it without sharing the same marketplace format.

## Validate

From the plugin creator skill root, validate the plugin:

```bash
python scripts/validate_plugin.py <repo-root>/plugins/ai-trend-report
```

## License

MIT
