---
name: codex_pr-review-toolkit
description: Guide selection and coordination of specialized review skills for comments, tests, errors, types, code quality, and simplification; use when deciding which review skills to run for a PR or when combining multiple reviews.
---

# PR Review Toolkit

## Agents
- codex_comment-analyzer: comment accuracy and comment rot
- codex_pr-test-analyzer: test coverage quality
- codex_silent-failure-hunter: error handling and silent failures
- codex_type-design-analyzer: type design and invariants
- codex_code-reviewer: general code quality and CLAUDE.md compliance
- codex_code-simplifier: simplify code after review

## When to use
- After writing code: run codex_code-reviewer.
- After adding docs or comments: run codex_comment-analyzer.
- After changing error handling: run codex_silent-failure-hunter.
- After adding or refactoring types: run codex_type-design-analyzer.
- Before PR: run codex_pr-test-analyzer and codex_code-reviewer, plus any relevant aspect.
- After review passes: run codex_code-simplifier.

## Usage patterns
- Targeted: ask for a specific aspect to trigger a single skill.
- Comprehensive: run all applicable reviews for a PR.
- Parallel vs sequential: default to sequential unless explicitly requested.

## Troubleshooting
- If wrong files are reviewed, specify files or the diff.
- If a skill does not trigger, mention it explicitly.

## Integration
- Focus on changed code, not the entire codebase.
- Re-run relevant reviews after fixes.
