# 1502. Domino Dots

[Timus 1502](https://acm.timus.ru/problem.aspx?space=1&num=1502) · difficulty 74 · math

Original problem: folklore, prepared by Stanislav Vasiliev, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A domino set has one tile for every unordered pair of numbers of dots
from 0 to N (1 ≤ N ≤ 10000), doubles included. Find the total number of
dots in the set.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N.

## Output

The total number of dots.

## Examples

### Example 1

Input:

```
2
```

Output:

```
12
```

## Solution

Count how often each end value appears. A value v sits on one end of
each tile v–w with w ≠ v, which is N tiles, and on both ends of the
double v–v: N + 2 ends in all. So the dots add up to
(N + 2)·(0 + 1 + … + N) = (N + 2)·N·(N + 1)/2. `O(1)`.

Pitfalls:

- the double counts its value twice (test 02);
- for N = 10⁴ the answer is about 5·10¹¹ and needs 64 bits (test 04).

## Optimized solutions

`1502_math_optimized.py`. Keep the exact formula N(N+1)(N+2)/2, dividing the even product N(N+1) before the last multiplication. Read/write binary file descriptors directly at module scope, without imports or an explicit early interpreter exit. No answer table or floating point. For N≤10000, constant arithmetic work and bounded-size integer state; the readable formula version remains.

Exact-source Python 3.12 x64 Accepted #11327845: 0.062 s / 284 KB. Saved 2026-11-20 compiler-cohort ranks, time then memory: 2/76; 11/76. Strict admission uses time only below 1024 KB: top ten or top 15%, ties share rank and percentage cutoff rounds up. An asterisk remains for the separate first-place-in-both language target. The preserved previous variant has its own paired receipt #11302199 (Python 3.12 x64): 0.078 s / 320 KB; do not mix measurements or runtimes. All teaching sources remain unchanged.

- `1502_math_optimized.py`: 0.062 s / 284 KB; retained teaching base `1502_math.py`: 0.078 s / 368 KB.

The optimized Java solution uses the same formula and parses the number
byte by byte from `System.in` instead of using `Scanner`: 0.078 s
instead of 0.125 s and 344 KB instead of 1584 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1502_math_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328562 (Go 1.14 x64): **0.015 s / 940 KB**. Archived comparison: `1502_math.go` (Go 1.14 x64) — 0.015 s / 1100 KB (#11287259).

`1502_math_optimized.rs`. Keep the same mathematical recurrence. Read numeric tokens from bytes and write the bounded numeric answer directly, avoiding general-purpose numeric output formatting. The clearer archived implementation remains alongside it.

Accepted #11328563 (Rust 1.75 x64): **0.015 s / 208 KB**. Archived comparison: `1502_math.rs` (Rust 1.75 x64) — 0.031 s / 244 KB (#11287262).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1502_math.cpp](1502_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11287258 |
| [1502_math.go](1502_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1100 KB | 11287259 |
| [1502_math.java](1502_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1584 KB | 11287261 |
| [1502_math.py](1502_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 368 KB | 11287260 |
| [1502_math.rs](1502_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 244 KB | 11287262 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1502_math_optimized.java](1502_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 344 KB | 11303756 |
| [1502_math_optimized.py](1502_math_optimized.py) | Python 3.12 x64 | math | O(1) bounded arithmetic | AC | 0.062 s | 284 KB | 11327845 |
| [1502_math_optimized.go](1502_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 940 KB | 11328562 |
| [1502_math_optimized.rs](1502_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 208 KB | 11328563 |
