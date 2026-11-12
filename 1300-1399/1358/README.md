# 1358. Cables

[Timus 1358](https://acm.timus.ru/problem.aspx?space=1&num=1358) · difficulty 540 · graphs

Original problem by Den Raskovalov (statement by Aleksandr Bikbaev), from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 1000 computers are joined by N − 1 cables into a connected network,
that is, a tree. Place the computers as points in the plane, with
coordinates of absolute value at most 1000, so that the cables, drawn as
straight segments, do not cross, and every two computers are farther
apart than 1.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

N, then N − 1 lines with the ends a, b of each cable.

## Output

N lines with the coordinates of computers 1 to N. Any valid placement
is accepted.

## Examples

### Example 1

Input:

```
3
1 2
2 3
```

Output:

```
0 0
10 0
0 10
```

## Solution

Root the tree at computer 1 and walk it depth-first. Put each computer
in the column given by its place in that walk, x = 2 · index − 999, and
in the row given by its depth, y = depth. Every computer gets its own
column, two units from the next one, so all distances are at least 2,
and all coordinates stay within [−999, 999].

The cables never cross. Every cable joins a computer in some row to a
child in the next row, so two cables can only cross if they lie in the
same strip between two rows. A depth-first walk visits each subtree as
one block of consecutive columns, and the computers of one row have
disjoint subtrees; so the cables leaving two different computers of a
row stay inside two disjoint column ranges, and the cables leaving the
same computer only share that end. `O(N)`.

Pitfalls:

- a path of 1000 computers rooted at an end reaches depth 999, which
  still fits in the bounds (generated test 8);
- N = 1 has no cables at all (test 02);
- the walk must be iterative or have enough stack for depth 999.

The tests are judged by a checker that tests the bounds, every pair of
points and every pair of cables, including cables that share an end and
overlap.

The teaching C++ version assigns a point when the recursive DFS enters a vertex. Its column starts at −999 and advances by two on each entry. The row is the depth passed to the call. It recurses on each neighbor except the parent. Since the input is a tree, this visits each vertex once and assigns all columns of one subtree consecutively. The time and storage are O(N), with at most N recursive calls on the stack.

## Optimized solutions

Go and Rust keep x=2·preorder−999 and y=depth. Each vertex has a distinct column spaced by 2, so every pair is farther than 1. N ≤ 1000 gives x in [−999,999] and y in [0,999]. An edge stays in the strip between consecutive depths and within its parent’s subtree columns. Different parents on the same row have disjoint column intervals. Edges from one parent have distinct endpoints on the next row and meet only at that parent. The new versions use flat 16-bit arrays for adjacency heads, destinations, next edges, preorder, depth and the stack. Edge indices are at most 1998, vertex IDs at most 1000, and stored depth plus one at most 1000. Zero depth means undiscovered, so a separate seen or parent array is unnecessary. Prepending input edges and pushing their chain onto LIFO retains the original child order. Both use fixed arrays for the 1000-vertex limit. Go reads and writes fixed 256-byte buffers through standard handles. Rust uses C-runtime character I/O and a C entry point. Time and space are O(N) under the fixed maximum. All simple files remain; C++/Java/Python reuse admitted bases.

The accepted base implementations [1358_graphs.cpp](1358_graphs.cpp), [1358_graphs.java](1358_graphs.java), [1358_graphs.py](1358_graphs.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- All languages visit children in input order and produce the same
  placement; a checker accepts other valid answers too.
- Java keeps the adjacency lists in flat arrays to stay within the
  short time limit.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1358_graphs.cpp](1358_graphs.cpp) | G++ 13.2 x64 | graphs | O(N) | AC | 0.015 s | 260 KB | 11285300 |
| [1358_graphs.go](1358_graphs.go) | Go 1.14 x64 | graphs | O(N) | AC | 0.031 s | 1208 KB | 11285313 |
| [1358_graphs.java](1358_graphs.java) | Java 1.8 | graphs | O(N) | AC | 0.140 s | 624 KB | 11285343 |
| [1358_graphs.py](1358_graphs.py) \* | Python 3.12 x64 | graphs | O(N) | AC | 0.093 s | 820 KB | 11285322 |
| [1358_graphs.rs](1358_graphs.rs) | Rust 1.75 x64 | graphs | O(N) | AC | 0.046 s | 308 KB | 11285353 |
| [1358_dfs.cpp](1358_dfs.cpp) | G++ 13.2 x64 | dfs | O(N) | AC | 0.015 s | 564 KB | 11315912 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1358_graphs_optimized.rs](1358_graphs_optimized.rs) \* | Rust 1.75 x64 | graphs | O(N) | AC | 0.015 s | 56 KB | 11315908 |
| [1358_graphs_optimized.go](1358_graphs_optimized.go) \* | Go 1.14 x64 | graphs | O(N) | AC | 0.015 s | 324 KB | 11315964 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
