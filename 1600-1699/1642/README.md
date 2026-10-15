# 1642. 1D Maze

[Timus 1642](https://acm.timus.ru/problem.aspx?space=1&num=1642) · difficulty 96 · implementation

Original problem by Daniil Ayzenshteyn, from the USU Junior Contest, October 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A person stands at 0 on a line with obstacles and an exit at x. They
walk in a chosen direction, leave as soon as they reach the exit, and
turn around at every obstacle. For both starting directions, forward
(increasing) and backward, find the distance walked before leaving, or
report that the exit cannot be reached.

## Input

n and x (0 ≤ n ≤ 100), then n distinct obstacle coordinates. All
coordinates are non-zero, at most 1000 in absolute value, and no
obstacle is at the exit. Whatever the direction, the walk meets the
exit or an obstacle.

## Output

Two distances, forward first, or `Impossible`.

## Examples

### Example 1

Input:

```
3 -2
-10 -4 2
```

Output:

```
6 2
```

### Example 2

Input:

```
3 -2
10 -1 2
```

Output:

```
Impossible
```

## Solution

Only the nearest obstacles matter: left, the largest one below 0 (or −∞
if absent), and right, the smallest one above 0 (or +∞ if absent). The
exit is reachable exactly when left < x < right; otherwise
`Impossible`. In both directions the walk is then direct, or one detour:

- x > 0: forward x; backward to left and back, 2 · |left| + x;
- x < 0: forward to right and back, 2 · right + |x|; backward |x|.

The obstacle needed for the detour exists by the promise in the
statement. `O(n)`.

Pitfalls:

- an obstacle between the start and the exit blocks both directions,
  so one answer covers both (the second example, test 06);
- there may be no obstacles at all on the side of the exit.

The answers match an independent accepted implementation on 300 random
lines.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1642_implementation.cpp](1642_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB |
| [1642_implementation.go](1642_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1076 KB |
| [1642_implementation.java](1642_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1688 KB |
| [1642_implementation.py](1642_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 504 KB |
| [1642_implementation.rs](1642_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.062 s | 228 KB |
