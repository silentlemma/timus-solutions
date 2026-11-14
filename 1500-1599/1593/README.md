# 1593. Square Country. Version 2

[Timus 1593](https://acm.timus.ru/problem.aspx?space=1&num=1593) · difficulty 725 · math

Original problem prepared by Fedor Menshikov, with special thanks to Svyatoslav Demidov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Land is sold in square plots with positive integer sides, a plot of side a costing
a². Spend exactly N ≤ 10¹⁵ on as few plots as possible and print how
many plots that takes. This is
[problem 1073](../../1000-1099/1073/README.md) with a much larger N.

Time limit: 1 second. Memory limit: 64 MB.

## Input

A positive integer N, 1 ≤ N ≤ 10¹⁵.

## Output

The least number of squares that add up to N.

## Examples

### Example 1

Input:

```
344
```

Output:

```
3
```

## Solution

By Lagrange's theorem every N is a sum of four squares, so the answer is
1 to 4, and classical theorems tell which:

- 1 when N is a perfect square;
- 2 when every prime of the form 4k + 3 divides N an even number of
  times (Fermat's theorem on sums of two squares);
- 4 when N = 4ᵃ(8b + 7), after removing every factor 4 (Legendre's
  three-square theorem);
- 3 otherwise.

Only the two-square test needs the factorization of N. In C++, Go, Java
and Rust trial division by odd numbers up to √N, at most about 1.6·10⁷
of them, is fast enough; whatever is left at the end is 1 or a prime. In
Python that loop is too slow, so small divisors up to 1000 are removed
by trial division and the rest is split by Pollard's rho, with a
Miller–Rabin test using the first twelve primes as bases, which is exact
far beyond 10¹⁵.

Python's complexity is an expected estimate for randomized rho; its
retries give no deterministic worst-case time bound.

The answers were checked against a dynamic programming over all N up to
20000.

Pitfalls:

- the square root needs care: a floating-point root of a number near
  10¹⁵ can be off by one, so it is corrected with integer steps;
- the product of two primes near √N, both 4k + 3, has no small factor
  and leaves remainder 1 modulo 4, so stopping trial division at the
  cube root and guessing about the rest gives a wrong answer (test 06);
- the factor left after trial division must be checked too: when N is a
  prime 4k + 3 itself, nothing divides it below √N (test 08); the prime
  2 never matters, since 2 = 1 + 1.
- generated inputs must also respect N ≤ 10¹⁵: bound the prime search
  in generator mode 2, and reserve the +7 before multiplying by 4ᵃ in
  mode 4. Neither boundary issue affects a stored numbered test.

## Optimized solutions

The optimized versions check for a square and apply Legendre's test before factoring. Miller–Rabin identifies prime factors, and Pollard's rho splits remaining composite factors. Square factors can be dropped because they contribute even exponents.

G++ 13.2 x64, submission 11322019. Time 0.171 → 0.031 s, memory 116 → 172 KB.

Go 1.14 x64, submission 11322020. Time 0.203 → 0.031 s, memory 1072 → 1104 KB.

Java 1.8, submission 11322021. Time 0.578 → 0.109 s, memory 1624 → 524 KB.

Python 3.12 x64, submission 11322023. Time 0.109 → 0.093 s, memory 944 → 780 KB.

Rust 1.75 x64, submission 11322024. Time 0.156 → 0.046 s, memory 220 → 216 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322314 · Go 1.14 x64 №11322315 · Java 1.8 №11322316 · Python 3.12 x64 №11322319 · Rust 1.75 x64 №11322320.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1593_math.cpp](1593_math.cpp) | G++ 13.2 x64 | math | O(√N) | AC | 0.171 s | 116 KB | 11322314 |
| [1593_math.go](1593_math.go) | Go 1.14 x64 | math | O(√N) | AC | 0.203 s | 1072 KB | 11322315 |
| [1593_math.java](1593_math.java) | Java 1.8 | math | O(√N) | AC | 0.578 s | 1624 KB | 11322316 |
| [1593_math.py](1593_math.py) | Python 3.12 x64 | math | O(√N) expected | AC | 0.109 s | 944 KB | 11322319 |
| [1593_math.rs](1593_math.rs) | Rust 1.75 x64 | math | O(√N) | AC | 0.156 s | 220 KB | 11322320 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1593_math_optimized.cpp](1593_math_optimized.cpp) | G++ 13.2 x64 | math | O(n^1/4 log n) expected | AC | 0.031 s | 172 KB | 11322019 |
| [1593_math_optimized.go](1593_math_optimized.go) \* | Go 1.14 x64 | math | O(n^1/4 log n) expected | AC | 0.031 s | 1104 KB | 11322020 |
| [1593_math_optimized.java](1593_math_optimized.java) | Java 1.8 | math | O(n^1/4 log n) expected | AC | 0.109 s | 524 KB | 11322021 |
| [1593_math_optimized.py](1593_math_optimized.py) | Python 3.12 x64 | math | O(n^1/4 log n) expected | AC | 0.093 s | 780 KB | 11322023 |
| [1593_math_optimized.rs](1593_math_optimized.rs) \* | Rust 1.75 x64 | math | O(n^1/4 log n) expected | AC | 0.046 s | 216 KB | 11322024 |

\* The marked versions have room to improve in the ratings.
