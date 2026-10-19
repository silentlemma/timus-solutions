# 1848. Fly Hunt

[Timus 1848](https://acm.timus.ru/problem.aspx?space=1&num=1848) · difficulty 4252 · geometry

Original problem by Denis Dublennykh, from the Ural SU Contest at the Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n flies sit at distinct points of a wall. m friends hit the wall with
swatters, leaving marks that are simple polygons with no common points.
A fly is killed if it lies inside a mark or on its border. Count the
flies killed by each swatter.

## Input

n (1 ≤ n ≤ 10⁵) and the flies' coordinates, then m (1 ≤ m ≤ 30 000)
and the marks, each as its number of corners and the corners in
counter-clockwise order. There are at most 10⁵ corners in all, and all
coordinates are integers of absolute value at most 10⁷.

## Output

The number of flies killed by each swatter, in input order.

## Examples

### Example 1

Input:

```
3
0 0
1 1
4 4
3
3 -2 -2 -3 -3 -2 -3
3 0 0 2 0 1 1
3 3 0 5 0 4 6
```

Output:

```
0
2
1
```

## Solution

The marks are disjoint, so none lies inside another, and a fly not on
any border is inside a mark exactly when the nearest side straight
above it is a side of that mark with the inside below it. In a
counter-clockwise polygon the inside is to the left of every side, so
the sides running from right to left are the ones with the inside below.

A vertical sweep from left to right keeps the sides that cross the
sweep line, ordered from bottom to top. To dodge the corners, a fly at
x is looked up just to the right of x: a side from x₁ to x₂ (x₁ < x₂)
is active for x₁ ≤ x < x₂, and in every column the sides that end leave
before the sides that start come in. A fly that sits at a corner is
inside after all, so the corners are kept in a hash table, and vertical
sides, which never enter the sweep, are kept per x as sorted intervals.
Every other fly on a border lies inside an active side.

Sides never cross, so two active sides are ordered by one orientation
test: take the one whose left end is further right and test that end
against the line of the other; when that end lies on it, the two sides
start at a common corner of one mark, and the other end decides. A fly
is compared the same way, as a side of length zero. All the products
stay below 4·10¹⁴. The first active side not below the fly either passes
through it or is the nearest side above it. The sides sit in a balanced
search tree (a treap in Go, a list of short sorted buckets in Python,
which runs on PyPy). `O((n + V) log V)` for V corners. The Python
solution keeps the edges and coordinates in flat integer arrays and
takes 25 MB on the judge; an earlier version with tuples and
dictionaries took 70 MB on the judge's test 11.

In the example the flies (0, 0) and (1, 1) are corners of the second
triangle. Just right of x = 4 the nearest side above (4, 4) is the side
of the third triangle from (5, 0) to (4, 6), which runs right to left,
so that fly is inside too.

Pitfalls:

- flies in line with a corner: looking just to the right of x avoids
  the ties between the two sides of a spike;
- vertical sides and corners must be checked apart from the sweep;
- sides given from the top down make every insertion land at the
  bottom, which a plain sorted list handles in quadratic time.

The counts agree with a direct test of every fly against every nearby
mark on random walls of up to 30 000 marks, with flies on grids, on
corners and on sides, and with an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1848_geometry.cpp](1848_geometry.cpp) | G++ 13.2 x64 | geometry | O((n + V) log V) | AC | 0.421 s | 18080 KB |
| [1848_geometry.go](1848_geometry.go) | Go 1.14 x64 | geometry | O((n + V) log V) | AC | 0.312 s | 36780 KB |
| [1848_geometry.java](1848_geometry.java) | Java 1.8 | geometry | O((n + V) log V) | AC | 0.671 s | 35404 KB |
| [1848_geometry.py](1848_geometry.py) | PyPy 3.10 x64 | geometry | O((n + V) log V) | AC | 0.906 s | 25480 KB |
| [1848_geometry.rs](1848_geometry.rs) | Rust 1.75 x64 | geometry | O((n + V) log V) | AC | 0.109 s | 25816 KB |
