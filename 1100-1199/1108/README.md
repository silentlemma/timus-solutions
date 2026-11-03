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

Keep all five readable Sylvester-recurrence sources. Fast variants compute the same a[1]=2,a[k+1]=a[k]^2-a[k]+1 and avoid forming an unused term after the final output. Java uses base-10000 integer digits, symmetric schoolbook squaring into long accumulators, then subtracts the old value and adds one with exact carries. For N <= 18, a[18]<2^131072<10^40960, so 11000 chunks suffice; even the largest convolution coefficient fits long. Stream four-digit chunks instead of constructing a large decimal string. Python retains native big-integer arithmetic but recursively splits decimal output into at most 1000-digit conversions, below the normal conversion cap. A rational upper bound on log10(2), followed by an exact power-of-ten comparison, gives the output width without converting the full value. Each decimal is emitted exactly once. Conservative arithmetic/output bounds are O(D²) time and O(D) working digits. All 18 prefixes were independently verified. Python's one-tick time difference is not the admission basis; its own memory reduction exceeds 30%.

- `1108_math_optimized.java`: 0.125 s / 516 KB; base `1108_math.java`: 0.187 s / 6508 KB; relative change: time -33.2%, memory -92.1%.
- `1108_math_optimized.py`: 0.015 s / 788 KB; base `1108_math.py`: 0.031 s / 1144 KB; relative change: time -51.6%, memory -31.1%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1108_math.cpp`; covering source `1108_math.cpp`; time/memory places 1/4, other-author entries 23/23.

- Go: preferred teaching base `1108_math.go`; covering source `1108_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1108_math.java`; covering source `1108_math_optimized.java`; time/memory places 2/1, other-author entries 13/13.

- Python/PyPy: preferred teaching base `1108_math.py`; covering source `1108_math_optimized.py`; time/memory places 1/3, other-author entries 21/21.

- Rust: preferred teaching base `1108_math.rs`; covering source `1108_math.rs`; time/memory places 1/1, other-author entries 0/0.

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
| [1108_math_optimized.java](1108_math_optimized.java) \* | Java 1.8 | math | O(D²) arithmetic/output bound; O(D) working digits | AC | 0.125 s | 516 KB | 11309742 |
| [1108_math_optimized.py](1108_math_optimized.py) \* | Python 3.12 x64 | math | O(D²) arithmetic/output bound; O(D) working digits | AC | 0.015 s | 788 KB | 11309753 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
