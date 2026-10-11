# 1235. The largest square field between the trees

[Timus 1235](https://acm.timus.ru/problem.aspx?space=1&num=1235) · difficulty 769 · geometry

Original problem by Andrey Demidov, from the ACM ICPC Northeastern European Regional Contest 2002–2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A W × H park (1 ≤ W, H ≤ 10 000) with its corner at the origin holds N
trees (0 ≤ N ≤ 100) at distinct integer points. Find the largest square
with sides parallel to the park's that lies inside the park and has no
tree strictly inside it; trees on its border are fine.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, W and H, then the N trees as `x y`.

## Output

The southwest corner P, Q of a largest square and its side L. Any largest
square will do.

## Checking

Several squares can be largest, so the checker accepts any: L must equal
the maximum side length, the square must lie inside the park, and no
tree may be strictly inside it.

## Examples

### Example 1

Input:

```
7 10 7
3 2
4 2
7 0
7 3
4 5
2 4
1 7
```

Output:

```
4 3 4
```

## Solution

Take a largest square and slide it left: it can move until its left side
reaches the park border or a tree whose height is strictly between its
bottom and top. Then slide it down the same way. It stays empty and keeps
its size, and now its corner has x equal to 0 or the x of a tree, and y
equal to 0 or the y of a tree.

So try every such corner, at most 101 × 101. From corner (p, q) the side
is limited by the park, `min(W − p, H − q)`, and by every tree up and to
the right, x > p and y > q: that tree is strictly inside if the side
exceeds `max(x − p, y − q)`. Trees to the left or below never get inside.
The largest side over all corners is the answer. `O(N³)` with N ≤ 100.

Pitfalls:

- the corner coordinates can come from different trees, so they are tried as
  all pairs, not tree by tree;
- a tree on the border is allowed, which is why the comparisons are
  strict: in the example the field 4 3 4 has trees on two of its sides
  and its top on the park border;
- with no trees the answer is the shorter side of the park (test 02).

## Language notes

- Python drops, for each p, the trees that are not to its right before
  trying the values of q.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1235_geometry.cpp](1235_geometry.cpp) | G++ 13.2 x64 | geometry | O(N³) | AC | 0.015 s | 200 KB |
| [1235_geometry.go](1235_geometry.go) | Go 1.14 x64 | geometry | O(N³) | AC | 0.031 s | 1084 KB |
| [1235_geometry.java](1235_geometry.java) | Java 1.8 | geometry | O(N³) | AC | 0.093 s | 520 KB |
| [1235_geometry.py](1235_geometry.py) | Python 3.12 x64 | geometry | O(N³) | AC | 0.218 s | 524 KB |
| [1235_geometry.rs](1235_geometry.rs) | Rust 1.75 x64 | geometry | O(N³) | AC | 0.015 s | 244 KB |
