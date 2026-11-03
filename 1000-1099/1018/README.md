# 1018. Keeping the most valuable connected branches of a binary tree

[Timus 1018](https://acm.timus.ru/problem.aspx?space=1&num=1018) · difficulty 281 · dp, graphs, trees

Original problem from the Ural State University Internal Contest '99 #2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tree has `N` vertices (`2 ≤ N ≤ 100`) numbered `1..N` with the root `1`;
every vertex has zero or two children. Each of the `N - 1` edges (branches)
carries between 0 and 30 000 apples. Keep exactly `Q` branches
(`1 ≤ Q ≤ N - 1`) so that they stay connected to the root, i.e. a removed
branch takes everything above it away, and the number of apples on the kept
branches is as large as possible. Print that number.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `Q`, then `N - 1` lines `a b c`: a branch between the vertices `a`
and `b` (in any order) with `c` apples.

## Output

The largest number of apples.

## Checking

Compare the exact answer tokens; whitespace formatting is immaterial.

- `1018_dp_graphs.java` (Java 1.8): 12 repository cases; 514 additional source-bound comparisons.

- `1018_dp_graphs.py` (PyPy 3.10 x64): 12 repository cases.

## Examples

### Example 1

Input:

```
7 3
1 2 1
1 3 5
2 4 9
2 5 9
3 6 2
3 7 3
```

Output:

```
19
```

### Example 2

Input:

```
3 1
2 1 30000
1 3 0
```

Output:

```
30000
```

## Solution

The kept branches form a subtree that contains the root. Root the tree at 1
(the input gives the edges in arbitrary direction) and compute, for every
vertex `v`, the table `best_v[k]`: the most apples on `k` branches kept in
the subtree of `v`, connected to `v`.

**Tree knapsack.** Start with `best = [0]` (nothing kept). For each child
`c` of `v` with `w` apples on the edge `v–c`: keeping `j ≥ 1` branches on
that side means keeping the edge itself and `j - 1` branches below `c`,
worth `w + best_c[j - 1]`. Merge it into the current table like a knapsack:

`new[i + j] = max(new[i + j], best[i] + (j = 0 ? 0 : w + best_c[j - 1]))`.

The answer is `best_1[Q]`. Cutting every table at `Q + 1` entries, the merges
cost `O(N · Q^2)` in total — at most about `10^6` steps; with the tables
limited to the subtree sizes it is even `O(N^2)`.

Why connectivity is kept: a branch below `c` is counted only together with
the edge `v–c` (the case `j ≥ 1`), so no kept branch hangs in the air.

Pitfalls:

- the input tree must have zero or two children per vertex, so the smallest
  valid input has three vertices; keeping just one branch is allowed (test 02);
- an edge may be given as "child parent": build an undirected adjacency list
  and root it by a DFS from 1;
- a greedy choice of the heaviest available branch fails: a light branch
  may lead to heavy ones.

## Optimized solutions

Keep the tree-knapsack teaching sources. Flatten the rooted tree in preorder; a nonroot vertex and its descendants form one interval [pos,end), whose incoming edges have exactly that interval's weights. In maximum-kept mode, keep the current edge and advance one position, or skip its entire subtree. In minimum-removed mode, keep it for zero removals, or remove the complete interval and its prefix-sum weight. A skipped ancestor jumps over all descendants, so every reached position already has its ancestors kept; no additional ancestor state is needed. Use K=min(Q,N-1-Q), maximize Q kept edges or minimize the complementary removed weight, then subtract that loss from the total. Each cell has two transitions: O(N(1+K)) time/space including graph/index preparation. Keeping all edges returns the input weight sum directly. Python uses native integer-list storage under the recorded PyPy runtime.

- `1018_dp_graphs.java`: 0.125 s / 368 KB; base `1018_dp_trees.java`: 0.140 s / 1912 KB; relative change: time -10.7%, memory -80.8%.
- `1018_dp_graphs.py`: 0.125 s / 408 KB; base `1018_dp_trees.py`: 0.078 s / 596 KB; relative change: time +60.3%, memory -31.5%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1018_dp_trees.cpp`; covering source `1018_dp_trees.cpp`; time/memory places 1/1, other-author entries 126/126.

- Go: preferred teaching base `1018_dp_trees.go`; covering source `1018_dp_trees.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1018_dp_trees.java`; covering source `1018_dp_graphs.java`; time/memory places 4/1, other-author entries 4/4.

- Python/PyPy: preferred teaching base `1018_dp_trees.py`; covering source `1018_dp_graphs.py`; time/memory places 11/1, other-author entries 13/13.

- Rust: preferred teaching base `1018_dp_trees.rs`; covering source `1018_dp_trees.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1018_dp_trees.cpp](1018_dp_trees.cpp) | G++ 13.2 x64 | dp, trees | O(N · Q^2) | AC | 0.015 s | 212 KB | 11278199 |
| [1018_dp_trees.go](1018_dp_trees.go) | Go 1.14 x64 | dp, trees | O(N · Q^2) | AC | 0.031 s | 1152 KB | 11278201 |
| [1018_dp_trees.java](1018_dp_trees.java) | Java 1.8 | dp, trees | O(N · Q^2) | AC | 0.140 s | 1912 KB | 11278206 |
| [1018_dp_trees.py](1018_dp_trees.py) | Python 3.12 x64 | dp, trees | O(N · Q^2) | AC | 0.078 s | 596 KB | 11278203 |
| [1018_dp_trees.rs](1018_dp_trees.rs) | Rust 1.75 x64 | dp, trees | O(N · Q^2) | AC | 0.015 s | 260 KB | 11278211 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1018_dp_graphs.java](1018_dp_graphs.java) \* | Java 1.8 | dp, graphs | O(N(1+min(Q,N-1-Q))) time and space | AC | 0.125 s | 368 KB | 11309309 |
| [1018_dp_graphs.py](1018_dp_graphs.py) \* | PyPy 3.10 x64 | dp, graphs | O(N(1+min(Q,N-1-Q))) time and space | AC | 0.125 s | 408 KB | 11309731 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
