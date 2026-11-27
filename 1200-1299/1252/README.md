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

## Checking

`tests/tests.json` uses exact `tokens`: one decimal token K in 0..N−1. Whitespace/newlines around it do not matter; extra tokens or a different numeral spelling fail. Both increasing and decreasing target orders are allowed; already sorted rows permit N−1 even though swaps that far apart do not exist.

## Examples

### Example 1

Input:

```
6
40
50
60
10
20
30
```

Output:

```
2
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

Simple C++/Go retain weights and sorted original-position indices; Java retains one packed long[N] array; all use O(N) array storage including any sorting workspace. Python also keeps whole input, integer list/slices and sorted indices, Rust whole input and parsed/index vectors: O(I+N) for I input bytes. Fast native versions retain a full 130001-entry position table, O(W) for W=130000, regardless of the smaller occupied weight interval. They do not store a second full stone sequence. Input buffers are 16384 bytes in C++, 4096 in Java, and bounded locked standard input in Rust. General gcd processing costs up to O(N log N) arithmetic work; table initialization/scanning adds O(W), input adds O(I).

## Optimized solutions

All three native fast versions replace sorting with a zero-initialized weight→original-position table, possible because weights are distinct and bounded. Track minimum/maximum occupied weight and scan only that interval, skipping zero entries; rank gives both increasing and decreasing target positions. C++ and Rust stop once both gcds reach 1: a gcd that is 1 remains 1 after further values, so neither direction can permit d>1 and K=0 is final. Java continues the entire interval. C++ uses a custom fread parser, Java a4096-byte parser, Rust locked byte input. Conservative time O(I+W+N log N), space O(W+B) with bounded input B.

The source-bound saved audit qualifies the reused Go 4012 KB base against its applicable sparse exact-compiler reference, requiring both metrics; it is not admitted by an ordinary top-ten/top 15% assertion. Python 13612 KB qualifies both ordinary rankings. Java base1596 KB and Rust base3652 KB qualify both; fast Java 972 KB, C++ 604 KB and Rust 712 KB require only time below 1024 KB. Simple C++ remains teaching despite missing required metrics. The shared [rating criteria](../../RATING_CRITERIA.md) apply without separate first-place or 30%-gain exceptions.

Only explanatory early-exit comments were added to `1252_sorting.cpp` (historical#11310440,0.015 s/604 KB) and `1252_sorting.rs` (historical#11310439,0.015 s/712 KB). Simple versions and unchanged fast Java remain available.

## Language notes

These notes describe the simple implementations.

- Java sorts weights packed with their positions in one `long` array
  instead of sorting boxed indices with a comparator.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1252_number_theory.cpp](1252_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log N) | AC | 0.093 s | 1212 KB | 11284003 |
| [1252_number_theory.go](1252_number_theory.go) | Go 1.14 x64 | number_theory | O(N log N) | AC | 0.125 s | 4012 KB | 11284006 |
| [1252_number_theory.java](1252_number_theory.java) | Java 1.8 | number_theory | O(N log N) | AC | 0.093 s | 1596 KB | 11284010 |
| [1252_number_theory.py](1252_number_theory.py) | Python 3.12 x64 | number_theory | O(N log N) | AC | 0.14 s | 13612 KB | 11284007 |
| [1252_number_theory.rs](1252_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log N) | AC | 0.031 s | 3652 KB | 11284011 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1252_sorting.cpp](1252_sorting.cpp) | G++ 13.2 x64 | sorting | O(W + N log N) | AC | 0.015 s | 608 KB | 11331145 |
| [1252_sorting.java](1252_sorting.java) | Java 1.8 | sorting | O(W + N log N) | AC | 0.078 s | 972 KB | 11310354 |
| [1252_sorting.rs](1252_sorting.rs) | Rust 1.75 x64 | sorting | O(W + N log N) | AC | 0.015 s | 712 KB | 11331120 |
