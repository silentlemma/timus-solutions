# 2092. One subscription plus single tickets at the lowest cost

[Timus 2092](https://acm.timus.ru/problem.aspx?space=1&num=2092) · difficulty 1175 · greedy, binary_search

Original problem by Denis Dublennykh, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are n concerts, concert i costs sᵢ and a single ticket for it has
a student discount of dᵢ percent. A subscription of type j covers any kⱼ
or more concerts at a discount of pⱼ percent of their total, but student
discounts do not apply inside it. Every concert is attended once. Find
the lowest total cost. The limits are 1 second and 64 MB.

## Input

n and m, 2 ≤ n ≤ 10⁵, 1 ≤ m ≤ 10⁵, the n pairs sᵢ (100 to 50 000) and
dᵢ (0 to 100), then the m pairs kⱼ (2 to n) and pⱼ (1 to 100).

## Output

The lowest cost with an absolute or relative error of at most 10⁻⁶.

## Examples

### Example 1

Input:

```
6 2
500 0
700 0
300 0
400 0
500 50
800 0
5 10
6 15
```

Output:

```
2680.00
```

## Solution

Two subscriptions are never needed: merging them into the one with the
larger discount covers the same concerts cheaper and still has enough
concerts. For a discount p only the smallest k offered with it matters,
and a type with a smaller discount and no smaller k is useless. Python,
Go and Java try discounts from 100 down, keeping only those whose k beats
all larger discounts. C++ and Rust try all offered discounts in ascending
order without this optional dominance pruning.

All costs are kept in hundredths of a rouble: a single ticket costs
s (100 − d), the same concert inside the subscription s (100 − p). With
a subscription at p, every concert with d ≤ p goes into it, and the rest
are bought singly; if that gives fewer than k concerts, the missing ones
are the cheapest to move, each concert with d > p adding s (d − p). The
concerts are grouped by their discount and sorted by price inside each
group, with prefix sums, so the cost of the need cheapest moves is found
by a binary search on the extra cost: for a threshold x, a group with
discount d contributes the concerts with s ≤ x / (d − p). Every move at
the final threshold costs the same, so the surplus is subtracted
exactly. The answer is the best of these costs and of buying every ticket
singly. Let D = 100 and S = 50000. Each discount takes
O(D log(DS) log n): the threshold search has O(log(DS)) iterations, each
searching at most D sorted groups. Including input reading and sorting,
the total time is O(n log n + m + D^2 log(DS) log n).

Pitfalls: equal-discount tickets fill subscription places for free (test
07), and only the needed tickets at a tied threshold should be charged
(test 06). Dominance pruning is optional; competing and dominated offers
must still produce the same minimum (test 10).

In the example the 10 % subscription for every concert but the fifth
costs 2700 · 0.9 = 2430, and the fifth ticket with its 50 % discount
costs 250: 2680.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2092_greedy_binary_search.cpp](2092_greedy_binary_search.cpp) | G++ 13.2 x64 | greedy, binary_search | O(n log n + m + D^2 log(DS) log n) | AC | 0.234 s | 1620 KB |
| [2092_greedy_binary_search.go](2092_greedy_binary_search.go) | Go 1.14 x64 | greedy, binary_search | O(n log n + m + D^2 log(DS) log n) | AC | 0.046 s | 7356 KB |
| [2092_greedy_binary_search.java](2092_greedy_binary_search.java) | Java 1.8 | greedy, binary_search | O(n log n + m + D^2 log(DS) log n) | AC | 0.125 s | 2480 KB |
| [2092_greedy_binary_search.py](2092_greedy_binary_search.py) | Python 3.12 x64 | greedy, binary_search | O(n log n + m + D^2 log(DS) log n) | AC | 0.187 s | 26884 KB |
| [2092_greedy_binary_search.rs](2092_greedy_binary_search.rs) | Rust 1.75 x64 | greedy, binary_search | O(n log n + m + D^2 log(DS) log n) | AC | 0.015 s | 4348 KB |
