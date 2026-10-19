# 1894. Non-Flying Weather

[Timus 1894](https://acm.timus.ru/problem.aspx?space=1&num=1894) · difficulty 1395 · geometry

Original problem by Daniil Ayzenshteyn, from the NEERC 2011 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two strictly convex, nondegenerate polygons are given at their positions
60 seconds ago. Polygon A is stationary; polygon B translates without
rotation at exactly 1 meter per second in an unknown constant direction.
In the snapshot, B covers at least one interior point of A.

Find the minimum possible waiting time from now until the polygons
separate, over all possible fixed movement directions. If some direction
could have separated them already, the answer is 0. The limits are
2 seconds and 64 MB.

## Input

The first line contains n and m, the vertex counts of A and B, with
3 ≤ n, m ≤ 50 000. The next n lines give A's vertices, followed by
m lines giving B's vertices. Both lists are in counterclockwise order.
Coordinates are integer meters with absolute value at most 10⁸.

## Output

Print the minimum remaining time in seconds.

## Checking

Absolute or relative error must not exceed 10⁻⁶.

## Examples

### Example 1

Input:

```
4 4
400 400
600 400
600 600
400 600
0 0
1000 0
1000 1000
0 1000
```

Output:

```
540.0
```

## Solution

Let K = A + (−B) be the Minkowski difference: it consists of all vectors
a − b with a in A and b in B. After translating B by a vector v, the
polygons intersect exactly when v belongs to K. The initial overlap
guarantees that the origin lies strictly inside K.

For a fixed unit direction u, the displacement after t seconds is t·u.
Clearing A means leaving K along that ray. The shortest possible exit
distance over all rays is therefore the distance r from the origin to
the boundary of K: every exit reaches that boundary, and a closest
boundary point supplies a direction attaining the clearance threshold.
Since the speed is 1 and the snapshot is 60 seconds old, the answer is
max(0, r − 60).

Construct K in linear time. Negate every vertex of B; this preserves
counterclockwise order. Rotate each polygon's list to start at its
lowest vertex, breaking ties by x-coordinate. Their edge directions
are then already in angular order. Merge the two edge lists by angle,
advancing the smaller direction or adding both vectors when they are
parallel and point the same way. Starting at the sum of the first
vertices, these steps produce K's boundary in counterclockwise order.

For consecutive vertices p and q of K, the distance from the origin
to their supporting line is cross(p, q) / hypot(q − p). The numerator
is positive because the origin is inside. Take the minimum over edges.
This also equals the distance to the polygon boundary: if r is the
smallest supporting-line distance, the disk centered at the origin
with radius r lies inside every defining half-plane. Its contact with
a closest supporting line is therefore on the corresponding edge.

The merge can evaluate each new edge immediately, so it need not store
K separately. Reading the polygons, merging and scanning take
`O(n + m)` time and `O(n + m)` memory for the input arrays.

In the example, K is the square [−600, 600] × [−600, 600]. Its nearest
boundary is 600 meters from the origin, so the minimum remaining time
is 600 − 60 = 540 seconds.

Pitfalls:

- subtract the elapsed 60 seconds and clamp the answer at zero;
- negate B without reversing its vertex order;
- merge equal edge directions together;
- keep cross products exact in signed 64-bit integers before the
  floating-point division; Python integers already have enough precision;
- do not square a cross product in 64-bit arithmetic: it may overflow;
- negative coordinates are valid; use signed arithmetic and `hypot`.

The tests include a thin polygon that catches precision loss and
polygons with 50 000 vertices each; the answers were also checked
separately on 128 cases.

## Language notes

Keep the edge-direction and distance cross products in integer
arithmetic: C++ uses `long long`, Go `int64`, Java `long` and Rust `i64`;
Python integers have arbitrary precision. Convert to floating point only
for the hypotenuse and final division, so nearly parallel coordinates do
not lose the sign or the small difference of large products.

All versions print ten digits after the decimal point. Java explicitly
uses `Locale.US` so that the decimal separator is a dot.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1894_geometry.cpp](1894_geometry.cpp) | G++ 13.2 x64 | geometry | O(n + m) | AC | 0.031 s | 3148 KB |
| [1894_geometry.go](1894_geometry.go) | Go 1.14 x64 | geometry | O(n + m) | AC | 0.031 s | 8288 KB |
| [1894_geometry.java](1894_geometry.java) | Java 1.8 | geometry | O(n + m) | AC | 0.156 s | 4152 KB |
| [1894_geometry.py](1894_geometry.py) | Python 3.12 x64 | geometry | O(n + m) | AC | 0.296 s | 14956 KB |
| [1894_geometry.rs](1894_geometry.rs) | Rust 1.75 x64 | geometry | O(n + m) | AC | 0.031 s | 4744 KB |
