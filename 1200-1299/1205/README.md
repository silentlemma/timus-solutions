# 1205. The fastest way across town on foot and by subway

[Timus 1205](https://acm.timus.ru/problem.aspx?space=1&num=1205) · difficulty 235 · graphs

Original problem by Alexander Klepinin, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

You can walk anywhere at one speed or ride the subway at a speed at
least as high, between `2 ≤ N ≤ 200` stations joined by up to 400
straight two-way links; trains can be boarded, left and changed only at
stations, at no cost in time. Find the fastest way from point A to point
B and the stations it passes through.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The walking and subway speeds; `N` and the stations' coordinates; the
links as pairs of station numbers, ended by `0 0`; then A and B.

## Output

The least time, accurate to `10⁻⁶`, then the number of stations on the
route followed by the stations in the order they are visited.

## Checking

Several routes can take the same time, so any is accepted if its printed
time matches the time of the route itself, counted as walking from A to
the first station, riding between linked consecutive stations, walking
between unlinked ones and walking from the last station to B, and if
that time is the least.

## Examples

### Example 1

Input:

```
1 100
4
0 0
1 0
9 0
9 9
1 2
1 3
2 4
0 0
10 10
10 0
```

Output:

```
2.6346295
4 4 2 1 3
```

## Solution

Make a complete graph on the stations, A and B: between any two points
the cost is the walking time, except between linked stations, where it is
the riding time; riding is never slower over the same straight line.
Dijkstra's algorithm on this dense graph of `N + 2` nodes, picking the
next node by a linear scan, gives the least time, and the predecessors
give the route; the stations on it are the route without A and B.
`O(N²)`.

Pitfalls:

- the route can be empty: with equal speeds, or when no subway trip
  helps, the answer is to walk straight and print `0` stations;
- walking between two stations is allowed and can be part of the best
  route, for example to change to another line nearby;
- the list of links can be empty, with `0 0` right after the stations.

The routes were compared with a separately written solution on 200
random cities and on every test, using the checker in both directions.

## Language notes

- All languages run the same quadratic Dijkstra on an adjacency matrix
  and print ten decimals; Java formats the time with `Locale.US`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1205_graphs.cpp](1205_graphs.cpp) | G++ 13.2 x64 | graphs | O(N²) | AC | 0.015 s | 256 KB |
| [1205_graphs.go](1205_graphs.go) | Go 1.14 x64 | graphs | O(N²) | AC | 0.031 s | 1208 KB |
| [1205_graphs.java](1205_graphs.java) | Java 1.8 | graphs | O(N²) | AC | 0.125 s | 1416 KB |
| [1205_graphs.py](1205_graphs.py) | Python 3.12 x64 | graphs | O(N²) | AC | 0.062 s | 1012 KB |
| [1205_graphs.rs](1205_graphs.rs) | Rust 1.75 x64 | graphs | O(N²) | AC | 0.046 s | 344 KB |
