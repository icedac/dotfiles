---
name: codex_review-pr
description: Run a comprehensive PR review by coordinating specialized review skills for comments, tests, errors, types, general code quality, and simplification; use when asked for a full PR review or to review multiple quality aspects.
---

# Review PR

## Determine scope
- Identify changed files (default to `git diff --name-only` if available).
- If a PR exists, use its diff or user-specified files.

## Review aspects
- comments: comment accuracy and maintainability
- tests: test coverage quality
- errors: silent failures and error handling
- types: type design and invariants
- code: general code review and project rules
- simplify: code simplification after review
- all: run all applicable reviews (default)

## Decide applicability
- Always run code review.
- Run tests review when test files or new behavior appear.
- Run comments review when docs or comments are added.
- Run errors review when error handling or fallbacks change.
- Run types review when new or modified types appear.
- Run simplification after issues are addressed.

## Execution
- Use sequential reviews by default.
- Use parallel reviews only if explicitly requested.

## Aggregate results
- Summarize Critical Issues, Important Issues, Suggestions, and Strengths.
- Provide a short action plan to address findings.

## Output template
# PR Review Summary

## Critical Issues (X found)
- [aspect]: issue description [file:line]

## Important Issues (X found)
- [aspect]: issue description [file:line]

## Suggestions (X found)
- [aspect]: suggestion [file:line]

## Strengths
- notable positives

## Recommended Action
1. Fix critical issues.
2. Address important issues.
3. Consider suggestions.
4. Re-run targeted reviews.
