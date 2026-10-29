# 1106. Splitting a graph so that every vertex has a neighbour on the other side

[Timus 1106](https://acm.timus.ru/problem.aspx?space=1&num=1106) · difficulty 74 · bfs

Original problem by Dmitry Filimonenkov, from the Tetrahedron Team Contest, May 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An undirected graph has `N ≤ 100` vertices, and every vertex has at
least one neighbour. Split the vertices into two groups so that every
vertex has a neighbour in the other group. Print `0` if this is
impossible.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines: line `i` lists the neighbours of vertex `i` and ends
with `0`. The lists are symmetric.

## Output

The size of the first group, then its vertices on the second line,
separated by single spaces.

## Checking

Any valid split is accepted. The checker verifies that the listed
vertices are distinct, match the size, and that every vertex, in the
first group or not, has a neighbour on the other side.

## Examples

### Example 1

Input:

```
7
2 3 0
3 1 0
1 2 4 5 0
3 0
3 0
7 0
6 0
```

Output:

```
4
1 4 5 6
```

## Solution

A split always exists, so `0` is never printed. Run a BFS from every
vertex not yet reached and put each vertex in the group given by the
parity of its depth in the BFS tree. A non-root vertex is on the other
side from its parent; a root has at least one neighbour, and that
neighbour is its child in the tree, at depth 1. Only tree edges matter,
so odd cycles do no harm. `O(N + M)` for `M` friendships.

Pitfalls:

- this is not a bipartite check: a triangle cannot be 2-coloured
  properly, yet it splits fine as one vertex against two;
- the graph can have several components, and each needs its own BFS
  root.

The answers were checked with the checker on every test and on hundreds
of random graphs of all four generator shapes.

## Optimized solutions

The optimized solutions (Go, Java) parse the input by hand from a
buffer, keep the neighbours of each vertex as bytes, since there are at
most 100 vertices, and run the BFS over a plain array used as the queue.
The team of a vertex is stored as 1 or 2, with 0 for a vertex not
reached yet, so one array replaces both the "visited" marks and the
colours. Java collects the neighbours of a vertex in a buffer of `n`
bytes before copying them into an array of the exact size: a line lists
the neighbours of its vertex among the other `n - 1` vertices, each
once, so it has fewer than `n` entries. Go: 948 KB instead of 1480 KB,
with the same time; Java: 0.093 s instead of 0.125 s and 420 KB instead
of 748 KB.

The optimized Python solution parses the input line by line, keeps the
adjacency lists and the sides in `bytearray`s (there are at most 100
vertices) and walks a plain list as the queue: 548 KB instead of 964 KB,
with the same time.

## Language notes

- Rust takes each list with `take_while` on a shared token iterator.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1106_bfs.cpp](1106_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + M) | AC | 0.015 s | 272 KB | 11279182 |
| [1106_bfs.go](1106_bfs.go) | Go 1.14 x64 | bfs | O(N + M) | AC | 0.031 s | 1480 KB | 11279183 |
| [1106_bfs.java](1106_bfs.java) | Java 1.8 | bfs | O(N + M) | AC | 0.125 s | 748 KB | 11279185 |
| [1106_bfs.py](1106_bfs.py) | Python 3.12 x64 | bfs | O(N + M) | AC | 0.093 s | 964 KB | 11279184 |
| [1106_bfs.rs](1106_bfs.rs) | Rust 1.75 x64 | bfs | O(N + M) | AC | 0.031 s | 296 KB | 11279186 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1106_bfs_optimized.go](1106_bfs_optimized.go) | Go 1.14 x64 | bfs | O(N + M) | AC | 0.031 s | 948 KB | 11303554 |
| [1106_bfs_optimized.java](1106_bfs_optimized.java) | Java 1.8 | bfs | O(N + M) | AC | 0.093 s | 420 KB | 11303555 |
| [1106_bfs_optimized.py](1106_bfs_optimized.py) | Python 3.12 x64 | bfs | O(N + M) | AC | 0.078 s | 548 KB | 11303707 |
