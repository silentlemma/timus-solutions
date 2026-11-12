# 1198. Which senators can pass a law on their own

[Timus 1198](https://acm.timus.ru/problem.aspx?space=1&num=1198) · difficulty 489 · graphs

Original problem by Nikita Rybak.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Each of `N ≤ 2000` senators keeps compromising files on some of the
others. A senator who wants a law calls everyone they hold files on and
asks them to support it and to make the same calls in turn. A law passes
when every senator supports it. Find all senators who can get a law
passed this way on their own.

Time limit: 1.5 seconds. Memory limit: 96 MB.

## Input

`N`, then one line per senator listing the senators they hold files on,
ended by `0`.

## Output

The numbers of those senators in increasing order on one line, followed
by `0`; just `0` when there are none.

## Examples

### Example 1

Input:

```
5
3 2 0
0
4 5 0
1 5 0
2 0
```

Output:

```
1 3 4 0
```

## Solution

Draw an edge from each senator to everyone they hold files on; the
answer is the set of vertices from which every vertex is reachable.

Search the graph from every vertex not reached yet, each search marking
only unmarked vertices. Nothing marked earlier can reach the root of a
later search, since a search would have marked it, so the root of the
last search lies in a strongly connected component that no other
component reaches. If that root does not reach everyone, nobody does,
because anyone who reaches everyone reaches the root and therefore lies
in its component. If it does, the answer is exactly the vertices that
reach the root, found by one more search along reversed edges.
`O(N + M)` (`O(N² + M)` in Python) for `M` files, up to about `4·10⁶`.

Pitfalls:

- the input can be close to 20 MB, so slow reading costs more than the
  graph work;
- adjacency lists of `4·10⁶` entries must be stored compactly, as 32-bit
  numbers in flat arrays, to stay well under the memory limit;
- a senator may appear in their own list or twice in one list;
- when nobody qualifies, the output is a single `0`.

The answers were compared with a separately written solution, based on
the transitive closure with bit sets, on 300 small random graphs and on
every test.

The teaching C++ version stores one Boolean adjacency matrix. In a forward search it reads a row, and in a reverse search it reads a column of the same matrix. A repeated edge simply sets the same entry again. The last search root is checked in the forward graph, then a reverse search finds all vertices that reach it. In each pass every vertex is queued at most once and its search scans N entries. Time O(N² + M), space O(N²).

## Optimized solutions

C++, Go and Rust pack each forward/reverse adjacency row into 64-bit words. Repeated edges and self-loops are handled by setting the same bit. A search intersects a row with the unvisited mask and clears new bits before queueing, so every vertex is queued once. Keep the standard last-search-root candidate, verify it reaches all vertices, then search the reverse graph from it. If a universal source exists the last root must reach everyone; after verification another vertex is universal exactly when it reaches that root. Thus the final reverse search gives precisely the answer. The three traversals inspect O(N⌈N/64⌉) words in total besides input O(M). At N=2000, both matrices occupy 1024000 bytes rather than millions of separate edges; 16-bit queue IDs suffice. All ordinary CSR files remain; Java/Python reuse admitted bases.

The accepted base implementations [1198_graphs.java](1198_graphs.java), [1198_graphs.py](1198_graphs.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- C++, Go, Java and Rust store both graphs as flat arrays with offsets,
  building the reverse one by counting.
- Python stores each senator's list as a big integer with one byte per
  senator, filled through a `bytearray`, so all per-file work stays in
  built-in functions; the searches then cost a few whole-set operations
  per senator, and the reverse graph comes from `zip` over the rows. It
  reads the whole input at once, which is much faster here than reading
  line by line.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1198_graphs.cpp](1198_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.140 s | 32064 KB | 11283511 |
| [1198_graphs.go](1198_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.296 s | 50472 KB | 11283512 |
| [1198_graphs.java](1198_graphs.java) \* | Java 1.8 | graphs | O(N + M) | AC | 0.250 s | 37092 KB | 11283514 |
| [1198_graphs.py](1198_graphs.py) \* | Python 3.12 x64 | graphs | O(N² + M) | AC | 1.281 s | 36148 KB | 11283513 |
| [1198_graphs.rs](1198_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.281 s | 64220 KB | 11283517 |
| [1198_bfs.cpp](1198_bfs.cpp) | G++ 13.2 x64 | bfs | O(N² + M) | AC | 0.609 s | 4228 KB | 11315851 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1198_graphs_bitmask.cpp](1198_graphs_bitmask.cpp) | G++ 13.2 x64 | graphs, bitmask | O(M + N⌈N/64⌉) | AC | 0.078 s | 1092 KB | 11315333 |
| [1198_graphs_bitmask.go](1198_graphs_bitmask.go) \* | Go 1.14 x64 | graphs, bitmask | O(M + N⌈N/64⌉) | AC | 0.062 s | 1320 KB | 11315339 |
| [1198_graphs_bitmask.rs](1198_graphs_bitmask.rs) \* | Rust 1.75 x64 | graphs, bitmask | O(M + N⌈N/64⌉) | AC | 0.062 s | 1092 KB | 11315334 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
