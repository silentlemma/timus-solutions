# 1301. Cube in Labyrinth

[Timus 1301](https://acm.timus.ru/problem.aspx?space=1&num=1301) · difficulty 720 · bfs

Original problem from the Second Ural Team Student Programming Championship, Yekaterinburg, April 3–4, 1998.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A cube the size of one cell stands on an X × Y field (2 ≤ X, Y ≤ 10).
One move rolls it over an edge onto a neighbouring cell; it cannot roll
through a wall or off the field. Find the fewest moves that bring the
cube from cell (A, B) to cell (C, D) with the same face on top as at
the start, or report that it is impossible.

Time limit: 1 second. Memory limit: 64 MB.

## Input

X and Y, then A and B, then C and D. Then, optionally, a line `v`
followed by pairs `N M`, each a wall between cells (N, M) and
(N + 1, M), and a line `h` followed by pairs `N M`, each a wall between
(N, M) and (N, M + 1).

## Output

The number of moves, or `No solution`.

## Examples

### Example 1

Input:

```
10 2
1 1
10 1
v
2 1
6 2
h
4 1
```

Output:

```
11
```

## Solution

The full orientation of a cube has 24 states, but only one face
matters: the one that starts on top. Where that face is now (top,
bottom, north, south, east or west) changes by a fixed rule with each
roll. Rolling east, for example, sends top to east, east to bottom,
bottom to west and west to top, and leaves north and south alone.

So the state is (cell, side of the marked face), at most
10 · 10 · 6 = 600 states, and a breadth-first search from
(A, B, top) finds the shortest way to (C, D, top). Each wall blocks
the move across it in both directions. `O(X · Y)`.

Pitfalls:

- the start may be the goal: 0 moves (test 02);
- the right cell with the wrong face up does not count. In a straight
  corridor the marked face is on top only at net displacements divisible
  by 4, so a corridor of length 2 or 3 has no solution (tests 04 and 08), while
  one of length 4 has (test 09);
- even a neighbouring cell may need a detour: 3 moves on an open
  2 × 2 field (test 03);
- either wall section may be missing.

The answers were compared with a search over all 24 orientations of a
labelled cube on 120 random fields.

## Optimized solutions

Go tracks the side holding the initial top face and processes BFS one layer at a time. Each cell stores a bit mask of visited sides and a separate mask for walls. Go 1.14 x64, submission 11322929. Time 0.015 → 0.015 s, memory 1160 → 296 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1301_bfs_optimized.java`. Retain the archived algorithm, replacing Scanner with buffered byte input. Output avoids Formatter where ordinary numeric conversion suffices. EOF is stable even without a final newline; the simple source remains unchanged.

Accepted #11328648 (Java 1.8): **0.062 s / 456 KB**. Archived comparison: `1301_bfs.java` (Java 1.8) — 0.109 s / 528 KB (#11321840).

## Language notes

- The wall sections are read word by word, so the input layout
  (line breaks, extra spaces) does not matter.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321838 · Java 1.8 №11321840 · Python 3.12 x64 №11321841 · Rust 1.75 x64 №11321842.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1301_bfs.cpp](1301_bfs.cpp) | G++ 13.2 x64 | bfs | O(X * Y) | AC | 0.015 s | 184 KB | 11321838 |
| [1301_bfs.go](1301_bfs.go) | Go 1.14 x64 | bfs | O(X * Y) | AC | 0.015 s | 1160 KB | 11322052 |
| [1301_bfs.java](1301_bfs.java) | Java 1.8 | bfs | O(X * Y) | AC | 0.109 s | 528 KB | 11321840 |
| [1301_bfs.py](1301_bfs.py) | Python 3.12 x64 | bfs | O(X * Y) | AC | 0.062 s | 648 KB | 11321841 |
| [1301_bfs.rs](1301_bfs.rs) | Rust 1.75 x64 | bfs | O(X * Y) | AC | 0.015 s | 236 KB | 11321842 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1301_bfs_optimized.go](1301_bfs_optimized.go) \* | Go 1.14 x64 | bfs | O(X * Y) | AC | 0.015 s | 296 KB | 11322929 |
| [1301_bfs_optimized.java](1301_bfs_optimized.java) | Java 1.8 | bfs | O(X * Y) | AC | 0.062 s | 456 KB | 11328648 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
