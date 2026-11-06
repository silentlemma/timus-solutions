# 1588. Jamaica

[Timus 1588](https://acm.timus.ru/problem.aspx?space=1&num=1588) · difficulty 327 · geometry

Original problem by Andrey Demidov, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n distinct cities (1 ≤ n ≤ 300) at integer points with
coordinates from 0 to 10000. Every two cities are joined by a straight
road, and one road serves all the cities on its line. Find the total
length of the roads, rounded to a whole number of miles.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n, then the coordinates of each city.

## Output

The total length, rounded.

## Examples

### Example 1

Input:

```
4
0 0
0 100
100 0
50 50
```

Output:

```
412
```

## Solution

Each line through two or more cities carries one road, from its first
city to its last. Seen from city i, every other city lies in some
reduced direction (dx/g, dy/g) with g = gcd(dx, dy), g steps away. City
i is an end of the road in a direction exactly when no city lies in the
opposite direction, and then the road is g·|(dx/g, dy/g)| long for the
farthest city in that direction. Adding this over all cities finds every
road twice, once from each end, so the sum is halved. With the
directions kept in a hash map the expected work is `O(n²)`; C++ uses
an ordered map and Java sorts, giving `O(n² log n)`.

The results were checked against grouping the cities on the line of
every pair explicitly.

Pitfalls:

- a line with three or more cities is one road, not one per pair: the
  first example counts the diagonal through (50, 50) once;
- directions must be reduced by the gcd, or cities on one line in
  different steps look like different roads;
- the sum is halved before rounding.
- cities on several lines through one point also create roads between
  those lines; count these too (generator test `gen3`).

## Optimized solutions

Sort the cities lexicographically and count each road only from its first city. At a city, group both senses of a reduced direction under one key. If that group contains an earlier city, skip it. Otherwise the farthest city gives the road length. Go reuses a hash table for these groups, and Rust reuses a sortable vector. Both use compensated summation before rounding the total.

The accepted base implementations [1588_geometry.cpp](1588_geometry.cpp), [1588_geometry.java](1588_geometry.java), [1588_geometry.py](1588_geometry.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1588_geometry.cpp](1588_geometry.cpp) | G++ 13.2 x64 | geometry | O(n² log n) | AC | 0.031 s | 240 KB | 11287971 |
| [1588_geometry.go](1588_geometry.go) | Go 1.14 x64 | geometry | O(n² log n) | AC | 0.046 s | 6288 KB | 11287972 |
| [1588_geometry.java](1588_geometry.java) \* | Java 1.8 | geometry | O(n² log n) | AC | 0.171 s | 1344 KB | 11287979 |
| [1588_geometry.py](1588_geometry.py) \* | Python 3.12 x64 | geometry | O(n² log n) | AC | 0.187 s | 572 KB | 11287976 |
| [1588_geometry.rs](1588_geometry.rs) | Rust 1.75 x64 | geometry | O(n² log n) | AC | 0.031 s | 452 KB | 11287980 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1588_geometry_optimized.go](1588_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(n²) expected | AC | 0.046 s | 1020 KB | 11310418 |
| [1588_geometry_optimized.rs](1588_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n² log n) | AC | 0.015 s | 236 KB | 11310417 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
