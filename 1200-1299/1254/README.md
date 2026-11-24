# 1254. Defusing bombs in order across a town

[Timus 1254](https://acm.timus.ru/problem.aspx?space=1&num=1254) · difficulty 646 · shortest_paths

Original problem by Pavel Atnashev, from the Ural State University Open Team Contest, March 15, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A town is an N × M grid (N, M ≤ 75) of free blocks `.` and buildings
`#`. John moves between neighbouring blocks, by a side or diagonally, at
speed V. Starting at (x₀, y₀), he must defuse K bombs (K ≤ 1000) in the
given order; a bomb he cannot reach is skipped. Find the least total
time, to two decimals.

Time limit: 5 seconds. Memory limit: 64 MB.

## Input

N, M, K and V; the map as M lines of N characters; the start; the K
bombs as `x y`.

## Output

The least time, with two digits after the point.

## Examples

### Example 1

Input:

```
4 3 3 1.23
....
##..
....
1 1
1 3
4 1
4 3
```

Output:

```
8.66
```

## Solution

Defusing is instantaneous and the order is fixed, so the total is the
sum of shortest walks from each position to the next reachable bomb,
divided by V. A step along a side is 1 long and a diagonal step √2; a
diagonal step may pass the corner of a building, which the example
needs on its way past `##`.

Up to 1000 shortest-path searches on 5625 cells are needed. Three things
keep them cheap:

- the town is split once into parts joined by moves, so a bomb in
  another part is skipped at once instead of after a full search;
- each search is A* with the octile distance
  `max(dx, dy) + (√2 − 1)·min(dx, dy)` as its estimate, which never
  exceeds the true length, so the first time the bomb leaves the queue
  its distance is final, and in open town the estimate is exact;
- walks already found are kept by their pair of ends, in both
  directions.

The map is surrounded by a border of buildings, so moves need no bounds
check. `O(K · NM log NM)` in the worst case.

Pitfalls:

- after an unreachable bomb John stays where he was (test 03);
- the start may coincide with a bomb, a walk of length 0 (test 02);
- the start cell is treated as free whatever the map shows there.

The totals were compared with a plain Dijkstra search on 300 random
small towns with buildings and unreachable bombs.

## Language notes

- Python is the slowest here: about 1.5 s on the largest winding street
  in testing, against a limit of 5 seconds.

## Optimized solutions

Go uses a typed heap for A* and reuses the heap and distance arrays across searches. Search numbers distinguish stale distances. In a town with no buildings, the octile distance is exact and can be used directly. Submission 11317201 took 0.171 s and used 1376 KB, versus 0.359 s and 6564 KB for the base.

Java stores cell positions in an indexed heap, so a shorter route updates the priority of a queued cell in place. It reuses the primitive arrays across searches. Submission 11317202 took 0.218 s and used 1980 KB, versus 0.375 s and 7200 KB for the base.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321821 · Python 3.12 x64 №11321822 · Rust 1.75 x64 №11321824 · Go 1.14 x64 №11322060 · Java 1.8 №11322061.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1254_shortest_paths.cpp](1254_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(K · NM log NM) | AC | 0.109 s | 288 KB | 11321821 |
| [1254_shortest_paths.go](1254_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(K · NM log NM) | AC | 0.359 s | 6564 KB | 11322060 |
| [1254_shortest_paths.java](1254_shortest_paths.java) | Java 1.8 | shortest_paths | O(K · NM log NM) | AC | 0.375 s | 7200 KB | 11322061 |
| [1254_shortest_paths.py](1254_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(K · NM log NM) | AC | 2.875 s | 1684 KB | 11321822 |
| [1254_shortest_paths.rs](1254_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(K · NM log NM) | AC | 0.14 s | 796 KB | 11321824 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1254_shortest_paths_optimized.go](1254_shortest_paths_optimized.go) | Go 1.14 x64 | shortest_paths | O(K · NM log NM) | AC | 0.171 s | 1376 KB | 11317201 |
| [1254_shortest_paths_optimized.java](1254_shortest_paths_optimized.java) | Java 1.8 | shortest_paths | O(K · NM log NM) | AC | 0.218 s | 1980 KB | 11317202 |
