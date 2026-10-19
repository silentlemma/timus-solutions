# 2076. A circle on a symmetry axis of a quadratic curve

[Timus 2076](https://acm.timus.ru/problem.aspx?space=1&num=2076) · difficulty 6156 · geometry, math

Original problem by Mikhail Rubinchik.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A curve is the set of points (a t² + b t + c, d t² + e t + f) for all
real t. A point P is projected onto one of the symmetry axes of the
curve, giving a point Q. Does the closed disk with centre Q and radius R
meet the curve? Answer `YES` if it does for every axis, `NO` if it does
for none, and `MAYBE` if it depends on the axis. The curve is guaranteed
to have at least one axis. The limits are 2 seconds and 256 MB.

## Input

T ≤ 7000 tests, each three lines `a b c`, `d e f`, `Px Py R` of
integers with absolute values up to 10²⁰, R ≥ 1.

## Output

`YES`, `NO` or `MAYBE` for each test.

## Examples

### Example 1

Input:

```
1
0 1 0
1 0 0
2 1 1
```

Output:

```
YES
```

## Solution

Write the curve as C + B t + A t² with A = (a, d), B = (b, e),
C = (c, f), and let W = P − C. The curve is a point, a line, a ray or a
parabola.

- A = B = 0: a single point C. Every line through C is an axis, and the
  foot Q runs over the circle with diameter CP, from C itself (distance
  0) to P (distance |CP|). So the answer is `YES` if |CP| ≤ R and
  `MAYBE` otherwise.
- A = 0, B ≠ 0: a line. The line itself is an axis, with Q on it, which
  gives `YES`. Every perpendicular line is an axis too, and Q is then at
  the distance of P from the line, |W × B| / |B|. So again `YES` or
  `MAYBE`.
- A ≠ 0: the only axis is the line through the vertex with direction A
  (for a parabola, and also for a ray, when A × B = 0). With
  t₀ = −(A·B) / (2|A|²) at the vertex, the coordinate of Q along the axis
  measured from the vertex works out to N / (4|A|³), where
  N = 4|A|² (W·A) + (A·B)². Across the axis a parabola opens like
  s = κw² with κ = |A|³ / K, K = (A × B)².

For a point Q = (s, 0) on the axis the squared distance to the curve is
the minimum over u = w² ≥ 0 of (κu − s)² + u. Its derivative vanishes at
u = s/κ − 1/(2κ²). If that is not positive (s ≤ 1/(2κ), that is
N ≤ 2K), the nearest point is the vertex at distance |s|, and the test
is N² ≤ 16 R² |A|⁶. Otherwise the squared distance is
s/κ − 1/(4κ²) = K (N − K) / (4|A|⁶), and the test is
K (N − K) ≤ 4 R² |A|⁶. For a ray K = 0, and the formulas still say what
they should: inside the ray the distance is 0, behind its end it is |s|.
The answer is `YES` or `NO`, since there is one axis.

Everything is compared exactly. Inputs reach 10²⁰, so the products reach
about 10¹⁶³: Python, Go and Java use their big integers, while the C++
and Rust solutions carry a small signed big integer of their own with
addition, subtraction, multiplication and comparison on 32-bit limbs.
The work is O(1) big-number operations per test.

In the example the curve is the parabola y = x², the axis is x = 0, and
Q = (0, 1) lies on the parabola's inner side at distance √3/2 < 1 from
it, so the answer is `YES`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2076_geometry_math.cpp](2076_geometry_math.cpp) | G++ 13.2 x64 | geometry, math | O(T) | AC | 0.312 s | 444 KB |
| [2076_geometry_math.go](2076_geometry_math.go) | Go 1.14 x64 | geometry, math | O(T) | AC | 0.093 s | 6760 KB |
| [2076_geometry_math.java](2076_geometry_math.java) | Java 1.8 | geometry, math | O(T) | AC | 0.203 s | 17400 KB |
| [2076_geometry_math.py](2076_geometry_math.py) | Python 3.12 x64 | geometry, math | O(T) | AC | 0.109 s | 6764 KB |
| [2076_geometry_math.rs](2076_geometry_math.rs) | Rust 1.75 x64 | geometry, math | O(T) | AC | 0.281 s | 2144 KB |
