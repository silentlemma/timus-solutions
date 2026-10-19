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

## Language notes

All traversals are iterative, so a 100000-vertex path does not require
recursion. Java uses primitive adjacency and queue arrays; Go uses
buffered byte input. Python reads edges line by line into a compact
endpoint array before reading the last terminal triple, then constructs
adjacency through an iterator. Rust retains the input text and parses by
iterator. Every variant stays within `O(n+m)` storage; distances and
scores fit signed 32-bit integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2034_bfs_dp.cpp](2034_bfs_dp.cpp) | G++ 13.2 x64 | bfs, dp | O(n+m) | AC | 0.078 s | 6892 KB |
| [2034_bfs_dp.go](2034_bfs_dp.go) | Go 1.14 x64 | bfs, dp | O(n+m) | AC | 0.109 s | 11080 KB |
| [2034_bfs_dp.java](2034_bfs_dp.java) | Java 1.8 | bfs, dp | O(n+m) | AC | 0.125 s | 8304 KB |
| [2034_bfs_dp.py](2034_bfs_dp.py) | Python 3.12 x64 | bfs, dp | O(n+m) | AC | 0.515 s | 28236 KB |
| [2034_bfs_dp.rs](2034_bfs_dp.rs) | Rust 1.75 x64 | bfs, dp | O(n+m) | AC | 0.078 s | 13112 KB |
