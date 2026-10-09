# 1109. The fewest edges touching every vertex of a bipartite graph

[Timus 1109](https://acm.timus.ru/problem.aspx?space=1&num=1109) · difficulty 250 · matching

Original problem from the Bulgarian National Olympiad in Informatics, Day 1.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A bipartite graph has `M` vertices on the left and `N` on the right
(`M, N ≤ 1000`) and `K` edges, each joining a left vertex to a right one;
every vertex has at least one edge. Find the smallest number of edges
such that every vertex is an end of at least one chosen edge.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`M N K`, then `K` lines `a b`: an edge between left vertex `a` and right
vertex `b`. Edges may repeat.

## Output

The smallest number of edges.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3 2 4
1 1
2 1
3 1
3 2
```

Output:

```
3
```

## Solution

This is a minimum edge cover, and its size is `M + N − ν`, where `ν` is
the size of a maximum matching. Given a maximum matching, add for every
unmatched vertex any one of its edges: `ν + (M + N − 2ν)` edges. Back the
other way, in a minimum edge cover every edge has an end covered by it
alone, so the cover is a set of stars; taking one edge from each star
gives a matching of `M + N − |cover|` edges, so no cover can be smaller.

The maximum matching is found with Hopcroft–Karp: a BFS from all free
left vertices splits the graph into layers, then a DFS along the layers
augments over vertex-disjoint shortest paths, and the phases repeat while
an augmenting path exists. `O(K √(M + N))`.

Pitfalls:

- matching is not the answer by itself: the unmatched vertices still need
  an edge each;
- a matching found greedily, taking the first free partner, can be too
  small, as in the staircase tests;
- with up to a million edges and half a second, a plain augmenting-path
  search from every vertex can be too slow, and so can slow input.

The answers were checked against a brute force over all edge subsets on
hundreds of small graphs and against Kuhn's simple augmenting-path
matching on the large ones.

## Language notes

- C++, Java and Rust search augmenting paths recursively; Python walks
  them with an explicit stack.
- Go and Java read the numbers with their own byte readers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1109_matching.cpp](1109_matching.cpp) | G++ 13.2 x64 | matching | O(K √(M + N)) | AC | 0.062 s | 468 KB |
| [1109_matching.go](1109_matching.go) | Go 1.14 x64 | matching | O(K √(M + N)) | AC | 0.015 s | 2512 KB |
| [1109_matching.java](1109_matching.java) | Java 1.8 | matching | O(K √(M + N)) | AC | 0.125 s | 1264 KB |
| [1109_matching.py](1109_matching.py) | Python 3.12 x64 | matching | O(K √(M + N)) | AC | 0.093 s | 8516 KB |
| [1109_matching.rs](1109_matching.rs) | Rust 1.75 x64 | matching | O(K √(M + N)) | AC | 0.015 s | 1820 KB |
