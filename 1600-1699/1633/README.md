# 1633. Hippogriffs

[Timus 1633](https://acm.timus.ru/problem.aspx?space=1&num=1633) · difficulty 754 · math

Original problem by Igor Chevdar, from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A hippogriff with beak length A and claw length B has danger
√(A² + B²). An elixir turns them into a₁A + b₁B and a₂A + b₂B. Its
quality is the largest factor by which it can multiply the danger of any
hippogriff of nonzero danger. Find the quality.

## Input

Two lines: a₁ b₁, then a₂ b₂, non-negative integers up to 10⁶.

## Output

The quality, accurate to 9 digits after the decimal point.

## Examples

### Example 1

Input:

```
1 2
3 4
```

Output:

```
5.4649857042190426504511884932842
```

### Example 2

Input:

```
1 2
2 4
```

Output:

```
5
```

## Solution

The elixir is the matrix M = [[a₁, b₁], [a₂, b₂]] acting on the vector
(A, B), and the danger is the Euclidean length, so the quality is the
largest stretch of M: its largest singular value, the square root of the
largest eigenvalue of MᵀM.

The textbook form √((T + √(T² − 4D²)) / 2), with T = a₁² + b₁² + a₂² + b₂²
and D = a₁b₂ − b₁a₂, loses digits in doubles: when M is nearly a multiple
of a rotation, T² and 4D² are about 10²⁵ and almost equal, and their
difference loses significant digits. Factoring it avoids that:
T − 2D = (a₁ − b₂)² + (b₁ + a₂)² = Q and T + 2D = (a₁ + b₂)² + (b₁ − a₂)² = P,
and the singular values are (√P + √Q) / 2 and |√P − √Q| / 2. P and Q are integers
below 2⁵³, exact in a double, so the answer (√P + √Q) / 2 is half the sum of two
correctly rounded roots, accurate to about 2 · 10⁻¹⁰ even near 2 · 10⁶.
`O(1)`.

Pitfalls:

- the eigenvalue formula in doubles fails the precision on almost
  orthogonal matrices (tests 06, 07);
- the squares reach 4 · 10¹², past 32-bit integers;
- a matrix of rank one still has a positive norm (the second example),
  and the zero matrix has 0 (test 03).

The answers agree with an independent accepted implementation to within
2.4 · 10⁻¹⁰ on 200 random elixirs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1633_math.cpp](1633_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 140 KB |
| [1633_math.go](1633_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1088 KB |
| [1633_math.java](1633_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1820 KB |
| [1633_math.py](1633_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.109 s | 496 KB |
| [1633_math.rs](1633_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 264 KB |
