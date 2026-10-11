# 1308. Dean's Pyramid

[Timus 1308](https://acm.timus.ru/problem.aspx?space=1&num=1308) · difficulty 2786 · bfs

Original problem: idea by Stanislav Vasiliev, prepared by Pavel Egorov and Alexander Mironenko, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A pyramid with a unit square base and four equilateral side faces
stands on its base, centred at the origin, with the base edges along
the axes. A move rolls it over an edge of the face it lies on, the edge
staying in place on the table. One extra rule applies: after rolling
onto the base over some edge, the next roll must go over the opposite
edge of the base. In at most 70 rolls, bring the pyramid back onto its
base with the centre of the base as close as possible to a given point
at most 25 from the origin. Print that distance with four decimals.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The coordinates of the target point.

## Output

The smallest distance.

## Examples

### Example 1

Input:

```
2.3660254037 1.3660254038
```

Output:

```
0.0000
```

## Solution

Rolling a solid over an edge lays the next face on the other side of
that edge, so it helps to follow the faces on the table.

- From a side face to the next side face, the roll goes over an edge
  through the apex. The apex stays where it is, and the new triangle
  is the old one turned by 60° around it.
- From a side face onto the base, the square lies beyond the
  triangle's base edge, and by the rule the next roll goes straight on
  to the opposite side face. So the pair of rolls moves the apex by the
  triangle's height twice plus the square's side,
  1 + √3 in the direction from the apex to the base edge, and that
  direction is reversed.

So a lying triangle is described by its apex and one of six directions.
The moves are a turn of ±60° (one roll) and a jump of 1 + √3 (two
rolls), and stopping means one more roll onto the base, whose centre is
then (1 + √3) / 2 beyond the apex.

The first roll leaves the base over one of its four edges. With 60°
turns, the edges at 0° and 180° lead to the same six directions, and
the edges at 90° and 270° to six others. So the apex, measured in
half jumps, always sits on a hexagonal lattice, and all positions can
be listed exactly as pairs of integers. A shortest-path search by
number of rolls (each move costs 1 or 2, so buckets by cost are enough)
visits every triangle state reachable within 69 rolls, a few thousand per class.
Each state is tried as the last one before rolling onto the base, and
the closest centre wins; rolling not at all is also allowed.

`O(S)` for S reachable states.

Pitfalls:

- many points are reached exactly, like the example and one full jump
  away (tests 01 and 08), but not every lattice point: half a jump
  along an axis is never reached (test 07);
- the start itself counts, with no rolls at all (test 02).

The model was compared with a real 3D simulation of the rolling
pyramid, the solid turned about each edge until the next face lies
flat, under the dean's rule. Up to 10 rolls both gave exactly the same
set of base positions.

## Language notes

- (1 + √3) / 2 is computed as 1/2 + sin 60°, from the same 60° used
  for the directions.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1308_bfs.cpp](1308_bfs.cpp) | G++ 13.2 x64 | bfs | O(S) for S reachable states | AC | 0.015 s | 960 KB |
| [1308_bfs.go](1308_bfs.go) | Go 1.14 x64 | bfs | O(S) for S reachable states | AC | 0.031 s | 2996 KB |
| [1308_bfs.java](1308_bfs.java) | Java 1.8 | bfs | O(S) for S reachable states | AC | 0.171 s | 3912 KB |
| [1308_bfs.py](1308_bfs.py) | Python 3.12 x64 | bfs | O(S) for S reachable states | AC | 0.125 s | 1556 KB |
| [1308_bfs.rs](1308_bfs.rs) | Rust 1.75 x64 | bfs | O(S) for S reachable states | AC | 0.015 s | 1544 KB |
