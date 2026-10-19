# 1966. Connectivity Along Intersecting Segments

[Timus 1966](https://acm.timus.ru/problem.aspx?space=1&num=1966) · difficulty 682 · dsu, geometry

Original problem from the Open Ural FU Personal Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n marked points and m closed straight segments joining pairs
of them. Movement is allowed in both directions along every segment.
Segments can be switched at any common point, even one without a mark.
A marked point lying inside a segment can also be visited. Determine
whether all marked points are reachable from the marked starting point.
The starting index is unnecessary: this holds exactly when all marks
belong to one connected geometric network. Limits: 1 second, 64 MB.

## Input

n,m with 1≤m<n≤200. Then n distinct integer coordinate pairs x,y, each
coordinate of absolute value at most 30,000. The next m lines give two
distinct indices between 1 and n, the endpoints of a segment. Repeated
segments and reversed endpoint pairs are allowed.

## Output

`YES` if all marked points are connected by allowed movement; otherwise `NO`.

## Checking

Outputs are compared token by token.

## Examples

```
4 2
0 0
1 0
1 1
0 1
1 3
4 2
```

```
YES
```

```
4 3
0 0
1 0
1 1
0 1
1 2
2 1
3 4
```

```
NO
```

```
3 2
0 0
1 0
1 1
1 3
3 2
```

```
YES
```

## Solution

In the first example the two diagonals intersect at the center of the
square. Switching there connects all four endpoints, giving YES, although
the endpoint-only graph has two components. In the second, the first
segment is listed again in reverse; it does not connect the lower side
to the separate upper side, so the answer is NO. In the third, the two
segments form a chain through a shared endpoint and reach all three marks.

Maintain a disjoint-set union structure on the n marked points. First
unite the two endpoints of every segment. For every pair of intersecting
closed segments, unite one endpoint of the first with one endpoint of
the second. Finally, for every marked point and every segment containing
it, unite that point with one endpoint of the segment. Return YES exactly
when every marked point has the same representative.

Each union is sound: its points can be joined along one segment, through
a common point of two segments, or from an interior mark to an endpoint.
Conversely, any allowed route follows a sequence of segments, changing
only at intersections. All endpoints of each segment are already united,
every possible change between segments is united, and every mark lying
on a segment is attached. Thus every physical connection is represented.
A mark outside all segments remains isolated, as required. This proves
the equivalence between the DSU test and geometric reachability.

Use exact integer predicates. For points a,b,c define the oriented area
cross(a,b,c)=(b_x−a_x)(c_y−a_y)−(b_y−a_y)(c_x−a_x).
A point is on a closed segment exactly when this value is zero and
both coordinates lie in the inclusive endpoint ranges.

Two closed segments intersect exactly when their x and y bounding
intervals overlap and the endpoints of each segment lie on opposite
sides of the other's supporting line, allowing zero. The bounding-box
test handles disjoint collinear segments; the non-strict sign tests also
handle shared endpoints, T-junctions and collinear overlap.

`O((nm+m²)·α(n))` time and `O(n+m)` space, using path compression and
union by size. There are nm point/segment tests and m(m−1)/2 segment
pairs. α is the inverse Ackermann function from disjoint-set operations.

An endpoint-only graph misses crossings and interior marks. The condition
m=n−1 does not guarantee connectivity, especially with duplicate segments.
All geometric contacts are inclusive. Collinearity alone does not imply
that segments overlap. Use signed 64-bit coordinates before multiplying:
a cross product may exceed signed 32-bit range. Do not multiply two raw
cross products even in 64 bits: magnitudes 3.6·10⁹ can produce 1.296·10¹⁹,
above signed 64-bit range. Compare their signs directly. No epsilon is needed.

## Language notes

C++ uses int64_t, Go 1.14 int64, Java 8 long and Rust 1.75 i64 for
geometry. Python 3.12 uses exact integers. Each version uses comparisons
for the straddle condition, iterative path compression, and union by
component size. No recursion, planar graph construction or floating point
is necessary.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1966_dsu_geometry.cpp](1966_dsu_geometry.cpp) | G++ 13.2 x64 | dsu, geometry | O((n*m+m*m)*alpha(n)) | AC | 0.015 s | 412 KB |
| [1966_dsu_geometry.go](1966_dsu_geometry.go) | Go 1.14 x64 | dsu, geometry | O((n*m+m*m)*alpha(n)) | AC | 0.031 s | 1116 KB |
| [1966_dsu_geometry.java](1966_dsu_geometry.java) | Java 1.8 | dsu, geometry | O((n*m+m*m)*alpha(n)) | AC | 0.140 s | 2260 KB |
| [1966_dsu_geometry.py](1966_dsu_geometry.py) | Python 3.12 x64 | dsu, geometry | O((n*m+m*m)*alpha(n)) | AC | 0.140 s | 784 KB |
| [1966_dsu_geometry.rs](1966_dsu_geometry.rs) | Rust 1.75 x64 | dsu, geometry | O((n*m+m*m)*alpha(n)) | AC | 0.046 s | 224 KB |
