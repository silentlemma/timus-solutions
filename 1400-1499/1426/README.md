# 1426. Rectangles

[Timus 1426](https://acm.timus.ru/problem.aspx?space=1&num=1426) · difficulty 4823 · geometry

Original problem by Nikita Rybak, Dmitry Kovalioff and Ilya Grebnov, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For each of N paintings (0 ≤ N ≤ 10 000) four points with integer
coordinates from −5000 to 5000 are given; some may coincide. Draw a
rectangle, turned any way, with no two vertices equal, inside the square
from −10 000 to 10 000, such that every one of the four points lies on
one of its sides. Print "+" and the vertices in order around the
rectangle with at least six digits after the point, or "-" if there is
no such rectangle; any rectangle will do.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines of eight numbers: the four points.

## Output

A line per painting.

## Examples

### Example 1

Input:

```
2
1 0 0 1 3 2 1 2
0 1 0 -1 1 0 -1 0
```

Output:

```
+ 0.000000 0.000000 0.000000 2.000000 3.1234567890 2.000000 3.1234567890 0.000000
+ 0.000000 -1.000000 1.000000 0.000000 0.000000 1.000000 -1.000000 0.000000
```

## Solution

Fix a direction for the sides. All four points must lie in the
rectangle, and a point can only be on a side that touches the set, so
it is enough to look at the bounding box in that direction: it works
exactly when every point is extreme in one of the two turned
coordinates. If all points share one coordinate the box is flat, and it
is given width 1 on one side, which keeps every point on a side.

As the direction turns, the set of good directions is closed, and each
end of it is a moment when two points tie in a turned coordinate, that
is, when the sides are parallel or perpendicular to the segment between
them. So it suffices to try the at most six directions from one point to
another (one direction also stands for its perpendicular). With the
direction (dx, dy) itself as the frame, the turned coordinates
x·dx + y·dy and y·dx − x·dy are integers and the test is exact; only the
vertices are computed in floating point. If all points coincide, any
small square with that corner works.

The box of points within ±5000 never leaves ±10 000: the points lie in
a disk of radius 5000·√2, and any square circumscribed about that disk has its
corners within 10 000 of the centre. `O(N)`.

Pitfalls:

- a point inside the triangle of the others can never be on a side
  (tests 03, 06);
- collinear or repeated points need a rectangle of positive width
  (tests 02, 04, 07);
- the box may reach the edge of the canvas exactly (test 05).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1426_geometry.cpp](1426_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.125 s | 1980 KB |
| [1426_geometry.go](1426_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.109 s | 5888 KB |
| [1426_geometry.java](1426_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.312 s | 10072 KB |
| [1426_geometry.py](1426_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.390 s | 11424 KB |
| [1426_geometry.rs](1426_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.046 s | 2276 KB |
