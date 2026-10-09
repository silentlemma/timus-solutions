# 1033. The visible wall area of a maze

[Timus 1033](https://acm.timus.ru/problem.aspx?space=1&num=1033) · difficulty 237 · bfs, dfs

Original problem by Vladimir Pinaev, from the Third Ural Collegiate Team Programming Championship, 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A maze is an `N × N` grid (`3 ≤ N ≤ 33`) of 3 × 3-metre cells: `.` is
empty and `#` is a solid block. The maze is surrounded by an outer wall,
except at the upper left and lower right cells, which are the two entrances
(always empty). Walls are 3 metres high. A visitor walks between empty cells
that share a side; blocks touching at a corner leave no gap. Find the total
area of the wall surfaces a visitor can see from the parts of the maze
reachable from the entrances.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines of `N` characters `.` and `#`.

## Output

The visible wall area in square metres.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
....
.##.
.#..
....
```

Output:

```
180
```

### Example 2

Input:

```
3
...
...
...
```

Output:

```
72
```

## Solution

A wall surface is seen exactly when it is a side of a reachable empty cell
that faces a block or the outer wall. Each such side is a 3 × 3 square, so
the answer is `9 ·` (the number of such sides).

Run a BFS (or DFS) over empty cells, moving through shared sides, starting
from **both** entrances at once — they may lead to different parts of the
maze. For every visited cell look at its four sides: a side towards a `#`
or past the border is a visible wall, a side towards an empty cell is
followed. Finally, subtract the 4 sides that are openings: above and to the
left of the upper left cell, below and to the right of the lower right one.
`O(N^2)`.

Pitfalls:

- only the cells reachable from an entrance count; closed rooms are not
  seen;
- start from both entrances: the maze may be split in two;
- diagonal neighbours are not connected.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: BFS with a queue.
- **Python**: the same search with a stack (DFS); the order does not matter.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1033_bfs.cpp](1033_bfs.cpp) | G++ 13.2 x64 | bfs | O(N^2) | AC | 0.001 s | 416 KB |
| [1033_bfs.go](1033_bfs.go) | Go 1.14 x64 | bfs | O(N^2) | AC | 0.015 s | 1124 KB |
| [1033_bfs.java](1033_bfs.java) | Java 1.8 | bfs | O(N^2) | AC | 0.125 s | 1644 KB |
| [1033_bfs.rs](1033_bfs.rs) | Rust 1.75 x64 | bfs | O(N^2) | AC | 0.015 s | 228 KB |
| [1033_dfs.py](1033_dfs.py) | Python 3.12 x64 | dfs | O(N^2) | AC | 0.078 s | 452 KB |
