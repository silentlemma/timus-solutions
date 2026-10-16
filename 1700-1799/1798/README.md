# 1798. Fire Circle. Version 2

[Timus 1798](https://acm.timus.ru/problem.aspx?space=1&num=1798) · difficulty 2105 · geometry

Original problem by Alexander Ipatov; a version of problem 1490 with a larger radius.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A floor is paved with 1 × 1 slabs, and a fire circle of radius R is
centred at a common corner of four slabs. A slab is damaged if it has
at least two common points with the fire circle. Count the damaged
slabs.

## Input

R, a whole number from 1 to 10⁹.

## Output

The number of damaged slabs.

## Examples

### Example 1

Input:

```
2
```

Output:

```
16
```

### Example 2

Input:

```
4
```

Output:

```
60
```

## Solution

As the examples show, the fire covers the whole disk. In the first
quarter, slab [x, x + 1] × [y, y + 1] shares more than a single point
with the disk exactly when its nearest corner is strictly inside:
x² + y² ≤ R² − 1 = n. So the answer is 4 times the number of lattice
points with x, y ≥ 0 in the disk x² + y² ≤ n.

By symmetry about the diagonal it is enough to sum g(x) = ⌊√(n − x²)⌋
over the columns x = 0 … m, where m = ⌊√(n/2)⌋, since there the circle
is no steeper than 45°. That is about 0.7·10⁹ columns, too many to visit.
Instead, walk from column m to the left along the upper convex hull of
the lattice points in the disk. Along a hull edge (a, b), going a
columns left and b rows up with gcd(a, b) = 1, every column holds the
floor of the edge line, so the a columns add a·y + (a − 1)(b − 1)/2 + b
at once. The next edge is found by a Stern–Brocot search between the
last direction that left the disk and one that stays inside. It stops
once, from an outside mediant point, steps along the inside direction
rise at least as fast as the circle, as then no inside point can lie
between the two directions. The hull has about R^(2/3)
vertices, so the walk takes about a million steps for R = 10⁹. Then
the first quarter holds 2·(Σ g(x) − m(m + 1)/2) + m + 1 points: the
part above the diagonal twice and the diagonal once. `O(R^(2/3))`.

In the second example n = 15 and m = 2; the columns 0, 1, 2 have
heights 3, 3, 3, so the quarter holds 2·(9 − 3) + 3 = 15 points and the
answer is 60.

Pitfalls:

- a slab touching the circle at one corner only is not damaged, hence
  the strict inequality and n = R² − 1;
- the answer is near π·10¹⁸, close to the limit of signed 64-bit
  integers;
- the slope test multiplies numbers near 10¹⁸ by squares of the edge
  lengths, which needs 128 bits: __int128, i128, bits.Mul64, or in Java
  doubles with an exact BigInteger check when the two sides are close.

Every radius up to 4000 gives the same column sum as a direct sum, and
the Go version agrees with an independent accepted implementation on
every radius up to 600 and on large ones up to 10⁹, among them
multiples of Pythagorean hypotenuses. The Python solution runs on PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1798_geometry.cpp](1798_geometry.cpp) | G++ 13.2 x64 | geometry | O(R^(2/3)) | AC | 0.031 s | 928 KB |
| [1798_geometry.go](1798_geometry.go) | Go 1.14 x64 | geometry | O(R^(2/3)) | AC | 0.046 s | 2516 KB |
| [1798_geometry.java](1798_geometry.java) | Java 1.8 | geometry | O(R^(2/3)) | AC | 0.218 s | 2672 KB |
| [1798_geometry.py](1798_geometry.py) | PyPy 3.10 x64 | geometry | O(R^(2/3)) | AC | 0.312 s | 3536 KB |
| [1798_geometry.rs](1798_geometry.rs) | Rust 1.75 x64 | geometry | O(R^(2/3)) | AC | 0.031 s | 1060 KB |
