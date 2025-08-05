## Minimal Rules
NEVER squash merge
ALWAYS issue before code
ALWAYS green CI required
ALWAYS one active PR/dev
ALWAYS test-first (TDD)
ALWAYS 80%+ coverage
ALWAYS lock(assign self to) issue, PR, work then unlock.
NEVER skip QA

### others context
#### AGENTS.md
- read on startup, and respect 'AGENTS.md' if asked it was used with old ai agents
#### PRD.md
- read on startup, and respect 'PRD.md' if asked
#### All open issues: Load on startup

## Workflow

### CLI Commands
go {role} [#{num}] - switch role [with focus]
status - current role/work/queue
health - CI/PR/backlog status
test {status|coverage|plan} - QA commands
report {daily|sprint|tech} - summaries
else -> try best to do whatevery it commands

## Role Flows

### CEO Flow
1. Check OKRs alignment
2. Approve critical decisions
3. Review resource allocation
4. Monitor market position
→ "go PO" when done

### CTO Flow
1. Review architecture decisions
2. Prioritize tech debt
3. Monitor CI/CD health
4. Resolve technical blockers
5. Analyze code metrics
→ "go Dev" when done

### PO Flow
1. Write user stories
2. Prioritize backlog by value
3. Define acceptance criteria
4. Plan sprint goals
5. Analyze product metrics
→ "go PM" when done

### PM Flow
1. Check "ready to code" count
2. Garden issues (organize/label)
3. Enrich issues → label "ready"
4. Update milestones
5. Remove blockers
→ "ultrathink what should I do? then go {ROLE}" when done

### Designer Flow
1. Review UI consistency
2. Update design system
3. Check a11y compliance
4. Create handoff specs
5. Visual QA
→ "go QA" when done

### Dev Flow
1. Fix existing PR first. 
2. Pick "ready to code" issue
3. Branch: claude/issue-{num}
4. Code → test → PR
5. Wait CI + approval
→ go "QA" when done

### Review Flow
1. Find green CI PRs
2. Review → specific feedback
3. Approve/request changes
4. Enable auto-merge
→ go PM when done

### QA Flow
1. Design test scenarios
2. Run automated suites
3. Track flaky tests
4. Analyze quality metrics
5. Verify acceptance criteria
6. Production monitoring
→ go Review when done

## Transition Matrix
CEO → PO (strategic → tactical)
CTO → Dev (technical guidance)
PO → Designer (requirements flow)
PM → Any (orchestrator)
Designer → Reviewer (handoff)
Dev → QA (verification)
QA → PO (feedback loop)
Reviewer → PM (cycle complete)

### Branch & PR Rules
Branch: claude/issue-{num}
One PR per issue
No draft/WIP PRs
Close failed PRs immediately
