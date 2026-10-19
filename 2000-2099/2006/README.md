# 2006. Blocking the Most Critical Grid Cell

[Timus 2006](https://acm.timus.ru/problem.aspx?space=1&num=2006) · difficulty 3676 · graphs, shortest_paths

Original problem by Ilya Kuchumov. (Prepared by Oleg Merkurev), from the Ural Regional School Programming Contest 2013.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A rectangular grid has free cells `.` and blocked cells `#`. Moves
between free cells sharing a side cost one. Two distinct free cells are
the start and target, initially connected. Block exactly one other free
cell to maximize the new shortest-path length. Disconnecting the
endpoints is better than every finite distance. Output any best cell. At
least one legal cell to block exists, including possibly a cell in
another component.

## Input

Integers `n m`, with `2 ≤ n,m ≤ 1000` and `n·m ≤ 100000`. The next two
lines give the start and target as `row column`, numbered from 1 at the
top left. The following `n` rows contain `m` characters each, only `.`
or `#`; both endpoints are free and distinct, their initial path exists,
and there are at least three free cells. Time 2 seconds, memory 128 MB.

## Output

The row and column of a free nonendpoint cell whose deletion maximizes
the shortest distance, giving disconnection highest priority. Ties are
arbitrary.

## Checking

A checker blocks the printed cell, runs BFS and compares the new
distance, or the disconnection, with the optimum; any best cell is
accepted.

## Examples

```
4 4
1 1
4 4
..##
#.##
#...
###.
```

```
2 2
```

Removing `(2,2)` breaks the only passage between the endpoints, which is
optimal.

## Solution

Let `P[0..k]` be one shortest start-to-target path. Deleting a cell
outside `P` leaves this path, so it cannot increase distance. Only the
internal path cells need examination. If `k=1`, the endpoints are
adjacent: return any other free cell.

Run BFS from the start to obtain distances `ds` and a tree containing
`P`, and from the target to obtain `dt`. The level `λ(v)` is the index
of the last vertex of `P` on the tree path to `v`. Assign levels in BFS
order. For a possible failed cell `P[i]`, partition the remaining
reachable component into `R` with level below `i`, `V` with level `i`
excluding `P[i]`, and `S` with level above `i`.

A shortest prefix to a vertex of `R` stays in `R`. For `y` in `S`, write
`j=λ(y)>i`. Following its tree branch to `P[j]` and then the path to the
target costs `ds[y]+k−2j`. Any route through `P[i]` costs at least
`ds[y]+k−2i`, which is strictly larger. Consequently a shortest suffix
of length `dt[y]` avoids the failed cell.

There are two ways to cross from `R∪V` to `S`. For an edge `x–y` with
`λ(x)<i<λ(y)`, the candidate is `ds[x]+1+dt[y]`. This one edge offers
the same cost to every internal path index strictly between its endpoint
levels. Those are interval offers.

For the other case, `x` belongs to `V`, so its ordinary shortest prefix
might use the failed cell. Compute a corrected prefix `detour[x]`: every
off-path vertex `v` gets seed `min(ds[u]+1)` over neighbors `u` of lower
level. Run multi-source Dijkstra, allowing propagation only between
off-path vertices of the same level. All these level regions are
disjoint. Then an edge from off-path `x` to higher-level `y` offers
`detour[x]+1+dt[y]` specifically for failure index `λ(x)`.

Why is this corrected prefix exact? In any path restricted to `R∪V`,
consider its last entry from `R` to `V`. Its prefix is bounded below by
the corresponding seed, and the remainder stays within `V`. Conversely
every seeded Dijkstra path has a valid prefix in `R` and avoids the
failed cell. Every replacement path must cross the cut to `S`; the two
types above exhaust that crossing. Their minimum therefore equals the
replacement distance, including infinity if no offer exists.

Sort interval offers by their left endpoint and sweep path indices,
keeping a heap of `(cost,right endpoint)`. Insert intervals that have
started and discard expired heap minima. Combine the cheapest active
interval with the point offers. Choose the path cell with largest
resulting distance.

This uses the node-avoiding reduction of [Lee and Lu, section
2.2](https://arxiv.org/html/1310.8062#S2.SS2), implemented here with
ordinary Dijkstra and interval heaps. No linear-time matrix-minimum
routine is needed. With `N=n·m` and at most `2N` undirected grid edges,
time is `O(N log N)` and memory `O(N)`. Padding makes neighbor access
simple; unreachable components do not participate in the computation.

An edge-failure shortcut alone is insufficient for deleting a vertex:
same-level detours are essential. Intervals exclude both endpoint
levels; the lower-level point offer excludes the path vertex itself.
Never block either endpoint. Disconnection outranks every finite length.
If endpoints are adjacent, a valid third cell can even be disconnected
initially. Count moves, not visited vertices, and preserve row/column
order.

## Language notes

All ports use iterative BFS, a padded flat grid, sparse crossing-edge
records and heaps; there is no deep recursion on a long corridor.
Distances and the named infinity sentinel fit signed 32-bit arithmetic.
Rust checks unsigned missing-level markers before comparisons. Python
writes only the selected coordinates. Full-program time and memory are
measured before readiness is published.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2006_graphs_shortest_paths.cpp](2006_graphs_shortest_paths.cpp) | G++ 13.2 x64 | graphs, shortest_paths | O(N log N) | AC | 0.031 s | 5332 KB |
| [2006_graphs_shortest_paths.go](2006_graphs_shortest_paths.go) | Go 1.14 x64 | graphs, shortest_paths | O(N log N) | AC | 0.062 s | 19532 KB |
| [2006_graphs_shortest_paths.java](2006_graphs_shortest_paths.java) | Java 1.8 | graphs, shortest_paths | O(N log N) | AC | 0.218 s | 11892 KB |
| [2006_graphs_shortest_paths.py](2006_graphs_shortest_paths.py) | Python 3.12 x64 | graphs, shortest_paths | O(N log N) | AC | 0.578 s | 33312 KB |
| [2006_graphs_shortest_paths.rs](2006_graphs_shortest_paths.rs) | Rust 1.75 x64 | graphs, shortest_paths | O(N log N) | AC | 0.031 s | 9068 KB |
