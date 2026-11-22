# 1068. The sum of all integers between 1 and N

[Timus 1068](https://acm.timus.ru/problem.aspx?space=1&num=1068) · difficulty 37 · math

Original problem from the trial round of the ACM ICPC Northeastern European Regional Contest 2000–2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An integer `N` with `|N| ≤ 10000` is given. Print the sum of all integers
between 1 and `N`, both included.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`.

## Output

The sum.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
-3
```

Output:

```
-5
```

## Solution

The numbers between 1 and `N` form one interval of `|N − 1| + 1` numbers,
whichever side of 1 `N` is on. The sum of an interval is its length times
the average of its ends, `(1 + N) / 2`. The product `(1 + N) · (|N − 1| + 1)`
is always even, since its two factors add up to an odd number when
`N ≤ 0` and are `N + 1` and `N` otherwise, so the division is exact. `O(1)`.

Pitfalls:

- `N` may be zero or negative: then the interval runs from `N` up to 1, and
  `N(N + 1)/2` gives a wrong answer, for example 0 instead of 1 for
  `N = 0`;
- the sum reaches about `5 · 10^7` in absolute value, which fits 32-bit
  integers; the solutions still multiply in 64 bits (Python in its
  unbounded integers).

The answers were checked against adding the numbers one by one.

## Optimized solutions

`1068_math_optimized.java`. Keep the inclusive arithmetic-progression sum (1+N)*(abs(N-1)+1)/2, including zero and negative N. For |N|<=10000 the intermediate product fits int. A 256-byte input buffer, 128-byte output buffer and reusable digit array replace per-byte input calls and general decimal printing. Constant arithmetic work and auxiliary storage; the readable base remains.

Exact-source Java 1.8 Accepted #11327461: 0.062 s / 364 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/1616, memory 20/1616. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11303705 was 0.125 s / 368 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1068_math_optimized.java`: 0.062 s / 364 KB; retained teaching base `1068_math.java`: 0.109 s / 1568 KB.

`1068_math_optimized.go`. Keep the inclusive arithmetic progression from 1 to N: (abs(N−1)+1)(N+1)/2 in int64 handles positive, zero and negative N without a loop. Use bounded 256-byte input and 64-byte output buffers with Go 1.14 syscall.Read/Write, retrying EINTR and partial writes and handling zero-byte EOF. This removes fmt/bufio/os.File initialization overhead. Linux tests and Windows cross-builds establish functional/build checks; the paired memory figures below come from our own exact Windows judge Accepted. Preserve the readable teaching source.

Compared with `1068_math.go`: time 0.031 s → 0.015 s; memory 1072 KB → 260 KB.

`1068_math_optimized.py`. Keep the arithmetic-progression formula (1+N)*(abs(N-1)+1)//2, which also covers zero and negative N. Read the bounded integer from raw bytes instead of input(), and avoid the wrapper call. Time and arithmetic storage remain O(1) under |N|<=10000. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1068_math.py`: time 0.078 s → 0.109 s; memory 448 KB → 196 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1068_math_optimized.py`: time place 644/739, memory place 1/739 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1068_math.cpp](1068_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11278883 |
| [1068_math.go](1068_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1072 KB | 11278886 |
| [1068_math.java](1068_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1568 KB | 11278891 |
| [1068_math.py](1068_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 448 KB | 11278889 |
| [1068_math.rs](1068_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB | 11278892 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1068_math_optimized.java](1068_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.062 s | 364 KB | 11327461 |
| [1068_math_optimized.py](1068_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 196 KB | 11324832 |
| [1068_math_optimized.go](1068_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 260 KB | 11325649 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
