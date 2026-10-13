# 1384. Goat in the Garden 4

[Timus 1384](https://acm.timus.ru/problem.aspx?space=1&num=1384) · difficulty 4368 · geometry

Original problem by Alexander Ipatov, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A garden is a simple polygon, not always convex, with 3 ≤ N ≤ 25
vertices with integer coordinates from 0 to 1000. A goat will be tied
to a stake somewhere inside it and may touch
the fence only when the rope is taut. Find the longest such rope over all
places for the stake, rounded to 2 digits after the point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N vertices counterclockwise.

## Output

The length of the rope.

## Examples

### Example 1

Input:

```
3
0 0
200 0
0 200
```

Output:

```
58.58
```

## Solution

The answer is the radius of the largest circle inside the polygon: the
largest distance from an inner point to the fence. The fence is made of
sites: an edge interior is represented by its line, and each reflex
vertex is a site of its own. A nearest fence point from inside cannot
be a convex vertex. Points nearest to two sites form a curve along
which the distance is linear (two lines) or convex (a line and a
vertex, two vertices), so a maximum can be chosen where at least three
sites meet.

So try every triple of sites and find the points at the same distance
from all three:

- three lines: a linear system n_i · p + c_i = r, with the unit normals
  pointing inside;
- two lines and a vertex: walk along the bisector of the lines, where
  the distance to the lines is linear, and solve a quadratic for the
  points as far from the vertex;
- a line and two vertices: the same along the perpendicular bisector of
  the vertices;
- three vertices: the centre of their circle.

Each candidate is checked for polygon membership and its minimum
distance to all edge segments. Extra interior candidates cannot
overestimate the answer, and an optimal centre is among the candidates.
At most 28 590 candidates are checked in O(N) each:
`O(N⁴)`.

Pitfalls:

- the circle may rest on inner corners only: in a plus sign of width 2
  the answer is √2, through four reflex vertices (test 03);
- at a right-angle turn of a corridor of width w the circle has radius
  about 0.586·w, more than half the corridor (test 10);
- a quadratic whose leading coefficient is near zero, or that only touches
  zero when a vertex lies on the line, needs a stable form of the roots;
- vertices in the middle of a side give the same line twice, and the
  system for them is singular (test 12).

The answers were compared on 150 random polygons, built from random
points by undoing crossings or as star shapes, with a grid search over
the polygon refined by local hill climbing. The tests are judged as
numbers within 0.011.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1384_geometry.cpp](1384_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^4) | AC | 0.031 s | 476 KB |
| [1384_geometry.go](1384_geometry.go) | Go 1.14 x64 | geometry | O(N^4) | AC | 0.031 s | 1780 KB |
| [1384_geometry.java](1384_geometry.java) | Java 1.8 | geometry | O(N^4) | AC | 0.187 s | 1488 KB |
| [1384_geometry.py](1384_geometry.py) | Python 3.12 x64 | geometry | O(N^4) | AC | 0.437 s | 2184 KB |
| [1384_geometry.rs](1384_geometry.rs) | Rust 1.75 x64 | geometry | O(N^4) | AC | 0.031 s | 532 KB |
