# 2196. The day a growing offset of a convex polygon reaches each point

[Timus 2196](https://acm.timus.ru/problem.aspx?space=1&num=2196) · difficulty 2094 · geometry, binary_search

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

On day 0 a convex polygon with N vertices is infected. Each later day
the infected set is all points within some distance of the polygon, and
its area doubles every day. For each of Q points, find the first day on
which it is inside or on the border of the infection. Points are at
least 10⁻⁶ away from every later border. The limits are 3 seconds and
256 MB.

## Input

N, 3 ≤ N ≤ 10⁵, then the vertices counterclockwise, then Q,
1 ≤ Q ≤ 10⁵, and the points, all coordinates up to 10⁹ in absolute
value.

## Output

The day for each point.

## Examples

### Example 1

Input:

```
4
1 3
1 1
3 1
3 3
4
2 2
1 2
4 1
6 2
```

Output:

```
0
0
2
4
```

## Solution

The set of points within distance d of a convex polygon with area A and
perimeter P has area A + P d + π d²: the polygon, a strip along each
side, and circular sectors at the corners that add up to a full circle.
So day i has the radius dᵢ that solves A + P d + π d² = 2ⁱ A, written as
dᵢ = (2ⁱ − 1) A / (P/2 + √(P²/4 + π (2ⁱ − 1) A)) to avoid cancellation.
The radii pass the largest possible distance after about 70 days, and a
point at distance D from the polygon is answered by the first dᵢ ≥ D.

The distance to a convex polygon takes O(log N) per point. A binary
search over the fan of triangles from vertex 0 finds whether the point
is inside (day 0) and, if not, two vertices separating the sides that
face the point from the rest. Along the facing chain the distance to
the sides first falls and then rises, so a second binary search, on the
sign of a projection, finds the closest side or vertex.

When the distance is within 10⁻⁵ of a radius, the comparison is redone
without square roots in double-double arithmetic: with the distance as
√(u / v) and E = (2ⁱ − 1) A, the point is infected when
E v − π u ≥ 0 and (E v − π u)² ≥ P² u v.

In the example the square has A = 4 and P = 8; the point (6, 2) is at
distance 3, and day 4 is the first with 8d + πd² = 60 at d ≈ 3.28.

The whole run takes O(N + Q log N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2196_geometry_binary_search.cpp](2196_geometry_binary_search.cpp) | G++ 13.2 x64 | geometry, binary_search | O(N + Q log N) | AC | 0.171 s | 7904 KB |
| [2196_geometry_binary_search.go](2196_geometry_binary_search.go) | Go 1.14 x64 | geometry, binary_search | O(N + Q log N) | AC | 0.187 s | 30296 KB |
| [2196_geometry_binary_search.java](2196_geometry_binary_search.java) | Java 1.8 | geometry, binary_search | O(N + Q log N) | AC | 0.578 s | 12632 KB |
| [2196_geometry_binary_search.py](2196_geometry_binary_search.py) | PyPy 3.10 x64 | geometry, binary_search | O(N + Q log N) | AC | 1.187 s | 49568 KB |
| [2196_geometry_binary_search.rs](2196_geometry_binary_search.rs) | Rust 1.75 x64 | geometry, binary_search | O(N + Q log N) | AC | 0.171 s | 15164 KB |
