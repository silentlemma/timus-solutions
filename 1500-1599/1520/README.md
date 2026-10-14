# 1520. Empire Strikes Back

[Timus 1520](https://acm.timus.ru/problem.aspx?space=1&num=1520) · difficulty 2430 · geometry

Original problem by Nikita Rybak, Ilya Grebnov and Dmitry Kovalioff, from Timus Top Coders: Third Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A republic is the disk of radius R (1 ≤ R ≤ 1000) around the origin, with
N factories (1 ≤ N ≤ 300) at integer points inside it. A bomb of one
common radius falls on each factory. Find the smallest radius for which
the bombs together cover the whole disk, with at least five digits
after the point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and R, then the coordinates of the N factories.

## Output

The smallest radius.

## Examples

### Example 1

Input:

```
4 4
0 2
0 -2
2 0
-2 0
```

Output:

```
2.94725152
```

## Solution

The answer is the largest distance from a point of the disk to its
nearest factory. Points nearest to factory i form its Voronoi cell, a
convex polygon; clip a square around the disk by the bisectors with the
other factories, nearest first, and stop once the next one is more than
twice the cell's reach away, as no farther bisector can cut it then.
Distance from the factory is a convex function, so over the part of the
cell inside the disk it peaks at a cell vertex inside the disk, at a
point where a cell edge crosses the circle, or somewhere on an arc of
the circle inside the cell, where it peaks at the circle point opposite
the factory if that point lies in the cell. Take the largest of all
these candidates over all cells. About `O(N²)` clipping steps with
small cells.

Pitfalls:

- the farthest point is often on the border, where a bisector meets the
  circle (test 01, test 04);
- an arc of the border can hold the farthest point in its middle, at
  the point opposite the factory (tests 02, 03);
- factories can repeat, and two equal points have no bisector, so they
  are skipped (test 05, gen5);
- a single factory gives R plus its distance from the centre (tests 02,
  03, gen3).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1520_geometry.cpp](1520_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2) | AC | 0.031 s | 248 KB |
| [1520_geometry.go](1520_geometry.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.062 s | 6044 KB |
| [1520_geometry.java](1520_geometry.java) | Java 1.8 | geometry | O(N^2) | AC | 0.203 s | 6652 KB |
| [1520_geometry.py](1520_geometry.py) | Python 3.12 x64 | geometry | O(N^2) | AC | 0.375 s | 888 KB |
| [1520_geometry.rs](1520_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2) | AC | 0.046 s | 296 KB |
