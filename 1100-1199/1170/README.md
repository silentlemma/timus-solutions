# 1170. The fastest straight walk of length L through zones of different speed

[Timus 1170](https://acm.timus.ru/problem.aspx?space=1&num=1170) · difficulty 1479 · geometry

Original problem by Mugurel Ionut Andreica, from the Romanian Open Contest, December 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

From the origin, walk `L` metres in a straight line to a point with
positive coordinates. `N ≤ 500` axis-parallel rectangles in the first
quadrant have delay coefficients: crossing a piece of length `d` inside
one costs `d·c`, and outside them the desert costs `d·c0`. All numbers are
positive integers up to 32000, and `L` reaches past every rectangle. Find
the least total time and a point that achieves it.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines `x1 y1 x2 y2 c`, then `c0` and `L`.

## Output

The least time, then the end point, all with six decimals.

## Checking

Any end point is accepted if it is `L` away from the origin, has positive
coordinates and gives the least time; the checker recomputes the time
along its direction rectangle by rectangle.

## Examples

### Example 1

Input:

```
1
1 1 2 2 1
2 3
```

Output:

```
4.585786
2.121320 2.121320
```

## Solution

Walking at angle `t`, the line `x = a` is reached after `a / cos t` and
the line `y = b` after `b / sin t`. A rectangle is entered at the larger
of `x1 / cos t` and `y1 / sin t`, and left at the smaller of `x2 / cos t`
and `y2 / sin t`. So the time is `c0·L` plus `(c − c0)` times the chord of
each rectangle, and which side is used switches only at the directions of
the four corners.

Between two neighbouring corner directions the time therefore has the
form `c0·L + p / cos t + q / sin t` with fixed integers `p` and `q`. If
`p, q > 0`, it is above `c0·L` on the whole piece. Otherwise it is
monotone (when `p` and `q` have different signs) or concave (both
negative), so its smallest value is at an end of the piece. Directions
below the lowest corner miss every rectangle and cost exactly `c0·L`. So
the answer is the best of `c0·L` and the times at the corner directions.

Each rectangle adds four terms, each switched on and off at two corner
directions, so a sweep over the directions sorted by slope keeps `p` and
`q` up to date. Slopes are compared as fractions, so corners on the same
ray share one event. `O(N log N)`.

Pitfalls:

- the time is continuous in the direction, so evaluating a corner with the
  `p` and `q` of the piece just before it is exact;
- two corners on one ray must be merged exactly, or a tiny false piece
  between them could show a time that no direction has;
- the end point must have positive coordinates, so the empty direction is
  taken halfway below the lowest corner, not along the axis.

The answers were compared with a dense scan of 20,000 directions on 400
random sets of rectangles, including fast zones behind slow strips, and
with a separately written solution on every test.

## Language notes

- C++ and Java keep the events in an ordered map whose comparator
  compares slopes as fractions; Python, Go and Rust reduce each direction
  by the gcd and sort.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1170_geometry.cpp](1170_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 340 KB |
| [1170_geometry.go](1170_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.015 s | 1560 KB |
| [1170_geometry.java](1170_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.171 s | 3856 KB |
| [1170_geometry.py](1170_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 1592 KB |
| [1170_geometry.rs](1170_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.015 s | 540 KB |
