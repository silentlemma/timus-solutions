# 1077. The most tours that each own a road

[Timus 1077](https://acm.timus.ru/problem.aspx?space=1&num=1077) · difficulty 395 · bfs, graphs

Original problem by Nguyen Xuan My (converted by Dinh Quang Hiep and Tran Nam Trung), from the third contest at the Department of Mathematics and Informatics, College of Natural Sciences, Vietnam National University, Hanoi.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` cities (`1 ≤ N ≤ 200`) are joined by `M` two-way roads, at most one
between two cities. A tour visits `K > 2` different cities in a cycle.
Make as many tours as possible such that each tour has a road that no
other tour uses. Print their number `T` and the tours.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `M`, then `M` lines with the two cities of a road.

## Output

`T`, then `T` lines, each with `K` and the `K` cities of a tour in order.

## Checking

Any valid set of tours is accepted. The checker verifies that `T` is the
largest possible, that every tour is a cycle of more than two different
cities joined by roads, and that every tour has a road used by no other
tour.

## Examples

### Example 1

Input:

```
5 7
1 2
1 3
1 4
2 4
2 3
3 4
5 4
```

Output:

```
3
3 2 1 4
3 2 1 3
3 3 1 4
```

## Solution

Think of the tours as vectors over `GF(2)` with one coordinate per road.
A tour that owns a road is the only one with a 1 in that coordinate, so
no combination of the others can give it: the tours are linearly
independent. Cycles live in the cycle space of the graph, whose dimension
is `M − N + C` for `C` connected components, so `T ≤ M − N + C`.

That bound is reached by the fundamental cycles of a spanning forest.
Each road outside the forest, together with the forest path between its
ends, forms a cycle, and that road belongs to no other such cycle. There
are exactly `M − (N − C)` such roads. A breadth-first forest keeps the
paths short. To list a cycle, lift the deeper end to the depth of the
other, then lift both until they meet. `O(N + M + total output)`.

Pitfalls:

- the graph may be disconnected or have isolated cities, so the forest is
  grown from every city not yet reached;
- a tree or an empty graph gives `T = 0` and no further lines;
- with all 19 900 roads among 200 cities there are 19 701 tours, so the
  output is built in one buffer.

The checker computes `M − N + C` with a disjoint-set union and checks
every tour independently of the solutions.

## Language notes

- Python reads all numbers at once and pairs them with slices;
  `zip(rest[0::2], rest[1::2])` gives the roads.
- Java reads with `StreamTokenizer` and collects the output in a
  `StringBuilder`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1077_bfs.cpp](1077_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + M + output) | AC | 0.015 s | 304 KB |
| [1077_bfs.go](1077_bfs.go) | Go 1.14 x64 | bfs | O(N + M + output) | AC | 0.015 s | 2400 KB |
| [1077_bfs.java](1077_bfs.java) | Java 1.8 | bfs | O(N + M + output) | AC | 0.140 s | 2716 KB |
| [1077_bfs.py](1077_bfs.py) | Python 3.12 x64 | bfs | O(N + M + output) | AC | 0.109 s | 2524 KB |
| [1077_bfs.rs](1077_bfs.rs) | Rust 1.75 x64 | bfs | O(N + M + output) | AC | 0.031 s | 804 KB |
