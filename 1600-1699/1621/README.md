# 1621. Definite Integral

[Timus 1621](https://acm.timus.ru/problem.aspx?space=1&num=1621) · difficulty 4445 · math

Original problem from the SPbSU ITMO Contest at the Petrozavodsk Training Camp, Winter 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

P(x) = a4·x⁴ + a3·x³ + a2·x² + a1·x + a0 has integer coefficients of
absolute value at most 10⁶, a4 ≠ 0, no real roots and no repeated roots.
Compute the integral of 1 / P(x) over the whole real line, with an
absolute or relative error of at most 10⁻⁹.

Time limit: 1 second. Memory limit: 64 MB.

## Input

a0, a1, a2, a3 and a4.

## Output

The value of the integral.

## Examples

### Example 1

Input:

```
16 0 0 0 1
```

Output:

```
0.2776801836
```

## Solution

The substitution x = sinh t, dx = cosh t dt turns the infinite line into
t ∈ (−∞, ∞) with an integrand that falls off like e⁻³ᵗ; cutting at
|t| = 20 (x ≈ 2.4·10⁸) loses less than 10⁻²⁰. The rest is adaptive
three-point Gauss–Legendre quadrature: an interval is split in two
while the two halves together differ from the whole by more than
10⁻¹³ · (1 + |value|), up to 50 levels deep, so sharp peaks from roots
near the real axis get fine intervals and flat stretches stay coarse.
`O(S)` for S intervals.

A cross-check comes from complex analysis: the integral equals 2πi times
the sum of 1 / P′(z) over the roots z in the upper half-plane. Roots
found numerically give the same values on every test here.

Pitfalls:

- a negative leading coefficient makes P negative everywhere and the
  integral negative (test 03);
- roots like 999 ± i give a narrow peak far from the origin (test 04);
- 10⁶ x⁴ + 1 and x⁴ + 10⁶ put the mass at very different scales
  (tests 05, 06).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1621_math.cpp](1621_math.cpp) | G++ 13.2 x64 | math | O(S) | AC | 0.031 s | 464 KB |
| [1621_math.go](1621_math.go) | Go 1.14 x64 | math | O(S) | AC | 0.046 s | 1088 KB |
| [1621_math.java](1621_math.java) | Java 1.8 | math | O(S) | AC | 0.234 s | 1960 KB |
| [1621_math.py](1621_math.py) | Python 3.12 x64 | math | O(S) | AC | 0.265 s | 552 KB |
| [1621_math.rs](1621_math.rs) | Rust 1.75 x64 | math | O(S) | AC | 0.015 s | 280 KB |
