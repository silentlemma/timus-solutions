# 1281. River basin

[Timus 1281](https://acm.timus.ru/problem.aspx?space=1&num=1281) · difficulty 1771 · geometry

Original problem by Sergey Volchenkov, Vladimir Pinaev and Michael Kopachev, from the Central Russia regional quarterfinal of the ACM ICPC 2003–2004, Rybinsk, October 15–16, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A map shows N ≤ 10 rivers as broken lines, each listed from its head to
its mouth, with at most 1000 points in all. A river whose mouth lies on
an inner vertex of another river is a tributary of it. The basin of a
river is the smallest convex polygon holding the river, its
tributaries, their tributaries and so on. Print the largest basin area
with two digits after the point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then for each river the number of points and the points, which may
be fractional.

## Output

The largest basin area.

## Examples

### Example 1

Input:

```
3
4
6 9
5 11
3 12
1 7
3
7 9
5 7
5 5.5
6
3 10
5 8
4 6
5 5.5
6 5
3 5
```

Output:

```
16.00
```

### Example 2

Input:

```
2
4
6 9
5 11
3 12
1 7
6
3 10
5 8
4 6
5 5.5
6 5
3 5
```

Output:

```
12.00
```

## Solution

Find the tributaries by looking up the last point of every river among
the inner vertices of all rivers. The basin of a river then holds its
own points and, recursively, those of its tributaries, and its area is
the area of their convex hull: a monotone chain gives the hull, the
shoelace formula its area. The rivers form a forest, so the recursion
ends. P denotes the total number of points.

Pitfalls:

- tributaries can have tributaries, and all of them belong to the basin
  (test 05);
- a straight river has area zero (test 03);
- mouths match inner vertices by exact parsed-coordinate keys;
- an area may end in an exact half of the last printed digit, which can
  round either way, so these tests compare with a tolerance of 0.01.

The answers were compared with an independent implementation on 90
generated maps; they differed only on such halves, by 0.01.

## Language notes

- All use doubles; Java/Rust coordinate keys distinguish `-0.0` from `0.0`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1281_geometry.cpp](1281_geometry.cpp) | G++ 13.2 x64 | geometry | O(N · P log P) | AC | 0.015 s | 388 KB |
| [1281_geometry.go](1281_geometry.go) | Go 1.14 x64 | geometry | O(N · P · (N + log P)) | AC | 0.031 s | 1836 KB |
| [1281_geometry.java](1281_geometry.java) | Java 1.8 | geometry | O(N · P log P) | AC | 0.203 s | 4484 KB |
| [1281_geometry.py](1281_geometry.py) | Python 3.12 x64 | geometry | O(N · P · (N + log P)) | AC | 0.093 s | 1044 KB |
| [1281_geometry.rs](1281_geometry.rs) | Rust 1.75 x64 | geometry | O(N · P log P) | AC | 0.046 s | 560 KB |
