# 1498. Stroke at Full Speed

[Timus 1498](https://acm.timus.ru/problem.aspx?space=1&num=1498) · difficulty 884 · bfs

Original problem by Alex Samsonov, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A knight stands on an N × M field (N, M ≤ 100) and may make at most L
steps (L ≤ 1000) to neighbouring cells, never leaving the field and
never entering the demon's cell. From a cell next to the demon the
knight then strikes once with force K + 1, where K is the length of the
straight run made just before the strike. Find the largest possible
force, or 0 if the knight cannot get next to the demon at all.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, M and L, then the knight's cell, then the demon's cell.

## Output

The largest force.

## Examples

### Example 1

Input:

```
3 4 4
1 1
3 4
```

Output:

```
4
```

## Solution

The strike happens from one of the at most four cells A next to the
demon, after a straight run of k steps in one of four directions, so
the run starts at S = A − k·d and all its cells must be on the field
and not the demon's. Before the run the knight only needs to reach S,
which takes the breadth-first distance from the start with the demon's
cell blocked. The plan fits when that distance plus k is at most L. Try
every A, every direction and every k until the run leaves the field,
and keep the largest k + 1. If the knight arrives at S already moving
in the run's direction, the real run is only longer, and that longer
run is tried as well. `O(NM)`.

Pitfalls:

- the last run does not have to point at the demon: in the example the
  knight runs along a row and strikes downwards;
- the demon blocks both the way and the run, so the run may have to use
  the next row or column (test 08);
- when no cell next to the demon is in reach the answer is 0, and a
  knight already next to it strikes with force at least 1 (tests 02,
  03, 05).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1498_bfs.cpp](1498_bfs.cpp) | G++ 13.2 x64 | bfs | O(NM) | AC | 0.015 s | 240 KB |
| [1498_bfs.go](1498_bfs.go) | Go 1.14 x64 | bfs | O(NM) | AC | 0.031 s | 2052 KB |
| [1498_bfs.java](1498_bfs.java) | Java 1.8 | bfs | O(NM) | AC | 0.125 s | 1880 KB |
| [1498_bfs.py](1498_bfs.py) | Python 3.12 x64 | bfs | O(NM) | AC | 0.109 s | 1744 KB |
| [1498_bfs.rs](1498_bfs.rs) | Rust 1.75 x64 | bfs | O(NM) | AC | 0.046 s | 276 KB |
