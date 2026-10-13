# 1441. From the History of Gringotts Bank

[Timus 1441](https://acm.timus.ru/problem.aspx?space=1&num=1441) · difficulty 1133 · graphs

Original problem by Magaz Asanov (idea), Stanislav Vasiliev (text) and Pavel Zuev (preparation), from the Tenth Ural Collegiate Team Programming Championship, March 24–25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The goblins dug M tunnels between N rooms of the bank
(2 ≤ N ≤ 20000, 1 ≤ M ≤ 20000); no tunnel joins a room to itself, no two
tunnels join the same pair of rooms, and all rooms are connected. Each
tunnel was dug by a hyperworm, and one hyperworm can dig a whole chain of
tunnels where each next tunnel starts in the room where the previous one
ended, but it never walks through an existing tunnel. Find the smallest
number of hyperworms K that could have dug all tunnels, and the route of
each.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N and M, then M pairs of rooms joined by tunnels.

## Output

K, then K lines, each listing the rooms one hyperworm passes in order.
Any valid plan is accepted.

## Examples

### Example 1

Input:

```
7 7
1 2
4 1
6 7
5 7
7 4
2 3
4 2
```

Output:

```
3
5 7 4 2 1 4
2 3
6 7
```

## Solution

Every hyperworm route is a trail: a walk that uses each tunnel at most
once. A room with an odd number of tunnels must be an end of some trail,
so with 2k odd rooms at least k trails are needed, and at least one in
any case. That many always suffice: add a helper vertex joined to every
odd room, after which all degrees are even and the connected graph has
an Euler circuit. Removing the 2k helper edges cuts the circuit into k
trails of real tunnels; with no odd rooms the circuit itself is the
single route.

The circuit comes from Hierholzer's algorithm with an explicit stack:
from the vertex on top take the next unused edge, or pop the vertex into
the circuit when none is left, with a pointer per vertex so that every
edge is looked at O(1) times. A route through 20000 rooms would be too deep
for recursion. `O(N + M)`.

Pitfalls:

- with no odd rooms the answer is one closed route, not zero (tests 03,
  07, gen2);
- a star makes almost every room odd (tests 04, gen3);
- the route may pass a room several times (tests 05, 09).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1441_graphs.cpp](1441_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.046 s | 2604 KB |
| [1441_graphs.go](1441_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.062 s | 8992 KB |
| [1441_graphs.java](1441_graphs.java) | Java 1.8 | graphs | O(N + M) | AC | 0.140 s | 5212 KB |
| [1441_graphs.py](1441_graphs.py) | Python 3.12 x64 | graphs | O(N + M) | AC | 0.140 s | 13552 KB |
| [1441_graphs.rs](1441_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.031 s | 4688 KB |
