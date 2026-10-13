# 1405. Goat in the Garden 5

[Timus 1405](https://acm.timus.ru/problem.aspx?space=1&num=1405) · difficulty 715 · geometry

Original problem by Vladimir Yakovlev, from the Twelfth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 15, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A garden has 2 ≤ N ≤ 1000 trees, given to the centimetre. Two goats are
tied to two different trees. A goat must not reach any other tree, the
two goats must not reach each other, and a rope is at least 1 and at
most 50 metres long. Print the largest total area the goats can reach,
to 1 cm². A valid tying is promised to exist.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the coordinates of the trees.

## Output

The largest area in m² with four digits after the point.

## Examples

### Example 1

Input:

```
8
1 1
-2 0
5 3
-2 3
8 3.10
-2 -1
-2 2
8 4.10
```

Output:

```
36.8060
```

## Solution

At tree i the rope may not reach the nearest other tree, so with the
50-metre cap it is at most topᵢ = min(50, distance to the nearest other
tree). For goats at trees i and j at distance d the ropes a and b need

1 ≤ a ≤ topᵢ, 1 ≤ b ≤ topⱼ, a + b ≤ d,

and the area is π(a² + b²). That is a convex function on a polygon, so
it is largest at a corner: a box corner, or a point where the line
a + b = d meets a side of the box. Try those seven points, keep the ones
inside the region, and take the best over all pairs of trees. `O(N²)`.
The Python solution goes through the trees by their top and stops a row
as soon as top² of both trees together cannot beat the best.

Pitfalls:

- the limits of 1 and 50 metres are easy to miss: two trees 141 m apart
  give 5000π, not the square of the distance (test 02);
- a tree with a neighbour closer than 1 m cannot take a goat (tests 03
  and 06);
- the touching cases are allowed: a rope of exactly 1 m, or two ropes
  that add up to exactly the distance (test 05 and generated test 4);
- C++ has no M_PI on the judge, so π is acos(-1).

The corner search was compared with a fine grid over the region on 3 000
random cases, and the forum's examples give the expected answers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1405_geometry.cpp](1405_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2) | AC | 0.046 s | 240 KB |
| [1405_geometry.go](1405_geometry.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.078 s | 1152 KB |
| [1405_geometry.java](1405_geometry.java) | Java 1.8 | geometry | O(N^2) | AC | 0.140 s | 5560 KB |
| [1405_geometry.py](1405_geometry.py) | Python 3.12 x64 | geometry | O(N^2) | AC | 0.640 s | 1248 KB |
| [1405_geometry.rs](1405_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2) | AC | 0.046 s | 304 KB |
