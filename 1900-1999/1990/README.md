# 1990. Widest horizontal segment through a corridor

[Timus 1990](https://acm.timus.ru/problem.aspx?space=1&num=1990) · difficulty 1061 · geometry, sorting

Original problem by Denis Dublennykh, prepared by Egor Shchelkonogov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two nonintersecting, nontouching polylines bound a corridor on the left
and right. Their vertex heights strictly increase, and both polylines
have the same bottom and top heights. A horizontal segment starts
anywhere at the bottom and must reach the top by a continuous path. It
may translate in any direction, but cannot rotate or leave the corridor.
Touching a wall is allowed.

There are point obstacles, possibly outside the corridor. An obstacle
may touch either endpoint of the segment, but cannot lie in its strict
interior. Find the maximum segment width permitting a route.

Each wall has between 2 and 100000 vertices; there are `0≤q≤100000`
obstacles. Coordinates are integers of absolute value at most `10⁹`.
Obstacles are listed in nondecreasing order of height; their horizontal
coordinates within a height are arbitrary. Time limit: 1 second; memory
limit: 64 MB.

## Input

The number `n` of left-wall vertices followed by their `x y` pairs; then
the number `m` of right-wall vertices and their pairs; then `q` and the
obstacle pairs. Each wall's vertices appear in strictly increasing `y`
order. At every height between the shared endpoints, the left wall is
strictly to the left of the right wall.

## Output

One real number: the largest feasible width.

## Checking

Numbers are compared with absolute or relative error 10⁻⁶.

## Examples

Input:

```
2
0 0
5 10
3
5 0
10 5
10 10
1
6 5
```

Output:

```
4.0
```

At obstacle height 5 the walls have coordinates 2.5 and 10. The point at
6 leaves gaps 3.5 and 4. Elsewhere the wall spacing is at least 5, so
width 4 is optimal.

## Solution

Write the wall positions at height `y` as `L(y)<R(y)`. Without
obstacles, the width is bounded by `C=min_y(R(y)−L(y))`. Between
consecutive heights in the union of wall vertices, both walls are
affine, so their difference is affine and its minimum occurs at an
endpoint. Evaluate every left vertex against the right polyline and
every right vertex against the left. Each opposing-edge index only
advances, giving `O(n+m)` work.

For each distinct obstacle height within the corridor's height range,
sort the obstacle `x` coordinates and discard those outside
`[L(y),R(y)]`. Insert the two walls as endpoints. Let `G(y)` be the
largest gap between consecutive remaining coordinates. A segment avoids
all obstacle interiors at this height exactly when its width is at most
`G(y)`. Duplicate points add zero gaps; points on a wall cause no
additional restriction. If no obstacle remains inside, that level
imposes only the wall-width constraint already included in `C`.

The answer is `min(C, min_y G(y))`. Different obstacle heights impose
separate constraints: a point has zero vertical extent, so points at
different heights do not form a continuous barrier by themselves.
Process one height group at a time and move two wall cursors forward to
evaluate its boundaries.

### Why these local bounds suffice

Every bottom-to-top continuous route crosses every intermediate height.
Thus each wall-width and obstacle-gap bound is necessary, even if the
route moves backwards in height.

For sufficiency, collect all wall-vertex and obstacle heights. At each
such event, choose any allowed placement of a segment of the proposed
width `w`. Its left endpoint `a` satisfies `L(y)≤a≤R(y)−w`. Between
consecutive event heights there is no obstacle and both walls are
affine. Linearly interpolate the chosen left endpoints: both
inequalities hold throughout the slab by convexity. Connecting these
segments constructs a route increasing in height. At an event, its
chosen placement is safe by construction. Equalities are allowed because
walls and obstacle tips may be touched. Therefore the local bounds are
sufficient, including at the maximum width.

### Stable interpolation

Do not first interpolate two large floating coordinates and subtract
them. For a wall vertex `(x,y)` opposite an edge `(aₓ,aᵧ),(bₓ,bᵧ)`,
compute the signed clearance numerator `(aₓ−x)(bᵧ−y)+(bₓ−x)(y−aᵧ)` in
integers, then divide by `bᵧ−aᵧ`. Reverse the sign when evaluating a
right vertex against the left wall.

At an obstacle level store each wall as a fraction `N/D`, with
`N=aₓ(bᵧ−y)+bₓ(y−aᵧ)` and `D=bᵧ−aᵧ>0`. Test obstacle inclusion by
integer products. The boundary gaps are `(x·D−N)/D` and `(N−x·D)/D`;
gaps between obstacles are integers. At the final vertex use its
coordinate with denominator 1. Cancellation happens before floating
conversion.

The nonnegative interpolation weights sum to at most `2·10⁹`. Thus a
clearance numerator is at most `4·10¹⁸` in absolute value, a coordinate
numerator at most `2·10¹⁸`, and all used products and differences fit
signed 64-bit integers. Avoid cross-multiplying two wall fractions,
which would require a larger bound. Convert only a completed gap to
double; print twelve decimal places.

## Language notes

If `k_y` obstacles share a height, time is `O(n+m+q+Σ k_y log(k_y+1))`,
hence `O(n+m+q log(q+1))`. The walls and largest group of size `K` use
`O(n+m+K)` memory. Groups are consumed in input order; no global
obstacle sort is needed. Go and Rust additionally retain `I` input
bytes, giving actual memory `O(n+m+K+I)`. Other versions stream input.

Java uses primitive-array heapsort for a guaranteed `O(k log k)` group
sort, a byte-buffer reader and `long` products. C++, Go and Rust use
signed 64-bit coordinates before multiplication. Python uses exact
integers. A zero-obstacle input, groups at the bottom/top, out-of-range
heights and unsorted horizontal coordinates all follow the same rules.
Binary search with interval feasibility is an alternative, but requires
repeated sweeps.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1990_geometry.cpp](1990_geometry.cpp) | G++ 13.2 x64 | geometry | O(n+m+q log(q+1)) | AC | 0.109 s | 3164 KB |
| [1990_geometry.go](1990_geometry.go) | Go 1.14 x64 | geometry | O(n+m+q log(q+1)) | AC | 0.046 s | 20820 KB |
| [1990_geometry.java](1990_geometry.java) | Java 1.8 | geometry | O(n+m+q log(q+1)) | AC | 0.171 s | 8564 KB |
| [1990_geometry.py](1990_geometry.py) | Python 3.12 x64 | geometry | O(n+m+q log(q+1)) | AC | 0.625 s | 28596 KB |
| [1990_geometry.rs](1990_geometry.rs) | Rust 1.75 x64 | geometry | O(n+m+q log(q+1)) | AC | 0.031 s | 12468 KB |
