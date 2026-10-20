# 2199. Two days in a range whose changes sum closest to zero

[Timus 2199](https://acm.timus.ru/problem.aspx?space=1&num=2199) · difficulty 1123 · sqrt_decomposition, sorting

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An array d of N integers gets Q range queries [l, r]: report two
different positions i, j in the range with the smallest |dᵢ + dⱼ|, any
of them if several are best. The limits are 3 seconds and 256 MB.

## Input

N and Q, 2 ≤ N ≤ 30 000, 1 ≤ Q ≤ 30 000, then d with |dᵢ| ≤ 10⁹, then queries with 1 ≤ l < r ≤ N.

## Output

Two positions for each query.

## Examples

### Example 1

Input:

```
6 4
17 11 -1 -4 20 -24
1 2
3 4
2 3
1 6
```

Output:

```
1 2
3 4
2 3
5 6
```

## Solution

Order the elements by absolute value. At least one optimal pair is
adjacent in this order. Indeed, take a, c, b with |a| ≤ |c| ≤ |b|.
If a and b have the same sign, (a, c) is no worse than (a, b).
Otherwise, if c has b's sign, (a, c) is no worse; if c has a's sign,
(c, b) is no worse. Zero can take either sign. Repeating this replacement
gives an adjacent optimal pair, so insertions only need the predecessor
and successor in this order.

The queries are answered offline, grouped by the block of their left
end. Inside a block of B days, queries are sorted by right end. The core
to the right of the block only grows. C++, Java and Rust keep occupied
absolute-value ranks in ordered sets; Go uses a Fenwick tree of rank
counts with order-statistic searches. Each search or update costs O(log N).
For a query crossing the block boundary, combine the core's best pair,
the precomputed best pair in the block suffix, and cross pairs found by
searching the core's neighboring ranks for each suffix element. The suffix
is not inserted into the core. Queries wholly inside the block use a
temporary set, cleared after each query.

The compiled versions use two bounds. A prefix table finds a pair
attaining the whole array's minimum score whenever one lies in the
query. Also, an element whose best possible partner in the whole array
cannot improve the current answer can be skipped. These bounds improve
practical performance but do not change the worst-case bound.

Python uses the same block decomposition with different preprocessing,
without those two pruning shortcuts. Inserting elements into the order
by absolute value is deleting them from the full order in reverse. A
linked list therefore records each element's neighbors at insertion,
both for the growing core and for block suffixes. Queries wholly inside
the block scan its absolute-value order, filtering by their endpoints.
For cross pairs, each fringe value x needs the core value nearest to −x.
Reverse deletion in numeric order gives the interval of reflected values
for which a newly inserted core value becomes strictly nearer; midpoint
ties keep the earlier partner. Binary searches locate this interval among
the reflected fringe values. Assignments are applied in arrival order to
a tree over groups of 16 fringe elements, with individual updates at the
edges. The latest timestamp wins, and each query reads its suffix partners.

In the example the whole array gives |20 − 24| = 4 at days 5 and 6.

With 1 ≤ B ≤ N and B about N / √Q, the compiled versions take
O(N log N + Q log Q + (N²/B + QB) log N) time. Python takes
O(N log N + Q log Q + (N²/B) log(B+1) + QB) time. All five use O(N + Q)
auxiliary space. The table uses B for the block length.

Pitfalls: Q may be 1 (tests 02–04); these valid tests need no replacement.
Adjacency refers to absolute-value order, not dates (test 06), and only
one optimal pair must be adjacent. Ordered-set and Fenwick operations
have logarithmic cost, rather than constant-time bitset operations.

## Language notes

- The table records historical PyPy 3.10 results. Performance under
  CPython depends on the runtime and hardware; those timings are not a
  guarantee for CPython or a mapping to local test numbers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2199_sqrt_decomposition_sorting.cpp](2199_sqrt_decomposition_sorting.cpp) | G++ 13.2 x64 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B + QB) log N) | AC | 0.656 s | 3472 KB |
| [2199_sqrt_decomposition_sorting.go](2199_sqrt_decomposition_sorting.go) | Go 1.14 x64 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B + QB) log N) | AC | 1.234 s | 12004 KB |
| [2199_sqrt_decomposition_sorting.java](2199_sqrt_decomposition_sorting.java) | Java 1.8 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B + QB) log N) | AC | 1.812 s | 11324 KB |
| [2199_sqrt_decomposition_sorting.py](2199_sqrt_decomposition_sorting.py) | PyPy 3.10 x64 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B) log(B+1) + QB) | AC | 1.125 s | 17704 KB |
| [2199_sqrt_decomposition_sorting.rs](2199_sqrt_decomposition_sorting.rs) | Rust 1.75 x64 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B + QB) log N) | AC | 0.703 s | 7536 KB |
