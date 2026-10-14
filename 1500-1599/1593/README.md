# 1593. Square Country. Version 2

[Timus 1593](https://acm.timus.ru/problem.aspx?space=1&num=1593) · difficulty 729 · math

Original problem prepared by Fedor Menshikov, with special thanks to Svyatoslav Demidov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Land is sold in square plots with whole sides, a plot of side a costing
a². Spend exactly N ≤ 10¹⁵ on as few plots as possible and print how
many plots that takes. This is
[problem 1073](../../1000-1099/1073/README.md) with a much larger N.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1593_math.cpp](1593_math.cpp) | G++ 13.2 x64 | math | O(√N) | AC | 0.171 s | 132 KB |
| [1593_math.go](1593_math.go) | Go 1.14 x64 | math | O(√N) | AC | 0.203 s | 1080 KB |
| [1593_math.java](1593_math.java) | Java 1.8 | math | O(√N) | AC | 0.546 s | 1632 KB |
| [1593_math.py](1593_math.py) | Python 3.12 x64 | math | O(√N) | AC | 0.109 s | 928 KB |
| [1593_math.rs](1593_math.rs) | Rust 1.75 x64 | math | O(√N) | AC | 0.171 s | 224 KB |
