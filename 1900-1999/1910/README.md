# 1910. The Strongest Consecutive Triple

[Timus 1910](https://acm.timus.ru/problem.aspx?space=1&num=1910) · difficulty 34 · implementation

Original problem by Denis Dublennykh, from NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a sequence of positive values, find the three consecutive elements
with the largest sum. Report that sum and the 1-based position of the
middle element. The maximizing triple is guaranteed to be unique.
Limits: 1 second and 64 MB.

## Input

First n, 3≤n≤1000, then n integers aᵢ with 1≤aᵢ≤10⁶.
Whitespace and line breaks are interchangeable separators.

## Output

Print the maximum sum followed by the 1-based middle position.

## Checking

Two exact integers, checked token by token.

## Examples

```
6
1 4 4 4 1 1
```

```
12 3
```

## Solution

Try every section from the second to the next to last as the middle of
the three: add it to its two neighbours and keep the largest sum with
its number. The statement promises that the best triple is unique, so a
strict comparison is enough. `O(n)`; a sum is at most 3·10⁶ and fits a
32-bit integer.

Pitfalls:

- the answer is the number of the middle section, counted from 1;
- with n = 3 there is only one triple.

## Optimized solutions

`1910_implementation_optimized.java`. Java keeps the same rolling triple maximum. Retain only the two preceding values, add each new value, and update the best sum and the one-based middle index on a strict improvement. The stated unique maximum makes this sufficient. Every sum is at most 3000000 and fits int. Fixed byte input and raw numeric output avoid Scanner, concatenated strings and general integer formatting; the input sequence is never stored. Time O(N), auxiliary space O(1).

Exact-source Java 1.8 Accepted #11327450: 0.078 s / 356 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/532, memory 2/532. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11303787 was 0.125 s / 380 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1910_implementation_optimized.java`: 0.078 s / 356 KB; retained teaching base `1910_implementation.java`: 0.156 s / 2372 KB.

The optimized C++ solution does not store the sections: it reads them
one by one with `scanf` and keeps only the two before the current one,
which is all a triple needs: 128 KB instead of 192 KB, with the same
time.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1910_implementation_optimized.rs`. The C entry calls the solver directly and flushes Rust output before returning; the archived ordinary-entry implementation remains available.

Accepted #11328940 (Rust 1.75 x64): **0.015 s / 136 KB**. Archived comparison: `1910_implementation.rs` (Rust 1.75 x64) — 0.031 s / 236 KB (#11303334).

## Language notes

No language needs anything special.

Keep a window of three values while reading the sequence and record the first maximum. Accepted submission 11324269 took 0.140 s and used 240 KB. The simple version took 0.062 s and used 452 KB. The recorded runtime is higher than for the simple version.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1910_implementation.cpp](1910_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 192 KB | 11303319 |
| [1910_implementation.go](1910_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1108 KB | 11303324 |
| [1910_implementation.java](1910_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.156 s | 2372 KB | 11303327 |
| [1910_implementation.py](1910_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.062 s | 452 KB | 11303331 |
| [1910_implementation.rs](1910_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 236 KB | 11303334 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1910_implementation_optimized.cpp](1910_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11303648 |
| [1910_implementation_optimized.java](1910_implementation_optimized.java) | Java 1.8 | implementation | O(N) time; O(1) auxiliary space | AC | 0.078 s | 356 KB | 11327450 |
| [1910_implementation_optimized.py](1910_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(n) | AC | 0.140 s | 240 KB | 11324269 |
| [1910_implementation_optimized.rs](1910_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 136 KB | 11328940 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
