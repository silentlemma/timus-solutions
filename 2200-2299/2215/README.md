# 2215. Counting points in rectangles while the whole plane keeps turning

[Timus 2215](https://acm.timus.ru/problem.aspx?space=1&num=2215) · difficulty 2164 · geometry, fenwick

Original problem by Vadim Barinov, from the University Academic School Olympiad in Informatics 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N distinct points get Q events in order: rotate all points by 90°,
180° or 270° counterclockwise around a given point, or count the points
inside an axis-parallel rectangle. The limits are 3 seconds and 256 MB.

## Input

N, 1 ≤ N ≤ 4 · 10⁴, then the points, then Q, 1 ≤ Q ≤ 4 · 10⁴, and the
events "r90 x y", "r180 x y", "r270 x y" or "ask x1 y1 x2 y2", all
coordinates up to 10⁹ in absolute value.

## Output

The count for every "ask".

## Examples

### Example 1

Input:

```
4
1 1
2 2
3 3
4 4
4
r90 0 0
ask -2 -1 0 4
r180 1 1
ask 3 -3 6 0
```

Output:

```
2
3
```

## Solution

Any sequence of quarter turns around points is one quarter turn around
the origin followed by a shift: the current position of an original
point p is Rᵏ p + t. A new turn by j quarters around c maps this to
Rʲ(Rᵏ p + t − c) + c, so it is enough to update k and t.

A query rectangle in current coordinates is mapped back to the original
coordinates by subtracting t and turning by −k quarters. A quarter turn
maps an axis-parallel rectangle to an axis-parallel rectangle, so
mapping two opposite corners and sorting their coordinates is enough.
All queries then ask about the same fixed point set.

That is answered offline: every rectangle becomes two events at its
right edge and just left of its left edge, the events and the points
are swept in x order, and a Fenwick tree over compressed y counts the
inserted points in each y range.

In the example, after the first turn the points are (−1, 1) … (−4, 4),
and the first rectangle contains (−1, 1) and (−2, 2).

This takes O((N + Q) log N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2215_geometry_fenwick.cpp](2215_geometry_fenwick.cpp) | G++ 13.2 x64 | geometry, fenwick | O((N + Q) log N) | AC | 0.078 s | 5076 KB |
| [2215_geometry_fenwick.go](2215_geometry_fenwick.go) | Go 1.14 x64 | geometry, fenwick | O((N + Q) log N) | AC | 0.296 s | 10672 KB |
| [2215_geometry_fenwick.java](2215_geometry_fenwick.java) | Java 1.8 | geometry, fenwick | O((N + Q) log N) | AC | 0.421 s | 12104 KB |
| [2215_geometry_fenwick.py](2215_geometry_fenwick.py) | Python 3.12 x64 | geometry, fenwick | O((N + Q) log N) | AC | 0.718 s | 37016 KB |
| [2215_geometry_fenwick.rs](2215_geometry_fenwick.rs) | Rust 1.75 x64 | geometry, fenwick | O((N + Q) log N) | AC | 0.062 s | 8496 KB |
