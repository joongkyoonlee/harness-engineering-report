# Harness Engineering Report

This repository publishes Codex and Claude Code marketplace plugins that research Harness Engineering topics and create sourced PDF reports.

## Repository Layout

```text
.
|-- .agents/
|   `-- plugins/
|       `-- marketplace.json
|-- .claude-plugin/
|   `-- marketplace.json
`-- plugins/
    `-- harness-engineering-report/
        |-- .claude-plugin/
        |   `-- plugin.json
        |-- .codex-plugin/
        |   `-- plugin.json
        |-- scripts/
        |   `-- render_report.py
        `-- skills/
            `-- harness-engineering-report/
                `-- SKILL.md
```

## How It Works

- `.agents/plugins/marketplace.json` is the Codex marketplace catalog.
- `.claude-plugin/marketplace.json` is the Claude Code marketplace catalog.
- `plugins/harness-engineering-report/.codex-plugin/plugin.json` is the Codex plugin manifest.
- `plugins/harness-engineering-report/.claude-plugin/plugin.json` is the Claude Code plugin manifest.
- `plugins/harness-engineering-report/skills/` contains the Harness Engineering report workflow.
- `plugins/harness-engineering-report/scripts/render_report.py` renders Markdown to HTML and optionally PDF.

## Publish To GitHub

Create a new GitHub repository, then push this folder:

```bash
git init
git add .
git commit -m "Create Harness Engineering report plugin"
git branch -M main
git remote add origin https://github.com/joongkyoonlee/harness-engineering-report.git
git push -u origin main
```

## Register In Codex

After publishing, another user can register this marketplace by adding the repository's marketplace root.

```bash
codex plugin marketplace add https://github.com/joongkyoonlee/harness-engineering-report
codex plugin add harness-engineering-report@harness-engineering-report
```

If your installed marketplace name differs, check the name in `.agents/plugins/marketplace.json` and use:

```bash
codex plugin add harness-engineering-report@<marketplace-name>
```

## Register In Claude Code

Claude Code users can add the repository as a plugin marketplace and install the plugin:

```text
/plugin marketplace add joongkyoonlee/harness-engineering-report
/plugin install harness-engineering-report@harness-engineering-report
```

After installation, run:

```text
/reload-plugins
/harness-engineering-report:harness-engineering-report
```

## Adapting This Starter

Use it with prompts like:

```text
Harness Engineering 관련 최신 내용을 조사해 PDF 보고서를 만들어줘.
Harness의 CI/CD, IDP, 보안, FinOps 흐름을 분석해줘.
```

For multi-host distribution, keep the core logic portable:

- Codex: ship `.codex-plugin/plugin.json`, `skills/`, optional MCP/app config.
- Claude Code: expose shared logic through MCP or Claude-specific commands/config.
- Other harnesses: expose the same tools through MCP or an HTTP API when possible.

MCP is the best cross-agent compatibility layer because many hosts can consume it without sharing the same marketplace format.

## Validate

From the plugin creator skill root, validate the plugin:

```bash
python scripts/validate_plugin.py <repo-root>/plugins/harness-engineering-report
```

## License

MIT
