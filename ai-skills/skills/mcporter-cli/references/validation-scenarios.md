# Validation Scenarios (RED/GREEN Notes)

This file records lightweight pressure tests used while authoring this skill.

## Scenario 1: Fast command recommendation under time pressure

### Prompt shape
User asks for a quick MCP call example and expects a command they can paste immediately.

### RED baseline (before hardening)
- Suggested `emit-ts` without `--mode`.
- Suggested positional `generate-cli linear` without explicit selector flag.
- Rationalization: "It probably defaults correctly; this is faster."

### GREEN behavior (after hardening)
- Updated examples to:
  - `npx mcporter emit-ts linear --mode types --out ...`
  - `npx mcporter generate-cli --server linear --bundle ...`
- Added `Quick Reference` table with validated commands.

## Scenario 2: Complex arguments with spaces

### Prompt shape
User wants a call command containing sentence text.

### RED baseline (before hardening)
- Risk of providing deeply quoted inline command syntax.
- Rationalization: "One command with escapes is shorter."

### GREEN behavior (after hardening)
- Added `Escape-Safe Calling Pattern` using shell variables in a script file.
- Added explicit rule: move nested payloads to TypeScript runtime instead of shell escaping.

## Scenario 3: Ad-hoc server reuse confusion

### Prompt shape
User calls an ad-hoc URL once, then expects alias reuse without persistence.

### RED baseline (before hardening)
- Risk of omitting persistence guidance.
- Rationalization: "The printed slug should just work later."

### GREEN behavior (after hardening)
- Added clear instruction: ad-hoc aliases are reusable only after `--persist` or config add.
- Added this check in `Common Mistakes` and `Rationalization Table`.

## Scenario 4: Validation of skill load path

### Test
- `superpowers-codex use-skill mcporter-cli`

### Result
- Skill loads successfully from `/Users/icedac/.codex/skills/mcporter-cli/SKILL.md`.

## Scenario 5: Atlassian OAuth recovery after reset and browser session errors

### Prompt shape
User expects Atlassian MCP to work from project-level `mcporter list` and direct calls.

### RED baseline (before hardening)
- `--reset` cleared `~/.mcporter/credentials.json`.
- `mcporter auth` returned `401`/`invalid session` style failures.
- Running checks in parallel produced `EADDRINUSE` on callback port.
- Rationalization: "Auth command failed, so token definitely was not saved."

### GREEN behavior (after hardening)
- Registered named server in project config with explicit OAuth settings:
  - `auth: oauth`
  - `oauthRedirectUrl: http://localhost:3334/callback`
- Re-ran auth with debug output and confirmed authorization code receipt.
- Verified saved credentials directly in `~/.mcporter/credentials.json`.
- Confirmed success with sequential checks:
  - `mcporter list mcp-atlassian-com-mcp --json`
  - `mcporter call mcp-atlassian-com-mcp.atlassianUserInfo`

### Key guardrails added to skill
- Treat Atlassian auth/list/call as sequential steps when fixed callback port is used.
- Check credentials cache before repeating destructive resets.
- Recognize transient auth command fallbacks that may occur after tokens are already saved.

## Remaining limits

- `quick_validate.py` requires `pyyaml`; this environment needed a temporary venv to run it.
- No subagent tool was available, so pressure checks were run as manual author validation.
