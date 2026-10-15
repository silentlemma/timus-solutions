# 1705. Gangster Hares

[Timus 1705](https://acm.timus.ru/problem.aspx?space=1&num=1705) · difficulty 948 · math

Original problem by Alexander Ipatov, from the Thirteenth Ural Championship in Sports Programming, April 4, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A gang of k hares stole n cabbages and shared them equally, the
remainder of fewer than k going to a fox. An extra hare joined the
sharing unnoticed: with k + 1 hares everyone still got exactly as many
cabbages as with k. For each n, find the least possible k.

## Input

The number of tests t (1 ≤ t ≤ 30000), then t lines with n
(1 ≤ n ≤ 10^18).

## Output

For each test, the least k on its own line.

## Examples

### Example 1

Input:

```
3
9
11
18
```

Output:

```
5
4
5
```

## Solution

We need the least k with ⌊n/k⌋ = ⌊n/(k + 1)⌋. With q = ⌊n/k⌋ and
r = n mod k this holds exactly when the extra hare can be fed from the
remainder, r ≥ q. As r < k, it needs q < k, so k is above s = ⌊√n⌋.

Write n = s² + e and k = s + x with x ≥ 1. Since (s + x)(s − x) =
s² − x², we get n = k(s − x) + x² + e, so the quotient is s − x or
s − x + 1:

- quotient s − x, remainder x² + e: the condition is x² + x ≥ s − e;
- quotient s − x + 1, remainder x² + e − s − x: the condition is
  x² ≥ 2s − e + 1.

Each inequality gives its least x through one integer square root.
Near the borders between the two cases the guess may be one off, so
k = s + x − 1, s + x and s + x + 1 are checked directly for both
values of x, and the least k that works is the answer. Small n
(below 100) are simply searched. `O(1)` per test.

Pitfalls:

- n reaches 10^18, so everything is 64-bit; a floating square root is
  not exact there and is corrected by integer comparisons;
- the smallest n behave differently: n = 1 gives 2 and n = 2 gives 3
  (test 02 has every n up to 100);
- up to 30000 tests, so the input and output should be fast.

The answers match a brute force over every n up to 200000, and an
independent accepted implementation on 15000 values up to 10^18,
including the numbers next to squares and products s(s + 1).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1705_math.cpp](1705_math.cpp) | G++ 13.2 x64 | math | O(1) per test | AC | 0.062 s | 144 KB |
| [1705_math.go](1705_math.go) | Go 1.14 x64 | math | O(1) per test | AC | 0.031 s | 3152 KB |
| [1705_math.java](1705_math.java) | Java 1.8 | math | O(1) per test | AC | 0.156 s | 5284 KB |
| [1705_math.py](1705_math.py) | Python 3.12 x64 | math | O(1) per test | AC | 0.234 s | 5496 KB |
| [1705_math.rs](1705_math.rs) | Rust 1.75 x64 | math | O(1) per test | AC | 0.046 s | 2532 KB |
