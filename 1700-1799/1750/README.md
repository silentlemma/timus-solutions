# 1750. Pakhom and the Gully

[Timus 1750](https://acm.timus.ru/problem.aspx?space=1&num=1750) · difficulty 1267 · geometry

Original problem by Petr Lezhankin, from the Ufa SATU Contest at the Petrozavodsk summer training camp, August 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A gully is the broken line ABC. Find the shortest way from S to T that
does not cross it; walking along its edge or around its ends is fine.

## Input

The number of tests n (1 ≤ n ≤ 5000), then for each test the
coordinates of S, T, A, B and C, integers up to 10 in absolute value.
All five points differ, and S and T are not on the gully.

## Output

The length of the shortest way for each test, with an error of at most
10⁻⁶.

## Examples

### Example 1

Input:

```
3
1 2 5 6 4 4 5 2 1 6
2 2 4 3 1 3 3 3 3 1
2 1 4 4 3 2 4 3 1 4
```

Output:

```
8.000000
3.650282
3.828427
```

## Solution

A shortest way is a broken line that bends only at points of the gully,
so it is S, then some of A, B and C in some order, then T: at most 16
candidates. Sort them by length and take the first one that is allowed.
`O(1)` per test.

All tests run on integers. A candidate is not allowed when one of its
pieces properly crosses AB or BC. The bend B needs more care: the gully
goes on from it both ways, so the way may touch B but must stay in one
of the two closed sectors between the rays BA and BC, both when it
passes straight through B and when it turns there. When BA and BC point
the same way, the gully folds back on itself, B is a free end, and an
end of the gully that lies inside the other piece is no corner at all:
the way may not switch sides there.

In the first example the straight way crosses BC, and going around C
takes 4 + 4 = 8.

Pitfalls:

- the gully may be straight, with B in the middle: crossing at B is
  still crossing;
- the gully may fold back so that A lies inside BC, or C inside AB;
  then that point is in the middle of the gully, not an end to go
  around;
- a way along a side of the gully only touches it.

The lengths match an independent accepted implementation on 4986 of
5000 random tests. The other 14 are all folded gullies, where that
implementation goes straight through the end lying inside the other
piece, which crosses the gully; the ways here go around the free end
instead.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1750_geometry.cpp](1750_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) per test | AC | 0.046 s | 240 KB |
| [1750_geometry.go](1750_geometry.go) | Go 1.14 x64 | geometry | O(1) per test | AC | 0.109 s | 6956 KB |
| [1750_geometry.java](1750_geometry.java) | Java 1.8 | geometry | O(1) per test | AC | 0.296 s | 6096 KB |
| [1750_geometry.py](1750_geometry.py) | Python 3.12 x64 | geometry | O(1) per test | AC | 0.453 s | 5016 KB |
| [1750_geometry.rs](1750_geometry.rs) | Rust 1.75 x64 | geometry | O(1) per test | AC | 0.031 s | 1380 KB |
