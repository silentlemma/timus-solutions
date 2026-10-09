# 1103. A circle through three pencils that splits the rest in half

[Timus 1103](https://acm.timus.ru/problem.aspx?space=1&num=1103) · difficulty 503 · geometry

Original problem by Katya Ovechkina, from the Tetrahedron Team Contest, May 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` pencils stand at integer points (`N` odd, `3 ≤ N ≤ 5000`, coordinates
at most `10^8` in absolute value). No three of them are on a line and no
four on a circle. Pick three pencils so that the circle through them has
exactly `(N − 3) / 2` of the other pencils inside and the same number
outside. If there is no such circle, print `No solution`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines `x y`.

## Output

The coordinates of the three pencils, one pencil per line.

## Checking

Any valid circle is accepted. The checker verifies that the three points
are distinct pencils and counts the pencils inside and outside the circle
with an exact integer determinant.

## Examples

### Example 1

Input:

```
7
0 0
1 0
2 -1
2 1
1 1
0 2
-3 -1
```

Output:

```
-3 -1
2 -1
1 1
```

## Solution

A solution always exists. Take `A`, the lowest pencil (the leftmost of
the lowest), and `B`, its neighbour on the convex hull, chosen so that
every other pencil lies on the left of the line `AB`. Every circle
through `A` and `B` then cuts that half-plane the same way: a pencil `P`
is inside the circle through `A`, `B` and `C` exactly when it sees the
segment `AB` under a larger angle than `C` does. All the angles `APB` are
below 180° and, since no four pencils are concyclic, all different. Sort
the other `N − 2` pencils by this angle and take the middle one as `C`:
`(N − 3) / 2` pencils see `AB` under a larger angle and lie inside, the
same number see it under a smaller one and lie outside. `O(N log N)`.

The angle is compared without floating point. Its cotangent is
`dot / cross`, where `dot = (A − P)·(B − P)` and `cross` is the oriented
area of `P`, `A`, `B`, positive for every `P`. A larger angle has a
smaller cotangent, so `P` comes before `Q` when
`dot_P · cross_Q > dot_Q · cross_P`.

Pitfalls:

- the coordinates reach `10^8`, so `dot` and `cross` reach about
  `8 · 10^16` and their products about `6 · 10^33`, well past 64 bits;
- comparing angles with `atan2` is risky: two distant pencils can see
  `AB` under angles that differ by less than the rounding error;
- `B` must be a hull neighbour of `A`; for an arbitrary second point the
  pencils on both sides of `AB` are not ordered by one angle.

The answers were checked with an exact in-circle determinant on every
test, including random sets of thousands of pencils over the full
coordinate range.

## Language notes

- C++ and Rust compare the products in 128-bit integers and pick the
  middle element with `nth_element` and `select_nth_unstable_by`.
- Go and Java have no 128-bit type in these versions and compare the
  products as big integers while sorting.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1103_geometry.cpp](1103_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 444 KB |
| [1103_geometry.go](1103_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 2628 KB |
| [1103_geometry.java](1103_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 7336 KB |
| [1103_geometry.py](1103_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.171 s | 1548 KB |
| [1103_geometry.rs](1103_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 1160 KB |
