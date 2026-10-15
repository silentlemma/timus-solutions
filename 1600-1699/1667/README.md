# 1667. Square Country 3

[Timus 1667](https://acm.timus.ru/problem.aspx?space=1&num=1667) · difficulty 1847 · constructive

Original problem by Ivan Burmistrov (prepared by Alexander Ipatov), from the Ural SU Contest at the Petrozavodsk Winter Training Camp, January 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For each of T tests, fill an N × M table with squares of distinct
positive integers, each square at most 10¹⁷, so that every row and every
column adds up to a square; print `-1` if that is impossible. Tables of
different tests are separated by an empty line.

## Input

T (1 ≤ T ≤ 20), then T pairs N M (1 ≤ N, M ≤ 20).

## Output

The tables, or `-1`.

## Examples

### Example 1

Input:

```
3
1 2
3 1
2 2
```

Output:

```
9 16

1024
25
274576

4761 8464
627264 1115136
```

Any valid table is accepted; this solution prints different ones.

## Solution

Take two lists of distinct positive integers a₁ … a_N and b₁ … b_M whose
squares add up to squares, and put (aᵢ·bⱼ)² in cell (i, j). Row i then
adds up to aᵢ² · Σbⱼ², a square times a square, and the same holds for
columns. A table always exists, and the work is to find lists with
small enough numbers and distinct products.

- One number: 1. Two numbers: legs of a Pythagorean triple,
  m² − n² and 2mn.
- k + 1 ≥ 3 numbers: for positive integers u₁ … u_k with S = Σuᵢ²,
  the numbers 2u₁, …, 2u_k and S − 1 work, because
  4S + (S − 1)² = (S + 1)². The u are taken as arithmetic sequences
  and as runs of consecutive primes; lists with a repeated number are dropped.

Two products aᵢbⱼ and a_kb_l are equal exactly when aᵢ / a_k = b_l / bⱼ,
so the lists must have no ratio below 1 in common. Lists keep reduced
ratios in sets or sorted arrays; for a test the solution scans pairs of
lists by their largest numbers and takes the first pair with disjoint
ratio sets and max(a) · max(b) ≤ √10¹⁷. With arithmetic sequences alone
some large sizes fail (no disjoint pair fits the bound), and with primes
alone the numbers grow too large, but together every one of the 400
sizes succeeds, the largest product being about 1.9 · 10⁸. Sizes 1, 2,
3 and 4…20 have 1, 315, 203 and 204 candidates, respectively; K is the
maximum candidate count and D = max(N, M).

Pitfalls:

- equal sizes greater than 1 cannot use the same list twice: its ratios
  would match;
- the entries reach about 3.5 · 10¹⁶, so they need 64-bit integers.

All 400 sizes were checked with the checker, which tests distinctness,
the bound and every row and column.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1667_constructive.cpp](1667_constructive.cpp) | G++ 13.2 x64 | constructive | O(K^2 D^2 + K D^2 log(KD)) | AC | 0.046 s | 4092 KB |
| [1667_constructive.go](1667_constructive.go) | Go 1.14 x64 | constructive | O(K^2 D^2 + K D^2 log(KD)) | AC | 0.078 s | 7680 KB |
| [1667_constructive.java](1667_constructive.java) | Java 1.8 | constructive | O(K^2 D^2 + K D^2 log(KD)) | AC | 0.234 s | 8600 KB |
| [1667_constructive.py](1667_constructive.py) | Python 3.12 x64 | constructive | O(K^2 D^2 + K D^2 log(KD)) | AC | 0.281 s | 35156 KB |
| [1667_constructive.rs](1667_constructive.rs) | Rust 1.75 x64 | constructive | O(K^2 D^2 + K D^2 log(KD)) | AC | 0.046 s | 5028 KB |
