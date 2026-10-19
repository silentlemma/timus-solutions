# 2109. Common ancestor of a range of consecutive vertices

[Timus 2109](https://acm.timus.ru/problem.aspx?space=1&num=2109) · difficulty 532 · trees, dp

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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2109_trees_dp.cpp](2109_trees_dp.cpp) | G++ 13.2 x64 | trees, dp | O(n log n + q) | AC | 0.406 s | 26432 KB |
| [2109_trees_dp.go](2109_trees_dp.go) | Go 1.14 x64 | trees, dp | O(n log n + q) | AC | 0.296 s | 98064 KB |
| [2109_trees_dp.java](2109_trees_dp.java) | Java 1.8 | trees, dp | O(n log n + q) | AC | 0.468 s | 17584 KB |
| [2109_trees_dp.py](2109_trees_dp.py) | Python 3.12 x64 | trees, dp | O(n log n + q) | AC | 2.875 s | 222288 KB |
| [2109_trees_dp.rs](2109_trees_dp.rs) | Rust 1.75 x64 | trees, dp | O(n log n + q) | AC | 0.359 s | 77192 KB |
