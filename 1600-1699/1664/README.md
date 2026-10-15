# 1664. Pipeline Transportation

[Timus 1664](https://acm.timus.ru/problem.aspx?space=1&num=1664) · difficulty 1965 · graphs

Original problem by Artem Melentyev, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, January 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N stations lie in the plane, and M straight pipes join pairs of them;
two pipes meet only at a common station. Each pipe carries at most its
capacity, in either direction. Station 1 has the smallest x and station
N the largest. Find the maximum flow from station 1 to station N and a
plan: for every pipe, the direction and the amount.

## Input

N (2 ≤ N ≤ 10000) and the coordinates of the stations (integers of
absolute value at most 10⁸), then M and the pipes as two stations and a
capacity from 1 to 10⁸. The maximum flow is positive and at most 2·10⁹.

## Output

The maximum flow, then M lines "A B C": C units flow from A to B, with
C ≥ 0 and every pipe listed exactly once.

## Examples

### Example 1

Input:

```
3
0 0
1 1
2 0
2
1 2 2
2 3 1
```

Output:

```
1
1 2 1
2 3 1
```

## Solution

The pipes form a plane graph with the source and the sink on the outer
face, so a maximum flow comes from shortest paths in the dual graph.
Add one extra edge that leaves the source to the left, goes round the
outside and enters the sink from the right; it splits the outer face in
two, an upper and a lower one. Every cut between source and sink is a
path in the dual from one of these faces to the other, so the maximum
flow equals the shortest such path with capacities as lengths.

The faces come from sorting the pipes around each station by angle:
after arriving at a station along a pipe, a face continues along the
next pipe clockwise. Dijkstra from one of the two gives a distance d for
every face, and the flow along a pipe from its left face to its right
one is d(right) − d(left). These differences never exceed the capacity,
cancel out around every transit station and add up to the shortest
distance at the source. `O(M log M)`.

Pitfalls:

- with coordinates up to 10⁸ two directions can differ by less than a
  double can tell (test 02), so the angles are compared exactly with
  integer cross products; Python sorts by floating angles first and
  then repairs the nearly equal neighbours exactly;
- parts of the map that the source cannot reach have faces out of reach
  of Dijkstra; their pipes get no flow (test 04);
- the direction of the extra edge fixes the sign of all differences, so
  the solution flips the plan if the source would receive oil.

The flows are checked by a checker for capacity, conservation and total,
and the totals match an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1664_graphs.cpp](1664_graphs.cpp) | G++ 13.2 x64 | graphs | O(M log M) | AC | 0.078 s | 5244 KB |
| [1664_graphs.go](1664_graphs.go) | Go 1.14 x64 | graphs | O(M log M) | AC | 0.062 s | 8164 KB |
| [1664_graphs.java](1664_graphs.java) | Java 1.8 | graphs | O(M log M) | AC | 0.187 s | 9512 KB |
| [1664_graphs.py](1664_graphs.py) | Python 3.12 x64 | graphs | O(M log M) | AC | 0.296 s | 33124 KB |
| [1664_graphs.rs](1664_graphs.rs) | Rust 1.75 x64 | graphs | O(M log M) | AC | 0.031 s | 8920 KB |
