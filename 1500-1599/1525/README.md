# 1525. Path

[Timus 1525](https://acm.timus.ru/problem.aspx?space=1&num=1525) · difficulty 375 · implementation

Original problem by Dmitry Gozman, from Dmitry Gozman Contest 1 at the Petrozavodsk Winter Training Camp, January 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A robot stands in an unknown cell of an n × m × k box (1 ≤ n, m, k ≤ 10⁵)
and runs a program of at most 10⁵ moves: 'l' and 'r' along the width,
'd' and 'u' along the height, 'b' and 'f' along the length. A move that
would leave the box is ignored. Count the cells where the robot can end.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n, m and k, then the program on one line.

## Output

The number of possible final cells.

## Examples

### Example 1

Input:

```
1 1 1
uuuur
```

Output:

```
1
```

### Example 2

Input:

```
2 2 2
ulf
```

Output:

```
1
```

### Example 3

Input:

```
13 14 15
uudlbdrruffbr
```

Output:

```
1560
```

## Solution

The three axes do not affect each other, so the answer is the product
of the counts for each axis. On one axis a move shifts every start by
one or leaves it at the wall, so two neighbouring starts stay in order
and at most one apart. Hence the finishes of all starts fill the whole
range between the finishes of the two extreme starts 1 and L, and that
axis gives f(L) − f(1) + 1. Simulate just those two starts. `O(len)`.

Pitfalls:

- the count reaches about 10¹⁵ and needs 64 bits (test 04, gen1);
- the program can be empty, and then every cell counts (test 05);
- a long run of moves pushes every start against a wall (tests 01, 06,
  gen3).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1525_implementation.cpp](1525_implementation.cpp) | G++ 13.2 x64 | implementation | O(len) | AC | 0.015 s | 528 KB |
| [1525_implementation.go](1525_implementation.go) | Go 1.14 x64 | implementation | O(len) | AC | 0.015 s | 1748 KB |
| [1525_implementation.java](1525_implementation.java) | Java 1.8 | implementation | O(len) | AC | 0.140 s | 2212 KB |
| [1525_implementation.py](1525_implementation.py) | Python 3.12 x64 | implementation | O(len) | AC | 0.109 s | 692 KB |
| [1525_implementation.rs](1525_implementation.rs) | Rust 1.75 x64 | implementation | O(len) | AC | 0.046 s | 468 KB |
