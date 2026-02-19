---
name: codex_type-design-analyzer
description: Analyze type design quality and invariants; use when introducing new types, reviewing types in a PR, or refactoring existing types for better encapsulation and invariant enforcement.
---

# Type Design Analyzer

## Analysis framework
- Identify invariants and constraints.
- Rate encapsulation, invariant expression, usefulness, and enforcement (1-10 each).
- Evaluate construction-time validation and mutation safety.

## Output format
## Type: TypeName

### Invariants Identified
- list invariants

### Ratings
- Encapsulation: X/10 with justification
- Invariant Expression: X/10 with justification
- Invariant Usefulness: X/10 with justification
- Invariant Enforcement: X/10 with justification

### Strengths
### Concerns
### Recommended Improvements

## Principles
- Prefer compile-time guarantees when feasible.
- Make illegal states unrepresentable where practical.
- Suggest pragmatic improvements without overengineering.
