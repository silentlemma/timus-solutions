# 1405. Goat in the Garden 5

[Timus 1405](https://acm.timus.ru/problem.aspx?space=1&num=1405) · difficulty 709 · geometry

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

## Optimized solutions

Compute each tree's rope limit from squared distances, then sort the limits in descending order. Skip pairs whose two limits cannot beat the best area. If both full ropes fit, use them. Otherwise check the two endpoints on the line where the ropes touch.

**Timus submissions for the optimized versions**

Go sorts the trees by horizontal coordinate and uses that distance to stop each nearest-neighbor scan early.

`1405_geometry_optimized.cpp` (G++ 13.2 x64) №11317478 · `1405_geometry_optimized.go` (Go 1.14 x64) №11322346 · `1405_geometry_optimized.java` (Java 1.8) №11317519 · `1405_geometry_optimized.py` (Python 3.12 x64) №11317508 · `1405_geometry_optimized.rs` (Rust 1.75 x64) №11323258.

Rust sorts trees by x to stop nearest-neighbor scans early and checks the largest radius bounds first. Rust 1.75 x64, submission 11323258. Time 0.031 → 0.015 s, memory 308 → 76 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322120 · Go 1.14 x64 №11322121 · Java 1.8 №11322122 · Python 3.12 x64 №11322132 · Rust 1.75 x64 №11322133.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1405_geometry.cpp](1405_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2) | AC | 0.046 s | 224 KB | 11322120 |
| [1405_geometry.go](1405_geometry.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.062 s | 1136 KB | 11322121 |
| [1405_geometry.java](1405_geometry.java) | Java 1.8 | geometry | O(N^2) | AC | 0.14 s | 5548 KB | 11322122 |
| [1405_geometry.py](1405_geometry.py) | Python 3.12 x64 | geometry | O(N^2) | AC | 0.625 s | 1236 KB | 11322132 |
| [1405_geometry.rs](1405_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2) | AC | 0.031 s | 308 KB | 11322133 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1405_geometry_optimized.cpp](1405_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(N^2) | AC | 0.015 s | 232 KB | 11317478 |
| [1405_geometry_optimized.go](1405_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(N^2) | AC | 0.031 s | 1016 KB | 11322346 |
| [1405_geometry_optimized.rs](1405_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(N^2) | AC | 0.015 s | 76 KB | 11323258 |
| [1405_geometry_optimized.py](1405_geometry_optimized.py) | Python 3.12 x64 | geometry | O(N^2) | AC | 0.125 s | 1064 KB | 11317508 |
| [1405_geometry_optimized.java](1405_geometry_optimized.java) \* | Java 1.8 | geometry | O(N^2) | AC | 0.171 s | 3204 KB | 11317519 |

\* The marked solutions can improve their target rankings. Go took 0.031 s versus 0.062 s for the simple version, and used 1016 KB versus 1136 KB. The saved ranking has no comparable Go submissions from other authors. Rust took 0.031 s versus 0.031 s for the simple version and used 324 KB versus 308 KB. The saved ranking has no comparable Rust submissions from other authors. Java used 3204 KB versus 5548 KB for the simple version, and took 0.171 s versus 0.14 s.
