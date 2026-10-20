# 2165. Triangulation of a convex polygon with the largest smallest triangle

[Timus 2165](https://acm.timus.ru/problem.aspx?space=1&num=2165) · difficulty 1622 · dp, geometry

Original problem by Vadim Barinov, from the Ural School Programming Contest 2021.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Cut a convex polygon with N vertices into triangles by non-crossing
diagonals so that the smallest triangle is as large as possible, and
print its area within 10⁻⁹ absolute or relative error. The limits are 1 second and
256 MB.

## Input

N, 3 ≤ N ≤ 200, then the vertices counterclockwise, with coordinates up
to 10⁸ in absolute value.

## Output

The largest possible area of the smallest triangle.

## Examples

### Example 1

Input:

```
4
0 0
5 -1
8 3
0 4
```

Output:

```
11.5
```

## Solution

This is the classic interval DP over triangulations. Let f(i, j) be the
best smallest triangle in a triangulation of the sub-polygon with
vertices i … j. Its side (i, j) belongs to exactly one triangle (i, k, j)
with i < k < j, which splits it into the parts i … k and k … j, so

f(i, j) = max over k of min(f(i, k), f(k, j), area(i, k, j)),

with f(i, i + 1) = +∞ for a single side: an edge must not restrict the
minimum. C++ and Python use the doubled polygon area; Go, Java and Rust
use the safe upper bound 8 · 10¹⁶. Using zero would force every score to
zero, even on test 02. The answer is f(0, N − 1).
Areas are kept doubled as exact integers,
from cross products of up to about 4 · 10¹⁶, so the final half-integer
is printed exactly. Candidates that cannot beat the current best are
skipped early. The work is O(N³).

In the example the two triangulations of the quadrilateral give
smallest pieces of 11.5 and 10, so the answer is 11.5.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2165_dp_geometry.cpp](2165_dp_geometry.cpp) | G++ 13.2 x64 | dp, geometry | O(N^3) | AC | 0.031 s | 764 KB |
| [2165_dp_geometry.go](2165_dp_geometry.go) | Go 1.14 x64 | dp, geometry | O(N^3) | AC | 0.031 s | 1444 KB |
| [2165_dp_geometry.java](2165_dp_geometry.java) | Java 1.8 | dp, geometry | O(N^3) | AC | 0.109 s | 816 KB |
| [2165_dp_geometry.py](2165_dp_geometry.py) | Python 3.12 x64 | dp, geometry | O(N^3) | AC | 0.171 s | 2656 KB |
| [2165_dp_geometry.rs](2165_dp_geometry.rs) | Rust 1.75 x64 | dp, geometry | O(N^3) | AC | 0.015 s | 464 KB |
