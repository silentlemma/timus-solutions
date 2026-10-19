# 1847. Zamkadye

[Timus 1847](https://acm.timus.ru/problem.aspx?space=1&num=1847) · difficulty 3793 · dp

Original problem by Alexander Ipatov, from the Ural SU Contest at the Petrozavodsk summer session, August 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n cities on a plane are joined by n − 1 straight roads of the least
total length. A king started at city 1 and travelled depth-first: from
the current city he went along any road to a city he had not seen yet,
and when there was none he went back the way he had first come; every
new city went into his diary. His son flies straight between cities and
visits them in the diary's order, then returns to city 1. The order in
which the king chose roads is unknown: find the shortest possible
flight.

## Input

n (2 ≤ n ≤ 1000), the coordinates of the n cities (integers of absolute
value at most 10 000, all points distinct), an empty line and the n − 1
roads as pairs of cities.

## Output

The shortest flight, with relative error at most 10⁻⁹.

## Examples

### Example 1

Input:

```
4
0 0
1 0
1 1
0 1

1 2
1 4
4 3
```

Output:

```
4.000
```

## Solution

The diary is a preorder of the tree rooted at city 1, with the children
of every city taken in any order. The flight through a subtree starts
at its root and, since every child's subtree is finished before the next
child begins, ends at one of its leaves. So for every city u and every
leaf e below it let cost(u, e) be the shortest flight through the
subtree of u that ends at e.

Inside u the children are flown in some order. Entering child b right
after child a has finished costs link(a, b) = min over leaves e of a of
cost(a, e) + |e b|, which does not depend on what came before. Hence
the order of the children is a shortest-path problem over subsets:
enter(m, b) is the cheapest way to enter b after finishing the other
children in the set m, starting from enter({b}, b) = |u b| and growing by
enter(m, a) + link(a, b). Then cost(u, e) = enter(all, b) + cost(b, e)
for a leaf e of child b, and the answer is the least cost(1, e) + |e 1|.

The roads form a minimum spanning tree of points in the plane, where two
edges at a city make an angle of at least 60°, so a city has at most six
neighbours and the subset step costs at most 2⁶·6² per city. Computing
the links touches every leaf below a city at most six times, and a leaf
lies below at most n cities, so this part is `O(n²)`. The cities are
processed children first, in reverse breadth-first order, to avoid deep
recursion.

In the example the tree is 1 – 2 and 1 – 4 – 3. Visiting 2 first gives
1, 2, 4, 3 and a flight of 1 + √2 + 1 + √2; visiting 4 first gives 1,
4, 3, 2 and four unit steps, 4.

Pitfalls:

- a subtree's flight always starts at its root, which is what makes
  link(a, b) independent of the rest of the order;
- the degree bound comes from the tree being minimal; an arbitrary tree
  would make the subset step exponential.

The answers agree with an independent accepted implementation on sixty
random sets of up to 1000 cities, including grids with many equal
roads, long spines and nested five-armed stars.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1847_dp.cpp](1847_dp.cpp) | G++ 13.2 x64 | dp | O(n^2) | AC | 0.015 s | 596 KB |
| [1847_dp.go](1847_dp.go) | Go 1.14 x64 | dp | O(n^2) | AC | 0.031 s | 2312 KB |
| [1847_dp.java](1847_dp.java) | Java 1.8 | dp | O(n^2) | AC | 0.156 s | 2764 KB |
| [1847_dp.py](1847_dp.py) | Python 3.12 x64 | dp | O(n^2) | AC | 0.109 s | 1196 KB |
| [1847_dp.rs](1847_dp.rs) | Rust 1.75 x64 | dp | O(n^2) | AC | 0.046 s | 532 KB |
