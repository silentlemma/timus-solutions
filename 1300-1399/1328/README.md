# 1328. Fireball

[Timus 1328](https://acm.timus.ru/problem.aspx?space=1&num=1328) · difficulty 1408 · geometry

Original problem by Pavel Egorov, from the Tenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 16, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A rectangular room spans from (0, 0) to (W, H), with 2 ≤ W, H ≤ 1000. A
point thrown from A moves in a straight line and bounces off the walls,
the angle of incidence equal to the angle of reflection. A hit exactly
in a corner sends it straight back and counts as two bounces. Find the
direction in which to throw it from A so that it reaches B after
exactly N bounces, 0 ≤ N ≤ 10, along the shortest such path. Among
equally short paths print the smallest angle. A and B are inside the
room, and all numbers are integers. Until its last bounce the point
flies through everything except the walls, the target included.

The angle is in degrees, counted counter-clockwise from the direction of
the x axis, from 0 up to 360, with two digits after the point.

Time limit: 1 second. Memory limit: 64 MB.

## Input

W and H, then N, then the coordinates of A and of B.

## Output

The angle.

## Examples

### Example 1

Input:

```
1000 10
3
101 5 128 8
```

Output:

```
45.00
```

## Solution

Reflect the room instead of the path. Mirroring the room across its
walls again and again tiles the plane, and a bouncing path becomes a
straight line through the copies. Copy (i, j), i rooms across and j
rooms up, holds an image of B at

x = i · W + (Bx if i is even, else W − Bx),
y = j · H + (By if j is even, else H − By),

and the straight line from A to it crosses |i| vertical and |j|
horizontal walls, so it bounces |i| + |j| times. A corner is a vertical
and a horizontal wall at once, which matches the rule that it counts
twice, and mirroring in both walls is exactly the reflection back.

So the candidates are the 4N images with |i| + |j| = N (one for
N = 0), compared by squared length, exactly in integers, and then by
angle. A line may pass through an image with fewer bounces on its way,
but that only means the point flies through the target before its
last bounce, which it does unharmed. `O(N)`.

Pitfalls:

- the shortest path may cross the target before the last bounce: in a
  2 by 2 room with the target in the middle the diagonal crosses it
  between every two corners and still wins (test 08);
- the target may stand where the thrower stands, and then paths of the
  same length leave in several directions (test 05);
- a shot into a corner is two bounces (test 06);
- the angle is from 0 up to 360, so negative results of atan2 get 360
  added (test 03).

The answers were compared with a simulation that follows each bounce
with exact fractions, for every direction towards an image within N + 1
rooms, on 600 random small rooms, and with an independent program on
300 random rooms.

## Language notes

- All five solutions compute the angle as atan2 · 180 / π in the same
  order, so that they round in the same way.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1328_geometry.cpp](1328_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 212 KB |
| [1328_geometry.go](1328_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.015 s | 1116 KB |
| [1328_geometry.java](1328_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.125 s | 1864 KB |
| [1328_geometry.py](1328_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.093 s | 512 KB |
| [1328_geometry.rs](1328_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.046 s | 268 KB |
