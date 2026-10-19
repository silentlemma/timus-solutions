# 1862. Very Wealthy Mole

[Timus 1862](https://acm.timus.ru/problem.aspx?space=1&num=1862) · difficulty 1270 · math

Original problem by Denis Dublennykh, from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A mole can turn a number x into 2x, into 2x + 1, or into ⌊x/2⌋, one
step at a time. For every pair 1 ≤ x < y ≤ 2ˡ − 1 the mole turns x into
y with the fewest steps. How many steps are made in all, modulo
10⁹ + 7?

## Input

l (2 ≤ l ≤ 10¹⁸).

## Output

The total number of steps modulo 10⁹ + 7.

## Examples

### Example 1

Input:

```
2
```

Output:

```
4
```

## Solution

The numbers 1 … 2ˡ − 1 form a perfect binary tree with root 1, where x
is the parent of 2x and 2x + 1, and the three steps move along its
edges. The fewest steps from x to y is the tree distance, so the answer
is the sum of distances over all pairs.

Count the pairs through every edge instead. The edge above a node at
depth k (1 ≤ k ≤ l − 1) separates the 2^(l−k) − 1 nodes of its subtree
from the other 2ˡ − 2^(l−k), and there are 2ᵏ such edges. Their total is
2ˡ·(2^(l−k) − 1)(2ᵏ − 1), and summing over k gives
2ˡ·((l − 1)(2ˡ + 1) − 2(2ˡ − 2)) = 2ˡ·((l − 3)·2ˡ + l + 3). With
2ˡ by fast exponentiation and l taken modulo 10⁹ + 7 this is
`O(log l)`.

For l = 2 the tree is 1 with children 2 and 3: the pairs (1, 2) and
(1, 3) are one step apart and (2, 3) two steps, 4 in all.

Pitfalls:

- l itself is up to 10¹⁸, so it must be reduced before multiplying;
- the differences can go negative modulo 10⁹ + 7; add the modulus back.

The formula agrees with summing all the distances directly for l up to
9 and with an independent accepted implementation for heights up to
10¹⁸, including ones at and around multiples of the modulus.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1862_math.cpp](1862_math.cpp) | G++ 13.2 x64 | math | O(log l) | AC | 0.015 s | 128 KB |
| [1862_math.go](1862_math.go) | Go 1.14 x64 | math | O(log l) | AC | 0.031 s | 1084 KB |
| [1862_math.java](1862_math.java) | Java 1.8 | math | O(log l) | AC | 0.125 s | 1740 KB |
| [1862_math.py](1862_math.py) | Python 3.12 x64 | math | O(log l) | AC | 0.093 s | 412 KB |
| [1862_math.rs](1862_math.rs) | Rust 1.75 x64 | math | O(log l) | AC | 0.046 s | 240 KB |
