# 2113. Smallest jump height to outrun a spreading flood

[Timus 2113](https://acm.timus.ru/problem.aspx?space=1&num=2113) · difficulty 432 · bfs, binary_search

Original problem by Anton Lipin, from the University Academic School Olympiad in Informatics 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A hare and water start in different cells of an n × m grid of heights.
They move in turns, the hare first. The hare stays or steps to a
side-adjacent cell at most J higher than its current one. The water
floods every cell that has a flooded neighbour at least as high. Find
the smallest jump height J for which the hare can stay out of the water
forever, or −1 if no J works. The limits are 2 seconds and 256 MB.

## Input

n and m, 1 ≤ n, m ≤ 100, n · m ≠ 1, the heights 0 ≤ hᵢⱼ ≤ 10⁵, the
hare's cell and the water's cell.

## Output

The smallest J, or −1.

## Examples

### Example 1

Input:

```
2 3
6 5 4
1 2 3
2 1
1 3
```

Output:

```
3
```

### Example 2

Input:

```
1 3
0 0 0
1 1
1 3
```

Output:

```
-1
```

## Solution

The water does not depend on the hare, so a breadth-first search from
its cell gives the move F(c) after which each cell c is flooded (cells
the water never reaches get infinity). The hare makes its k-th step
before the k-th water move and is still there during it, so it may stand
on c after k steps only if F(c) > k. Waiting never helps: arriving
earlier is never worse.

For a fixed J a second search from the hare's cell walks along allowed
steps with these deadlines. The hare survives exactly when the search
reaches a cell that is never flooded: every other cell is flooded
eventually. A larger J allows more steps, so survival is monotone in J.
If even J = 10⁵ fails the answer is −1, otherwise a binary search over J
finds the smallest one. The total time is O(n m log H).

In the first example the water from the top right corner floods the
whole bottom row but never the cells of height 5 and 6. The hare steps
from height 1 to height 2 and then climbs three units to height 5 just
before the water reaches it.

## Optimized solutions

The new Go and Rust sources preserve the water BFS and monotone binary search on jump height. Flat padded arrays use 32-bit signed heights and 16-bit flood/arrival times and queue entries. There are at most 10000 real cells and 10404 padded positions, so all identifiers and real shortest-path lengths fit; 65535 marks unreached cells. Border flood times are zero, making them fail every positive-arrival deadline without extra boundary branches. One arrival array and queue serve all survival checks; Go also avoids the old per-check allocations. Rust already reused its buffers and now packs them and streams input. The strict test arrival<flood remains: the hare moves before water, but must survive that same water turn. Reaching a permanently dry cell suffices; waiting earlier cannot improve a route. Time remains O(n·m log H), storage O(n·m). Simple files remain; C++, Java and Python reuse admitted bases in the fast set.

The accepted base implementations [2113_bfs_binary_search.cpp](2113_bfs_binary_search.cpp), [2113_bfs_binary_search.java](2113_bfs_binary_search.java), [2113_bfs_binary_search.py](2113_bfs_binary_search.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2113_bfs_binary_search.cpp](2113_bfs_binary_search.cpp) | G++ 13.2 x64 | bfs, binary_search | O(n m log H) | AC | 0.015 s | 432 KB | 11294935 |
| [2113_bfs_binary_search.go](2113_bfs_binary_search.go) | Go 1.14 x64 | bfs, binary_search | O(n m log H) | AC | 0.031 s | 3712 KB | 11294936 |
| [2113_bfs_binary_search.java](2113_bfs_binary_search.java) \* | Java 1.8 | bfs, binary_search | O(n m log H) | AC | 0.125 s | 648 KB | 11294938 |
| [2113_bfs_binary_search.py](2113_bfs_binary_search.py) \* | Python 3.12 x64 | bfs, binary_search | O(n m log H) | AC | 0.125 s | 2492 KB | 11294937 |
| [2113_bfs_binary_search.rs](2113_bfs_binary_search.rs) | Rust 1.75 x64 | bfs, binary_search | O(n m log H) | AC | 0.046 s | 364 KB | 11294939 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2113_bfs_binary_search_optimized.go](2113_bfs_binary_search_optimized.go) \* | Go 1.14 x64 | bfs, binary_search | O(n·m log H) | AC | 0.031 s | 364 KB | 11315082 |
| [2113_bfs_binary_search_optimized.rs](2113_bfs_binary_search_optimized.rs) \* | Rust 1.75 x64 | bfs, binary_search | O(n·m log H) | AC | 0.031 s | 164 KB | 11315092 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
