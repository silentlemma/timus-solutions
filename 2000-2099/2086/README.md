# 2086. A triangle placed through a point on one of its sides

[Timus 2086](https://acm.timus.ru/problem.aspx?space=1&num=2086) · difficulty 4671 · geometry, math

Original problem by Dmitry Ivankov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Points V (Vanya) and E (Eugene) are given. Denis's place D is at
distance X from V, an unknown hall F is at distance Y from V and at
distance Z from D, and E lies on the segment DF. The three lengths form
a proper triangle. Output all possible positions of D. The limits are
2 seconds and 256 MB.

## Input

X, Y, Z (1 to 10⁴, |X − Y| < Z < X + Y), then the integer coordinates
of V and of E (up to 10⁴ in absolute value), V ≠ E.

## Output

The number of positions, then the positions with an absolute or relative
error of at most 10⁻⁶, in any order.

## Checking

A checker compares the number of points and matches the points in any
order with the allowed error.

## Examples

### Example 1

Input:

```
3 3 3
0 0
2 2
```

Output:

```
4
2.968700210890 -0.432225702453
-0.432225702453 2.968700210890
2.354856947625 1.858668543938
1.858668543938 2.354856947625
```

### Example 2

Input:

```
1 1 1
0 0
100 500
```

Output:

```
0
```

### Example 3

Input:

```
28 46 20
28 10
5 -6
```

Output:

```
2
5.007867947356 -5.980045796986
5.021444895601 -5.999562660088
```

## Solution

The triangle VDF is fixed up to motion by its sides. A point at fraction
t of the way from D to F is, by Stewart's theorem, at squared distance
(1 − t) X² + t Y² − t (1 − t) Z² from V. E must be such a point with
t ∈ [0, 1], and its squared distance d² from V is an integer, so t
solves Z² t² + (Y² − X² − Z²) t + (X² − d²) = 0 with integer
coefficients. The discriminant and the comparisons of the roots with 0
and 1 are done exactly with integer arithmetic (comparing ±√disc with an
integer by squaring), so the number of answers never depends on
rounding. A double root counts once.

For each valid t a model triangle is built with V at the origin, D on
the x axis and F above it; the point P at fraction t has |P| = d. A
rotation that takes P to E − V places the model, and so does a new
rotation after reflecting the model in the x axis, so each t gives two
mirror positions of D. They coincide only when t = 0, that is when E is
D itself (then d = X); at t = 1, E is the hall and both mirror images
count. Everything is O(1).

In the first example both roots t lie inside [0, 1], giving four
positions symmetric with respect to the line through V and E.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2086_geometry_math.cpp](2086_geometry_math.cpp) | G++ 13.2 x64 | geometry, math | O(1) | AC | 0.031 s | 216 KB |
| [2086_geometry_math.go](2086_geometry_math.go) | Go 1.14 x64 | geometry, math | O(1) | AC | 0.031 s | 1112 KB |
| [2086_geometry_math.java](2086_geometry_math.java) | Java 1.8 | geometry, math | O(1) | AC | 0.140 s | 1880 KB |
| [2086_geometry_math.py](2086_geometry_math.py) | Python 3.12 x64 | geometry, math | O(1) | AC | 0.109 s | 768 KB |
| [2086_geometry_math.rs](2086_geometry_math.rs) | Rust 1.75 x64 | geometry, math | O(1) | AC | 0.062 s | 280 KB |
