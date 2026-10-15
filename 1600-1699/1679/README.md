# 1679. Scrooge's Tower

[Timus 1679](https://acm.timus.ru/problem.aspx?space=1&num=1679) · difficulty 1009 · geometry

Original problem: folklore, from the Ural SU Contest at the Petrozavodsk Summer Training Camp, August 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A round island of radius R is centred at the origin. Tell whether some
square inscribed in its circle has both given points on its boundary.

## Input

T (1 ≤ T ≤ 1000), then T lines of integers R, x1, y1, x2, y2
(1 ≤ R ≤ 10000); both points lie in the disc.

## Output

YES or NO for each line.

## Examples

### Example 1

Input:

```
3
2 1 1 1 -1
2 1 1 0 0
1 1 0 -1 0
```

Output:

```
YES
NO
YES
```

## Solution

Each side of an inscribed square is a chord at distance s = R / √2 from
the centre, and the disc cuts exactly that side out of its line. So a
point of the disc lies on a given side iff it lies on that side's line.

Let u be the unit normal of the side through the first point P, so
u · P = s. The other sides have normals −u and u turned by ±90°, and
u · Q = s for those are the same as u · Q′ = s, where Q′ is the second
point Q turned by 0°, 180° or ±90°. So the answer is YES iff for one of
the four turns Q′ the points P and Q′ lie on a common line at distance
s from the centre:

- if Q′ = P, any line through P at distance s will do, which exists
  iff |P| ≥ s, that is 2|P|² ≥ R²;
- otherwise the line is the one through P and Q′, at distance
  |P × Q′| / |P − Q′|, so the test is 2 (P × Q′)² = R² |P − Q′|².

Everything is an exact integer check, below 10¹⁷. `O(T)`.

Pitfall: floating-point angles are fragile here. A point at distance
exactly s, the midpoint of a side (R = 12, (6, 6), say), gives an arc
cosine of 1 that rounding can push out of range; test 02 holds such
points.

The answers match a floating-point search over the orientations for
every pair of points with R ≤ 3 and on 21000 random cases with R ≤ 30.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1679_geometry.cpp](1679_geometry.cpp) | G++ 13.2 x64 | geometry | O(T) | AC | 0.015 s | 128 KB |
| [1679_geometry.go](1679_geometry.go) | Go 1.14 x64 | geometry | O(T) | AC | 0.031 s | 1196 KB |
| [1679_geometry.java](1679_geometry.java) | Java 1.8 | geometry | O(T) | AC | 0.109 s | 504 KB |
| [1679_geometry.py](1679_geometry.py) | Python 3.12 x64 | geometry | O(T) | AC | 0.062 s | 892 KB |
| [1679_geometry.rs](1679_geometry.rs) | Rust 1.75 x64 | geometry | O(T) | AC | 0.046 s | 268 KB |
