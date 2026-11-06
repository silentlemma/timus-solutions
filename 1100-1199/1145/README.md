# 1145. The longest path between two cells of a tree-shaped maze

[Timus 1145](https://acm.timus.ru/problem.aspx?space=1&num=1145) · difficulty 344 · bfs

Original problem on Timus; its author and source are not given.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A maze of `n × m` cells, `3 ≤ n, m ≤ 820`, has free cells (`.`) and walls
(`#`); moves go between free cells that share a side, and between any two
free cells there is exactly one path. A thread will be tied between two
free cells that are not known in advance. Find the shortest thread that
is long enough for any two free cells, that is the longest of all those
paths.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`n` (the width) and `m` (the height), then `m` rows of `n` characters.

## Output

The length of the thread in cell sides.

## Examples

### Example 1

Input:

```
7 6
#######
#.#.###
#.#.###
#.#.#.#
#.....#
#######
```

Output:

```
8
```

## Solution

The free cells with their shared sides form a tree, and the answer is the
diameter of that tree. Two breadth-first searches find it: from any free
cell, the farthest cell `u` is an end of some longest path; from `u`, the
farthest cell is the other end, and its distance is the answer.

Why the first search lands on an end: let `a … b` be a longest path and
`u` the farthest cell from the start `s`. The path from `s` to `u` meets
the path `a … b` (or the way to it), and if `u` were not at least as far
from that meeting point as `a` or `b`, one of them would be farther from
`s` than `u`. So replacing one end of `a … b` by `u` gives a path no
shorter.

The grid gets a border of walls, so every cell has four neighbours in the
array, and cells are numbered `r·(n + 2) + c`. A search is `O(n·m)`.

Pitfalls:

- the maze has up to 672400 cells, so the search uses a flat array and an
  explicit queue, not recursion;
- the first number is the width and the second the height;
- free cells may lie on the edge of the maze, which the border of walls
  takes care of.

The answers were compared with a breadth-first search from every free
cell on 120 small random mazes, which also checked that the free cells
form a tree.

## Optimized solutions

The C++ depth-first version still finds the diameter with two searches. A tree has one path between any two cells, so the current depth gives the distance from the starting cell. While descending, store the direction back to the parent in the current cell byte. On ascent, restore that byte and resume the next direction at the parent. This keeps the O(n·m) time bound and uses O(1) extra space beyond the grid. The Accepted run used 772 KB instead of 6112 KB and took 0.015 s instead of 0.046 s.

The accepted base implementations [1145_bfs.go](1145_bfs.go), [1145_bfs.java](1145_bfs.java), [1145_bfs.py](1145_bfs.py), [1145_bfs.rs](1145_bfs.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- All languages run the same two searches over a padded flat grid.
- Python takes about a quarter of a second on the largest mazes in our
  runs, but under CPython 3.12 on Timus it exceeds the 0.5 s limit on
  test 9 (0.515 s); the same file is accepted under PyPy 3.10 in
  0.218 s, so the Python solution passes only under PyPy.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1145_bfs.cpp](1145_bfs.cpp) | G++ 13.2 x64 | bfs | O(n·m) | AC | 0.046 s | 6112 KB | 11279477 |
| [1145_bfs.go](1145_bfs.go) | Go 1.14 x64 | bfs | O(n·m) | AC | 0.062 s | 21300 KB | 11279478 |
| [1145_bfs.java](1145_bfs.java) \* | Java 1.8 | bfs | O(n·m) | AC | 0.125 s | 9544 KB | 11279482 |
| [1145_bfs.py](1145_bfs.py) \* | PyPy 3.10 x64 | bfs | O(n·m) | AC | 0.218 s | 11572 KB | 11279480 |
| [1145_bfs.rs](1145_bfs.rs) | Rust 1.75 x64 | bfs | O(n·m) | AC | 0.031 s | 9556 KB | 11279485 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1145_dfs.cpp](1145_dfs.cpp) | G++ 13.2 x64 | dfs | O(n·m) | AC | 0.015 s | 772 KB | 11310346 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
