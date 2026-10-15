# 1703. Robotic Arm

[Timus 1703](https://acm.timus.ru/problem.aspx?space=1&num=1703) · difficulty 1229 · geometry

Original problem by Pavel Atnashev, from the Thirteenth Ural Championship in Sports Programming, April 4, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A robot's arm has an upper arm of length a, fixed at the shoulder (the
origin) and free to turn any way, and a forearm of length b. The
forearm bends at the elbow around an axis across both segments, and the
bend may not be acute. The claw at the end of the forearm closes around
a rail of unit diameter only when the rail's axis is parallel to the
elbow's axis. Given the rail's axis, find an elbow position and the
bend angle that let the claw close on the rail, or say that none
exists.

## Input

a and b, then two different points of the rail's axis. All numbers are
integers up to 100 in absolute value, a, b ≥ 4, and the axis does not
pass through the shoulder.

## Output

The elbow's coordinates and the bend angle in [π/2, π], or
"No solution.". Any valid position is accepted.

## Examples

### Example 1

Input:

```
8 6
-10 10 0
10 10 0
```

Output:

```
0 6.4 4.8 1.5707963267948966
```

### Example 2

Input:

```
5 10
-10 10 0
10 10 0
```

Output:

```
No solution.
```

## Solution

The elbow's axis is across both segments and parallel to the rail, so
the shoulder, the elbow and the claw all lie in the plane through the
shoulder across the rail. The claw holds the rail where the axis meets
that plane: the point h of the axis nearest to the shoulder. With
r = |h|, the shoulder, the elbow and h form a triangle with sides a, b
and r, and the bend is the angle opposite r. It is not acute exactly
when a² + b² ≤ r², and the triangle closes when r ≤ a + b.

Both tests are exact in integers. With a point p of the axis and its
direction d, r² = |p × d|² / |d|², so compare a² + b² and (a + b)²
times |d|² with |p × d|². When they hold, put the elbow in that plane:
x = (a² − b² + r²) / (2r) along h and √(a² − x²) across it, and the
bend is arccos((a² + b² − r²) / (2ab)). `O(1)`.

Pitfalls:

- a right angle (a² + b² = r², the first example) and a straight arm
  (r = a + b, test 04) are both allowed, which is why the comparison is
  exact;
- a rail too close to the shoulder makes the bend acute (tests 02 and
  08), even though the arm could reach it;
- the elbow may be mirrored across the line to h, and either side is
  accepted.

The checker verifies the segment lengths, the plane, and the reported
angle. The verdicts match an independent accepted implementation on 150
random cases, many of them at the limits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1703_geometry.cpp](1703_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 156 KB |
| [1703_geometry.go](1703_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1084 KB |
| [1703_geometry.java](1703_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1880 KB |
| [1703_geometry.py](1703_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 708 KB |
| [1703_geometry.rs](1703_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 292 KB |
