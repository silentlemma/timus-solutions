# 1752. Tree 2

[Timus 1752](https://acm.timus.ru/problem.aspx?space=1&num=1752) · difficulty 257 · graphs

Original problem by Petr Lezhankin, from the Ufa SATU Contest at the Petrozavodsk summer training camp, August 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

In a tree of n vertices, the distance between two vertices is the
number of edges on the path between them. For each query, a vertex v
and a number d, find a vertex at distance exactly d from v.

## Input

n (1 ≤ n ≤ 20000) and q (1 ≤ q ≤ 50000), then the n − 1 edges, then q
queries v (1 ≤ v ≤ n) and d (0 ≤ d ≤ n).

## Output

For each query a vertex at distance d from v, or 0 if there is none.
Any fitting vertex is accepted.

## Examples

### Example 1

Input:

```
9 10
1 8
1 5
1 4
2 7
2 5
3 6
5 9
6 9
5 4
8 1
4 3
2 4
9 3
1 1
5 2
3 5
6 4
7 3
```

Output:

```
0
1
2
3
4
5
6
7
8
9
```

## Solution

The vertex farthest from any vertex v is always an end of a diameter of
the tree, the longest path in it. So if a vertex at distance d exists,
then one of the two ends, a or b, is at distance at least d, and the
path from v towards it passes a vertex at distance exactly d.

The ends are found the usual way: the deepest vertex seen from vertex
1 is a, and the deepest vertex seen from a is b. Walking the tree from
a root in depth-first order, the current path from the root is kept in
an array by depth. When the walk reaches v at depth h, every query at v
with d ≤ h is answered by the vertex at depth h − d on that path. Three
walks, from 1, from a and from b, answer every query that has an
answer; the rest get 0. `O(n + q)`.

The program may print other vertices than the example, for instance 9
for the third query instead of 2; both are at distance 3 from vertex 4.

Pitfalls:

- a query with d = 0 is answered by v itself;
- a path of 20000 vertices is too deep for recursion in some languages,
  so the walk uses its own stack;
- the queries are many, so they are grouped by vertex rather than
  answered by a walk each.

The answers agree with a search from each query vertex on 300 random
trees of up to 10 vertices with every query, and an independent
accepted implementation agrees on which large queries have no answer.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1752_graphs.cpp](1752_graphs.cpp) | G++ 13.2 x64 | graphs | O(n + q) | AC | 0.109 s | 1516 KB |
| [1752_graphs.go](1752_graphs.go) | Go 1.14 x64 | graphs | O(n + q) | AC | 0.078 s | 7244 KB |
| [1752_graphs.java](1752_graphs.java) | Java 1.8 | graphs | O(n + q) | AC | 0.125 s | 3756 KB |
| [1752_graphs.py](1752_graphs.py) | Python 3.12 x64 | graphs | O(n + q) | AC | 0.250 s | 21372 KB |
| [1752_graphs.rs](1752_graphs.rs) | Rust 1.75 x64 | graphs | O(n + q) | AC | 0.062 s | 4172 KB |
