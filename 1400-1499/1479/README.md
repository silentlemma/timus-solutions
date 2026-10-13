# 1479. Scheduled Checking

[Timus 1479](https://acm.timus.ru/problem.aspx?space=1&num=1479) · difficulty 3958 · bitmask

Original problem by Alexander Ipatov, from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A simple graph has N stops (3 ≤ N ≤ 14) and M roads. The company runs
as many routes as possible, each a ring through at least three
different stops with no stop repeated, and any two routes differing in
at least one road. A schedule is a table: rows are moments, columns are
routes, and a cell holds the stop where that route's bus is checked at
that moment. Every bus is checked once at each stop of its route, no
stop checks two buses at once, and no bus is at two stops at once.
Find the smallest possible number of rows.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

N and M, then M lines with the two stops of a road.

## Output

The smallest number of rows.

## Examples

### Example 1

Input:

```
4 4
1 2
2 3
1 3
1 4
```

Output:

```
3
```

## Solution

Two different simple cycles always differ in some road, so the routes
are all simple cycles of the graph. Join each route to each of its
stops: the schedule must cover every such pair once, and a row is a set
of pairs that share no route and no stop, a matching. Covering the
edges of a bipartite graph by matchings is edge colouring, and by
König's theorem the largest degree is enough. So the answer is the
larger of the longest route (its number of stops) and the largest
number of routes through one stop, or 0 when there are no cycles.

The cycles are counted by sets of stops. For each set S, count the
simple paths that start at the lowest stop of S, pass through all of S
and end at v; those with v next to the start close into cycles with
stop set S, each counted once per direction. Every path grows only
through stops above its start, so each cycle is seen from its lowest
stop only. Adding the cycles of every S to each stop of S gives the
counts per stop. `O(2^N·N²)`.

Pitfalls:

- with no cycles there are no routes and no rows (tests 02, 03);
- with all 14 stops joined, about 8.5·10⁹ routes pass through each stop,
  which needs 64 bits (test 06);
- a lone ring has one route through each stop, so its length decides
  (test 04), and two triangles sharing a stop put two routes there but
  still need 3 rows (test 07).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1479_bitmask.cpp](1479_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^N N^2) | AC | 0.015 s | 1676 KB |
| [1479_bitmask.go](1479_bitmask.go) | Go 1.14 x64 | bitmask | O(2^N N^2) | AC | 0.031 s | 3052 KB |
| [1479_bitmask.java](1479_bitmask.java) | Java 1.8 | bitmask | O(2^N N^2) | AC | 0.125 s | 3700 KB |
| [1479_bitmask.py](1479_bitmask.py) | Python 3.12 x64 | bitmask | O(2^N N^2) | AC | 0.343 s | 4408 KB |
| [1479_bitmask.rs](1479_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^N N^2) | AC | 0.031 s | 2016 KB |
