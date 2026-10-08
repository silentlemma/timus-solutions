# 1018. Keeping the most valuable connected branches of a binary tree

[Timus 1018](https://acm.timus.ru/problem.aspx?space=1&num=1018) · difficulty 280 · dp, trees

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

The output is compared token by token; extra whitespace does not matter.

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
2 1
2 1 30000
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

- an edge may be given as "child parent": build an undirected adjacency list
  and root it by a DFS from 1;
- a greedy choice of the heaviest available branch fails: a light branch
  may lead to heavy ones.

## Language notes

The same recursive DFS in every language; the depth is at most 100.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1018_dp_trees.cpp](1018_dp_trees.cpp) | G++ 13.2 x64 | dp, trees | O(N · Q^2) | AC | 0.015 s | 212 KB |
| [1018_dp_trees.go](1018_dp_trees.go) | Go 1.14 x64 | dp, trees | O(N · Q^2) | AC | 0.031 s | 1152 KB |
| [1018_dp_trees.java](1018_dp_trees.java) | Java 1.8 | dp, trees | O(N · Q^2) | AC | 0.140 s | 1912 KB |
| [1018_dp_trees.py](1018_dp_trees.py) | Python 3.12 x64 | dp, trees | O(N · Q^2) | AC | 0.078 s | 596 KB |
| [1018_dp_trees.rs](1018_dp_trees.rs) | Rust 1.75 x64 | dp, trees | O(N · Q^2) | AC | 0.015 s | 260 KB |
