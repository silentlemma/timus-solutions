# 1252. Sorting stones by swaps K apart

[Timus 1252](https://acm.timus.ru/problem.aspx?space=1&num=1252) · difficulty 397 · number_theory

Original problem by Alexey Lakhtin, from the Ural State University Open Team Contest, March 15, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N stones (1 ≤ N ≤ 130 000) of distinct weights stand in a row. Two stones may
be swapped when exactly K other stones lie between them. Find the largest
K (0 ≤ K < N) with which the row can be sorted by weight, in increasing
or decreasing order.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N weights, one per line. Each weight is an integer from 1 to
130 000, inclusive.

## Output

The largest such K.

## Examples

### Example 1

Input:

```
5
30
21
56
40
17
```

Output:

```
1
```

## Solution

A swap with K stones between moves both stones by d = K + 1 places, so a
stone stays in its class of positions modulo d, and within a class any
order can be made from swaps of neighbours in the class. Sorting is
therefore possible exactly when d divides every stone's distance from
its current place to its place in the sorted row.

So find, for the increasing and for the decreasing order, the gcd g of
these distances. The largest d dividing g is g itself, which is below N,
so K = g − 1; if the row is already in that order, g = 0 and every K
works, so K = N − 1. The answer is the larger of the two orders.
`O(N log N)` for the sort.

Pitfalls:

- the decreasing order counts too (test 04), and the two orders can give
  different K;
- a sorted row allows the largest K, N − 1, even though no swap is then
  possible at all (tests 03 and gen4).

The rule was compared with a search over all reachable orders for every
K on 300 random rows of up to 7 stones.

## Optimized solutions

C++, Java and Rust use a table indexed by weight. Since weights are distinct, each cell holds either the stone’s original position or zero. Scanning the occupied cells in weight order gives the increasing rank r and the decreasing rank N + 1 − r, so both gcds are updated in one pass. W is the size of the weight table.

The accepted base implementations [1252_number_theory.go](1252_number_theory.go), [1252_number_theory.py](1252_number_theory.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- Java sorts weights packed with their positions in one `long` array
  instead of sorting boxed indices with a comparator.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1252_number_theory.cpp](1252_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log N) | AC | 0.093 s | 1212 KB | 11284003 |
| [1252_number_theory.go](1252_number_theory.go) | Go 1.14 x64 | number_theory | O(N log N) | AC | 0.125 s | 4012 KB | 11284006 |
| [1252_number_theory.java](1252_number_theory.java) | Java 1.8 | number_theory | O(N log N) | AC | 0.093 s | 1596 KB | 11284010 |
| [1252_number_theory.py](1252_number_theory.py) | Python 3.12 x64 | number_theory | O(N log N) | AC | 0.140 s | 13612 KB | 11284007 |
| [1252_number_theory.rs](1252_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log N) | AC | 0.031 s | 3652 KB | 11284011 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1252_sorting.cpp](1252_sorting.cpp) | G++ 13.2 x64 | sorting | O(W + N log N) | AC | 0.015 s | 604 KB | 11310440 |
| [1252_sorting.java](1252_sorting.java) \* | Java 1.8 | sorting | O(W + N log N) | AC | 0.078 s | 972 KB | 11310354 |
| [1252_sorting.rs](1252_sorting.rs) \* | Rust 1.75 x64 | sorting | O(W + N log N) | AC | 0.015 s | 712 KB | 11310439 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
