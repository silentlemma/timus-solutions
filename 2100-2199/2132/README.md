# 2132. Splitting the edges of a graph into adjacent pairs

[Timus 2132](https://acm.timus.ru/problem.aspx?space=1&num=2132) · difficulty 1528 · graphs, constructive

Original problem by Alexander Petrov, prepared by Alexander Ipatov, from the “Later is better than never” contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A simple graph with an even number of edges is given as a list of
edges. Split all edges into pairs of edges that share a vertex, or
report that it is impossible. Any valid split is accepted. The limits
are 1 second and 128 MB.

## Input

Pairs of vertex numbers, one pair per edge: an even number of edges
between 2 and 10⁵, vertices from 1 to 10⁵.

## Output

The number of pairs m and m triples a b c for the edges {a, b} and
{b, c}, or −1.

## Checking

A checker verifies that the triples use every edge exactly once.

## Examples

### Example 1

Input:

```
1 2
2 3
3 1
1 10
```

Output:

```
2
1 2 3
3 1 10
```

### Example 2

Input:

```
1 2
2 3
3 1
4 10
```

Output:

```
-1
```

## Solution

Edges in different connected components cannot be paired, so a
component with an odd number of edges makes the answer −1. A connected
graph with an even number of edges can always be split, and the
construction shows it.

Build a spanning tree of every component with a search and process the
vertices so that each one comes after all its descendants. Every edge
outside the tree is given to one of its ends, the one processed first.
At a vertex v, collect the edges to its children that are still free
and the non-tree edges given to v, and pair them up through v. If one
edge is left over, pair it with the edge from v to its parent, which is
then used; otherwise the parent edge stays free for the parent. If the
root of a component is left with an odd edge, the component had an odd
number of edges. The search is iterative and everything is O(V + E).

In the second example the triangle 1 – 2 – 3 has three edges and the
edge 4 – 10 is alone, so no split exists.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2132_graphs_constructive.cpp](2132_graphs_constructive.cpp) | G++ 13.2 x64 | graphs, constructive | O(V + E) | AC | 0.109 s | 7376 KB |
| [2132_graphs_constructive.go](2132_graphs_constructive.go) | Go 1.14 x64 | graphs, constructive | O(V + E) | AC | 0.078 s | 21920 KB |
| [2132_graphs_constructive.java](2132_graphs_constructive.java) | Java 1.8 | graphs, constructive | O(V + E) | AC | 0.156 s | 8900 KB |
| [2132_graphs_constructive.py](2132_graphs_constructive.py) | Python 3.12 x64 | graphs, constructive | O(V + E) | AC | 0.359 s | 30520 KB |
| [2132_graphs_constructive.rs](2132_graphs_constructive.rs) | Rust 1.75 x64 | graphs, constructive | O(V + E) | AC | 0.046 s | 12784 KB |
