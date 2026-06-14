# Agent Marketplace Starter

This repository is a starter layout for publishing a Codex marketplace plugin from GitHub.

## Repository Layout

```text
.
|-- .agents/
|   `-- plugins/
|       `-- marketplace.json
`-- plugins/
    `-- agent-marketplace-starter/
        |-- .codex-plugin/
        |   `-- plugin.json
        `-- skills/
            `-- marketplace-starter/
                `-- SKILL.md
```

## How It Works

- `.agents/plugins/marketplace.json` is the marketplace catalog.
- `plugins/agent-marketplace-starter/.codex-plugin/plugin.json` is the plugin manifest.
- `plugins/agent-marketplace-starter/skills/` contains Codex skills shipped by the plugin.

## Publish To GitHub

Create a new GitHub repository, then push this folder:

```bash
git init
git add .
git commit -m "Create Codex marketplace plugin starter"
git branch -M main
git remote add origin https://github.com/YOUR_ORG/agent-marketplace-starter.git
git push -u origin main
```

## Register In Codex

After publishing, another user can register this marketplace by adding the repository's marketplace root.

```bash
codex plugin marketplace add https://github.com/YOUR_ORG/agent-marketplace-starter
codex plugin add agent-marketplace-starter@agent-marketplace-starter
```

If your installed marketplace name differs, check the name in `.agents/plugins/marketplace.json` and use:

```bash
codex plugin add agent-marketplace-starter@<marketplace-name>
```

## Adapting This Starter

Rename the plugin folder, update `.codex-plugin/plugin.json`, and update the matching entry in `.agents/plugins/marketplace.json`.

For multi-host distribution, keep the core logic portable:

- Codex: ship `.codex-plugin/plugin.json`, `skills/`, optional MCP/app config.
- Claude Code: expose shared logic through MCP or Claude-specific commands/config.
- Other harnesses: expose the same tools through MCP or an HTTP API when possible.

MCP is the best cross-agent compatibility layer because many hosts can consume it without sharing the same marketplace format.

## Validate

From the plugin creator skill root, validate the plugin:

```bash
python scripts/validate_plugin.py <repo-root>/plugins/agent-marketplace-starter
```

## License

MIT
