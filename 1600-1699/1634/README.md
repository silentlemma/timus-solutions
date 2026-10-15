# 1634. Spider Mite

[Timus 1634](https://acm.timus.ru/problem.aspx?space=1&num=1634) · difficulty 2257 · combinatorics

Original problem by Igor Chevdar (prepared by Alexander Ipatov), from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

After every spraying, N tubs with trees are rearranged by a fixed
permutation P, and the mite eggs die once every tub is back in its
original place for the first time. For P chosen uniformly among all
permutations of N elements, find the expected number of sprayings and
print its integer part.

## Input

One integer N (1 ≤ N ≤ 50).

## Output

The integer part of the expected number of sprayings.

## Examples

### Example 1

Input:

```
2
```

Output:

```
1
```

## Solution

The number of sprayings is the order of P: the least common multiple of
its cycle lengths. A permutation with m_k cycles of length k for every k
has probability 1 / Π k^(m_k) m_k! when drawn uniformly (the classical
count of permutations of a given cycle type), so the expectation is a
sum over cycle types.

There are 204226 cycle types for N = 50, but many share the same lcm.
A knapsack over cycle lengths merges them: dp[s][l] is the probability
that a random permutation of s elements uses only the lengths 1…k seen
so far and that their lcm is l. Adding m cycles of length k moves weight
from dp[s][l] to dp[s + mk][lcm(l, k)], multiplied by 1 / (k^m m!), which
is built up one factor k · m at a time. For N = 50 there are only about
a thousand distinct lcm values per size (Landau's function bounds them by
180180). The answer is Σ l · dp[N][l]. `O(N² log N · L)` for L states per
size.

Doubles are enough: over all 50 inputs, the exact expectations (computed
separately in fractions) are never closer than 0.005 to the integer
above them, except for N = 1 where it is exactly 1, which a 10⁻⁹ nudge
keeps whole. The expectation grows slowly: 1069.51 for N = 50.

Pitfalls:

- the order is the lcm of the cycle lengths, not their product or sum;
- enumerating all partitions with exact big numbers is correct but slow
  in some languages; merging by lcm keeps the work small;
- an exact integer must survive truncation: a sum that came out as
  0.9999999… would print 0 for N = 1 (test 02).

The answers match exact rational values on all 50 inputs, and an
independent accepted implementation as well.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1634_combinatorics.cpp](1634_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N² log N · L) | AC | 0.046 s | 1520 KB |
| [1634_combinatorics.go](1634_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N² log N · L) | AC | 0.109 s | 6216 KB |
| [1634_combinatorics.java](1634_combinatorics.java) | Java 1.8 | combinatorics | O(N² log N · L) | AC | 0.203 s | 8348 KB |
| [1634_combinatorics.py](1634_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N² log N · L) | AC | 0.203 s | 2728 KB |
| [1634_combinatorics.rs](1634_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N² log N · L) | AC | 0.046 s | 1736 KB |
