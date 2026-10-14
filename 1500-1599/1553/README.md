# 1553. Caves and Tunnels

[Timus 1553](https://acm.timus.ru/problem.aspx?space=1&num=1553) · difficulty 282 · trees

Original problem from the Novosibirsk SU Contest at the Petrozavodsk Training Camp, September 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 100000 caves form a tree. Each cave has a radiation level, 0 at
first. Answer Q ≤ 100000 queries: "I U V" raises the level of cave U by
V ≤ 10000, and "G U V" asks for the highest level on the path from U to
V.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

N, the N − 1 tunnels, Q and the queries.

## Output

The answer to every G query, one per line.

## Examples

### Example 1

Input:

```
4
1 2
2 3
2 4
6
I 1 1
G 1 1
G 3 4
I 2 3
G 1 1
G 3 4
```

Output:

```
1
0
1
3
```

## Solution

Heavy-light decomposition: root the tree at cave 1 and let every cave
continue its chain into the child with the largest subtree. Any path
from a cave up to the root crosses at most log₂ N chains, because each
light edge at least halves the subtree size. Lay the chains out one
after another, so that every chain occupies consecutive places, and keep
a segment tree of maxima over the places.

An increase changes one leaf and the maxima above it. A path query
climbs from the end whose chain head is deeper, taking the maximum over
that chain's stretch, until both ends share a chain, and finishes with
the stretch between them. The tree is built without recursion, from a
breadth-first order, as a path of 100000 caves would overflow a
recursive search. `O((N + Q) log² N)`.

Pitfalls:

- a query from a cave to itself is that cave's level (tests 01, 04);
- increases by 0 are allowed (test 04);
- a level can reach 10⁹ (10⁵ increases of 10⁴), close to the 32-bit
  limit, so the solutions keep levels in 64 bits;
- a path of 100000 caves is one long chain (gen2).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1553_trees.cpp](1553_trees.cpp) | G++ 13.2 x64 | trees | O((N + Q) log^2 N) | AC | 0.390 s | 9584 KB |
| [1553_trees.go](1553_trees.go) | Go 1.14 x64 | trees | O((N + Q) log^2 N) | AC | 0.203 s | 19108 KB |
| [1553_trees.java](1553_trees.java) | Java 1.8 | trees | O((N + Q) log^2 N) | AC | 0.203 s | 10684 KB |
| [1553_trees.py](1553_trees.py) | Python 3.12 x64 | trees | O((N + Q) log^2 N) | AC | 2.140 s | 60768 KB |
| [1553_trees.rs](1553_trees.rs) | Rust 1.75 x64 | trees | O((N + Q) log^2 N) | AC | 0.140 s | 19664 KB |
