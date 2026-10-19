# 2101. Inscribed rectangles through a point inside a triangle

[Timus 2101](https://acm.timus.ru/problem.aspx?space=1&num=2101) · difficulty 1666 · geometry

Original problem by Alexey Danilyuk, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A triangle and a point strictly inside it are given. A rectangle is
inscribed in the triangle when all its vertices lie on the sides. Among
the inscribed rectangles that have the point on their border, find the
largest area and count how many different such rectangles there are.
The limits are 1 second and 64 MB.

## Input

The three vertices and the point, integer coordinates up to 10⁴ in
absolute value; the vertices are not collinear.

## Output

The largest area with an absolute or relative error of at most 10⁻⁶,
then the number of rectangles.

## Examples

### Example 1

Input:

```
0 0
10 0
0 20
4 6
```

Output:

```
48.0000000000
4
```

### Example 2

Input:

```
-3 0
2 -1
5 7
0 1
```

Output:

```
9.0697674419
2
```

## Solution

An inscribed rectangle has one side on a side of the triangle, its base,
and its two upper vertices on the other two sides. This is possible only
when the altitude foot lies on the base, including its endpoints, so a
side whose adjacent angle is obtuse has no rectangles. For a base of length b and
height H, the rectangle of height h has width b (1 − h/H). In a right
triangle the two legs describe the same rectangles, those with a corner
at the right angle, so that family is counted once.

For each usable base the point can lie on the top side of the rectangle,
which fixes h as the distance from the point to the base, or on the
left or right side, which fixes the position of that side along the
base and thus h. The top case always gives one rectangle; the side case
gives one more unless the point lies on the altitude itself, where the
side would shrink the rectangle to nothing. The point is strictly
inside, so these rectangles are all different. The areas are rational
with integer data: the dot and cross products used in place of distances
and projection lengths are integers, so each area is a fraction computed
exactly and rounded to 10 decimal places. Everything is O(1).

Pitfall (test 19): integer coordinates do not imply integer distances or
projection lengths. For (0, 0), (2, 1), (1, 2) and the point (1, 1), the
distance to the side (0, 0)–(2, 1) is 1/√5. Use integer dot and cross
products without rounding these geometric lengths.

In the first example the legs lie on the axes and the point is (4, 6):
with the corner at the origin, the rectangle whose right side passes
through the point is 4 wide and 12 high, area 48, the largest of the
four.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2101_geometry.cpp](2101_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 412 KB |
| [2101_geometry.go](2101_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1188 KB |
| [2101_geometry.java](2101_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 584 KB |
| [2101_geometry.py](2101_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 612 KB |
| [2101_geometry.rs](2101_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 244 KB |
