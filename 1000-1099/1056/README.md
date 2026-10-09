# 1056. The centers of a tree

[Timus 1056](https://acm.timus.ru/problem.aspx?space=1&num=1056) · difficulty 551 · bfs, trees

Original problem from the Rybinsk State Aviation Academy.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tree of `N` vertices (`2 ≤ N ≤ 10000`) is built by adding vertices one
by one: vertex `i` (for `i = 2 … N`) is joined to an earlier vertex `p_i`.
A center is a vertex whose largest distance (in edges) to the other
vertices is the smallest. Print all centers in increasing order.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, then `p_2 … p_N`, one per line.

## Output

The centers in increasing order.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5
1
1
2
2
```

Output:

```
1 2
```

### Example 2

Input:

```
6
1
2
3
4
5
```

Output:

```
3 4
```

## Solution

A tree has one or two centers, and they are the middle of any longest path
(a diameter): the largest distance from a vertex is at least the distance
to the farther end of the diameter, and the middle vertex reaches every
vertex within half the diameter — otherwise there would be a longer path.

A diameter takes two breadth-first searches: the vertex `u` farthest from
any start (vertex 1) is an end of some longest path, and the vertex `v`
farthest from `u` is its other end. Walking back from `v` along the BFS
predecessors gives the path of length `D`; its vertices number `D / 2` and
`(D + 1) / 2` from `v` are the centers — one vertex if `D` is even, two
neighbours if it is odd. `O(N)`.

Pitfalls:

- two centers must both be printed, in increasing order;
- `N = 2`: both vertices are centers;
- the tree can be a path of 10000 vertices, so a recursive search may be
  too deep; the BFS has no recursion.

Another way is to peel off all leaves layer by layer until one or two
vertices remain; the tests were checked with it and, for small trees, by
the distances from every vertex.

## Language notes

- All languages run the same two breadth-first searches with an array as
  the queue.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1056_bfs.cpp](1056_bfs.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.015 s | 596 KB |
| [1056_bfs.go](1056_bfs.go) | Go 1.14 x64 | bfs | O(N) | AC | 0.015 s | 2964 KB |
| [1056_bfs.java](1056_bfs.java) | Java 1.8 | bfs | O(N) | AC | 0.093 s | 2536 KB |
| [1056_bfs.py](1056_bfs.py) | Python 3.12 x64 | bfs | O(N) | AC | 0.078 s | 3088 KB |
| [1056_bfs.rs](1056_bfs.rs) | Rust 1.75 x64 | bfs | O(N) | AC | 0.015 s | 1380 KB |
