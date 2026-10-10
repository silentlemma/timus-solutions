# 1173. A closed walk through all points with no crossing segments

[Timus 1173](https://acm.timus.ru/problem.aspx?space=1&num=1173) · difficulty 1050 · geometry

Original problem by Mugurel Ionut Andreica, from the Romanian Open Contest, December 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Wally's house and `N ≤ 1000` friends' houses are points in the plane, no
three of them on one line, with coordinates of at most three decimals.
Find an order in which Wally leaves home, visits every friend once along
straight segments and returns, so that no two segments cross except
consecutive ones at their shared end. Print `-1` if there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Wally's coordinates, `N`, then `N` lines with a friend's coordinates and
id from 1 to `N`.

## Output

`0`, the friends' ids in visiting order, and `0` again, one per line.

## Checking

Any order is accepted if it visits every friend once and no two
non-neighbouring sides of the closed walk meet; the checker tests every
pair of sides exactly. Since a walk always exists, `-1` is never right.

## Examples

### Example 1

Input:

```
0 0
3
3 3 1
6 0 2
6 2 3
```

Output:

```
0
1
3
2
0
```

## Solution

Sort the friends by angle around the house. Two friends that are
neighbours in this order span a wedge seen from the house, and the segment
between them stays inside that wedge as long as the wedge is narrower than
half a turn. Wedges of different pairs do not overlap, so these segments
never cross each other or the two segments from the house, which run
along wedge borders.

The walk goes from the house to some friend, around the angular order and
back. It skips exactly one wedge, the one between the last and the first
friend. At most one wedge can be wider than half a turn, so if there is
one, the walk starts right after it; otherwise it can start anywhere.
Hence the answer is never `-1`. `O(N log N)`.

Pitfalls:

- the coordinates have three decimals, so they are turned into integers
  in thousandths and the angular order uses exact cross products, which
  stay within 64 bits;
- the house itself may be inside the crowd of friends, where a careless
  start would put a segment across the wedge of more than half a turn;
- with two friends there are only two wedges, and exactly one of them is
  wider than half a turn.

Every output was checked by testing all pairs of sides on every test,
including a thousand friends around, beside and far from the house.

## Language notes

- All languages sort with the same exact comparison: first the half-plane
  of the direction, then the sign of the cross product.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1173_geometry.cpp](1173_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 244 KB |
| [1173_geometry.go](1173_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1212 KB |
| [1173_geometry.java](1173_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.156 s | 3388 KB |
| [1173_geometry.py](1173_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.109 s | 1036 KB |
| [1173_geometry.rs](1173_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.015 s | 364 KB |
