# 1665. Dean's Financial Pyramid

[Timus 1665](https://acm.timus.ru/problem.aspx?space=1&num=1665) · difficulty 440 · number_theory

Original problem by Alex Samsonov, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, January 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

By the evening of day 1 there is one application on the table. Every
next day the number of applications is multiplied by a whole factor
that is either 2 or an odd number above 1, possibly different each day.
Money is paid only on an even day, and only if exactly N applications
lie on the table that evening. For each N, decide whether this can
happen.

## Input

T (1 ≤ T ≤ 100), then T numbers N (1 ≤ N ≤ 2²⁵ − 1).

## Output

`YES` or `NO` for each N.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
4
4
7
6
30
```

Output:

```
NO
YES
NO
YES
```

## Solution

On day d the count is a product of d − 1 factors, and d must be even, so
the question is whether N is a product of an odd number of factors, each
2 or an odd number above 1. Write N = 2ᵃ · r with r odd. A factor 2 is
the only source of twos, so exactly a factors are 2, and the odd factors
multiply to r.

- If r = 1, there are exactly a factors: `YES` when a is odd (N = 1 is
  day 1 and never paid).
- If a is even and r > 1, the a twos and r itself make a + 1 factors,
  an odd count: `YES`.
- If a is odd, r must split into an even number of odd factors above 1,
  which is possible exactly when r is not a prime (take two factors, or
  more if needed): `YES` for composite r, `NO` for prime r.

Primality is tested by trial division up to √r, at most about 2900 odd
divisors. `O(T · √N)`.

Pitfalls:

- N = 1 and N = 2ᵃ with even a are `NO`; 2ᵃ with odd a is `YES` (test 02);
- a power of two with odd exponent times a prime is `NO` (6 in the
  example, 2²³ · 3 in test 03).

The answers match an exhaustive search over all factor sequences for
every N up to 3000, and an independent accepted implementation.

## Optimized solutions

`1665_number_theory_optimized.java`. Keep the parity-of-factor-count classification. Count powers of two with numberOfTrailingZeros and obtain the odd part by shifting. Handle pure powers of two, an even power-of-two exponent and divisibility by 3 explicitly; only the remaining odd primality case needs trial division. Test the 6k-1/6k+1 wheel via alternating steps 2,4, with divisor<=odd/divisor instead of squaring the divisor. This preserves the decision, not a probabilistic prime test. For positive N<=2^25-1, time O(T sqrt N) worst case and O(1) state plus byte buffers. Emit each answer directly instead of building one output StringBuilder.

Compared with `1665_number_theory.java`: time 0.14 s → 0.093 s; memory 420 KB → 508 KB.

The new Go source keeps the factor-count parity classification but sieves odd trial primes once for the whole batch. Primality is needed only when the exponent of two is odd, hence at least one factor two was removed: the remaining odd value is below 2²⁴ and its square root below R=4096. Every composite residual therefore has a prime divisor in the prepared list. Compare p²≤residual so prime squares are classified correctly. A pure power of two is handled before this test; one application on day one still gives NO. The sieve and 16-bit prime list use O(R) storage, with O(R log log R+T·π(R)) work. Standard-handle I/O replaces fmt. All ordinary sources remain; the other four admitted bases also cover the fast set.

The accepted base implementations [1665_number_theory.cpp](1665_number_theory.cpp), [1665_number_theory.java](1665_number_theory.java), [1665_number_theory.py](1665_number_theory.py), [1665_number_theory.rs](1665_number_theory.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1665_number_theory_optimized.rs`. Retain the archived algorithm and its integer types. Convert decimal integer tokens directly instead of calling the general string parser; negative values are accumulated with their sign so the minimum signed value remains representable. Existing input storage and algorithmic bounds are unchanged.

Accepted #11328584 (Rust 1.75 x64): **0.015 s / 216 KB**. Archived comparison: `1665_number_theory.rs` (Rust 1.75 x64) — 0.046 s / 192 KB (#11325612).

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`1665_number_theory_optimized.java`: time place 3/13, memory place 2/13 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1665_number_theory.cpp](1665_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T sqrt N) | AC | 0.015 s | 112 KB | 11325587 |
| [1665_number_theory.go](1665_number_theory.go) | Go 1.14 x64 | number_theory | O(T sqrt N) | AC | 0.015 s | 1084 KB | 11288647 |
| [1665_number_theory.java](1665_number_theory.java) | Java 1.8 | number_theory | O(T sqrt N) | AC | 0.14 s | 420 KB | 11325559 |
| [1665_number_theory.py](1665_number_theory.py) | Python 3.12 x64 | number_theory | O(T sqrt N) | AC | 0.078 s | 452 KB | 11325597 |
| [1665_number_theory.rs](1665_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T sqrt N) | AC | 0.046 s | 192 KB | 11325612 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1665_number_theory_optimized.go](1665_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(R log log R + T·π(R)) | AC | 0.015 s | 288 KB | 11315121 |
| [1665_number_theory_optimized.java](1665_number_theory_optimized.java) | Java 1.8 | number_theory | O(T·sqrt N) | AC | 0.093 s | 508 KB | 11325020 |
| [1665_number_theory_optimized.rs](1665_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(T sqrt N) | AC | 0.015 s | 216 KB | 11328584 |
