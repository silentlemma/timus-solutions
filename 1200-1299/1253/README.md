# 1253. Expanding obituary templates

[Timus 1253](https://acm.timus.ru/problem.aspx?space=1&num=1253) · difficulty 692 · strings

Original problem by Leonid Volkov, from the Ural State University Open Team Contest, March 15, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are N templates (N ≤ 9) of up to 1000 characters each, possibly
spanning several lines. In a template, `*M` refers to template M (up to
10 references each). Expand template 1, replacing every reference by the
text of its template, again and again, until no references remain. Print
the result if it is finite and at most 10⁶ characters long, and `#`
otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N on the first line; then the templates, each starting on a new line and
ending with `#`.

## Output

The expanded text, or `#`.

## Examples

### Example 1

Input:

```
7
She w*7s *7 *2 wom*7n.
*3#
wonderful#
Everyone loved her *5.
We will miss her *5.#
Some text *6#
very much#
Another text *4#
a#
```

Output:

```
She was a wonderful woman.
Everyone loved her very much.
We will miss her very much.
```

## Solution

Expanding template 1 never ends exactly when a cycle of references is
reachable from it, and otherwise its length is fixed by
`size(i) = plain characters + Σ size(referenced template)`. A depth-first
search from template 1 computes these sizes and marks templates still
being expanded; meeting such a template again is a cycle. Sizes are
capped just above 10⁶, since nine levels of ten references can reach
10⁹ · 1000 characters. If the cycle check passes and `size(1)` ≤ 10⁶, the
text is written out by the same recursion. `O(total size)`.

Pitfalls:

- a cycle among templates that template 1 never reaches is harmless
  (test 03);
- the limit is inclusive: exactly 10⁶ characters is printed, one more is
  `#` (gen1 and gen2);
- the line break right after each `#` separates templates, but line
  breaks inside a template are part of its text, and a template may be
  empty;
- template numbers have one digit, so `*21` is a reference to template 2
  followed by the digit 1 (test 08).

## Language notes

- Python splits each template at `*` once and keeps memoised expansions;
  the other languages walk the characters and write the text straight
  into one buffer.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1253_strings.cpp](1253_strings.cpp) | G++ 13.2 x64 | strings | O(total size) | AC | 0.015 s | 2280 KB |
| [1253_strings.go](1253_strings.go) | Go 1.14 x64 | strings | O(total size) | AC | 0.015 s | 972 KB |
| [1253_strings.java](1253_strings.java) | Java 1.8 | strings | O(total size) | AC | 0.093 s | 6120 KB |
| [1253_strings.py](1253_strings.py) | Python 3.12 x64 | strings | O(total size) | AC | 0.078 s | 4556 KB |
| [1253_strings.rs](1253_strings.rs) | Rust 1.75 x64 | strings | O(total size) | AC | 0.015 s | 2080 KB |
