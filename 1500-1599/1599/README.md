# 1599. Winding Number

[Timus 1599](https://acm.timus.ru/problem.aspx?space=1&num=1599) · difficulty 1843 · geometry

Original problem by Vladimir Yakovlev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A closed railway runs through n joints (3 ≤ n ≤ 5000) along straight
tracks, which may cross and overlap. For each of m standing points
(m ≤ 5000), print `EDGE` if the point lies on a track, and otherwise how
many full turns counterclockwise one makes following the train once
around: its winding number. Coordinates are integers up to 10⁹ in
absolute value.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n and the joints, then m and the standing points.

## Output

`EDGE` or the number of turns for each point.

## Examples

### Example 1

Input:

```
8
-2 -2
-5 1
-2 4
1 3
-2 0
-3 1
-2 2
1 1
3
-2 1
0 0
1 2
```

Output:

```
-2
EDGE
0
```

## Solution

Look along the ray from the point to the right. Each time the train
crosses it going up, it passes the point counterclockwise; each time
going down, clockwise. So the winding number is the number of tracks
that cross the ray upwards minus those that cross it downwards. A track
from a to b crosses upwards when a.y ≤ p.y < b.y and the point lies to
its left, that is cross(b − a, p − a) > 0, and downwards when
b.y ≤ p.y < a.y and the point lies to its right. Counting the lower end
of each track but not the upper one makes a ray through a joint count
the joint exactly once, and horizontal tracks never count.

A point is on a track when the cross product is 0 and the point lies in
the track's bounding box. Every track is checked for every point:
`O(n·m)`, 2.5·10⁷ steps with integers only.

The results were checked against summing the turning angles with atan2
on small routes, including routes through the points' rows and routes
that go there and back.

Pitfalls:

- the cross product reaches 2·(2·10⁹)² = 8·10¹⁸, still below 2⁶³, so
  64-bit integers suffice, but there is no room for anything larger;
- a ray through a joint or along a horizontal track must not count
  twice or not at all, which the half-open test a.y ≤ p.y < b.y handles;
- the route may run back over itself, and tracks of zero length are
  possible: they only matter for `EDGE`.

## Language notes

- Python runs under PyPy: 5000 points against 5000 tracks take about
  5.5 s with CPython and about 0.4 s with PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1599_geometry.cpp](1599_geometry.cpp) | G++ 13.2 x64 | geometry | O(n·m) | AC | 0.250 s | 228 KB |
| [1599_geometry.go](1599_geometry.go) | Go 1.14 x64 | geometry | O(n·m) | AC | 0.515 s | 1572 KB |
| [1599_geometry.java](1599_geometry.java) | Java 1.8 | geometry | O(n·m) | AC | 0.781 s | 936 KB |
| [1599_geometry.py](1599_geometry.py) | PyPy 3.10 x64 | geometry | O(n·m) | AC | 0.906 s | 5464 KB |
| [1599_geometry.rs](1599_geometry.rs) | Rust 1.75 x64 | geometry | O(n·m) | AC | 0.328 s | 612 KB |
