# 2221. Hull sizes of every subtree of a Cartesian tree of points

[Timus 2221](https://acm.timus.ru/problem.aspx?space=1&num=2221) · difficulty 1127 · geometry, trees

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2025.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N points with distinct x and distinct y are split recursively: the
highest point of a set is its delegate, and the points to its left and
to its right form two new sets. For every point, report the number of
vertices of the convex hull of the set it is the delegate of (1 for a
point, 2 for a segment). The limits are 2 seconds and 512 MB.

## Input

N, 1 ≤ N ≤ 10⁵, then the points with coordinates up to 10⁹ in absolute
value.

## Output

The hull size for each point, in input order.

## Examples

### Example 1

Input:

```
5
0 0
6 4
4 7
8 9
12 1
```

Output:

```
1
1
3
4
1
```

## Solution

This splitting is exactly a Cartesian tree with x as the key and y as
the heap priority, built with a stack after sorting by x; the set of a
delegate is its subtree, a contiguous range of x.

The hull of a subtree is its lower chain and its upper chain, built
like Andrew's monotone chain. A point that is not on the hull of a
child's set cannot be on the hull of the parent's set, so a parent only
needs the children's chains and its own point. Going up the tree, the
parent keeps the chain of its larger child as a linked list and inserts
the delegate and then the points of the smaller child's chain from the
nearer end of the list: appending to the right for a left base, or
prepending for a right base. Each insertion pops points that no longer
make a strict turn, so collinear points drop out.

Smaller into larger means every point is inserted O(log n) times, and
pops never exceed insertions. The hull size is the length of the lower
chain plus the upper chain minus the two shared ends, and at least 1.

In the example the highest point (8, 9) is the delegate of all five
points, whose hull has 4 vertices, and (4, 7) is the delegate of the
three points to its left, a triangle.

This takes O(n log n).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2221_geometry_trees.cpp](2221_geometry_trees.cpp) | G++ 13.2 x64 | geometry, trees | O(n log n) | AC | 0.093 s | 6508 KB |
| [2221_geometry_trees.go](2221_geometry_trees.go) | Go 1.14 x64 | geometry, trees | O(n log n) | AC | 0.109 s | 21892 KB |
| [2221_geometry_trees.java](2221_geometry_trees.java) | Java 1.8 | geometry, trees | O(n log n) | AC | 0.328 s | 12136 KB |
| [2221_geometry_trees.py](2221_geometry_trees.py) | Python 3.12 x64 | geometry, trees | O(n log n) | AC | 0.859 s | 45392 KB |
| [2221_geometry_trees.rs](2221_geometry_trees.rs) | Rust 1.75 x64 | geometry, trees | O(n log n) | AC | 0.078 s | 15152 KB |
