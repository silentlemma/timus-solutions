# 1108. Unit fractions that leave the smallest positive remainder

[Timus 1108](https://acm.timus.ru/problem.aspx?space=1&num=1108) · difficulty 252 · math

Original problem by Pavlin Peev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose positive integers `a_1 ≤ a_2 ≤ … ≤ a_N` (`1 ≤ N ≤ 18`) so that
`1 − (1/a_1 + … + 1/a_N)` is positive and as small as possible. Print
them in that order, one per line.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`.

## Output

`a_1`, …, `a_N`, each on its own line.

## Checking

Compare the exact answer tokens; whitespace formatting is immaterial.

- `1108_math_optimized.java` (Java 1.8): 11 repository cases; 18 additional source-bound comparisons.

- `1108_math_optimized.py` (Python 3.12 x64): 11 repository cases; 18 additional source-bound comparisons.

## Examples

### Example 1

Input:

```
2
```

Output:

```
2
3
```

## Solution

Take every fraction greedily: the largest unit fraction that still leaves
something. This gives Sylvester's sequence `a_1 = 2`,
`a_{k+1} = a_k (a_k − 1) + 1`, and by induction the remainder after `k`
terms is exactly `1 / (a_{k+1} − 1)`, so the next largest admissible
fraction is `1/a_{k+1}`. That the greedy choice is also the best one for
every `N` is a classical result on Egyptian fractions (Curtiss, 1922).

The terms square at every step: `a_18` has about 26 700 digits and the
whole output about 53 000 characters, so big integers are needed. One
multiplication per term, `O(D²)` with the schoolbook method for `D`
digits, is fast enough.

Pitfalls:

- 64-bit integers overflow already at `a_8`;
- Python refuses by default to convert integers longer than 4300 digits
  to text, which `a_16` already exceeds;
- the denominators must be printed in full, without scientific notation
  or rounding.

The answers were checked against a search over all non-decreasing
denominators with exact fractions for `N ≤ 4`, and for every `N` by
verifying with exact fractions that the remainder is `1 / (a_1 ⋯ a_N)`,
the value the greedy argument gives.

## Optimized solutions

`1108_math_optimized.rs`. Keep Sylvester’s recurrence a_next=a²-a+1, using base-10^4 u32 limbs. Squaring computes diagonal products once and doubles only off-diagonal products; normalize a reusable u64 scratch array, subtract a, then add one. Reuse the next/scratch vectors and stream padded four-digit limbs. Most importantly, do not compute the unused next term after the last printed term; the basic source did. With D limbs in the largest required term, total schoolbook limb work is O(D²) and storage O(D), including scratch. N<=18 keeps convolution coefficients within u64. Preserve the basic base-10^9 implementation.

Compared with `1108_math.rs`: time 0.015 s → 0.015 s; memory 356 KB → 188 KB.

Keep all five readable Sylvester-recurrence sources. Fast variants compute the same a[1]=2,a[k+1]=a[k]^2-a[k]+1 and avoid forming an unused term after the final output. Java uses base-10000 integer digits, symmetric schoolbook squaring into long accumulators, then subtracts the old value and adds one with exact carries. For N <= 18, a[18]<2^131072<10^40960, so 11000 chunks suffice; even the largest convolution coefficient fits long. Stream four-digit chunks instead of constructing a large decimal string. Python retains native big-integer arithmetic but recursively splits decimal output into at most 1000-digit conversions, below the normal conversion cap. A rational upper bound on log10(2), followed by an exact power-of-ten comparison, gives the output width without converting the full value. Each decimal is emitted exactly once. Conservative arithmetic/output bounds are O(D²) time and O(D) working digits. All 18 prefixes were independently verified. Python's one-tick time difference is not the admission basis; its own memory reduction exceeds 30%.

- `1108_math_optimized.java`: 0.125 s / 516 KB; base `1108_math.java`: 0.187 s / 6508 KB; relative change: time -33.2%, memory -92.1%.
- `1108_math_optimized.py`: 0.015 s / 788 KB; base `1108_math.py`: 0.031 s / 1144 KB; relative change: time -51.6%, memory -31.1%.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1108_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1108_math.cpp](1108_math.cpp) | G++ 13.2 x64 | math | O(D²) per term | AC | 0.015 s | 232 KB | 11279192 |
| [1108_math.go](1108_math.go) | Go 1.14 x64 | math | O(D²) per term | AC | 0.015 s | 1920 KB | 11279193 |
| [1108_math.java](1108_math.java) | Java 1.8 | math | O(D²) per term | AC | 0.187 s | 6508 KB | 11279195 |
| [1108_math.py](1108_math.py) | Python 3.12 x64 | math | O(D²) per term | AC | 0.031 s | 1144 KB | 11279194 |
| [1108_math.rs](1108_math.rs) | Rust 1.75 x64 | math | O(D²) per term | AC | 0.015 s | 356 KB | 11279196 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1108_math_optimized.java](1108_math_optimized.java) | Java 1.8 | math | O(D²) arithmetic/output bound; O(D) working digits | AC | 0.125 s | 516 KB | 11309742 |
| [1108_math_optimized.py](1108_math_optimized.py) | Python 3.12 x64 | math | O(D²) arithmetic/output bound; O(D) working digits | AC | 0.015 s | 788 KB | 11309753 |
| [1108_math_optimized.rs](1108_math_optimized.rs) | Rust 1.75 x64 | math | O(D²) limb work; O(D) space | AC | 0.015 s | 188 KB | 11325539 |
