# 2139. Juice left in a rotating polygon with a hole in its side

[Timus 2139](https://acm.timus.ru/problem.aspx?space=1&num=2139) · difficulty 3641 · geometry, binary_search

Original problem by Vadim Barinov, from the Ural Team Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A convex polygon full of juice gets a hole at a point H of one side, so
everything above the horizontal line through H pours out. Then it is
slowly rotated about the origin by q given angles in turn. Print the
amount of juice left after the hole is made and after every rotation,
with absolute or relative error at most 10⁻⁴. The limits are 4 seconds
and 256 MB.

## Input

n, 3 ≤ n ≤ 10⁵, the vertices counterclockwise, the hole, then q,
0 ≤ q ≤ 10⁵, and the angles in degrees, −360 ≤ αᵢ ≤ 360; coordinates and angles have
exactly three decimals and coordinates are at most 10⁵ in absolute
value.

## Output

q + 1 areas.

## Examples

### Example 1

Input:

```
3
-2.000 1.000
1.000 -2.000
4.000 1.000
1.000 1.000
4
45.000
45.000
45.000
45.000
```

Output:

```
9.000000000
6.750000000
4.500000000
2.250000000
0.000000000
```

## Solution

Rotating about the origin moves the hole together with the polygon, so
only the total angle θ turned so far matters. The capacity c(θ) is the
area of the polygon below the horizontal line through H at that angle,
and the juice left is the smallest capacity seen during the slow
rotation.

As θ changes, that line turns about H, a point of the boundary. One of
its two rays from H leaves the polygon at once, so the region below
only gains area on one side or only loses it, and c(θ) is monotone
between two special angles: where the side of H is horizontal with the
polygon above it (c = 0, the hole at the bottom) and where it is
horizontal with the polygon below (c is the whole area). So on the
circle c rises from 0 to the full area and falls back. If the total
angle ever passes an angle where the hole is at the bottom, everything
pours out for good. Otherwise the turned angle stays inside one arc
between two such angles, where c rises and then falls, so the minimum
over any rotation is at its ends and the answer is
min(previous answer, c(θ)).

To compute c(θ), store the vertices starting next to the hole, with
exact integer coordinates in thousandths taken relative to H, and
prefix sums of the shoelace terms. The vertices on one side of the line
through H form one arc of this list, so a binary search over the signed
heights finds the edge the line leaves through, and the area below is a
prefix or suffix of the fan from H plus a fraction of one triangle.
Each rotation costs O(log n).

In the example the triangle starts with area 9; every turn by 45° lowers
the level relative to the polygon, and after the fourth turn the hole is
at the bottom and nothing is left.

## Language notes

To print the same digits in every language, the programs compute sine
and cosine with the same polynomial and the same order of operations
instead of the library functions.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2139_geometry_binary_search.cpp](2139_geometry_binary_search.cpp) | G++ 13.2 x64 | geometry, binary_search | O(n + q log n) | AC | 0.140 s | 2320 KB |
| [2139_geometry_binary_search.go](2139_geometry_binary_search.go) | Go 1.14 x64 | geometry, binary_search | O(n + q log n) | AC | 0.062 s | 13544 KB |
| [2139_geometry_binary_search.java](2139_geometry_binary_search.java) | Java 1.8 | geometry, binary_search | O(n + q log n) | AC | 0.312 s | 16468 KB |
| [2139_geometry_binary_search.py](2139_geometry_binary_search.py) | Python 3.12 x64 | geometry, binary_search | O(n + q log n) | AC | 1.734 s | 51704 KB |
| [2139_geometry_binary_search.rs](2139_geometry_binary_search.rs) | Rust 1.75 x64 | geometry, binary_search | O(n + q log n) | AC | 0.062 s | 12684 KB |
