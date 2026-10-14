# 1597. Chernobyl’ Eagle on a Roof. Version 2

[Timus 1597](https://acm.timus.ru/problem.aspx?space=1&num=1597) · difficulty 1897 · binary_search

Original problem prepared by Sergey Vedernikov.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There is an unknown highest floor E from which an egg survives a drop,
0 ≤ E ≤ n. With k eggs, where unbroken eggs can be reused, find the
least number of drops that determines E in the worst case. Up to 1000
test cases, with k and n up to 10¹⁸, end with `0 0`. This is
[problem 1223](../../1200-1299/1223/README.md) with much larger numbers.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

Lines with k and n, then `0 0`.

## Output

The least number of drops for each case.

## Examples

### Example 1

Input:

```
1 10
2 5
0 0
```

Output:

```
10
3
```

## Solution

Turn the question around: with t drops and k eggs, how many floors can
be settled? The first drop splits the building: if the egg breaks, t − 1
drops and k − 1 eggs remain for the floors below, otherwise t − 1 drops
and k eggs for the floors above, so f(t, k) = f(t − 1, k − 1) +
f(t − 1, k) + 1. The solution of this recurrence is
f(t, k) = C(t, 1) + C(t, 2) + … + C(t, k). The answer is the least t
with f(t, k) ≥ n, and f grows with t, so a binary search finds it.

One egg allows only floor-by-floor drops, so the answer is n itself.
With two or more eggs f(t, 2) = t(t + 1)/2 already reaches 10¹⁸ for t
below 1.5·10⁹, so the search runs over t up to 2·10⁹. The sum is built
term by term, C(t, i) = C(t, i − 1)·(t − i + 1)/i, and stops as soon as it
passes n, which also covers huge k: the terms grow so fast that only a
few dozen are ever needed. At most 31 steps of about 60 terms per case.

The results were checked against the classic dynamic programming over
floors and eggs for all buildings up to 120 floors with up to 8 eggs.

Pitfalls:

- the product C(t, i − 1)·(t − i + 1) overflows 64 bits; the solutions in
  C++, Go, Java and Rust split C(t, i − 1) = q·i + r and compute
  q·(t − i + 1) + r·(t − i + 1)/i, which is exact, and give up as soon as
  q·(t − i + 1) would pass n;
- with k ≥ 60 eggs the answer is just the binary search on floors, the
  bit length of n, and the same loop gives it;
- one egg needs n drops, which does not fit the search range and is
  handled first.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1597_binary_search.cpp](1597_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(log n · min(k, log n)) | AC | 0.015 s | 128 KB |
| [1597_binary_search.go](1597_binary_search.go) | Go 1.14 x64 | binary_search | O(log n · min(k, log n)) | AC | 0.031 s | 1140 KB |
| [1597_binary_search.java](1597_binary_search.java) | Java 1.8 | binary_search | O(log n · min(k, log n)) | AC | 0.140 s | 892 KB |
| [1597_binary_search.py](1597_binary_search.py) | Python 3.12 x64 | binary_search | O(log n · min(k, log n)) | AC | 0.140 s | 752 KB |
| [1597_binary_search.rs](1597_binary_search.rs) | Rust 1.75 x64 | binary_search | O(log n · min(k, log n)) | AC | 0.046 s | 300 KB |
