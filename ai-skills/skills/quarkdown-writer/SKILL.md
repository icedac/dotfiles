---
name: quarkdown-writer
description: Write and edit Quarkdown (.qd) documents with proper modular structure. Use when creating documents, presentations, papers, or any .qd file. Triggers on "write qd", "create quarkdown", "make presentation", "문서 작성".
allowed-tools: Read, Write, Edit, Bash(python:*)
---

# Quarkdown Document Writer

Create professional Quarkdown documents with proper modular architecture.

## Quick Start

For complete syntax reference, see [syntax-reference.md](syntax-reference.md).

## Project Structure (MANDATORY)

Always use modular file structure:

```
project/
├── main.qd          # Entry: theme, doctype, includes
├── setup.qd         # Metadata, footer, abstract, TOC
├── content.qd       # Main content (or split further)
├── images/          # Image assets
├── code/            # Code snippets for .read
└── diagrams/        # Mermaid .mmd files
```

## Core Templates

### main.qd (Entry Point)

```qd
.theme {paperwhite} layout:{latex}
.doctype {paged}

.includeall
    - setup.qd
    - introduction.qd
    - chapter1.qd
    - conclusion.qd
```

**Document Types:**
- `paged` - Papers, books (print-ready)
- `slides` - Presentations
- `plain` - Web/continuous flow

### setup.qd (Metadata)

```qd
.docname {Document Title}
.docauthor {Author Name}
.doclang {English}

.footer
    .docname

.center
    #! .docname
    .docauthor (c) 2024

---

.abstract
    Document summary here.

.tableofcontents
```

### Content Module

```qd
# Section Title

Introduction paragraph.

## Subsection

Content with **bold** and *italic*.

.box {Key Point} type:{tip}
    Important information here.

<<<

# Next Section
```

## Essential Syntax

### Function Calls
```qd
.functionname {positional-arg} named:{value}
    Body content (indented)
```

### Headings
```qd
# H1          #! Numbered H1
## H2         ##! Numbered H2
### H3        ###! Numbered H3
```

### Layout
```qd
.center
    Centered content

.row alignment:{spacebetween} gap:{1cm}
    Column 1

    Column 2

.grid columns:{3}
    Item 1
    Item 2
    Item 3
```

### Boxes & Alerts
```qd
.box {Title} type:{tip|note|warning|error}
    Content

> Tip: Quick tip here.
> Warning: Caution message.
```

### Math (LaTeX)
```qd
Inline $ E = mc^2 $ math.

Block equation:
$ \int_0^\infty f(x) dx $

Multiline:
$$$
f(x) = \begin{cases}
  x^2 & x \ge 0 \\
  -x & x < 0
\end{cases}
$$$
```

### Images
```qd
![Alt](path.jpg "Caption")
!(50%)[Alt](path.jpg "50% width")

.clip {circle}
    ![Image](path.jpg)
```

### Code
```qd
.code lang:{python} caption:{Example}
    .read {code/example.py}

.code lang:{javascript} focus:{3..5}
    function hello() {
        console.log("Hello");
    }
```

### Variables & Functions
```qd
.var {myvar}
    Reusable content

.myvar

.function {greet}
    name:
    Hello, .name!

.greet {World}
```

### Control Flow
```qd
.foreach {.items}
    Item: .1

.repeat {5}
    Repeated .1 times

.if {.condition}
    True branch
.else
    False branch
```

### Page Control
```qd
<<<                         # Page break
.whitespace height:{2cm}    # Vertical space
```

### Cross-References
```qd
# Section {#sec-intro}
![Figure](img.jpg) {#fig-1}
$ E=mc^2 $ {#eq-energy}

See .ref {sec-intro} and .ref {fig-1}.
```

### Footnotes
```qd
Text with footnote[^label].

[^label]: Footnote content.

Inline[^: Direct footnote content.].
```

## Compilation

Use the bundled tooling script:

```bash
# Check Quarkdown installation
python scripts/qd_tools.py status

# Install Quarkdown (if needed)
python scripts/qd_tools.py install

# Compile document
python scripts/qd_tools.py compile main.qd

# Live preview (watch + browser)
python scripts/qd_tools.py preview main.qd

# PDF export
python scripts/qd_tools.py pdf main.qd

# Create new project
python scripts/qd_tools.py create my_project paged
```

## Workflow

1. Create `main.qd` with theme and includes
2. Create `setup.qd` with metadata
3. Create content modules (one topic per file)
4. Use `<<<` for page breaks between major sections
5. Compile: `python scripts/qd_tools.py preview main.qd`
