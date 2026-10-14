# 1541. Chase

[Timus 1541](https://acm.timus.ru/problem.aspx?space=1&num=1541) · difficulty 2123 · backtracking

Original problem by Alexander Ipatov, from the Eighth Ural State University Open Personal Contest, March 3, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The friends ran K leagues (K < 20), the i-th league at a whole speed of
Vi leagues per hour, each slower than the one before (Vi < Vj for
i > j) and none above 100000. The chase took M/N hours, with M and N
coprime, 1 ≤ M, N ≤ 50 and M/N ≤ 3. Find K and the speeds, or print
-1 if there are none. Any answer is accepted.

Time limit: 1 second. Memory limit: 64 MB.

## Input

M and N.

## Output

K, then V1 … VK.

## Examples

### Example 1

Input:

```
2 3
```

Output:

```
2
6 2
```

## Solution

The time is 1/V1 + … + 1/VK, so M/N must be written as a sum of fewer
than 20 distinct unit fractions with denominators up to 10⁵, listed
from the largest denominator down.

Search with iterative deepening on the number of fractions, choosing
denominators in increasing order. With p/q left to cover by at most
`left` fractions after denominator `last`, the next denominator d
satisfies

- d > last and 1/d ≤ p/q, so d ≥ ⌈q/p⌉;
- `left` fractions of at most 1/d must reach p/q, so d ≤ left·q/p;
- the largest possible sum of `left` fractions from d on, a stretch of
  the harmonic series taken from prefix sums, must still reach p/q, both
  before choosing d and for what remains after it.

The remainder is kept as a reduced fraction. Before reduction, branches
with p·d > 2⁶¹ or q·d > 2⁶¹ are skipped to avoid 64-bit overflow; all five
languages skip the same branches and search the same tree.

All 1291 valid inputs were run: every one has an answer, with at most
13 fractions (for M/N close to 3 most of the small denominators are
needed), the largest denominator stays below 10⁵, and the slowest input
takes about 0.3 s in Python. The answers were checked exactly with
fractions.

Pitfalls:

- the speeds must be printed decreasing, the reverse of the search
  order (all tests);
- 3/1 in test 02 uses 1, 1/2, …, 1/10 and three more fractions;
- an answer can be a single fraction, even 1/1 (tests 03, 04);
- products of denominators overflow 64 bits without the bound above;
- several answers exist, so the tests use a checker (all tests).

Complexity: `O(D^K)` for K fractions with denominators up to D = 10⁵ in
the worst case.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1541_backtracking.cpp](1541_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(D^K) | AC | 0.015 s | 968 KB |
| [1541_backtracking.go](1541_backtracking.go) | Go 1.14 x64 | backtracking | O(D^K) | AC | 0.031 s | 1876 KB |
| [1541_backtracking.java](1541_backtracking.java) | Java 1.8 | backtracking | O(D^K) | AC | 0.125 s | 2896 KB |
| [1541_backtracking.py](1541_backtracking.py) | Python 3.12 x64 | backtracking | O(D^K) | AC | 0.156 s | 4552 KB |
| [1541_backtracking.rs](1541_backtracking.rs) | Rust 1.75 x64 | backtracking | O(D^K) | AC | 0.031 s | 1016 KB |
