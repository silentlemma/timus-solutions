# 2102. Does a number have exactly twenty prime factors

[Timus 2102](https://acm.timus.ru/problem.aspx?space=1&num=2102) · difficulty 147 · number_theory

Original problem by Vladimir Leskov, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Tell whether the prime factorisation of n has exponents adding up to
exactly 20, that is whether n is a product of exactly 20 primes counted
with multiplicity. The limits are 2 seconds and 64 MB.

## Input

n, 1 ≤ n ≤ 10¹⁸.

## Output

`Yes` or `No`.

## Examples

### Example 1

Input:

```
2
```

Output:

```
No
```

### Example 2

Input:

```
1048576
```

Output:

```
Yes
```

### Example 3

Input:

```
10000000000
```

Output:

```
Yes
```

## Solution

Divide n by every d from 2 up to B = 2·10⁶ while d² ≤ n, counting the
prime factors removed. If the loop stops because d² exceeds what is
left, the rest is 1 or a prime and adds 0 or 1. Otherwise the rest is at
least B² = 4·10¹², so the removed part is at most 10¹⁸ / B², less than
2¹⁸, which means fewer than 18 factors so far; the rest has no factor
below B and is at most 10¹⁸ < B³, so it adds at most two. The total
cannot reach 20, and the answer is No. The work is O(min(sqrt n, B)).

In the third example 10¹⁰ = 2¹⁰ · 5¹⁰ has 20 prime factors.

## Optimized solutions

`2102_number_theory_optimized.java`. Keep the exactly-20-prime-factors test. Remove twos and threes, then scan 6k-1/6k+1 divisors; enough checks the minimum possible remaining product using division before multiplication to avoid overflow. With at most two missing factors, test the square shortcut: only a square of a prime can supply exactly two. Math.sqrt is only a candidate, accepted after exact long root*root==n; a missed square safely uses the unchanged wheel fallback. After removing at least 18 factors the residual is at most 10^18/2^18, so root primality needs divisors below 1400 and fallback divisors are bounded by 1953125. Parse the single long byte by byte and write constant answer bytes. No answer table or probabilistic primality. Actual Java code passed 315488 exact factor cases and 100000 overflow-safe product-bound comparisons. Teaching trial division remains.

Exact-source Java 1.8 Accepted #11327435: 0.109 s / 468 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/78, memory 1/78. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. Both metrics rank first, so the separate language target also passes; no asterisk. The previously documented optimized run #11304532 was 0.14 s / 400 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `2102_number_theory_optimized.java`: 0.109 s / 468 KB; retained teaching base `2102_number_theory.java`: 0.125 s / 1592 KB.

`2102_number_theory_optimized.py`. Keep the target of exactly 20 prime factors with multiplicity. Remove powers of two and three, then try divisors 6k-1 and 6k+1. While more than two factors are needed, divisor**remaining>n proves rejection. Once at most two remain, use exact isqrt: a square succeeds only when two factors are needed and its root is prime. At least 18 factors have then been removed, so the residual is at most 10^18/2^18; trial division of its square root for primality is below 1400. Nonsquares keep the wheel fallback, whose divisor bound is at most 1953125 in this phase. Fixed input bounds give constant storage; no float rounding, probabilistic primality or answer table. This Accepted is on PyPy 3.10; the old CPython measurement is a separate runtime pair. Top-level raw output precedes os._exit(0).

Exact-source PyPy 3.10 x64 Accepted #11327440: 0.125 s / 928 KB. Saved 2026-11-20 compiler-cohort comparison: time 8/28, memory 6/28. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11304531 (Python 3.12 x64) was 0.265 s / 424 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `2102_number_theory_optimized.py`: 0.125 s / 928 KB; retained teaching base `2102_number_theory.py`: 0.453 s / 388 KB.

`2102_number_theory_optimized.cpp`. Keep exact prime-factor counting and the lower bound on the remaining product. For positive n≤10^18, ctz counts all factors two at once; divide out threes, then test only divisors 6k±1. While more than two prime factors are needed, multiply the lower bound in unsigned 128-bit arithmetic and stop as soon as it exceeds the remainder. Before that multiplication the bound is at most 10^18 and the divisor at most about 10^9, so the temporary fits 128 bits. Once at most two factors remain, trial division uses the original square bound. No zero is passed to ctz, and the decision remains exactly twenty prime factors with multiplicity.

Exact-source Accepted #11326999: 0.015 s / 108 KB. Saved G++ 13.2 comparison, 2026-11-20: time rank 1/113, memory rank 1/113.

### Measured gains

Every retained optimized version has Accepted. It qualifies through top-ten or top-15% ranks on both metrics, top-30% ranks on both metrics with an improvement over the base in at least one, or at least a 30% reduction in time or memory against the same-language base. Negative reduction means increased cost. A star concerns the separate language rating target.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [2102_number_theory.rs](2102_number_theory.rs).

Exact-source Accepted #11326999: 0.015 s / 108 KB; retained simple version: 0.031 s / 116 KB. Both time values are compared with the 0.015 s timer floor.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2102_number_theory.cpp](2102_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 116 KB | 11304072 |
| [2102_number_theory.go](2102_number_theory.go) | Go 1.14 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.046 s | 1120 KB | 11294722 |
| [2102_number_theory.java](2102_number_theory.java) | Java 1.8 | number_theory | O(min(sqrt n, B)) | AC | 0.125 s | 1592 KB | 11304073 |
| [2102_number_theory.py](2102_number_theory.py) | Python 3.12 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.453 s | 388 KB | 11304074 |
| [2102_number_theory.rs](2102_number_theory.rs) | Rust 1.75 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 232 KB | 11294726 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2102_number_theory_optimized.java](2102_number_theory_optimized.java) | Java 1.8 | number_theory | Pruned trial division; O(1) storage | AC | 0.109 s | 468 KB | 11327435 |
| [2102_number_theory_optimized.py](2102_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | Pruned trial division; O(1) bounded storage | AC | 0.125 s | 928 KB | 11327440 |
| [2102_number_theory_optimized.cpp](2102_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.015 s | 108 KB | 11326999 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
