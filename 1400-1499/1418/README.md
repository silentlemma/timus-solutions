# 1418. Military Story

[Timus 1418](https://acm.timus.ru/problem.aspx?space=1&num=1418) · difficulty 1491 · geometry

Original problem by Alexey Lakhtin, from the Ural State University Championship, October 29, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N distinct posts stand at integer points (3 ≤ N ≤ 4000, coordinates
from 0 to 10 000). Fences are simple polygons of non-zero area with
corners at posts; they must not touch or cross, and each must lie
inside the next. Find the largest number of fences.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N, then N lines with the coordinates.

## Output

The largest number of fences.

## Examples

### Example 1

Input:

```
4
100 100
200 100
100 200
300 300
```

Output:

```
1
```

## Solution

A post on the border of the convex hull, at a corner or in the middle
of an edge, can never be strictly inside a polygon whose corners are
posts, because such a polygon lies within the hull. So the outer fence
is the only one that can use these posts, every inner fence uses only
posts strictly inside the hull, and by induction the number of fences
is at most the number of hull layers: remove the whole hull border,
then the border of the hull of the rest, and so on, while the remaining
posts still have positive area. The hulls themselves reach this bound,
each strictly inside the previous one.

Sort the posts once; each layer is then found by Andrew's monotone
chain in linear time, popping only on a strict right turn so that posts
on the edges stay in the chain. Peeling stops when fewer than three
posts are left or all of them lie on one line. `O(N²)` in the worst
case, which is N / 3 nested triangles.

Pitfalls:

- posts in the middle of hull edges belong to the outer layer (test 09);
- leftover posts on a line, or one or two leftover posts, make no fence
  (tests 02, 07, 08, gen4);
- dense grids put many posts on every hull edge (tests 06, 07, gen3).

## Language notes

- Python runs under PyPy: 1333 nested triangles take about 1.3 s with
  CPython and about 0.2 s with PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1418_geometry.cpp](1418_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2) | AC | 0.062 s | 472 KB |
| [1418_geometry.go](1418_geometry.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.093 s | 9556 KB |
| [1418_geometry.java](1418_geometry.java) | Java 1.8 | geometry | O(N^2) | AC | 0.234 s | 6280 KB |
| [1418_geometry.py](1418_geometry.py) | PyPy 3.10 x64 | geometry | O(N^2) | AC | 0.562 s | 7684 KB |
| [1418_geometry.rs](1418_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2) | AC | 0.062 s | 552 KB |
