# 1781. Clean Code

[Timus 1781](https://acm.timus.ru/problem.aspx?space=1&num=1781) · difficulty 2024 · graphs

Original problem by Alex Samsonov, from the XV Open USU Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An n × n table of zeros and ones says which rooms each of n contests
uses, the contests held in order. Room i is cleaned right after contest
i and cannot be used afterwards, so contest i may not use any room j
with j < i. One operation swaps rows i and j and then columns i and j.
With at most 200 operations, make the table fit, or report that it is
impossible.

## Input

n (2 ≤ n ≤ 100), then the table.

## Output

The number of operations and the pairs i, j, or −1. Any fitting answer
is accepted.

## Examples

### Example 1

Input:

```
3
0 0 0
1 1 0
1 1 0
```

Output:

```
1
1 3
```

### Example 2

Input:

```
3
1 1 1
1 1 0
1 0 0
```

Output:

```
-1
```

## Solution

Swapping rows and columns together only renumbers the contests and
their rooms alike, and any renumbering can be reached. The table fits
when every 1 off the diagonal lies above it, that is, a contest a that
uses room b ≠ a comes before contest b. These are edges a → b of a
graph, and a fitting numbering is a topological order of it; if the
graph has a cycle, nothing works and the answer is −1.

The order is reached by putting its contests into places 1, 2, … one at
a time, each with at most one swap of the contest now in that place and
the wanted one, so at most n − 1 ≤ 99 operations are used. `O(n²)`.

In the first example contests 2 and 3 use room 1, so contest 1 must
come after both; swapping 1 and 3 puts it last.

Pitfalls:

- a contest may use its own room, and those diagonal 1s set no order;
- each operation swaps rows and columns alike, so it is a renumbering,
  not a free move of rows;
- the answer is not unique, so the checker replays the swaps.

Whether an answer exists agrees with a search over every renumbering on
300 random tables of up to 5 rooms, and the swaps pass the checker on
100 random tables of up to 100 rooms, as do those of an independent
accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1781_graphs.cpp](1781_graphs.cpp) | G++ 13.2 x64 | graphs | O(n^2) | AC | 0.015 s | 256 KB |
| [1781_graphs.go](1781_graphs.go) | Go 1.14 x64 | graphs | O(n^2) | AC | 0.031 s | 1204 KB |
| [1781_graphs.java](1781_graphs.java) | Java 1.8 | graphs | O(n^2) | AC | 0.171 s | 5700 KB |
| [1781_graphs.py](1781_graphs.py) | Python 3.12 x64 | graphs | O(n^2) | AC | 0.078 s | 968 KB |
| [1781_graphs.rs](1781_graphs.rs) | Rust 1.75 x64 | graphs | O(n^2) | AC | 0.015 s | 304 KB |
