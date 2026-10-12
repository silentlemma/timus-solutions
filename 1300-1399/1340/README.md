# 1340. Cucaracha

[Timus 1340](https://acm.timus.ru/problem.aspx?space=1&num=1340) · difficulty 4914 · geometry

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

- Arc and segment: if the crumb is not inside the circle, the cockroach
  turns until it faces the crumb along a tangent. With the crumb at
  distance d from the center, the segment is √(d² − R²) long, and the
  tangent point lies acos(R / d) before the direction of the crumb as
  seen from the center.
- Two arcs: the second circle touches the first, so its center is 2R
  from the first center, and it passes through the crumb, so its center
  is R from the crumb. Each of the at most two points that meet both
  conditions gives a path; the two arc angles follow from the angles
  around the centers.

All arc angles are measured in the direction of the turn and taken
modulo 2π. An angle a rounding error below a full turn is read as no
turn, or a crumb straight ahead would cost a full circle. The answer is
the shortest of the at most six candidates. `O(1)`.

Pitfalls:

- with the crumb inside a turning circle, the arc-and-segment path on
  that side does not exist, and two arcs can be shortest (test 06);
- a crumb straight ahead must give the plain distance, not a full
  circle and back (test 03);
- the crumb under the cockroach is reached at once, 0 (test 05);
- R = 0 lets the cockroach turn on the spot (test 02).

The answers were compared, on 300 random cases, with a search over the
final heading that tries all six standard Dubins paths for each heading.
The paths of that search were checked by following them step by step.
The largest gap was 5 · 10⁻⁵, the step of the search.

## Language notes

- All five solutions try the same candidates.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1340_geometry.cpp](1340_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 204 KB |
| [1340_geometry.go](1340_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1104 KB |
| [1340_geometry.java](1340_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 2008 KB |
| [1340_geometry.py](1340_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 736 KB |
| [1340_geometry.rs](1340_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 272 KB |
