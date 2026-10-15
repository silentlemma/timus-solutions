# 1632. Lasers

[Timus 1632](https://acm.timus.ru/problem.aspx?space=1&num=1632) · difficulty 4586 · shortest_paths

Original problem by Dmitry Ivankov (prepared by Alex Samsonov), from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N laser beams cross a room. Beam i starts at (X_i, Y_i, Z_i) and goes along
(u_i, v_i, w_i); everything is known except the heights Z_i. For some
pairs it is known that beam i is above beam j: where their vertical
projections cross, at a common (X, Y), beam i is strictly higher. Find
any heights consistent with all pairs, each within 10⁶ in absolute value.

## Input

The first line holds N (1 ≤ N ≤ 100); each of the next N lines holds X_i,
Y_i, u_i, v_i, w_i, integers up to 100 in absolute value. Then M
(0 ≤ M ≤ 10000) and M lines "i j", meaning beam i is above beam j. No
beam is vertical and no two beams lie in one vertical plane; a valid
arrangement exists.

## Output

N real numbers Z_i, one per line, printed as precisely as possible.

## Examples

### Example 1

Input:

```
4
0 0 1 0 0
1 0 0 1 0
1 1 -1 0 0
0 1 0 -1 0
3
1 2
2 3
3 4
```

Output:

```
4.000
3.000
2.000
1.000
```

## Solution

Where the projections of beams i and j cross, at parameters t_i and t_j
(two linear equations in two unknowns), the heights are Z_i + w_i t_i
and Z_j + w_j t_j. So "i above j" reads Z_i − Z_j > c with
c = w_j t_j − w_i t_i: a system of difference constraints, which is a
longest-path problem on a graph with an edge j → i of weight c.

Bellman–Ford from an imaginary source joined to every beam with weight 0
gives heights that satisfy every constraint with ≥ and have the
smallest possible spread, so if any answer fits into [−10⁶, 10⁶], this
one does too. Rounds stop early: only beams raised in the previous round
are relaxed again.

The constraints met with equality ("tight", slack below 10⁻⁷) must become
strict. They form an acyclic graph, since a tight cycle would be a cycle
of weight 0, which no valid input has. Every beam gets its level in that
graph (the longest chain of tight edges ending in it) and is raised by
step · level. Each tight edge gains at least one step; any other edge
loses at most step · levels. Taking step = room / (2 · levels + 2), where
room is the smaller of the least non-tight slack and the free space
2 · 10⁶ minus the spread, keeps every other edge strict and the spread
within the box. Finally the heights are centred and printed with
10 decimals. `O(N · M)`.

Pitfalls:

- the relation is not transitive and may contain cycles, since each pair
  meets at its own point, so a topological sort of the input pairs fails;
- with all lifts 0 (the example) every edge is tight and the steps alone
  separate the beams;
- printing too few decimals can erase a tiny margin.

The checker verifies every pair exactly in rational arithmetic, and the
answers pass it on all tests, as do those of an independent accepted
implementation. All five programs compute in doubles.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1632_shortest_paths.cpp](1632_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(N · M) | AC | 0.015 s | 368 KB |
| [1632_shortest_paths.go](1632_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(N · M) | AC | 0.031 s | 1608 KB |
| [1632_shortest_paths.java](1632_shortest_paths.java) | Java 1.8 | shortest_paths | O(N · M) | AC | 0.125 s | 1580 KB |
| [1632_shortest_paths.py](1632_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(N · M) | AC | 0.078 s | 1888 KB |
| [1632_shortest_paths.rs](1632_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(N · M) | AC | 0.046 s | 596 KB |
