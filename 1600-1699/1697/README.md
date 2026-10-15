# 1697. Sniper Shot

[Timus 1697](https://acm.timus.ru/problem.aspx?space=1&num=1697) · difficulty 5442 · geometry

Original problem by Alex Samsonov, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, February 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sniper at S = (sx, sy, sz) watches a target riding along the ground
from A to B. Bullets fly in straight lines; they may touch a skyscraper
(an axis-parallel box standing on the ground) but not pass through it.
Find the first point of the way the sniper can hit, or report that
there is none.

## Input

S, then A and B on the ground, then n (0 ≤ n ≤ 100) buildings
lx ly rx ry h. All values are integers up to 100 in absolute value,
sz ≥ 0. Buildings share no points, S is outside every building, and the
segment AB touches none.

## Output

The coordinates of that point with an error of at most 10⁻⁷, or
Impossible.

## Examples

### Example 1

Input:

```
0 0 2
-4 4 4 4
2
-3 2 -1 3 10
1 -1 4 2 20
```

Output:

```
-1.3333333333 4.0000000000
```

### Example 2

Input:

```
0 0 2
4 1 4 -1
1
1 -1 3 1 10
```

Output:

```
Impossible
```

## Solution

Let P(t) = A + t(B − A). A point of the shot towards P(t) is
S + u(P(t) − S) = S + u(A − S) + v(B − A) with v = u·t, which is linear
in (u, v). So the inside of a building pulls back to an open convex
polygon in the (u, v) plane, cut out by two strips (for x and y) and by
the height range of u, where sz·(1 − u) must be below h. The times t it
blocks are the values v / u over that polygon, an open interval
(lᵢ, rᵢ). Two more lines, −1 ≤ t ≤ 2, keep the polygon bounded without
touching the times that matter.

All boundary lines have small integer coefficients. So the polygon's
corners are found exactly as the intersections of pairs of lines that
satisfy every constraint, and lᵢ and rᵢ are the extreme ratios v / u
over them. The polygon has an inside, and the building blocks
anything, exactly when it has three different corners: a polygon that
only touches is a segment or a point. The one exception is a plane of
shots that holds a wall, as when S, A and B all have x = lx: the
polygon has an inside, yet every shot only slides along the wall. Then
a strip line has both coefficients zero, and such a building blocks
nothing. A sniper on the ground (sz = 0) just loses the height
constraint.

The free times form a closed set, so its first point is 0 or the right
end rᵢ of some interval. Test those candidates in order against all
the open intervals and print the first free one. Every comparison is a
cross-multiplication of integers below 10¹⁰. `O(n²)`.

Pitfalls:

- touching a wall, an edge or a roof is allowed, so the intervals are
  open and a free time can sit exactly between two of them;
- a shot grazing along a roof or a wall must not count as blocked,
  which floating-point tests get wrong easily;
- all shots can lie in the plane of a wall (tests 10 and 11), and the
  inside of the polygon then does not mean a blocked shot;
- A = B leaves a single time, 0.

The answers match an independent accepted implementation on 330 random
cases, most with small coordinates where shots graze edges and corners,
and on 400 cases with all shots in the plane of walls.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1697_geometry.cpp](1697_geometry.cpp) | G++ 13.2 x64 | geometry | O(n²) | AC | 0.015 s | 216 KB |
| [1697_geometry.go](1697_geometry.go) | Go 1.14 x64 | geometry | O(n²) | AC | 0.031 s | 1204 KB |
| [1697_geometry.java](1697_geometry.java) | Java 1.8 | geometry | O(n²) | AC | 0.156 s | 3560 KB |
| [1697_geometry.py](1697_geometry.py) | Python 3.12 x64 | geometry | O(n²) | AC | 0.093 s | 944 KB |
| [1697_geometry.rs](1697_geometry.rs) | Rust 1.75 x64 | geometry | O(n²) | AC | 0.046 s | 272 KB |
