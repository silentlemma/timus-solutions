# 2085. A tree path that uses every technology once

[Timus 2085](https://acm.timus.ru/problem.aspx?space=1&num=2085) · difficulty 1643 · hashing, trees

Original problem by Alexander Fetisov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n projects form a tree, and each project uses a set of the m
technologies. Find a simple path (possibly a single project) on which
every technology appears in exactly one project, and print its ends, or
"No solution". Any valid path is accepted. The limits are 5 seconds and
256 MB.

## Input

n and m, 1 ≤ n, m ≤ 10⁵, the n − 1 edges, then for each project the
number of its technologies and their numbers; the sets have at most 10⁶
elements in total.

## Output

The two ends of the path, or `No solution`.

## Checking

A checker accepts "No solution" only when the expected output says so,
and otherwise walks the printed path and counts the technologies.

## Examples

### Example 1

Input:

```
5 3
1 2
1 3
3 4
3 5
1 1
1 3
0
2 1 3
1 2
```

Output:

```
2 5
```

### Example 2

Input:

```
3 3
1 2
1 3
2 2 3
3 1 2 3
1 3
```

Output:

```
2 2
```

### Example 3

Input:

```
2 3
1 2
2 1 2
2 1 3
```

Output:

```
No solution
```

## Solution

Give every technology a random 64-bit weight and every project the sum
of the weights of its technologies. On a path where each technology is
used once, the project values add up to the sum G of all weights; if some
technology is used twice or missing, the sum is a different linear
combination of independent random numbers, which equals G only with
probability about 2⁻⁶⁴. So the task becomes: find a path whose values add
up to G modulo 2⁶⁴.

Root the tree and let depth(v) be the sum of the values from the root to
v. A path u … v through its highest vertex x has sum
depth(u) + depth(v) − 2 depth(x) + value(x). For every x the vertices of
its subtree are kept in a hash map from depth to vertex, built small to
large: x starts with its own map {depth(x)}, and each child's map is
merged into it, the smaller into the larger. Before a merge, every depth
d of the smaller map looks up G + 2 depth(x) − value(x) − d in the larger
one; a hit is a path through x, since the two sides lie in different
children of x (or one end is x). A single project with value G is a
path by itself. Each vertex moves O(log n) times, so the work is
O(n log n + Σ aᵢ) expected.

The tree is walked in breadth-first order, children before parents when
going back, so deep trees need no recursion. In the first example the
path 5, 3, 4 uses technologies 2, then none, then 1 and 3; the sample
answer 2 … 5 is just as good.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2085_hashing_trees.cpp](2085_hashing_trees.cpp) | G++ 13.2 x64 | hashing, trees | O(n log n + sum a) | AC | 0.937 s | 23040 KB |
| [2085_hashing_trees.go](2085_hashing_trees.go) | Go 1.14 x64 | hashing, trees | O(n log n + sum a) | AC | 0.343 s | 44040 KB |
| [2085_hashing_trees.java](2085_hashing_trees.java) | Java 1.8 | hashing, trees | O(n log n + sum a) | AC | 0.593 s | 50248 KB |
| [2085_hashing_trees.py](2085_hashing_trees.py) | Python 3.12 x64 | hashing, trees | O(n log n + sum a) | AC | 1.312 s | 101000 KB |
| [2085_hashing_trees.rs](2085_hashing_trees.rs) | Rust 1.75 x64 | hashing, trees | O(n log n + sum a) | AC | 0.156 s | 31624 KB |
