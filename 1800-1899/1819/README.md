# 1819. Professional Approach

[Timus 1819](https://acm.timus.ru/problem.aspx?space=1&num=1819) · difficulty 6417 · graphs

Original problem from the Tavrida NU Akai Contest, Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A city has n crossroads and k two-way roads, with no two roads between
the same pair. For each of q queries (hotel, venue), tell whether there
are three paths from the hotel to the venue such that no two of them
use the same road.

## Input

n and k (2 ≤ n ≤ 50000, 1 ≤ k ≤ 50000), then k roads as pairs of
distinct crossroads, then q (1 ≤ q ≤ 50000) and q pairs of distinct
crossroads.

## Output

For every query, "Yes" or "No" on its own line.

## Examples

### Example 1

Input:

```
6 9
1 2
1 5
1 4
1 6
2 3
3 4
3 5
4 5
4 6
9
1 2
1 3
1 5
2 4
5 6
3 6
3 4
2 6
2 3
```

Output:

```
No
Yes
Yes
No
No
No
Yes
No
No
```

## Solution

By Menger's theorem the answer is "Yes" exactly when no one or two
roads separate the two crossroads, so the task is to answer queries
about 3-edge-connectivity.

Take a DFS forest. Every other road joins a crossroad to one of its
ancestors and covers the tree edges between them. Give each such road
a random 64-bit number and let the cover of a tree edge be the xor of
the numbers of the roads covering it: marking both ends of each road
and summing xors up the tree gives all covers in `O(n + k)`. A count of
covering roads is summed the same way. Then the cuts of at most two
roads are:

- a tree edge covered by nothing, a bridge;
- a tree edge covered by exactly one road, together with that road;
- two tree edges with equal covers.

Tree edges with the same cover lie on one root path and split the tree
into pieces that the covering roads close into a ring; two crossroads
are separated by such a pair unless the tree path between them crosses
all edges of the class or none. So every tree edge gets a value: a
fresh random one for bridges and once-covered edges, and for a class of
equal covers random values whose xor is zero, with 0 for an edge that
is alone in its class. Since any proper part of a class xors to a
nonzero number with overwhelming probability, two crossroads of one
tree are 3-edge-connected exactly when their labels, the xors of
values from the root, coincide. Each query is then a comparison.
`O(n + k + q)` expected with a hash map for the classes.

In the example crossroad 6 has only the roads 1–6 and 4–6, and
crossroad 2 only 1–2 and 2–3, so each is cut off by two roads.
Depending on the DFS tree such a pair is either two tree edges with
equal covers or a tree edge covered by the other road alone. The other
four crossroads get equal labels.

Pitfalls:

- crossroads in different components share label 0 at their roots, so
  the components are compared too;
- a class whose path is crossed completely does not separate: the ends
  of a chain of cut pairs lie in one piece of the ring;
- 50000 vertices on a path need an iterative DFS.

All answers agree with a max-flow brute force on hundreds of random
small graphs and with an independent accepted implementation on random
graphs, wheels, rings of K4 blocks, paths and forests at full size.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1819_graphs.cpp](1819_graphs.cpp) | G++ 13.2 x64 | graphs | O(n + k + q) | AC | 0.156 s | 5008 KB |
| [1819_graphs.go](1819_graphs.go) | Go 1.14 x64 | graphs | O(n + k + q) | AC | 0.062 s | 10436 KB |
| [1819_graphs.java](1819_graphs.java) | Java 1.8 | graphs | O(n + k + q) | AC | 0.125 s | 6744 KB |
| [1819_graphs.py](1819_graphs.py) | Python 3.12 x64 | graphs | O(n + k + q) | AC | 0.359 s | 34464 KB |
| [1819_graphs.rs](1819_graphs.rs) | Rust 1.75 x64 | graphs | O(n + k + q) | AC | 0.031 s | 9700 KB |
