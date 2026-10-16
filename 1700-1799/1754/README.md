# 1754. Explosion in a Pyramid

[Timus 1754](https://acm.timus.ru/problem.aspx?space=1&num=1754) · difficulty 646 · geometry

Original problem by Alexander Ipatov, from the XI USU Open Personal Contest, March 13, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A hollow triangular pyramid has base corners (x₁, y₁, 0), (x₂, y₂, 0),
(x₃, y₃, 0) and apex (x₄, y₄, H). A lich rises from (x₀, y₀, 0) to
(x₀, y₀, h), which costs h mana, and makes a ball-shaped field around
that point, which costs its radius in mana. The pyramid collapses if
the field touches a wall or the floor. With m mana, can the lich bring
it down?

## Input

m, h and H (1 ≤ m, h, H ≤ 1000), then the five points xᵢ, yᵢ
(−1000 ≤ xᵢ, yᵢ ≤ 1000). The point (x₀, y₀, h) lies strictly inside
the pyramid.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
13 6 30
6 6
0 0
0 30
30 0
0 0
```

Output:

```
YES
```

### Example 2

Input:

```
11 6 30
6 6
0 0
0 30
30 0
0 0
```

Output:

```
NO
```

## Solution

After the rise m − h mana is left, and the field must reach the
nearest point of the pyramid's surface. From a point inside a convex
solid that is the distance to the nearest of its face planes: h to the
floor, and |n·(P − A)| / |n| to a wall through corners A, B and the
apex, where n is the cross product of B − A and apex − A. The answer is
`YES` when m − h ≥ 0 and one of these distances is at most m − h.

A distance can be exactly m − h, as with an upright wall, so it is
compared without rounding: |n·(P − A)| ≤ k·|n| becomes
(n·(P − A))² ≤ k²·|n|², with k = m − h. The left side reaches about
3·10²⁰, past 64 bits, so the products are taken in 128 bits, or with
big numbers where a language has nothing else. `O(1)`.

In the examples the floor and the two upright walls x = 0 and y = 0
are all 6 away and the sloped wall about 6.93, so 6 + 6 = 12 mana is
needed: 13 is enough, 11 is not.

Pitfalls:

- with m < h the lich cannot even rise;
- floating point with a tolerance can misjudge a distance that only
  just misses m − h;
- the base corners may come in either order around the triangle.

The answers agree with an independent accepted implementation on 450
random pyramids, a third of them with upright walls at whole-number
distances and the mana set right at the threshold.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1754_geometry.cpp](1754_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 124 KB |
| [1754_geometry.go](1754_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1084 KB |
| [1754_geometry.java](1754_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1688 KB |
| [1754_geometry.py](1754_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 596 KB |
| [1754_geometry.rs](1754_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 224 KB |
