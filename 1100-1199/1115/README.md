# 1115. Splitting lengths into rows of given total lengths

[Timus 1115](https://acm.timus.ru/problem.aspx?space=1&num=1115) · difficulty 409 · backtracking

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
solutions search with pruning. Initially, rows are filled shortest first
and items are tried in decreasing length. This is only a heuristic:
shorter rows need not have fewer fillings. The last row takes every item
that remains. Equal lengths are tried only once at each place, since
equal items are interchangeable.

Before filling a row, the bitset `reach[k]` records the sums that the
still-free items from position `k` on can make, built from the end with
`reach[k] = reach[k+1] | reach[k+1] << len`. If any unfinished row's target
is unreachable, the branch fails immediately. An item is taken only if
the rest of the current row is reachable from the items after it.

A fixed search order can still spend too long on incompatible row
fillings. Each of the first 128 attempts allows 256 calls to the subset
search, then unwinds all assignments and permutes the rows and the order
of distinct item lengths. Equal lengths remain together. The permutations
use the same fixed integer generator in every language, so outputs stay
identical. If these attempts fail, a final unrestricted search examines
all remaining possibilities; reaching a budget never means that no split
exists. Output rows retain their original input indices.

With total item length `S` and bitset word width `W`, a conservative
worst-case time bound is `O(M^N * N^2 * ceil(S/W))`, and auxiliary memory
is `O(M * N * ceil(S/W))` words. Restarts do not remove the exponential
worst case; measured speed is not a guarantee for every valid input.

Pitfalls:

- trying equal items in every order makes the search explode on fleets
  with many equal lengths;
- without the subset-sum checks, unreachable current or future rows
  remain in the search;
- test **07** exposes millions of calls with a fixed shortest-first
  order; short rows do not necessarily have the fewest fillings (items
  `[1,1,2,5]`, targets `[2,2,5]` give two fillings for 2 but only one for 5);
- interrupted attempts must undo every assignment, and the final search
  must have no call budget;
- the rows must be printed in input order, though they are filled in a
  different one.

The Python solution was checked on all 7 stored tests, all 5 declared
generator cases, 1,500 small random cases against an independent exact
oracle, and 406 large or boundary cases.

## Language notes

- C++ uses `std::bitset`; Go, Java and Rust keep the sums in arrays of
  64-bit words with a hand-written shift-or; Python uses big integers as
  bitsets.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1115_backtracking.cpp](1115_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 436 KB |
| [1115_backtracking.go](1115_backtracking.go) | Go 1.14 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.031 s | 1904 KB |
| [1115_backtracking.java](1115_backtracking.java) | Java 1.8 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.156 s | 4448 KB |
| [1115_backtracking.py](1115_backtracking.py) | Python 3.12 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.062 s | 732 KB |
| [1115_backtracking.rs](1115_backtracking.rs) | Rust 1.75 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 756 KB |
