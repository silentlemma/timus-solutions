# 1219. A million letters with no letter, pair or triple too common

[Timus 1219](https://acm.timus.ru/problem.aspx?space=1&num=1219) · difficulty 121 · constructive

Original problem by Pavel Atnashev and Leonid Volkov, from the Seventh Ural State University Collegiate Programming Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Print 1,000,000 lowercase Latin letters such that every letter occurs at
most 40,000 times, every two consecutive letters at most 2,000 times and
every three consecutive letters at most 100 times.

Time limit: 1 second. Memory limit: 64 MB.

## Input

There is no input.

## Output

One line with the letters.

## Checking

Any sequence that meets the three limits is accepted.

## Examples

There is no input, and the statement gives no example output.

## Solution

Spread the million letters as evenly as possible. There are 26 letters,
`26² = 676` pairs and `26³ = 17,576` triples, so a perfectly even spread
gives about 38,462, 1,479 and 57 occurrences, all under the limits.

A de Bruijn sequence of order 3 over 26 letters is a cycle of 17,576
letters in which every triple appears exactly once as three consecutive
letters, going around the cycle. Repeating it end to end keeps every
window of three letters a window of the cycle, so after about 57 copies
every triple appears 56 or 57 times, every pair 26 times as often and
every letter 676 times as often: at most 38,532, 1,482 and 57 here. The
cycle comes from the classic construction that joins the Lyndon words
whose length divides 3, in lexicographic order. `O(L)` for `L = 10⁶`.

Pitfalls:

- the windows that cross from one copy to the next are cyclic windows of
  the sequence, so they do not break the balance;
- a random sequence would probably pass too, but its largest triple count
  would only be about 90, close to the limit.

The output was checked against all three limits, and the counts above are
its actual maxima.

## Optimized solutions

The optimized C++ solution builds the cycle directly as 17,576 bytes,
one per letter, and writes it 56 times with `fwrite`, followed by its
first 15,744 letters, instead of filling a string of a million letters;
the output is the same: {1219_constructive_optimized.cpp}.

The optimized Go solution turns the cycle into a block of 17,576 bytes,
one per letter, and writes it 56 times through `bufio`, followed by its
first 15,744 letters, instead of filling a slice of a million bytes; the
output is the same: {1219_constructive_optimized.go}.

The optimized Java solution builds the cycle directly as 17,576 bytes,
one per letter, and writes it 56 times, followed by its first
15,744 letters, instead of keeping an `int` array and a byte array of a
million entries each; the output is the same:
{1219_constructive_optimized.java}.

The optimized Python solution builds the cycle directly in a `bytearray`
of 17,576 letters and writes it 56 times, followed by its first
15,744 letters, instead of creating a list of numbers and a string of a
million letters; the output is the same:
{1219_constructive_optimized.py}.

The optimized Rust solution turns the cycle into a block of
17,576 bytes, one per letter, and writes it 56 times through a
`BufWriter`, followed by its first 15,744 letters, instead of collecting
a vector of a million bytes; the output is the same:
{1219_constructive_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1219_constructive_optimized.cpp`: time reduction +0.00%; memory
  reduction +91.89%; base: `1219_constructive.cpp`.

- `1219_constructive_optimized.go`: time reduction +0.00%; memory
  reduction +38.11%; base: `1219_constructive.go`.

- `1219_constructive_optimized.java`: time reduction +75.81%; memory
  reduction +95.58%; base: `1219_constructive.java`.

- `1219_constructive_optimized.py`: time reduction +60.26%; memory
  reduction +86.97%; base: `1219_constructive.py`.

- `1219_constructive_optimized.rs`: time reduction +0.00%; memory
  reduction +80.53%; base: `1219_constructive.rs`.

## Language notes

- All languages generate the cycle with the same recursive construction
  and write the whole line at once.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1219_constructive.cpp](1219_constructive.cpp) | G++ 13.2 x64 | constructive | O(L) | AC | 0.001 s | 1184 KB | 11283683 |
| [1219_constructive.go](1219_constructive.go) | Go 1.14 x64 | constructive | O(L) | AC | 0.015 s | 2624 KB | 11283684 |
| [1219_constructive.java](1219_constructive.java) | Java 1.8 | constructive | O(L) | AC | 0.062 s | 8868 KB | 11283687 |
| [1219_constructive.py](1219_constructive.py) | Python 3.12 x64 | constructive | O(L) | AC | 0.078 s | 3224 KB | 11283686 |
| [1219_constructive.rs](1219_constructive.rs) | Rust 1.75 x64 | constructive | O(L) | AC | 0.001 s | 2404 KB | 11283688 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1219_constructive_optimized.cpp](1219_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(L) | AC | 0.001 s | 96 KB | 11304363 |
| [1219_constructive_optimized.go](1219_constructive_optimized.go) | Go 1.14 x64 | constructive | O(L) | AC | 0.001 s | 1624 KB | 11304367 |
| [1219_constructive_optimized.java](1219_constructive_optimized.java) | Java 1.8 | constructive | O(L) | AC | 0.001 s | 392 KB | 11304365 |
| [1219_constructive_optimized.py](1219_constructive_optimized.py) \* | Python 3.12 x64 | constructive | O(L) | AC | 0.031 s | 420 KB | 11304366 |
| [1219_constructive_optimized.rs](1219_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(L) | AC | 0.015 s | 468 KB | 11304368 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
