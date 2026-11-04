# 1320. Graph Decomposition

[Timus 1320](https://acm.timus.ru/problem.aspx?space=1&num=1320) · difficulty 283 · dsu

Original problem: idea by Alexander Petrov, prepared by Alexander Petrov and Leonid Volkov, from the Eighth Ural Team Student Programming Championship, Yekaterinburg, March 11–16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A simple graph has an even number of edges, from 2 to 1050, on vertices
numbered from 1 to 1000. Decide whether its edges can be split into
pairs of adjacent edges, that is, edges with a common vertex.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

The edges, each as a pair of vertex numbers, until the end of input.
There are no loops and no repeated edges.

## Output

1 if such a split exists, otherwise 0.

## Checking

Exact answer tokens. Each new source has its own full target-runtime checks, independent mathematical comparisons and source-bound Accepted; retained simple versions keep their own metrics.

## Examples

### Example 1

Input:

```
1 2
2 3
3 1
1 10
```

Output:

```
1
```

### Example 2

Input:

```
1 2
2 3
3 1
4 10
```

Output:

```
0
```

## Solution

Two adjacent edges always lie in the same connected component, so every
component needs an even number of edges. That is also enough: a
connected graph with an even number of edges can always be split. Take
a depth-first search tree and handle the vertices from the deepest up.
At a vertex v, pair the still free edges at v other than the one to its
parent; if one is left over, pair it with the edge to the parent,
otherwise the parent edge stays free for the parent. Every vertex but
the root leaves no free edges below it, and at the root the free edges
are paired among themselves, which works because the total is even.

So the answer only needs the number of edges in each component. A
disjoint set union over the vertices keeps it at each root: joining two
components adds their counts, and every edge adds one.
Finally, check that every root has an even count. Here V is the vertex
range and M is the number of edges. Roots are linked without rank or
size balancing, so path halving gives a safe total bound of
`O(V + M log V)`, including initialization and the final root scan.

Pitfalls:

- the whole graph always has an even number of edges, but a component
  may not: a triangle and a separate edge give 0 (test 02, also two
  separate triangles in test 06);
- the number of edges is not given, the input simply ends;
- two triangles sharing a vertex form one component of six edges and
  can be split (test 07).

The rule was compared with a search over all pairings on 487 random
graphs with up to 14 edges.

## Optimized solutions

Keep the original clear DSU sources. Pairing edges is possible exactly when each connected component has even edge count. Java stores positive parent links and root parity 0/-1 in one zero-initialized short array. An internal edge toggles parity; a merge takes both parities XOR one. Path shortening preserves components; labels 1..1000 fit short. A 512 byte buffer on standard input safely refills even inside a four-digit label, accepts arbitrary valid whitespace and EOF, and writes bytes directly. Python independently packs size and edge parity into a negative root value -(2*size+parity), uses size-based merging and maintains the number of odd components. Compare each exact source with its current same-language base. Java: O((V+M)log V)amortized/O(V)storage; Python: O((V+M)alpha(V))amortized, O(V+M)including input tokens.

PyPy also suppresses JIT compilation to reduce its code-cache memory; this can increase runtime.

- `1320_dsu_optimized.java`: 0.093 s / 408 KB; base `1320_dsu.java`: 0.109 s / 420 KB; relative change: time -14.7%, memory -2.9%.
- `1320_dsu_optimized.py`: 0.156 s / 436 KB; base `1320_dsu.py`: 0.093 s / 656 KB; relative change: time +67.7%, memory -33.5%.

## Language notes

The saved snapshots are from 1 and 4 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1320_dsu.cpp`; covering source `1320_dsu.cpp`; time/memory places 1/2, other-author entries 100/100.

- Go: preferred teaching base `1320_dsu.go`; covering source `1320_dsu.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1320_dsu.java`; covering source `1320_dsu_optimized.java`; time/memory places 1/1, other-author entries 5/5.

- Python/PyPy: preferred teaching base `1320_dsu.py`; covering source `1320_dsu_optimized.py`; time/memory places 34/1, other-author entries 34/34.

- Rust: preferred teaching base `1320_dsu.rs`; covering source `1320_dsu.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1320_dsu.cpp](1320_dsu.cpp) | G++ 13.2 x64 | dsu | O(V + M log V) | AC | 0.015 s | 184 KB | 11284943 |
| [1320_dsu.go](1320_dsu.go) | Go 1.14 x64 | dsu | O(V + M log V) | AC | 0.015 s | 1112 KB | 11284944 |
| [1320_dsu.java](1320_dsu.java) | Java 1.8 | dsu | O(V + M log V) | AC | 0.109 s | 420 KB | 11284946 |
| [1320_dsu.py](1320_dsu.py) | Python 3.12 x64 | dsu | O(V + M log V) | AC | 0.093 s | 656 KB | 11284945 |
| [1320_dsu.rs](1320_dsu.rs) | Rust 1.75 x64 | dsu | O(V + M log V) | AC | 0.015 s | 264 KB | 11284947 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1320_dsu_optimized.java](1320_dsu_optimized.java) | Java 1.8 | dsu | O((V+M) log V) amortized; O(V) storage | AC | 0.093 s | 408 KB | 11310097 |
| [1320_dsu_optimized.py](1320_dsu_optimized.py) \* | PyPy 3.10 x64 | dsu | O((V+M) alpha(V)) amortized; O(V+L) space, L=max line tokens | AC | 0.156 s | 436 KB | 11309751 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
