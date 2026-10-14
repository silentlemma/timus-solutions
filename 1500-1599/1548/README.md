# 1548. Sakura and Statistics

[Timus 1548](https://acm.timus.ru/problem.aspx?space=1&num=1548) · difficulty 10900 · greedy

Original problem by Sergey Pupyrev, from the Eleventh Ural Collegiate Team Programming Championship, Ekaterinburg, April 21, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A black-and-white picture of N × M pixels (1 ≤ N, M ≤ 50) is given, and the
black pixels of every column form at most one vertical run. Find the
smallest set of rectangles of black pixels whose union is exactly the
set of black pixels; rectangles may overlap. Any smallest set will do.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then N lines of M characters: `1` for black, `0` for white.

## Output

The number of rectangles, then each rectangle as the row and column of
two opposite corners, rows counted from the top.

## Examples

### Example 1

Input:

```
3 3
010
111
010
```

Output:

```
2
1 2 3 2
2 1 2 3
```

### Example 2

Input:

```
4 5
00000
11100
11010
10000
```

Output:

```
4
2 1 2 3
3 1 3 2
2 1 4 1
3 4 3 4
```

## Solution

Since each column has at most one black run of rows, the columns of an
interval [l, r) are all black exactly on the rows where all their runs
meet, again one run of rows, possibly empty. A rectangle can be
stretched to all those rows, and a rectangle is described by its
interval of columns alone.

Every row splits into maximal runs of black pixels. A set of intervals
gives a cover of the picture exactly when every such row run is the
union of the chosen intervals that lie inside it. So the task is the
smallest family of intervals that generates all the row runs this way,
and the answer is its size.

Such a family is found greedily, in the way Franzblau and Kleitman
cover vertically convex polygons. Start with the distinct row runs
and go over the right ends from left to right. A backward scan,
counting chosen intervals, finds an interval to remove. Drop it and
move the left ends of some intervals ending earlier to the right,
in decreasing order of right ends, so that every row run is still
generated. Repeat the scan at the same right end until no interval
can be removed; `O(N·M + M⁴)`, small for M ≤ 50.

Pitfalls:

- rectangles may overlap, and the best answers need it: the cross of
  the first example and the two squares of test 05 take two rectangles,
  where any partition needs three;
- a row may hold several runs, each generated on its own: row 3 of the
  second example has the runs of columns 1–2 and of column 4;
- a white picture needs no rectangles (test 03).

The counts were compared with an exhaustive search over sets of maximal
rectangles on 400 random small pictures and with an independent
accepted implementation on 300 pictures up to 50 × 50. The tests use a
checker that accepts any smallest cover.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1548_greedy.cpp](1548_greedy.cpp) | G++ 13.2 x64 | greedy | O(N·M + M⁴) | AC | 0.015 s | 220 KB |
| [1548_greedy.go](1548_greedy.go) | Go 1.14 x64 | greedy | O(N·M + M⁴) | AC | 0.031 s | 1164 KB |
| [1548_greedy.java](1548_greedy.java) | Java 1.8 | greedy | O(N·M + M⁴) | AC | 0.109 s | 516 KB |
| [1548_greedy.py](1548_greedy.py) | Python 3.12 x64 | greedy | O(N·M + M⁴) | AC | 0.093 s | 800 KB |
| [1548_greedy.rs](1548_greedy.rs) | Rust 1.75 x64 | greedy | O(N·M + M⁴) | AC | 0.046 s | 236 KB |
