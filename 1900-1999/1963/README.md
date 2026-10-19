# 1963. Boundary Points on Reflection Axes

[Timus 1963](https://acm.timus.ru/problem.aspx?space=1&num=1963) · difficulty 496 · geometry

Original problem from Open Ural FU Personal Contest 2013 | by Alexander Ipatov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a simple quadrilateral in boundary order, count distinct points on
its boundary that belong to at least one reflection axis of the entire
figure. The quadrilateral may be concave. No three consecutive vertices
are collinear, and opposite sides do not intersect. Limits: 1 second, 64 MB.

## Input

Four lines, each with integer coordinates x,y of the next vertex in
cyclic order. Every coordinate has absolute value at most 1000.

## Output

One integer: the number of distinct boundary points on symmetry axes.
A reflection axis is a line whose reflection preserves the whole figure.

## Checking

Outputs are compared token by token.

## Examples

```
0 0
1 2
2 2
2 1
```

```
2
```

```
0 0
2 1
2 2
0 2
```

```
0
```

## Solution

In the first sample, reflection in y=x fixes (0,0) and (2,2), while
exchanging (1,2) and (2,1). These two fixed vertices are the boundary
points on the only axis, giving 2. In the second sample none of the four
possible vertex reflections preserves the polygon, so the answer is 0.

Index the vertices p_i by 0,…,3. Reflection maps corners to corners and
reverses their cyclic boundary order. Its induced permutation must be
i→(s−i) mod 4 for some s in 0,…,3. Thus only four candidates are needed.

For even s, two opposite vertices are fixed; the candidate line passes
through them. For odd s, two pairs of adjacent vertices are exchanged;
the line passes through the midpoints of these two opposite edges.
Represent its defining points A,B in doubled coordinates, so a vertex
becomes 2p and an edge midpoint becomes p+q. Half-integer positions stay
exact integers. Skip a zero direction D=B−A.

For every pair p,q under the proposed permutation, check

(p+q−A)×D=0 and (p−q)·D=0.

The cross product says their midpoint lies on the axis; the dot product
says their connecting segment is perpendicular to it. Together they are
exactly the condition that p reflects to q, including p=q. All arithmetic
is integral. Accept a candidate only if all four vertex pairs pass.

These tests are necessary for any reflection symmetry. Conversely, a
passing candidate maps each edge to the edge prescribed by the reversed
cyclic order, so it preserves the boundary and the enclosed figure.
This argument also applies to a concave quadrilateral.

The boundary intersections of a valid candidate are precisely its two
defining points. In the even case only the opposite fixed vertices lie
on the axis. In the odd case the two exchanged edges meet the axis at
their midpoints. Any further intersection would force an edge to meet
its reflected different edge away from a shared vertex, contradicting
simplicity. An entire edge cannot lie on the axis because adjacent
vertices cannot both be fixed by these permutations.

Insert both doubled points of every valid candidate into a set, then
return the size of the union. This counts points rather than axes and
does not rely on assuming their intersections are distinct.

`O(1)` time and `O(1)` space: four candidates, four vertex checks each,
and at most eight stored points.

Do not assume convexity, use only equal side lengths, or consider only
the diagonals. Edge-midpoint axes matter, and midpoint coordinates can
be half-integers. Keep the input boundary order. Reflection must preserve
edges as well as the vertex set. No floating point or epsilon is needed;
the four possible reversed cyclic permutations make the test complete.

## Language notes

C++, Go 1.14, Java 8 and Rust 1.75 use 64-bit integers for cross and dot
products. Python 3.12 uses exact integers. C++/Go/Python/Rust store the
doubled points in sets; Java scans a list of at most eight points to
deduplicate coordinates. No recursion or geometry library is needed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1963_geometry.cpp](1963_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 396 KB |
| [1963_geometry.go](1963_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1100 KB |
| [1963_geometry.java](1963_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1676 KB |
| [1963_geometry.py](1963_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 712 KB |
| [1963_geometry.rs](1963_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 232 KB |
