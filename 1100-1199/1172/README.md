# 1172. Counting round trips through three islands by ship only

[Timus 1172](https://acm.timus.ru/problem.aspx?space=1&num=1172) · difficulty 549 · combinatorics

Original problem by Mugurel Ionut Andreica, from the Romanian Open Contest, December 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three islands have `N ≤ 30` cities each. Ships connect every two cities
on different islands, and there is no travel within an island. Starting
from a given city, count the round trips that visit every other city
exactly once and return; a trip and the same trip read backwards count
once.

Time limit: 1 second. Memory limit: 16 MB.

## Input

`N`.

## Output

The number of trips, which has dozens of digits for large `N`.

## Examples

### Example 1

Input:

```
2
```

Output:

```
16
```

## Solution

Split a trip into its pattern of islands and the choice of cities. The
pattern is a cyclic sequence of `3N` island labels, starting with the
tourist's island, with `N` of each label and no two neighbours equal,
including the last and the first. For a fixed pattern, the other `N − 1`
cities of the home island fill its slots in `(N − 1)!` ways and each other
island in `N!` ways. Reading a trip backwards gives a different sequence
from the same start (the trip has at least three cities), so the total is
halved.

Patterns are counted with `ways[a][b][c][i]`: sequences that start on
island 0, use `a`, `b` and `c` slots of the three islands and end on island
`i`. Each value is the sum of two values for one fewer slot of island `i`,
ending elsewhere. The answer counts the full sequences that do not end on
island 0. Only two planes of fixed `a` are kept, which keeps the big
numbers few. `O(N³)` big-number additions.

Pitfalls:

- the cycle also forbids the last city being on the home island;
- the starting city is fixed, so the home island contributes `(N − 1)!`,
  not `N!`;
- the full table for `N = 30` would hold about 90,000 big numbers, while
  two planes need only about 6,000.

The answers were compared with a brute force over all orders for
`N ≤ 3` and with a separately written solution for every `N` up to 30.

## Language notes

- Python, Go and Java use their big integers; C++ and Rust keep numbers
  as arrays of base-10⁹ digits with addition, multiplication by a small
  number and halving.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1172_combinatorics.cpp](1172_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N³) big additions | AC | 0.015 s | 376 KB |
| [1172_combinatorics.go](1172_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N³) big additions | AC | 0.015 s | 6024 KB |
| [1172_combinatorics.java](1172_combinatorics.java) | Java 1.8 | combinatorics | O(N³) big additions | AC | 0.125 s | 4580 KB |
| [1172_combinatorics.py](1172_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N³) big additions | AC | 0.093 s | 884 KB |
| [1172_combinatorics.rs](1172_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N³) big additions | AC | 0.031 s | 568 KB |
