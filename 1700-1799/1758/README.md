# 1758. Bald Spot Revisited 2

[Timus 1758](https://acm.timus.ru/problem.aspx?space=1&num=1758) · difficulty 2676 · backtracking

Original problem by Ekaterina Vasilyeva, from the XI USU Open Personal Contest, March 13, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Inns are numbered 1 to n. A walk starts at inn 1 and may go from one
inn to another only if one of their numbers divides the other, never
visiting an inn twice. Find a walk through as many inns as possible.

## Input

n (2 ≤ n ≤ 50).

## Output

The number of inns in the longest walk, then the inns in the order of
the walk. Any longest walk is accepted.

## Examples

### Example 1

Input:

```
9
```

Output:

```
7
1 9 3 6 2 4 8
```

## Solution

This is a longest simple path in the divisibility graph, a hard
problem in general, but there are only 49 inputs. The solutions hold a
table of longest walks, found in advance by an exhaustive search
([1758_backtracking_table.py](1758_backtracking_table.py)), and
print the entry for the largest n' ≤ n where the length grows: a walk
for n' is still a walk for n, and between such points the best length
does not change. The table has 26 entries, and the answer is `O(1)`.

The search extends the walk from its last inn in every possible way
and cuts a branch when even the best case cannot beat the record. The
upper bound counts the free inns reachable from the last inn through free
inns. Among those inns, count the ones with at most one neighbour in the
set of reachable free inns plus the current endpoint. At most one of
these can be visited, and only last, so subtract their count minus one
if there are at least two. The record starts at zero and is updated
whenever a longer prefix is found. The full search proves that nothing
longer exists, but is too slow for the one-second limit, so it is done
in advance.

For n = 9 the walk 1 9 3 6 2 4 8 leaves out 5 and 7: each is joined
only to inn 1, which is taken by the start.

Pitfalls:

- a prime p above n / 2 is joined only to 1, so it can only be the
  second inn and the walk would end there;
- the walk must start at inn 1, though it may end anywhere;
- a greedy walk misses the best length already for small n.
- the pruning bound must count the current endpoint as a neighbour:
  test `gen1` (n = 4) has the optimal walk 1 2 4; counting only free
  neighbours would give an incorrect upper bound of 2 at the start.

The lengths agree with an independent accepted implementation for every
n from 2 to 50, and the checker verifies the walks.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1758_backtracking.cpp](1758_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(1) with a table of 26 walks | AC | 0.015 s | 376 KB |
| [1758_backtracking.go](1758_backtracking.go) | Go 1.14 x64 | backtracking | O(1) with a table of 26 walks | AC | 0.031 s | 1128 KB |
| [1758_backtracking.java](1758_backtracking.java) | Java 1.8 | backtracking | O(1) with a table of 26 walks | AC | 0.140 s | 1752 KB |
| [1758_backtracking.py](1758_backtracking.py) | Python 3.12 x64 | backtracking | O(1) with a table of 26 walks | AC | 0.078 s | 412 KB |
| [1758_backtracking.rs](1758_backtracking.rs) | Rust 1.75 x64 | backtracking | O(1) with a table of 26 walks | AC | 0.062 s | 228 KB |
