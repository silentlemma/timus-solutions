# 1206. Pairs of numbers whose digit sums add up

[Timus 1206](https://acm.timus.ru/problem.aspx?space=1&num=1206) · difficulty 124 · combinatorics

Original problem by Leonid Volkov, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Let `S(N)` be the digit sum of `N`. For `2 ≤ K ≤ 50`, count the ordered
pairs of `K`-digit numbers `A` and `B`, without leading zeros, with
`S(A + B) = S(A) + S(B)`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`K`.

## Output

The number of pairs.

## Examples

### Example 1

Input:

```
2
```

Output:

```
1980
```

## Solution

Every carry in the addition turns a 10 in one position into a 1 in the
next, lowering the digit sum by 9. So the equality holds exactly when no
position carries, that is when the digits in each position add up to at
most 9. The positions are then independent. In the leading position both
digits are from 1 to 9, which allows `8 + 7 + … + 1 = 36` pairs; in each
of the other `K − 1` positions the digits are from 0 to 9, which allows
`10 + 9 + … + 1 = 55` pairs. The answer is `36 · 55^(K−1)`, a number of
up to 87 digits. `O(K²)` with schoolbook multiplication.

Pitfalls:

- the answer outgrows 64 bits already at `K = 12`;
- the leading digits cannot be 0, so their count differs from the
  others.

The formula was checked by brute force over all pairs for `K = 2` and
`K = 3`, and every `K` was compared with a separately written solution.

## Language notes

- Python uses its own integers, Go `math/big` and Java `BigInteger`;
  C++ and Rust multiply a decimal digit array by 55 `K − 1` times.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1206_combinatorics.cpp](1206_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(K²) | AC | 0.015 s | 188 KB |
| [1206_combinatorics.go](1206_combinatorics.go) | Go 1.14 x64 | combinatorics | O(K²) | AC | 0.031 s | 1200 KB |
| [1206_combinatorics.java](1206_combinatorics.java) | Java 1.8 | combinatorics | O(K²) | AC | 0.140 s | 1748 KB |
| [1206_combinatorics.py](1206_combinatorics.py) | Python 3.12 x64 | combinatorics | O(K²) | AC | 0.109 s | 416 KB |
| [1206_combinatorics.rs](1206_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(K²) | AC | 0.015 s | 212 KB |
