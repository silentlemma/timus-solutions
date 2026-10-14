# 1623. Fractal Labyrinth

[Timus 1623](https://acm.timus.ru/problem.aspx?space=1&num=1623) · difficulty 3124 · shortest_paths

Original problem from the SPbSU ITMO Contest at the Petrozavodsk Training Camp, Winter 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A house has N doors (2 ≤ N ≤ 20) and contains K inner houses
(K ≤ 5), each an exact copy of the whole house, so the nesting goes on
forever. M roads of length 1 join doors of the outer house and of the
inner houses (house 0 is the outer one, doors `house.door`). Find the
shortest path between two given doors of the outer house, or print
`no solution`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and K, then M and the roads `a.b - c.d`, then the two doors.

## Output

The length of the shortest path, or `no solution`.

## Examples

### Example 1

Input:

```
12 1
11
0.0 - 1.1
0.1 - 0.2
1.2 - 1.3
0.3 - 0.4
1.4 - 1.5
0.5 - 0.6
1.6 - 1.7
0.7 - 0.8
1.8 - 1.9
0.9 - 0.10
1.10 - 0.11
0 11
```

Output:

```
11
```

### Example 2

Input:

```
8 0
8
0.0 - 0.2
0.1 - 0.3
0.2 - 0.4
0.3 - 0.5
0.4 - 0.6
0.5 - 0.7
0.6 - 0.0
0.7 - 0.1
2 5
```

Output:

```
no solution
```

## Solution

Let D(i, j) be the distance between doors i and j of the outer house.
Going through an inner house from its door i to its door j costs exactly
D(i, j), since the inner house is a copy. So D is a fixed point: it is
the shortest-path distance in the graph of all (K + 1) · N doors, with
the roads and with an edge of length D(i, j) between doors i and j of
every inner house.

Start with D = ∞ (inner houses closed) and recompute D from the graph
again and again. After round t, D counts every path that goes at most t
houses deep, so the values only shrink towards the true distances; each
round depends only on the previous one, so once a round changes nothing,
D is final. A round runs Dijkstra on the dense graph from each of the N
outer doors. `O(R · N · ((K + 1) N)²)` for R rounds.

Pitfalls:

- the two doors may coincide: the answer is 0 (test 03);
- the best path may need several levels of nesting, found only in later
  rounds (test 04: 6 after one round, 5 after two);
- a door may have no roads at all (test 06).

The answers match an independent accepted implementation on 360 random
labyrinths.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1623_shortest_paths.cpp](1623_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(R · N · ((K + 1) N)²) | AC | 0.015 s | 552 KB |
| [1623_shortest_paths.go](1623_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(R · N · ((K + 1) N)²) | AC | 0.015 s | 3908 KB |
| [1623_shortest_paths.java](1623_shortest_paths.java) | Java 1.8 | shortest_paths | O(R · N · ((K + 1) N)²) | AC | 0.109 s | 2928 KB |
| [1623_shortest_paths.py](1623_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(R · N · ((K + 1) N)²) | AC | 0.250 s | 952 KB |
| [1623_shortest_paths.rs](1623_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(R · N · ((K + 1) N)²) | AC | 0.031 s | 340 KB |
