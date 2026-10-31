# 1335. White Thesis

[Timus 1335](https://acm.timus.ru/problem.aspx?space=1&num=1335) · difficulty 182 · math

Original problem by Den Raskovalov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given N, 2 ≤ N ≤ 30 000, find three different whole numbers A, B and C
between N² and (N + 1)² inclusive such that A² + B² is divisible by C,
or print `No solution` if there are none. Any such triple is accepted.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The number N.

## Output

A, B and C, or `No solution`.

## Checking

The checker accepts any three different numbers in the range with
A² + B² divisible by C. A triple always exists, so `No solution` is
never accepted.

## Examples

### Example 1

Input:

```
2
```

Output:

```
8 6 4
```

### Example 2

Input:

```
1000
```

Output:

```
1000000 1000756 1000976
```

## Solution

Take C = N² + 1, A = N² and B = N² + N + 1. Modulo C the first number
is −1 and the second is N, so A² + B² ≡ 1 + N², which is C itself, and
the sum is divisible by C. All three lie between N² and (N + 1)², since
N² + N + 1 < N² + 2N + 1, and they are different for every N ≥ 1. So
the answer always exists and `No solution` never happens. `O(1)`.

The triple was found by listing all solutions with A = N² for small N
and noticing (N² + N + 1, N² + 1) among them every time.

Pitfalls:

- the numbers reach about 9 · 10⁸, and the squares, which only a
  checker needs, reach 8 · 10¹⁷, more than 32 bits hold;
- the samples show other triples; any correct one is accepted.

## Optimized solutions

The optimized Java solution prints the same triple, but reads N by hand
from the bytes of the input instead of with `Scanner`, whose regular
expressions take time and memory to set up even for a single number:
{1335_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1335_math_optimized.java`: time reduction +12.80%; memory reduction
  +77.67%; base: `1335_math.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1335_math.cpp](1335_math.cpp).
- [1335_math.go](1335_math.go).
- [1335_math.rs](1335_math.rs).

- All five solutions print the same triple.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1335_math.cpp](1335_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11285027 |
| [1335_math.go](1335_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1064 KB | 11285028 |
| [1335_math.java](1335_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1612 KB | 11285030 |
| [1335_math.py](1335_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 392 KB | 11285029 |
| [1335_math.rs](1335_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 244 KB | 11285032 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1335_math_optimized.java](1335_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.109 s | 360 KB | 11307311 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
