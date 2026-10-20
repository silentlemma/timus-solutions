# 2154. Closest line through two points to the origin

[Timus 2154](https://acm.timus.ru/problem.aspx?space=1&num=2154) · difficulty 2318 · geometry, sorting

Original problem by Valentin Zuev, from the Ural School Programming Contest 2020.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n cannon batteries at distinct integer points. From a battery
one can fly on a cannonball towards any other battery, jump off over any
battery on the way, and the ball flies on forever. Find the smallest
distance to the origin that can be reached this way, with absolute or
relative error at most 10⁻⁶. The limits are 2 seconds and 256 MB.

## Input

n, 2 ≤ n ≤ 10⁵, then the points, |xᵢ|, |yᵢ| ≤ 10⁵.

## Output

The smallest distance.

## Examples

### Example 1

Input:

```
4
1 0
0 1
-1 0
0 -1
```

Output:

```
0.0000000000
```

### Example 2

Input:

```
5
0 3
1 2
1 3
1 4
2 3
```

Output:

```
0.7071067812
```

## Solution

Every battery can be reached from every other, and a flight from A over
B followed by one from B over A covers the whole line AB. So the answer
is the smallest distance from the origin to a line through two
batteries, |A × B| / |A − B|, and 0 if a battery is at the origin.

Checking all pairs is too slow, but only pairs that are neighbours in
the order of directions modulo π are needed: sort the points by the
angle of the line from the origin through them, x / y as a key, and take
every pair of cyclic neighbours: the two points of the closest line are
always neighbours in this cyclic order, on one side or the other. Points on one line through
the origin have equal keys, are neighbours and give 0. An exhaustive
comparison with all pairs on many small random sets agrees with this.
The work is O(n log n).

Pitfall: compare answers numerically with absolute or relative error at
most 10⁻⁶, rather than comparing their text. In test 01, both `0` and
`0.0000000000` are valid outputs. The checker accepts either format and
rejects non-finite values and extra tokens.

In the first example the line through (1, 0) and (−1, 0) passes through
the origin.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2154_geometry_sorting.cpp](2154_geometry_sorting.cpp) | G++ 13.2 x64 | geometry, sorting | O(n log n) | AC | 0.062 s | 1580 KB |
| [2154_geometry_sorting.go](2154_geometry_sorting.go) | Go 1.14 x64 | geometry, sorting | O(n log n) | AC | 0.062 s | 9244 KB |
| [2154_geometry_sorting.java](2154_geometry_sorting.java) | Java 1.8 | geometry, sorting | O(n log n) | AC | 0.187 s | 9136 KB |
| [2154_geometry_sorting.py](2154_geometry_sorting.py) | Python 3.12 x64 | geometry, sorting | O(n log n) | AC | 0.312 s | 30008 KB |
| [2154_geometry_sorting.rs](2154_geometry_sorting.rs) | Rust 1.75 x64 | geometry, sorting | O(n log n) | AC | 0.062 s | 6320 KB |
