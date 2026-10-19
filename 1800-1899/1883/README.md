# 1883. Ent's Birthday

[Timus 1883](https://acm.timus.ru/problem.aspx?space=1&num=1883) · difficulty 1215 · geometry

Original problem by Denis Mukhametianov, from the Ural Regional School Programming Contest 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cake is the square from (−10⁹, −10⁹) to (10⁹, 10⁹) with n candles at
distinct integer points strictly inside. Cut out a convex polygon of
nonzero area that holds exactly k of the candles, counting those on its
border. Its vertices must be integer points of the cake, listed
counterclockwise, with no straight angles and no zero-length sides.

## Input

n and k (1 ≤ k < n ≤ 1000), then the n candles; all coordinates are
below 10⁹ in absolute value.

## Output

The number m of vertices (3 ≤ m ≤ 10 000) and the vertices. Any valid
polygon is accepted.

## Examples

### Example 1

Input:

```
5 3
1 0
1 2
2 1
3 0
3 2
```

Output:

```
3
1 0
2 1
1 2
```

## Solution

Sort the candles by x and then by y, and let (x, y) be the k-th one.
The first k candles are all candles with a smaller x, together with
those in column x up to y. Take everything left of the column, the
column up to (x, y), and the strip between columns x − 1 and x below
the line from (x, y) to (x − 1, 10⁹):

(−10⁹, −10⁹), (x, −10⁹), (x, y), (x − 1, 10⁹), (−10⁹, 10⁹).

Every turn is a strict left turn. Column x − 1 lies wholly inside,
since candles stay below 10⁹, while candles above (x, y) in column x
are outside the slanted edge. If x − 1 = −10⁹ the fourth vertex would
repeat the fifth, so it is dropped and a quadrilateral is left. Sorting
takes `O(n log n)`.

For the example the third candle in this order is (2, 1), and the
pentagon (−10⁹, −10⁹), (2, −10⁹), (2, 1), (1, 10⁹), (−10⁹, 10⁹) holds
(1, 0), (1, 2) and (2, 1), a different but valid answer.

Pitfalls:

- a plain vertical cut fails when several candles share a column; the
  slanted top edge splits that column at the k-th candle;
- candles on the border count, so the k-th candle may sit on a vertex;
- with x − 1 = −10⁹ the vertex (x − 1, 10⁹) coincides with the corner
  and must be left out to avoid a zero-length side.

The pieces pass a checker for strict convexity, orientation, the
coordinate range and the candle count on 40 small boards and on 125
random large cakes, many with crowded columns.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1883_geometry.cpp](1883_geometry.cpp) | G++ 13.2 x64 | geometry | O(n log n) | AC | 0.015 s | 208 KB |
| [1883_geometry.go](1883_geometry.go) | Go 1.14 x64 | geometry | O(n log n) | AC | 0.031 s | 1148 KB |
| [1883_geometry.java](1883_geometry.java) | Java 1.8 | geometry | O(n log n) | AC | 0.171 s | 2816 KB |
| [1883_geometry.py](1883_geometry.py) | Python 3.12 x64 | geometry | O(n log n) | AC | 0.078 s | 700 KB |
| [1883_geometry.rs](1883_geometry.rs) | Rust 1.75 x64 | geometry | O(n log n) | AC | 0.046 s | 296 KB |
