# 1076. Sorting trash into containers with the least moving

[Timus 1076](https://acm.timus.ru/problem.aspx?space=1&num=1076) · difficulty 713 · matching

Original problem by Jivko Ganev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N` containers (`1 ≤ N ≤ 150`), and container `i` holds
`a[i][j]` units (`0 ≤ a[i][j] ≤ 100`) of each of `N` types of trash `j`.
Sort the trash so that every type ends up alone in its own container.
Moving one unit between two different containers costs 1. Find the
smallest total cost.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines with `N` amounts each: line `i` describes container
`i`.

## Output

The smallest total cost.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
62 41 86 94
73 58 11 12
69 93 89 88
81 40 69 13
```

Output:

```
650
```

## Solution

In the end every type has its own container, so the final state is a
one-to-one assignment of types to containers. If type `j` goes to
container `i`, the `a[i][j]` units already there stay and all other units
of type `j` move once. So the cost is the total amount minus the sum of
`a[i][j]` over the assigned pairs, and the task is a maximum-weight
perfect matching between containers and types: the assignment problem.

The Hungarian algorithm solves it in `O(N^3)`. This is the version with
potentials `u` for rows and `v` for columns: rows are added one by one,
and for each a shortest augmenting path in reduced costs is grown column
by column, with the potentials moved by the smallest slack `delta` at every
step. With costs `−a[i][j]` the minimum is `−v[0]`, and the answer is the
total plus that minimum.

Pitfalls:

- taking the largest amount first is wrong: with rows `10 9 0`, `9 0 0`
  and `0 0 1` the greedy choice keeps 11 units, the best assignment keeps
  19;
- trying all permutations is out of the question for `N = 150`, and a
  general min-cost flow is slower than needed in Python.

The answers were checked against a min-cost flow with shortest paths by
SPFA, and for `N ≤ 7` against all assignments.

## Language notes

- All five languages implement the same Hungarian algorithm with
  1-based potentials and `owner` and `way` arrays.
- Java reads the matrix with `StreamTokenizer`, which is much faster than
  `Scanner` for 22 500 numbers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1076_matching.cpp](1076_matching.cpp) | G++ 13.2 x64 | matching | O(N^3) | AC | 0.031 s | 252 KB |
| [1076_matching.go](1076_matching.go) | Go 1.14 x64 | matching | O(N^3) | AC | 0.031 s | 1612 KB |
| [1076_matching.java](1076_matching.java) | Java 1.8 | matching | O(N^3) | AC | 0.125 s | 804 KB |
| [1076_matching.py](1076_matching.py) | Python 3.12 x64 | matching | O(N^3) | AC | 0.515 s | 2460 KB |
| [1076_matching.rs](1076_matching.rs) | Rust 1.75 x64 | matching | O(N^3) | AC | 0.046 s | 796 KB |
