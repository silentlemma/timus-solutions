# 1627. Join

[Timus 1627](https://acm.timus.ru/problem.aspx?space=1&num=1627) · difficulty 1093 · math

Original problem from the SPbSU ITMO Contest at the Petrozavodsk Training Camp, Winter 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A house is an n × m grid of rooms (1 ≤ n, m ≤ 9), each a bedroom `.` or
a pantry `*`, with at least one bedroom. Doors may join bedrooms that
share a wall. Count the ways to place doors so that between any two
bedrooms there is exactly one path, modulo 10⁹.

Time limit: 4 seconds. Memory limit: 64 MB.

## Input

n and m, then the n rows of the map.

## Output

The number of ways modulo 10⁹.

## Examples

### Example 1

Input:

```
2 2
..
..
```

Output:

```
4
```

### Example 2

Input:

```
2 2
*.
.*
```

Output:

```
0
```

## Solution

Exactly one path between any two bedrooms means the doors form a
spanning tree of the graph of bedrooms. By Kirchhoff's matrix-tree
theorem the number of spanning trees is the determinant of the Laplacian
(degrees on the diagonal, −1 for each pair of neighbours) with one row
and column removed; for a disconnected graph it is 0. With up to 81
bedrooms that is an 80 × 80 determinant.

The count is wanted modulo 10⁹, which is not prime, so ordinary
elimination modulo 10⁹ cannot divide by a pivot. Euclid's algorithm on
rows can: to clear an entry below the pivot, subtract the right multiple
of that row from the pivot row and swap the two, as in a gcd, until the
entry is 0. Only subtraction, multiplication and swaps are used, so all
of it holds modulo 10⁹; each swap flips the sign. `O(v³ log M)` for v
bedrooms. Python uses Bareiss elimination instead: `O(v³)` big-integer
operations with exact division, then the remainder.

Pitfalls:

- bedrooms touching only at a corner are not connected: 0 (the second
  example);
- a single bedroom has one way, the empty set of doors (test 03).

The answers match an independent accepted implementation on 160 random
houses.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1627_math.cpp](1627_math.cpp) | G++ 13.2 x64 | math | O(v³ log M) | AC | 0.015 s | 460 KB |
| [1627_math.go](1627_math.go) | Go 1.14 x64 | math | O(v³ log M) | AC | 0.015 s | 1200 KB |
| [1627_math.java](1627_math.java) | Java 1.8 | math | O(v³ log M) | AC | 0.125 s | 1744 KB |
| [1627_math.py](1627_math.py) | Python 3.12 x64 | math | O(v³) | AC | 0.125 s | 660 KB |
| [1627_math.rs](1627_math.rs) | Rust 1.75 x64 | math | O(v³ log M) | AC | 0.046 s | 292 KB |
