# 2034. The safest bottleneck among shortest routes

[Timus 2034](https://acm.timus.ru/problem.aspx?space=1&num=2034) · difficulty 283 · bfs, dp

Original problem by Oleg Merkurev, from the Ural Regional School Programming Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A connected simple undirected graph has unit-length edges. Three
distinct vertices `s,f,r` are given. A route must be a shortest path
from `s` to `f`. Its score is the smallest graph distance from `r` to
any vertex on that route, including both endpoints. Find the largest
possible score over all such shortest routes. Distances from `r` use all
graph edges, independently of the chosen route. A longer route cannot be
selected even if its score is larger.

Constraints: `3 ≤ n ≤ 100000`, `2 ≤ m ≤ 100000`, no loops or repeated edges.
The graph is connected. Time limit: 1 second; memory limit: 64 MB.

## Input

First `n m`, followed by `m` pairs of endpoints in `1..n`.
The last line is `s f r`, pairwise distinct.

## Output

One integer, the maximum of the minimum distance along a shortest route.
Zero is valid when every shortest route contains `r`. The endpoints are possible
nearest vertices and must be included.

## Checking

Outputs are compared token by token.

## Examples

```
7 7
1 2
2 4
2 5
3 4
4 6
5 6
6 7
1 7 3
```

```
2
```

## Solution

Run BFS from `s`, obtaining distances `ds` and visitation order. Run BFS
from `r` to obtain clearances `dr`. Orient a usable edge `u→v` only when
`ds[v]=ds[u]+1`. These edges form a directed acyclic graph ordered by
BFS layers.

Let `best[v]` be the largest minimum clearance among all shortest paths from
`s` to `v`. Initialize `best[s]=dr[s]` and the other entries to `-1`.
Process vertices in the BFS order from `s`. For each usable edge, update
`best[v]=max(best[v],min(best[u],dr[v]))`. Output `best[f]`.

### Correctness

Every prefix of a shortest route is itself shortest: replacing a longer prefix
would shorten the full route. Thus every route edge increases `ds` by one.
Conversely, any path from `s` to `f` consisting of such edges has exactly
`ds[f]` edges and is shortest.

The initial value includes the starting vertex. Every shortest path to `v`
ends at a predecessor `u` in the previous BFS layer, with score equal to the
minimum of its prefix score and `dr[v]`. This minimum is monotone in the
prefix score, so keeping only the best prefix at each `u` loses no candidate.
Taking the maximum over all predecessors gives exactly `best[v]`.
BFS order processes every predecessor first; induction proves the answer at `f`.

Vertices outside all shortest `s-f` routes may also be processed. They
can affect `f` only through a path of strictly increasing layers, which
would itself be a valid shortest route. Their presence therefore does
not change the result.

In the sample, route `1-2-4-6-7` has minimum distance one from vertex 3,
attained at vertex 4. Route `1-2-5-6-7` has minimum two, attained at 2 or 6.
The maximum of the two route scores is two.

Two BFS traversals and one edge scan take `O(n+m)` time. Adjacency, distance,
order and dynamic-programming arrays use `O(n+m)` memory.

Pitfalls:

- Maximize over routes after taking the minimum over a route's vertices.
- Restrict transitions to an increase of exactly one BFS layer.
- Use full-graph distances from `r` and include `s` and `f` in each score.
- Zero is a legitimate result when `r` cannot be avoided on shortest routes.
- A safer detour with more edges is not a valid competitor.

## Optimized solutions

`2034_bfs_dp_optimized.rs`. Keep two BFS distance arrays and the max–min DP restricted to edges that advance one shortest-path layer. Flat u32 forward-star edges replace nested adjacency vectors and the retained endpoint list; reuse one BFS order vector and direct output. Connected-graph distances fit u32, with MAX reserved for unreached. O(N+M) time and storage, preserving the simple graph/BFS derivation.

Compared with `2034_bfs_dp.rs`: time 0.078 s → 0.062 s; memory 13112 KB → 3 448 KB.

`2034_bfs_dp_optimized.go`. Keep two BFS traversals and the bottleneck DP over edges that increase distance from s by one. In BFS order, best[v] is the largest minimum distance from r attainable along a shortest s-to-v path; propagate min(best[v],clearance[u]) and maximize at u. Store the graph directly in flat int32 first/to/next arrays as edges arrive, avoiding the original separate edge-pair list and nested native-int slices. Distances, queues and DP values use int32, safe for n,m<=100000; both BFS routines still allocate their own arrays. The graph is connected, so every required distance is defined. Time and storage O(n+m). Portable os.Stdin.Read/os.Stdout.Write and direct integer conversion use fixed 4096-byte input and output buffers. Partial writes are handled before reusing the output buffer. The original simple Accepted source is preserved.

Compared with `2034_bfs_dp.go`: time 0.109 s → 0.031 s; memory 11080 KB → 5244 KB.

After distances from the first origin are known, fuse the second BFS with the bottleneck DP on shortest-path layers. FIFO order ensures that every predecessor layer is complete when a vertex is popped, so its best score is final then. Stop at the destination when popped, not at its first discovery. Flat adjacency arrays and one reusable queue replace nested containers; compact distance and score arrays retain the same linear graph algorithm.

- `2034_bfs_dp_optimized.cpp`: 0.031 s / 3228 KB; base `2034_bfs_dp.cpp`: 0.078 s / 6892 KB; relative change: time -60.3%, memory -53.2%.
- `2034_bfs_dp_optimized.py`: 0.468 s / 4072 KB; base `2034_bfs_dp.py`: 0.515 s / 28236 KB; relative change: time -9.1%, memory -85.6%.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`2034_bfs_dp_optimized.go`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2034_bfs_dp.cpp](2034_bfs_dp.cpp) | G++ 13.2 x64 | bfs, dp | O(n+m) | AC | 0.078 s | 6892 KB | 11293137 |
| [2034_bfs_dp.go](2034_bfs_dp.go) | Go 1.14 x64 | bfs, dp | O(n+m) | AC | 0.109 s | 11080 KB | 11293143 |
| [2034_bfs_dp.java](2034_bfs_dp.java) | Java 1.8 | bfs, dp | O(n+m) | AC | 0.171 s | 8272 KB | 11309217 |
| [2034_bfs_dp.py](2034_bfs_dp.py) | Python 3.12 x64 | bfs, dp | O(n+m) | AC | 0.515 s | 28236 KB | 11293145 |
| [2034_bfs_dp.rs](2034_bfs_dp.rs) | Rust 1.75 x64 | bfs, dp | O(n+m) | AC | 0.078 s | 13112 KB | 11293149 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2034_bfs_dp_optimized.cpp](2034_bfs_dp_optimized.cpp) | G++ 13.2 x64 | bfs, dp | O(N+M) | AC | 0.031 s | 3228 KB | 11309340 |
| [2034_bfs_dp_optimized.py](2034_bfs_dp_optimized.py) \* | Python 3.12 x64 | bfs, dp | O(N+M) | AC | 0.468 s | 4072 KB | 11309323 |
| [2034_bfs_dp_optimized.go](2034_bfs_dp_optimized.go) \* | Go 1.14 x64 | bfs, dp | O(n+m) | AC | 0.031 s | 5244 KB | 11328337 |
| [2034_bfs_dp_optimized.rs](2034_bfs_dp_optimized.rs) \* | Rust 1.75 x64 | bfs, dp | O(N+M) time; O(N+M) space | AC | 0.062 s | 3448 KB | 11325553 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
