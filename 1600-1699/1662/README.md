# 1662. Goat in the Garden 6

[Timus 1662](https://acm.timus.ru/problem.aspx?space=1&num=1662) · difficulty 4622 · geometry

Original problem by Alex Samsonov, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, January 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cabbage bed is a convex polygon. A stake is to be driven in outside
it, with a goat on a rope of length R and a kid on a rope of length r
tied to it, so that the goat reaches every point of the bed and the kid
reaches no interior point of it. Print a place for the stake, rounded to
10⁻⁶, or `No solution`.

## Input

N (3 ≤ N ≤ 50), then the N vertices of the polygon in order, integers
of absolute value at most 1000, then r and R (1 ≤ r < R ≤ 1000).

## Output

The coordinates of the stake, or `No solution`.

## Examples

### Example 1

Input:

```
4
0 0
0 1
1 1
1 0
1 3
```

Output:

```
0.500000 -1.000000
```

### Example 2

Input:

```
3
0 0
0 14
2 7
8 10
```

Output:

```
No solution
```

Any valid place is accepted; for the first example this solution prints
a different one.

## Solution

The goat reaches the whole bed exactly when it reaches every vertex, so
the stake must lie in A, the intersection of the discs of radius R
around the vertices. The kid misses the interior exactly when the stake
is at least r from the bed, that is, outside the interior of B, the bed
grown by r (its boundary is the edges pushed out by r joined by arcs of
radius r around the vertices). Both A and B are convex.

If some point of A lies outside the interior of B, then some point of
the boundary of A does too: move away from B across a line that
separates the point from it until A ends. The part of the boundary of A
outside B is made of pieces, and each piece either is the whole boundary
or ends where the boundary of A crosses the boundary of B. So it is
enough to try:

- the corners of A, where two circles of radius R meet;
- the points where a circle of radius R meets an edge pushed out by r;
- the points where a circle of radius R meets a circle of radius r
  around a vertex.

Each candidate is checked directly, with a tolerance of 10⁻⁷: within R
of every vertex, outside the bed and at least r from every edge. The
first that passes is printed. `O(N³)`.

Pitfalls:

- the answer may be a single point where everything is tight, for
  example where three circles of radius R meet (test 03), or exactly r
  from an edge and exactly R from a vertex (test 04); a search that only
  tries corners of A and midpoints of its arcs misses the second kind;
- the vertices may go either way round, which decides which side of an
  edge is outward;
- the checker accepts any place that meets the conditions within 10⁻⁵.

On random inputs, and at the smallest integer R that admits a place for
many polygons, the answers agree with an independent accepted
implementation about whether a place exists, except for the exact case
of test 04, where the place found here is checked to be valid.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1662_geometry.cpp](1662_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^3) | AC | 0.015 s | 216 KB |
| [1662_geometry.go](1662_geometry.go) | Go 1.14 x64 | geometry | O(N^3) | AC | 0.015 s | 1128 KB |
| [1662_geometry.java](1662_geometry.java) | Java 1.8 | geometry | O(N^3) | AC | 0.140 s | 1120 KB |
| [1662_geometry.py](1662_geometry.py) | Python 3.12 x64 | geometry | O(N^3) | AC | 0.093 s | 852 KB |
| [1662_geometry.rs](1662_geometry.rs) | Rust 1.75 x64 | geometry | O(N^3) | AC | 0.031 s | 272 KB |
