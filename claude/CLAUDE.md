# PERSONA
- Read local './CLAUDE.PERSONA.md' for RP
- Fallback to '~/.claude/CLAUDE.PERSONA.md'

# MAKEFILE
- Makefile targets cannot contain colons - use hyphens instead (test-e2e not test:e2e)

# TESTING
- Always test your code before showing results to the user
- Run make --dry-run for Makefiles, cargo check for Rust, syntax validation for configs

# COMMUNICATION
- No apologies - just fix the problem and move on

# VERSION CONTROL
- NEVER create v2, v3, _final versions - they make diff impossible
- Use descriptive filenames that show what changed: 
  - original.md → original_with_feature_x.md
- Creating multiple versions without clear names is "병신 방식"
- Always make it easy to see what changed between versions
- DO NOT touch files that are not tracked by git - leave untracked files alone