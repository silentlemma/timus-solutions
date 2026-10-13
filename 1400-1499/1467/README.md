# 1467. Sum of Degrees

[Timus 1467](https://acm.timus.ru/problem.aspx?space=1&num=1467) · difficulty 1215 · math

Original problem by Alexander Ipatov, from the Ural State University Contest at the Petrozavodsk Winter Training Camp, January 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For every k the sum 1^k + 2^k + ... + N^k is a polynomial P(N) of
degree k + 1 with rational coefficients; for example
1 + ... + N = N(N + 1)/2. Given 0 ≤ k ≤ 30, print its k + 2
coefficients from the highest power down, as reduced fractions "a/b" or
"-a/b" with b ≥ 1, zero written as "0/1".

Time limit: 1 second. Memory limit: 64 MB.

## Input

k.

## Output

The coefficients of P, separated by single spaces.

## Examples

### Example 1

Input:

```
1
```

Output:

```
1/2 1/2 0/1
```

## Solution

This is Faulhaber's formula. With the Bernoulli numbers in the
convention B₁ = +1/2,
P(N) = 1/(k + 1) · Σ C(k + 1, j) · B_j · N^(k + 1 − j) over j = 0..k,
so the coefficient of N^(k + 1 − j) is C(k + 1, j) B_j / (k + 1), and
the free term is 0. The Bernoulli numbers follow from the identity
Σ C(m + 1, j) B_j = m + 1 over j = 0..m, which in this convention gives
B_m from the earlier ones: B_m = (m + 1 − Σ_{j < m} C(m + 1, j) B_j) / (m + 1).

All arithmetic is exact. The reduced coefficients stay small, but the
sums along the way do not fit in 32 bits for k near 30: Python uses
Fraction, Go big.Rat, Java BigInteger, and C++ and Rust 128-bit
integers, reducing every fraction by the greatest common divisor.
`O(k²)` fraction operations; Go takes `O(k³)` arithmetic operations
because it recomputes binomial coefficients.

Pitfalls:

- the coefficients of N^(k − 2), N^(k − 4), ... are zero for k ≥ 3 and
  must still be printed as 0/1 (tests 04, 10);
- B₁ must be +1/2 for sums that run up to N (with −1/2 they would run
  up to N − 1);
- intermediate products overflow 32 bits for k near 30 (tests 09,
  10).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1467_math.cpp](1467_math.cpp) | G++ 13.2 x64 | math | O(k^2) | AC | 0.015 s | 232 KB |
| [1467_math.go](1467_math.go) | Go 1.14 x64 | math | O(k^3) | AC | 0.031 s | 1628 KB |
| [1467_math.java](1467_math.java) | Java 1.8 | math | O(k^2) | AC | 0.125 s | 2292 KB |
| [1467_math.py](1467_math.py) | Python 3.12 x64 | math | O(k^2) | AC | 0.078 s | 868 KB |
| [1467_math.rs](1467_math.rs) | Rust 1.75 x64 | math | O(k^2) | AC | 0.031 s | 280 KB |
