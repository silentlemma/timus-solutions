# 1733. Forgotten Technology

[Timus 1733](https://acm.timus.ru/problem.aspx?space=1&num=1733) · difficulty 4590 · geometry

Original problem by Pavel Atnashev (idea by Alex Samsonov), from the XIV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A rectangular book lies on a cloth, and a disk lies on the book with
its center inside the book or on its edge. A mouse runs on the cloth
only, so it cannot cross the book, and wants to reach a point of the
disk that hangs over the cloth, strictly outside the book. Find the
length of the shortest way.

## Input

The four corners of the book in counterclockwise order, then the
center and radius of the disk (radius at least 1), then the mouse.
All numbers are integers up to 1000 in absolute value. The mouse is
away from both the book and the disk, and a way exists.

## Output

The length of the shortest way, with an error of at most 10⁻⁵.

## Examples

### Example 1

Input:

```
-4 -3 8 6 5 10 -7 1
1 7 5
7 -1
```

Output:

```
12.07107
```

## Solution

The target is the part of the disk outside the book, together with its
edge. A shortest way around a convex obstacle runs straight between
the mouse and corners of the book, so it is a straight piece from the
mouse or from a corner to the target, after the shortest way to that
corner. Dijkstra over the mouse and the four corners gives those
shortest ways: the mouse is joined to every corner it sees, and each
corner to its two neighbours.

From a point s, the closest target point that s sees is one of:

- the point of the circle on the ray from the center to s, if it is
  outside the book and s sees it;
- the closest point of a side's chord inside the disk, if s is on the
  outer side of that side or on its line; the side is then fully in
  view.

Other target points never matter. Distance along the circle has a
single minimum, so on an arc it is the ray point or an arc end, which
is also a chord end; distance along a chord is convex. If the best
point were cut off by the edge of what s sees, the way to it would
pass a corner, and that corner as a starting point does at least as
well. The answer is the least shortest way to a point plus the
distance to its closest target point. `O(1)`.

In the example the mouse runs 7.071 to the corner (8, 6) and then 5
along the side to the corner (5, 10), which lies on the circle.

Pitfalls:

- a side that touches the circle from inside gives a single point that
  is not strictly outside the book, so chords of zero length are
  skipped;
- a corner may lie inside the disk, then it is a target point itself;
- the mouse may be on the line of a side, so the side tests allow a
  small tolerance;
- a part of the disk in plain sight is not always the closest: going
  around a corner to the other side of the book can be shorter, so
  every corner is tried even when the mouse sees the target.

The answers match a search over a dense sample of the target, with the
segments tested point by point, to the sample's precision on 210 random
cases. An independent accepted implementation agrees on 209 of them;
on the other one, test 07, it stops at the part of the disk in plain
sight, 1068.837, while the way around the corner (−2, 16) is 1060.690,
as the sample confirms.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1733_geometry.cpp](1733_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 460 KB |
| [1733_geometry.go](1733_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1120 KB |
| [1733_geometry.java](1733_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1892 KB |
| [1733_geometry.py](1733_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 1140 KB |
| [1733_geometry.rs](1733_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 280 KB |
