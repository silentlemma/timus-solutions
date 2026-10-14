# 1584. Pharaohs’ Secrets

[Timus 1584](https://acm.timus.ru/problem.aspx?space=1&num=1584) · difficulty 1326 · matching

Original problem by Alex Gevak, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Statues stand in an n × m grid (n and m even, up to 20), each a letter
naming its kind, fewer than 30 kinds. Rearrange them so that every row
and every column reads the same from both ends, carrying as few statues
as possible from place to place, and print that number. An arrangement
is always possible.

Time limit: 1 second. Memory limit: 64 MB.

## Input

n and m, then n lines of m letters.

## Output

The least number of carries.

## Examples

### Example 1

Input:

```
4 4
abxa
xyyb
xyyx
abba
```

Output:

```
2
```

## Solution

Symmetric rows and columns mean that the four mirror images of a cell,
(i, j), (i, m−1−j), (n−1−i, j) and (n−1−i, m−1−j), hold one kind. So
the grid splits into nm/4 groups of four cells, each to be filled with
one kind, and a kind with c statues fills exactly c/4 groups.

A statue already standing where its kind will be stays; every other
statue is carried at least once, and carrying them round each cycle of
the permutation takes exactly that many carries (a swap takes two, as
in the example). So the answer is the number of cells whose kind
changes. Giving kind k to a group costs 4 minus the statues of kind k
already there, and the best choice is an assignment problem: one column
per place of each kind (c/4 columns for kind k), one row per group,
solved by the Hungarian method in O(G³) for G = nm/4 ≤ 100 groups. The
results were checked against trying every assignment on 200 random
small grids.

Pitfalls:

- the carries count statues, not swaps: one swap is two carries (the
  example);
- a group may hold two kinds two by two, and then two statues change
  if it gets either of those kinds (test 03);
- a greedy choice per group can block a better match elsewhere, so the
  groups need a real assignment.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1584_matching.cpp](1584_matching.cpp) | G++ 13.2 x64 | matching | O((n m)^3) | AC | 0.031 s | 468 KB |
| [1584_matching.go](1584_matching.go) | Go 1.14 x64 | matching | O((n m)^3) | AC | 0.031 s | 1344 KB |
| [1584_matching.java](1584_matching.java) | Java 1.8 | matching | O((n m)^3) | AC | 0.156 s | 1784 KB |
| [1584_matching.py](1584_matching.py) | Python 3.12 x64 | matching | O((n m)^3) | AC | 0.171 s | 804 KB |
| [1584_matching.rs](1584_matching.rs) | Rust 1.75 x64 | matching | O((n m)^3) | AC | 0.031 s | 288 KB |
