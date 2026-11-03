# 1752. Tree 2

[Timus 1752](https://acm.timus.ru/problem.aspx?space=1&num=1752) · difficulty 259 · graphs

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

## Checking

For every query, check that the returned vertex is at the requested distance; verify an impossibility answer when no such vertex exists.

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

For any fixed diameter of the tree, the longest path in it, at least
one of its ends is farthest from each vertex v. So if a vertex at
distance d exists, then one of the two ends, a or b, is at distance at
least d, and the path from v towards it passes a vertex at distance
exactly d.

The ends are found the usual way: the deepest vertex seen from vertex
1 is a, and the deepest vertex seen from a is b. Walking the tree from
a root in depth-first order, the current path from the root is kept in
an array by depth. When the walk reaches v at depth h, every query at v
with d ≤ h that is still unanswered is answered by the vertex at depth
h − d on that path. Three walks, from 1, from a and from b, answer every
query that has an answer; the rest get 0. Time and space are `O(n + q)`.

Integer tokens are separated by whitespace, including tabs. All five
versions push neighbors onto the stack in reverse input order and keep
the first answer found, so they choose the same vertices.

The program may print other vertices than the example, for instance 9
for the third query instead of 2; both are at distance 3 from vertex 4.

Pitfalls:

- skip all whitespace before each integer, including the leading tab
  in test 06; otherwise a valid query can be read as vertex 0;
- a query with d = 0 is answered by v itself;
- a path of 20000 vertices is too deep for recursion in some languages,
  so the walk uses its own stack;
- the queries are many, so they are grouped by vertex rather than
  answered by a walk each.

The answers agree with independent breadth-first searches on 1200 small
random inputs with mixed whitespace. All five versions print identical
answers on these inputs and on the static, generated and maximum-size
cases.

## Optimized solutions

The linear tree algorithm based on diameter endpoints and depth-first paths is unchanged. Bounds on vertex, edge, query and distance indices permit unsigned 16-bit storage, while transient arithmetic uses a sufficiently wide type. Remove query fields that are never read again and reuse work arrays. The same path invariant answers the queries; packing changes representation, not the ancestor or distance chosen. Input and output remain bounded buffers.

- `1752_graphs_optimized.cpp`: 0.031 s / 372 KB; base `1752_graphs.cpp`: 0.109 s / 1492 KB; relative change: time -71.6%, memory -75.1%.
- `1752_graphs_optimized.go`: 0.046 s / 1756 KB; base `1752_graphs.go`: 0.062 s / 6500 KB; relative change: time -25.8%, memory -73.0%.
- `1752_graphs_optimized.java`: 0.125 s / 1100 KB; base `1752_graphs.java`: 0.109 s / 3748 KB; relative change: time +14.7%, memory -70.7%.
- `1752_graphs_optimized.py`: 0.296 s / 4832 KB; base `1752_graphs.py`: 0.265 s / 21232 KB; relative change: time +11.7%, memory -77.2%.
- `1752_graphs_optimized.rs`: 0.031 s / 2124 KB; base `1752_graphs.rs`: 0.078 s / 4136 KB; relative change: time -60.3%, memory -48.6%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1752_graphs.cpp`; covering source `1752_graphs_optimized.cpp`; time/memory places 2/1, other-author entries 75/75.

- Go: preferred teaching base `1752_graphs.go`; covering source `1752_graphs.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1752_graphs.java`; covering source `1752_graphs.java`; time/memory places 1/1, other-author entries 5/5.

- Python/PyPy: preferred teaching base `1752_graphs.py`; covering source `1752_graphs_optimized.py`; time/memory places 1/1, other-author entries 6/6.

- Rust: preferred teaching base `1752_graphs.rs`; covering source `1752_graphs.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1752_graphs.cpp](1752_graphs.cpp) | G++ 13.2 x64 | graphs | O(n + q) | AC | 0.109 s | 1492 KB | 11308923 |
| [1752_graphs.go](1752_graphs.go) | Go 1.14 x64 | graphs | O(n + q) | AC | 0.062 s | 6500 KB | 11298038 |
| [1752_graphs.java](1752_graphs.java) | Java 1.8 | graphs | O(n + q) | AC | 0.109 s | 3748 KB | 11308924 |
| [1752_graphs.py](1752_graphs.py) | Python 3.12 x64 | graphs | O(n + q) | AC | 0.265 s | 21232 KB | 11298042 |
| [1752_graphs.rs](1752_graphs.rs) | Rust 1.75 x64 | graphs | O(n + q) | AC | 0.078 s | 4136 KB | 11308925 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1752_graphs_optimized.cpp](1752_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(N+Q) | AC | 0.031 s | 372 KB | 11308204 |
| [1752_graphs_optimized.go](1752_graphs_optimized.go) | Go 1.14 x64 | graphs | O(N+Q) | AC | 0.046 s | 1756 KB | 11308205 |
| [1752_graphs_optimized.java](1752_graphs_optimized.java) | Java 1.8 | graphs | O(N+Q) | AC | 0.125 s | 1100 KB | 11309392 |
| [1752_graphs_optimized.py](1752_graphs_optimized.py) | Python 3.12 x64 | graphs | O(N+Q) | AC | 0.296 s | 4832 KB | 11308203 |
| [1752_graphs_optimized.rs](1752_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(N+Q) | AC | 0.031 s | 2124 KB | 11308207 |
