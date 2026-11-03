# 1109. The fewest edges touching every vertex of a bipartite graph

[Timus 1109](https://acm.timus.ru/problem.aspx?space=1&num=1109) · difficulty 249 · matching

Original problem from the Bulgarian National Olympiad in Informatics, Day 1.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A bipartite graph has `M` vertices on the left and `N` on the right
(`M, N ≤ 1000`) and `K` edges, each joining a left vertex to a right one;
every vertex has at least one edge. Find the smallest number of edges
such that every vertex is an end of at least one chosen edge.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`M N K`, then `K` lines `a b`: an edge between left vertex `a` and right
vertex `b`. Edges may repeat.

## Output

The smallest number of edges.

## Checking

The result is compared as one integer token. The actual Python
candidate matched an independent subset-matching oracle on all 46312
non-isolated bipartite graphs with both sides at most four. On 327 graphs
through 3×3, exhaustive edge-cover subsets directly checked the answer
without assuming the matching formula. All six actual candidate programs
passed 82 extra graph shapes and 12 repository inputs each in Docker,
then obtained their own exact-source Accepted.

Extra shapes include a 1000-vertex alternating chain, one million distinct
edges, Hall-deficient blocks, duplicates and 63/64/65-bit boundaries. Python
also checked 16 token/pair chunk boundaries and an unterminated last token.
The 46312 exhaustive executions are Python only, not that many executions
of each native source. Four CPython stress shapes peaked at 0.194 CPU seconds
and 17240 KB RSS locally, within 0.5 seconds/64 MB; local RSS is not the
judge's memory metric.

## Examples

### Example 1

Input:

```
3 2 4
1 1
2 1
3 1
3 2
```

Output:

```
3
```

## Solution

Make the delegates vertices of a bipartite graph and allowed calls
its edges. Every vertex has a neighbor, as promised. If a maximum matching
has size `q`, its edges cover `2q` vertices; add an incident edge for each
remaining vertex. Two unmatched vertices cannot be adjacent, or the matching
could grow. This constructs an edge cover of `M+N−q` edges.

For the lower bound, consider any edge cover with `c` connected components.
It has at least `M+N−c` edges. Taking one edge from each component gives
a matching of size `c`, so `c≤q`. Every cover therefore has at least
`M+N−q` edges. The answer is exactly `M+N−q`; the no-isolated-vertex
promise is essential.

The preferred C++ teaching source uses Kuhn DFS. Start with any greedy
matching, then search one augmenting path for each initially unmatched
left vertex, using a visit timestamp for right vertices. The greedy match
is already maximum on the subset of left vertices it covers. Adding one
free left vertex can increase the optimum by at most one, and any new
augmenting path must start there. A successful DFS flips a path and
increases size by one; failure leaves the optimum unchanged. Induction
proves maximal size after all vertices. This shorter algorithm is verified
on C++; no claim is made about untested ports. Time `O(M(V+K))`, space
`O(V+K)`, where `V=M+N`, including initialization.

All five earlier Accepted layered BFS/DFS sources are retained. Their
searches continue until no augmenting path exists, which proves maximum
matching by symmetric difference. They do not restrict every successful
path to the shortest free-right distance: for rows `[1,2,3]`, `[2,3]`,
`[1]`, Python can take a five-edge path while a three-edge one exists.
Use the safe bound `O(L(V+K))` for these implementations, with current-arc
iterators and at most `L=min(M,N)` successful phases, rather than assuming
the strict shortest-path Hopcroft–Karp bound. Their space is `O(V+K)`.

## Optimized solutions

The new algorithm stores one adjacency bitset per left vertex,
orienting the smaller side as `L=min(M,N)` and the other as `R=max(M,N)`.
For each new left root, BFS searches an alternating path. First intersect
its neighbors with all free right vertices; a hit ends the search. Otherwise
all neighbors are matched: visit each unseen right vertex once, record its
left parent, and queue its unique matched left partner. The queue has at
most `L` entries. Flip parent links using the old matching until the free
root is reached. No free-right hit means no augmenting path, so the same
incremental-optimum argument proves maximum matching.

Duplicate edges set an existing bit. Unused bits in native final words
never appear in adjacency rows, so they cannot produce a false vertex.
With `B=ceil(R/w)`, a conservative bound is `O(K+L²B+LR)` word operations
and `O(LB+V)` words plus bounded I/O buffers. Native words have 64 bits;
Python uses arbitrary-precision limbs, not an assumed 64-bit integer.
When a scan has no free neighbor, there are at most `L` matched right
vertices to extract; this also bounds Python's repeated big-integer work.

Python builds mutable byte rows and converts each to an integer once,
avoiding a wide immutable copy per edge. Its 65536-byte input chunks retain
both unfinished integers and half-pairs across boundaries; native readers
use 4096-byte buffers. Output is one integer. The algorithm differs from
both teaching DFS and retained layered search, so it has its own approach name.

All five qualify by memory: C++ 280 KB versus the NEW simple C++'s 496 KB
(43.5% less), Go 1292/2512 (48.6%), Java 680/1264 (46.2%), Python 3868/8516
(54.6%), Rust 356/1820 (80.4%). C++'s 0.031→0.015 s is one tick and is not
reliable speedup evidence. Python records 0.140 versus 0.093 s, 50.5% more
time. Java/Go/Rust also record higher times, each by one tick. These are
memory improvements with explicit timing tradeoffs, not universal speedups.

## Language notes

The new C++ DFS is the preferred simple base; the old C++ layered
source remains an additional Accepted algorithm. Other families retain
their old simple bases. Every fast comparison uses the CURRENT same-language
base, including the new C++ Accepted. Python stays CPython 3.12.

In the 2 November 2026 snapshot, fast C++ is 1/1 against 74 filtered
other-author entries. Java is 3/1 against six, Python 11/12 against 25:
both keep stars and room for improvement. Go/Rust samples are empty and
provide formal coverage, not competitive evidence. C++ requires top15%
or first ten places in both metrics; other families require first in both.
Below-target admitted memory improvements remain valid with stars.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1109_dfs_matching.cpp](1109_dfs_matching.cpp) | G++ 13.2 x64 | dfs, matching | O(M(V+K)) | AC | 0.031 s | 496 KB | 11308433 |
| [1109_matching.go](1109_matching.go) | Go 1.14 x64 | matching | O(L(V+K)) | AC | 0.015 s | 2512 KB | 11279198 |
| [1109_matching.java](1109_matching.java) | Java 1.8 | matching | O(L(V+K)) | AC | 0.125 s | 1264 KB | 11279200 |
| [1109_matching.py](1109_matching.py) | Python 3.12 x64 | matching | O(L(V+K)) | AC | 0.093 s | 8516 KB | 11279199 |
| [1109_matching.rs](1109_matching.rs) | Rust 1.75 x64 | matching | O(L(V+K)) | AC | 0.015 s | 1820 KB | 11279201 |
| [1109_matching.cpp](1109_matching.cpp) | G++ 13.2 x64 | matching | O(L(V+K)) | AC | 0.062 s | 468 KB | 11279197 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1109_bfs_bitmask_matching.cpp](1109_bfs_bitmask_matching.cpp) | G++ 13.2 x64 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.015 s | 280 KB | 11308425 |
| [1109_bfs_bitmask_matching.go](1109_bfs_bitmask_matching.go) | Go 1.14 x64 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.031 s | 1292 KB | 11308428 |
| [1109_bfs_bitmask_matching.java](1109_bfs_bitmask_matching.java) \* | Java 1.8 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.140 s | 680 KB | 11308426 |
| [1109_bfs_bitmask_matching.py](1109_bfs_bitmask_matching.py) \* | Python 3.12 x64 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.140 s | 3868 KB | 11308424 |
| [1109_bfs_bitmask_matching.rs](1109_bfs_bitmask_matching.rs) | Rust 1.75 x64 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.031 s | 356 KB | 11308431 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
