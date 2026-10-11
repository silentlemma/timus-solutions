# 1305. Convex Hull

[Timus 1305](https://acm.timus.ru/problem.aspx?space=1&num=1305) · difficulty 708 · geometry

Original problem from the Second Ural Team Student Programming Championship, Yekaterinburg, April 3–4, 1998.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given up to 100 000 points with integer coordinates from 0 to 1000
(points may repeat), build their "regular convex hull": the smallest
convex set containing them whose boundary is a closed polyline with
every side either parallel to an axis or at 45° to the axes. Print its
vertices counterclockwise, each once, from any starting vertex, with
no three consecutive vertices (cyclically) on one line.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines with a point each.

## Output

The vertices of the hull, one per line.

## Checking

The hull is unique, but its walk may start at any vertex. The checker
accepts the expected vertex list turned round to any starting point.

## Examples

### Example 1

Input:

```
4
3 3
3 1
2 2
4 2
```

Output:

```
3 1
4 2
3 3
2 2
```

## Solution

A side of the hull can only point in one of eight directions, so its
outward normal is one of (1, 0), (1, 1), (0, 1), (−1, 1) and their
opposites. The smallest convex set with such sides is the intersection
of the tightest half-plane for each normal:

minX ≤ x ≤ maxX, minY ≤ y ≤ maxY, minS ≤ x + y ≤ maxS, minD ≤ x − y ≤ maxD.

One pass over the points finds these eight extremes. Going
counterclockwise from the bottom side, each corner is where an axis
line meets a diagonal one, for example (minS − minY, minY) and
(maxD + minY, minY) at the ends of the bottom side. All eight corners
have integer coordinates. Every one of the eight lines touches a real
point, so the corners always come in this order, but a side may have
zero length, and then its two corners coincide. Equal neighbours (also
around the end) are merged, and that is all the cleaning needed: the
sides that remain point in different directions of the eight, each
turning left from the one before, so no corner is left in the middle of
a straight side. A single point or a segment is what remains when all
sides but none or two vanish.

`O(N)`.

Pitfalls:

- a single point, even repeated, is printed once (tests 02 and 03);
- points on one line in one of the eight directions give a segment with
  two vertices (tests 04 and 05), but any other slope widens into a
  real polygon (test 06);
- several corners can coincide in a row, as at every tip of the sample
  diamond, where the axis-parallel sides have length 0 (test 01).

The output was checked on 300 random point sets: strictly convex and
counterclockwise, sides only in the eight directions, every side on its
tightest line, and every point inside.

## Language notes

- C++, Go and Java keep only the eight extremes while reading; Python
  and Rust read all the points first, which still fits easily.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1305_geometry.cpp](1305_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.109 s | 196 KB |
| [1305_geometry.go](1305_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.015 s | 1680 KB |
| [1305_geometry.java](1305_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.125 s | 544 KB |
| [1305_geometry.py](1305_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.078 s | 26160 KB |
| [1305_geometry.rs](1305_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 3716 KB |
