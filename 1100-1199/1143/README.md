# 1143. The shortest path through all vertices of a convex polygon

[Timus 1143](https://acm.timus.ru/problem.aspx?space=1&num=1143) · difficulty 589 · dp

Original problem from the selection contest for the Vietnam IOI team.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 200` camps stand at the vertices of a convex polygon, given in
counter-clockwise order with real coordinates. Find the length of the
shortest path that starts at any camp and visits every camp, printed with
three digits after the point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines with the coordinates of the vertices.

## Output

The length of the shortest path, with three decimals.

## Examples

### Example 1

Input:

```
4
50.0 1.0
5.0 1.0
0.0 0.0
45.0 0.0
```

Output:

```
50.211
```

## Solution

A shortest path never crosses itself: if two of its segments cross,
reversing the part between them replaces them by two segments that are
together shorter, by the triangle inequality. On points in convex
position this has a strong consequence: at every moment the visited
vertices form an arc of the polygon, and the path stands at one end of
that arc. Otherwise the path would have to jump over the arc to reach
the other side, and a later segment would cross an earlier one.

So the state is an arc `(i, length)` and the end where the path stands.
An arc grows by one vertex at either side, from either end, which gives
four transitions. Let `at[i]` and `at_end[i]` be the shortest paths over
the arc that starts at vertex `i`, standing at its first or its last
vertex. Start with all arcs of length 1 at cost 0, grow them to length
`N`, and take the smallest value. `O(N²)` time, `O(N)` memory per length.

Pitfalls:

- going around the polygon is not always best: in a long thin polygon the
  path zigzags between the two long sides;
- `N = 1` gives `0.000`;
- the arcs wrap around the end of the vertex list, so indices are taken
  modulo `N`;
- the answer is printed with exactly three decimals.

The answers were compared with the Held–Karp search over all subsets,
which does not use convexity, on 120 random polygons of up to 11
vertices, including thin ellipses and vertices crowded on a short arc.

## Language notes

- All languages run the same arc DP with two arrays per length.
- Java formats the answer with `Locale.US` so that the decimal separator
  is a point.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1143_dp.cpp](1143_dp.cpp) | G++ 13.2 x64 | dp | O(N²) | AC | 0.015 s | 240 KB |
| [1143_dp.go](1143_dp.go) | Go 1.14 x64 | dp | O(N²) | AC | 0.031 s | 1864 KB |
| [1143_dp.java](1143_dp.java) | Java 1.8 | dp | O(N²) | AC | 0.203 s | 1836 KB |
| [1143_dp.py](1143_dp.py) | Python 3.12 x64 | dp | O(N²) | AC | 0.156 s | 2244 KB |
| [1143_dp.rs](1143_dp.rs) | Rust 1.75 x64 | dp | O(N²) | AC | 0.046 s | 272 KB |
