# 2025. Maximize pairs across groups

[Timus 2025](https://acm.timus.ru/problem.aspx?space=1&num=2025) · difficulty 60 · math

Original problem by Alexey Danilyuk, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Partition `n` distinct objects into between two and `k` nonempty groups.
Every object must belong to exactly one group. An unordered pair
contributes one if its two objects are in different groups, and zero
otherwise. Find the largest possible total number of contributing pairs.
Only the maximum count is required, not a partition.

There are `1 ≤ T ≤ 10` independent test cases. Each satisfies `2 ≤ k ≤ n
≤ 10000`. Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line contains `T`. Each of the next `T` lines contains `n` and `k`.

## Output

For each case, print one integer on a separate line, in the input order.

## Checking

Outputs are compared token by token.

## Examples

```
3
6 3
5 5
4 2
```

```
12
10
4
```

## Solution

Using all k groups is best: with fewer groups some group has at least
two objects, and splitting it adds pairs. With group sizes s₁, …, s_k
the number of pairs from different groups is (n² − Σ sᵢ²) / 2, so the
sum of squares should be as small as possible. That happens when the
sizes differ by at most one, since moving an object from a group of
size a to a group of size b ≤ a − 2 lowers the sum of squares. So
r = n mod k groups get q + 1 objects and the other k − r get
q = n div k, and the answer is (n² − (k − r)·q² − r·(q + 1)²) / 2.
`O(1)` per test.

For n = 6, k = 3 the groups are 2, 2, 2 and the answer is 12.

Pitfalls:

- every pair counts once, hence the division by two;
- integer arithmetic only, no average in floating point.

## Optimized solutions

`2025_math_optimized.java`. Java keeps the balanced-group formula. Let q=N/K and r=N%K; r groups have q+1 people and K-r have q. The answer is (N*N-((K-r)*q*q+r*(q+1)*(q+1)))/2, computed in long. With N<=10000 it is at most 49995000, so the final int conversion is exact. Raw 128-byte input/output buffers avoid BufferedInputStream, StringBuilder and per-answer strings. At most ten answers use at most 90 bytes; the output helper also flushes safely if full. Time O(T), auxiliary space O(1), with O(1) arithmetic per test.

Exact-source Java 1.8 Accepted #11327424: 0.093 s / 344 KB. Saved 2026-11-20 compiler-cohort comparison: time 4/650, memory 4/650. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11302162 was 0.14 s / 372 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `2025_math_optimized.java`: 0.093 s / 344 KB; retained teaching base `2025_math.java`: 0.125 s / 1628 KB.

`2025_math_optimized.cpp`. Keep the balanced-group sum-of-squares formula with exact long long arithmetic. Replace scanf with a 256-byte refillable input buffer plus a sentinel byte; tokens crossing a refill are still read fully. Collect answers in a fixed 128-byte output buffer and write once instead of calling printf for every test. At most ten answers are needed, each at most 49995000, so at most 90 output bytes fit. O(1) arithmetic per test, O(T) total and fixed auxiliary storage. The simple mathematical version remains unchanged.

Exact-source G++ 13.2 x64 Accepted #11327412: 0.015 s / 76 KB. The complete public rating downloaded on 2026-11-21 contains 3066 rows. After excluding our author and selecting current C/C++ compilers, time rank is 1/463 and memory rank 2/463; equal measurements share a rank and times below 0.015 s use the 0.015 s floor. Both top-ten targets pass, so no asterisk. With memory below 1024 KB, strict admission also permits time only. The prior optimized run #11303661 was 0.031 s / 128 KB; the retained simple C++ run #11292869 is 0.031 s / 444 KB. These are separate paired measurements, not mixed minima. No repeat submission was needed.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`2025_math_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328621 (Go 1.14 x64): **0.015 s / 980 KB**. Archived comparison: `2025_math.go` (Go 1.14 x64) — 0.031 s / 1128 KB (#11292876).

## Language notes

No language needs anything special.

Subtract the within-group pairs from the total. Count the extra pairs contributed by the larger groups separately. Accepted submission 11324249 took 0.140 s and used 224 KB. The simple version took 0.078 s and used 448 KB. The recorded runtime is higher than for the simple version.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2025_math.cpp](2025_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 444 KB | 11292869 |
| [2025_math.go](2025_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1128 KB | 11292876 |
| [2025_math.java](2025_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1628 KB | 11303364 |
| [2025_math.py](2025_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 448 KB | 11292879 |
| [2025_math.rs](2025_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB | 11292891 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2025_math_optimized.cpp](2025_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 76 KB | 11327412 |
| [2025_math_optimized.java](2025_math_optimized.java) | Java 1.8 | math | O(T) time; O(1) auxiliary space | AC | 0.093 s | 344 KB | 11327424 |
| [2025_math_optimized.py](2025_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.140 s | 224 KB | 11324249 |
| [2025_math_optimized.go](2025_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 980 KB | 11328621 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
