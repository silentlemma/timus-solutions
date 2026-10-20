# 2200. How many separate boards a knight can visit

[Timus 2200](https://acm.timus.ru/problem.aspx?space=1&num=2200) · difficulty 1651 · dsu, sorting

Original problem by Vadim Barinov, from the University Academic School Olympiad in Informatics 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N rectangular boards, each at least 3 × 3, lie on a grid without
touching, not even at corners. A knight stands on one cell and may move
within a board or jump between boards in one move. Count the boards it
can visit, its own included. The limits are 4 seconds and 256 MB.

## Input

N and M, 1 ≤ N ≤ 5 · 10⁴, 2 ≤ M ≤ 10⁹, then the knight's cell, then
each board as its lower left and upper right corners, all coordinates
up to M in absolute value.

## Output

The number of boards.

## Examples

### Example 1

Input:

```
4 12
0 0
0 0 3 3
5 0 8 3
0 4 8 7
9 8 12 11
```

Output:

```
3
```

### Example 2

Input:

```
2 10
-1 -1
-2 -2 1 1
-2 2 1 5
```

Output:

```
1
```

## Solution

Inside a board of at least 3 × 3 the knight reaches every cell, with one
exception: the center of a 3 × 3 board has no move at all. If the knight
starts there, the answer is 1; otherwise its whole board is reachable,
and no jump from outside can land on such a center.

Two boards are one jump apart only when they are separated by exactly
one empty column and their closed spans of rows meet, or by exactly one
empty row and their closed spans of columns meet. A knight move changes
one coordinate by 2 and the other by 1. Crossing a gap of g columns
needs a change of g + 1 ≤ 2 in x, and since the boards do not touch,
g = 1, so x changes by 2 and y by 1, which is possible exactly when the
row spans, as closed intervals, share a point. The diagonal cases are
covered too, since a gap of one row with columns meeting at a single
line is the second case.

So the boards form a graph, and the answer is the size of the start's
component in a disjoint set union. To find the edges, every right side
at x = R is matched with every left side at x = R + 1: the events are
sorted by line and then by the start of their interval, and since sides
of one kind on one line never overlap, each interval only has to be
compared with the most recent interval of the other kind. The same
sweep runs for the horizontal sides.

In the first example the two small boards both reach the long board
above them across one empty row, while the last board lies
diagonally with a gap in both directions.

Sorting makes it O(N log N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2200_dsu_sorting.cpp](2200_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(N log N) | AC | 0.062 s | 2888 KB |
| [2200_dsu_sorting.go](2200_dsu_sorting.go) | Go 1.14 x64 | dsu, sorting | O(N log N) | AC | 0.140 s | 14944 KB |
| [2200_dsu_sorting.java](2200_dsu_sorting.java) | Java 1.8 | dsu, sorting | O(N log N) | AC | 0.218 s | 11824 KB |
| [2200_dsu_sorting.py](2200_dsu_sorting.py) | Python 3.12 x64 | dsu, sorting | O(N log N) | AC | 0.500 s | 26580 KB |
| [2200_dsu_sorting.rs](2200_dsu_sorting.rs) | Rust 1.75 x64 | dsu, sorting | O(N log N) | AC | 0.046 s | 12828 KB |
