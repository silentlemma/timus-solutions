# 1854. Negotiations with Parthians

[Timus 1854](https://acm.timus.ru/problem.aspx?space=1&num=1854) · difficulty 424 · number_theory

Original problem by Grigoriy Nazarov, from the Ural SU Team.GOV Contest at the Petrozavodsk summer session, August 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Emperor Hadrian sacrifices a flock of n rams, n odd, sharing it equally
among some number of gods. Theon of Smyrna wants that number to be odd
and to have an odd number of positive divisors. Find the largest such
number of gods.

## Input

An odd integer n (1 ≤ n ≤ 10¹⁸ − 1).

## Output

The largest suitable number of gods.

## Examples

### Example 1

Input:

```
45
```

Output:

```
9
```

## Solution

A number has an odd count of divisors exactly when it is a perfect
square: divisors pair up as k and m/k, and only a square has a divisor
paired with itself. Every divisor of an odd n is odd, so the answer is
the largest square dividing n, the product of p^(2⌊e/2⌋) over the prime
powers p^e of n.

Divide out the odd primes p while p³ ≤ n, n shrinking as it goes. What
remains has no prime factor up to its cube root, so it is 1, a prime,
a product of two primes or the square of a prime, and only the last
adds a square: check with an exact integer square root. The trial
division takes at most 10⁶ steps, and the Python solution only tries
the primes, from a sieve. `O(n^(1/3))`.

In the example 45 = 3²·5, so the answer is 9.

Pitfalls:

- a large prime factor squared, such as (10⁹ − 63)², is left after the
  trial division and must still be recognised;
- a floating-point square root of a number near 10¹⁸ can be off by one;
  correct it with integer checks.

The answers agree with a direct search on a hundred small numbers and
with an independent accepted implementation on large primes, products
of two large primes, squares of large primes and products of many small
primes.

## Optimized solutions

`1854_number_theory_optimized.py`. Keep the exact largest-square-divisor factorization for the promised odd input. Remove all factors of three first, then test only 6k-1 and 6k+1 divisors. After removing each prime power, an exact isqrt test can return a square residual immediately; after the shrinking cube-root loop only a square residual contributes. There is no sieve or stored answer table. O(n^(1/3)) trial divisions and constant arithmetic state under n<10^18; the readable sieve-based Python source remains.

Exact-source PyPy 3.10 x64 Accepted #11327061: 0.125 s / 1068 KB. Saved 2026-11-20 comparison of current Python-family compilers: time 2/23, memory 7/23; both strict top-ten criteria pass. Memory is at least 1024 KB, so time and memory are both required. The separate first-place-in-both language target is not met: keep the asterisk. Previously documented optimized CPython 3.12 run #11314964: 0.203 s / 392 KB. The selected PyPy run has lower recorded time but higher memory; these are independent paired runs on different interpreters, not an algorithm-only speed claim or mixed minima. Current retained simple CPython Accepted #11327562: 0.171 s / 1928 KB. No extra source copy or repeat submission is needed.

Own Accepted after formatting only: `1854_number_theory.java` #11327560, `1854_number_theory.cpp` #11327561, `1854_number_theory.py` #11327562. The basic algorithms and all other source files remain.

The new Go, Python and Rust implementations keep the shrinking cube-root trial division and remove square powers as before. A square input, or a square residual after removing a factor, can be returned immediately: the whole residual is its own largest square divisor. Python drops the million-entry sieve, removes factor three separately and tries only 6k±1 divisors, with constant arithmetic state. This retains O(n^(1/3)) trial divisions; composite trial divisors cannot divide the residual after all their smaller prime factors have been removed. Python uses exact isqrt; Go and Rust use integer binary square roots bounded by 10⁹. Even the next cube-root test at 1000001 fits signed 64-bit arithmetic, and every accumulated square factor divides the original n. Go uses standard handles and Rust a C entry point with bounded character I/O. All original sources, including the sieve-based Python base, remain; C++ and Java reuse their admitted bases in the fast set.

Retained accepted bases [1854_number_theory.cpp](1854_number_theory.cpp), [1854_number_theory.java](1854_number_theory.java) also meet strict top-ten or top-15% admission for the required metrics in the saved comparison. They are reused without identical optimized copies. Their current exact paired measurements are in the table; an asterisk denotes the separate language target. Formatting changes no algorithm and is not credited with speed improvements.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1854_number_theory.cpp](1854_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n^(1/3)) | AC | 0.015 s | 112 KB | 11327561 |
| [1854_number_theory.go](1854_number_theory.go) | Go 1.14 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 1160 KB | 11290776 |
| [1854_number_theory.java](1854_number_theory.java) \* | Java 1.8 | number_theory | O(n^(1/3)) | AC | 0.125 s | 488 KB | 11327560 |
| [1854_number_theory.py](1854_number_theory.py) | Python 3.12 x64 | number_theory | O(n^(1/3)) | AC | 0.171 s | 1928 KB | 11327562 |
| [1854_number_theory.rs](1854_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n^(1/3)) | AC | 0.062 s | 224 KB | 11290781 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1854_number_theory_optimized.go](1854_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 280 KB | 11314959 |
| [1854_number_theory_optimized.py](1854_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(n^(1/3)) trial divisions; O(1) arithmetic state | AC | 0.125 s | 1068 KB | 11327061 |
| [1854_number_theory_optimized.rs](1854_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 48 KB | 11314970 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
