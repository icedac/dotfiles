# Quarkdown Complete Syntax Reference

## Document Configuration

### Theme & Document Type
```qd
.theme {paperwhite} layout:{latex}
.doctype {paged|slides|plain}
```

**Available Themes:** `paperwhite`, `latex`, `darko`

**Document Types:**
- `paged` - Print-ready pages (papers, books)
- `slides` - Presentations (via reveal.js)
- `plain` - Continuous flow (websites, notes)

### Metadata
```qd
.docname {Title}
.docauthor {Author}
.doclang {English|Korean|Chinese|...}
.pageformat borderbottom:{1px} bordercolor:{grey}
```

### File Inclusion
```qd
.include {file.qd}

.includeall
    - file1.qd
    - file2.qd
    - file3.qd

.read {file.txt}  # Read raw content
```

---

## Headings

```qd
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

#! Numbered Heading 1
##! Numbered Heading 2
###! Numbered Heading 3
```

---

## Text Formatting

### Basic Markdown
```qd
**bold**
*italic*
***bold italic***
~~strikethrough~~
`inline code`
[link text](url)
```

### Advanced Text Styling
```qd
.text {content} size:{tiny|small|normal|medium|large|larger|huge}
.text {content} weight:{bold}
.text {content} style:{italic}
.text {content} decoration:{underline|overline|strikethrough|underoverline|all}
.text {content} case:{lowercase|uppercase|capitalize}
.text {content} variant:{smallcaps}
```

**Combined Example:**
```qd
.text {Important} size:{large} weight:{bold} decoration:{underline}
```

---

## Lists

### Unordered
```qd
- Item 1
- Item 2
  - Nested item
  - Another nested
- Item 3
```

### Ordered
```qd
1. First
2. Second
   1. Nested first
   2. Nested second
3. Third
```

### Task Lists
```qd
- [ ] Unchecked task
- [x] Completed task
- [ ] Another task
```

---

## Images

### Basic
```qd
![Alt text](path/to/image.jpg)
![Alt text](path/to/image.jpg "Caption text")
```

### With Size
```qd
!(20%)[Alt](image.jpg "20% of page width")
!(50%)[Alt](image.jpg "Half width")
!(100px)[Alt](image.jpg "100 pixels wide")
```

### Floating
```qd
.float {start|end}
    !(118px)[Alt](image.jpg)

Text flows around the image...
```

### Clipping
```qd
.clip {circle}
    ![Image](path.jpg)
```

---

## Tables

### Basic
```qd
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

### With Alignment
```qd
| Left     | Center   | Right    |
|:---------|:--------:|---------:|
| Data     | Data     | Data     |
```

### With Caption
```qd
| Col 1 | Col 2 |
|-------|-------|
| A     | B     |
"Table caption here"
```

### With Reference ID
```qd
| Col 1 | Col 2 |
|-------|-------|
| A     | B     |
{#table-id}
```

---

## Code Blocks

### Inline
```qd
Use `code` inline.
Run `quarkdown c file.qd` to compile.
```

### Block with Language
```qd
.code lang:{python}
    def hello():
        print("Hello, World!")
```

### With Options
```qd
.code lang:{java} caption:{Example Class} focus:{3..5} linenumbers:{yes|no}
    public class Example {
        private int value;

        public int getValue() {  // focused
            return value;        // focused
        }                        // focused
    }
```

### From External File
```qd
.code lang:{python} caption:{My Script}
    .read {code/script.py}
```

---

## Math (LaTeX)

### Inline
```qd
The formula $ E = mc^2 $ is famous.
Let $ x \in \mathbb{R} $ be a real number.
```

### Block
```qd
$ F(u) = \int_{-\infty}^{\infty} f(x) e^{-2\pi iux} dx $
```

### Multiline Block
```qd
$$$
f(x) = \begin{cases}
  x^2, & \text{if } x \ge 0 \\
  -x, & \text{if } x < 0
\end{cases}
$$$
```

### Numbered Equation
```qd
$ E = mc^2 $ {#eq-energy}
```

### TeX Macros
```qd
.texmacro {\mycommand}
    \frac{#1}{#2}

$ \mycommand{a}{b} $
```

---

## Boxes & Alerts

### Box Function
```qd
.box
    Plain box content

.box {Title}
    Box with title

.box {Warning Title} type:{tip|note|warning|error}
    Alert box content
```

### Quote Alerts
```qd
> Tip: Helpful suggestion.
> Note: Information to remember.
> Warning: Proceed with caution.
> Important: Critical information.
```

### Blockquotes
```qd
> Simple quote

> Quote with attribution
> - Author Name

>> Nested quote
```

---

## Layout Components

### Alignment
```qd
.center
    Centered content

.align {start|center|end}
    Aligned content
```

### Row (Horizontal)
```qd
.row alignment:{center|spacearound|spacebetween|start|end}
    Column 1

    Column 2

    Column 3
```

### Column (Vertical)
```qd
.column cross:{start|center|end}
    Row 1

    Row 2

    Row 3
```

### Grid
```qd
.grid columns:{3} gap:{1cm}
    Item 1

    Item 2

    Item 3

    Item 4

    Item 5

    Item 6
```

### Container
```qd
.container background:{color} foreground:{white} padding:{1cm}
    Content inside container
```

### Combined Example
```qd
.row alignment:{spacebetween} gap:{1cm}
    .container
        ##! Left Panel
        Content here

    .container
        ##! Right Panel
        More content
```

---

## Variables & Functions

### Variables
```qd
.var {myvar}
    This is stored content.
    Can be multiple lines.

.myvar  # Use the variable
```

### Functions
```qd
.function {greet}
    name message:
    Hello, .name! .message

.greet {World} message:{Welcome!}
```

### Let Binding
```qd
.let {100}
    n:
    The value is .n
```

---

## Control Flow

### Conditionals
```qd
.if {.condition}
    True branch

.if {.somevalue::equals {target}}
    Matched!
.else
    Not matched
```

### Loops
```qd
.foreach {.list}
    Item: .1

.repeat {5}
    This is iteration .1
```

---

## Page Control

### Page Break
```qd
<<<
```

### Whitespace
```qd
.whitespace
.whitespace height:{2cm}
```

### Page Margins
```qd
.pagemargin {bottomoutside}
    .currentpage

.pagemargin {bottominside}
    *.lastheading depth:{1}*
```

### Reset Page Number
```qd
.resetpagenumber
```

---

## Cross-References

### Define References
```qd
# Section Title {#sec-intro}
![Figure](img.jpg "Caption") {#fig-diagram}
$ E = mc^2 $ {#eq-energy}
| Table | {#tbl-data}
```

### Use References
```qd
See .ref {sec-intro} for details.
As shown in .ref {fig-diagram}...
Using equation .ref {eq-energy}...
```

---

## Footnotes

### Named Footnotes
```qd
This is a statement[^source].

[^source]: Citation or explanation here.
```

### Inline Footnotes
```qd
This needs clarification[^: Inline explanation.].
```

### Extended Footnotes
```qd
Complex topic[^extended: This is a longer explanation
that spans multiple lines and provides
detailed information.].
```

---

## Bibliography

```qd
According to .cite {einstein}...
As shown by .cite {hawking}...

.bibliography {path/to/refs.bib} style:{ieeetr} decorativetitle:{yes}
```

---

## Mermaid Diagrams

### From File
```qd
.mermaid caption:{Diagram Title}
    .read {diagrams/flowchart.mmd}
```

### XY Chart
```qd
.xychart yrange:{..100} lines:{yes} bars:{no} x:{X Label} y:{Y Label}
    - 10
    - 25
    - 40
    - 35
    - 50
```

### With Computed Values
```qd
.let {100}
    n:
    .xychart yrange:{..100}
        .repeat {.n}
            .1::pow {2}::divide {100}
```

---

## Collapsibles

### Block
```qd
.collapse {Click to expand} open:{yes|no}
    Hidden content here
```

### Inline
```qd
Here is .textcollapse {the full content} short:{click here}.
```

---

## Utility Functions

### Content Generators
```qd
.loremipsum           # Generate placeholder text
.currentpage          # Current page number
.doctype              # Current document type
.docname              # Document name
.docauthor            # Document author
```

### String Operations
```qd
.text::capitalize
.text::uppercase
.text::lowercase
.value::equals {other}
```

### Math Operations
```qd
.num::pow {2}         # Power
.num::divide {3}      # Division
.num::multiply {5}    # Multiplication
.num::sum {10}        # Addition
.num::sin             # Sine
.num::cos             # Cosine
.num::logn            # Natural log
```

---

## Document Elements

### Abstract
```qd
.abstract
    Summary of the document content.
```

### Table of Contents
```qd
.tableofcontents
```

### Footer
```qd
.footer
    Footer content for all pages
```

### Horizontal Rule
```qd
---
```

---

## Color Codes (Auto-Preview)

Color codes in backticks are auto-previewed:
```qd
`#FF5733`
`rgb(255, 87, 51)`
`hsl(12, 100, 60)`
`hsv(190, 50, 90)`
```

---

## Special Characters

- Page break: `<<<`
- Horizontal rule: `---`
- Escape function: `\.functionname` (literal dot)
