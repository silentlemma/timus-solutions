# 1451. Beerhouse Tale

[Timus 1451](https://acm.timus.ru/problem.aspx?space=1&num=1451) · difficulty 995 · geometry

Original problem by Ilya Grebnov, Dmitry Kovalioff and Nikita Rybak, from Timus Top Coders: Second Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three programmers live at three different points with real coordinates
from −1000 to 1000, given with at most seven decimals. Find a place for
a beer stall with the smallest sum of distances to the three houses; the
sum must match the minimum to six decimals, and any such place is
accepted.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

X1, Y1, X2, Y2, X3, Y3 on one line.

## Output

The coordinates of the stall.

## Examples

### Example 1

Input:

```
1.1 3.1 5.1 1.1 4.1 5.1
```

Output:

```
3.37423161 3.38281356
```

## Solution

This is the Fermat point of the triangle. If one corner of the triangle
is at least 120°, that house itself is the answer: moving away from it
cannot pay, since the other two houses pull at an angle of 120° or more
and their pulls add up to less than the unit cost of the step. Three
houses on one line fall into this case, with a corner of 180° at the
middle house.

Otherwise the best point sees every side at 120°. Its barycentric
coordinates are a / sin(A + 60°), b / sin(B + 60°), c / sin(C + 60°),
with a, b, c the sides opposite the corners A, B, C; all three weights
are positive because every corner is below 120°. The corners come from
atan2 of the cross and dot products, which stays accurate for very flat
triangles, and the point is the weighted average of the houses. `O(1)`.

Pitfalls:

- three houses on one line (tests 02, 12, 13);
- corners just below and just above 120° (tests 05, 10, 11);
- a needle-thin triangle, where cosines lose precision (tests 08, 13).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1451_geometry.cpp](1451_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 156 KB |
| [1451_geometry.go](1451_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1112 KB |
| [1451_geometry.java](1451_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 2012 KB |
| [1451_geometry.py](1451_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 672 KB |
| [1451_geometry.rs](1451_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.062 s | 268 KB |
