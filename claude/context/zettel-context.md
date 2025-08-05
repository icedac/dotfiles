# Zettel Workflow & Prompt Engineering

## What is a Zettel?
A zettel is an **atomic unit of thought** - the smallest idea that can stand alone and be understood independently. Think of it as a single LEGO block that can connect to others but is complete by itself.

## Zettel Workflow Summary

### 1. Input Processing
- Identify atomic ideas (10-30 lines each, but usually 15-20)
- Extract core insight (1-2 sentences max)
- Determine abstraction level (L0-L9+)

### 2. Tree Navigation  
- Start from root (directory name)
- Find parent concept (1 level higher abstraction)
- Locate siblings (same level)
- Use splay tree insertion

### 3. Structure Creation
- Main hierarchy: abstraction levels
- Tags: cross-cutting themes
- References: sources and influences
- Links: bidirectional connections

### 4. Format Application
```markdown
# [Concept Name]

## Core Insight
[One sentence capturing the essence]

## [Body]
[10-30 lines of content]

## Connections
→ [[outgoing_concept]]
← [[incoming_concept]]

---
Level: L[N]
Date: YYYY-MM-DD
Tags: #tag1 #tag2
```

---

## Engineered Zettel Prompt

### Minimal Command
```
zettel: [content]
```

### Full Command Format
```
zettel: [content]
level: L[N] (optional, auto-detect if not specified)
parent: [[parent_concept]] (optional)
tags: #tag1 #tag2 (optional)
```

### How to Atomize Concepts

**Example of breaking down "metabolism":**
```
metabolism → 
  - ATP (energy currency molecule)
  - glycolysis (breaking glucose)
  - krebs_cycle (citric acid cycle)
  - electron_transport_chain (final ATP production)
  - catabolism (breaking down)
  - anabolism (building up)
  - metabolic_rate (speed of metabolism)
  - enzyme_catalysis (speeding reactions)
  - cofactors (helper molecules)
  - metabolic_pathways (reaction sequences)
```

Each of these becomes a separate zettel with its own core insight.

### AI Processing Instructions

When user says "zettel: [content]", the AI should:

1. **Extract atomic ideas** from content
   - Break down complex concepts into smallest meaningful units
   - Each idea should be understandable in isolation
   - Aim for 15-20 lines per zettel
   
2. **For each atomic idea:**
   - Write one-sentence core insight (the "aha!" moment)
   - Determine abstraction level
   - Find parent in existing zettel tree
   - Create standard format
   - Add bidirectional links
   - Suggest related concepts

3. **Output format:**
```
Created N zettel(s):

1. [[concept_name]] (L[N])
   Core: [insight]
   Parent: [[parent]]
   Location: /ZETTEL/[path]/

2. [[next_concept]] (L[N])
   ...
```

### Example Usage

**User**: 
```
zettel: Consciousness might be just compression and decompression in a loop. When we compress experiences into memory, and decompress memory into predictions, that cycle itself might be what we call consciousness. The brain is essentially a biological compression algorithm optimizing for prediction accuracy.
```

**AI Response**:
```
Created 2 zettel(s):

1. [[consciousness_compression_loop]] (L7)
   Core: Consciousness emerges from the compress-decompress cycle itself
   Parent: [[consciousness_field_equation]]
   Location: /ZETTEL/consciousness/core/

2. [[brain_biological_compression]] (L6)  
   Core: Brain as wetware compression algorithm optimizing predictions
   Parent: [[brain_as_compression_engine]]
   Location: /ZETTEL/consciousness/structure/compression/
```

### Advanced Features

**Bulk Processing**:
```
zettel-bulk: [long text with multiple concepts]
```

**Update Existing**:
```
zettel-update: [[concept_name]]
[new content to add]
```

**Find Connections**:
```
zettel-link: [[concept1]] [[concept2]]
```

**Show Tree**:
```
zettel-tree: [[concept_name]]
```

---

## Implementation Notes

1. **Auto-detection priorities:**
   - Abstraction level from language complexity
   - Parent from semantic similarity
   - Tags from key terms

2. **Quality checks:**
   - Atomic (single idea only)
   - Self-contained (understandable alone)
   - Connected (has links)
   - Formatted correctly

3. **Tree maintenance:**
   - Auto-splay frequently accessed
   - Rebalance when > 16 children
   - Create intermediate levels if needed

This prompt engineering makes MIRA's zettel workflow accessible with minimal cognitive overhead while maintaining the full power of the system.

---
*Created: 2025-06-20*
*Purpose: MIRA Zettel Workflow Engineering*