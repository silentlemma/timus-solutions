# 1477. Airplanes

[Timus 1477](https://acm.timus.ru/problem.aspx?space=1&num=1477) · difficulty 2918 · geometry

Original problem by Dmitry Ivankov, from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N airplanes (1 ≤ N ≤ 150) are points on a sphere centred at the
origin, given by integer direction vectors (X, Y, Z) with coordinates up
to 600 in absolute value; no two share a direction. From far away one
sees an open hemisphere. Find the largest number of airplanes visible
at once.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines X Y Z.

## Output

The largest number of visible airplanes.

## Examples

### Example 1

Input:

```
6
0 0 1
0 0 -1
0 1 0
0 -1 0
1 0 0
-1 0 0
```

Output:

```
3
```

## Solution

An open hemisphere with pole d shows the points p with d·p > 0. Tilt an
optimal d, keeping its visible points before the limit; unless all
directions are collinear, the limiting boundary plane can contain two
non-parallel airplanes. So it is enough to try every plane through the
origin and two non-parallel airplanes, with normal n = p × q normalized
by sign and gcd so that each plane is tried once. The airplanes off the
plane are on one side or the other.

The airplanes on the plane form a circle, and a slight tilt of the pole
toward a direction u in the plane shows those with u·p > 0, which is the
same problem one dimension lower. There the edge of the best open
half-circle can approach an airplane z: take the larger side of the
diameter through z, plus z itself, which a further slight turn adds.
So each plane gives max(above, below) + the best half
of its circle, and the answer is the largest of these, but at least 1.
`O(N³)` overall, since each non-parallel pair determines one plane.

Pitfalls:

- the hemisphere is open: airplanes on its boundary are not seen, so
  the six axis directions give 3, not 5 (test 01);
- if all airplanes lie on one line through the origin there is no
  plane to try, and the answer is 1 (tests 02, 03);
- many airplanes on one great circle need the step on the circle
  (tests 04, 06, gen3);
- the scalar products reach about 7.3·10¹¹, beyond 32 bits (gen1).

## Language notes

- Python runs under PyPy: CPython exceeds the 1 s limit on the judge's
  test 13, and PyPy takes 0.81 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1477_geometry.cpp](1477_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^3) | AC | 0.031 s | 472 KB |
| [1477_geometry.go](1477_geometry.go) | Go 1.14 x64 | geometry | O(N^3) | AC | 0.046 s | 3116 KB |
| [1477_geometry.java](1477_geometry.java) | Java 1.8 | geometry | O(N^3) | AC | 0.187 s | 7416 KB |
| [1477_geometry.py](1477_geometry.py) | PyPy 3.10 x64 | geometry | O(N^3) | AC | 0.812 s | 11780 KB |
| [1477_geometry.rs](1477_geometry.rs) | Rust 1.75 x64 | geometry | O(N^3) | AC | 0.062 s | 1224 KB |
