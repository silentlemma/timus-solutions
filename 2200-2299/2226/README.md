# 2226. Where a walk along the shortest unused edge ends, from every start

[Timus 2226](https://acm.timus.ru/problem.aspx?space=1&num=2226) · difficulty 738 · dp, trees

Original problem by Vadim Barinov, from the Ural Championship 2025.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tree has N vertices and edges of distinct lengths. A walk starts at
some vertex and always takes the shortest edge to a vertex it has not
visited yet, until no such edge is left. For every starting vertex,
print where the walk ends. The limits are 1 second and 256 MB.

## Input

N, 2 ≤ N ≤ 10⁵, then the N − 1 edges u v l with distinct lengths up to
10⁹.

## Output

The end vertex for each start.

## Examples

### Example 1

Input:

```
5
1 2 109
2 3 547
2 4 652
5 3 318
```

Output:

```
5 1 5 1 1
```

## Solution

In a tree the only visited neighbor of the current vertex is the one
the walk came from, so the next step depends only on the current vertex
and that previous one: it is the shortest edge, or the second shortest
if the shortest leads back. Only the two shortest edges of every vertex
are needed.

Root the tree and compute two values per vertex:

- down(v), the end of the walk that has just arrived at v from its
  parent: it continues along the shortest edge to a child c and ends at
  down(c), or ends at v if there is none;
- up(v), the end of the walk that has just stepped from v to its parent
  p: at p it takes the shortest edge other than the one to v, which
  either goes to the parent of p (giving up(p)), to another child c
  (giving down(c)), or does not exist (the walk ends at p).

down is filled from the leaves up and up from the root down, with
iterative traversals. A walk starting at v first takes v's shortest
edge, so its end is up(v) when that edge leads to the parent and down(v)
otherwise.

In the example the walk from 1 goes to 2, then along 547 to 3, then
along 318 to 5, where it stops.

This takes O(N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2226_dp_trees.cpp](2226_dp_trees.cpp) | G++ 13.2 x64 | dp, trees | O(N) | AC | 0.125 s | 7784 KB |
| [2226_dp_trees.go](2226_dp_trees.go) | Go 1.14 x64 | dp, trees | O(N) | AC | 0.093 s | 21936 KB |
| [2226_dp_trees.java](2226_dp_trees.java) | Java 1.8 | dp, trees | O(N) | AC | 0.187 s | 9544 KB |
| [2226_dp_trees.py](2226_dp_trees.py) | Python 3.12 x64 | dp, trees | O(N) | AC | 0.734 s | 51044 KB |
| [2226_dp_trees.rs](2226_dp_trees.rs) | Rust 1.75 x64 | dp, trees | O(N) | AC | 0.078 s | 20468 KB |
