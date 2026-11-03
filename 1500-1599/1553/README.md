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

## Checking

Compare query answers in order. New Java passed 106 target main invocations: 100 random small trees checked by literal BFS paths, a 100000-vertex chain with 100000 operations, a 99999-vertex star and 4 repository cases. Include zero increments and answers up to 10^9.

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
from a cave up to the root crosses at most ⌊log₂ N⌋ + 1 chains, because each
light edge at least halves the subtree size when going down. Lay the chains out one
after another, so that every chain occupies consecutive places, and keep
a segment tree of maxima over the places.

An increase changes one leaf and the maxima above it. A path query
climbs from the end whose chain head is deeper, taking the maximum over
that chain's stretch, until both ends share a chain, and finishes with
the stretch between them. The tree is built without recursion, from a
breadth-first order, as a path of 100000 caves would overflow a
recursive search. `O((N + Q) log² N)`.

Pitfalls:

- a query from a cave to itself is that cave's level (tests 01, 02, 03);
- increases by 0 are allowed (test 04);
- a level is at most 10⁹ (10⁵ increases of 10⁴), within signed 32 bits;
  the native teaching sources retain 64-bit values, while the compact
  variants use 32-bit storage (the teaching Python uses Python integers);
- a path can split into two chains when cave 1 is internal: gen2 has
  chains of 52487 and 47513 caves, not one chain of 100000 caves.

## Optimized solutions

Keep the iterative heavy-light decomposition and path maximum queries. Compact C++/Python versions use flat graph/DP arrays, 32-bit segment maxima and bounded input/output. With at most 100000 increases of at most 10000, a value is at most 10^9 and fits signed 32 bits. Nonnegative increases permit stopping propagation once an ancestor maximum does not change.

Java additionally reuses storage after the old meaning is dead: adjacency heads become heavy-child indices after traversal; subtree sizes become vertex positions; traversal order becomes chain heads. Chain roots are then enumerated by vertex number, never by the overwritten traversal order. After chain numbering, the edge-destination array has 2N cells and becomes the cleared segment tree. Parent and depth arrays remain intact for queries. This eliminates three N-cell allocations and a separate 2N-cell tree without overlapping live meanings. Preparation stays `O(N)`, updates `O(log N)`, path queries `O(log² N)` and storage `O(N)`. All clear HLD bases are preserved.

- `1553_trees_optimized.cpp`: 0.046 s / 5200 KB; base `1553_trees.cpp`: 0.390 s / 9584 KB; relative change: time -88.2%, memory -45.7%.
- `1553_trees_optimized.java`: 0.187 s / 6968 KB; base `1553_trees.java`: 0.203 s / 10684 KB; relative change: time -7.9%, memory -34.8%.
- `1553_trees_optimized.py`: 1.703 s / 5432 KB; base `1553_trees.py`: 2.140 s / 60768 KB; relative change: time -20.4%, memory -91.1%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1553_trees.cpp`; covering source `1553_trees_optimized.cpp`; time/memory places 2/1, other-author entries 149/149.

- Go: preferred teaching base `1553_trees.go`; covering source `1553_trees.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1553_trees.java`; covering source `1553_trees_optimized.java`; time/memory places 2/1, other-author entries 5/5.

- Python/PyPy: preferred teaching base `1553_trees.py`; covering source `1553_trees_optimized.py`; time/memory places 2/1, other-author entries 1/1.

- Rust: preferred teaching base `1553_trees.rs`; covering source `1553_trees.rs`; time/memory places 1/1, other-author entries 2/2.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1553_trees.cpp](1553_trees.cpp) | G++ 13.2 x64 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 0.390 s | 9584 KB | 11287607 |
| [1553_trees.go](1553_trees.go) | Go 1.14 x64 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 0.203 s | 19108 KB | 11287610 |
| [1553_trees.java](1553_trees.java) | Java 1.8 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 0.203 s | 10684 KB | 11287615 |
| [1553_trees.py](1553_trees.py) | Python 3.12 x64 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 2.140 s | 60768 KB | 11287612 |
| [1553_trees.rs](1553_trees.rs) | Rust 1.75 x64 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 0.140 s | 19664 KB | 11287616 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1553_trees_optimized.cpp](1553_trees_optimized.cpp) | G++ 13.2 x64 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 0.046 s | 5200 KB | 11309316 |
| [1553_trees_optimized.java](1553_trees_optimized.java) \* | Java 1.8 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 0.187 s | 6968 KB | 11309559 |
| [1553_trees_optimized.py](1553_trees_optimized.py) \* | Python 3.12 x64 | trees | O(N) preparation; O(log N) update; O(log^2 N) query | AC | 1.703 s | 5432 KB | 11309314 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
