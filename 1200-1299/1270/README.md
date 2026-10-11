# 1270. Unicube

[Timus 1270](https://acm.timus.ru/problem.aspx?space=1&num=1270) · difficulty 2285 · matching

Original problem by Alexander Mironenko, from the Ural State University Championship, October 25, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are N ≤ 30 cubes, each face painted one of 30 colours, given in
the order front, up, right, down, left, back. A figure has M ≤ 30 cells,
each with demands on the colours of its six faces (0 means any colour).
Put a different cube, turned as needed, into every cell so that all
demands hold, and print the cube number for each cell, or 0 if this is
impossible.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, the N cubes, M, then M lines `X Y Z F U R D L B`.

## Output

M cube numbers, or 0.

## Checking

Several assignments may work, so the checker accepts any: the numbers
must be distinct, and each cube must meet the demands of its cell in one
of the 24 rotations. An answer of 0 is accepted only when the expected
answer is 0.

## Examples

### Example 1

Input:

```
1
6 1 3 4 5 2
1
0 0 0 1 2 3 6 5 4
```

Output:

```
1
```

## Solution

Where a cell stands does not matter: demands are only on faces, and
neighbouring cubes do not interact. So the task is a bipartite matching
between cells and cubes. A cube may go to a cell if one of its 24
rotations meets all the cell's demands. The rotations are found by
closing two quarter turns, about the vertical axis and about the
left-right axis, under composition. This gives exactly the 24 proper
rotations and none of the mirror images. Kuhn's algorithm then tries
an augmenting path from every cell; if one fails, the answer is 0.
`O(M · N · 24 · 6 + M · N · M)`.

Pitfalls:

- only rotations are allowed: a cube whose mirror image fits a cell
  may still not fit it (test 02);
- a greedy choice can block a later cell, so the matching must be able
  to move cubes already placed (test 05);
- with more cells than cubes there is no answer (test 03).

Whether an assignment exists was compared with trying every injective
assignment on 300 small random cases.

## Language notes

- All languages build the rotations the same way and run Kuhn's
  algorithm recursively; the depth is at most 30.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1270_matching.cpp](1270_matching.cpp) | G++ 13.2 x64 | matching | O(M · N · 24 · 6 + M · N · M) | AC | 0.015 s | 212 KB |
| [1270_matching.go](1270_matching.go) | Go 1.14 x64 | matching | O(M · N · 24 · 6 + M · N · M) | AC | 0.031 s | 1184 KB |
| [1270_matching.java](1270_matching.java) | Java 1.8 | matching | O(M · N · 24 · 6 + M · N · M) | AC | 0.093 s | 716 KB |
| [1270_matching.py](1270_matching.py) | Python 3.12 x64 | matching | O(M · N · 24 · 6 + M · N · M) | AC | 0.093 s | 752 KB |
| [1270_matching.rs](1270_matching.rs) | Rust 1.75 x64 | matching | O(M · N · 24 · 6 + M · N · M) | AC | 0.015 s | 452 KB |
