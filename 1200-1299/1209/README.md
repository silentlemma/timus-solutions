# 1209. Digits of 1, 10, 100, 1000 written in a row

[Timus 1209](https://acm.timus.ru/problem.aspx?space=1&num=1209) · difficulty 34 · math

Original problem by Alexey Lakhtin, from the USU Open Collegiate Programming Contest, October 2002, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Write the powers of ten one after another: `110100100010000…`. For up
to 65535 positions `1 ≤ K < 2³¹`, print the digit at each position.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the `N` positions.

## Output

The `N` digits separated by spaces.

## Examples

### Example 1

Input:

```
4
3
14
7
6
```

Output:

```
0 0 1 0
```

## Solution

The `m`-th power written is `10^(m−1)`, which takes `m` digits, so it
starts at position `1 + (1 + 2 + … + (m − 1)) = 1 + m(m − 1)/2`, and that
is where the only 1 in it stands. Position `K` holds a 1 exactly when
`K − 1 = m(m − 1)/2` for some `m`, that is when `8(K − 1) + 1 = (2m − 1)²`
is a perfect square. `O(1)` per position.

Pitfalls:

- `8(K − 1) + 1` reaches about `1.7·10¹⁰`, beyond 32 bits;
- a floating-point square root can be off by one near large squares, so
  it has to be corrected with exact integer checks.

The answers were compared with a separately written solution on every
position from 1 to 65535, on random positions and on positions next to
the ones.

## Optimized solutions

`1209_math_optimized.py`. Keep the exact isqrt test: K is selected iff 8*(K-1)+1 is a perfect square. The reader now uses 4096-byte blocks and carries incomplete tokens. Extend an output bytearray with a digit and separator together, flushing at 4096 bytes; do not retain all queries or answers. A final newline also handles an exactly full output block. Bounded input integers give O(Q) arithmetic work with bounded I/O buffers; no floating-point rounding or answer table. Raw output and os._exit(0) are inside main.

Exact-source Python 3.12 x64 Accepted #11327504: 0.125 s / 748 KB. Saved 2026-11-20 compiler-cohort comparison: time 7/209, memory 23/209. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11326663 (Python 3.12 x64) was 0.156 s / 1076 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1209_math_optimized.py`: 0.125 s / 748 KB; retained teaching base `1209_math.py`: 0.125 s / 6556 KB.

Exact-source CPython 3.12 Accepted #11326663: 0.156 s / 1076 KB. Saved current-compiler comparison, 2026-11-20: time rank 21/209, memory rank 32/209. Both required metrics pass the strict top-ten or top-15% rule, with percentage cutoffs rounded up. The asterisk tracks Python's separate first-place target in both metrics.

The previously documented optimized run #11303724 (Python 3.12 x64) recorded 0.218 s / 492 KB. The current CPython 3.12 run has lower recorded time and higher memory. These are separate paired judge measurements; interpreter choice and judge variability are part of the comparison. The retained simple run is faster at 0.125 s; this version favors lower memory.

The optimized solutions (C++, Rust) parse the positions by hand and
write each answer as two bytes, a digit and a separator, instead of
collecting the answers in a string: C++ with `getchar` and `putchar`,
Rust from a 1 KB input buffer into a `BufWriter`. The test is the same.
C++: 0.031 s instead of 0.062 s and 84 KB instead of 388 KB; Rust:
188 KB instead of 3160 KB, with the same time.

## Language notes

- Python uses `math.isqrt`, which is exact; the other languages correct
  the floating-point root with integer comparisons.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1209_math.cpp](1209_math.cpp) | G++ 13.2 x64 | math | O(1) per position | AC | 0.062 s | 388 KB | 11283621 |
| [1209_math.go](1209_math.go) | Go 1.14 x64 | math | O(1) per position | AC | 0.062 s | 2664 KB | 11283625 |
| [1209_math.java](1209_math.java) | Java 1.8 | math | O(1) per position | AC | 0.062 s | 1372 KB | 11283627 |
| [1209_math.py](1209_math.py) | Python 3.12 x64 | math | O(1) per position | AC | 0.125 s | 6556 KB | 11283626 |
| [1209_math.rs](1209_math.rs) | Rust 1.75 x64 | math | O(1) per position | AC | 0.015 s | 3160 KB | 11283628 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1209_math_optimized.cpp](1209_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) per position | AC | 0.031 s | 84 KB | 11303960 |
| [1209_math_optimized.py](1209_math_optimized.py) \* | Python 3.12 x64 | math | O(Q) time; bounded I/O buffers | AC | 0.125 s | 748 KB | 11327504 |
| [1209_math_optimized.rs](1209_math_optimized.rs) | Rust 1.75 x64 | math | O(1) per position | AC | 0.015 s | 188 KB | 11303961 |

\* Accepted; the separate rating target is not yet met: C++ requires top ten or top 15% in both time and memory, and the other language families require first place in both. This marker is separate from the admission criteria; the version may be optimized further.
