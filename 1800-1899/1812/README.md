# 1812. The Island of Bad Luck 2

[Timus 1812](https://acm.timus.ru/problem.aspx?space=1&num=1812) · difficulty 2729 · math

Original problem from the Tavrida NU Akai Contest, Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two circles of radii r₁ and r₂ touch a line and each other. In each of
n rounds, a circle touching the line and both is inscribed between
every two neighbouring circles. Number all circles along the line,
starting from the r₁ circle. Print the radius of the i-th circle as an
irreducible fraction, or "Irrational".

## Input

r₁, r₂, n and i (1 ≤ r₁, r₂ ≤ 1000, 0 ≤ n ≤ 30, 1 ≤ i ≤ 2ⁿ + 1).

## Output

The radius as p/q, or "Irrational".

## Examples

### Example 1

Input:

```
1 1 1 2
```

Output:

```
1/4
```

### Example 2

Input:

```
3 5 2 4
```

Output:

```
Irrational
```

## Solution

Two circles of radii r and s touching a line and each other are
2√(rs) apart along it, and the circle inscribed between them has
1/√t = 1/√r + 1/√s. So every circle has
1/√r = a/√r₁ + b/√r₂, where the pairs (a, b) behave like Stern's
diatomic sequence: the ends have (1, 0) and (0, 1), and a new circle
gets the sum of its neighbours' pairs. The pair at position x after n
rounds comes from the coarser level: an even x is an old circle, an odd
x is the sum of the two around it. Writing the value as α·f(x) +
β·f(x + 1) and halving x n times gives (a, b) in n steps.

The end circles keep r₁ and r₂. For an inner circle both a and b are
positive, and 1/r = a²/r₁ + b²/r₂ + 2ab/√(r₁r₂) is rational exactly
when r₁r₂ is a square. With g = gcd(r₁, r₂) that means r₁ = g·p² and
r₂ = g·q², and then r = g·p²·q² / (a·q + b·p)². `O(n)`.

In the first example the middle circle between two unit circles has
1/√r = 2, so r = 1/4. In the second 3·5 = 15 is not a square.

Pitfalls:

- the end circles are rational even when r₁r₂ is not a square;
- a and b grow like Fibonacci numbers, so (a·q + b·p)² needs 64 bits;
- the fraction must be reduced.

The answers agree with an independent accepted implementation on 430
inputs, among them every circle after up to 3 rounds and positions
deep in 30 rounds.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1812_math.cpp](1812_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 128 KB |
| [1812_math.go](1812_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1080 KB |
| [1812_math.java](1812_math.java) | Java 1.8 | math | O(n) | AC | 0.109 s | 1636 KB |
| [1812_math.py](1812_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 500 KB |
| [1812_math.rs](1812_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 232 KB |
