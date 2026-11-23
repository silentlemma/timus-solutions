# 1416. Confidential

[Timus 1416](https://acm.timus.ru/problem.aspx?space=1&num=1416) · difficulty 385 · graphs

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

## Optimized solutions

The compact C++ version keeps the same Prim recurrence and stores both matrices in 16-bit entries. Once an edge joins the tree, mark it absent in the weight matrix. Both endpoints have joined, so this has no effect on later Prim updates. The final scan then sees exactly the non-tree edges and can stop as soon as one has zero extra cost.

The accepted base implementations [1416_graphs.go](1416_graphs.go), [1416_graphs.java](1416_graphs.java), [1416_graphs.py](1416_graphs.py), [1416_graphs.rs](1416_graphs.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1416_graphs_parsing_implementation_optimized.go`. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments. Use an 8192-byte refillable input buffer instead of retaining the entire input. Tokens and partial/EOF reads retain their original meaning.

Accepted #11328937 (Go 1.14 x64): **0.031 s / 8892 KB**. Archived comparison: `1416_graphs.go` (Go 1.14 x64) — 0.203 s / 10568 KB (#11286112).

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1416_graphs_implementation_optimized.rs`. Use 32-bit bounded edge weights and endpoints while keeping spanning-tree totals in 64 bits. The two spanning-tree computations and their ordering remain unchanged. Read tokens through a bounded native byte buffer; short tokens stay inline and only long tokens allocate spill storage. Decimal conversion retains the signed bounds without keeping the full command input. The C entry calls the solver directly and flushes Rust output before returning; the archived ordinary-entry implementation remains available.

Accepted #11328963 (Rust 1.75 x64): **0.031 s / 3908 KB**. Archived comparison: `1416_graphs.rs` (Rust 1.75 x64) — 0.015 s / 9656 KB (#11286115).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1416_graphs.cpp](1416_graphs.cpp) | G++ 13.2 x64 | graphs | O(n^2 + m) | AC | 0.187 s | 3448 KB | 11286111 |
| [1416_graphs.go](1416_graphs.go) | Go 1.14 x64 | graphs | O(n^2 + m) | AC | 0.203 s | 10568 KB | 11286112 |
| [1416_graphs.java](1416_graphs.java) | Java 1.8 | graphs | O(n^2 + m) | AC | 0.109 s | 8164 KB | 11286114 |
| [1416_graphs.py](1416_graphs.py) | Python 3.12 x64 | graphs | O(n^2 + m) | AC | 0.39 s | 44108 KB | 11328275 |
| [1416_graphs.rs](1416_graphs.rs) | Rust 1.75 x64 | graphs | O(n^2 + m) | AC | 0.015 s | 9656 KB | 11286115 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1416_graphs_optimized.cpp](1416_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(n^2 + m) | AC | 0.015 s | 1132 KB | 11310409 |
| [1416_graphs_parsing_implementation_optimized.go](1416_graphs_parsing_implementation_optimized.go) | Go 1.14 x64 | graphs, parsing, implementation | O(n^2 + m) | AC | 0.031 s | 8892 KB | 11328937 |
| [1416_graphs_implementation_optimized.rs](1416_graphs_implementation_optimized.rs) | Rust 1.75 x64 | graphs, implementation | O(n^2 + m) | AC | 0.031 s | 3908 KB | 11328963 |
