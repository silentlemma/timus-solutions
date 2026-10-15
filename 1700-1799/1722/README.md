# 1722. Observation Deck

[Timus 1722](https://acm.timus.ru/problem.aspx?space=1&num=1722) · difficulty 1355 · geometry

Original problem by Eugene Kurpilyansky, from the Ural Regional School Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The city is a disk of radius R around the origin. The observation deck
is the roof of a round building of radius r_old around the origin; a new
round building of radius r_new stands at (x, y). Both lie inside the
city and do not touch. A city point is hidden if from every point of the
deck the segment to it meets the new building. Find the hidden part of
the city in percent.

## Input

R, r_old and r_new (1 ≤ r_old < r_new < R ≤ 1000), then the integers x
and y.

## Output

The hidden part of the city in percent, with at least six digits after
the decimal point.

## Examples

### Example 1

Input:

```
10 1 3
-1 4
```

Output:

```
20.9346176061
```

## Solution

Fix a point P. The points Q for which the segment PQ meets the new
building form a convex set: the cone from P around the building, cut
off at the building's near side. P is hidden when the whole deck lies
in it, that is, when P lies between the two outer common tangents of
the buildings, behind the new one or inside it. Since r_new > r_old the
tangents move apart behind the new building, and the hidden part
reaches the city border.

Let d be the distance between the centers and k = (r_new − r_old)/d.
The unit normals of the tangents make an angle with cosine −k with the
direction to the new building, so they touch it at C + r_new·n on the
side that faces the deck, and run along C + (r_new − r_old)·n away
from it. Each leaves the city where |T + tD| = R, a quadratic in t.

The area follows by going around the hidden part counterclockwise and
adding signed areas seen from the new center C: the sector of the
building between the touching points on the deck's side, 2·acos k wide;
the triangles from C to each tangent piece; and the border arc, which
is the triangle from C to its ends plus the piece of the city cut off
by its chord. With signed areas the sum is right whatever the shape.
`O(1)`.

Pitfalls:

- the touching points lie on the deck's side of the new building, so
  the sector to add is the 2·acos k one, not the far one;
- the base of the new building is hidden too;
- `M_PI` is not standard C++ and is missing on the judge, so the C++
  solution uses `acos(-1)`.

The answers match a grid estimate made straight from the definition on
small cities, and an independent accepted implementation in all ten
printed digits on 500 random cases, including buildings that touch the
border or almost touch each other.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1722_geometry.cpp](1722_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 452 KB |
| [1722_geometry.go](1722_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1176 KB |
| [1722_geometry.java](1722_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1836 KB |
| [1722_geometry.py](1722_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 812 KB |
| [1722_geometry.rs](1722_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 264 KB |
