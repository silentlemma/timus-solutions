# 1022. Ordering a family so that ancestors come first

[Timus 1022](https://acm.timus.ru/problem.aspx?space=1&num=1022) · difficulty 142 · graphs, bfs, dfs

Original problem from the Second Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 7, 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` members (`1 ≤ N ≤ 100`), numbered `1..N`, are related by parent-child
links: a member may have any number of parents and children, and there are
no cycles. Print an order of all members in which every member comes before
all of its descendants. Any such order is accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines: the `i`-th lists the children of member `i` in any
order and ends with `0` (a line with just `0` means no children).

## Output

The `N` numbers in the chosen order, separated by spaces.

## Checking

Any valid order is accepted. The checker verifies that the output is a
permutation of `1..N` and that every member comes before each of its
children (which gives "before all descendants" by induction).

## Examples

### Example 1

Input:

```
4
0
1 0
1 4 0
1 0
```

Output:

```
2 3 4 1
```

### Example 2

Input:

```
1
0
```

Output:

```
1
```

## Solution

The members and the links form a directed acyclic graph, and the required
order is a **topological order** of it.

**Kahn's algorithm (BFS).** Count the parents of every member. Members
without parents can speak first; put them in a queue. Take members from the
queue one by one; for each of its children decrease the parent count, and a
child whose count drops to zero joins the queue — all its parents have
already spoken. The queue in the order of insertion is the answer.

**Depth-first search.** Run a DFS from every unvisited member and append a
member to a list when its DFS finishes, i.e. after all of its descendants.
The reversed list puts every member before its descendants.

Both are `O(N + E)`, where `E` is the number of links — at most about
5 000 here.

Pitfalls:

- the input lists children, not parents: count in-degrees from the lists;
- a line with just `0` is an empty list, not the end of the input.

## Optimized solutions

`1022_bfs_graphs_optimized.java`. Java keeps Kahn topological sorting, but each adjacency row is packed into long words rather than boolean cells. A repeated child is ignored before increasing indegree. Dequeue each zero-indegree vertex and scan only set bits of its child words with numberOfTrailingZeros and bits&=bits-1, adding a child when its indegree becomes zero. An int array serves as the queue and answer; no boxed vertex lists or StringBuilder are used. Separate 4096-byte input/output buffers parse and emit decimal values directly through ordinary streams. With E listed edges, time O(N*ceil(N/64)+E), storage O(N*ceil(N/64)+N), plus fixed byte buffers. Teaching Kahn and DFS sources remain unchanged.

Exact-source Java 1.8 Accepted #11327520: 0.078 s / 380 KB. Saved 2026-11-20 compiler-cohort comparison: time 5/179, memory 2/179. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11304481 was 0.093 s / 360 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1022_bfs_graphs_optimized.java`: 0.078 s / 380 KB; retained teaching base `1022_bfs_graphs.java`: 0.125 s / 1828 KB.

`1022_bfs_graphs.py`. Keep Kahn topological sorting, indegrees and one growing list used as both FIFO and answer. With at most 100 vertices, split the whole bounded byte input once instead of using Python chunk/token generators. Each edge and vertex is still processed once: O(V+E) time and storage including input. Flush before direct exit. The different DFS teaching algorithm remains unchanged.

Exact-source CPython 3.12 Accepted #11327003: 0.062 s / 724 KB. Comparison saved 2026-11-20 on the current language-family compiler cohort: time rank 4/54, memory rank 44/54. Below 1024 KB, strict admission uses time only.

- `1022_bfs_graphs.py`: 0.062 s / 724 KB; retained teaching base `1022_dfs_graphs.py` (Python 3.12 x64): 0.078 s / 512 KB; time change -20.5%; memory change +41.4%.

Compared with `1022_dfs_graphs.py`: time 0.078 s → 0.093 s; memory 512 KB → 256 KB.

The optimized C++ solution of Kahn's algorithm keeps the links in a
fixed `bool` matrix of 101 × 101 cells, about 10 KB since `N ≤ 100`, and
the queue in a fixed array, instead of a `vector` of `vector`s that
grows with every link. Taking a member from the queue, it scans the
whole row of the matrix, `O(N²)` in total, which costs nothing for 100
members: {1022_bfs_graphs_optimized.cpp}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1022_bfs_graphs_optimized.cpp`: time reduction +0.00%; memory
  reduction +45.10%; base: `1022_bfs_graphs.cpp`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1022_bfs_graphs.go](1022_bfs_graphs.go).
- [1022_dfs_graphs.rs](1022_dfs_graphs.rs).

- **C++**, **Go**, **Java**: Kahn's algorithm.
- **C++**, **Rust**: recursive DFS (the depth is at most 100); **Python**:
  the same DFS with an explicit stack of iterators.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1022_bfs_graphs.cpp](1022_bfs_graphs.cpp) | G++ 13.2 x64 | bfs, graphs | O(N + E) | AC | 0.015 s | 204 KB | 11278266 |
| [1022_dfs_graphs.cpp](1022_dfs_graphs.cpp) | G++ 13.2 x64 | dfs, graphs | O(N + E) | AC | 0.015 s | 196 KB | 11278269 |
| [1022_bfs_graphs.go](1022_bfs_graphs.go) | Go 1.14 x64 | bfs, graphs | O(N + E) | AC | 0.015 s | 1124 KB | 11278272 |
| [1022_bfs_graphs.java](1022_bfs_graphs.java) | Java 1.8 | bfs, graphs | O(N + E) | AC | 0.125 s | 1828 KB | 11278276 |
| [1022_dfs_graphs.py](1022_dfs_graphs.py) | Python 3.12 x64 | dfs, graphs | O(N + E) | AC | 0.078 s | 512 KB | 11278274 |
| [1022_dfs_graphs.rs](1022_dfs_graphs.rs) | Rust 1.75 x64 | dfs, graphs | O(N + E) | AC | 0.015 s | 236 KB | 11278277 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1022_bfs_graphs_optimized.cpp](1022_bfs_graphs_optimized.cpp) | G++ 13.2 x64 | bfs, graphs | O(N²) | AC | 0.015 s | 112 KB | 11304480 |
| [1022_bfs_graphs_optimized.java](1022_bfs_graphs_optimized.java) | Java 1.8 | bfs, graphs | O(N ceil(N/64) + E) time; O(N ceil(N/64) + N) space | AC | 0.078 s | 380 KB | 11327520 |
| [1022_bfs_graphs.py](1022_bfs_graphs.py) | Python 3.12 x64 | bfs, graphs | O(V+E) time; O(V+E) space | AC | 0.062 s | 724 KB | 11327003 |
