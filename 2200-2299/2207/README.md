# 2207. The smallest Manhattan reach that fills the most jobs

[Timus 2207](https://acm.timus.ru/problem.aspx?space=1&num=2207) · difficulty 1280 · geometry, dsu

Original problem by Ivan Kogut, from the University Academic School Olympiad in Informatics 2022.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n houses hold aᵢ people and m farms offer bⱼ jobs, all at distinct grid
cells. With reach D, a person may move between a house and a farm at
Manhattan distance at most D, any number of times, but never directly
between two houses or two farms. Find the largest number of filled jobs
and the smallest D that achieves it. The limits are 2 seconds and
256 MB.

## Input

W and H, 1 ≤ W, H ≤ 10⁹, then n and m, 1 ≤ n, m ≤ 10⁴, then the n houses
followed by the m farms as x y count, with 1 ≤ x ≤ W, 1 ≤ y ≤ H and
1 ≤ count ≤ 10⁹. All values are integers.

## Output

The best score and the smallest reach.

## Examples

### Example 1

Input:

```
11 11
4 4
1 1 2
7 1 1
1 11 2
11 11 1
4 4 1
10 4 2
4 11 1
8 11 2
```

Output:

```
6 7
```

## Solution

For a fixed D, people move freely inside each connected component of
the bipartite graph between houses and farms, so a component fills
min(people, jobs) jobs. Once D connects everything the score is
min(Σa, Σb), the best possible, and the task is the smallest D whose
components reach that total.

The components for every D are those of the minimum spanning forest of
the house–farm graph with Manhattan weights, so the edges of a minimum
spanning tree are added in increasing order with a disjoint set union
that tracks people and jobs per component, and the answer is the weight
of the edge at which the score first reaches min(Σa, Σb).

The spanning tree is built by Borůvka's algorithm. In each round every
component needs its cheapest edge to a point of the other kind in
another component. For Manhattan distance this splits into four sign
quadrants: in the quadrant where the partner has x' ≤ x and y' ≤ y, the
distance is (x + y) − (x' + y'), so a sweep in x order with a Fenwick
tree over y asks for the largest x' + y' of the other kind. Each
Fenwick node keeps the best two values from different components, so
the best partner outside the own component is always available. There
are O(log N) rounds of O(N log N) work each.

In the example there are 6 people and 6 jobs, and reach 7 is the first
that lets all of them work.

This takes O(N log² N) for N = n + m.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2207_geometry_dsu.cpp](2207_geometry_dsu.cpp) | G++ 13.2 x64 | geometry, dsu | O(N log² N) | AC | 0.140 s | 3032 KB |
| [2207_geometry_dsu.go](2207_geometry_dsu.go) | Go 1.14 x64 | geometry, dsu | O(N log² N) | AC | 0.218 s | 12280 KB |
| [2207_geometry_dsu.java](2207_geometry_dsu.java) | Java 1.8 | geometry, dsu | O(N log² N) | AC | 0.453 s | 11112 KB |
| [2207_geometry_dsu.py](2207_geometry_dsu.py) | PyPy 3.10 x64 | geometry, dsu | O(N log² N) | AC | 1.390 s | 34872 KB |
| [2207_geometry_dsu.rs](2207_geometry_dsu.rs) | Rust 1.75 x64 | geometry, dsu | O(N log² N) | AC | 0.140 s | 5568 KB |
