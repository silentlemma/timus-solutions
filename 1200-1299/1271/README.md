# 1271. Pilot

[Timus 1271](https://acm.timus.ru/problem.aspx?space=1&num=1271) · difficulty 4551 · geometry

Original problem by Alexey Lakhtin, from the Ural State University Championship, October 25, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A triangular tanker sails in a rectangular harbour 0 ≤ x ≤ DX,
0 ≤ y ≤ DY (DX, DY < 10⁸) among N ≤ 40 triangular ships at anchor. It
can only move, never turn. Find the length of the shortest route that
brings its first corner to a given point, rounded to three digits, or
−1 if this is impossible. The tanker may touch the ships and the
harbour's sides but not overlap them; ships do not overlap each other.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

DX and DY, the tanker's three corners, the goal for its first corner,
N, then the three corners of every ship. All coordinates are integers.

## Output

The length of the route, or −1.

## Examples

### Example 1

Input:

```
2003 2003
20 50
10 30
30 30
140 60
1
80 1000
100 20
60 20
```

Output:

```
146.569
```

## Solution

Track only the first corner A of the tanker; the other corners sit at
fixed offsets d₁, d₂, d₃ from it (one of them zero).

- The tanker stays in the harbour exactly when A stays in a smaller
  rectangle, shifted in by the smallest and largest offsets.
- The tanker overlaps a ship exactly when A lies strictly inside the
  convex hull of the nine points (ship corner − tanker offset). These
  are the Minkowski sums, open convex polygons of at most six corners.

So a point moves in a rectangle around open convex obstacles. A shortest
path bends only at corners of the obstacles. The graph therefore has the
start, the goal and every obstacle corner that lies in the rectangle and
not strictly inside another obstacle. Two of these points are joined
when the segment between them misses the inside of every obstacle.
Dijkstra's algorithm then finds the route.

Everything is exact in 64-bit integers: corners are integer, below
3 · 10⁸ in absolute value. A segment misses an open convex polygon
exactly when some axis separates them, at worst touching. The axes to
try are the normals of the polygon's edges and the normal of the
segment itself. Each test compares dot products of about 10¹⁷. With
V ≤ 242 graph points and N polygons this is `O(V² · N)`.

Pitfalls:

- touching is allowed: the tanker may slide along a ship, pass a gap
  exactly as wide as itself, or end touching a ship (tests 06, 07, 09);
- the goal may be unreachable because the tanker does not fit there,
  inside the harbour or among the ships (test 03);
- floating-point tests can go wrong at 10⁸, where a sliver one unit thick
  must still block the way (test 05);
- an obstacle may stick out of the shrunken rectangle; its corners
  outside are not usable, but the parts inside still block;
- when the goal is the start, the answer is 0 (test 04).

The answers were compared with an independent implementation on 240
random harbours, including 40-ship ones, 10⁸ coordinates and walls with
narrow gaps.

## Language notes

- All languages use the same exact integer tests and a simple O(V²)
  Dijkstra.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1271_geometry.cpp](1271_geometry.cpp) | G++ 13.2 x64 | geometry | O(V² · N) | AC | 0.015 s | 280 KB |
| [1271_geometry.go](1271_geometry.go) | Go 1.14 x64 | geometry | O(V² · N) | AC | 0.031 s | 1260 KB |
| [1271_geometry.java](1271_geometry.java) | Java 1.8 | geometry | O(V² · N) | AC | 0.171 s | 5508 KB |
| [1271_geometry.py](1271_geometry.py) | Python 3.12 x64 | geometry | O(V² · N) | AC | 0.390 s | 1200 KB |
| [1271_geometry.rs](1271_geometry.rs) | Rust 1.75 x64 | geometry | O(V² · N) | AC | 0.062 s | 500 KB |
