# 1659. Regular Triangles

[Timus 1659](https://acm.timus.ru/problem.aspx?space=1&num=1659) · difficulty 650 · geometry

Original problem by Vladimir Yakovlev, from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A regular triangle is given. Mark six more points, three strictly inside
it and three strictly outside, so that the nine points are the vertices
of at least nine regular triangles, the given one included. Any two of
the nine points must be at least 1 apart, every new point must be at
least 0.1 from the sides of the triangle, and sides count as equal when
they differ by at most 10⁻⁶.

## Input

Three lines with the vertices of the triangle. The coordinates are at
most 100 in absolute value, and the sides are at least 10 long.

## Output

The three inner points, then the three outer points, one per line.

## Examples

### Example 1

Input:

```
0 30
-25.9807621135 -15
25.9807621135 -15
```

Output:

```
0.0000000000 15.0000000000
-12.9903810567 -7.5000000000
12.9903810567 -7.5000000000
0.0000000000 -45.0000000000
38.9711431703 22.5000000000
-38.9711431703 22.5000000000
```

Any valid answer is accepted. The answer printed in the statement for
this example is deliberately wrong (its points form only three regular
triangles), so the output above is the one this solution prints.

## Solution

Put the centre g of the triangle at the origin and let a, b and c be the
vectors to the vertices A, B and C; they have equal length, lie 120°
apart, and a + b + c = 0. Take the inner points at t·a, t·b, t·c and the
outer points at −s·a, −s·b, −s·c. Each set is a regular triangle on its
own, which together with the given one makes three.

The other six come from triples like A, the inner point t·b, and the
outer point −s·c. Turning the plane by 60° in the right direction sends
a to −c and b to −a, so it sends the side from t·b to A, which is
a − t·b, to −c + t·a. That vector equals −s·c − t·b exactly when
s = 1 + t (use a + b = −c), so with this choice the triple is regular.
Every vertex pairs with both of its neighbours this way, which gives six
triangles and nine in all.

The solution takes t = 1/2 and s = 3/2. With sides of at least 10 every
distance stays comfortably above the limits: the inner triangle has side
at least 5, an inner point is a quarter of the circumradius (at least
1.44) from the nearest side, and an outer point is a whole circumradius
beyond the nearest side. `O(1)`.

Pitfalls:

- the vertices may come in either order, clockwise or not; the
  construction does not care;
- the outer points of a large triangle land well outside the box of the
  input, which the statement allows;
- the answer is checked rather than compared, by a checker that counts
  the regular triangles and tests every distance.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1659_geometry.cpp](1659_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 152 KB |
| [1659_geometry.go](1659_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1124 KB |
| [1659_geometry.java](1659_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 1084 KB |
| [1659_geometry.py](1659_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.062 s | 480 KB |
| [1659_geometry.rs](1659_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 268 KB |
