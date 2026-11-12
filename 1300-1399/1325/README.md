# 1325. Dirt

[Timus 1325](https://acm.timus.ru/problem.aspx?space=1&num=1325) · difficulty 533 · bfs

Original problem: idea by Stanislav Vasiliev, prepared by Stanislav Vasiliev and Pavel Egorov, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A flat is an N × M grid (N, M ≤ 500) of clean cells (1), dirty cells (2)
and walls (0). From a cell one may step to any of the eight cells that
share a corner with it, and every step between a clean and a dirty cell
means changing shoes. Find a way from the computer to the fridge with
the fewest changes of shoes and, among those, the fewest cells. Print
its length in cells, counting both ends, and the number of changes, or
0 0 if the fridge cannot be reached.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N and M, the row and column of the computer, the row and column of the
fridge, then N rows of M digits. The top left cell is (1, 1).

## Output

The length of the way in cells and the number of changes.

## Examples

### Example 1

Input:

```
3 7
1 1
3 7
1200121
1212020
1112021
```

Output:

```
8 4
```

### Example 2

Input:

```
5 5
1 5
5 1
00001
00000
00000
00000
20000
```

Output:

```
0 0
```

## Solution

The cost of a way is the pair (changes, steps), compared first by
changes. Every change switches between clean and dirty, so all cells
first reached after exactly c changes are of the same kind: the kind of
the start if c is even, the other one if c is odd. That splits the
search into layers c = 0, 1, 2, ….

Inside layer c an ordinary breadth-first search over cells of that kind
gives the fewest steps. Its starting cells, the seeds, are the cells of
this kind next to layer c − 1, each with the step count at which it was
first touched. Layer c − 1 was handled in order of steps, so the seeds
already come sorted by steps. The search then goes level by level: at
each step count it first takes in the seeds of that count that have
not been reached yet, then expands the cells of the level. A cell of
the other kind that is touched becomes a seed for layer c + 1 only the
first time in this layer, which is also its smallest step count. The
first layer that reaches the fridge gives the answer. Each cell is
finalized once and looks at eight neighbours, `O(N · M)`.

Pitfalls:

- moves go along diagonals too (test 05);
- fewer changes win over a shorter way: a clean detour of 9 cells beats
  a straight way of 7 with two changes (test 06);
- the computer and the fridge can be in the same cell: 1 0 (test 03);
- without the once-per-layer rule a cell can be queued as a seed up to
  eight times, which costs too much memory on a 500 × 500 flat.

The answers were compared with Dijkstra's algorithm on (changes, steps)
on 500 random flats of up to 8 × 8 cells.

The teaching C++ version runs Dijkstra directly on pairs (changes, steps). A move adds (0,1) on the same surface or (1,1) when it changes. Lexicographic order is preserved when the same pair is added, and every move increases the cost, so the first current entry for the target gives its optimal pair. Add one to the steps to count the starting cell. A frame of walls allows the same eight offsets at every cell. With V=N·M, the grid has O(V) edges, so the heap takes O(V log V) time and O(V) space.

## Optimized solutions

Go separates the two objectives into two passes. First, 0–1 BFS finds the minimum shoe changes to every reachable cell. Moving on the same floor type costs 0 and changing type costs 1. When processing distance d, a newly queued cell receives d or d + 1. Its label can only decrease once before it is settled, from d + 1 to d. A circular deque with 2NM + 1 uint32 slots therefore suffices. Next, unit BFS uses only edges u→v satisfying changes[v]=changes[u]+edgeCost. Along such a path, costs telescope to the minimum changes of its endpoint. Every minimum-change path has minimum-change prefixes, otherwise replacing a prefix improves the whole path. Therefore unit BFS on these edges minimizes length among exactly the minimum-change routes. Reuse the deque as its FIFO, store one uint32 change label per padded cell and reuse a bit in the byte grid for visitation. A wall frame removes bounds checks; all eight touching neighbors, including diagonal corner passage, are allowed. Count the starting cell, handle equal endpoints as 1 0, and unreachable as 0 0. Time and space are O(NM), without dynamic per-layer seed records or a separate step-distance array. All simple sources remain; other families reuse admitted bases.

The accepted base implementations [1325_bfs.cpp](1325_bfs.cpp), [1325_bfs.java](1325_bfs.java), [1325_bfs.py](1325_bfs.py), [1325_bfs.rs](1325_bfs.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

New Go uses typed compact buffers and bounded integer I/O; original Go keeps the one-pass layered lexicographic algorithm. Other original ports retain their own algorithms and receipts. The preserved Python file keeps its actual Accepted PyPy3.10 interpreter.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1325_bfs.cpp](1325_bfs.cpp) | G++ 13.2 x64 | bfs | O(N·M) | AC | 0.031 s | 3860 KB | 11284971 |
| [1325_bfs.go](1325_bfs.go) | Go 1.14 x64 | bfs | O(N·M) | AC | 0.078 s | 17476 KB | 11284972 |
| [1325_bfs.java](1325_bfs.java) | Java 1.8 | bfs | O(N·M) | AC | 0.156 s | 9092 KB | 11284974 |
| [1325_bfs.py](1325_bfs.py) | PyPy 3.10 x64 | bfs | O(N·M) | AC | 0.250 s | 16492 KB | 11284973 |
| [1325_bfs.rs](1325_bfs.rs) | Rust 1.75 x64 | bfs | O(N·M) | AC | 0.046 s | 7628 KB | 11284975 |
| [1325_dijkstra.cpp](1325_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(N·M log(N·M)) | AC | 0.046 s | 4500 KB | 11315868 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1325_graphs_bfs.go](1325_graphs_bfs.go) \* | Go 1.14 x64 | graphs, bfs | O(N·M) | AC | 0.031 s | 3572 KB | 11315686 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
