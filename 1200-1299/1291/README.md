# 1291. Gear-wheels

[Timus 1291](https://acm.timus.ru/problem.aspx?space=1&num=1291) · difficulty 383 · bfs

Original problem by Pavel Egorov, from the Ninth Open Team Programming Contest for Schoolchildren, March 13, 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 1000 gears, each with 1 to 1000 teeth, are meshed in pairs, and
the links form no cycle. One gear is driven counterclockwise at a
speed from 1 to 1000. Print the speed of every gear as a reduced
fraction: positive for counterclockwise, negative for clockwise, and
0/1 for a gear that does not turn.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then for each gear its number of teeth and the list of gears it is
meshed with, ended by 0. The last line holds the driven gear and its
speed.

## Output

N lines with the speeds as `p/q`, the minus sign before p.

## Examples

### Example 1

Input:

```
4
10 2 3 0
20 1 0
40 1 4 0
100 3 0
1 6
```

Output:

```
6/1
-3/1
-3/2
3/5
```

## Solution

Two meshed gears pass the same number of teeth per unit of time, so
speed × teeth is equal for both, and they turn in opposite directions.
Going along any chain from the driven gear r, speed × teeth never
changes, so every gear j that the drive reaches turns at

± speed · teeth(r) / teeth(j),

with the sign flipping at every link: + at an even distance from r and
− at an odd one. Since the links form no cycle, the distance is well
defined, and a breadth-first search from r finds its parity. Gears not
reached stand still. Each fraction is reduced by the gcd of
speed · teeth(r) ≤ 10⁶ and teeth(j), which fits in 32 bits. `O(N + L)`,
where L is the number of listed links.

Pitfalls:

- gears outside the driven tree print 0/1 (test 03);
- the statement does not promise that a link is listed at both ends,
  so every link is stored both ways (test 04);
- fractions must be reduced (test 05).

The answers were compared with a direct propagation of exact fractions
on 40 random forests.

## Language notes

- The search uses an explicit queue, so a path of 1000 gears needs no
  deep recursion.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1291_bfs.cpp](1291_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + L) | AC | 0.015 s | 248 KB |
| [1291_bfs.go](1291_bfs.go) | Go 1.14 x64 | bfs | O(N + L) | AC | 0.015 s | 1192 KB |
| [1291_bfs.java](1291_bfs.java) | Java 1.8 | bfs | O(N + L) | AC | 0.078 s | 784 KB |
| [1291_bfs.py](1291_bfs.py) | Python 3.12 x64 | bfs | O(N + L) | AC | 0.078 s | 988 KB |
| [1291_bfs.rs](1291_bfs.rs) | Rust 1.75 x64 | bfs | O(N + L) | AC | 0.015 s | 264 KB |
