# 1065. The shortest sub-polygon that keeps given points inside

[Timus 1065](https://acm.timus.ru/problem.aspx?space=1&num=1065) · difficulty 1413 · dp, geometry

Original problem from the ACM ICPC Northeastern European Regional Contest 2000–2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A convex polygon with `N` vertices (`3 ≤ N ≤ 50`, clockwise, integer
coordinates up to 10000 in absolute value; several vertices may lie on one
side) and `M` points inside it (`0 ≤ M ≤ 1000`) are given. Choose some of
the vertices, keeping their order, so that they form a polygon with
non-zero area that has all `M` points strictly inside, and its perimeter is
as small as possible. Print the perimeter with two decimals.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N` and `M`, then `N` lines with the vertices in clockwise order, then `M`
lines with the points.

## Output

The smallest perimeter, with at least two digits after the decimal point.

## Checking

Numbers are compared with an absolute error of 0.011: the answers are
printed with two decimals, so the last digit may differ by one.

## Examples

### Example 1

Input:

```
5 0
8 9
0 -7
-8 -7
-8 1
-8 9
```

Output:

```
27.31
```

### Example 2

Input:

```
5 2
8 9
0 -7
-8 -7
-8 1
-8 9
-4 -3
-1 -5
```

Output:

```
51.78
```

## Solution

Vertices of a convex polygon taken in their order always form a convex
polygon, so the only question is which sides `i → j` may be used. The new
polygon also goes clockwise, so its inside is on the right of every side:
a side is allowed when every point lies strictly to its right (a negative
cross product). That takes `O(N^2 · M)`.

The new border is then a cycle that goes around once through allowed
sides. For each first vertex `s`, a DP over the following vertices in
order gives the shortest way from `s` to each of them, and an allowed side
back to `s` closes the border. `O(N^3)`.

Without points (`M = 0`) every side is allowed, but the border must not
collapse: three vertices on one side of the original polygon have no area.
Every convex polygon contains a triangle of its own vertices with a
perimeter that is not larger, so the answer is the shortest triangle of
vertices with a non-zero area. With at least one point the border
encloses it, so a degenerate border cannot appear.

Pitfalls:

- the points must be strictly inside: a point on a side does not count;
- collinear vertices of the original polygon: a "triangle" of three of
  them is not a polygon;
- coordinate differences reach `2 · 10^4`, so a cross product reaches
  `8 · 10^8`: it fits 32-bit integers only just, and the solutions use
  64-bit ones.

The answers were checked against all subsets of vertices for small `N`.

## Language notes

- All languages use exact integer cross products and floating point only
  for the lengths.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1065_dp_geometry.cpp](1065_dp_geometry.cpp) | G++ 13.2 x64 | dp, geometry | O(N^2 · M + N^3) | AC | 0.015 s | 276 KB |
| [1065_dp_geometry.go](1065_dp_geometry.go) | Go 1.14 x64 | dp, geometry | O(N^2 · M + N^3) | AC | 0.015 s | 1188 KB |
| [1065_dp_geometry.java](1065_dp_geometry.java) | Java 1.8 | dp, geometry | O(N^2 · M + N^3) | AC | 0.125 s | 1172 KB |
| [1065_dp_geometry.py](1065_dp_geometry.py) | Python 3.12 x64 | dp, geometry | O(N^2 · M + N^3) | AC | 0.656 s | 1056 KB |
| [1065_dp_geometry.rs](1065_dp_geometry.rs) | Rust 1.75 x64 | dp, geometry | O(N^2 · M + N^3) | AC | 0.031 s | 340 KB |
