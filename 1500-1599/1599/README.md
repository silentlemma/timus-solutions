# 1599. Winding Number

[Timus 1599](https://acm.timus.ru/problem.aspx?space=1&num=1599) · difficulty 1732 · geometry

Original problem by Vladimir Yakovlev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A closed railway runs through n joints (3 ≤ n ≤ 5000) along straight
tracks, which may cross and overlap. For each of m standing points
(1 ≤ m ≤ 5000), print `EDGE` if the point lies on a track, and otherwise how
many full turns counterclockwise one makes following the train once
around: its winding number. Coordinates are integers up to 10⁹ in
absolute value.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line contains n, followed by n lines of joint coordinates x y
in traversal order. Tracks join successive joints and the last to the
first. Then comes m, followed by m lines of standing point coordinates x y.

## Output

For each point, on a separate line, print `EDGE` or the signed number
of turns, positive counterclockwise and negative clockwise.

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
of each track but not the upper one counts a crossing through a joint
once; at a tangency the contributions cancel or are both excluded.
Horizontal tracks never contribute to the winding sum.

A point is on a track when the cross product is 0 and the point lies in
the track's bounding box. For each point, scan the tracks and check
this before counting crossings; stop and output `EDGE` on a match.
Otherwise, output the sum after the scan. The worst-case time is
`O(n·m)`, at most 2.5·10⁷ track checks with integers only.

The results were checked against summing the turning angles with atan2
on small routes, including routes through the points' rows and routes
that go there and back.

Pitfalls:

- the cross product has magnitude at most (2·10⁹)² = 4·10¹⁸, below
  the signed 64-bit maximum 2⁶³ − 1; 32-bit integers do not suffice;
- at joints on the ray, count crossings once and give tangencies a
  net contribution of zero; the half-open y-tests handle this, while
  horizontal tracks only matter for `EDGE`;
- opposite traversals of the same track cancel in the winding sum,
  and zero-length tracks contribute zero; both still require the
  `EDGE` check.

## Language notes

- Python runs under PyPy, precomputes the edge tuples and uses
  arbitrary-precision integers. C++, Go, Java and Rust obtain the
  next endpoint by index and use signed 64-bit geometry arithmetic.
- Java reads numbers through `StreamTokenizer` as doubles, which
  represent all allowed integer coordinates exactly, then converts
  them to `long` before geometry calculations.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1599_geometry.cpp](1599_geometry.cpp) | G++ 13.2 x64 | geometry | O(n·m) | AC | 0.250 s | 228 KB |
| [1599_geometry.go](1599_geometry.go) | Go 1.14 x64 | geometry | O(n·m) | AC | 0.515 s | 1572 KB |
| [1599_geometry.java](1599_geometry.java) | Java 1.8 | geometry | O(n·m) | AC | 0.781 s | 936 KB |
| [1599_geometry.py](1599_geometry.py) | PyPy 3.10 x64 | geometry | O(n·m) | AC | 0.906 s | 5464 KB |
| [1599_geometry.rs](1599_geometry.rs) | Rust 1.75 x64 | geometry | O(n·m) | AC | 0.328 s | 612 KB |
