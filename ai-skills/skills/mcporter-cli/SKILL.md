---
name: mcporter-cli
description: Use when Codex must discover MCP servers, call MCP tools, complete OAuth setup, inspect or edit MCPorter config, or generate TypeScript clients and standalone CLIs from MCP schemas in terminal workflows.
---

# MCPorter CLI

## Overview

Use MCPorter as the default terminal interface for MCP-first workflows. Prefer shell-safe calls and small script files over long escaped inline strings.

If deeper details are needed for specific flags or edge cases, read `references/command-cookbook.md`.
If this skill is being edited, review `references/validation-scenarios.md` before changing examples.

## Quick Start

1. Discover servers and tools: `npx mcporter list`
2. Inspect one server: `npx mcporter list <server> --schema`
3. Authenticate protected servers: `npx mcporter auth <server-or-url>`
4. Call a tool: `npx mcporter call <server.tool> key=value`
5. Move repeated calls into `.sh` or `.ts` files

## Decision Guide

- Need tool signatures or optional params: `mcporter list <server> --all-parameters`
- Need one-shot MCP call: `mcporter call <server.tool> key=value`
- Need ad-hoc URL or stdio server: `mcporter list --http-url <url>` or `mcporter call --stdio "<cmd>"`
- Need persistence for ad-hoc server aliases: `--persist <config-path>` or `mcporter config add`
- Need reusable TypeScript types/clients: `mcporter emit-ts`
- Need shareable generated CLI artifact: `mcporter generate-cli`
- Need keep-alive stateful stdio transport: `mcporter daemon start` and `mcporter daemon status`

## Quick Reference

| Goal | Command |
| --- | --- |
| List all discovered servers | `npx mcporter list` |
| Show one server + schema | `npx mcporter list context7 --schema` |
| Authenticate OAuth server | `npx mcporter auth vercel` |
| Call with shell-safe args | `npx mcporter call linear.search_documentation query=automations` |
| Ad-hoc HTTPS server | `npx mcporter list --http-url https://mcp.linear.app/mcp --name linear` |
| Generate types only | `npx mcporter emit-ts linear --mode types --out types/linear-tools.d.ts` |
| Generate standalone CLI | `npx mcporter generate-cli --server linear --bundle dist/linear.js` |
| Inspect daemon status | `npx mcporter daemon status` |

## Atlassian OAuth Runbook

Use this exact flow for `https://mcp.atlassian.com/v1/mcp`.

1. Register a named server in project config:

```json
{
  "mcpServers": {
    "mcp-atlassian-com-mcp": {
      "baseUrl": "https://mcp.atlassian.com/v1/mcp",
      "auth": "oauth",
      "oauthRedirectUrl": "http://localhost:3334/callback"
    }
  }
}
```

2. Run a clean auth attempt:
`npx mcporter auth mcp-atlassian-com-mcp --reset --oauth-timeout 300000 --log-level debug`

3. If auth exits non-zero, verify token state before retry loops:
`cat ~/.mcporter/credentials.json`

4. Validate connectivity with sequential commands:
`npx mcporter list mcp-atlassian-com-mcp --json`
`npx mcporter call mcp-atlassian-com-mcp.atlassianUserInfo`

5. When using fixed redirect port `3334`, avoid parallel `list`/`call`/`auth` runs to prevent port collisions.

## Escape-Safe Calling Pattern

Prefer key-value calls and variables in scripts:

```bash
#!/usr/bin/env bash
set -euo pipefail

issue_id="ENG-123"
comment_body="Looks good!"

npx mcporter call linear.create_comment issueId="$issue_id" body="$comment_body"
```

When payloads become nested or hard to quote, switch to TypeScript runtime calls instead of escaping JSON in shell.

## TypeScript Runtime Pattern

```ts
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const context7 = createServerProxy(runtime, "context7");

const lib = await context7.resolveLibraryId({ libraryName: "react" });
console.log(lib.text());

await runtime.close();
```

## Common Mistakes

- Calling OAuth-protected servers before `mcporter auth`: run auth first.
- Using ad-hoc slugs without `--persist`: reuse the original `--http-url` or `--stdio` flags until persisted.
- Expecting daemon keep-alive for ad-hoc targets: only configured named servers are daemon-managed.
- Debugging with default output only: add `--json`, `--output json`, or `--tail-log` for scriptable diagnostics.
- Running `--reset` without understanding it clears `~/.mcporter/credentials.json` entries.
- Running multiple Atlassian commands in parallel while using `oauthRedirectUrl` on a fixed port.

## Rationalization Table

| Excuse | Reality | Correct action |
| --- | --- | --- |
| "One escaped inline call is faster" | Nested escaping fails often and is hard to debug | Move command into `.sh` or `.ts` file |
| "Auth errors mean server is down" | OAuth and transport failures are distinct | Run `mcporter auth <server>` and retry |
| "Ad-hoc alias should work forever" | Alias is reusable only after persistence | Use `--persist` or `config add` |
| "Any stdio target should stay warm" | Daemon ignores ad-hoc targets | Persist config entry and set lifecycle |
| "Auth exited 1 so no token was saved" | Atlassian flow can save tokens before later transport fallback fails | Check `~/.mcporter/credentials.json`, then test with `list` and `call` |
| "Parallel checks are faster" | Fixed OAuth callback ports can collide (`EADDRINUSE`) | Run Atlassian auth/list/call sequentially |

## Red Flags

- Shell command contains many backslashes or nested quotes
- Same auth/offline failure repeated without checking `--json` envelope
- Repeated ad-hoc calls without persisting a stable server definition
- Generating typed clients manually instead of using `emit-ts`
- `StreamableHTTPClientTransport already started` followed by SSE 400 during auth
- `EADDRINUSE` on `localhost:3334`

## Common Failure Recovery

1. Re-run with diagnostics: `--json` (list/auth) or `--output json` (call)
2. Re-check server visibility: `mcporter list <server> --schema`
3. Re-run auth: `mcporter auth <server-or-url>`
4. Persist ad-hoc definitions if repeatedly used
5. Inspect OAuth cache entry: `cat ~/.mcporter/credentials.json`
6. For Atlassian with fixed redirect port, run one command at a time
7. Use runtime API for complex payload construction
