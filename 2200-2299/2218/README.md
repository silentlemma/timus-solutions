# 2218. Counting points at an exact Manhattan distance

[Timus 2218](https://acm.timus.ru/problem.aspx?space=1&num=2218) · difficulty 817 · geometry, binary_search

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2025.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N distinct computers stand at integer points. A runner at (x, y) must
cover exactly d moving along the axes, and may not go to a computer that
is closer than d. For each of Q runners, count the computers at
Manhattan distance exactly d. The limits are 3 seconds and 256 MB.

## Input

N, 1 ≤ N ≤ 10⁵, then the computers, then Q, 1 ≤ Q ≤ 10⁵, and the
runners x, y, d with coordinates up to 10⁹ in absolute value and
0 ≤ d ≤ 4 · 10⁹.

## Output

The count for each runner.

## Examples

### Example 1

Input:

```
5
0 0
1 1
2 0
1 -1
1 0
4
1 0 1
2 2 2
5 1 5
0 1 4
```

Output:

```
4
2
1
0
```

## Solution

Rotate by u = x + y and v = x − y. The Manhattan distance becomes
max(|Δu|, |Δv|), so the points at distance exactly d lie on the
boundary of an axis-parallel square: two vertical sides u = U ± d with
|v − V| ≤ d, and two horizontal sides v = V ± d with |u − U| < d, the
corners being counted with the vertical sides.

Sort the points by (u, v) and, separately, by (v, u). Each side is then
a contiguous run in one of the lists, so two binary searches count it.
For d = 0 only the runner's own point can match.

In the example the runner at (1, 0) with d = 1 reaches the four
neighbors (0, 0), (1, 1), (2, 0) and (1, −1).

Sorting takes O(N log N) and each runner at most eight binary searches:
eight for d > 0 and two for d = 0. Pitfall (tests 02 and 09): when
d = 0 the square collapses to one point, so check that point once
instead of counting four sides.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2218_geometry_binary_search.cpp](2218_geometry_binary_search.cpp) | G++ 13.2 x64 | geometry, binary_search | O((N + Q) log N) | AC | 0.203 s | 2880 KB |
| [2218_geometry_binary_search.go](2218_geometry_binary_search.go) | Go 1.14 x64 | geometry, binary_search | O((N + Q) log N) | AC | 0.250 s | 19016 KB |
| [2218_geometry_binary_search.java](2218_geometry_binary_search.java) | Java 1.8 | geometry, binary_search | O((N + Q) log N) | AC | 0.562 s | 11280 KB |
| [2218_geometry_binary_search.py](2218_geometry_binary_search.py) | PyPy 3.10 x64 | geometry, binary_search | O((N + Q) log N) | AC | 1.453 s | 61836 KB |
| [2218_geometry_binary_search.rs](2218_geometry_binary_search.rs) | Rust 1.75 x64 | geometry, binary_search | O((N + Q) log N) | AC | 0.140 s | 12772 KB |
