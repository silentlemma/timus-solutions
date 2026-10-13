# 1422. Fireflies

[Timus 1422](https://acm.timus.ru/problem.aspx?space=1&num=1422) · difficulty 851 · geometry

Original problem by Ilya Grebnov, Dmitry Kovalioff and Nikita Rybak, from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N flies (1 ≤ N ≤ 2000) hang still at integer points with coordinates up
to 10⁷ by absolute value. A point-sized fireball flies along any
straight line and turns every fly it meets into a firefly. Find the
largest number of flies one fireball can reach, that is, the largest
number of the points on one line.

Time limit: 3 seconds. Memory limit: 64 MB.

## Input

N, then N lines X Y Z.

## Output

The largest number of flies on one line.

## Examples

### Example 1

Input:

```
6
-1 1 -1
0 1 2
0 0 -1
-2 -1 2
2 -1 -2
-1 0 2
```

Output:

```
3
```

## Solution

Take every fly in turn as the first fly of a line and look at the
directions to the flies after it. Two flies lie on the same line
through the first one exactly when their difference vectors are
multiples of each other, so each vector is divided by the greatest
common divisor of its parts and its sign is fixed so that the first
non-zero part is positive. Equal reduced vectors mean the same line;
counting them (with a hash map, or by sorting) gives the best line
through this fly. Flies at the very same point as the first one lie on
every line through it and are added to the best count. Expected
`O(N² log C)` with hashing; `O(N²(log C + log N))` with sorting,
for C = 2·10⁷, including the gcd.

Pitfalls:

- several flies may share a point (tests 03, 05, gen4);
- one fly alone still counts as 1 (test 02);
- differences reach 2·10⁷, which still fits in 32 bits, and integer
  keys avoid any rounding of directions (tests 06, gen2).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1422_geometry.cpp](1422_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2 (log C + log N)) | AC | 0.328 s | 224 KB |
| [1422_geometry.go](1422_geometry.go) | Go 1.14 x64 | geometry | O(N^2 log C) | AC | 0.468 s | 6524 KB |
| [1422_geometry.java](1422_geometry.java) | Java 1.8 | geometry | O(N^2 log C) | AC | 0.343 s | 744 KB |
| [1422_geometry.py](1422_geometry.py) | Python 3.12 x64 | geometry | O(N^2 log C) | AC | 1.828 s | 1868 KB |
| [1422_geometry.rs](1422_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2 (log C + log N)) | AC | 0.312 s | 312 KB |
