# 2160. Permutations with the same Cartesian tree

[Timus 2160](https://acm.timus.ru/problem.aspx?space=1&num=2160) · difficulty 1132 · combinatorics, trees

Original problem by Vadim Barinov, from the Ural School Programming Contest 2021.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two permutations are equivalent when both are empty, or their smallest
elements stand at the same position and the parts to the left and to
the right of it are equivalent in turn. Count the permutations of
1 … N equivalent to the given one, modulo 10⁹ + 7. The limits are
2 seconds and 256 MB.

## Input

N, 1 ≤ N ≤ 10⁵, then the permutation.

## Output

The number of equivalent permutations modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
3
2 1 3
```

Output:

```
2
```

### Example 2

Input:

```
12
12 5 3 11 2 8 4 9 1 6 10 7
```

Output:

```
34650
```

## Solution

The recursive definition is exactly the shape of the Cartesian tree of
the permutation: the root is the smallest element, and its left and
right subtrees are built from the two sides. So the task is to count the
labellings of a fixed binary tree with 1 … N in which every node is
smaller than all nodes of its subtree.

In such a labelling the root of every subtree of size s must carry the
smallest of its s labels, which happens with probability 1 / s, and
these events are independent. Hence the count is N! divided by the
product of all subtree sizes. The Cartesian tree, and with it the
subtree sizes, comes from the usual stack pass: when a smaller element
arrives, the popped elements complete their subtrees, and their sizes
accumulate into the left child of the new element. The division is a
multiplication by the inverse modulo the prime. The work is O(N).

In the first example the tree has root 1 with two leaves, so the count
is 3! / (3 · 1 · 1) = 2.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2160_combinatorics_trees.cpp](2160_combinatorics_trees.cpp) | G++ 13.2 x64 | combinatorics, trees | O(N) | AC | 0.015 s | 1208 KB |
| [2160_combinatorics_trees.go](2160_combinatorics_trees.go) | Go 1.14 x64 | combinatorics, trees | O(N) | AC | 0.031 s | 5160 KB |
| [2160_combinatorics_trees.java](2160_combinatorics_trees.java) | Java 1.8 | combinatorics, trees | O(N) | AC | 0.109 s | 1196 KB |
| [2160_combinatorics_trees.py](2160_combinatorics_trees.py) | Python 3.12 x64 | combinatorics, trees | O(N) | AC | 0.125 s | 11584 KB |
| [2160_combinatorics_trees.rs](2160_combinatorics_trees.rs) | Rust 1.75 x64 | combinatorics, trees | O(N) | AC | 0.046 s | 3692 KB |
