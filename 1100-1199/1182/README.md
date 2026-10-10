# 1182. Two teams of mutual acquaintances, as equal as possible

[Timus 1182](https://acm.timus.ru/problem.aspx?space=1&num=1182) · difficulty 512 · graphs

Original problem by Vladimir Kotov and Roman Elizarov, from the ACM ICPC Northeastern European Regional Contest 2001–2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`2 ≤ N ≤ 100` persons each list whom they know; knowing need not be
mutual. Split everyone into two non-empty teams so that in each team
every member knows every other member, with team sizes as close as
possible, or say that no split exists.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then for each person the list of persons they know, ending with 0.

## Output

`No solution`, or two lines, each with a team size and its members.

## Checking

Any split is accepted if both teams are non-empty, cover everyone, are
groups of mutual acquaintances and differ in size as little as possible;
the checker takes the best difference from the stored answer.

## Examples

### Example 1

Input:

```
5
3 4 5 0
1 3 5 0
2 1 4 5 0
2 3 5 0
1 2 3 4 0
```

Output:

```
No solution
```

### Example 2

Input:

```
5
2 3 5 0
1 4 5 3 0
1 2 5 0
1 2 3 0
4 3 2 1 0
```

Output:

```
3 1 3 5
2 2 4
```

## Solution

Call two persons strangers unless each knows the other. Strangers must
be in different teams, so the strangers graph must be bipartite, which a
breadth-first colouring checks; an odd cycle means `No solution`. Each
connected component of that graph has two sides, and its sides must go to
different teams, either way round. Persons in different components know
each other both ways, so any combination of choices is valid.

What remains is a knapsack: `reach[k][s]` says whether the first `k`
components can give the first team exactly `s` persons, and remembers the
side used. Take the reachable `s` closest to `N/2` and walk back to
collect the teams. `O(N²)`.

Pitfalls:

- knowing is one-way in the input, so a pair counts as acquainted only if
  both list each other;
- a component of one person can join either team, which is what lets the
  sizes even out;
- both teams are automatically non-empty: a component with strangers has
  both sides non-empty, and single persons are spread by the knapsack.

The answers were compared with a separately written solution on 300
random groups of up to 41 persons, twelve of them without a solution, and
every printed split passed the checker.

## Language notes

- All languages colour the strangers graph straight from the
  acquaintance matrix and run the same knapsack.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1182_graphs.cpp](1182_graphs.cpp) | G++ 13.2 x64 | graphs | O(N²) | AC | 0.015 s | 280 KB |
| [1182_graphs.go](1182_graphs.go) | Go 1.14 x64 | graphs | O(N²) | AC | 0.031 s | 1400 KB |
| [1182_graphs.java](1182_graphs.java) | Java 1.8 | graphs | O(N²) | AC | 0.171 s | 5732 KB |
| [1182_graphs.py](1182_graphs.py) | Python 3.12 x64 | graphs | O(N²) | AC | 0.078 s | 1332 KB |
| [1182_graphs.rs](1182_graphs.rs) | Rust 1.75 x64 | graphs | O(N²) | AC | 0.046 s | 384 KB |
