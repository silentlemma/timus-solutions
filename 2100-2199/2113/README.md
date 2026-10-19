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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2113_bfs_binary_search.cpp](2113_bfs_binary_search.cpp) | G++ 13.2 x64 | bfs, binary_search | O(n m log H) | AC | 0.015 s | 432 KB |
| [2113_bfs_binary_search.go](2113_bfs_binary_search.go) | Go 1.14 x64 | bfs, binary_search | O(n m log H) | AC | 0.031 s | 3712 KB |
| [2113_bfs_binary_search.java](2113_bfs_binary_search.java) | Java 1.8 | bfs, binary_search | O(n m log H) | AC | 0.125 s | 648 KB |
| [2113_bfs_binary_search.py](2113_bfs_binary_search.py) | Python 3.12 x64 | bfs, binary_search | O(n m log H) | AC | 0.125 s | 2492 KB |
| [2113_bfs_binary_search.rs](2113_bfs_binary_search.rs) | Rust 1.75 x64 | bfs, binary_search | O(n m log H) | AC | 0.046 s | 364 KB |
