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

After distances from the first origin are known, fuse the second BFS with the bottleneck DP on shortest-path layers. FIFO order ensures that every predecessor layer is complete when a vertex is popped, so its best score is final then. Stop at the destination when popped, not at its first discovery. Flat adjacency arrays and one reusable queue replace nested containers; compact distance and score arrays retain the same linear graph algorithm.

- `2034_bfs_dp_optimized.cpp`: 0.031 s / 3228 KB; base `2034_bfs_dp.cpp`: 0.078 s / 6892 KB; relative change: time -60.3%, memory -53.2%.
- `2034_bfs_dp_optimized.py`: 0.468 s / 4072 KB; base `2034_bfs_dp.py`: 0.515 s / 28236 KB; relative change: time -9.1%, memory -85.6%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `2034_bfs_dp.cpp`; covering source `2034_bfs_dp_optimized.cpp`; time/memory places 1/1, other-author entries 137/137.

- Go: preferred teaching base `2034_bfs_dp.go`; covering source `2034_bfs_dp.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `2034_bfs_dp.java`; covering source `2034_bfs_dp.java`; time/memory places 1/1, other-author entries 5/5.

- Python/PyPy: preferred teaching base `2034_bfs_dp.py`; covering source `2034_bfs_dp_optimized.py`; time/memory places 5/1, other-author entries 11/11.

- Rust: preferred teaching base `2034_bfs_dp.rs`; covering source `2034_bfs_dp.rs`; time/memory places 1/1, other-author entries 0/0.

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

\* Accepted; the rating target is not yet met. This version may be optimized further.
