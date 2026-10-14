# 1616. Square Country 4

[Timus 1616](https://acm.timus.ru/problem.aspx?space=1&num=1616) · difficulty 3993 · geometry

Original problem by Vladimir Yakovlev (idea by Stanislav Vasilyev), from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A map of the square [−n, n] × [−n, n] (1 ≤ n ≤ 30) shows who owns each
unit cell: a lowercase letter per owner, `.` for the state. The x axis
goes right and the y axis up. The coordinate axes are then turned
clockwise about (0, 0) by α degrees (0 ≤ α ≤ 90, a real number), and
every unit cell of the new grid goes to an owner who held more than half
of its area before the turn, or to the state if nobody did. Print the new
map of [−2n, 2n] × [−2n, 2n] in the same form.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n and α, then 2n rows of 2n characters.

## Output

4n rows of 4n characters.

## Examples

### Example 1

Input:

```
2 45.0
aaaa
aaaa
bb.x
bbx.
```

Output:

```
........
........
...aa...
..aa.x..
..a..x..
...bb...
........
........
```

## Solution

Turning the axes clockwise turns the land counterclockwise in the new
coordinates. Each owned cell becomes a square turned by α; it overlaps
only the few new cells within its bounding box. Clipping the turned
square against each of those cells (four half-planes, as in the
Sutherland–Hodgman method) gives the overlap polygon, and the shoelace
formula gives its area, added to that owner's share of the cell. A cell
then goes to an owner whose share exceeds 1/2 by more than 10⁻⁹. With at
most 3 600 owned cells this is instant. `O(n²)`.

Pitfalls:

- a share of exactly one half is not more than half: such cells go to
  the state (the example's cut cells at 45 degrees);
- α = 0 and α = 90 map cells exactly onto cells, and edges that only
  touch must add no area (tests 02, 03);
- the radians are computed as α · π / 180 in every language, so that
  borderline shares round the same way.

The outputs match an independent accepted implementation on 150 random
maps.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1616_geometry.cpp](1616_geometry.cpp) | G++ 13.2 x64 | geometry | O(n²) | AC | 0.031 s | 3564 KB |
| [1616_geometry.go](1616_geometry.go) | Go 1.14 x64 | geometry | O(n²) | AC | 0.046 s | 8724 KB |
| [1616_geometry.java](1616_geometry.java) | Java 1.8 | geometry | O(n²) | AC | 0.187 s | 9704 KB |
| [1616_geometry.py](1616_geometry.py) | Python 3.12 x64 | geometry | O(n²) | AC | 0.359 s | 5252 KB |
| [1616_geometry.rs](1616_geometry.rs) | Rust 1.75 x64 | geometry | O(n²) | AC | 0.031 s | 3040 KB |
