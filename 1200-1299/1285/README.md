# 1285. Thread in hyperspace

[Timus 1285](https://acm.timus.ru/problem.aspx?space=1&num=1285) · difficulty 1584 · geometry

Original problem by Alexander Mironenko and Alexey Lakhtin, from the Ural State University Personal Contest 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

In eight-dimensional space there are two points A and B and a ball of
positive integer radius R ≤ 3000 centred at C; all coordinates are
integers with absolute value at most 1000, and A and B lie strictly
outside the ball.
Find the length of the shortest path from A to B that never enters the
ball (it may run along its surface), with two digits after the point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

A, B and C, eight integers each, then R.

## Output

The shortest length.

## Examples

### Example 1

Input:

```
0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0
10 10 10 10 5 5 5 5
3
```

Output:

```
1.00
```

## Solution

If the segment AB does not enter the ball, the answer is |AB|. The
closest point of the line to C is at t = (C − A)·(B − A) / |AB|². When t
lies strictly between 0 and 1, the segment enters the ball exactly when

```text
|AC|² · |AB|² − ((C − A)·(B − A))² < R² · |AB|²
```

For t outside (0, 1), the closest point is an end, and the ends are
outside. All of this is exact in 64-bit integers.

When the segment does enter, the shortest path stays in the plane
through A, B and C, where the ball cuts a disc. It runs along a tangent
from A, around the circle, and along a tangent to B. With d = |CA| and
e = |CB| the tangents have lengths √(d² − R²) and √(e² − R²). The arc
spans the angle ACB minus arccos(R/d) and arccos(R/e), the angles
between each point and its tangent point seen from C. `O(1)`.

Pitfalls:

- a segment that only touches the ball is allowed and stays straight
  (test 03);
- A and B may coincide (test 04);
- C may lie on the segment itself, and then the plane is any plane
  through the line; the formula does not depend on it (test 02);
- the statement requires half-cent ties to be rounded up; the local
  tests compare with a tolerance of 0.01.

The answers were compared on 150 random cases with a shortest path
around a polygon of 20 000 sides drawn just outside the circle in that
plane.

## Language notes

- All languages run the same integer test and the same formula in
  double precision.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1285_geometry.cpp](1285_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 152 KB |
| [1285_geometry.go](1285_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1136 KB |
| [1285_geometry.java](1285_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1532 KB |
| [1285_geometry.py](1285_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 636 KB |
| [1285_geometry.rs](1285_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 260 KB |
