# 1317. Hail

[Timus 1317](https://acm.timus.ru/problem.aspx?space=1&num=1317) · difficulty 1064 · geometry

Original problem: idea by Pavel Atnashev, prepared by Pavel Atnashev and Alexey Lakhtin, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A parking lot is a convex polygon with 3 to 10 vertices, surrounded by
a fence of height h (1 ≤ h ≤ 100). A laser stands on the ground
strictly inside the lot and destroys a hailstone if the hailstone is
at most d away (h < d < 1000). Hailstones fall straight down.

The range is always enough for hailstones falling onto the lot itself,
and the laser also shoots hailstones falling outside it, as long as it
can see them over the fence and reach them. Given up to 100 points where
hailstones land, count how many are shot down in the air. All
coordinates are at most 1000 in absolute value.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line has n and h, then n lines with the vertices in order
around the polygon, then a line with d and the laser's coordinates,
then k and k lines with the landing points.

## Output

The number of hailstones shot down.

## Examples

### Example 1

Input:

```
4 10.00
1.00 0.00
0.00 1.00
-1.00 0.00
0.00 -1.00
50.00 0.00 0.00
5
0.00 0.00
1.00 1.00
2.00 2.00
3.00 3.00
4.00 4.00
```

Output:

```
3
```

## Solution

Take a hailstone landing at horizontal distance r from the laser,
outside the lot. The beam leaves the lot at some horizontal distance a,
where the ray from the laser towards the landing point crosses the
fence. A beam that hits the hailstone at height z has height z · a / r
over the fence, so it clears the fence only when z ≥ h · r / a. The
laser should fire as low as it can, and the hailstone is shot if that
lowest point is in range:

r² + (h · r / a)² ≤ d², that is r² · (a² + h²) ≤ d² · a².

To find a, the polygon is turned counter-clockwise (by the sign of its
area) and each side is written as an outward normal n with an offset c,
so that the lot is n · p ≤ c on every side. Along the ray L + t · u the
sides it moves towards (n · u > 0) are crossed at
t = (c − n · L) / (n · u), and since the lot is convex the ray leaves
it at the smallest of these. A hailstone with n · p ≤ c for every side
lands on the lot or on the fence and always counts. `O(n · k)`.

Pitfalls:

- hailstones on the fence count as over the lot (test 02);
- the vertices may come clockwise (test 05), so the orientation has to
  be found first;
- comparisons need a small relative tolerance: with h = 100, a square of
  half-width 1 and a hailstone at distance 2, d² must be at least 40004,
  so d = 200 just misses and d = 201 reaches (tests 06 and 07).

The answers were compared with a direct check that searches for the
lowest visible height by bisection and tests the beam against every
side of the fence, on 400 random lots.

## Language notes

- All five solutions follow the same steps; the side through which the
  ray leaves starts from an infinite distance and takes the minimum.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1317_geometry.cpp](1317_geometry.cpp) | G++ 13.2 x64 | geometry | O(n k) | AC | 0.001 s | 220 KB |
| [1317_geometry.go](1317_geometry.go) | Go 1.14 x64 | geometry | O(n k) | AC | 0.031 s | 1084 KB |
| [1317_geometry.java](1317_geometry.java) | Java 1.8 | geometry | O(n k) | AC | 0.093 s | 600 KB |
| [1317_geometry.py](1317_geometry.py) | Python 3.12 x64 | geometry | O(n k) | AC | 0.078 s | 628 KB |
| [1317_geometry.rs](1317_geometry.rs) | Rust 1.75 x64 | geometry | O(n k) | AC | 0.015 s | 228 KB |
