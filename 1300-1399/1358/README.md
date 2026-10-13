# 1358. Cables

[Timus 1358](https://acm.timus.ru/problem.aspx?space=1&num=1358) · difficulty 540 · graphs

Original problem by Den Raskovalov (statement by Aleksandr Bikbaev), from the School Championship, March 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N ≤ 1000 computers are joined by N − 1 cables into a connected network,
that is, a tree. Place the computers as points in the plane, with
coordinates of absolute value at most 1000, so that the cables, drawn as
straight segments, do not cross, and every two computers are farther
apart than 1.

Time limit: 0.25 seconds. Memory limit: 64 MB.

## Input

N, then N − 1 lines with the ends a, b of each cable.

## Output

N lines with the coordinates of computers 1 to N. Any valid placement
is accepted.

## Examples

### Example 1

Input:

```
3
1 2
2 3
```

Output:

```
0 0
10 0
0 10
```

## Solution

Root the tree at computer 1 and walk it depth-first. Put each computer
in the column given by its place in that walk, x = 2 · index − 999, and
in the row given by its depth, y = depth. Every computer gets its own
column, two units from the next one, so all distances are at least 2,
and all coordinates stay within [−999, 999].

The cables never cross. Every cable joins a computer in some row to a
child in the next row, so two cables can only meet if they lie in the
same strip between two rows. A depth-first walk visits each subtree as
one block of consecutive columns, and the computers of one row have
disjoint subtrees; so the cables leaving two different computers of a
row stay inside two disjoint column ranges, and the cables leaving the
same computer only share that end. `O(N)`.

Pitfalls:

- a path of 1000 computers is 999 rows deep, which still fits in the
  bounds (generated test 2);
- N = 1 has no cables at all (test 02);
- the walk must be iterative or have enough stack for depth 999.

The tests are judged by a checker that tests the bounds, every pair of
points and every pair of cables, including cables that share an end and
overlap.

## Language notes

- The languages visit children in different orders, so their answers
  differ, which is why a checker is needed; all of them follow the same
  rule.
- Java keeps the adjacency lists in flat arrays to stay within the
  short time limit.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1358_graphs.cpp](1358_graphs.cpp) | G++ 13.2 x64 | graphs | O(N) | AC | 0.015 s | 260 KB |
| [1358_graphs.go](1358_graphs.go) | Go 1.14 x64 | graphs | O(N) | AC | 0.031 s | 1208 KB |
| [1358_graphs.java](1358_graphs.java) | Java 1.8 | graphs | O(N) | AC | 0.140 s | 624 KB |
| [1358_graphs.py](1358_graphs.py) | Python 3.12 x64 | graphs | O(N) | AC | 0.093 s | 820 KB |
| [1358_graphs.rs](1358_graphs.rs) | Rust 1.75 x64 | graphs | O(N) | AC | 0.046 s | 308 KB |
