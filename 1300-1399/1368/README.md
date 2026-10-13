# 1368. Goat in the Garden 3

[Timus 1368](https://acm.timus.ru/problem.aspx?space=1&num=1368) · difficulty 2449 · geometry

Original problem by Alexey Lakhtin, from the Ninth Ural Team Student Programming Championship, Yekaterinburg, April 19–24, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A goat stands in cell (0, 0) of an endless grid and moves only up,
down, left and right. Fence sections can be put into single cells. Shut
the goat into an area of exactly K cells, 1 ≤ K ≤ 10⁶, with as few
sections as possible. Print their number and the sections in the order
of a walk around the area.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The number K.

## Output

N, then N lines with fence cell coordinates, in order around the area.

## Examples

### Example 1

Input:

```
3
```

Output:

```
7
-1 0
0 1
1 2
2 1
2 0
1 -1
0 -1
```

## Solution

The fence of an area R must hold every cell next to R by a side, and
those cells already shut R in, so the task is to choose K connected
cells with the fewest side neighbours. The best shapes are diamonds or
their variants, and no K cells have fewer than ⌈√(8K − 4)⌉ + 2 neighbours: 4 for one
cell, 4r + 4 for the diamond of radius r with 2r² + 2r + 1 cells.

Build the area from rows. If the ends of consecutive rows move by at
most one cell, the fence is one cell left and one cell right of every
row plus the cells under the first row and over the last one: for H rows
it holds 2H + w₁ + w_H cells. A diamond grows by one cell at each end
per row up to its middle and shrinks after that. Fix the fence size at
the lower bound and try the first and last widths 1 or 2. That fixes H.
The widest possible rows are min(w₁ + 2i, w_H + 2(H − 1 − i)). Cap them
at the lowest level that still holds K cells, found by binary search,
then take one cell off some of the inner rows at the cap until exactly K
remain. If no choice works, the fence size goes up by one; for every K
that was tried, the lower bound itself was reached.

Then place the rows, moving the left end first when a row narrows, and
list the fence around the area: along the bottom, up the right side,
back along the top and down the left side. Consecutive sections touch by
a side or a corner. `O(√K · log K)`.

Pitfalls:

- the fence may touch only at corners, since the goat cannot move
  diagonally; a fence that touches by sides needs many more sections;
- a square is not the best shape: 1 000 000 cells need 2 831 sections,
  against 4 000 around a square;
- the order of the output matters: the cells go around the area.

The construction was checked for every K up to 3 000 and for large K by
flood filling the area from (0, 0); the bound was checked against all
polyominoes of up to 14 cells. The tests are judged by a checker that
does the same flood fill and checks the size and the order.

## Language notes

- All five solutions search the same shapes; Java builds the output
  before it knows the count, so the count is printed in front at the
  end.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1368_geometry.cpp](1368_geometry.cpp) | G++ 13.2 x64 | geometry | O(√K·log K) | AC | 0.015 s | 256 KB |
| [1368_geometry.go](1368_geometry.go) | Go 1.14 x64 | geometry | O(√K·log K) | AC | 0.031 s | 1512 KB |
| [1368_geometry.java](1368_geometry.java) | Java 1.8 | geometry | O(√K·log K) | AC | 0.109 s | 1956 KB |
| [1368_geometry.py](1368_geometry.py) | Python 3.12 x64 | geometry | O(√K·log K) | AC | 0.093 s | 1500 KB |
| [1368_geometry.rs](1368_geometry.rs) | Rust 1.75 x64 | geometry | O(√K·log K) | AC | 0.015 s | 268 KB |
