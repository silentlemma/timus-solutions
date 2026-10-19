# 2119. Weight of the subtree spanning a changing vertex set

[Timus 2119](https://acm.timus.ru/problem.aspx?space=1&num=2119) · difficulty 780 · trees, fenwick

Original problem by Alexey Danilyuk, from the t.me/umnik_team contest, Petrozavodsk training camp, summer 2018.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tree has weighted edges and a set A of vertices that starts empty.
Each query adds a vertex to A or removes one from it. After every query
print the total weight of the smallest subtree containing all of A (0
when A is empty). The limits are 5 seconds and 256 MB.

## Input

n, 1 ≤ n ≤ 3 · 10⁵, the n − 1 edges "u v w" with 0 ≤ w ≤ 10⁹, then q,
1 ≤ q ≤ 3 · 10⁵, and the queries "+ v" or "− v". A vertex is only added
when it is outside A and only removed when it is inside.

## Output

The weight after each query, one per line.

## Examples

### Example 1

Input:

```
5
1 2 1
2 3 10
3 4 100
3 5 1000
8
+ 2
+ 5
+ 4
- 5
+ 1
- 4
- 2
- 1
```

Output:

```
0
1010
1110
110
111
1
0
0
```

## Solution

Sort the vertices of A by their preorder number in a depth-first search:
v₁, v₂, …, vₖ. Walking v₁ → v₂ → … → vₖ → v₁ along tree paths passes
every edge of the spanning subtree exactly twice, the way a closed walk
around the subtree does, so the weight is half of
d(v₁, v₂) + … + d(vₖ, v₁). When v is inserted between its cyclic
neighbours a and b in this order, the sum grows by
d(a, v) + d(v, b) − d(a, b); a removal subtracts the same amount.

The neighbours come from a Fenwick tree over preorder positions that
marks the members of A: the number of marked positions before v gives
the rank of a, and a descent through the tree finds the element of a
given rank, wrapping around at both ends. Distances use weighted depths,
d(u, v) = D(u) + D(v) − 2 D(LCA). For u ≠ v with tin(u) < tin(v), the
LCA is the vertex whose preorder number is the smallest among the
parents of the vertices at preorder positions tin(u) + 1 … tin(v). A
sparse table over those parent numbers answers that in O(1).

The search is iterative, because the tree can be a path. Weights reach
3 · 10¹⁴, so the sums need 64-bit integers. The total time is
O((n + q) log n).

In the example after "+ 2", "+ 5" and "+ 4" the subtree is 2 – 3 – 4
plus 3 – 5 with weight 10 + 100 + 1000 = 1110.

## Language notes

The Python solution runs on PyPy 3.10: the same loops take several seconds
in CPython.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2119_trees_fenwick.cpp](2119_trees_fenwick.cpp) | G++ 13.2 x64 | trees, fenwick | O((n + q) log n) | AC | 0.343 s | 46600 KB |
| [2119_trees_fenwick.go](2119_trees_fenwick.go) | Go 1.14 x64 | trees, fenwick | O((n + q) log n) | AC | 0.453 s | 47972 KB |
| [2119_trees_fenwick.java](2119_trees_fenwick.java) | Java 1.8 | trees, fenwick | O((n + q) log n) | AC | 0.546 s | 76516 KB |
| [2119_trees_fenwick.py](2119_trees_fenwick.py) | PyPy 3.10 x64 | trees, fenwick | O((n + q) log n) | AC | 1.953 s | 224172 KB |
| [2119_trees_fenwick.rs](2119_trees_fenwick.rs) | Rust 1.75 x64 | trees, fenwick | O((n + q) log n) | AC | 0.406 s | 94224 KB |
