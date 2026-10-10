# 1168. Counting the places where a receiver hears every radio station

[Timus 1168](https://acm.timus.ru/problem.aspx?space=1&num=1168) · difficulty 727 · geometry

Original problem by Mugurel Ionut Andreica, from the Romanian Open Contest, December 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A map is an `M×N` grid (`M, N ≤ 50`) of integer altitudes from 0 to
32000. `K ≤ 1000` radio stations stand at the centres of distinct squares,
at the altitude of their square, each with a real broadcast radius `R`
up to 100000. A receiver may be put at the centre of any square without a
station, at the square's altitude or any whole number of metres higher.
Count the placements (square and altitude) at which the 3D distance to
every station is at most its radius.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`M`, `N` and `K`, then the `M` rows of altitudes, then `K` lines with the
row, column and radius of a station.

## Output

The number of placements.

## Examples

### Example 1

Input:

```
5 5 3
1 2 3 4 5
6 7 8 9 10
1 2 3 4 5
6 7 8 9 10
5 4 3 2 1
1 1 4.3
5 5 4.3
5 1 4.3
```

Output:

```
4
```

## Solution

Every coordinate apart from the radii is an integer, so the squared
distance from a placement to a station is an integer, and the condition
`distance² ≤ R²` only depends on `⌊R²⌋`. This turns the whole problem into
integer arithmetic; the one floating-point step is `⌊R² + ε⌋` per
station.

For a square at horizontal squared distance `d` from a station of height
`z`, the receiver at altitude `a` hears it exactly when
`(a − z)² ≤ ⌊R²⌋ − d`, that is, when `a` lies in
`[z − s, z + s]` with `s = ⌊√(⌊R²⌋ − d)⌋`, or never if `⌊R²⌋ < d`.
Intersect these intervals over all stations, starting from the square's
own altitude at the bottom, and add the number of whole altitudes left.
`O(M·N·K)`, at most 1.5 million interval steps.

Pitfalls:

- the receiver cannot go below its square, so the lower end starts at the
  square's altitude, not at 0;
- a distance exactly equal to the radius counts, which is why `⌊R²⌋` is
  taken with a small tolerance;
- squares with stations are not allowed even when every station reaches
  them.

The answers were compared on 150 small random maps with a direct count
over all altitudes using exact fractions for the radii, and on one of the
generated tests.

## Language notes

- All languages compute the integer square root from a floating-point one
  and correct it by a step if needed; Python uses `math.isqrt`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1168_geometry.cpp](1168_geometry.cpp) | G++ 13.2 x64 | geometry | O(M·N·K) | AC | 0.015 s | 256 KB |
| [1168_geometry.go](1168_geometry.go) | Go 1.14 x64 | geometry | O(M·N·K) | AC | 0.031 s | 1180 KB |
| [1168_geometry.java](1168_geometry.java) | Java 1.8 | geometry | O(M·N·K) | AC | 0.171 s | 1176 KB |
| [1168_geometry.py](1168_geometry.py) | Python 3.12 x64 | geometry | O(M·N·K) | AC | 0.765 s | 940 KB |
| [1168_geometry.rs](1168_geometry.rs) | Rust 1.75 x64 | geometry | O(M·N·K) | AC | 0.046 s | 288 KB |
