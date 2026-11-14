# 1253. Expanding obituary templates

[Timus 1253](https://acm.timus.ru/problem.aspx?space=1&num=1253) · difficulty 690 · strings

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
capped just above 10⁶, since eight levels of ten references can reach
10⁸ · 1000 characters. If the cycle check passes and `size(1)` ≤ 10⁶, the
text is written out by the same recursion. Time is `O(S + L + 10^N)`, or
`O(N(S + L))` in Python, for input size S and output length L.

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

## Optimized solutions

The C++ variant measures the expansion first and then writes literal spans directly to buffered output. It skips references whose expansion is empty and keeps no buffer for the full result. With S input characters, L output characters and N templates, the running time is O(S + NL) and the extra space is O(S + N). The metrics come from submission 11317000.

Java 1.8 stores templates as byte arrays, measures the expansion, then writes literal spans through a buffer without building the complete result. Submission 11317131 took 0.062 s and 432 KB; the base took 0.109 s and 6088 KB.

Rust 1.75 x64 parses templates into literal spans and references, measures the expansion, then writes spans through a buffer without materializing the result. Submission 11317130 took 0.015 s and 212 KB; the base took 0.015 s and 2032 KB.

Python 3.12 x64 computes lengths before output, caches expansions of at most 4096 bytes and writes longer expansions in pieces. Submission 11317128 took 0.062 s and 660 KB; the base took 0.078 s and 4356 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322206 · Go 1.14 x64 №11322207 · Java 1.8 №11322208 · Python 3.12 x64 №11322209 · Rust 1.75 x64 №11322210.

Go computes expansion lengths before writing and streams literal spans and references. When the output is large, it caches expansions that fit in a fixed buffer. Go 1.14 x64, submission 11322833. Time 0.015 → 0.015 s, memory 940 → 400 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1253_strings.cpp](1253_strings.cpp) | G++ 13.2 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 2264 KB | 11322206 |
| [1253_strings.go](1253_strings.go) | Go 1.14 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 940 KB | 11322207 |
| [1253_strings.java](1253_strings.java) | Java 1.8 | strings | O(S + L + 10^N) | AC | 0.109 s | 6088 KB | 11322208 |
| [1253_strings.py](1253_strings.py) | Python 3.12 x64 | strings | O(N(S + L)) | AC | 0.078 s | 4356 KB | 11322209 |
| [1253_strings.rs](1253_strings.rs) | Rust 1.75 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 2032 KB | 11322210 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1253_strings_optimized.cpp](1253_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(S + NL) | AC | 0.015 s | 172 KB | 11317000 |
| [1253_strings_optimized.py](1253_strings_optimized.py) | Python 3.12 x64 | strings | O(S + NL) | AC | 0.062 s | 660 KB | 11317128 |
| [1253_strings_optimized.rs](1253_strings_optimized.rs) | Rust 1.75 x64 | strings | O(S + NL) | AC | 0.015 s | 212 KB | 11317130 |
| [1253_strings_optimized.java](1253_strings_optimized.java) | Java 1.8 | strings | O(S + NL) | AC | 0.062 s | 432 KB | 11317131 |
| [1253_strings_optimized.go](1253_strings_optimized.go) \* | Go 1.14 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 400 KB | 11322833 |

\* The marked versions have room to improve in the ratings.
