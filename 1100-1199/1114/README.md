# 1114. Placing up to A and B identical balls of two colours into N boxes

[Timus 1114](https://acm.timus.ru/problem.aspx?space=1&num=1114) · difficulty 194 · combinatorics, math

Original problem from the first selection contest for the Bulgarian IOI team.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N` boxes in a row (`1 ≤ N ≤ 20`), `A` identical red balls and
`B` identical blue balls (`0 ≤ A, B ≤ 15`). Any number of balls, of
either colour, may go into each box, boxes may stay empty and balls may
stay unused. Count the different placements.

Time limit: 0.6 seconds. Memory limit: 64 MB.

## Input

`N A B` on one line.

## Output

The number of placements.

## Checking

Compare one exact integer token. New Python was executed on all 5120 legal triples plus 12 repository inputs under both CPython 3.12 and PyPy 3.10; additionally each runtime launched 12 fresh processes for the repository inputs. The expected answers were crosschecked by independent box-by-box distribution DP, summing all allowed used counts for each colour. This includes zero balls and the maximum answer above signed 64 bits. The retained exact Java source separately has its saved source-bound coefficient and unsigned-product proof over all 5120 triples.

## Examples

### Example 1

Input:

```
2 1 1
```

Output:

```
9
```

## Solution

Treat the colours independently. A placement of at most `A` red
balls in `N` labelled boxes uniquely extends to exactly `A` balls in
`N + 1` boxes: put every unused ball in the extra box. Conversely, discard
that extra box. Stars and bars counts these weak compositions as
`C(N + A, N)`. Multiplying the independent red and blue counts gives
`C(N + A, N) × C(N + B, N)`.

The readable C++, Go, Java and Rust bases build Pascal's triangle with
`TOP = 40`, then make two lookups. Time and space are `O(TOP²)`; the
needed indices are at most 35. Python calls `math.comb` twice without
a table. All bounds are fixed, so these programs are `O(1)` with respect
to the stated input limits. All five original Accepted files remain.

The requested coefficients are at most `C(35,15) = 3247943160 < 2^32`;
this does not mean every entry of the larger Pascal table fits 32 bits.
The maximum answer is `10549134770590785600`, above signed 64 bits but
below `2^64`. C++, Go and Rust use unsigned 64-bit products; Java keeps
the product's low 64 bits and prints them with `Long.toUnsignedString`.
Python integers are unbounded.

## Optimized solutions

Java computes each binomial coefficient multiplicatively: after step i, r=C(N+i,i), so the next division is exact. Every pre-division product is at most 35*C(35,15)=113678010600 and fits signed long. The final answer can exceed signed 64 bits but remains below 2^64; Java keeps the low 64 bits and uses Long.toUnsignedString. This removes the Pascal table while preserving all readable bases.

Java qualifies by its 77.4% memory reduction; its one-tick time difference is not reliable speedup evidence.

The Python optimization keeps the same stars-and-bars formula and preserves the short math.comb base. It reads text through the existing standard input stream, imports only the standard streams from sys, and computes each coefficient by exact multiplicative divisions. After step i, coefficient=C(N+i,i), so division by i is exact. Each factor is at most C(35,15)=3247943160; every pre-division product is at most 113678010600. Multiply the two completed factors only once, then write the exact decimal string. Python's unbounded final integer handles the maximum 10549134770590785600, above signed 64 bits. No Pascal table or math-module import is needed. Time is O(A+B) coefficient steps with bounded-size arithmetic under these constraints.

Its own Accepted 11309624 used PyPy 3.10 x64: 0.125 s and 240 KB, against the unchanged CPython 3.12 base at 0.078 s and 372 KB. The measured memory reduction is 35.5%; runtime increases 60.3%. Admission is by memory only, and the rating shortfall remains marked with a star. These are two actual compiler-specific runs, not metrics transferred between interpreters.

- `1114_combinatorics_math.java`: 0.093 s / 372 KB; base `1114_combinatorics.java`: 0.109 s / 1648 KB; relative change: time -14.7%, memory -77.4%.
- `1114_combinatorics_optimized.py`: 0.125 s / 240 KB; base `1114_combinatorics.py`: 0.078 s / 372 KB; relative change: time +60.3%, memory -35.5%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1114_combinatorics.cpp`; covering source `1114_combinatorics.cpp`; time/memory places 1/1, other-author entries 45/45.

- Go: preferred teaching base `1114_combinatorics.go`; covering source `1114_combinatorics.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1114_combinatorics.java`; covering source `1114_combinatorics_math.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1114_combinatorics.py`; covering source `1114_combinatorics_optimized.py`; time/memory places 22/1, other-author entries 24/24.

- Rust: preferred teaching base `1114_combinatorics.rs`; covering source `1114_combinatorics.rs`; time/memory places 1/1, other-author entries 1/1.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1114_combinatorics.cpp](1114_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(TOP^2) | AC | 0.015 s | 140 KB | 11279222 |
| [1114_combinatorics.go](1114_combinatorics.go) | Go 1.14 x64 | combinatorics | O(TOP^2) | AC | 0.015 s | 1060 KB | 11279223 |
| [1114_combinatorics.java](1114_combinatorics.java) | Java 1.8 | combinatorics | O(TOP^2) | AC | 0.109 s | 1648 KB | 11279225 |
| [1114_combinatorics.py](1114_combinatorics.py) | Python 3.12 x64 | combinatorics | O(1) under fixed bounds | AC | 0.078 s | 372 KB | 11279224 |
| [1114_combinatorics.rs](1114_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(TOP^2) | AC | 0.015 s | 232 KB | 11279226 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1114_combinatorics_math.java](1114_combinatorics_math.java) | Java 1.8 | combinatorics, math | O(A+B) exact coefficient steps; bounded storage | AC | 0.093 s | 372 KB | 11308284 |
| [1114_combinatorics_optimized.py](1114_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O(A+B) exact coefficient steps; bounded storage | AC | 0.125 s | 240 KB | 11309624 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
