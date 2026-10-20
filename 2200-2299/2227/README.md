# 2227. Measuring and cutting a convex polygon along its diagonals

[Timus 2227](https://acm.timus.ru/problem.aspx?space=1&num=2227) · difficulty 1875 · geometry, fenwick

Original problem by Vadim Barinov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A convex polygon with N vertices gets Q actions along diagonals of the
current polygon: a measure reports the larger of the two areas, and a
cut throws away the smaller part (on a tie, the part with a vertex
numbered outside the chosen pair) and reports its area. Print every
reported area within 10⁻⁹. The limits are 0.5 seconds and 256 MB.

## Input

N and Q, 4 ≤ N ≤ 10⁵, 1 ≤ Q ≤ 10⁵, then the vertices counterclockwise
with coordinates up to 10⁹ in absolute value, then the actions "m l r"
or "c l r".

## Output

One area per action.

## Examples

### Example 1

Input:

```
5 4
2 0
3 1
2 2
0 2
0 0
m 5 3
m 2 4
c 1 3
m 4 1
```

Output:

```
3.0
4.0
1.0
2.0
```

## Solution

All areas are kept doubled, as exact integers, so every answer ends in
".0" or ".5". With l < r, the doubled area of the polygon l, l + 1, …, r
of the original vertices is a range of the shoelace prefix sums plus the
closing term x_r y_l − y_r x_l.

Cuts only remove pieces, and each removed piece cut off by a diagonal
of the current polygon lies on one side of every later diagonal. A piece
cut from the arc l … r is charged to the first edge l + 1 of that arc in
a Fenwick tree; a piece on the outside of the arc is charged to edge
r + 1, outside every later arc. For a later diagonal (l, r), the current
polygon's part on the inner arc is the original area of the arc minus
the charges on edges l + 1 … r, and the other part is the current total
minus it.

A measure prints the larger part. A cut drops the smaller part, or the
outer one on a tie, charges it as above, and lowers the total.

In the example the first measure splits the pentagon of area 5 along
5–3 into parts of 3 and 2 and prints 3.

This takes O(N + Q log N).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2227_geometry_fenwick.cpp](2227_geometry_fenwick.cpp) | G++ 13.2 x64 | geometry, fenwick | O(N + Q log N) | AC | 0.171 s | 2900 KB |
| [2227_geometry_fenwick.go](2227_geometry_fenwick.go) | Go 1.14 x64 | geometry, fenwick | O(N + Q log N) | AC | 0.078 s | 12032 KB |
| [2227_geometry_fenwick.java](2227_geometry_fenwick.java) | Java 1.8 | geometry, fenwick | O(N + Q log N) | AC | 0.218 s | 13944 KB |
| [2227_geometry_fenwick.py](2227_geometry_fenwick.py) | PyPy 3.10 x64 | geometry, fenwick | O(N + Q log N) | AC | 0.343 s | 52180 KB |
| [2227_geometry_fenwick.rs](2227_geometry_fenwick.rs) | Rust 1.75 x64 | geometry, fenwick | O(N + Q log N) | AC | 0.046 s | 11220 KB |
