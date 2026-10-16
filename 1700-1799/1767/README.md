# 1767. The House of Doctor Dee

[Timus 1767](https://acm.timus.ru/problem.aspx?space=1&num=1767) · difficulty 728 · geometry

Original problem by Alex Samsonov, from the Fourteenth Ural Championship in Sports Programming, April 10, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Streets form a square grid. One walk goes from A to B and another from
C to D, each along some shortest path on the grid. Choose the two paths
so that the total length of the streets they share is as large as
possible, and print that length.

## Input

The points A, B, C and D, one per line, as whole coordinates of
absolute value at most 10⁹.

## Output

The largest shared length.

## Examples

### Example 1

Input:

```
2 2
4 4
5 5
3 3
```

Output:

```
2
```

## Solution

A shortest path stays in the box spanned by its two ends, so the
shared streets lie in the overlap of the two boxes, a w by h rectangle,
or nowhere if the boxes are apart. A shortest path moves only one way
along each axis: it rises to the right or to the left, or it is a
straight line, which fits both.

If both walks rise the same way, both can reach one corner of the
overlap, follow the same staircase to the opposite corner and go on to
their ends, sharing w + h, and no path inside the overlap is longer. If
one rises to the right and the other to the left, a shared piece must
move one way along each axis for both, so it is a single straight
segment, at most max(w, h), and both can follow one side of the
overlap. `O(1)`.

In the example both walks rise to the right, the overlap is the square
from (3, 3) to (4, 4), and the walks share 1 + 1 = 2.

Pitfalls:

- a walk is undirected for sharing: C to D rising to the right is the
  same as D to C;
- boxes that meet only at a point or along a line share 0 or that line;
- lengths reach 4·10⁹, beyond 32 bits.

The answers agree with all pairs of shortest paths on 400 random cases
with coordinates up to 5 and with an independent accepted
implementation on 90 random cases.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1767_geometry.cpp](1767_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 128 KB |
| [1767_geometry.go](1767_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1084 KB |
| [1767_geometry.java](1767_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1648 KB |
| [1767_geometry.py](1767_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 452 KB |
| [1767_geometry.rs](1767_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.062 s | 244 KB |
