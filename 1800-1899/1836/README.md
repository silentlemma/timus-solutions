# 1836. Babel Fish

[Timus 1836](https://acm.timus.ru/problem.aspx?space=1&num=1836) · difficulty 1170 · geometry

Original problem by Denis Dublennykh, from the Fifteenth Ural Championship in Sports Programming, April 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An open aquarium has a square base of side a. A sensor on each
vertical edge shows the water level on that edge; the car is tilted, so
the surface need not be parallel to the bottom. For each test, find the
volume of water, or say "error" if the readings cannot happen, or
"ambiguous" if they do not fix the volume.

## Input

t (1 ≤ t ≤ 10⁴), then t lines: a and the four levels, edges in order
around the base, all integers from 0 to 10⁶ with a > 0.

## Output

For each test the volume with absolute or relative error at most 10⁻⁶,
or "error", or "ambiguous".

## Examples

### Example 1

Input:

```
2
10 2 3 4 3
10 2 3 3 3
```

Output:

```
300.000
error
```

## Solution

The surface is a plane, so its heights f₁, …, f₄ over the corners
satisfy f₁ + f₃ = f₂ + f₄, and a sensor shows max(0, fᵢ): a reading of
0 only says fᵢ ≤ 0.

- No zero readings: the plane is known. It is consistent exactly when
  the diagonal sums agree, and the volume is a²·(h₁ + h₂ + h₃ + h₄)/4.
- All readings zero: the plane is nowhere above the bottom, volume 0.
- One zero, at corner i: the plane gives fᵢ = (left + right) − far,
  which must be at most 0. The plane dips below the bottom in a corner
  tetrahedron: it drops to fᵢ at the corner and crosses zero on the two edges
  at fractions −fᵢ/(left − fᵢ) and −fᵢ/(right − fᵢ). Its volume, a
  sixth of the product of its legs, is divided by a² and added to the
  mean height.
- Two or more zeros: the hidden heights only need to be at most 0 and
  balance the diagonals. If both diagonals hold a hidden corner they
  can always do that, in many ways; if only one does, it fails exactly
  when that diagonal's known sum is below the other one. In the other
  cases the volume is not fixed.

`O(1)` per test; Python's correction uses exact fractions, other
languages use floating point.

In the first example 2 + 4 = 3 + 3 and the volume is 100·12/4 = 300;
in the second 2 + 3 ≠ 3 + 3.

Pitfalls:

- a zero reading is not a height of zero, only a bound;
- with one dry corner the formula without the tetrahedron undercounts:
  for side 4 and levels 0 1 5 1 the hidden height is −3 and the volume
  is 16·(1 + 27/96) = 20.5, not 16;
- volumes reach 10¹⁸.

The answers agree with an independent accepted implementation on ten
thousand random tests, half of them true planes cut at the bottom.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1836_geometry.cpp](1836_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) per test | AC | 0.046 s | 460 KB |
| [1836_geometry.go](1836_geometry.go) | Go 1.14 x64 | geometry | O(1) per test | AC | 0.062 s | 2444 KB |
| [1836_geometry.java](1836_geometry.java) | Java 1.8 | geometry | O(1) per test | AC | 0.171 s | 6924 KB |
| [1836_geometry.py](1836_geometry.py) | Python 3.12 x64 | geometry | O(1) per test | AC | 0.156 s | 4868 KB |
| [1836_geometry.rs](1836_geometry.rs) | Rust 1.75 x64 | geometry | O(1) per test | AC | 0.015 s | 1292 KB |
