# 1199. The least exposed way for a mouse to reach the cheese

[Timus 1199](https://acm.timus.ru/problem.aspx?space=1&num=1199) · difficulty 3906 · geometry

Original problem by Nikita Rybak.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A kitchen holds up to 100 pieces of furniture, each a convex polygon with
3 to 10 corners, any two pieces more than 20 cm apart. A point is
dangerous when it is more than 10 cm from every piece. Find a polyline
from the mouse to the cheese with the smallest total length of dangerous
parts. Every segment must be wholly dangerous or wholly safe, apart from
its ends, and the polyline may have at most 1000 vertices.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The mouse and the cheese as `x y x y`, then `N`, then each polygon as
`K` followed by `K` corners. Coordinates are in metres with at most three
decimals and at most `10⁵` in absolute value; neither the mouse nor the
cheese is inside a polygon.

## Output

The number of vertices of the polyline, counting both ends, then the
vertices, one per line, accurate to `10⁻⁴`.

## Checking

Any polyline is accepted if it starts at the mouse, ends at the cheese,
has at most 1000 vertices, has no segment that is partly safe and partly
dangerous, and has the smallest dangerous length; the reference checker
finds the safe part of each segment exactly and allows 1 mm of slack.

## Examples

### Example 1

Input:

```
1.0 1.5 0.0 1.5
1
4
0.0 0.0
0.0 1.0
1.0 1.0
1.0 0.0
```

Output:

```
4
1.0 1.5
1.0 1.1
0.0 1.1
0.0 1.5
```

## Solution

The safe area around a piece is the polygon grown by 10 cm, a convex
zone, and the zones do not touch because the pieces are more than 20 cm
apart. Moving inside one zone is free, so a path is a chain of zones
joined by dangerous stretches, and each stretch costs at least the gap
between the two things it joins. That gives a graph with the mouse, the
cheese and the zones as nodes: the gap between two zones is the distance
between the polygons minus 20 cm, the gap from the mouse or the cheese to
a zone is its distance to the polygon minus 10 cm (or 0 when it is
already safe), and mouse to cheese costs the straight distance. Dijkstra's
algorithm on this complete graph gives the answer.

Every gap can be realised exactly. Between two polygons take their
closest pair of points; the segment between them, shortened by 10 cm at
each end, is dangerous all along. A dangerous segment that cut through
a third zone would make a cheaper path through that zone, so the
shortest path never needs one. Inside a zone the mouse steps onto the
nearest point of the polygon, walks along the boundary the way that
passes fewer corners, and steps off at the closest point to the next
zone; it never goes through the furniture, and each zone adds at most
nine vertices, well within the limit.

The distance between two polygons is the smallest distance from a corner
of one to an edge of the other. A pair is skipped when even the bound from
their bounding circles cannot improve the target's distance, which
removes most pairs in practice. `O(N²K²)` at worst.

Pitfalls:

- the corners are not promised to be in order, so each polygon is sorted
  by angle around its centre first;
- points exactly 10 cm away count as safe, so the sample's answer walks
  along the edge of the safe zone;
- the mouse or the cheese may already be within 10 cm of a piece;
- the straight path from the mouse to the cheese must also be a candidate.

The dangerous lengths were compared with a separately written solution
on 320 random kitchens and on every test, using the checker in both
directions.

## Language notes

- All languages run the same search with the same bounding-circle bound
  and print nine decimals.
- Java formats numbers with `Locale.US`, since the default locale could
  print commas.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1199_geometry.cpp](1199_geometry.cpp) | G++ 13.2 x64 | geometry | O(N²K²) | AC | 0.015 s | 352 KB |
| [1199_geometry.go](1199_geometry.go) | Go 1.14 x64 | geometry | O(N²K²) | AC | 0.031 s | 1360 KB |
| [1199_geometry.java](1199_geometry.java) | Java 1.8 | geometry | O(N²K²) | AC | 0.234 s | 6572 KB |
| [1199_geometry.py](1199_geometry.py) | Python 3.12 x64 | geometry | O(N²K²) | AC | 0.640 s | 1892 KB |
| [1199_geometry.rs](1199_geometry.rs) | Rust 1.75 x64 | geometry | O(N²K²) | AC | 0.031 s | 376 KB |
