# 1416. Confidential

[Timus 1416](https://acm.timus.ru/problem.aspx?space=1&num=1416) · difficulty 394 · graphs

Original problem by Den Raskovalov, from the Ural State University Championship, October 29, 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A connected graph has n vertices (2 ≤ n ≤ 500) and m edges with costs
from 0 to 1000, at most one edge between any two vertices. Print the
cost of a minimum spanning tree and the cost of the next spanning tree
in order of cost (which may be equal to the first), or −1 if there is
no other spanning tree.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

n and m, then m lines a b w.

## Output

"Cost: " and the first cost, then "Cost: " and the second.

## Examples

### Example 1

Input:

```
4 6
1 2 2
2 3 2
3 4 2
4 1 2
1 3 1
2 4 1
```

Output:

```
Cost: 4
Cost: 4
```

### Example 2

Input:

```
3 2
1 2 2
2 3 2
```

Output:

```
Cost: 4
Cost: -1
```

## Solution

A second-best spanning tree differs from some minimum spanning tree in
exactly one edge: an edge outside the tree comes in and the heaviest
edge on the tree path between its ends goes out. So the second cost is
the minimum cost plus the smallest value of w − (heaviest edge on the
path) over the edges outside the tree, and −1 if every edge is in the
tree.

With up to 500 vertices, Prim's algorithm on the cost matrix takes
O(n²). The heaviest edge on every tree path comes for free: when vertex
v joins through parent p with edge cost c, for each vertex u already in
the tree heaviest(u, v) = max(heaviest(u, p), c). `O(n² + m)`.

Pitfalls:

- the second tree may cost the same as the first (test 01);
- a graph that is itself a tree has no second tree (tests 02, 03, gen2);
- costs can be 0 (tests 04, 06).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1416_graphs.cpp](1416_graphs.cpp) | G++ 13.2 x64 | graphs | O(n^2 + m) | AC | 0.187 s | 3448 KB |
| [1416_graphs.go](1416_graphs.go) | Go 1.14 x64 | graphs | O(n^2 + m) | AC | 0.203 s | 10568 KB |
| [1416_graphs.java](1416_graphs.java) | Java 1.8 | graphs | O(n^2 + m) | AC | 0.109 s | 8164 KB |
| [1416_graphs.py](1416_graphs.py) | Python 3.12 x64 | graphs | O(n^2 + m) | AC | 0.343 s | 44112 KB |
| [1416_graphs.rs](1416_graphs.rs) | Rust 1.75 x64 | graphs | O(n^2 + m) | AC | 0.015 s | 9656 KB |
