# 1444. Elephpotamus

[Timus 1444](https://acm.timus.ru/problem.aspx?space=1&num=1444) · difficulty 263 · geometry

Original problem by Ekaterina Vasilyeva (idea and text) and Alexander Mironenko, Alexey Lakhtin and Den Raskovalov (programming), from the Tenth Ural Collegiate Team Programming Championship, March 24–25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N pumpkins (3 ≤ N ≤ 30000) lie at distinct integer points with
coordinates from −1000 to 1000, not all on one line. An elephpotamus
starts at pumpkin 1 and eats it; after each pumpkin it can be sent in a
straight line to any remaining pumpkin. The animal stops for good as soon
as it steps on its own tracks, so the walk must never touch itself. Find
the largest number of pumpkins K it can eat and the order of the walk,
starting with 1.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, then the coordinates of the pumpkins 1 to N.

## Output

K, then the numbers of the pumpkins in the order they are eaten, one per
line. Any valid walk is accepted.

## Examples

### Example 1

Input:

```
4
0 0
10 10
0 10
10 0
```

Output:

```
4
1
3
2
4
```

## Solution

All N pumpkins can always be eaten. Sort the others by the angle of the
direction from pumpkin 1, and on one ray by the distance, nearer first;
the comparisons use integer cross products, so they are exact. Walking
in this order sweeps around pumpkin 1 like a fan: every step either goes
further out along the same ray or moves into the next direction, so the
walk stays inside one narrow wedge at a time and never comes back.

The only danger is the start of the circle. If two neighbouring
directions are half a turn or more apart, the step between them could
pass through pumpkin 1 or cut across earlier steps, so the circle is cut
right after that gap; there can be at most one such gap, since not all
pumpkins lie on one line. Without such a gap any starting point works.
`O(N log N)`.

Pitfalls:

- several pumpkins on one ray must be eaten from the nearest outwards
  (tests 03, 06, gen2);
- a gap of exactly half a turn, with pumpkins on both sides of pumpkin
  1 along one line (tests 03, 09);
- pumpkin 1 in a corner leaves a gap of more than half a turn (tests
  04, gen3, gen4).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1444_geometry.cpp](1444_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.062 s | 444 KB |
| [1444_geometry.go](1444_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.078 s | 2336 KB |
| [1444_geometry.java](1444_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.187 s | 6232 KB |
| [1444_geometry.py](1444_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.453 s | 11600 KB |
| [1444_geometry.rs](1444_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 2104 KB |
