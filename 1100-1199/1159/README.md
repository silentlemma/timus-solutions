# 1159. The largest area a fence of given blocks can enclose

[Timus 1159](https://acm.timus.ru/problem.aspx?space=1&num=1159) · difficulty 755 · geometry

Original problem by Nick Durov, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` straight blocks, `3 ≤ N ≤ 100`, with integer lengths up to 100, must
all be used, end to end, as the sides of a closed fence. Find the largest
area the fence can enclose, with two digits after the point, or `0.00` if
no fence can be built.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the `N` lengths.

## Output

The largest area with two decimals.

## Examples

### Example 1

Input:

```
4
10
5
5
4
```

Output:

```
28.00
```

## Solution

A polygon with given sides exists exactly when the longest side is
shorter than the sum of the others. Among all polygons with these sides,
the one with the largest area is the one inscribed in a circle (a classic
result; the order of the sides does not change its area). So the task is
to find that circle.

A side of length `l` in a circle of radius `R` is seen from the centre
at the angle `2·asin(l / 2R)`. If the centre lies inside the polygon, the
angles of all sides add up to `2π`. If it lies outside, it is beyond the
longest side, and the angle of that side equals the sum of the angles of
all the others. At the smallest possible radius, half the longest side,
the angles add up to at least `2π` exactly when the centre is inside; in
either case the matching equation has one root in `R`, found by bisection
on doubles. The area is the sum of the triangles from the centre,
`R²·sin(angle)/2`, with the triangle of the longest side subtracted when
the centre is outside.

Pitfalls:

- a longest side equal to the sum of the others gives a flat fence, area
  `0.00`;
- with the centre outside, the longest side's triangle must be
  subtracted, not added;
- `asin` gets its argument clamped to 1 against rounding.

The answers were compared with Heron's formula on random triangles and
with Brahmagupta's formula on random quadrilaterals (300 inputs), and
equal blocks with the formula for a regular polygon.

## Language notes

- All languages run the same bisection.
- Java rounds the area through `BigDecimal` with ties to even, as `printf`
  does in C.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1159_geometry.cpp](1159_geometry.cpp) | G++ 13.2 x64 | geometry | O(N·STEPS) | AC | 0.015 s | 224 KB |
| [1159_geometry.go](1159_geometry.go) | Go 1.14 x64 | geometry | O(N·STEPS) | AC | 0.031 s | 1112 KB |
| [1159_geometry.java](1159_geometry.java) | Java 1.8 | geometry | O(N·STEPS) | AC | 0.171 s | 4220 KB |
| [1159_geometry.py](1159_geometry.py) | Python 3.12 x64 | geometry | O(N·STEPS) | AC | 0.078 s | 596 KB |
| [1159_geometry.rs](1159_geometry.rs) | Rust 1.75 x64 | geometry | O(N·STEPS) | AC | 0.015 s | 264 KB |
