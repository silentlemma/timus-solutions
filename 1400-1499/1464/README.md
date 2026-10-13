# 1464. Light

[Timus 1464](https://acm.timus.ru/problem.aspx?space=1&num=1464) · difficulty 2749 · geometry

Original problem by Dmitry Ivankov (idea by Alexander Ipatov), from the Ural State University Contest at the Petrozavodsk Winter Training Camp, January 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A room is a simple polygon with N corners (3 ≤ N ≤ 50000) listed
counterclockwise, with coordinates from 0 to 1000 given to at most four
decimals. A lamp hangs at a point strictly inside it. Find the area of
the part of the room that the lamp lights, that is, the area visible
from the lamp, to at least two decimals.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

The lamp, N, then the N corners.

## Output

The lit area.

## Examples

### Example 1

Input:

```
1.0 1.0
6
0 0
3 0
3 2
2 2
2 3
0 3
```

Output:

```
8.00
```

## Solution

Look at the room from the lamp. Sort the corners by direction and merge
equal directions; since the lamp is inside, consecutive directions are
less than half a turn apart. Between two consecutive directions no
corner is seen, so within such a gap the lit region ends on a single
edge, the nearest one crossing the gap, and the gap contributes the
triangle between the lamp and that edge, cut by the two rays.

An edge, seen from the lamp, covers a run of consecutive gaps (an edge
seen edge-on covers none and hides nothing). Put the gaps in a segment
tree and add every edge to the O(log N) nodes that make up its run.
Each node keeps only the nearest of its edges: two edges covering the
same gaps never cross, so one comparison along a ray through the node's
first gap decides for all of its gaps. For every gap the nearest edge is
then among the nodes on its path to the root. `O(N log N)`.

All coordinates are read exactly as integers in units of 10⁻⁴, so the
merging of directions and the orientation of edges are decided without
rounding; floating point handles angles, ray intersections and areas.

Pitfalls:

- corners in line with the lamp, and edges pointing straight at it
  (tests 07, 13, gen3);
- deep notches and combs with partly hidden regions (tests 04,
  gen2);
- a quadratic scan over edges for every gap is far too slow for 50000
  corners.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1464_geometry.cpp](1464_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.109 s | 6232 KB |
| [1464_geometry.go](1464_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.140 s | 13688 KB |
| [1464_geometry.java](1464_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.250 s | 9068 KB |
| [1464_geometry.py](1464_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 1.531 s | 38272 KB |
| [1464_geometry.rs](1464_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.046 s | 9092 KB |
