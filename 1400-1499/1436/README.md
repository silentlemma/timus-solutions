# 1436. Billboard

[Timus 1436](https://acm.timus.ru/problem.aspx?space=1&num=1436) · difficulty 830 · geometry

Original problem by Alexey Lakhtin, from the Seventh Ural State University Open Personal Contest, February 25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The road is the x-axis and a billboard is the segment between two
different integer points with coordinates from −1000 to 1000. Find the
largest angle, in radians with 6 digits after the point, under which
the billboard can be seen from a point of the road.

Time limit: 1 second. Memory limit: 64 MB.

## Input

x1, y1, x2, y2, one per line.

## Output

The largest angle.

## Examples

### Example 1

Input:

```
100
200
300
400
```

Output:

```
0.785398
```

### Example 2

Input:

```
123
456
789
-10
```

Output:

```
3.141593
```

### Example 3

Input:

```
-800
1
800
1
```

Output:

```
3.139093
```

### Example 4

Input:

```
9
7
3
0
```

Output:

```
3.141593
```

## Solution

If the billboard crosses or touches the road, a viewer can stand on it
and the answer is π, as the examples show for a crossing and for an end
on the road. A forum note says that a vertical billboard standing on the
road gives π/2, and the solutions follow it.

Otherwise reflect both ends to the same side, y > 0. The points from
which AB is seen under a fixed angle lie on circles through A and B, and
the largest angle belongs to the smallest such circle that still reaches
the road, the one tangent to it. If AB meets the road's line at Q, the
point of tangency P satisfies QP² = QA·QB (the power of the point Q), so
P lies at distance √(QA·QB) from Q on one side or the other; both
candidates are tried. If AB is level with the road, P is under its
middle. The angle at P comes from atan2 of the cross and dot products.
`O(1)`.

Pitfalls:

- the best point may lie beyond both ends of the billboard (test 08);
- a billboard below the road is the same as its reflection (tests 09,
  14);
- a billboard lying on the road gives π (test 10).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1436_geometry.cpp](1436_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 220 KB |
| [1436_geometry.go](1436_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1084 KB |
| [1436_geometry.java](1436_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1828 KB |
| [1436_geometry.py](1436_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 572 KB |
| [1436_geometry.rs](1436_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 244 KB |
