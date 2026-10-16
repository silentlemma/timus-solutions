# 1814. Continued Fraction

[Timus 1814](https://acm.timus.ru/problem.aspx?space=1&num=1814) · difficulty 2928 · math

Original problem from the Tavrida NU Akai Contest, Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Write √x as an infinite continued fraction [a₀; a₁, a₂, …] and print
its convergent of order k, [a₀; a₁, …, aₖ], as an irreducible fraction
with the numerator and denominator taken modulo 10⁹ + 7.

## Input

x and k (2 ≤ x ≤ 10⁶, 0 ≤ k ≤ 10⁹); x is not a perfect square.

## Output

The convergent as p/q, both modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
2 3
```

Output:

```
17/12
```

## Solution

The partial quotients of √x are periodic after a₀. The usual recurrence
m ← d·a − m, d ← (x − m²)/d, a ← ⌊(a₀ + m)/d⌋ produces them, and the
period ends at the first term equal to 2a₀. For x ≤ 10⁶ it is at most
a few thousand terms long. Convergents grow by matrix products: the
matrix [[pₖ, pₖ₋₁], [qₖ, qₖ₋₁]] equals
M(a₀)·M(a₁)·…·M(aₖ) with M(a) = [[a, 1], [1, 0]]. So multiply M(a₀),
then the product of one whole period raised to the power ⌊k/L⌋ by
repeated squaring, then the first k mod L terms of the period, all
modulo 10⁹ + 7. The first column is (p, q). Convergents are always in
lowest terms, since pₖqₖ₋₁ − pₖ₋₁qₖ = ±1, so no reduction is needed
before taking the remainders. `O(L + log k)`.

In the example √2 = [1; 2, 2, 2, …], and the convergents are 1, 3/2,
7/5 and 17/12.

Pitfalls:

- the fraction must be irreducible before the remainders are taken,
  which convergents already are;
- the order k counts from 0, so order 0 is a₀/1;
- d never becomes 0 for a non-square x, but a square would break the
  period recurrence.

The answers agree with an independent accepted implementation on 300
random cases and with exact fractions for the first twenty convergents
of eight square roots.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1814_math.cpp](1814_math.cpp) | G++ 13.2 x64 | math | O(L + log k) | AC | 0.015 s | 216 KB |
| [1814_math.go](1814_math.go) | Go 1.14 x64 | math | O(L + log k) | AC | 0.015 s | 1168 KB |
| [1814_math.java](1814_math.java) | Java 1.8 | math | O(L + log k) | AC | 0.125 s | 1984 KB |
| [1814_math.py](1814_math.py) | Python 3.12 x64 | math | O(L + log k) | AC | 0.078 s | 596 KB |
| [1814_math.rs](1814_math.rs) | Rust 1.75 x64 | math | O(L + log k) | AC | 0.015 s | 248 KB |
