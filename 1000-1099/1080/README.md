# 1080. Colouring a map with two colours

[Timus 1080](https://acm.timus.ru/problem.aspx?space=1&num=1080) · difficulty 186 · bfs, graphs, dsu

Original problem by Emil Kelevedzhiev, from the Informatics Tournament of the Winter Mathematical Festival, Varna 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A map has `N` countries (`0 < N < 99`); every country can be reached
from every other one by crossing borders. Colour the countries red (0)
and blue (1) so that neighbours always differ, with country 1 red. Print
the colours as one string of digits, or `-1` if it cannot be done.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines: line `i` lists the neighbours of country `i` with
larger numbers and ends with 0.

## Output

The string of colours, or `-1`.

## Checking

The exact frozen Python candidate was rechecked against independent
BFS on all 27,476 connected labelled simple graphs with at most six
vertices, plus 701 random and maximum-size connected graphs. These
include odd cycles and the 98-vertex complete bipartite graph. The
oracle fixes country 1 to colour 0 and compares the unique answer,
or `-1`. This is an exhaustive small-graph proof by execution, not
exhaustive testing of all 98-vertex maps. Each of the four actual DSU
candidates also passed 11 repository inputs in Docker and has its own
exact-source Accepted. The 28,177 oracle inputs were Python executions,
not 28,177 runs of every compiled language.

## Examples

### Example 1

Input:

```
3
2 0
3 0
0
```

Output:

```
010
```

## Solution

A legal colouring is exactly a bipartition of the undirected border
graph. Although each input border is listed only at its smaller endpoint,
store it in both directions. Start BFS at country 1 with colour 0; assign
each new neighbour the opposite colour. A conflicting border proves
impossibility: the two BFS paths and that border yield an odd closed
walk and hence an odd cycle. Without conflicts every border has opposite
colours, so the result is valid. Connectivity ensures every country is
reached and the fixed first colour determines the unique colouring.

The readable BFS sources use `O(N + E)` time and storage, including
adjacency lists and the queue; `E` is the number of borders. Keep all
five original Accepted bases unchanged. Print digits without separators,
or `-1` for a conflict. A row containing only `0` adds no outgoing input
border, and `N = 1` is valid.

## Optimized solutions

The compact BFS implementation retains the usual opposite-color invariant with bounded queues and color storage. The Go alternative instead maintains a parity disjoint-set forest: each edge requires endpoint parities to differ. Path compression preserves parity to the representative, and a conflicting edge detects an odd cycle. Normalize the component containing the first country so its required color is fixed. Streaming edges avoids an adjacency list.

- `1080_dsu.cpp`: 0.015 s / 104 KB; base `1080_bfs.cpp`: 0.001 s / 284 KB; relative change: time -0.0%, memory -63.4%.
- `1080_dsu.java`: 0.078 s / 348 KB; base `1080_bfs.java`: 0.125 s / 5556 KB; relative change: time -37.6%, memory -93.7%.
- `1080_dsu.py`: 0.093 s / 524 KB; base `1080_bfs.py`: 0.078 s / 816 KB; relative change: time +19.2%, memory -35.8%.
- `1080_dsu.rs`: 0.046 s / 200 KB; base `1080_bfs.rs`: 0.031 s / 296 KB; relative change: time +48.4%, memory -32.4%.
- `1080_dsu.go`: 0.031 s / 780 KB; base `1080_bfs.go`: 0.031 s / 1364 KB; relative change: time -0.0%, memory -42.8%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1080_bfs.cpp`; covering source `1080_dsu.cpp`; time/memory places 1/1, other-author entries 542/541.

- Go: preferred teaching base `1080_bfs.go`; covering source `1080_dsu.go`; time/memory places 3/1, other-author entries 6/6.

- Java: preferred teaching base `1080_bfs.java`; covering source `1080_dsu.java`; time/memory places 1/1, other-author entries 128/128.

- Python/PyPy: preferred teaching base `1080_bfs.py`; covering source `1080_dsu.py`; time/memory places 69/9, other-author entries 113/113.

- Rust: preferred teaching base `1080_bfs.rs`; covering source `1080_dsu.rs`; time/memory places 2/1, other-author entries 1/1.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1080_bfs.cpp](1080_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + M) | AC | 0.001 s | 284 KB | 11279001 |
| [1080_bfs.go](1080_bfs.go) | Go 1.14 x64 | bfs | O(N + M) | AC | 0.031 s | 1364 KB | 11279002 |
| [1080_bfs.java](1080_bfs.java) | Java 1.8 | bfs | O(N + M) | AC | 0.125 s | 5556 KB | 11279004 |
| [1080_bfs.py](1080_bfs.py) | Python 3.12 x64 | bfs | O(N + M) | AC | 0.078 s | 816 KB | 11279003 |
| [1080_bfs.rs](1080_bfs.rs) | Rust 1.75 x64 | bfs | O(N + M) | AC | 0.031 s | 296 KB | 11279005 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1080_dsu.cpp](1080_dsu.cpp) | G++ 13.2 x64 | dsu | O((N+M) alpha(N)) | AC | 0.015 s | 104 KB | 11308353 |
| [1080_dsu.java](1080_dsu.java) | Java 1.8 | dsu | O((N+M) alpha(N)) | AC | 0.078 s | 348 KB | 11308358 |
| [1080_dsu.py](1080_dsu.py) \* | Python 3.12 x64 | dsu | O((N+M) alpha(N)) | AC | 0.093 s | 524 KB | 11308342 |
| [1080_dsu.rs](1080_dsu.rs) \* | Rust 1.75 x64 | dsu | O((N+M) alpha(N)) | AC | 0.046 s | 200 KB | 11308363 |
| [1080_dsu.go](1080_dsu.go) \* | Go 1.14 x64 | dsu | O((N+M) alpha(N)) | AC | 0.031 s | 780 KB | 11309360 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
