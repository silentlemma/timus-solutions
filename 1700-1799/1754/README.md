# 1754. Explosion in a Pyramid

[Timus 1754](https://acm.timus.ru/problem.aspx?space=1&num=1754) · difficulty 644 · geometry

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
1.6·10¹⁹, past signed 64 bits, so the products are taken in 128 bits, or with
big numbers where a language has nothing else. `O(1)`.

In the examples the floor and the two upright walls x = 0 and y = 0
are all 6 away and the sloped wall about 6.93, so 6 + 6 = 12 mana is
needed: 13 is enough, 11 is not.

Pitfalls:

- with m < h the lich cannot even rise;
- floating point with a tolerance can misjudge a distance that only
  just exceeds m − h;
- the base corners may come in either order around the triangle.

The answers agree with an independent accepted implementation on 450
random pyramids, a third of them with upright walls at whole-number
distances and the mana set near the threshold.

## Optimized solutions

The optimized versions form each side-plane normal directly in coordinates and compare squared products to test the remaining reach.

Python 3.12 x64, submission 11318516. Time 0.078 → 0.109 s, memory 592 → 508 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321958 · Java 1.8 №11321955 · Python 3.12 x64 №11321956 · Rust 1.75 x64 №11321957 · Go 1.14 x64 №11322211.

Go checks each face of the pyramid using exact integer comparisons for the relevant distances. Go 1.14 x64, submission 11322932. Time 0.015 → 0.015 s, memory 1092 → 276 KB.

Java 1.8, submission 11321993. Time 0.14 → 0.125 s, memory 1664 → 376 KB.

Rust compares squared distances to the plane without dividing by the length of its normal. Rust 1.75 x64, submission 11323317. Time 0.031 → 0.046 s, memory 224 → 48 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1754_geometry.cpp](1754_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 108 KB | 11321958 |
| [1754_geometry.go](1754_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1092 KB | 11322211 |
| [1754_geometry.java](1754_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.14 s | 1664 KB | 11321955 |
| [1754_geometry.py](1754_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 592 KB | 11321956 |
| [1754_geometry.rs](1754_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 224 KB | 11321957 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1754_geometry_optimized.py](1754_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 508 KB | 11318516 |
| [1754_geometry_optimized.go](1754_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 276 KB | 11322932 |
| [1754_geometry_optimized.java](1754_geometry_optimized.java) \* | Java 1.8 | geometry | O(1) | AC | 0.125 s | 376 KB | 11321993 |
| [1754_geometry_optimized.rs](1754_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 48 KB | 11323317 |

\* The marked versions have room to improve in the ratings.
