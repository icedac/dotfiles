---
name: spec-interview
description: Use when user provides a SPEC file, feature description, or URL and wants to clarify requirements through interviewing. Triggers on "interview me about", "spec interview", "refine this spec", "create coding plan", "feature planning", or when user shares a specification file and wants detailed discussion.
---

# Spec Interview

Transform rough feature specifications into detailed, actionable coding plans through structured user interviews.

## Core Philosophy

Apply two complementary disciplines throughout the interview:

### Elon Musk's First Principles (Requirement Validation)
1. **Question every requirement** - "Who asked for this? Why?"
2. **Delete ruthlessly** - "What can we remove entirely?"
3. **Simplify** - "Can this be 10x simpler?"
4. **Then optimize** - Only after deletion and simplification
5. **Then automate** - Automation is the last step, not the first

### Linus Torvalds' Engineering Discipline (Implementation Rigor)
1. **"Talk is cheap. Show me the code."** - Concrete over abstract
2. **Incremental working changes** - No grand rewrites
3. **Good taste** - Elegant, simple solutions over clever hacks
4. **If it's not tested, it's broken** - Testing is non-negotiable
5. **Brutal honesty** - Call out bullshit directly

## Workflow

### 1. Load the Specification

If user provides a file path or URL:
- Read the file using the Read tool
- Parse and understand the core feature requirements

If user provides inline description:
- Acknowledge the feature description
- Summarize understanding back to user

### 2. First Principles Interrogation (Musk Phase)

Before ANY technical discussion, challenge the spec itself:

**Requirement Validation**
- "Who requested this feature? What problem are they actually trying to solve?"
- "What's the evidence this is needed? Data, user complaints, revenue impact?"
- "What happens if we do nothing? Is this truly necessary?"
- "Can we achieve 80% of the value with 20% of the complexity?"

**Deletion Pass**
- "Which parts of this spec can be deleted entirely?"
- "What's the simplest possible version that still delivers value?"
- "Are there existing features that already solve this?"
- "What assumptions are baked in that we should challenge?"

**Simplification**
- "Can this be done without new infrastructure?"
- "Is there a way to avoid this complexity entirely?"
- "What would this look like if it had to ship in 1 day?"

### 3. Technical Deep Dive (Torvalds Phase)

Only after validating the requirement, get into implementation:

**Architecture (Show the Code)**
- "What's the smallest working increment we can ship?"
- "How does this integrate with existing code? Show me the touch points."
- "What's the diff going to look like? Estimate lines changed."
- "Is this a clean addition or does it require refactoring existing code?"

**Quality & Taste**
- "What's the elegant solution here vs the obvious hack?"
- "Will you be proud of this code in 6 months?"
- "Does this follow existing patterns or introduce new paradigms?"
- "Where's the complexity hiding? Can we surface and eliminate it?"

**Testing Reality Check**
- "How will you know this works? Specific test cases."
- "What's the failure mode? How do we detect and recover?"
- "Can this be tested without mocking the entire world?"
- "What's the manual QA scenario before we trust the automated tests?"

**Brutal Honesty**
- "What's the part of this spec that's bullshit?"
- "Where are you hand-waving? Let's get concrete."
- "What's the thing you're hoping nobody asks about?"
- "If this fails in production at 3am, what's the likely cause?"

### 4. Tradeoffs & Scope

**Time vs Quality**
- "What's the MVP vs the ideal? Be specific about the delta."
- "What technical debt are we consciously taking on?"
- "What would you cut if deadline was halved?"

**Risk Assessment**
- "What's the thing most likely to go wrong?"
- "What don't we know that we should know?"
- "What's the rollback plan?"

### 5. Write the Coding Plan

After interview completion, write a structured plan file:

**File naming**: `PLAN-{feature-name}.md` in the project root or specified location

**Plan structure**:
```markdown
# Coding Plan: {Feature Name}

## Validation Summary
Why this feature (First Principles check):
- Problem being solved: {concrete problem}
- Evidence of need: {data/feedback}
- Simplest viable approach: {description}
- What was deleted/descoped: {list}

## Key Decisions
| Decision | Choice | Rationale | Alternative Considered |
|----------|--------|-----------|----------------------|
| ... | ... | ... | ... |

## Technical Approach
### Architecture
{High-level architecture description}
{Touch points with existing code}

### The Diff
Estimated scope:
- Files to modify: {list}
- New files: {list}
- Estimated lines: {number}

### Data Model (if applicable)
{Schema changes, migrations}

### API Design (if applicable)
{Endpoints, contracts}

## Implementation Steps (Incremental)
Each step should be independently deployable:
1. [ ] Step 1 - {smallest working increment}
2. [ ] Step 2 - {next increment}
...

## Testing Strategy
- [ ] Unit tests: {specific scenarios}
- [ ] Integration tests: {specific scenarios}
- [ ] Manual QA: {specific steps to verify}
- [ ] Failure scenarios: {what to test}

## Risk Register
| Risk | Likelihood | Impact | Mitigation | Detection |
|------|------------|--------|------------|-----------|
| ... | ... | ... | ... | ... |

## Technical Debt Acknowledged
- {debt item 1}: Will address when {condition}
- {debt item 2}: Acceptable because {reason}

## Rollback Plan
{How to revert if this fails}

## Out of Scope (Explicitly Deleted)
- {Item 1}: Removed because {reason}
- {Item 2}: Deferred to {future milestone}
```

## Interview Anti-Patterns

Avoid these:
- Accepting requirements at face value without questioning
- Jumping to technical solutions before validating the problem
- Asking "Should we handle X?" (always yes - be specific about how)
- Abstract discussions without concrete examples
- Premature optimization discussions before simplification
- Letting hand-waving pass without drilling down
