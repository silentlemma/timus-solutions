# 1004. Shortest cycle in an undirected multigraph

[Timus 1004](https://acm.timus.ru/problem.aspx?space=1&num=1004) · difficulty 580 · shortest_paths, graphs

Original problem from the Central European Olympiad in Informatics 1999.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An undirected graph has `N` vertices (`3 ≤ N ≤ 100`) and `M` edges
(`3 ≤ M ≤ N·(N-1)`) with positive integer lengths `1 ≤ l ≤ 300`. There may be
several edges between the same pair of vertices, but no loops.

Find a simple cycle with at least 3 vertices and the smallest total length:
distinct vertices `x1, ..., xk` (`k ≥ 3`) such that `x1-x2, ..., x(k-1)-xk` and
`xk-x1` are edges. Its length is the sum of the lengths of these edges. Report
if there is no such cycle.

The input holds `T ≤ 5` such tests.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

Tests one after another. A test is a line `N M` and `M` lines `a b l`: an edge
between `a` and `b` (`a ≠ b`) of length `l`. A line `-1` ends the input.

## Output

For every test, one line: the vertices `x1 ... xk` of a shortest cycle in
order, separated by single spaces, or `No solution.` if the graph has no
cycle with at least 3 vertices.

## Checking

Any shortest cycle, starting anywhere and in either direction, is accepted:
the checker verifies that the vertices are distinct, that consecutive ones are
joined by edges, and that the total length is minimal.

## Examples

### Example 1

Input:

```
5 7
1 2 2
2 3 2
3 1 2
3 4 1
4 5 1
5 3 1
1 5 10
4 3
1 2 5
2 3 5
3 4 5
-1
```

Output:

```
4 5 3
No solution.
```

### Example 2

Input:

```
3 3
1 2 1
1 2 1
2 1 3
-1
```

Output:

```
No solution.
```

## Solution

Only the shortest edge between two vertices matters, so keep a matrix of the
lightest direct edges; parallel edges alone never form a valid cycle (it
needs 3 distinct vertices).

Run Floyd-Warshall, and just before vertex `k` is allowed as an intermediate
vertex, look at all pairs `i < j < k` joined to `k` by edges: at that moment
`dist[i][j]` is the shortest path between `i` and `j` through vertices below
`k` only, so the path plus the edges `j-k` and `k-i` is a simple cycle in
which `k` is the largest vertex. Every simple cycle is found this way when its
largest vertex is processed, so the minimum over all candidates is the
answer. Keeping a `next` matrix (the first step of the shortest path) lets
the path be restored. Time `O(N^3)` per test, memory `O(N^2)`.

Pitfalls:

- two parallel edges are not a tour: a cycle needs at least 3 vertices;
- only the shortest of parallel edges should be used;
- the candidate cycles have to be checked before relaxing through `k`, or
  the path `i..j` may go through `k` itself.

## Language notes

- **C++**, **Go**, **Rust**: plain `O(N^3)` loops are far below the limit.
- **Python**: `5 · 100^3` inner steps are tight for 0.5 seconds; the loop
  over `j` works on local references to the rows (`di`, `dk`) and skips rows
  with `dist[i][k]` infinite. PyPy is a safe fallback.
- **Java**: a hand-written byte reader for the up to 50 000 input lines.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1004_shortest_paths_graphs.cpp](1004_shortest_paths_graphs.cpp) | G++ 13.2 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.046 s | 360 KB |
| [1004_shortest_paths_graphs.go](1004_shortest_paths_graphs.go) | Go 1.14 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.031 s | 3356 KB |
| [1004_shortest_paths_graphs.java](1004_shortest_paths_graphs.java) | Java 1.8 | shortest_paths, graphs | O(N^3) per test | AC | 0.125 s | 1384 KB |
| [1004_shortest_paths_graphs.py](1004_shortest_paths_graphs.py) | PyPy 3.10 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.187 s | 9912 KB |
| [1004_shortest_paths_graphs.rs](1004_shortest_paths_graphs.rs) | Rust 1.75 x64 | shortest_paths, graphs | O(N^3) per test | AC | 0.015 s | 1096 KB |
