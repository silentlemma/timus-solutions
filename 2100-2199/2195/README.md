# 2195. Turning one binary tree into another through a path

[Timus 2195](https://acm.timus.ru/problem.aspx?space=1&num=2195) · difficulty 1537 · constructive

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2023.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two binary trees on N vertices are rooted at 0. One move takes a
non-root vertex v with its subtree and hangs it under a vertex u outside
that subtree, and the tree must stay binary. Give at most N moves that
make the first tree isomorphic to the second. The limits are 1 second
and 256 MB.

## Input

N, 2 ≤ N ≤ 1000, then the parents of vertices 1 … N − 1 in the first
tree and in the second.

## Output

The number of moves M ≤ N, then M lines v u.

## Examples

### Example 1

Input:

```
4
0 0 1
0 1 2
```

Output:

```
1
2 3
```

### Example 2

Input:

```
4
2 0 0
0 3 0
```

Output:

```
2
3 1
1 0
```

## Solution

Every binary tree can be pulled into a path. List the vertices in
preorder; whenever the next vertex is not a child of the previous one,
hang it under the previous one. Going in preorder, the vertices seen so
far already form a path, and the previous vertex was a leaf, since in
preorder a vertex with children is followed by its first child. So it
receives its only child, the tree stays binary, and the previous vertex
is not inside the moved subtree. At the end the tree is the path of the
preorder.

A move happens only when the previous vertex is a leaf other than the
last one, so a tree with ℓ leaves takes ℓ − 1 moves, and a binary tree
on N vertices has at most (N + 1) / 2 leaves.

The second tree can be pulled into its own preorder path the same way,
and every move can be undone by hanging the subtree back where it was,
which keeps the tree binary because it restores an earlier state. So
the answer is the moves for the first tree, followed by the moves for
the second tree in reverse, with each vertex of the second tree renamed
to the vertex of the first tree at the same place on the path. The
total is at most N − 1.

In the second example the first tree is pulled into the path
0 → 2 → 1 → 3 with one move, and one undone move of the second tree
turns it into the target shape.

This takes O(N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2195_constructive.cpp](2195_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 296 KB |
| [2195_constructive.go](2195_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.046 s | 1052 KB |
| [2195_constructive.java](2195_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.109 s | 416 KB |
| [2195_constructive.py](2195_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.125 s | 808 KB |
| [2195_constructive.rs](2195_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 136 KB |
