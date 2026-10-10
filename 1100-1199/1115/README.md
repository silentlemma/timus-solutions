# 1115. Splitting lengths into rows of given total lengths

[Timus 1115](https://acm.timus.ru/problem.aspx?space=1&num=1115) · difficulty 415 · backtracking

Original problem from the first selection contest for the Bulgarian IOI team.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N < 100` items with integer lengths from 1 to 100 and
`M` rows (`1 < M < 10`) with given lengths. Split all items into the rows
so that the lengths in every row add up exactly to the row length; every
row gets at least one item. A split is known to exist. Print one.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N M`, then `N` lines with the item lengths, then `M` lines with the row
lengths.

## Output

For every row, in input order, two lines: the number of items in it and
their lengths.

## Checking

Any valid split is accepted. The checker verifies that every row adds up
to its length and that the items used are exactly the given ones.

## Examples

### Example 1

Input:

```
5 2
4
10
2
5
3
11
13
```

Output:

```
3
5 4 2
2
10 3
```

## Solution

This is exact multi-way partitioning, a hard problem in general, so the
solutions search with strong pruning. Rows are filled one at a time, the
shortest first, since short rows have the fewest fillings; the last row
simply takes every item that is left. Within a row, the items are tried in
decreasing length, and equal lengths are tried only once at each place,
since equal items are interchangeable.

The key pruning is a subset-sum table. Before filling a row, a bitset
`reach[k]` records which sums the still-free items from position `k` on
can make, built from the end with
`reach[k] = reach[k+1] | reach[k+1] << len`. An item is taken only if
the rest of the row can still be completed from the items after it, so a
row is never filled into a dead end; only the interplay between rows can
force backtracking. On random fleets, and on
fleets of nearly equal lengths where many partial fillings exist, every
case finishes far below the time limit.

Pitfalls:

- trying equal items in every order makes the search explode on fleets
  with many equal lengths;
- without the subset-sum check a row is explored even when its remainder
  can no longer be reached;
- the rows must be printed in input order, though they are filled in a
  different one.

The answers were checked by the checker on every test and on 120 random
fleets of up to 99 items in up to 9 rows, including nearly equal and
mostly equal lengths.

## Language notes

- C++ uses `std::bitset`; Go, Java and Rust keep the sums in arrays of
  64-bit words with a hand-written shift-or; Python uses big integers as
  bitsets.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1115_backtracking.cpp](1115_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(2^N) worst case | AC | 0.015 s | 440 KB |
| [1115_backtracking.go](1115_backtracking.go) | Go 1.14 x64 | backtracking | O(2^N) worst case | AC | 0.015 s | 1872 KB |
| [1115_backtracking.java](1115_backtracking.java) | Java 1.8 | backtracking | O(2^N) worst case | AC | 0.140 s | 4508 KB |
| [1115_backtracking.py](1115_backtracking.py) | Python 3.12 x64 | backtracking | O(2^N) worst case | AC | 0.078 s | 684 KB |
| [1115_backtracking.rs](1115_backtracking.rs) | Rust 1.75 x64 | backtracking | O(2^N) worst case | AC | 0.015 s | 748 KB |
