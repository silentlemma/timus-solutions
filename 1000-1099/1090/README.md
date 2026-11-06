# 1090. The row of recruits that jumps the most: counting inversions

[Timus 1090](https://acm.timus.ru/problem.aspx?space=1&num=1090) · difficulty 366 · fenwick, binary_search

Original problem by Nikita Shamgunov, from the USU Open Collegiate Programming Contest, March 2001, Senior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `K` rows (`1 ≤ K ≤ 20`) of `N` recruits each (`2 ≤ N ≤ 10000`),
numbered by height from 1 (tallest) to `N`; each row is a permutation of
`1 … N`. Every recruit jumps once for each recruit standing before them
in the row with a larger number. Print the row with the most jumps in
total, the smallest such row on ties.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N` and `K`, then `K` lines with `N` numbers each.

## Output

The number of the row.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3 3
1 2 3
2 1 3
3 2 1
```

Output:

```
3
```

## Solution

The total number of jumps in a row is the number of inversions of the
permutation: pairs of positions `i < j` with `a[i] > a[j]`. For `N = 10000`
the double loop is too slow, so count them while reading the row.
Before recruit `x` at position `i` there are `i` recruits, and the number
of those with a smaller number is a prefix count in a Fenwick tree over
the numbers `1 … N`; the jumps of `x` are `i` minus that count. Then add
`x` to the tree. `O(K · N log N)`.

Pitfalls:

- the total of a row reaches `N(N − 1)/2 ≈ 5 · 10^7`; it fits 32 bits, but
  the Fenwick solutions add in 64 bits;
- on ties the first row wins, so only a strictly larger total replaces
  the best one;
- the tree must be cleared for every row.

The answers were checked against inversion counts by merge sort, and for
`N ≤ 300` also by the double loop.

## Optimized solutions

The C++ and Go versions keep the Fenwick algorithm and parse input through a fixed-size buffer. Each tree cell stores at most N counts and fits in 16 bits. The PyPy version uses a Fenwick tree in place of the sorted list, so each prefix query and insertion takes O(log N). All three versions take O(K·N log N) time and O(N) extra space.

The accepted base implementations [1090_fenwick.java](1090_fenwick.java), [1090_fenwick.rs](1090_fenwick.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The teaching Python version uses a sorted list with binary search and was accepted under PyPy 3.10. The same source under CPython 3.12 exceeded the time limit on test 9 (0.515 s). The optimized Python version uses a Fenwick tree and was also accepted under PyPy 3.10. The table records the actual interpreter of each Accepted submission.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1090_binary_search.py](1090_binary_search.py) | PyPy 3.10 x64 | binary_search | O(K·N^2) | AC | 0.437 s | 20044 KB | 11279088 |
| [1090_fenwick.cpp](1090_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(K·N log N) | AC | 0.156 s | 236 KB | 11279084 |
| [1090_fenwick.go](1090_fenwick.go) | Go 1.14 x64 | fenwick | O(K·N log N) | AC | 0.046 s | 1916 KB | 11279085 |
| [1090_fenwick.java](1090_fenwick.java) \* | Java 1.8 | fenwick | O(K·N log N) | AC | 0.125 s | 512 KB | 11279089 |
| [1090_fenwick.rs](1090_fenwick.rs) \* | Rust 1.75 x64 | fenwick | O(K·N log N) | AC | 0.015 s | 2120 KB | 11279090 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1090_fenwick_optimized.cpp](1090_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(K·N log N) | AC | 0.015 s | 104 KB | 11310324 |
| [1090_fenwick_optimized.go](1090_fenwick_optimized.go) \* | Go 1.14 x64 | fenwick | O(K·N log N) | AC | 0.031 s | 816 KB | 11310344 |
| [1090_fenwick.py](1090_fenwick.py) \* | PyPy 3.10 x64 | fenwick | O(K·N log N) | AC | 0.156 s | 9076 KB | 11310319 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
