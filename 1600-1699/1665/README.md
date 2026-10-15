# 1665. Dean's Financial Pyramid

[Timus 1665](https://acm.timus.ru/problem.aspx?space=1&num=1665) · difficulty 438 · number_theory

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1665_number_theory.cpp](1665_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T sqrt N) | AC | 0.015 s | 128 KB |
| [1665_number_theory.go](1665_number_theory.go) | Go 1.14 x64 | number_theory | O(T sqrt N) | AC | 0.015 s | 1084 KB |
| [1665_number_theory.java](1665_number_theory.java) | Java 1.8 | number_theory | O(T sqrt N) | AC | 0.125 s | 448 KB |
| [1665_number_theory.py](1665_number_theory.py) | Python 3.12 x64 | number_theory | O(T sqrt N) | AC | 0.093 s | 412 KB |
| [1665_number_theory.rs](1665_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T sqrt N) | AC | 0.031 s | 208 KB |
