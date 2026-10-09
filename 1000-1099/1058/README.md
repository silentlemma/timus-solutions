# 1058. The shortest cut halving a convex polygon

[Timus 1058](https://acm.timus.ru/problem.aspx?space=1&num=1058) · difficulty 2756 · geometry

Original problem from the Rybinsk State Aviation Academy.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A convex polygon with `N` vertices (`4 ≤ N ≤ 50`, counterclockwise,
coordinates from −100 to 100 with at most three decimals) is cut by a
straight line into two parts of equal area. Find the smallest possible
length of the cut, with an error of at most `10^-4`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines with the coordinates of the vertices.

## Output

The smallest length of a halving cut.

## Checking

Numbers are compared with an absolute or relative error of `10^-4`.

## Examples

### Example 1

Input:

```
4
0 0
4 0
4 3
0 3
```

Output:

```
3.000000
```

### Example 2

Input:

```
4
0 -5
5 0
0 5
-5 0
```

Output:

```
7.071068
```

## Solution

Describe a cut by its first end `P` on the boundary, written as a position
`u ∈ [0, N)`: `u = i + t` is the point at fraction `t` of edge `i`. For
every `P` there is exactly one halving cut through it, and its other end
`Q` follows from areas:

- with prefix sums of the shoelace terms, twice the area of the polygon
  `P, V[i+1], …, V[j]` is an `O(1)` expression; it grows with `j`, so a
  binary search finds the edge `j` that contains `Q`;
- on that edge the area grows linearly with the position of `Q`, which
  gives `Q` exactly.

So the cut length `L(u)` is computed in `O(log N)`. As `u` moves, `L(u)`
is a smooth function except where `P` or `Q` passes a vertex. The
breakpoints are the integers and the partners of the vertices (the
partner relation is symmetric), at most `2N` of them. On each smooth
piece the solutions sample 64 points and refine every local minimum of
the samples, at the ends of the piece too, by a golden-section search;
the smallest value found is the answer.

This is a numerical search, not a closed formula: it relies on the length
having no two minima closer than the sampling step within one piece. It
was compared with a completely different method (a sweep over the
direction of the cut, where each halving line is found by bisection on its
offset) on about seventy random, regular, thin and nearly circular
polygons and on about a hundred random polygons with vertices on their
sides, a repeated vertex or clockwise order, always within `10^-6`.

Pitfalls:

- the cut need not pass through a vertex, nor be perpendicular to an
  edge;
- very thin polygons have very short cuts; relative precision matters;
- the walk along the boundary needs counterclockwise order; the solutions
  take the sign of the area and reverse a clockwise list instead of
  trusting the order (a first version that trusted it failed on the judge);
- a cut is found twice (from either end), which does no harm.

## Language notes

- All languages run the same search; the sizes are small, so it takes a
  few milliseconds even in Python.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1058_geometry.cpp](1058_geometry.cpp) | G++ 13.2 x64 | geometry | O(S·N log N), S = 64 samples | AC | 0.015 s | 232 KB |
| [1058_geometry.go](1058_geometry.go) | Go 1.14 x64 | geometry | O(S·N log N), S = 64 samples | AC | 0.031 s | 1140 KB |
| [1058_geometry.java](1058_geometry.java) | Java 1.8 | geometry | O(S·N log N), S = 64 samples | AC | 0.125 s | 2036 KB |
| [1058_geometry.py](1058_geometry.py) | Python 3.12 x64 | geometry | O(S·N log N), S = 64 samples | AC | 0.125 s | 976 KB |
| [1058_geometry.rs](1058_geometry.rs) | Rust 1.75 x64 | geometry | O(S·N log N), S = 64 samples | AC | 0.046 s | 276 KB |
