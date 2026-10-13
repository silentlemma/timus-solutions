# 1390. Shots at Walls

[Timus 1390](https://acm.timus.ru/problem.aspx?space=1&num=1390) · difficulty 8198 · geometry

Original problem by Andrew Rumyantsev, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Events happen in order. A wall is a segment whose line
does not pass through the origin; walls may cross. A shot is fired from
the origin with a nonzero velocity (vx, vy), and the bullet flies
straight at constant speed. For every shot print the time until its first
hit on a wall built before it, or Infinite. Coordinates and velocity
components are integers up to 10 000 in absolute value.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

Lines "shot vx vy" and "wall x1 y1 x2 y2", ending with "end".
There are at most 50 000 lines, including "end".

## Output

For every shot the flight time with an error up to 10⁻⁶, or Infinite.

## Examples

### Example 1

Input:

```
shot 1 0
wall 1 0 0 1
shot 1 1
shot -1 3
wall 1 0 -1 2
shot -1 3
wall 1 1 -1 1
shot -1 3
wall 2 3 2 -3
wall 3 -2 -3 -2
shot 1 -1
shot 40 -39
shot 9999 -10000
shot -1 -1
shot -3000 -2000
shot -3001 -2000
shot -3000 -2001
shot 1 0
shot 1 1
wall -1 2 10 -10
shot -1 1
shot 0 1
shot 1 1
shot 1 0
shot 1 -1
wall 0 -10000 -10000 0
shot -2 -1
end
```

Output:

```
Infinite
0.50000000000000000000
Infinite
0.50000000000000000000
0.33333333333333333333
2.00000000000000000000
0.05000000000000000000
0.00020000000000000000
2.00000000000000000000
0.00100000000000000000
Infinite
0.00099950024987506247
1.00000000000000000000
0.50000000000000000000
1.00000000000000000000
0.90909090909090909091
0.43478260869565217391
0.83333333333333333333
2.00000000000000000000
3333.33333333333333333
```

## Solution

Write the line of a wall as n · p = c with c > 0. A bullet with
velocity v reaches the line at time c / (n · v), so the nearest wall in
a direction is the one with the largest (n · v) / c among the walls that
cover that direction. A wall covers the directions from one end to the
other, an arc shorter than π. For two walls the difference of
(n · v) / c over unit vectors v is a sinusoid, which changes sign at
most once on such an arc.

That is the condition for a Li Chao tree. Read all events first, take
the distinct shot directions sorted by angle as the leaves, and process
the events in order. A wall is inserted over the range of leaves it
covers, split in two across the positive x axis (negative in Python):
in each fully covered node the better wall at the middle stays, and the
other one goes down into the half where it can still win. A shot walks
from the root to its leaf and takes the best wall met. Walls are compared
exactly as (n₁ · v)·c₂ against (n₂ · v)·c₁ in 64-bit integers
(arbitrary-precision integers in Python), and the time c / (n · v) is
printed by exact integer division with nine digits. `O(n log² n)`.

Pitfalls:

- a bullet that touches the end of a wall hits it (test 04);
- a wall across the angular wrap covers both ends of the sorted
  directions (tests 05, 10);
- the same direction comes at different speeds, so the leaves are
  directions and the time uses the speed of the shot (test 07);
- a later wall farther away does not hide an earlier nearer one
  (test 06), and walls may cross;
- walls without any shot must still be read (test 02).

The answers were compared with a check of every wall for every shot in
exact fractions on 400 small random cases and, in integers, on all
generated tests.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1390_geometry.cpp](1390_geometry.cpp) | G++ 13.2 x64 | geometry | O(n log^2 n) | AC | 0.218 s | 5452 KB |
| [1390_geometry.go](1390_geometry.go) | Go 1.14 x64 | geometry | O(n log^2 n) | AC | 0.125 s | 11156 KB |
| [1390_geometry.java](1390_geometry.java) | Java 1.8 | geometry | O(n log^2 n) | AC | 0.281 s | 11420 KB |
| [1390_geometry.py](1390_geometry.py) | Python 3.12 x64 | geometry | O(n log^2 n) | AC | 1.937 s | 32172 KB |
| [1390_geometry.rs](1390_geometry.rs) | Rust 1.75 x64 | geometry | O(n log^2 n) | AC | 0.062 s | 8744 KB |
