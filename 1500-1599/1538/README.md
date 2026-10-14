# 1538. Towers of Guard

[Timus 1538](https://acm.timus.ru/problem.aspx?space=1&num=1538) · difficulty 1271 · geometry

Original problem by Alexander Ipatov, from the Eighth Ural State University Open Personal Contest, March 3, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given N hills (5 ≤ N ≤ 5000) with integer coordinates up to 10⁸ in
absolute value, no three on a line, choose five that are the vertices of
a convex pentagon, or report that there are none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the coordinates of the hills, one hill per line.

## Output

`No`, or `Yes` and the numbers of five hills in counterclockwise order
around the pentagon. Any such pentagon is accepted.

## Examples

### Example 1

Input:

```
6
1 0
0 1
1 2
2 0
2 2
3 1
```

Output:

```
Yes
2 1 4 5 3
```

## Solution

By the Erdős–Szekeres theorem, any nine points in the plane with no
three on a line contain five in convex position (eight do not suffice).
So the first min(N, 9) hills are enough: try each of their at most
C(9, 5) = 126 five-element subsets, build its convex hull with Andrew's
monotone chain, and print the first subset whose hull has five
vertices. The chain lists the hull counterclockwise. The answer can be
`No` only when N ≤ 8. Cross products reach 4·10¹⁶, so they need 64 bits.

Pitfalls:

- eight hills may hold no convex pentagon (test 04), but a ninth always
  creates one (test 05);
- the hills must be listed counterclockwise, whatever their order in the
  input (test 06);
- coordinates of 10⁸ overflow 32-bit cross products (test 07);
- several answers exist, so the tests use a checker (all tests).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1538_geometry.cpp](1538_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 196 KB |
| [1538_geometry.go](1538_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1160 KB |
| [1538_geometry.java](1538_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 2812 KB |
| [1538_geometry.py](1538_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.093 s | 1176 KB |
| [1538_geometry.rs](1538_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.031 s | 472 KB |
