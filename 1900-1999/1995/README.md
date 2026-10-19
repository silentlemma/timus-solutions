# 1995. Minimum total weight with a prescribed selection count

[Timus 1995](https://acm.timus.ru/problem.aspx?space=1&num=1995) · difficulty 614 · greedy, constructive

Original problem by Denis Dublennykh, prepared by Oleg Dolgorukov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose a sequence of `n` positive integer weights. Its first item is
always discarded. At each later zero-based position `i`, count how many
of the `i` previous weights are strictly smaller than the current one.
Keep the item exactly when this count is at least `p` percent of `i`.
All previous items count, including discarded ones and the first item;
equal weights are not smaller.

Find the minimum total weight for which exactly `k` items are kept, and
output any sequence achieving that minimum. Bounds: `1≤k<n≤100000`,
`1≤p≤100`. A feasible sequence is guaranteed. Time limit: 1 second;
memory limit: 64 MB.

## Input

The first line contains `n k`; the second contains `p`.

## Output

The minimum total on the first line. On the second, `n` positive integer
weights in their processing order. Any optimum is accepted.

## Checking

A checker verifies the count and the sum of the weights, compares the
total with the optimum and simulates every decision; any optimal
sequence is accepted.

## Examples

Input:

```
3 1
50
```

Output:

```
4
1 2 1
```

Here weight 2 is kept and the last 1 is discarded. The implementation
may instead output `1 1 2`, also with total 4 and one kept item. No
total below `n+k=4` is possible: every item weighs at least 1 and every
kept item at least 2.

## Solution

### Construction

Let `D=n−k`. Start with `D` ones, all discarded, and then produce `k`
kept items. Their weights will be nondecreasing. For each zero-based
position `i=D..n−1`, the required number of smaller previous weights is
`q=ceil(p·i/100)`. In a sorted prefix, the smallest feasible new integer
weight is one more than its `q`-th element. Therefore:

`a[i]=a[(p·i−1)//100]+1`, with `a[0..D−1]=1`.

The index is `q−1`; it lies in `0..i−1` because `i≥1` and `1≤p≤100`. It
never decreases as `i` increases. Inductively the prefix stays sorted,
and its first `q` elements are strictly below the new weight. Thus
exactly the last `k` items are kept.

### Why the total is minimum

First, in any feasible sequence, replace every discarded weight by 1.
They remain discarded, and lowering those weights cannot decrease the
smaller-count of an unchanged kept item. The total does not increase.

Next exchange adjacent items consisting of a kept weight `x≥2` followed
by a discarded 1. If the old kept position had `i` previous items and
`L` lighter ones, then `100L≥pi`. After the swap it has `i+1` previous
items and `L+1` lighter ones. Its condition still holds since `100≥p`.
The 1 stays discarded, and later prefix multisets are unchanged.
Repeating the exchange moves all discarded ones to the front. Hence some
optimum has precisely the form used by the construction.

Finally compare the greedy sequence `a` with any feasible tail `b` after
those `D` ones. Suppose all earlier `a` values are at most the
corresponding `b` values. Their `q`-th order statistic cannot be larger.
Eligibility of `b[i]` requires that its prefix's `q`-th element is at
most `b[i]−1`; the greedy value, that element plus one in its own
prefix, is therefore at most `b[i]`. Induction proves coordinatewise
dominance and hence minimum sum, without assuming that an arbitrary
competing tail is sorted.

## Language notes

There is one direct lookup per item: `O(n)` arithmetic operations and
`O(n)` storage, plus output text. Each weight is at most `i+1≤n`. The
sum can reach `n(n+1)/2=5000050000`, for `n=100000`, `k=n−1`, `p=100`;
use 64-bit totals. The product `p·i` fits 32 bits. Python integers
handle the sum directly; C++, Go, Java and Rust use wide accumulators.

Do not include the current item in the percentage denominator, count
only previously kept items, treat equal weights as smaller, or replace
the non-strict percentage inequality by a strict one. Counting smaller
weights needs a tree only in the checker; the construction itself is
linear. The exchanges above prove a normal form; the
implementation does not perform the exchanges.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1995_greedy_constructive.cpp](1995_greedy_constructive.cpp) | G++ 13.2 x64 | greedy, constructive | O(n) | AC | 0.015 s | 816 KB |
| [1995_greedy_constructive.go](1995_greedy_constructive.go) | Go 1.14 x64 | greedy, constructive | O(n) | AC | 0.046 s | 2740 KB |
| [1995_greedy_constructive.java](1995_greedy_constructive.java) | Java 1.8 | greedy, constructive | O(n) | AC | 0.093 s | 6100 KB |
| [1995_greedy_constructive.py](1995_greedy_constructive.py) | Python 3.12 x64 | greedy, constructive | O(n) | AC | 0.093 s | 10976 KB |
| [1995_greedy_constructive.rs](1995_greedy_constructive.rs) | Rust 1.75 x64 | greedy, constructive | O(n) | AC | 0.031 s | 2220 KB |
