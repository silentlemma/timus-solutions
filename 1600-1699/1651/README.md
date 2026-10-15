# 1651. Shortest Subchain

[Timus 1651](https://acm.timus.ru/problem.aspx?space=1&num=1651) · difficulty 346 · dp

Original problem by Vladimir Yakovlev (idea by Magaz Asanov), from the NEERC 2008 Eastern Subregional Quarterfinal.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A walk p in a directed graph is given by its list of n vertices. Find a
walk q from the same first vertex to the same last vertex whose edges
are edges of p taken in the same order, with as few edges as possible.

## Input

n (2 ≤ n ≤ 100000), then n vertex numbers from 1 to 10000; no two
neighbouring numbers are equal.

## Output

The vertices of q separated by spaces; q may be a single vertex.

## Examples

### Example 1

Input:

```
9
1 2 7 3 2
8 4 8 5
```

Output:

```
1 2 8 5
```

## Solution

Position i of the list stands for "at vertex pᵢ, free to use edges of p
from the i-th on". From there q may take any later edge that starts at
pᵢ, that is an edge (pⱼ, pⱼ₊₁) with j ≥ i and pⱼ = pᵢ, and continue
from position j + 1. Arriving at the last vertex anywhere ends q, since
going on can only add edges.

So dp[i] = 0 when pᵢ is the last vertex, and otherwise
dp[i] = 1 + min dp[j + 1] over j ≥ i with pⱼ = pᵢ. Going from right to
left, a table indexed by vertex keeps that minimum for the suffix, so
each position costs O(1); remembering the chosen j rebuilds q from
position 0. When the first and last vertices coincide, q is that single
vertex. `O(n)`.

Among equally short walks the program keeps the latest jump for a
vertex. This makes all five solutions deterministic; any optimal walk
is valid. The checker verifies the endpoints, the edge order, and the
minimum length, computed independently by scanning edges left to right.

Pitfalls:

- a closed walk shrinks to its single vertex (test 03);
- different optimal vertex lists must all be accepted (test gen3);
- q may pass through the last vertex only at its end, so stopping at
  the first arrival is right;
- the jump target is the position after the chosen edge, j + 1, not j.

The Python solution and checker agree with exhaustive edge-subset
enumeration on 2000 random small walks and 1155 exhaustive cases.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1651_dp.cpp](1651_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.062 s | 1448 KB |
| [1651_dp.go](1651_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.078 s | 4176 KB |
| [1651_dp.java](1651_dp.java) | Java 1.8 | dp | O(n) | AC | 0.125 s | 2188 KB |
| [1651_dp.py](1651_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.156 s | 16708 KB |
| [1651_dp.rs](1651_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.031 s | 3840 KB |
