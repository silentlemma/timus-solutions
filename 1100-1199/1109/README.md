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

Left labels satisfy 1<=a<=M and right labels 1<=b<=N.

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

`1109_bfs_bitmask_matching.py`. The answer remains the minimum edge cover M+N minus the maximum matching; the input guarantees no isolated vertex. Put L=min(M,N), R=max(M,N). A 4096-byte token reader carries both unfinished numbers and half edge pairs across blocks. Build integer adjacency masks by OR-ing precomputed right-vertex bits; repeated edges are idempotent. Breadth-first augmenting paths first test a free-neighbor mask, then visit each matched right vertex at most once per root. Parent links flip the path. With B=max(1,ceil(R/w)) integer limbs, a conservative bound is O(I+(K+LR)*B) time and O((L+R)*B) peak graph/mask storage, plus bounded input and matching arrays; wide Python operations are not constant time. Flush the one answer before os._exit(0) inside main. This retains the BFS/bitmask algorithm, distinct from the teaching DFS and retained layered search.

Exact-source Python 3.12 x64 Accepted #11327428: 0.093 s / 1412 KB.
The saved 2026-11-20 time/memory ranks 3/28 and 1/28 are historical;
current cached admission also confirms both applicable metrics. No
separate first-place target applies, and this row has no asterisk.
Earlier run #11308424 (0.14 s / 3868 KB) remains a separate historical
pair, not this source's current measurement.

- `1109_bfs_bitmask_matching.py`: 0.093 s / 1412 KB; retained teaching base `1109_matching.py`: 0.093 s / 8516 KB.

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

Native readers
use 4096-byte buffers. Output is one integer. The algorithm differs from
both teaching DFS and retained layered search, so it has its own approach name.

Historical measurements of previous revisions (memory gains, not admission): C++ 280 KB versus the NEW simple C++'s 496 KB
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

The 2 November 2026 places were historical comparisons, not current
admission evidence. The source-bound cached audit now confirms fast
C++/Go/Python/Rust and simple Go/Java/Rust. Fast Java still fails time
and retains its star; simple Java can cover that language without
duplication. Go uses a small exact-compiler cohort, while the other
qualifying sources use ordinary ranks. Fast C++/Rust compare time only
below 1 MiB; fast Go/Python compare both metrics. Empty cohorts never
prove numerical admission.

Current admission uses the shared [rating criteria](../../RATING_CRITERIA.md):
ordinary top-ten/top-15% comparisons or the exact-compiler small-cohort
reference when applicable, with time only below 1 MiB. A 30% gain and a
separate first-place language target are not admission criteria. Keep
meaningful teaching versions without optimization-target stars.

Their table receipts describe
the preceding bytes: C++ #11279197, Go #11279198, Java #11279200,
Python #11279199 and Rust #11279201. Algorithms, simple alternatives
and measured pairs are preserved; no submissions have been started.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1109_dfs_matching.cpp](1109_dfs_matching.cpp) | G++ 13.2 x64 | dfs, matching | O(M(V+K)) | AC | 0.031 s | 496 KB | 11308433 |
| [1109_matching.go](1109_matching.go) | Go 1.14 x64 | matching | O(L(V+K)) | AC | 0.031 s | 2500 KB | 11331019 |
| [1109_matching.java](1109_matching.java) | Java 1.8 | matching | O(L(V+K)) | AC | 0.109 s | 1244 KB | 11331047 |
| [1109_matching.py](1109_matching.py) | Python 3.12 x64 | matching | O(L(V+K)) | AC | 0.093 s | 7840 KB | 11331066 |
| [1109_matching.rs](1109_matching.rs) | Rust 1.75 x64 | matching | O(L(V+K)) | AC | 0.015 s | 1792 KB | 11331110 |
| [1109_matching.cpp](1109_matching.cpp) | G++ 13.2 x64 | matching | O(L(V+K)) | AC | 0.046 s | 452 KB | 11331142 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1109_bfs_bitmask_matching.cpp](1109_bfs_bitmask_matching.cpp) | G++ 13.2 x64 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.015 s | 280 KB | 11308425 |
| [1109_bfs_bitmask_matching.go](1109_bfs_bitmask_matching.go) | Go 1.14 x64 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.031 s | 1292 KB | 11308428 |
| [1109_bfs_bitmask_matching.java](1109_bfs_bitmask_matching.java) \* | Java 1.8 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.14 s | 680 KB | 11308426 |
| [1109_bfs_bitmask_matching.py](1109_bfs_bitmask_matching.py) | Python 3.12 x64 | bfs, bitmask, matching | O(I+(K+LR)*B) time; O((L+R)*B) peak state | AC | 0.093 s | 1412 KB | 11327428 |
| [1109_bfs_bitmask_matching.rs](1109_bfs_bitmask_matching.rs) | Rust 1.75 x64 | bfs, bitmask, matching | O(K+L²B+LR) | AC | 0.031 s | 356 KB | 11308431 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
