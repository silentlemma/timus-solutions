# 2109. Common ancestor of a range of consecutive vertices

[Timus 2109](https://acm.timus.ru/problem.aspx?space=1&num=2109) · difficulty 533 · trees, dp

Original problem by Vladimir Leskov, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tree has n vertices rooted at vertex 1. A route [L, R] walks from L to
L + 1, then to L + 2 and so on up to R, always along tree paths. For each
of q routes print the visited vertex closest to the root. The limits are
4 seconds and 300 MB.

## Input

n, 1 ≤ n ≤ 2 · 10⁵, the n − 1 edges, then q, 0 ≤ q ≤ 10⁶, and the
routes L ≤ R.

## Output

The answer for each route, one per line.

## Examples

### Example 1

Input:

```
7
1 2
1 3
2 4
2 5
2 6
3 7
3
4 6
3 4
5 7
```

Output:

```
2
1
1
```

### Example 2

Input:

```
7
1 3
3 5
5 6
7 5
1 4
2 4
3
4 5
5 6
6 7
```

Output:

```
1
5
5
```

## Solution

The walk covers exactly the minimal subtree that joins L, L + 1, …, R,
and the vertex of that subtree closest to the root is the lowest common
ancestor of the whole range. That ancestor is the shallowest of the
pairwise ancestors LCA(i, i + 1) for L ≤ i < R: every one of them lies
inside its subtree, and the path between two vertices on different
child branches has to pass through it.

So compute c(i) = LCA(i, i + 1) for all i once, offline, with Tarjan's
method: during a depth-first search a finished vertex is merged into its
parent, and when vertex v is entered the representative of an already
visited neighbour i ± 1 is their common ancestor. Among ancestors of one
vertex the shallowest has the smallest preorder number, so store the
preorder of c(i) and answer every route with a range-minimum query on a
sparse table, in O(1) each. L = R is answered by L itself.

The search is iterative, since the tree can be a path of 2 · 10⁵
vertices. The total time is O(n log n + q).

In the first example the route 4 → 5 → 6 stays below vertex 2, and the
routes 3 → 4 and 5 → 6 → 7 go through the root.

The teaching C++ version finds depths and parents by breadth-first search. It builds a table of ancestors at distances 1, 2, 4, and so on. To find LCA(i, i + 1), first lift the deeper vertex to the same depth. If they meet, that vertex is the LCA. Otherwise lift both with the largest jumps that keep them distinct, then take their parent. Put each adjacent pair’s LCA in a segment tree ordered by depth. The query [L, R] takes the minimum over pairs starting at L through R − 1. If L = R, the answer is L. The time is O((n + q) log(n + 1)) and space is O(n log(n + 1)).

## Optimized solutions

Go and CPython retain the original iterative adjacent-city Tarjan/DSU preprocessing and sparse-table minimum of preorder positions. A visited subtree points to its nearest active ancestor on exit, so querying an already seen numeric neighbor obtains their LCA. Let a be the lowest common ancestor of the cities in [L, R]. For L < R, some adjacent pair has LCA a. If a is in the range, use a pair containing it. Otherwise the sequence of cities must cross from one child subtree of a to another. Every adjacent-pair LCA lies in the subtree of a, so a has the smallest preorder number and is the answer. The new ports store graph heads/edges, parent/representative/preorder, order and RMQ values in 32-bit arrays. A signed 32-bit event stack handles entry and exit. Preorder zero means unseen, and stored positions are converted back to zero-based for RMQ. Temporary graph/DFS arrays become unnecessary before RMQ allocation. Query tokens and answers use bounded buffers. For L = R, return L directly. With q = 0, skip DFS and RMQ construction. Go computes the table level with bits.Len. Python splits 65,536-byte chunks, carries an unfinished token forward, and flushes every 8192 answers. Its sparse table uses typed unsigned arrays. Edge indices reach at most 399,998, and event magnitudes at most 200,000. Time is O(n log n + q) and space is O(n log n). C++, Java and Rust reuse their admitted bases.

The accepted Python 3.12 x64 run takes 2.984 s versus 2.875 s for the base and uses 19 348 KB versus 222288 KB.

The accepted base implementations [2109_trees_dp.cpp](2109_trees_dp.cpp), [2109_trees_dp.java](2109_trees_dp.java), [2109_trees_dp.rs](2109_trees_dp.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2109_trees_dp.cpp](2109_trees_dp.cpp) | G++ 13.2 x64 | trees, dp | O(n log n + q) | AC | 0.406 s | 26432 KB | 11294864 |
| [2109_trees_dp.go](2109_trees_dp.go) | Go 1.14 x64 | trees, dp | O(n log n + q) | AC | 0.296 s | 98064 KB | 11294866 |
| [2109_trees_dp.java](2109_trees_dp.java) | Java 1.8 | trees, dp | O(n log n + q) | AC | 0.437 s | 17600 KB | 11328341 |
| [2109_trees_dp.py](2109_trees_dp.py) | Python 3.12 x64 | trees, dp | O(n log n + q) | AC | 2.875 s | 222288 KB | 11294869 |
| [2109_trees_dp.rs](2109_trees_dp.rs) \* | Rust 1.75 x64 | trees, dp | O(n log n + q) | AC | 0.359 s | 77192 KB | 11294872 |
| [2109_trees_segment_tree.cpp](2109_trees_segment_tree.cpp) | G++ 13.2 x64 | trees, segment_tree | O((n + q) log(n + 1)) | AC | 0.953 s | 29604 KB | 11315899 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2109_trees_dp_optimized.go](2109_trees_dp_optimized.go) \* | Go 1.14 x64 | trees, dp | O(n log n + q) | AC | 0.25 s | 21888 KB | 11315683 |
| [2109_trees_dp_optimized.py](2109_trees_dp_optimized.py) \* | Python 3.12 x64 | trees, dp | O(n log n + q) | AC | 2.984 s | 19348 KB | 11315684 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
