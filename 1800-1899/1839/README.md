# 1839. The Mentaculus

[Timus 1839](https://acm.timus.ru/problem.aspx?space=1&num=1839) · difficulty 2461 · geometry

Original problem by Alexey Samsonov (prepared by Victor Kamashev), from the Fifteenth Ural Championship in Sports Programming, April 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An arc PQR and two points A, B form a face when A and B lie on the
other side of line PR than Q, the angles APR, ARP, BPR, BRP are acute,
A and B are closer to line PR than twice the length of PR, and line AB
has no common point with segment PR. Given n arcs and m points, count
the faces.

## Input

n and m (1 ≤ n ≤ 100, 1 ≤ m ≤ 10⁴), then n arcs as three points in
order along the arc, each arc at most a half circle, then m points. All
coordinates are integers up to 10⁴ in absolute value.

## Output

The number of faces.

## Examples

### Example 1

Input:

```
2 7
-2 2 0 0 2 2
-2 -2 0 0 2 -2
-1 3
1 3
0 5
0 3
-1 -3
1 -3
2 -3
```

Output:

```
4
```

## Solution

Treat each arc separately. The first three conditions concern one
point at a time and are exact integer tests: the side of PR by a cross
product, the acute base angles by two dot products, and the distance
by |cross| < 2·|PR|². Call the points that pass eyes; they all project
strictly inside segment PR.

For two eyes A and B, line AB misses segment PR exactly when P and R
are strictly on one side of it. The orientation of P, A, B says whether
B is seen at a larger angle than A from P, and that of R, A, B whether
B is seen at a smaller angle from R. So the line misses PR exactly
when the two eyes come in opposite orders by the angle at P and by
the angle at R, and equal angles, which put P or R on the line, never
count. Sort the eyes by the angle at P, equal ones by the angle at R,
and count strict inversions of the angles at R with a Fenwick tree.

Angles are compared through their tangents height/near, with products
of numbers below 2³¹, so everything stays exact. `O(n·m log m)`.

In the example the upper arc gets eyes (−1, 3), (1, 3), (0, 3) and
(0, 5): the three on y = 3 pair up by parallel lines, while every
line through (0, 5) and another eye crosses PR. The lower arc gets
(−1, −3) and (1, −3); (2, −3) sees R at a right angle. That makes 3 + 1
faces.

Pitfalls:

- a line through P or R touches the segment, so eyes collinear with P
  or with R never pair up;
- right angles at P or R and points on line PR are excluded;
- the answer can exceed 2³¹;
- the Python solution sorts by float tangents first and then fixes the
  order with exact products, and runs on PyPy.

The answers agree with a check of every pair of points on hundreds of
small random pages and with an independent accepted implementation on
the large ones.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1839_geometry.cpp](1839_geometry.cpp) | G++ 13.2 x64 | geometry | O(n m log m) | AC | 0.234 s | 528 KB |
| [1839_geometry.go](1839_geometry.go) | Go 1.14 x64 | geometry | O(n m log m) | AC | 0.484 s | 7344 KB |
| [1839_geometry.java](1839_geometry.java) | Java 1.8 | geometry | O(n m log m) | AC | 0.515 s | 6980 KB |
| [1839_geometry.py](1839_geometry.py) | PyPy 3.10 x64 | geometry | O(n m log m) | AC | 2.078 s | 12808 KB |
| [1839_geometry.rs](1839_geometry.rs) | Rust 1.75 x64 | geometry | O(n m log m) | AC | 0.234 s | 1296 KB |
