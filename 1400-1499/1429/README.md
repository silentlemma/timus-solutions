# 1429. Biscuits

[Timus 1429](https://acm.timus.ru/problem.aspx?space=1&num=1429) · difficulty 2591 · geometry

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Dough is rolled into a disk of radius 32 000 centred at the origin, and
N circular cuts (0 ≤ N ≤ 500) are made in it, each with an integer centre
(|X|, |Y| ≤ 10 000) and radius (1 ≤ R ≤ 10 000), so all of them lie
well inside the dough. Count the pieces the dough falls into; pieces
may have holes, and the leftover around all cuts is a piece too.
Distinct crossing or touching points of the cuts are at least 10⁻³
apart.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N lines X Y R.

## Output

The number of pieces.

## Examples

### Example 1

Input:

```
3
-1 0 2
1 0 2
0 0 3
```

Output:

```
6
```

## Solution

The cuts form a plane graph: crossing and touching points are vertices,
the arcs between them are edges. Euler's formula for a plane graph with
C connected parts says V − E + F = 1 + C, where F counts the outer face
as well, and here the outer face is the leftover dough, which is itself
a piece. So the answer is E − V + C + 1. A circle with no crossings is
taken as one vertex and one edge, which changes nothing in E − V but
still makes its own part.

Repeated cuts are one cut, so equal circles are merged first. For a pair
of circles the number of common points is decided exactly with integers
from d², (r₁ − r₂)² and (r₁ + r₂)². The points themselves are
p₁ + (m·(dx, dy) ± √K·(−dy, dx)) / (2d²) with m = d² + r₁² − r₂² and
K = 4d²r₁² − m², where K is computed exactly as an integer before the
floating-point coordinates are evaluated. Points from different pairs
are merged through a grid hash with cells of 10⁻³: estimates of one point
differ by far less than 10⁻⁴, and distinct points are at least 10⁻³ apart. Each
circle with common points has as many arcs as distinct points on it, and
a union–find over intersecting or tangent pairs gives C. `O(N²)` pairs,
up to about 250 000 points.

Pitfalls:

- the leftover dough counts, so a single cut gives 2 (test 03);
- equal cuts must be merged (tests 06, 09);
- several circles can meet at one point, which is still one vertex
  (tests 07, gen4);
- tangencies and nearly tangent circles need exact tests and careful
  rounding (tests 04, 05, 08).

## Language notes

- C++ and Rust keep one grid hash of all points, as described above. In
  Go, Java and Python that table of up to 250 000 points went over the
  64 MB limit, so they keep only the estimates on each circle and merge
  them circle by circle. A group of s estimates on a circle is a point
  on s + 1 circles, so it adds 1 / (s + 1) to the number of vertices,
  and every point adds 1 in all. Go and Python merge with a small grid
  hash per circle; Java sorts the angles of the estimates around the
  centre, where estimates of one point are adjacent in circular order,
  since distinct points differ by at least 10⁻³ / r in angle.
- Python runs under PyPy; with CPython, depending on the machine, the
  largest tests here can exceed the 1 s limit.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1429_geometry.cpp](1429_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2 log N) | AC | 0.265 s | 24972 KB |
| [1429_geometry.go](1429_geometry.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.359 s | 19352 KB |
| [1429_geometry.java](1429_geometry.java) | Java 1.8 | geometry | O(N^2 log N) | AC | 0.187 s | 9948 KB |
| [1429_geometry.py](1429_geometry.py) | PyPy 3.10 x64 | geometry | O(N^2) | AC | 0.750 s | 22356 KB |
| [1429_geometry.rs](1429_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2 log N) | AC | 0.265 s | 51048 KB |
