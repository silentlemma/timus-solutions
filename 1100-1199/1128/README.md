# 1128. Splitting a graph of degree three so that each vertex has at most one neighbour on its side

[Timus 1128](https://acm.timus.ru/problem.aspx?space=1&num=1128) · difficulty 412 · greedy

Original problem by Dmitry Filimonenkov, from the Sixth Ural State University Collegiate Programming Contest, October 21, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N ≤ 7163` children; every child has at most three enemies, and
enmity is mutual. Split the children into two groups so that every child
has at most one enemy in its own group. Print the smaller group (at equal
sizes, the one with child 1): its size, then its children. Print
`NO SOLUTION` if no split exists.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines: the number of enemies of a child, then their numbers.

## Output

The size of the smaller group, then its children separated by spaces, or
`NO SOLUTION`.

## Checking

Any valid split is accepted. The checker verifies the size, that the
listed group is the smaller one (or contains child 1 at equal sizes), and
that every child, listed or not, has at most one enemy on its side.

## Examples

### Example 1

Input:

```
8
3 2 3 7
3 1 3 7
3 1 2 7
1 6
0
2 4 8
3 1 2 3
1 6
```

Output:

```
3
3 6 7
```

## Solution

A split always exists, and a simple local search finds it. Start with
everybody in one group. While some child has two or more enemies in its
own group, move it to the other group: having at most three enemies, it
has at most one on the other side, so the number of enemy pairs that
share a group drops by at least one. That number starts at most at
`3N/2`, so the moves stop after at most that many steps, and when they
stop, every child has at most one enemy on its side. A work list holds the
children to check, and after a move only the moved child and its enemies
are added. `O(N)`.

Pitfalls:

- `NO SOLUTION` is never the answer: degree at most three always allows a
  split;
- the printed group must be the smaller one of the split, and at equal
  sizes the one containing child 1;
- the smaller group may be empty, printed as `0` and an empty line.

The answers were checked by the checker on every test and 60 random
graphs, among them groups of four children who all quarrel.

## Language notes

- All languages run the same work-list search.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1128_greedy.cpp](1128_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.031 s | 500 KB |
| [1128_greedy.go](1128_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.031 s | 2704 KB |
| [1128_greedy.java](1128_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.109 s | 2072 KB |
| [1128_greedy.py](1128_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.109 s | 3948 KB |
| [1128_greedy.rs](1128_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.046 s | 1048 KB |
