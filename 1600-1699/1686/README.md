# 1686. Photovoltaic Spaceship

[Timus 1686](https://acm.timus.ru/problem.aspx?space=1&num=1686) · difficulty 1456 · geometry

Original problem by Pavel Atnashev, from the Tenth Ural State University Open Personal Contest, February 28, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tetrahedral spaceship is covered with solar panels. Each star shines
from a given direction with an intensity equal to the length of the
direction vector; a square metre lit with intensity I at incidence
angle α gives I · cos α watts. Find the total power, doubled as the
story demands.

## Input

The four vertices (integers up to 100 in absolute value, not
coplanar), then n (1 ≤ n ≤ 10) and the n star vectors, integers, with
lengths greater than 0 and at most 2500 and different directions.

## Output

The doubled power, with an error of at most 10⁻⁵.

## Examples

### Example 1

Input:

```
0 -1 0
0 1 0
0 0 2
1 0 0
2
0 0 -1358
21 0 0
```

Output:

```
2800.00000
```

## Solution

The tetrahedron is convex, so no face shades another, and a face is lit
by a star exactly when its outward normal points toward the star. For
a face with unit outward normal n̂ and area A, a star vector d gives
A · max(0, n̂ · d). Take instead the cross product N of two edges of the
face, turned away from the fourth vertex: it is the outward normal of
length 2A, so the face gives max(0, N · d) / 2. Doubling cancels the
half, and the answer is the integer Σ max(0, N · d) over the four faces
and all stars, printed with five zero decimals. `O(n)`.

Pitfalls:

- orient each normal against the opposite vertex: the input order of
  the vertices says nothing about orientation;
- a star in the plane of a face gives that face nothing (test 03).

The answers match an independent accepted implementation that
projects the tetrahedron onto the plane across each star and takes the
area of the silhouette.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1686_geometry.cpp](1686_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 132 KB |
| [1686_geometry.go](1686_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1132 KB |
| [1686_geometry.java](1686_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.093 s | 472 KB |
| [1686_geometry.py](1686_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.078 s | 684 KB |
| [1686_geometry.rs](1686_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.046 s | 236 KB |
