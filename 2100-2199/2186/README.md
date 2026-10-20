# 2186. The smallest rotation that points enough rays at a circle

[Timus 2186](https://acm.timus.ru/problem.aspx?space=1&num=2186) · difficulty 1765 · geometry, sorting

Original problem by Artyom Kutuzov, from the Ural Team Programming Contest 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n rays leave the origin in distinct directions (xᵢ, yᵢ), and a circle
of radius r is centered at (a, b) away from the origin. The rays are
turned together counterclockwise by an angle α, and then k shots are
fired, each from a ray chosen uniformly and independently; a shot hits
if its ray meets the circle, the boundary included. For each of q
probabilities pᵢ, find the smallest α in [0, 360) that gives a hit with
probability at least pᵢ, or −1. Answers within 10⁻³ are accepted. The
limits are 2 seconds and 256 MB.

## Input

n, k and q, 1 ≤ n ≤ 10⁵, 1 ≤ k ≤ 10, 1 ≤ q ≤ 10⁵, then the n directions
with coordinates up to 10⁹, then a, b and r, then the pᵢ with at most
five decimal digits.

## Output

The angle in degrees for each query, or −1.

## Examples

### Example 1

Input:

```
6 2 5
5 -5
3 0
-3 -2
-3 -1
-3 0
-4 -1
4 2 2
0.3 0.5 0.75 0.8 0.9
```

Output:

```
0.0000000000
45.0000000000
165.9637565321
180.0000000000
-1
```

## Solution

If c rays meet the circle, the hit probability is
1 − ((n − c) / n)ᵏ, which grows with c, so each query asks for the
smallest rotation with at least some count c of hitting rays.

The circle is seen from the origin as an arc of directions from the
lower tangent to the upper one, of width 2 · asin(r / √(a² + b²)). As α
grows, rays enter this arc through the lower tangent. So the count only
rises at α = 0 or at the moment some ray reaches the lower tangent, and
then the hitting rays are those whose directions lie within the arc's
width after it. With the rays sorted by angle, a two-pointer window over
the doubled list gives that count for every ray, and the smallest α per
count, made monotone by a suffix minimum, answers all counts.

Directions exactly on a tangent decide whether a ray hits, so whenever
floating point is close to a tie the test is redone in integers: the
window edge compares the angle between two rays with the arc width
through dot and cross products, and an entry near α = 0
is set to zero unless the ray is strictly inside the arc, in which case
it is set just below a full turn.

The probabilities have five decimals, so each count c gets a level
⌊10⁵ · (1 − ((n − c) / n)ᵏ)⌋, computed in floating point and confirmed
with integers near a grid point, and a query p becomes a binary search
for the first level of at least 10⁵ p in C++, Go and Python; Java and
Rust precompute answers for every grid value.

In the example k = 2 and n = 6. The ray (3, 0) touches the circle at
α = 0, which already gives 1 − (5/6)² ≥ 0.3, while 0.9 would need five
of the six rays, which the arc never holds at once.

Sorting and the window take O(n log n), and the queries O(q log n),
or O(q) in Java and Rust after O(n + 10⁵) table preprocessing.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2186_geometry_sorting.cpp](2186_geometry_sorting.cpp) | G++ 13.2 x64 | geometry, sorting | O((n + q) log n) | AC | 0.328 s | 3380 KB |
| [2186_geometry_sorting.go](2186_geometry_sorting.go) | Go 1.14 x64 | geometry, sorting | O((n + q) log n) | AC | 0.453 s | 16064 KB |
| [2186_geometry_sorting.java](2186_geometry_sorting.java) | Java 1.8 | geometry, sorting | O(n log n + q + 10⁵) | AC | 0.515 s | 19788 KB |
| [2186_geometry_sorting.py](2186_geometry_sorting.py) | Python 3.12 x64 | geometry, sorting | O((n + q) log n) | AC | 1.015 s | 54488 KB |
| [2186_geometry_sorting.rs](2186_geometry_sorting.rs) | Rust 1.75 x64 | geometry, sorting | O(n log n + q + 10⁵) | AC | 0.109 s | 16212 KB |
