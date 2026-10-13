# 1504. Good Manners

[Timus 1504](https://acm.timus.ru/problem.aspx?space=1&num=1504) · difficulty 2173 · geometry

Original problem by Stanislav Vasiliev, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

K pieces of cake (2 ≤ K ≤ 1000) lie at distinct points of a round table
of radius R (1 ≤ R ≤ 100) centred at the origin, each with a weight
from 1 to 10000 grams. A guest seated at a point of the table's edge
politely takes the nearest piece, the heaviest one if several are
equally near. Find a seat on the edge that gets the heaviest possible
piece.

Time limit: 1.5 seconds. Memory limit: 64 MB.

## Input

R and K, then K lines with the coordinates of a piece (real numbers)
and its weight.

## Output

The two coordinates of the seat, accurate to 7 digits. Any best seat is
accepted.

## Examples

### Example 1

Input:

```
10 3
1 -1 100
2 2 200
-2.5 -2.56 1
```

Output:

```
6 8
```

## Solution

The points nearer to piece i than to every other piece form its Voronoi
cell: the intersection of the half-planes bounded by the perpendicular
bisectors, a convex polygon containing the piece. A seat gets piece i
when it lies in that cell, so the answer is the heaviest piece whose
cell reaches the edge. The piece itself is on the table and the cell
is convex, so the cell reaches the edge exactly when its vertex
farthest from the centre is at least R away.

Try the pieces from the heaviest down. For each, start from a square
around the table and cut it by the bisectors with the other pieces,
nearest first. Stop with a failure as soon as every vertex is inside
the table, and stop cutting once the next piece is more than twice the
cell's reach away, since its bisector cannot touch the cell then. The
seat lies where the segment from the piece to the farthest vertex
crosses the edge. Each cut is linear in the cell size, and the cells
of pieces that fail shrink inside the table after a few of their
nearest neighbours, so the work stays near `O(K² log K)` at worst.

Pitfalls:

- the cell can touch the edge at a single point, where the seat is
  equally far from several pieces and the heaviest one is taken, so the
  test needs a small tolerance (test 02);
- a cell that misses the edge by a few hundredths must fail (test 07);
- the heaviest piece can be boxed in by lighter ones (test 05, gen2);
- a piece can lie on the edge itself (test 04);
- with equal weights every seat is right (test 06);
- many seats are right, so the tests use a checker (all tests);
- cutting every heavy cell by all pieces takes about 3 seconds in
  Python; the early stops bring it to a few tenths (gen2, gen6).

## Language notes

- Python runs under PyPy: CPython exceeds the 1.5 s limit on the judge's
  test 32, and PyPy takes about 1.1 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1504_geometry.cpp](1504_geometry.cpp) | G++ 13.2 x64 | geometry | O(K^2 log K) | AC | 0.359 s | 292 KB |
| [1504_geometry.go](1504_geometry.go) | Go 1.14 x64 | geometry | O(K^2 log K) | AC | 0.546 s | 7708 KB |
| [1504_geometry.java](1504_geometry.java) | Java 1.8 | geometry | O(K^2 log K) | AC | 0.343 s | 6796 KB |
| [1504_geometry.py](1504_geometry.py) | PyPy 3.10 x64 | geometry | O(K^2 log K) | AC | 1.125 s | 9332 KB |
| [1504_geometry.rs](1504_geometry.rs) | Rust 1.75 x64 | geometry | O(K^2 log K) | AC | 0.109 s | 1288 KB |
