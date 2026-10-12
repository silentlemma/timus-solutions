# 1340. Cucaracha

[Timus 1340](https://acm.timus.ru/problem.aspx?space=1&num=1340) · difficulty 4615 · geometry

Original problem by Pavel Egorov, from the USU Championship 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cockroach stands at (X, Y) facing the direction A, in degrees
counter-clockwise from the x axis, and cannot turn more sharply than
along a circle of radius R. Find the length of the shortest path to a
crumb at (KX, KY), in any final direction, with four digits after the
point. All coordinates and R are at most 10 000 in absolute value.

Time limit: 1 second. Memory limit: 64 MB.

## Input

X, Y, A and R on the first line, KX and KY on the second.

## Output

The length of the shortest path.

## Examples

### Example 1

Input:

```
1 2 90 10
21 2
```

Output:

```
31.4159
```

## Solution

This is the shortest path of a car that drives forward with a bounded
turning radius, the Dubins car, to a point with any final heading. Such
a path is known to be either an arc followed by a straight segment, or
two arcs that turn in opposite directions. Both kinds start on one of
the two circles of radius R that touch the start, the left one or the
right one.

Translate the start to the origin and align its heading with the positive
x axis, reducing the angle by quadrants. Let (u, v) be the transformed
crumb, D² the original squared displacement, s = ±1 the turn direction,
and d the distance from (0, sR) to the crumb. Compute
q = D² − 2sRv = d² − R² directly; correct negative roundoff to zero
only within 10⁻¹⁵D².

- Arc and segment: if the crumb is not inside the circle, the cockroach
  turns until it faces the crumb along a tangent. Require q ≥ 0, use
  √q for the segment length, and compute the turn as
  atan2(u, R − sv) − atan2(√q, R).
- Two arcs: the second circle touches the first, so its center is 2R
  from the first center, and it passes through the crumb, so its center
  is R from the crumb. Each of the at most two points that meet both
  conditions gives a path; the two arc angles follow from the angles
  around the centers. Intersections require 0 ≤ q ≤ 8R²; use height
  √(q(8R² − q)) / (2d) to avoid subtracting nearly equal squares.

All arc angles are measured in the direction of the turn and taken
modulo 2π; the second arc uses atan2 of the cross and dot products of
its radius vectors. Do not expand distance intervals with a fixed epsilon
or replace almost-full turns with zero: an interior target can require
a long detour. The answer is the shortest of the at most six candidates. `O(1)`.

Pitfalls:

- with the crumb inside a turning circle, the arc-and-segment path on
  that side does not exist, and two arcs can be shortest (test 06);
- a crumb straight ahead must give the plain distance, not a full
  circle and back (test 03);
- return 0 for coincident endpoints before circle calculations (tests 05, 10);
- even just inside the forward turning circle, a tangent shortcut is
  impossible; an epsilon must not admit it (test 18);
- R = 0 lets the cockroach turn on the spot (test 02).

The answers were checked on 10 000 small random inputs against an
independent exhaustive switching-angle oracle, which verifies each
candidate by integrating the path.

## Language notes

- All five solutions try the same candidates.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1340_geometry.cpp](1340_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 196 KB |
| [1340_geometry.go](1340_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1200 KB |
| [1340_geometry.java](1340_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 1976 KB |
| [1340_geometry.py](1340_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 792 KB |
| [1340_geometry.rs](1340_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 272 KB |
