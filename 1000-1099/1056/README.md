# 1056. The centers of a tree

[Timus 1056](https://acm.timus.ru/problem.aspx?space=1&num=1056) · difficulty 552 · bfs, trees

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
vertex within half the diameter rounded up — otherwise there would be a
longer path.

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

## Optimized solutions

Process vertices in decreasing order, since every parent has a smaller number. Keep the longest downward arm and its endpoint for each vertex. Each child offers a new arm; joining it to the longest previous arm through the parent gives the longest path using that child and an already processed branch. The maximum of these paths is the diameter. Starting from the end of the longer arm, climb half the diameter to find the middle vertex, or the two adjacent middle vertices when the diameter is odd. Time and space are O(N).

Every path between two vertices has a highest vertex where its two arms meet. When the later of those branches is processed, the algorithm checks it against the longest earlier branch at that vertex. The middle of the diameter lies on the longer arm or at the fork, so following parent links from the longer arm's endpoint is enough.

## Language notes

The five BFS implementations use an array as their queue. The Python tree version stores parents and downward arms instead of adjacency lists. Submission 11316948 used 1,532 KB versus 3,040 KB for BFS and took 0.093 s versus 0.062 s.

Go stores the parent, longest downward arm and its endpoint in 16-bit arrays. Submission 11317158 took 0.031 s and used 1196 KB, versus 0.015 s and 2972 KB for the BFS version.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321750 · Java 1.8 №11321752 · Rust 1.75 x64 №11321755 · Go 1.14 x64 №11322056 · Python 3.12 x64 №11322057.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1056_bfs.cpp](1056_bfs.cpp) | G++ 13.2 x64 | bfs | O(N) | AC | 0.001 s | 580 KB | 11321750 |
| [1056_bfs.go](1056_bfs.go) | Go 1.14 x64 | bfs | O(N) | AC | 0.015 s | 2972 KB | 11322056 |
| [1056_bfs.java](1056_bfs.java) | Java 1.8 | bfs | O(N) | AC | 0.078 s | 2548 KB | 11321752 |
| [1056_bfs.py](1056_bfs.py) | Python 3.12 x64 | bfs | O(N) | AC | 0.062 s | 3040 KB | 11322057 |
| [1056_bfs.rs](1056_bfs.rs) | Rust 1.75 x64 | bfs | O(N) | AC | 0.015 s | 1376 KB | 11321755 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1056_trees.py](1056_trees.py) \* | Python 3.12 x64 | trees | O(N) | AC | 0.093 s | 1532 KB | 11316948 |
| [1056_trees.go](1056_trees.go) | Go 1.14 x64 | trees | O(N) | AC | 0.031 s | 1196 KB | 11317158 |

\* Accepted; the Python rating target is still open. The saved rating has no comparable Go submissions from other authors.
