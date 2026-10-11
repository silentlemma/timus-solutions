# 1227. A rally route of a given length on one-way roads

[Timus 1227](https://acm.timus.ru/problem.aspx?space=1&num=1227) · difficulty 301 · graphs

Original problem from the Central Russia regional quarterfinal of the ACM ICPC 2002–2003, Rybinsk, October 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `M ≤ 100` cities and `N ≤ 10⁴` two-way roads of given lengths.
For safety every road on the rally route is driven in one direction only,
and the route may start and end anywhere along a road. Decide whether a
route of length exactly `S ≤ 2·10⁶` exists.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`M`, `N` and `S`, then each road as two cities and a length.

## Output

`YES` or `NO`.

## Examples

### Example 1

Input:

```
3 2 20
1 2 10
2 3 5
```

Output:

```
NO
```

### Example 2

Input:

```
3 3 1000
1 2 1
2 3 1
1 3 1
```

Output:

```
YES
```

## Solution

If the roads contain a cycle, the route can go round it again and again
in the same direction, so any length is possible. A loop from a city to
itself, or a second road between the same two cities, is such a cycle
too. Union–find spots the first road whose ends are already connected.

Otherwise the roads form a forest. Driving a road in one direction only
means the route can never turn back, so it follows a simple path, and
because it may start and stop in the middle of a road, every length up to
the longest path is reachable. The longest path of a tree is its
diameter: from any city go to the farthest one, and from there to the
farthest again. The answer is `YES` exactly when some tree's diameter is
at least `S`. `O(N α(M) + M)`.

Pitfalls:

- a road from a city to itself counts as a cycle;
- two roads between the same pair of cities also allow driving round
  forever;
- the forest may have several trees, and each needs its own diameter;
- a route exactly as long as the diameter is allowed.

The answers were compared with a separately written solution on 200
random maps with and without cycles, with `S` around the diameter.

## Language notes

- All languages use union–find with path halving and an explicit stack
  for the distances.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1227_graphs.cpp](1227_graphs.cpp) | G++ 13.2 x64 | graphs | O(N α(M) + M) | AC | 0.015 s | 204 KB |
| [1227_graphs.go](1227_graphs.go) | Go 1.14 x64 | graphs | O(N α(M) + M) | AC | 0.031 s | 1268 KB |
| [1227_graphs.java](1227_graphs.java) | Java 1.8 | graphs | O(N α(M) + M) | AC | 0.093 s | 800 KB |
| [1227_graphs.py](1227_graphs.py) | Python 3.12 x64 | graphs | O(N α(M) + M) | AC | 0.078 s | 2608 KB |
| [1227_graphs.rs](1227_graphs.rs) | Rust 1.75 x64 | graphs | O(N α(M) + M) | AC | 0.015 s | 464 KB |
