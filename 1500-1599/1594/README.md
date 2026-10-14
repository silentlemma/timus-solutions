# 1594. Aztec Treasure

[Timus 1594](https://acm.timus.ru/problem.aspx?space=1&num=1594) · difficulty 4014 · math

Original problem by Igor Chevdar, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, February 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the ways to tile an l × w rectangle (1 ≤ l, w ≤ 100) with 1 × 2
dominoes, modulo 10⁹ + 7.

Time limit: 1 second. Memory limit: 64 MB.

## Input

l and w.

## Output

The number of tilings modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
3 4
```

Output:

```
11
```

## Solution

A profile over a side of 100 cells has 2¹⁰⁰ states, so the usual dynamic
programming is out. Kasteleyn's formula counts the tilings of an m × n
board exactly:

T = ∏ ∏ (4cos²(jπ/(m + 1)) + 4cos²(kπ/(n + 1))), with j from 1 to
⌈m/2⌉ and k from 1 to ⌈n/2⌉.

Factors may lie outside the prime field, but their product is an integer.
The values 2cos(jπ/(m + 1)), j = 1..m, are the roots of
Sₘ(x) = Uₘ(x/2), the Chebyshev polynomial with S₀ = 1, S₁ = x and
Sₖ₊₁ = x·Sₖ − Sₖ₋₁, which has integer coefficients. The roots come in
pairs ±x, plus 0 when m is odd, so after an extra factor x for odd m
every power is even, and replacing x² by y gives a monic integer
polynomial Pₘ whose roots aⱼ are exactly the values 4cos²(jπ/(m + 1)) in
the product. With Q the monic polynomial whose roots are −bₖ for the
roots bₖ of Pₙ,

T = ∏ ∏ (aⱼ + bₖ) = Res(Pₘ, Q),

the resultant, which is the determinant of the Sylvester matrix of the
two polynomials. Its size is at most 50 + 50, so Gaussian elimination
modulo 10⁹ + 7 takes `O((l + w)³)`.

The results were checked against a profile dynamic programming on all
boards up to 9 × 14, and on the 8 × 8 board they give the known
12988816.

Pitfalls:

- with l·w odd the answer is 0, which the formula gives by itself: both
  polynomials have the root 0;
- Q(y) = (−1)ᵉ·Pₙ(−y), e = deg Pₙ, is monic; omitting the sign
  flips the answer only when both degrees are odd;
- the coefficients of Sₘ grow fast, so they are reduced modulo
  10⁹ + 7 at every step.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1594_math.cpp](1594_math.cpp) | G++ 13.2 x64 | math | O((l + w)³) | AC | 0.015 s | 392 KB |
| [1594_math.go](1594_math.go) | Go 1.14 x64 | math | O((l + w)³) | AC | 0.031 s | 1300 KB |
| [1594_math.java](1594_math.java) | Java 1.8 | math | O((l + w)³) | AC | 0.156 s | 1780 KB |
| [1594_math.py](1594_math.py) | Python 3.12 x64 | math | O((l + w)³) | AC | 0.125 s | 816 KB |
| [1594_math.rs](1594_math.rs) | Rust 1.75 x64 | math | O((l + w)³) | AC | 0.046 s | 320 KB |
