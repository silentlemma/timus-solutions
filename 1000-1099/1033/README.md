# 1033. The visible wall area of a maze

[Timus 1033](https://acm.timus.ru/problem.aspx?space=1&num=1033) · difficulty 237 · bfs, bitmask, dfs, graphs

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

Compare one integer token. New Rust passed 569 native executions against a separate cell BFS oracle: all 128 free-corner 3x3 labyrinths, random boards, sides 31/32/33, both separate and shared entrance components, whitespace/chunk boundaries and 11 repository inputs.

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

A visible wall face is exactly a side of an entrance-reachable empty
cell facing a stone block or the outer boundary. Run a four-neighbor flood
fill from both entrance cells. Mark on insertion so a cell shared by both
components is visited only once. For every reached cell count each side
facing `#` or leaving the board; ignore sides facing another empty cell.

This enumerates precisely the visible faces: each has one incident empty
cell, and that cell must be reachable. Counting different sides of one
stone block is correct. Closed rooms are excluded. Subtract the four
outside sides at the two entrance corners, since these are openings,
then multiply by 9 for a face of width 3 m and height 3 m.

The C++, Go, Java and Rust bases use a cell queue; Python uses a stack.
Their order changes neither the reachable set nor the face count.
Each empty cell is inserted at most once and has four neighbors, giving
`O(N²)` time and storage. Only shared sides allow movement: diagonal
touching leaves no passage. The two entrances can be disconnected.

## Optimized solutions

The retained C++/Java/Python row-mask algorithms group horizontal cell operations into bounded-width word operations; Python's old full-input token storage still contributes quadratic storage. The original cell BFS/DFS programs remain as teaching sources.

Rust uses an allocation-free row-mask flood fill. Seed both entrances. On a changed row, close the reachable mask horizontally within open cells, then send newly reached bits to the adjacent rows. A queued-row bitset prevents duplicates; a fixed circular queue and an explicit count support even all N rows queued at once. Every scheduled row has gained a cell, and each horizontal expansion gains a cell, so at most `O(N²)` word operations are charged to the N² cells. N≤33 makes every row one 64-bit word. Count the four wall directions with bit counts, include the outer boundary and subtract the four entrance faces before multiplying by nine. This counts the union of both reachable components once. Only masks, row indices and a 128-byte input buffer are retained. POSIX read/write handle bounded buffers directly, without stdio heap buffers or formatting; the output number is converted into a fixed byte array. All reads, shifts and indices respect the stated side bound.

- `1033_graphs_bitmask.cpp`: 0.001 s / 112 KB; base `1033_bfs.cpp`: 0.001 s / 416 KB; relative change: time -0.0%, memory -73.1%.
- `1033_graphs_bitmask.java`: 0.078 s / 376 KB; base `1033_bfs.java`: 0.125 s / 1644 KB; relative change: time -37.6%, memory -77.1%.
- `1033_graphs_bitmask.py`: 0.046 s / 576 KB; base `1033_dfs.py`: 0.078 s / 452 KB; relative change: time -41.0%, memory +27.4%.
- `1033_graphs_bitmask.rs`: 0.015 s / 140 KB; base `1033_bfs.rs`: 0.015 s / 228 KB; relative change: time -0.0%, memory -38.6%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1033_bfs.cpp`; covering source `1033_graphs_bitmask.cpp`; time/memory places 1/3, other-author entries 119/119.

- Go: preferred teaching base `1033_bfs.go`; covering source `1033_bfs.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1033_bfs.java`; covering source `1033_graphs_bitmask.java`; time/memory places 1/1, other-author entries 7/7.

- Python/PyPy: preferred teaching base `1033_dfs.py`; covering source `1033_graphs_bitmask.py`; time/memory places 2/2, other-author entries 29/29.

- Rust: preferred teaching base `1033_bfs.rs`; covering source `1033_graphs_bitmask.rs`; time/memory places 1/1, other-author entries 2/2.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1033_bfs.cpp](1033_bfs.cpp) | G++ 13.2 x64 | bfs | O(N^2) time and total space | AC | 0.001 s | 416 KB | 11278438 |
| [1033_bfs.go](1033_bfs.go) | Go 1.14 x64 | bfs | O(N^2) time and total space | AC | 0.015 s | 1124 KB | 11278439 |
| [1033_bfs.java](1033_bfs.java) | Java 1.8 | bfs | O(N^2) time and total space | AC | 0.125 s | 1644 KB | 11278443 |
| [1033_dfs.py](1033_dfs.py) | Python 3.12 x64 | dfs | O(N^2) time and total space | AC | 0.078 s | 452 KB | 11278441 |
| [1033_bfs.rs](1033_bfs.rs) | Rust 1.75 x64 | bfs | O(N^2) time and total space | AC | 0.015 s | 228 KB | 11278445 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1033_graphs_bitmask.cpp](1033_graphs_bitmask.cpp) | G++ 13.2 x64 | graphs, bitmask | O(N^2) time and total space | AC | 0.001 s | 112 KB | 11308624 |
| [1033_graphs_bitmask.java](1033_graphs_bitmask.java) | Java 1.8 | graphs, bitmask | O(N^2) time and total space | AC | 0.078 s | 376 KB | 11308630 |
| [1033_graphs_bitmask.py](1033_graphs_bitmask.py) \* | Python 3.12 x64 | graphs, bitmask | O(N^2) time and total space | AC | 0.046 s | 576 KB | 11308634 |
| [1033_graphs_bitmask.rs](1033_graphs_bitmask.rs) | Rust 1.75 x64 | graphs, bitmask | O(N^2) time; O(N) masks/buffer | AC | 0.015 s | 140 KB | 11309560 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
