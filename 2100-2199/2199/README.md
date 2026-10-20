# 2199. Two days in a range whose changes sum closest to zero

[Timus 2199](https://acm.timus.ru/problem.aspx?space=1&num=2199) · difficulty 1265 · sqrt_decomposition, sorting

Original problem by Vadim Barinov, from the ICPC Ural Regional Contest qualifier 2024.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An array d of N integers gets Q range queries [l, r]: report two
different positions i, j in the range with the smallest |dᵢ + dⱼ|, any
of them if several are best. The limits are 3 seconds and 256 MB.

## Input

N and Q, 2 ≤ N, Q ≤ 30 000, then d with |dᵢ| ≤ 10⁹, then the queries.

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

Order the elements by absolute value. The best pair of any set is two
neighbors in this order: for two elements a and b with |a| ≤ |c| ≤ |b|
for some element c between them, if c has the sign of b, the pair
(a, c) is no worse, and if it has the sign of a, the pair (c, b) is no
worse. So a set only
needs, for each element, its predecessor and successor in that order.

The queries are answered offline, grouped by the block of their left
end, in the style of Mo's algorithm without deletions. Inside a block,
the queries are sorted by right end, and the part of the range right of
the block only grows, keeping its elements in a bitset over the
absolute-value ranks, so a new element finds its two neighbors by bit
operations and updates the best pair. The few days between the left end
and the block boundary are added on top of that for each query and
dropped again, their own pairs having been prepared once per block.

Two cheap bounds cut most of the work. The smallest |dᵢ + dⱼ| over the
whole array is known in advance, and a query that contains a pair
reaching it is answered at once from a prefix table. And an element
whose best partner in the whole array cannot beat the current answer
never needs to be inserted.

The Python version avoids the bitset searches. Inserting elements one
by one into the order by absolute value is deleting them from the full
order in reverse, so a linked list over that order, deleted backwards,
gives every element its neighbors at the moment it arrives. For the few
days left of the block a query needs, for each such day x, the arrived
element y nearest to −x. When y arrives it becomes the nearest exactly
for the values −x between the midpoints to its neighbors in the order
by value, and these intervals are also found by deleting backwards. The
intervals are applied in arrival order to a tree over groups of 16 of
those days, the latest one winning, and a query reads the stored
partner of each of its days.

In the example the whole array gives |20 − 24| = 4 at days 5 and 6.

With blocks of about N / √Q days this takes O((N + Q)√N) bitset steps.

## Language notes

- Python runs under PyPy: under CPython 3.12 it exceeds the time limit on
  test 4 (3.031 s), while PyPy 3.10 is accepted in 1.125 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2199_sqrt_decomposition_sorting.cpp](2199_sqrt_decomposition_sorting.cpp) | G++ 13.2 x64 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 0.656 s | 3472 KB |
| [2199_sqrt_decomposition_sorting.go](2199_sqrt_decomposition_sorting.go) | Go 1.14 x64 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 1.234 s | 12004 KB |
| [2199_sqrt_decomposition_sorting.java](2199_sqrt_decomposition_sorting.java) | Java 1.8 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 1.812 s | 11324 KB |
| [2199_sqrt_decomposition_sorting.py](2199_sqrt_decomposition_sorting.py) | PyPy 3.10 x64 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 1.125 s | 17704 KB |
| [2199_sqrt_decomposition_sorting.rs](2199_sqrt_decomposition_sorting.rs) | Rust 1.75 x64 | sqrt_decomposition, sorting | O((N + Q) √N) | AC | 0.703 s | 7536 KB |
