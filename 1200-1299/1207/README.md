# 1207. A line through two points that halves the rest

[Timus 1207](https://acm.timus.ru/problem.aspx?space=1&num=1207) · difficulty 120 · geometry

Original problem by Pavel Atnashev, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are an even number `4 ≤ N ≤ 10000` of points with integer
coordinates up to `10⁶` in absolute value, no three on a line. Choose two
of them so that the line through them splits the other points into two
halves of equal size.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N`, then the coordinates of each point.

## Output

The numbers of the two chosen points.

## Checking

Many pairs work, so any two different points are accepted if their line
leaves `(N − 2)/2` points on each side.

## Examples

### Example 1

Input:

```
4
0 0
1 0
0 1
1 1
```

Output:

```
1 4
```

## Solution

Take the lowest point, the leftmost if two share the lowest height. All
the other points lie above it or to its right on the same height, within
half a turn, so they can be sorted by the angle around it using only the
sign of the cross product, with no floating point. In that order every
point before the `k`-th lies on one side of the line from the lowest
point to the `k`-th, and every point after it on the other side. With
`N − 1` other points, the one at index `(N − 2)/2` from zero has
`(N − 2)/2` before and after it. `O(N log N)`.

Pitfalls:

- with the lowest point picked by height alone, a point at the same
  height to its left would sit at half a turn and break the order;
- the cross products reach `8·10¹²`, beyond 32 bits;
- a comparator must return "equal" for an element compared with itself,
  or some sorting routines reject it.

Every answer was checked by counting the points on each side, and a
separately written solution passes the same checker on every test.

## Language notes

- Python sorts with `functools.cmp_to_key`; Java sorts boxed indices with
  a lambda that uses `Long.compare`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1207_geometry.cpp](1207_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 296 KB |
| [1207_geometry.go](1207_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.046 s | 1512 KB |
| [1207_geometry.java](1207_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.171 s | 5544 KB |
| [1207_geometry.py](1207_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.140 s | 3516 KB |
| [1207_geometry.rs](1207_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 908 KB |
