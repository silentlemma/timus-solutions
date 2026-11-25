# 1212. Places for one more ship in battleship

[Timus 1212](https://acm.timus.ru/problem.aspx?space=1&num=1212) · difficulty 493 · geometry

Original problem by Anton Botov and Anatoly Uglov, from the USU Open Collegiate Programming Contest, October 2002, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A battleship board has `N` rows and `M` columns, both up to 30000, and up
to 30 ships of one to four cells already stand on it. Ships may not touch
each other, not even at a corner. Count the ways to place one more ship
of `K` cells, horizontally or vertically.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, `M` and the number of ships `L`; then each ship as the column and
row of its top left cell, its length and `V` or `H`; then `K`.

## Output

The number of places for the new ship.

## Examples

### Example 1

Input:

```
4 4 2
1 2 2 V
3 1 2 H
2
```

Output:

```
4
```

## Solution

Every placed ship forbids the rectangle around it, one cell wider on
every side. Count the horizontal places first. The rows split into bands
at the top edge and just below the bottom edge of every forbidden
rectangle; inside a band every row meets the same rectangles, so all its
rows have the same count. For one row of a band, take the forbidden
column ranges in order and add `max(0, length − K + 1)` for every free
stretch between them; multiply by the height of the band. The vertical
places are the same count on the board turned on its side. A ship of one
cell is the same either way, so then only one count is taken. With at
most 61 bands, `O(L² log L)`.

Pitfalls:

- the first number of a ship is its column and the second its row;
- a one-cell ship must not be counted twice;
- forbidden rectangles extend past the board; ignore out-of-board cuts
  when splitting rows into bands;
- the answer can reach about `1.8·10⁹`, within signed 32-bit integers.

The answers were compared with a brute force over every cell on 450
random small boards, and with a separately written solution on every
test.

The teaching Python version counts forbidden starting cells directly. For a horizontal placement, expand each existing ship’s forbidden rectangle by K − 1 columns to the left and clip to the legal starts. Insert each resulting starting cell into a set so overlaps count once. Subtract the set size from all possible starts. Transpose for vertical placements, except when K = 1. Each existing ship contributes at most 36 cells per orientation, giving expected O(L) time and O(L) space.

## Optimized solutions

C++, Go and Rust count forbidden starting cells. For horizontal placements, extend each forbidden rectangle K − 1 columns to the left and clip to the legal starting cells. Each existing ship contributes at most 36 cells. Encode each as (row − 1)M + column − 1, sort the IDs and count the distinct ones. Transpose the board to count vertical placements.

The memory-optimized PyPy version counts forbidden final cells. A horizontal ship ending in column x meets a forbidden interval [a,b] exactly when x ≥ a and x − K + 1 ≤ b. Sort the forbidden rectangles once by their left boundaries. Extend their right edges by K − 1 for horizontal placements or their bottom edges for vertical placements, then clip to the legal final cells. For each affected row, store the farthest covered endpoint and subtract only newly covered cells from the total. Each rectangle touches at most nine rows. Both approaches count K = 1 once and use O(L log L) time and O(L) space.

The accepted PyPy 3.10 x64 run takes 0.14 s versus 0.078 s for the base and uses 340 KB versus 684 KB.

The accepted base implementations [1212_geometry.java](1212_geometry.java) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

C++, Go and Rust sort encoded starts in fixed arrays. Go stores the IDs in uint32 and uses standard handles with fixed buffers. PyPy keeps one right endpoint per affected row and uses the same rectangle order for both directions. Java keeps its original row-band implementation.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1212_geometry.cpp](1212_geometry.cpp) | G++ 13.2 x64 | geometry | O(L² log L) | AC | 0.031 s | 432 KB | 11283646 |
| [1212_geometry.go](1212_geometry.go) | Go 1.14 x64 | geometry | O(L² log L) | AC | 0.031 s | 1144 KB | 11283647 |
| [1212_geometry.java](1212_geometry.java) \* | Java 1.8 | geometry | O(L² log L) | AC | 0.140 s | 1940 KB | 11283649 |
| [1212_geometry.py](1212_geometry.py) | Python 3.12 x64 | geometry | O(L² log L) | AC | 0.078 s | 684 KB | 11283648 |
| [1212_geometry.rs](1212_geometry.rs) | Rust 1.75 x64 | geometry | O(L² log L) | AC | 0.046 s | 232 KB | 11283650 |
| [1212_hashing.py](1212_hashing.py) | Python 3.12 x64 | hashing | O(L) expected | AC | 0.093 s | 580 KB | 11315800 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1212_sorting.cpp](1212_sorting.cpp) | G++ 13.2 x64 | sorting | O(L log L) | AC | 0.015 s | 124 KB | 11315806 |
| [1212_sorting.rs](1212_sorting.rs) | Rust 1.75 x64 | sorting | O(L log L) | AC | 0.015 s | 220 KB | 11315821 |
| [1212_sorting.go](1212_sorting.go) \* | Go 1.14 x64 | sorting | O(L log L) | AC | 0.015 s | 308 KB | 11315959 |
| [1212_sorting.py](1212_sorting.py) | PyPy 3.10 x64 | sorting | O(L log L) | AC | 0.14 s | 340 KB | 11316273 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
