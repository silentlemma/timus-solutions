# 2046. Whole-word wrapping in a fixed timetable

[Timus 2046](https://acm.timus.ru/problem.aspx?space=1&num=2046) · difficulty 507 · implementation

Original problem by Oleg Dolgorukov, from the Ural Sport Programming Championship 2015.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Draw a table with four lesson rows and three columns, in the order Tuesday, Thursday,
Saturday. Every cell has content width ten. Preserve name words and their
order; put one space between words on the same line. Place each next
word on that line if it fits, including the separating space, otherwise
start a new line. Never split a word. Align content at the top and left,
pad each line to ten characters, and fill unused cell lines with spaces.
A row's height is the maximum wrapped height of its cells, or one if all
are empty. Draw borders with `+` at corners/intersections, `-`
horizontally and `|` vertically. There are no extra headers.

## Input

Read `1≤n≤12` courses. Each course occupies two lines: its name, then a
day and a lesson number. A name has one to five words, separated by
exactly one space with no outside spaces. Each word has one to ten
uppercase or lowercase Latin letters. All names are different. The day
is `Tuesday`, `Thursday` or `Saturday`, and the lesson is `1..4`. No two
courses occupy the same slot. Time limit: 1 second; memory limit: 64 MB.

## Output

Print only the table. Exact text is checked, including every internal
padding space, line boundary and border position. Use a final newline. A
border is `+----------+----------+----------+`; every table line has 34
characters. If `H` is the sum of the four content-row heights, there are
`H+5` lines, at most 25.

## Checking

The output is compared exactly, character by character; only the final
line break may differ.

## Examples

```
9
Physics
Thursday 3
Maths
Tuesday 1
Chemistry
Thursday 1
Physical education
Saturday 2
Astronomy
Saturday 4
Urban geography
Tuesday 4
History
Saturday 1
Modeling
Thursday 2
Biology
Thursday 4
```

```
+----------+----------+----------+
|Maths     |Chemistry |History   |
+----------+----------+----------+
|          |Modeling  |Physical  |
|          |          |education |
+----------+----------+----------+
|          |Physics   |          |
+----------+----------+----------+
|Urban     |Biology   |Astronomy |
|geography |          |          |
+----------+----------+----------+
```

The first row has three one-line names. In the second row, `Physical
education` cannot fit in ten columns: it becomes `Physical` and
`education`. This increases the entire lesson row to two lines; the
missing Tuesday cell and the second line of `Modeling` are blank.
Similarly, `Urban geography` creates the final row's second line. Names
remain in their assigned day and lesson.

## Solution

Wrap each name separately. Keep a current line. If it is empty, put the
next word there. Otherwise append a space and the word when their total
length is at most ten; if not, finish the current line and begin another
with that word. Store the resulting lines in the cell indexed by lesson
minus one and the fixed day index.

After every processed word, all finished lines contain the longest
consecutive word prefix that fits from their starting word, and the
current line contains exactly the remaining processed words in order.
Appending a fitting word preserves this invariant. If it does not fit,
any line containing it after the current words would exceed width ten,
so starting a new line is precisely the required rule. Every word
individually fits, hence wrapping never overflows or loses a word.

For each lesson compute the maximum of one and its three cell heights.
Print that many content lines. At level `r`, each cell contributes its
line `r` if present, otherwise an empty string; pad with spaces to width
ten. This preserves the independently wrapped text and gives top/left
alignment. The chosen height fits every cell and leaves the required one
line for an entirely empty row. Printing a top border and a border after
each lesson places all five horizontal borders correctly. Unique slots
guarantee no course is overwritten.

Let `L` be the sum of name lengths, `C=3`, `W=10`, and `H≤20` the sum of
row heights. Time and space are `O(L+WCH)`, including buffered output;
streaming ports use less output storage. Here `L≤648` and output is at
most 875 bytes.

## Language notes

Read each full name line, not one whitespace-delimited token. Account
for the separator when testing whether a word fits; equality with ten
still fits. Keep the fixed day order regardless of input order. Preserve
blank rows, extra blank lines within shorter cells and all right
padding; do not trim rendered lines. Uppercase and lowercase letters
remain unchanged.

All five ports use the same greedy wrapping and grid. Go's scanner
safely handles the bounded name length; Java uses typed lists and a
small output builder; Rust copies each wrapped string into owned
storage. Python builds independent cell lists and uses space padding.
CPython 3.12 is selected.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2046_implementation.cpp](2046_implementation.cpp) | G++ 13.2 x64 | implementation | O(L+WCH) | AC | 0.015 s | 436 KB |
| [2046_implementation.go](2046_implementation.go) | Go 1.14 x64 | implementation | O(L+WCH) | AC | 0.031 s | 1112 KB |
| [2046_implementation.java](2046_implementation.java) | Java 1.8 | implementation | O(L+WCH) | AC | 0.093 s | 580 KB |
| [2046_implementation.py](2046_implementation.py) | Python 3.12 x64 | implementation | O(L+WCH) | AC | 0.078 s | 536 KB |
| [2046_implementation.rs](2046_implementation.rs) | Rust 1.75 x64 | implementation | O(L+WCH) | AC | 0.015 s | 232 KB |
