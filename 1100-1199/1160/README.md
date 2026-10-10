# 1160. Connecting all hubs so that the longest cable is as short as possible

[Timus 1160](https://acm.timus.ru/problem.aspx?space=1&num=1160) · difficulty 146 · dsu

Original problem by Andrew Stankevich, from the Northern Subregion of the ACM ICPC Northeastern European Regional Contest 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 1000` hubs can be joined by `M ≤ 15000` possible cables of given
lengths. Choose cables that connect every hub to every other, directly or
through others, so that the longest chosen cable is as short as possible.
Print that length, then the number of cables and the cables themselves.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `M`, then `M` lines with two hubs and a length.

## Output

The longest cable, the number of cables `P`, then `P` pairs of hubs.

## Checking

Any plan is accepted if it connects all hubs with possible cables and its
longest cable is the smallest possible. The checker finds that smallest
length on its own, by binary search over the lengths with a connectivity
test, and verifies the printed length and plan.

## Examples

### Example 1

Input:

```
4 6
1 2 1
1 3 1
1 4 2
2 3 1
3 4 1
2 4 1
```

Output:

```
1
3
1 2
1 3
3 4
```

## Solution

Kruskal's algorithm builds a spanning tree from the shortest cables up,
skipping a cable whose ends are already connected, with a disjoint-set
union to tell. The tree it builds is a minimum spanning tree, and a
minimum spanning tree also minimises its longest edge: when Kruskal's
algorithm adds its last, longest edge `e`, the cables shorter than `e`
leave the hubs in at least two separate groups, so every connecting plan
needs a cable at least as long as `e`. The answer is the length of the last
edge taken, and the tree's `N − 1` cables are a valid plan.
`O(M log M)`.

Pitfalls:

- the plan does not have to be a tree, and any plan with the smallest
  longest cable is accepted;
- every hub must be reached, so the last edge Kruskal takes, not the last
  one considered, gives the answer;
- equal lengths need no special care.

The answers were checked by the checker on every test and on 60 random
networks.

## Language notes

- All languages sort the cables and run the same union with path
  halving.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1160_dsu.cpp](1160_dsu.cpp) | G++ 13.2 x64 | dsu | O(M log M) | AC | 0.031 s | 436 KB |
| [1160_dsu.go](1160_dsu.go) | Go 1.14 x64 | dsu | O(M log M) | AC | 0.046 s | 1448 KB |
| [1160_dsu.java](1160_dsu.java) | Java 1.8 | dsu | O(M log M) | AC | 0.171 s | 3500 KB |
| [1160_dsu.py](1160_dsu.py) | Python 3.12 x64 | dsu | O(M log M) | AC | 0.078 s | 5864 KB |
| [1160_dsu.rs](1160_dsu.rs) | Rust 1.75 x64 | dsu | O(M log M) | AC | 0.015 s | 1104 KB |
