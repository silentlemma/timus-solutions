# 1221. The largest black square with a white diamond inside

[Timus 1221](https://acm.timus.ru/problem.aspx?space=1&num=1221) · difficulty 424 · implementation

Original problem by Nikita Shamgunov, from the Seventh Ural State University Collegiate Programming Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A sheet of `N × N` cells, `N ≤ 100`, is painted black (1) and white (0).
Cut out the largest square, sides along the grid, that is black except
for a white square turned by 45 degrees whose corners touch the middles
of its sides. Print its size, or `No solution`. The input holds several
sheets and ends with `0`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

For each sheet `N` and `N` rows of cells; then `0`.

## Output

For each sheet, the size of the largest such figure or `No solution`.

## Examples

### Example 1

Input:

```
6
1 1 0 1 1 0
1 0 0 0 1 1
0 0 0 0 0 0
1 0 0 0 1 1
1 1 0 1 1 1
0 1 1 1 1 1
4
1 0 0 1
0 0 0 0
0 0 0 0
1 0 0 1
0
```

Output:

```
5
No solution
```

## Solution

The white diamond has a centre cell and reaches the middle of every side,
so the figure has an odd size `2r + 1` with `r ≥ 1`: a cell at offsets
`(d, e)` from the centre is white exactly when `|d| + |e| ≤ r`. Row `d`
of the figure is therefore `|d|` black cells, a white run of
`2(r − |d|) + 1` cells and `|d|` black cells again, and with prefix sums
of black cells along every row each row is checked in constant time.

Try the radii from the largest down and, for each, every centre; the
first figure found is the answer. Most candidates fail at once on three
single cells (the centre and the top tip must be white, the top left
corner black), and the rest usually fail on the first row checked.
`O(N⁴)` at worst, far less in practice.

Pitfalls:

- a single white cell is not a figure: the diamond needs room inside a
  black square, so the smallest figure is 3 × 3;
- figures have odd sizes only;
- several sheets follow each other until the `0`.

The answers were compared with a separately written solution on 300
files of random, planted and uniform sheets.

## Optimized solutions

The new Go algorithm counts white cells with two 2D prefix-sum tables: one in the original grid and one after u=row+column, v=row−column+N−1. A radius-r diamond becomes an axis-aligned rectangle in the transformed grid; unused parity positions contain zeros. It contains exactly A=2r(r+1)+1 actual cells. Require A white cells in that rectangle and exactly A in the surrounding (2r+1)-square. The first condition makes the entire diamond white; the second makes every other square cell black. Both queries cost O(1), so all candidate centres and radii take O(N³), after O(N²) preprocessing, with O(N²) storage. Counts are at most 10000 and fit uint16. The original O(N⁴) row-checking bases remain; the four other admitted bases also cover the fast set.

The accepted Go 1.14 x64 run takes 0.031 s versus 0.001 s for the base and uses 352 KB versus 2116 KB.

The accepted base implementations [1221_implementation.cpp](1221_implementation.cpp), [1221_implementation.java](1221_implementation.java), [1221_implementation.py](1221_implementation.py), [1221_implementation.rs](1221_implementation.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1221_implementation_optimized.py`. Store grid rows as bytes and row-prefix counts in compact byte arrays. Stream successive grids while retaining the original largest-figure search and its acceptance conditions. The standalone program flushes both output streams before os._exit(0), avoiding interpreter teardown after the complete answer has been written. This changes process shutdown, not the mathematical algorithm; the simple version remains available.

Accepted #11328771 (Python 3.12 x64): **0.156 s / 924 KB**. Archived comparison: `1221_implementation.py` (Python 3.12 x64) — 0.14 s / 1908 KB (#11283692).

## Language notes

These notes describe the simple implementations.

- All languages read the cells one digit at a time, so rows written with
  or without spaces both work.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1221_implementation.cpp](1221_implementation.cpp) | G++ 13.2 x64 | implementation | O(N⁴) | AC | 0.015 s | 316 KB | 11283690 |
| [1221_implementation.go](1221_implementation.go) | Go 1.14 x64 | implementation | O(N⁴) | AC | 0.001 s | 2116 KB | 11283691 |
| [1221_implementation.java](1221_implementation.java) | Java 1.8 | implementation | O(N⁴) | AC | 0.062 s | 936 KB | 11283693 |
| [1221_implementation.py](1221_implementation.py) | Python 3.12 x64 | implementation | O(N⁴) | AC | 0.140 s | 1908 KB | 11283692 |
| [1221_implementation.rs](1221_implementation.rs) | Rust 1.75 x64 | implementation | O(N⁴) | AC | 0.031 s | 500 KB | 11283694 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1221_prefix_sums.go](1221_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N³) | AC | 0.031 s | 352 KB | 11314933 |
| [1221_implementation_optimized.py](1221_implementation_optimized.py) | Python 3.12 x64 | implementation | O(N⁴) | AC | 0.156 s | 924 KB | 11328771 |
