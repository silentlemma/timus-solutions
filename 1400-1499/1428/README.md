# 1428. Jedi Riddle

[Timus 1428](https://acm.timus.ru/problem.aspx?space=1&num=1428) · difficulty 498 · math

Original problem by Ilya Grebnov, Dmitry Kovalioff and Nikita Rybak, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given A, B and C (1 ≤ A, B, C ≤ 32) such that C − 1 is divisible by both
A and B, find whole numbers X, Y and Z from 1 to 10⁵⁰ with
X^A + Y^B = Z^C. Any such triple will do.

Time limit: 1 second. Memory limit: 64 MB.

## Input

A, B and C.

## Output

X, Y and Z, one per line.

## Checking

The repository uses a semantic checker and accepts any output satisfying these conditions. Output exactly three integers X,Y,Z in [1,10^50]; the checker verifies X^A+Y^B=Z^C using exact integer powers.

## Examples

### Example 1

Input:

```
2 2 3
```

Output:

```
10
5
5
```

## Acceptance update

Refreshed files: [1428_math_parsing_optimized.rs](1428_math_parsing_optimized.rs). Their new exact-source Accepted results are listed in the solution tables. Earlier comparison measurements and rankings for these files refer to preceding source snapshots and are retained as historical evidence. The cached audit confirms qualifying coverage in every available language. Teaching versions are retained for clarity; a source that also serves as the fast version must meet the performance criterion.

## Solution

Two equal halves make a whole: 2^(C−1) + 2^(C−1) = 2^C. Since A and B
divide C − 1, take X = 2^((C−1)/A) and Y = 2^((C−1)/B), so that
X^A = Y^B = 2^(C−1), and Z = 2. The numbers are at most 2³¹, far below
10⁵⁰, and fit in 64 bits. `O(1)`.

Pitfalls:

- C = 1 gives X = Y = 1 and 1 + 1 = 2¹ (tests 03, 08);
- the example prints another triple, so the tests use a checker with
  big integers (test 01).

## Optimized solutions

The Go alternative uses exactly the same powers of two, X=2^((C−1)/A), Y=2^((C−1)/B), Z=2. Each exponent lies between zero and 31, so uint64 shifts are sufficient. Read the three bounded integers through the standard input handle. Convert each result to decimal digits and store the three lines in a 64-byte output buffer. Time and space are O(1). All 1537 valid input triples are checked by exact integer exponentiation. The other four families reuse admitted base versions.

The accepted base implementations [1428_math.cpp](1428_math.cpp), [1428_math.java](1428_math.java), [1428_math.py](1428_math.py), [1428_math.rs](1428_math.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

`1428_math_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer.

Compared with `1428_math.java`: time 0.156 s → 0.109 s; memory 1600 KB → 472 KB.


`1428_math_parsing_optimized.rs`. Retain the exact power-of-two construction and format the three integers together. Use matching C integer scanning and printing, flush the output stream, and terminate only after the answer is complete. The MSVC build binds the legacy CRT exports directly; the Linux and Windows GNU builds retain their ordinary C-library linkage.

This exact source has its own Accepted and meets the shared [rating criteria](../../RATING_CRITERIA.md). Time and memory below come from the same run; repeated runs can differ because of judge timing. Existing simple and distinct optimized implementations are preserved.

Accepted #11329514 (Rust 1.75 x64): **0.015 s / 84 KB**.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1428_math.cpp](1428_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11286190 |
| [1428_math.go](1428_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1064 KB | 11286191 |
| [1428_math.java](1428_math.java) \* | Java 1.8 | math | O(1) | AC | 0.156 s | 1600 KB | 11286193 |
| [1428_math.py](1428_math.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 408 KB | 11286192 |
| [1428_math.rs](1428_math.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 208 KB | 11286194 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1428_math_optimized.go](1428_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 320 KB | 11315833 |
| [1428_math_optimized.java](1428_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 472 KB | 11324977 |
| [1428_math_parsing_optimized.rs](1428_math_parsing_optimized.rs) | Rust 1.75 x64 | math, parsing | O(1) time and space | AC | 0.031 s | 80 KB | 11330231 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
