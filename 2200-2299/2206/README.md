# 2206. Coprime lattice points inside a convex polygon

[Timus 2206](https://acm.timus.ru/problem.aspx?space=1&num=2206) · difficulty 1875 · geometry, number_theory

Original problem by Vadim Barinov, from the University Academic School Olympiad in Informatics 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A convex polygon with N vertices is given with coordinates that have
exactly three decimals. Count the points (x, y) with positive integer
coprime coordinates inside it or on its border. The limits are 4.5
seconds and 512 MB.

## Input

N, 3 ≤ N ≤ 2 · 10⁵, then the vertices counterclockwise, each
coordinate between 1 and 2 · 10⁶.

## Output

The number of coprime points.

## Examples

### Example 1

Input:

```
3
1.000 1.000
3.000 1.000
1.000 3.000
```

Output:

```
5
```

## Solution

Multiply all coordinates by 1000 to make them integers. For each
integer column x the polygon covers one segment of y, between its lower
and its upper chain. Walking each edge over the integer columns it
spans, exact integer division gives upper(x) = ⌊top⌋ and
lower(x) = ⌈bottom⌉ − 1, so the column contains upper(x) − lower(x)
integer points; a vertical edge adds nothing new.

Among them, the points with gcd(x, y) = 1 are counted by Möbius
inversion over the common divisor d:

Σ over d of μ(d) · Σ over columns x divisible by d of
(⌊upper(x) / d⌋ − ⌊lower(x) / d⌋).

For every d the inner sum visits W / d columns, where W is the width of
the polygon, so the total is O(W log W) with W ≤ 2 · 10⁶. A divisor
above half the rightmost column can only be the column itself, which
is handled with a single term. μ comes from a sieve.

In the example the triangle holds (1, 1), (1, 2), (1, 3), (2, 1), (2, 2)
and (3, 1), and only (2, 2) is not coprime, so the answer is 5.

This takes O(N + W log W).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2206_geometry_number_theory.cpp](2206_geometry_number_theory.cpp) | G++ 13.2 x64 | geometry, number_theory | O(N + W log W) | AC | 0.359 s | 26576 KB |
| [2206_geometry_number_theory.go](2206_geometry_number_theory.go) | Go 1.14 x64 | geometry, number_theory | O(N + W log W) | AC | 1.421 s | 67156 KB |
| [2206_geometry_number_theory.java](2206_geometry_number_theory.java) | Java 1.8 | geometry, number_theory | O(N + W log W) | AC | 0.781 s | 28460 KB |
| [2206_geometry_number_theory.py](2206_geometry_number_theory.py) | PyPy 3.10 x64 | geometry, number_theory | O(N + W log W) | AC | 1.968 s | 122932 KB |
| [2206_geometry_number_theory.rs](2206_geometry_number_theory.rs) | Rust 1.75 x64 | geometry, number_theory | O(N + W log W) | AC | 0.875 s | 61056 KB |
