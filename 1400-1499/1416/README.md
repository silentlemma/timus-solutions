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

First line: n vertices and m undirected edges, 2≤n≤500 and 1≤m≤n(n−1)/2. Each of the next m lines contains endpoints a,b in 1..n and cost w in 0..1000. There are no loops or parallel edges, and the graph is connected.

## Output

"Cost: " and the first cost, then "Cost: " and the second.

## Checking

The repository compares the complete output exactly after removing trailing whitespace only: two lines, Cost: followed by the first and second tree costs. Capitalization, the colon, the following space and the interior newline matter. The second cost may equal the first; use -1 only when no distinct second spanning tree exists.

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

The fast set reuses qualifying simple Java and Python and selects optimized C++, Go and Rust. Simple Go/Rust are retained for teaching but fail current memory limits, so they are not claimed as qualifying fast sources. No identical source copies are needed. All historical Accepted time/memory pairs remain attached to their own versions.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1416_graphs_parsing_implementation_optimized.go`. Specialize token conversion and numeric output to the types actually used, removing unused generic branches while retaining the algorithm and comments. Use an 8192-byte refillable input buffer instead of retaining the entire input. Tokens and partial/EOF reads retain their original meaning.

Accepted #11328937 (Go 1.14 x64): **0.031 s / 8892 KB**. Archived comparison: `1416_graphs.go` (Go 1.14 x64) — 0.203 s / 10568 KB (#11286112).

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1416_graphs_implementation_optimized.rs`. Use 32-bit bounded edge weights and endpoints while keeping spanning-tree totals in 64 bits. The two spanning-tree computations and their ordering remain unchanged. Read tokens through a bounded native byte buffer; short tokens stay inline and only long tokens allocate spill storage. Decimal conversion retains the signed bounds without keeping the full command input. The C entry calls the solver directly and flushes Rust output before returning; the archived ordinary-entry implementation remains available.

Accepted #11328963 (Rust 1.75 x64): **0.031 s / 3908 KB**. Archived comparison: `1416_graphs.rs` (Rust 1.75 x64) — 0.015 s / 9656 KB (#11286115).

## Language notes

The simple implementations retain weight, heaviest-path and tree-membership matrices plus an edge list and O(n) Prim state: O(n²+m) auxiliary storage. Full-input parsers, notably Python and simple Rust, additionally retain I input bytes/tokens, O(n²+m+I). Compact C++ uses two uint16 matrices, marks chosen tree edges absent and scans the matrix instead of retaining separate edge/membership arrays, so storage is O(n²). Its absent sentinel exceeds all weights≤1000. Optimized Go keeps the graph structures but refills an 8192-byte input buffer; optimized Rust uses bounded input, 32-bit edge fields and 64-bit totals. All retain O(n²+m) algorithmic time.

Under shared [criteria](../../RATING_CRITERIA.md), memory is ignored only strictly below 1024 KB. Cached optimized C++ passes both ranks 1/89 and 2/89; Java simple passes 1/14 in both. Python simple passes its eight-exact-rival third-reference limits 0.52095 s / 53847.60 KB. Go’s one exact rival gives 1.8860 s / 9117.20 KB: optimized 8892 KB passes, simple 10568 KB fails memory. Rust’s one rival gives 0.1610 s / 7015 KB: optimized 3908 KB passes, simple 9656 KB fails memory. Rival times below 0.015 s are excluded; only our time is floored.

In `1416_graphs_parsing_implementation_optimized.go`, helper comments now describe refillable input and %d-only formatted output, and the unchanged 128-byte inline-token capacity has a name. Values, algorithm and meaningful explanations remain.

Only lint-required constants in `1416_graphs_implementation_optimized.rs` were given names; their values, algorithm and comments are unchanged. Accepted #11328963 describes the preceding exact bytes and paired metrics.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

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
| [1416_graphs_parsing_implementation_optimized.go](1416_graphs_parsing_implementation_optimized.go) | Go 1.14 x64 | graphs, parsing, implementation | O(n^2 + m) | AC | 0.046 s | 8900 KB | 11331024 |
| [1416_graphs_implementation_optimized.rs](1416_graphs_implementation_optimized.rs) | Rust 1.75 x64 | graphs, implementation | O(n^2 + m) | AC | 0.031 s | 3908 KB | 11331119 |
