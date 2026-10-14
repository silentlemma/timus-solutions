# 1609. Tram Tiles

[Timus 1609](https://acm.timus.ru/problem.aspx?space=1&num=1609) · difficulty 2916 · constructive

Original problem by Sergey Pupyrev, from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An n × m area (1 ≤ n, m ≤ 10, nm even) is to be covered with 1 × 2 tiles.
The foreman lays a few tiles first so that the rest of the covering can
be finished in exactly one way. Find the least number of tiles to lay
and show one such start: the cells covered by them as `1`, the rest as
`0`. Any optimal start is accepted.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

n and m.

## Output

The number of tiles, then n rows of m characters.

## Examples

### Example 1

Input:

```
4 4
```

Output:

```
2
1100
0110
0000
0000
```

### Example 2

Input:

```
2 5
```

Output:

```
2
11110
00000
```

## Solution

This is the minimum forcing number of domino tilings of a grid. There
are only 75 boards, so the answers are found once in advance by search
and stored in the program: 40 patterns, one for every n ≤ m, turned on
its side for n > m. [1609_constructive_table.py](1609_constructive_table.py)
runs this search and prints them.

The search rests on a quick test. A nonempty bipartite graph with exactly
one perfect matching always has a vertex of degree 1, so
the free cells have a unique tiling exactly when repeatedly covering a
cell that has only one free neighbour uses up all of them. For k = 0,
1, 2, … sets of k non-overlapping tiles are tried, testing both the free
and the laid cells. Minimality for the original task is checked separately
using only the free cells; the minima agree on all 40 boards. The largest
board, 10 × 10, needs 5 tiles.

The stored patterns also make the laid cells themselves tile in only
one way, so the picture of `1` and `0` fixes the whole covering under
any reading. The answers for squares agree with the theorem of Pachter
and Kim that a 2k × 2k board needs k tiles.

The tests use a checker that verifies the number of tiles, that the
marked cells can be covered by that many tiles, and that the free cells
have exactly one tiling.

Pitfalls:

- a 1 × m strip already has only one tiling, so the answer is 0 and the
  grid is all zeros (tests 03, 05 and 06);
- narrow boards are harder: 2 × 8 needs 3 tiles while 3 × 8 needs 2
  (tests 07 and 09);
- the output does not show how the laid tiles lie, only the cells they
  cover; patterns whose covered cells tile in a single way avoid any
  doubt.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1609_constructive.cpp](1609_constructive.cpp) | G++ 13.2 x64 | constructive | O(nm) | AC | 0.015 s | 196 KB |
| [1609_constructive.go](1609_constructive.go) | Go 1.14 x64 | constructive | O(nm) | AC | 0.031 s | 1120 KB |
| [1609_constructive.java](1609_constructive.java) | Java 1.8 | constructive | O(nm) | AC | 0.140 s | 1684 KB |
| [1609_constructive.py](1609_constructive.py) | Python 3.12 x64 | constructive | O(nm) | AC | 0.093 s | 724 KB |
| [1609_constructive.rs](1609_constructive.rs) | Rust 1.75 x64 | constructive | O(nm) | AC | 0.062 s | 224 KB |
