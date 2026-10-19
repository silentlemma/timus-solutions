# 1840. Victim of Advertising

[Timus 1840](https://acm.timus.ru/problem.aspx?space=1&num=1840) · difficulty 6905 · geometry

Original problem by Pavel Egorov, from the Fifteenth Ural Championship in Sports Programming, April 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A skater must ride n directed segments in order, joining neighbouring
segments by circular arcs so that the path is smooth; where no arc fits
between two neighbours, one of them may be lengthened. The speed is at
most 10, the acceleration along the path at most 1, and on an arc of
radius R the speed is at most √R (centripetal acceleration v²/R ≤ 1).
Starting and ending at rest, find the least time to ride the path.

## Input

n (1 ≤ n ≤ 1000), then n segments as the coordinates of the start and
the end, integers up to 1000 in absolute value. No two neighbours point
the same way, and a smooth path always exists.

## Output

The least time, with absolute or relative error at most 10⁻⁶.

## Examples

### Example 1

Input:

```
1
0 0 4 0
```

Output:

```
4.0000000000
```

### Example 2

Input:

```
2
-2 4 0 4
4 0 4 -2
```

Output:

```
7.1415926536
```

## Solution

The path. Take two neighbours: one ends at B going along u, the next
starts at A going along v. If the lines are not parallel, they meet at
a point X that lies t past B and back before A. An arc tangent to both
lines touches them at equal distances from X, so the largest arc, which
is also the fastest, uses distance min(t, back), and the segment with
the larger slack is lengthened by the difference. With turning angle φ
and tangent distance d the radius is d·(1 + cos φ)/sin φ and the arc
turns by φ. If X lies behind, min(t, back) is negative and the arc
goes the long way around, turning by 2π − φ. Distance 0 is a sharp
corner, an arc of radius 0 where the skater has to stop. Opposite
neighbours are joined by a half circle across the gap between their
lines, after lengthening one of them to line up.

The ride. The path is now a chain of pieces: segments with speed cap
10 and arcs with cap min(10, √R). With acceleration and braking at most
1, the speed where two pieces meet is the smaller of what one can reach
from the start, sweeping forward with v² growing by 2·length and capped
by every piece, and what one can still brake from before the end,
sweeping backward the same way. Each piece is then ridden fastest by
speeding up, cruising at its cap if there is room, and slowing down.
`O(n)`.

In the second example the lines y = 4 and x = 4 meet 4 past the first
segment and 4 before the second, giving a quarter circle of radius 4
and cap 2. The skater speeds up to 2 over 2 metres, rides the arc of
length 2π at speed 2 for π seconds and brakes over the last 2 metres:
2 + π + 2.

Pitfalls:

- on a tight arc the cap √R can force near-stops, so times can be
  huge; the answer is still a sum of short closed forms;
- a piece's cap limits the speed at both of its ends;
- the long way around happens when the next segment starts behind the
  turn.

The answers agree with an independent accepted implementation on five
hundred random paths and on the large tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1840_geometry.cpp](1840_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 308 KB |
| [1840_geometry.go](1840_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1396 KB |
| [1840_geometry.java](1840_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.125 s | 1132 KB |
| [1840_geometry.py](1840_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.093 s | 1728 KB |
| [1840_geometry.rs](1840_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.046 s | 376 KB |
