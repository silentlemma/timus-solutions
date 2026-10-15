# 1663. The Hobbit or There and Back Again 2

[Timus 1663](https://acm.timus.ru/problem.aspx?space=1&num=1663) · difficulty 3186 · dp

Original problem by Alexander Ipatov, from the Ural SU Contest at the Petrozavodsk Winter Training Camp, January 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tour starts in town 1, visits each of the N towns exactly once and
returns to town 1. Entering town A from town B costs P_A · ⌊1000 / P_B⌋,
where P is the population. Print a cheapest tour, starting from town 1;
any cheapest one is accepted.

## Input

N (2 ≤ N ≤ 1000), then the populations P₁ … P_N (1 ≤ Pᵢ ≤ 1000).

## Output

The N towns in the order of the tour.

## Examples

### Example 1

Input:

```
4
10 3 5 4
```

Output:

```
1 4 2 3
```

## Solution

Write q_B = ⌊1000 / P_B⌋, so a step from B to A costs q_B · P_A. Sort
the towns by population: then P only grows and q only shrinks along the
sorted order. For costs of this product form some cheapest tour is
pyramidal: it climbs from the smallest town to the largest through an
increasing sequence of towns and comes back down through the others.

So each town in the sorted order joins either the climbing path or the
returning one. After the first m towns one of the two paths ends at
town m, and only the end j of the other path matters. up[j] is the
cheapest cost when the climbing path ends at town m, down[j] when the
returning one does. Adding town m + 1 to the path that already ends at
m keeps j and adds the same cost to every entry, so this is kept as one
shared offset per array; adding it to the other path gives the single
new entry for j = m, a minimum over all j. The last town closes both
paths. Each step remembers which j gave the new entries, and walking
back from the best final state assigns every town to a path.
`O(N²)`.

Pitfalls:

- the first town of the tour must be town 1, which is not necessarily
  the smallest, so the found cycle is rotated;
- the tolls are integer divisions, so many towns share a value of q
  (test 06 and the large towns of gen4);
- with two towns there is only one tour.

The pyramidal shape was confirmed by an exhaustive search over all tours
on 400 random inputs with up to 9 towns, and the tour costs match an
independent accepted implementation on 60 random inputs with up to 1000
towns. A checker compares tour costs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1663_dp.cpp](1663_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 268 KB |
| [1663_dp.go](1663_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.031 s | 1284 KB |
| [1663_dp.java](1663_dp.java) | Java 1.8 | dp | O(N^2) | AC | 0.156 s | 2872 KB |
| [1663_dp.py](1663_dp.py) | Python 3.12 x64 | dp | O(N^2) | AC | 0.281 s | 1332 KB |
| [1663_dp.rs](1663_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.046 s | 400 KB |
