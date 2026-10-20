# 2129. Paying an amount with exactly l coins of powers of k

[Timus 2129](https://acm.timus.ru/problem.aspx?space=1&num=2129) · difficulty 943 · dp

Original problem by Daniil Ayzenshteyn, prepared by Oleg Merkurev, from the “Later is better than never” contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Coins are worth 1, k, k², k³, … Count, modulo 10⁹ + 7, the multisets of
exactly l coins that add up to n. There are up to 100 tests. The limits
are 3 seconds and 128 MB.

## Input

t, 1 ≤ t ≤ 100, then t lines n, k, l with 1 ≤ n ≤ 10¹⁸,
2 ≤ k ≤ 10¹⁸ and 1 ≤ l ≤ 100.

## Output

The count for every test.

## Examples

### Example 1

Input:

```
3
12 3 4
7 2 5
7 2 2
```

Output:

```
2
1
0
```

## Solution

The fewest coins come from the base-k digits dᵢ of n, s = Σ dᵢ coins.
Every other way arises from this one by splitting coins: a coin of kⁱ
becomes k coins of kⁱ⁻¹, adding k − 1 coins. Let xᵢ be the number of
coins of kⁱ that are split. The final counts are
dᵢ + k · xᵢ₊₁ − xᵢ, so different vectors x give different multisets, and
x is valid when no count goes negative: xᵢ ≤ dᵢ + k · xᵢ₊₁. With l coins
the splits add up to B = (l − s) / (k − 1), which must be a whole
non-negative number, so B ≤ 100.

A DP from the highest digit down keeps (splits used, splits on the
level above) with the number of ways. On each level xᵢ ranges over
0 … min(dᵢ + k · xᵢ₊₁, budget left), so for a fixed number used the new
value depends only on how large xᵢ₊₁ is; prefix sums over the previous
level fill each row in O(B), O(B²) per level. Coins of value 1 cannot be
split, and the answer is the number of ways that use exactly B splits.
With at most 60 digits this is O(B² log_k n) per test.

In the first example 12 = 110 in base 3, so s = 2 and l = 4 needs one
split: either the 9 becomes three 3s, or one of the 3s becomes three
1s — the 3 + 3 + 3 + 3 and 9 + 1 + 1 + 1 of the statement.

## Language notes

- Python runs under PyPy: under CPython 3.12 it exceeds the time limit on
  test 18 (3.05 s), while PyPy 3.10 is accepted in 0.63 s.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2129_dp.cpp](2129_dp.cpp) | G++ 13.2 x64 | dp | O(t l^2 log_k n) | AC | 0.078 s | 712 KB |
| [2129_dp.go](2129_dp.go) | Go 1.14 x64 | dp | O(t l^2 log_k n) | AC | 0.171 s | 8544 KB |
| [2129_dp.java](2129_dp.java) | Java 1.8 | dp | O(t l^2 log_k n) | AC | 0.359 s | 4940 KB |
| [2129_dp.py](2129_dp.py) | PyPy 3.10 x64 | dp | O(t l^2 log_k n) | AC | 0.625 s | 9460 KB |
| [2129_dp.rs](2129_dp.rs) | Rust 1.75 x64 | dp | O(t l^2 log_k n) | AC | 0.156 s | 712 KB |
