# 1052. The most points on one line

[Timus 1052](https://acm.timus.ru/problem.aspx?space=1&num=1052) · difficulty 238 · geometry

Original problem by Stanislav Vasiliev, from the Ural State University Collegiate Programming Contest, March 25, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `N` distinct points (`3 ≤ N ≤ 200`) with integer coordinates from
−2000 to 2000, find the largest number of them that lie on one straight
line.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines with `x` and `y`.

## Output

The largest number of points on one line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
6
7 122
8 139
9 156
10 173
11 190
-100 1
```

Output:

```
5
```

### Example 2

Input:

```
3
0 0
1 0
0 1
```

Output:

```
2
```

## Solution

Fix a point `i` and look at the directions to the points after it. Two
points `j`, `k` lie on one line with `i` exactly when the vectors
`i → j` and `i → k` are parallel. Make every vector canonical: divide
`(dx, dy)` by `gcd(|dx|, |dy|)` and flip the sign so that `dx > 0`, or
`dx = 0` and `dy > 0`. Parallel vectors then become equal, and counting
equal directions in a map gives the largest line through `i` (plus `i`
itself). Taking `i` as the first point of each line in input order is
enough, so only later points are counted. `O(N^2 log C)`.

Integers keep the comparison exact; with slopes as floating-point
numbers, vertical lines and nearly equal slopes need care.

Pitfalls:

- vertical lines (`dx = 0`) and horizontal lines (`dy = 0`);
- opposite vectors describe the same line: normalize the sign;
- any two points are on a line, so the answer is at least 2.

An alternative is the `O(N^3)` check of every pair with every point by a
cross product, which is also fast enough for `N = 200`; the tests were
checked with it.

## Language notes

- **C++**, **Go**, **Python**, **Rust**: a map keyed by the pair of
  components.
- **Java**: the pair is packed into one `long` key (`dx · 8192 + dy`,
  since `|dy| ≤ 4000`).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1052_geometry.cpp](1052_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2 log C) | AC | 0.001 s | 208 KB |
| [1052_geometry.go](1052_geometry.go) | Go 1.14 x64 | geometry | O(N^2 log C) | AC | 0.015 s | 3264 KB |
| [1052_geometry.java](1052_geometry.java) | Java 1.8 | geometry | O(N^2 log C) | AC | 0.156 s | 4180 KB |
| [1052_geometry.py](1052_geometry.py) | Python 3.12 x64 | geometry | O(N^2 log C) | AC | 0.078 s | 508 KB |
| [1052_geometry.rs](1052_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2 log C) | AC | 0.015 s | 412 KB |
