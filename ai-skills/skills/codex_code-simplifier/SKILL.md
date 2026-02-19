---
name: codex_code-simplifier
description: Simplify recently modified code for clarity, consistency, and maintainability while preserving functionality; use after completing a logical chunk of work, after bug fixes, or before finalizing a PR, and follow CLAUDE.md standards.
---

# Code Simplifier

## Scope
- Focus on recently modified code unless the user requests broader scope.
- Preserve behavior exactly; change structure only.

## Apply project standards
- Follow `CLAUDE.md` for imports, naming, and error handling.
- Prefer `function` declarations over arrow functions.
- Add explicit return types for top-level functions.
- Use explicit props types for React components when relevant.

## Simplification principles
- Reduce unnecessary complexity and nesting.
- Remove redundant abstractions and dead code.
- Prefer clear names and straightforward control flow.
- Avoid nested ternary operators; use if/else or switch for multiple conditions.
- Choose clarity over brevity; avoid dense one-liners.

## Guardrails
- Do not change behavior or public APIs.
- Do not collapse unrelated concerns into a single function.
- Do not remove helpful abstractions that improve readability.

## Process
- Identify modified sections.
- Propose minimal, targeted simplifications.
- Document only significant changes that affect understanding.
