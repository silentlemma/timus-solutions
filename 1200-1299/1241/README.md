# 1241. Counting triangles left by straight cuts

[Timus 1241](https://acm.timus.ru/problem.aspx?space=1&num=1241) · difficulty 1680 · geometry

Original problem by Elena Kruchkova, from the ACM ICPC Northeastern European Regional Contest 2002–2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An M × N plate (M, N ≤ 50) is cut K times (K ≤ 296). Each cut is a
straight line from one point of the border to another, both with integer
coordinates, running vertically, horizontally or at 45° to the sides; all
cuts are different. Count the pieces that are right isosceles triangles,
of any size.

Time limit: 1 second. Memory limit: 64 MB.

## Input

M, N and K, then each cut as `X1 Y1 X2 Y2`.

## Output

The number of triangular pieces.

## Examples

### Example 1

Input:

```
4 4 4
1 4 1 0
0 4 4 0
0 0 4 4
0 2 4 2
```

Output:

```
6
```

### Example 2

Input:

```
7 4 6
6 0 7 1
1 4 1 0
0 4 4 0
0 0 4 4
0 2 7 2
7 0 3 4
```

Output:

```
8
```

## Solution

A cut goes from border to border, so it is a whole line through the
plate, of one of four kinds: `x = c`, `y = c`, `x − y = c` or `x + y = c`
with integer c. Only which lines are cut matters, and there are just
(M − 1) + (N − 1) + 2(M + N − 1) of them, 296 for the largest plate.

Split every unit square by both its diagonals into four small triangles.
Every possible cut runs along edges of these small triangles, so every
piece is a union of them: join two neighbouring small triangles unless
their common edge lies on a cut line, with a disjoint-set union over at
most 10 000 of them.

To recognise a triangle, note that each piece is convex, since it is
the plate cut by straight lines, and its sides point in only 8 possible
directions, one side per direction. So a piece has as many sides as its
edges have distinct outward directions. Every small triangle records the
outward directions of its edges that lie on a cut or on the border; a
piece whose union of directions has exactly 3 is a triangle, with angles
45°, 45° and 90°: it is right isosceles.
`O(M·N)`.

Pitfalls:

- the cut is given by its two endpoints, which may come in either order;
  only the kind of line and its constant matter;
- a piece can be a large triangle made of many small ones, so the shape
  must be judged by its sides, not by its area.

The counts were compared with an exact splitting of the plate's polygon
by every cut line on 400 random small plates.

## Language notes

- All languages keep the directions as an 8-bit mask per small triangle
  and count its bits.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1241_geometry.cpp](1241_geometry.cpp) | G++ 13.2 x64 | geometry | O(M·N) | AC | 0.015 s | 236 KB |
| [1241_geometry.go](1241_geometry.go) | Go 1.14 x64 | geometry | O(M·N) | AC | 0.031 s | 1356 KB |
| [1241_geometry.java](1241_geometry.java) | Java 1.8 | geometry | O(M·N) | AC | 0.093 s | 604 KB |
| [1241_geometry.py](1241_geometry.py) | Python 3.12 x64 | geometry | O(M·N) | AC | 0.109 s | 2116 KB |
| [1241_geometry.rs](1241_geometry.rs) | Rust 1.75 x64 | geometry | O(M·N) | AC | 0.046 s | 380 KB |
