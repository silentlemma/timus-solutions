# 1091. Counting sets of numbers with a common divisor

[Timus 1091](https://acm.timus.ru/problem.aspx?space=1&num=1091) · difficulty 529 · number_theory

Original problem by Stanislav Vasiliev, from the USU Open Collegiate Programming Contest, March 2001, Senior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the sets of `K` different positive integers, none larger than `S`
(`2 ≤ K ≤ S ≤ 50`), whose greatest common divisor is larger than 1. Print
the count, or 10000 if it is larger than that.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`K` and `S`.

## Output

The number of sets, at most 10000.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3 10
```

Output:

```
11
```

## Solution

The preferred teaching Go version counts sets by their exact gcd, without a Möbius function. If K>floor(S/2), no divisor≥2 has enough multiples. Otherwise compute just C(m,K) for K≤m≤floor(S/2), starting at1 and using C(m,K)=C(m−1,K)·m/(m−K). For d from D=floor(S/K) down to2, start with C(floor(S/d),K) sets of multiples of d and subtract the previously computed exact-gcd counts for 2d,3d,… . Every set has one gcd, so these subtracted classes are disjoint and the sum for d≥2 is the answer. For K=3 and S=10, exact gcd 3 contributes C(3,3)=1 set and exact gcd 2 contributes C(5,3)=10 sets, giving 11. If C(m,K) reaches 10,000, choosing K of the first m even numbers already gives enough valid sets to return 10,000. Until that point, the binomial recurrence multiplies a value below 10,000 by m ≤ 25. Each exact count is bounded by its binomial, so adding it to a running total below 10,000 gives a value below 20,000. The final answer is capped at 10,000. Time is O(S + D log D), space O(S). The original Möbius versions compute the signed sum Σ−μ(d)C(floor(S/d),K) using a full Pascal table and cap the final result.

## Optimized solutions

The optimized Go version keeps the exact-gcd recurrence and uses direct standard handles and a six-byte answer buffer. Rust uses the same exact-gcd algorithm in a separate optimized port with fixed32-bit arrays, bounded C-runtime character I/O and a C entry point. C++/Java/Python reuse their admitted original implementations. D=floor(S/K)≤25; no table of precomputed answers is stored. Original Go is retained under Other Accepted approaches; original Rust stays available as a simple standard-library implementation. Stars concern language rating targets.

The accepted base implementations [1091_number_theory.cpp](1091_number_theory.cpp), [1091_number_theory.java](1091_number_theory.java), [1091_number_theory.py](1091_number_theory.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The Go teaching port uses ordinary buffered input and two26-entry integer arrays. Rust uses two26-entry u32 arrays and C-runtime I/O; getchar/putchar receive no pointers. Capacity10000 needs at most five output digits. The original five programs keep their exact source-bound Accepted and metrics. Python retains the actual accepted interpreter.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1091_number_theory.cpp](1091_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(S^2) | AC | 0.015 s | 232 KB | 11279091 |
| [1091_dp.go](1091_dp.go) | Go 1.14 x64 | dp | O(S + D log D) | AC | 0.015 s | 912 KB | 11315680 |
| [1091_number_theory.java](1091_number_theory.java) | Java 1.8 | number_theory | O(S^2) | AC | 0.109 s | 1640 KB | 11279094 |
| [1091_number_theory.py](1091_number_theory.py) \* | Python 3.12 x64 | number_theory | O(S^2) | AC | 0.078 s | 424 KB | 11279093 |
| [1091_number_theory.rs](1091_number_theory.rs) | Rust 1.75 x64 | number_theory | O(S^2) | AC | 0.046 s | 228 KB | 11279095 |

### Other Accepted approaches

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1091_number_theory.go](1091_number_theory.go) | Go 1.14 x64 | number_theory | O(S^2) | AC | 0.015 s | 1088 KB | 11279092 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1091_dp_optimized.go](1091_dp_optimized.go) \* | Go 1.14 x64 | dp | O(S + D log D) | AC | 0.015 s | 264 KB | 11315895 |
| [1091_dp.rs](1091_dp.rs) \* | Rust 1.75 x64 | dp | O(S + D log D) | AC | 0.015 s | 60 KB | 11315681 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
