# 2127. Determinant of the adjacency matrix of an almost-tree

[Timus 2127](https://acm.timus.ru/problem.aspx?space=1&num=2127) · difficulty 3079 · graphs, matrix

Original problem by Alexey Danilyuk, from the t.me/umnik_team contest, Petrozavodsk training camp, summer 2018.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A connected simple graph has n vertices and at most n + 50 edges. Print
the determinant of its adjacency matrix modulo 998 244 353. The limits
are 2 seconds and 128 MB.

## Input

n and m, 1 ≤ n ≤ 2 · 10⁵, n − 1 ≤ m ≤ n + 50, then the m edges.

## Output

The determinant modulo 998 244 353.

## Examples

### Example 1

Input:

```
4 3
1 2
2 3
3 4
```

Output:

```
1
```

### Example 2

Input:

```
5 10
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
```

Output:

```
4
```

### Example 3

Input:

```
1 0
```

Output:

```
0
```

### Example 4

Input:

```
2 1
2 1
```

Output:

```
998244352
```

## Solution

The matrix is huge, so first shrink the graph with steps that change the
determinant in a known way.

- A leaf u with neighbour v: row u has its only nonzero entry in column
  v, and column u only in row v, so expanding along both gives
  det A = −det A′ with u and v removed. This repeats while leaves exist
  (it can cut the graph into pieces), and a vertex left with no
  neighbours makes the determinant 0.
- A path through two degree-2 vertices a and b, x – a – b – y, is
  removed by a Schur complement on {a, b}: the block [[0, 1], [1, 0]] has
  determinant −1, and eliminating it adds an edge of weight −1 between x
  and y. So each pair of path vertices costs a factor −1 and flips the
  sign of the edge that replaces it. A path with an even number of inner
  vertices becomes a weighted edge, with an odd number one inner vertex
  remains.
- A piece that is just a cycle of length L has determinant 2 for odd L,
  0 for L divisible by 4 and −4 otherwise.

After the leaves are gone every vertex has degree at least 2, and since
m − n ≤ 50 at most about a hundred vertices have degree above 2. The
compressed matrix holds these vertices and one remaining vertex per odd
path. The rows of the remaining path vertices have entries only in the
columns of the branch vertices, so if there are more of them than branch
vertices they are linearly dependent and the determinant is 0. The rest
is a Gaussian elimination modulo the prime on at most about 200 rows.
The total time is O(n + m + k³) with k the size of the small matrix.

In the first example the path 1 – 2 – 3 – 4 loses the pairs (1, 2) and
(3, 4) as leaves, giving (−1)² = 1. In the fourth a single edge gives −1.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2127_graphs_matrix.cpp](2127_graphs_matrix.cpp) | G++ 13.2 x64 | graphs, matrix | O(n + m + k^3), k <= 200 | AC | 0.125 s | 9508 KB |
| [2127_graphs_matrix.go](2127_graphs_matrix.go) | Go 1.14 x64 | graphs, matrix | O(n + m + k^3), k <= 200 | AC | 0.062 s | 19976 KB |
| [2127_graphs_matrix.java](2127_graphs_matrix.java) | Java 1.8 | graphs, matrix | O(n + m + k^3), k <= 200 | AC | 0.109 s | 7904 KB |
| [2127_graphs_matrix.py](2127_graphs_matrix.py) | Python 3.12 x64 | graphs, matrix | O(n + m + k^3), k <= 200 | AC | 0.546 s | 56440 KB |
| [2127_graphs_matrix.rs](2127_graphs_matrix.rs) | Rust 1.75 x64 | graphs, matrix | O(n + m + k^3), k <= 200 | AC | 0.062 s | 21988 KB |
