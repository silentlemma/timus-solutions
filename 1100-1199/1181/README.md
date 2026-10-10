# 1181. Cutting a three-colored polygon into rainbow triangles

[Timus 1181](https://acm.timus.ru/problem.aspx?space=1&num=1181) · difficulty 455 · constructive

Original problem by Dmitry Filimonenkov, from the Third USU Personal Programming Contest, Ekaterinburg, February 16, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The vertices of a convex polygon with `4 ≤ N ≤ 1000` vertices are colored
R, G and B; all three colors occur and no two neighbours share a color.
Cut the polygon by non-crossing diagonals into triangles that each have
one vertex of every color, or print 0 if that is impossible.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the colors in order around the polygon.

## Output

The number of diagonals, then the diagonals as pairs of vertex numbers.

## Checking

Any cut is accepted if its `N − 3` distinct diagonals do not cross and
every triangle they make has all three colors. Such a cut always exists,
so `0` is never right.

## Examples

### Example 1

Input:

```
7
RBGBRGB
```

Output:

```
4
1 3
3 7
5 7
5 3
```

## Solution

If some color occurs only once, draw every diagonal from that vertex.
Each triangle of the fan has this vertex and two neighbouring vertices of
the rest, which differ from each other and from it.

Otherwise every color occurs at least twice. There is a vertex whose two
neighbours have different colors: if every vertex had equal neighbours,
the colors would repeat with period two around the polygon, and only two
colors would occur. Cut off that vertex with the diagonal between its
neighbours; the triangle has three colors, the rest still has all three
colors (the removed one occurs elsewhere) and no equal neighbours. Repeat
until a color is alone or a triangle remains. So the answer always
exists, with `N − 3` diagonals. `O(N²)` with plain list removal.

Pitfalls:

- the answer is never 0, which is easy to miss in a problem that asks
  for it;
- after a cut, the color counts change, so a color can become single
  later, which is when the fan finishes the job;
- an odd polygon cannot alternate two colors, which is another way to see
  that the search for a vertex with different neighbours never fails.

Every printed cut passed the checker on 200 random polygons of up to 33
vertices and on all tests, including thousand-vertex polygons.

## Language notes

- All languages keep the remaining vertices in a list and remove the cut
  vertex from it.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1181_constructive.cpp](1181_constructive.cpp) | G++ 13.2 x64 | constructive | O(N²) | AC | 0.015 s | 408 KB |
| [1181_constructive.go](1181_constructive.go) | Go 1.14 x64 | constructive | O(N²) | AC | 0.031 s | 1188 KB |
| [1181_constructive.java](1181_constructive.java) | Java 1.8 | constructive | O(N²) | AC | 0.218 s | 6632 KB |
| [1181_constructive.py](1181_constructive.py) | Python 3.12 x64 | constructive | O(N²) | AC | 0.203 s | 760 KB |
| [1181_constructive.rs](1181_constructive.rs) | Rust 1.75 x64 | constructive | O(N²) | AC | 0.031 s | 476 KB |
