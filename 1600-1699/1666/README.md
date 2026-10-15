# 1666. Vasya Ferrari

[Timus 1666](https://acm.timus.ru/problem.aspx?space=1&num=1666) · difficulty 1285 · math

Original problem by Igor Chevdar, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, January 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Factor x⁴ + ax³ + bx² + cx + d into as many factors with integer
coefficients as possible. Print `Irreducible` if there is no
factorization, otherwise the factors in parentheses, without spaces,
zero terms, unit coefficients or exponents of 1 (a constant term 1 is
written).

## Input

Integers a, b, c, d of absolute value at most 20000.

## Output

The factorization or `Irreducible`.

## Examples

### Example 1

Input:

```
0 0 0 0
```

Output:

```
(x)(x)(x)(x)
```

### Example 2

Input:

```
-4 -3 24 45
```

Output:

```
(x2+3x+3)(x2-7x+15)
```

### Example 3

Input:

```
1 1 1 1
```

Output:

```
Irreducible
```

## Solution

The polynomial is monic, so by Gauss's lemma every factorization over
the integers can use monic factors, and the most factors come from
splitting it into irreducible ones.

1. Take out integer roots one by one. A root of a monic integer
   polynomial divides its constant term (a zero constant term means the
   root 0), so trying the divisors of the constant term finds one. Each
   root r splits off x − r, and synthetic division leaves the quotient.
2. If no root is left, a cubic or a quadratic remainder is irreducible.
3. A quartic without roots is either irreducible or a product of two
   quadratics (x² + px + q)(x² + rx + s). Comparing coefficients:
   qs = d, p + r = a, q + s + pr = b, ps + qr = c. For each divisor q
   of d, s = d / q; if q ≠ s, the last two give p(s − q) = c − aq, so p
   is forced; if q = s, p and r are the roots of t² − at + (b − 2q),
   integer only when the discriminant is a perfect square. Each
   candidate is checked against all four equations.

Divisors of numbers up to 20000 take √20000 steps, and every value
stays below 10¹⁸. `O(√|d|)`.

Pitfalls:

- the factors may come in any order; a checker multiplies them back,
  counts them and checks how each one is written;
- x⁴ + 4 has no root but splits into (x² + 2x + 2)(x² − 2x + 2)
  (test 11);
- equal constant terms in the two quadratics need the discriminant
  route (test 06).

The answers match an independent accepted implementation on random and
constructed inputs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1666_math.cpp](1666_math.cpp) | G++ 13.2 x64 | math | O(sqrt d) | AC | 0.031 s | 200 KB |
| [1666_math.go](1666_math.go) | Go 1.14 x64 | math | O(sqrt d) | AC | 0.031 s | 1100 KB |
| [1666_math.java](1666_math.java) | Java 1.8 | math | O(sqrt d) | AC | 0.125 s | 1716 KB |
| [1666_math.py](1666_math.py) | Python 3.12 x64 | math | O(sqrt d) | AC | 0.093 s | 752 KB |
| [1666_math.rs](1666_math.rs) | Rust 1.75 x64 | math | O(sqrt d) | AC | 0.031 s | 240 KB |
