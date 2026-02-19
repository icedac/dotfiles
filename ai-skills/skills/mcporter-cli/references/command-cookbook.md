# MCPorter Command Cookbook

Use this file when `SKILL.md` is not enough and exact command variants are needed.

## Discovery

```bash
npx mcporter list
npx mcporter list context7 --schema
npx mcporter list context7 --all-parameters
npx mcporter list --json
npx mcporter list --verbose
```

## Safe Tool Calls

Prefer server-dot-tool plus key-value args:

```bash
npx mcporter linear.list_issues assignee=me
npx mcporter call linear.search_documentation query=automations
npx mcporter call context7.resolve-library-id libraryName=react
```

Function-call syntax is supported, but use it only when needed:

```bash
npx mcporter call 'linear.create_comment(issueId: "ENG-123", body: "Looks good!")'
```

## OAuth and Connection Setup

```bash
npx mcporter auth vercel
npx mcporter auth https://mcp.linear.app/mcp
npx mcporter auth --json vercel
```

## Atlassian MCP (Proven Session Recovery)

Add a named entry in `config/mcporter.json`:

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

Re-auth cleanly:

```bash
npx mcporter auth mcp-atlassian-com-mcp --reset --oauth-timeout 300000 --log-level debug
```

Validate token and connectivity:

```bash
cat ~/.mcporter/credentials.json
npx mcporter list mcp-atlassian-com-mcp --json
npx mcporter call mcp-atlassian-com-mcp.atlassianUserInfo
npx mcporter call mcp-atlassian-com-mcp.getAccessibleAtlassianResources
```

Important:
- Run Atlassian `auth`, `list`, and `call` commands sequentially when using fixed callback port `3334`.
- If auth exits non-zero but credentials were saved, verify with `list` and `call` before clearing tokens again.

## Ad-hoc MCP Targets

```bash
npx mcporter list --http-url https://mcp.linear.app/mcp --name linear
npx mcporter call --http-url https://mcp.linear.app/mcp --name linear list_issues assignee=me
npx mcporter call --stdio "bun run ./local-server.ts" --name local-tools
```

Persist when repeated:

```bash
npx mcporter list --http-url https://mcp.linear.app/mcp --name linear --persist config/mcporter.local.json
```

## Config Management

```bash
npx mcporter config list
npx mcporter config get linear
npx mcporter config add linear https://mcp.linear.app/mcp
npx mcporter config remove linear
npx mcporter config import cursor --copy
```

## Generated Artifacts

### Generate standalone CLI

```bash
npx mcporter generate-cli --server linear --bundle dist/linear.js
npx mcporter generate-cli "npx -y chrome-devtools-mcp@latest"
npx mcporter inspect-cli dist/linear.js
```

### Generate TypeScript types/client

```bash
npx mcporter emit-ts linear --mode types --out types/linear-tools.d.ts
npx mcporter emit-ts linear --mode client --out clients/linear.ts
npx mcporter emit-ts linear --json
```

## Daemon Operations

```bash
npx mcporter daemon status
npx mcporter daemon start
npx mcporter daemon stop
npx mcporter daemon restart
```

Enable logs while debugging:

```bash
npx mcporter daemon start --log
npx mcporter daemon start --log-file /tmp/mcporter-daemon.log
```

## Helpful Flags

```bash
--config <path>
--root <path>
--log-level <debug|info|warn|error>
--oauth-timeout <ms>
--tail-log
--output <format>
--raw
--json
--all-parameters
--http-url <url>
--stdio "<command>"
--env KEY=value
--cwd <path>
--name <server-name>
--persist <config-path>
```

## Troubleshooting Sequence

1. Verify server visibility:
```bash
npx mcporter list <server> --schema
```
2. Verify auth:
```bash
npx mcporter auth <server-or-url>
```
3. Retry call with structured output:
```bash
npx mcporter call <server.tool> <args> --output json
```
4. For stdio issues, inspect daemon/log behavior:
```bash
npx mcporter daemon status
```

## Minimal TypeScript Patterns

```ts
import { callOnce } from "mcporter";

const result = await callOnce({
  server: "context7",
  toolName: "resolve-library-id",
  args: { libraryName: "react" },
});

console.log(result);
```

```ts
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const linear = createServerProxy(runtime, "linear");
const docs = await linear.searchDocumentation({ query: "automations" });
console.log(docs.json());
await runtime.close();
```
