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

`1335_math_optimized.java`. Keep the triple A=N², B=N²+N+1, C=N²+1. Compute N² once in int: N<=30000 bounds the largest output by 900030001. Reusable 1024-byte input/output buffers and a digit array avoid string concatenation and general long printing. The modular identity and distinctness proof remain; O(1) bounded arithmetic and space. Every valid N from 2 through 30000 was checked against the independent 64-bit identity.

Exact-source Java 1.8 Accepted #11327452: 0.093 s / 356 KB. Saved 2026-11-20 compiler-cohort comparison: time 4/41, memory 1/41. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11307311 was 0.109 s / 360 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1335_math_optimized.java`: 0.093 s / 356 KB; retained teaching base `1335_math.java`: 0.125 s / 1612 KB.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

`1335_math_optimized.py`. Keep the construction A=N², B=N²+N+1, C=N²+1 and compute N² once. Modulo C the first two values are -1 and N, so A²+B² is divisible by C; the three values are distinct and in the allowed interval for N>=2. Bounded arithmetic and storage O(1). Reuse the one computed square and print all three integers in one call. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1335_math.py`: time 0.078 s → 0.125 s; memory 392 KB → 168 KB.

`1335_math_optimized.rs`. Keep the construction A=N², B=N²+N+1, C=N²+1 and compute N² once. Modulo C the first two values are -1 and N, so A²+B² is divisible by C; the three values are distinct and in the allowed interval for N>=2. Bounded arithmetic and storage O(1). Use signed i64 arithmetic and direct numeric output; N<=30000 bounds every constructed value well below i64 capacity. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1335_math.rs`: time 0.046 s → 0.015 s; memory 244 KB → 56 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1335_math_parsing_optimized.go`. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments.

Accepted #11328885 (Go 1.14 x64): **0.015 s / 908 KB**. Archived comparison: `1335_math.go` (Go 1.14 x64) — 0.031 s / 1064 KB (#11285028).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1335_math_optimized.py`: time place 18/26, memory place 1/26 in this comparable sample.

`1335_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

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
| [1335_math_optimized.java](1335_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 356 KB | 11327452 |
| [1335_math_optimized.py](1335_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 168 KB | 11324910 |
| [1335_math_optimized.rs](1335_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 56 KB | 11325094 |
| [1335_math_parsing_optimized.go](1335_math_parsing_optimized.go) | Go 1.14 x64 | math, parsing | O(1) | AC | 0.015 s | 908 KB | 11328885 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
