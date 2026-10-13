# 1471. Distance in the Tree

[Timus 1471](https://acm.timus.ru/problem.aspx?space=1&num=1471) · difficulty 163 · trees

Original problem by Dmitry Zhukov, from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tree has n vertices (1 ≤ n ≤ 50000), numbered from 0 to n − 1, and
n − 1 weighted edges (weights from 0 to 1000). For each of m questions
(1 ≤ m ≤ 75000) print the length of the path between two given
vertices.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n, then the edges as u v w, then m and the pairs of vertices.

## Output

One distance per line.

## Examples

### Example 1

Input:

```
3
1 0 1
2 0 1
3
0 1
0 2
1 2
```

Output:

```
1
1
2
```

## Solution

Hang the tree from vertex 0 and store each vertex's distance to the root.
The path between a and b goes up to their lowest common ancestor, so its
length is dist(a) + dist(b) − 2·dist(lca). The ancestor comes from the
Euler tour: a depth-first walk that writes a vertex when it enters it
and again after each child. Between the first entries of a and b the
tour passes through their ancestor and nowhere higher, so the ancestor
is the shallowest vertex on that stretch. A sparse table of minima over
stretches of length 2^k answers that with two overlapping lookups.
`O(n log n)` to build, `O(1)` per question.

Pitfalls:

- a path of 50000 vertices is too deep for recursion in most languages,
  so the walk keeps its own stack (gen3);
- vertex 0 may be a leaf, and edges come in either direction (test 03);
- a single vertex has no edges at all, and a question may name the same
  vertex twice (test 02).

## Language notes

- Python puts all input numbers and the rows of the sparse table into
  flat `array`s and frees the words of the input before building the
  tables: with lists of Python integers it went over the 64 MB limit on
  the judge's test 14. Now it takes 0.67 s and 44 MB.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1471_trees.cpp](1471_trees.cpp) | G++ 13.2 x64 | trees | O(n log n + m) | AC | 0.218 s | 9772 KB |
| [1471_trees.go](1471_trees.go) | Go 1.14 x64 | trees | O(n log n + m) | AC | 0.078 s | 21144 KB |
| [1471_trees.java](1471_trees.java) | Java 1.8 | trees | O(n log n + m) | AC | 0.140 s | 13228 KB |
| [1471_trees.py](1471_trees.py) | Python 3.12 x64 | trees | O(n log n + m) | AC | 0.671 s | 43868 KB |
| [1471_trees.rs](1471_trees.rs) | Rust 1.75 x64 | trees | O(n log n + m) | AC | 0.046 s | 22180 KB |
