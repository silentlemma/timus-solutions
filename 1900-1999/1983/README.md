# 1983. Triangle area inside a ball

[Timus 1983](https://acm.timus.ru/problem.aspx?space=1&num=1983) · difficulty 1547 · geometry

Original problem by Mikhail Rubinchik, from the Open Ural FU Championship 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three noncollinear points with integer coordinates of absolute value at
most 200 define a filled triangle in three-dimensional space. Find the
area of its intersection with the closed ball centered at the origin
with radius 100. This is planar area, not projected area or volume. Time
limit: 0.5 seconds; memory limit: 64 MB.

## Input

Three lines, each containing the three integer coordinates of one vertex.

## Output

One nonnegative real number: the intersection area.

## Checking

Numbers are compared with absolute or relative error 10⁻².

## Examples

Input:

```
0 0 0
0 2 0
2 0 0
```

Output:

```
2.00000
```

## Solution

Let `p,q,r` be the vertices, `n=(q−p)×(r−p)`, `N=n·n>0`, and `D=n·p`.
The triangle plane has equation `n·x=D`. Its intersection with the ball
is empty or a point if `F=10000N−D²≤0`; the answer is zero. Otherwise it
is a disk of squared radius `ρ²=F/N` centered at the projection of the
origin onto the plane.

Choose the unit vector `u=(q−p)/|q−p|`, unit normal `w=n/√N`, and
`v=w×u`. Map each vertex `x` to `(x·u,x·v)`. The disk center maps to
zero because it is parallel to `w`; this orthonormal chart preserves
area. The remaining problem is the intersection of a planar triangle
with a disk centered at zero.

Process every oriented edge `p+t e`, `0≤t≤1`, using its original integer
3D coordinates. Set `A=e·e`, `B=p·e`, `C=p·p−10000`, and `Δ=B²−AC`. The
sphere-interior part of this line satisfies `At²+2Bt+C<0`. If `Δ>0`, its
endpoints are the two quadratic roots. Compute them stably as `s/A` and
`C/s`, where `s=−B−copysign(√Δ,B)`, and sort them. Cut the edge at roots
strictly between zero and one. A subsegment is inside exactly when its
midpoint parameter lies strictly between the two roots. If `Δ≤0`, every
positive-length subsegment is outside; a tangent midpoint alone must
never classify an entire edge as inside.

For planar endpoints `a,b` of a subsegment, add `cross(a,b)` when it is
inside and `ρ²·atan2(cross(a,b),a·b)` otherwise. Sum these signed
contributions over the boundary, then take half the absolute value.
Interior pieces contribute their oriented triangular fan area; exterior
pieces contribute their oriented circular sector. The signed fans cancel
outside the triangle and count its intersection with the disk once.
Equivalently, this is the boundary integral of a continuous field with
curl one inside the disk and zero outside. Splitting at all crossings is
what makes each triangle/sector choice valid.

In the example the entire right triangle is inside the ball. Its
perpendicular sides have length 2, so its area is `2·2/2=2`.

There are always three edges and at most two roots per edge, hence
`O(1)` time and `O(1)` memory. Integer normal, plane residual and
discriminants are calculated before conversion to floating point; their
magnitudes fit signed 64-bit integers under the coordinate bounds.
Square roots, projections and angles use double precision.

Pitfalls:

- Vertices outside the ball do not imply zero area: the triangle can
  contain the whole disk.
- Preserve signs until the final absolute value; process the closing edge too.
- Plane tangency and edge tangency have zero interior extent, not a
  whole interior edge.
- Compute `F` and `Δ` with integer arithmetic to avoid cancellation
  changing intersection topology.
- Use `atan2`, not an unsigned angle or division by a dot product.
- Count surface area in the triangle plane, not its shadow on a
  coordinate plane.

## Language notes

All five versions use the same constant-size algorithm. C++, Go, Java
and Rust use signed 64-bit integers for the geometric predicates and
double precision for areas; Python uses exact integers and standard
floating-point math. Java fixes the output locale to use a decimal
point.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1983_geometry.cpp](1983_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 452 KB |
| [1983_geometry.go](1983_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1224 KB |
| [1983_geometry.java](1983_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1936 KB |
| [1983_geometry.py](1983_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 924 KB |
| [1983_geometry.rs](1983_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 260 KB |
