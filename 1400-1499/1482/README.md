# 1482. Triangle Game

[Timus 1482](https://acm.timus.ru/problem.aspx?space=1&num=1482) · difficulty 2944 · geometry

Original problem by Alexander Ipatov, from the Ural State University Championship, October 7, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A triangle is drawn on a map, and a triangular token lies elsewhere
(all coordinates are integers up to 2000 in absolute value). In one
move the token may be translated or rotated, but never turned over.
Can one move put the token's vertices exactly onto the drawn ones? Print
0 if not; 1 dx dy for a translation; otherwise 2 x0 y0 A for a rotation
about (x0, y0) by A degrees counterclockwise, 0 ≤ A < 360, with at
least ten digits after the point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The drawn triangle's vertices, then the token's, as x y pairs.

## Output

0, 1 dx dy or 2 x0 y0 A.

## Examples

### Example 1

Input:

```
0 0 10 0 0 -10
0 0 10 0 0 10
```

Output:

```
2 0.0000000000 0.0000000000 270.0000000000
```

## Solution

The vertices only have to coincide as sets, so try all six ways to
match the token's vertices with the drawn ones. A matching can be
realised by a move exactly when the three side lengths agree and both
triangles turn the same way, since a move cannot reflect. Both checks
use integer squared lengths and cross products, so they are exact.

If some working matching shifts all three vertices by the same vector,
that translation is the answer. Otherwise take a working matching. The
angle is the one between a side of the token and its image, from
atan2 of their cross and dot products, moved into [0, 360). The centre
is a vertex that stays in place, if there is one. If not, it lies on the
perpendicular bisector of each vertex and its image:
2(t − s)·c = |t|² − |s|². Two of these lines with different directions
meet in it, and Cramer's rule gives the centre as an exact fraction,
printed to ten digits. `O(1)`.

Pitfalls:

- the vertices may be listed in any order (tests 08, gen1);
- a mirror image has the same sides but cannot be reached (test 03);
- the token already in place is a translation by (0, 0) (test 02);
- a small turn has a distant centre, about 2·10⁴ away in test 05, so
  the centre is better computed exactly than from (I − R)⁻¹ in floating
  point.

## Language notes

- C++ and Rust print the exact fraction with integer arithmetic:
  the whole part, then the remainder times 10¹⁰ over the denominator,
  rounded. Go uses `big.Rat`, Java `BigDecimal`, Python `Fraction`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1482_geometry.cpp](1482_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 216 KB |
| [1482_geometry.go](1482_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1220 KB |
| [1482_geometry.java](1482_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 2172 KB |
| [1482_geometry.py](1482_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 1092 KB |
| [1482_geometry.rs](1482_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 276 KB |
