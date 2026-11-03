# 1205. The fastest way across town on foot and by subway

[Timus 1205](https://acm.timus.ru/problem.aspx?space=1&num=1205) · difficulty 234 · graphs

Original problem by Alexander Klepinin, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

You can walk anywhere at one speed or ride the subway at a speed at
least as high, between `2 ≤ N ≤ 200` stations joined by up to 400
straight two-way links; trains can be boarded, left and changed only at
stations, at no cost in time. Find the fastest way from point A to point
B and the stations it passes through.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The walking and subway speeds; `N` and the stations' coordinates; the
links as pairs of station numbers, ended by `0 0`; then A and B.

## Output

The least time, accurate to `10⁻⁶`, then the number of stations on the
route followed by the stations in the order they are visited.

## Checking

The repository checker verifies the optimum and a valid route/course pair; literal output equality is not required.

- `1205_graphs_optimized.java` (Java 1.8): 13 repository cases; 77 additional source-bound comparisons.

- `1205_graphs_optimized.py` (PyPy 3.10 x64): 13 repository cases.

- `1205_graphs_optimized.rs` (Rust 1.75 x64): 13 repository cases; 77 additional source-bound comparisons.

## Examples

### Example 1

Input:

```
1 100
4
0 0
1 0
9 0
9 9
1 2
1 3
2 4
0 0
10 10
10 0
```

Output:

```
2.6346295
4 4 2 1 3
```

## Solution

Make a complete graph on the stations, A and B: between any two points
the cost is the walking time, except between linked stations, where it is
the riding time; riding is never slower over the same straight line.
Dijkstra's algorithm on this dense graph of `N + 2` nodes, picking the
next node by a linear scan, gives the least time, and the predecessors
give the route; the stations on it are the route without A and B.
`O(N²)`.

Pitfalls:

- the route can be empty: with equal speeds, or when no subway trip
  helps, the answer is to walk straight and print `0` stations;
- walking between two stations is allowed and can be part of the best
  route, for example to change to another line nearby;
- the list of links can be empty, with `0 0` right after the stations.

The routes were compared with a separately written solution on 200
random cities and on every test, using the checker in both directions.

## Optimized solutions

Keep the readable matrix shortest-path sources. Compact variants run dense Dijkstra on the implicit complete geometric graph: compute a walking/train edge time with hypot only during relaxation, and retain predecessor IDs for the printed route. Subway membership is packed into bits instead of a real-valued time matrix. A station with no train edge can be omitted: replacing the two adjacent walking segments by their direct segment cannot increase time, by the triangle inequality. Thus keep the endpoints and stations incident to a train edge. Nonnegative travel times justify finalizing the minimum unvisited distance. Direct walking handles equal speeds, no train links or coincident endpoints. With K active vertices, time is O(N+M+K²); packed membership costs O(N²) bits plus O(N) numeric state. Robust hypot and original station labels are retained; any valid shortest route is accepted by the checker.

- `1205_graphs_optimized.java`: 0.093 s / 712 KB; base `1205_graphs.java`: 0.125 s / 1416 KB; relative change: time -25.6%, memory -49.7%.
- `1205_graphs_optimized.py`: 0.265 s / 636 KB; base `1205_graphs.py`: 0.062 s / 1012 KB; relative change: time +327.4%, memory -37.2%.
- `1205_graphs_optimized.rs`: 0.015 s / 208 KB; base `1205_graphs.rs`: 0.046 s / 344 KB; relative change: time -67.4%, memory -39.5%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1205_graphs.cpp`; covering source `1205_graphs.cpp`; time/memory places 1/1, other-author entries 83/83.

- Go: preferred teaching base `1205_graphs.go`; covering source `1205_graphs.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1205_graphs.java`; covering source `1205_graphs_optimized.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1205_graphs.py`; covering source `1205_graphs_optimized.py`; time/memory places 36/1, other-author entries 36/36.

- Rust: preferred teaching base `1205_graphs.rs`; covering source `1205_graphs_optimized.rs`; time/memory places 1/1, other-author entries 1/1.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1205_graphs.cpp](1205_graphs.cpp) | G++ 13.2 x64 | graphs | O(N²) | AC | 0.015 s | 256 KB | 11283587 |
| [1205_graphs.go](1205_graphs.go) | Go 1.14 x64 | graphs | O(N²) | AC | 0.031 s | 1208 KB | 11283588 |
| [1205_graphs.java](1205_graphs.java) | Java 1.8 | graphs | O(N²) | AC | 0.125 s | 1416 KB | 11283593 |
| [1205_graphs.py](1205_graphs.py) | Python 3.12 x64 | graphs | O(N²) | AC | 0.062 s | 1012 KB | 11283591 |
| [1205_graphs.rs](1205_graphs.rs) | Rust 1.75 x64 | graphs | O(N²) | AC | 0.046 s | 344 KB | 11283594 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1205_graphs_optimized.java](1205_graphs_optimized.java) | Java 1.8 | graphs | O(N+M+K²) time; O(N²) bits + O(N) numbers | AC | 0.093 s | 712 KB | 11309389 |
| [1205_graphs_optimized.py](1205_graphs_optimized.py) \* | PyPy 3.10 x64 | graphs | O(N+M+K²) time; O(N²) bits + O(N) numbers | AC | 0.265 s | 636 KB | 11309737 |
| [1205_graphs_optimized.rs](1205_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(N+M+K²) time; O(N²) bits + O(N) numbers | AC | 0.015 s | 208 KB | 11309390 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
