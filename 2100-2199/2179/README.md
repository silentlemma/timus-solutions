# 2179. Most non-crossing straight roads between cities

[Timus 2179](https://acm.timus.ru/problem.aspx?space=1&num=2179) · difficulty 1535 · geometry

Original problem by Vadim Barinov, from the Ural School Programming Contest 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N distinct cities are points in the plane. A road is a straight segment
between two cities with no other city on it, and roads may only meet at
shared endpoints. Find the largest number of roads. The limits are
1 second and 256 MB.

## Input

N, 2 ≤ N ≤ 10⁵, then N points with coordinates up to 10⁹ in absolute
value.

## Output

The largest number of roads.

## Examples

### Example 1

Input:

```
4
3 1
-2 -3
1 0
0 6
```

Output:

```
6
```

## Solution

A set of roads that cannot take one more is a triangulation of the
points: every bounded face is a triangle and the outer boundary is the
convex hull. If h cities lie on the hull boundary, collinear ones
included, Euler's formula gives every triangulation the same
3N − 3 − h edges, so the answer only needs h.

The monotone chain builds the lower and upper hull of the sorted points
and pops a point only on a strict right turn, so cities lying on a hull
edge stay in the chain. The two chains share their two ends, so
h = lower + upper − 2. When all cities are on one line both chains hold
all N of them, h comes out as 2N − 2, and the formula gives the N − 1
roads between neighbors, which is right.

In the example (1, 0) lies inside the triangle of the other three, so
h = 3 and the answer is 12 − 3 − 3 = 6: the three sides and three roads
to the inner city.

Sorting makes it O(N log N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2179_geometry.cpp](2179_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.062 s | 4392 KB |
| [2179_geometry.go](2179_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.078 s | 13208 KB |
| [2179_geometry.java](2179_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.187 s | 7228 KB |
| [2179_geometry.py](2179_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.484 s | 25840 KB |
| [2179_geometry.rs](2179_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.062 s | 8148 KB |
