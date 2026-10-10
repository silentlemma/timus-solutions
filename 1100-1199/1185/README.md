# 1185. The shortest wall that keeps a set distance from a polygonal castle

[Timus 1185](https://acm.timus.ru/problem.aspx?space=1&num=1185) · difficulty 301 · geometry

Original problem by Sergey Volchenkov and Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2001–2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A castle is a simple polygon with `3 ≤ N ≤ 1000` integer vertices given
clockwise. Find the length of the shortest closed wall around it that
never comes closer than `L` feet to the castle, rounded to a whole number
of feet.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `L`, then the vertices.

## Output

The length in feet, accurate to 8 inches.

## Examples

### Example 1

Input:

```
9 100
200 400
300 400
300 300
400 300
400 400
500 400
500 200
350 200
200 200
```

Output:

```
1628
```

## Solution

The wall must enclose the castle, so it also encloses its convex hull,
and the best wall is the set of points at distance exactly `L` from the
hull. Along each hull side it runs parallel at distance `L`, adding the
side length. At each hull vertex it turns along a circular arc of radius
`L` by the exterior angle there, and the exterior angles of a convex
polygon add up to a full turn. So the length is the hull perimeter plus
`2πL`.

The hull comes from Andrew's monotone chain: sort the points, build the
lower and the upper chains, and drop points that do not turn left,
including collinear ones. Rounding to the nearest foot leaves an error of
at most 6 inches. `O(N log N)`.

Pitfalls:

- the castle need not be convex, so its own perimeter is too long; dents
  are bridged by hull sides, as in the example;
- vertices in the middle of a straight side must not break the hull,
  hence dropping collinear points;
- the answer is rounded, not truncated.

The answers were compared with a separately written solution on 200
random castles and on every test.

## Language notes

- All languages build the hull the same way on 64-bit integer
  coordinates and add the side lengths in floating point.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1185_geometry.cpp](1185_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 236 KB |
| [1185_geometry.go](1185_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1204 KB |
| [1185_geometry.java](1185_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 3144 KB |
| [1185_geometry.py](1185_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 752 KB |
| [1185_geometry.rs](1185_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 264 KB |
