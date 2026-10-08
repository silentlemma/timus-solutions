# 1012. Counting base-K numbers without two adjacent zeros, with long arithmetic

[Timus 1012](https://acm.timus.ru/problem.aspx?space=1&num=1012) · difficulty 180 · dp

Original problem: a harder version of [problem 1009](../1009/README.md).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the `N`-digit numbers in base `K` (the first digit is not zero) whose
digits contain no two zeros in a row. `2 ≤ K ≤ 10`, `N ≥ 2`, `N + K ≤ 1800`.

Time limit: 0.5 seconds. Memory limit: 16 MB.

## Input

`N` and `K`, each on its own line.

## Output

The count, in full.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
2
```

Output:

```
5
```

### Example 2

Input:

```
3
10
```

Output:

```
891
```

## Solution

The recurrence is the one of [problem 1009](../1009/README.md): count valid
prefixes by their last digit, `zero` ending with `0` and `other` with a
nonzero digit:

- `zero' = other`;
- `other' = (zero + other) · (K - 1)`;

starting from `zero = 0`, `other = K - 1`, and the answer is `zero + other`
after `N` digits.

What changes is the size: the answer is close to `(K - 1)^N` and has up to
about 1 800 decimal digits, so it needs long arithmetic. Only two operations
are used — the sum of two long numbers and the product of a long number by a
small one — both linear in the length. Store a long number as an array of
"digits" in base `10^9`, least significant first: a digit times `K - 1` plus
a carry fits in 64 bits. `N` steps of `O(L)` work, where `L` is the length of
the answer in limbs: about `1800 · 200` operations.

Only the two current values are kept, so the memory is `O(L)` — keeping the
whole table of `N` long numbers would also fit, but there is no need.

Pitfalls:

- 64-bit integers overflow after about 20 digits: the small version's
  solution is wrong here;
- when printing base-`10^9` limbs, every limb but the most significant one
  must be padded with leading zeros to 9 digits.

## Language notes

- **Python**, **Go** (`math/big`) and **Java** (`BigInteger`) have long
  integers built in.
- **C++** and **Rust** implement the two operations on base-`10^9` limbs.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1012_dp.cpp](1012_dp.cpp) | G++ 13.2 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 268 KB |
| [1012_dp.go](1012_dp.go) | Go 1.14 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 2056 KB |
| [1012_dp.java](1012_dp.java) | Java 1.8 | dp | O(N·L), L = length of the answer | AC | 0.125 s | 3860 KB |
| [1012_dp.py](1012_dp.py) | Python 3.12 x64 | dp | O(N·L), L = length of the answer | AC | 0.062 s | 340 KB |
| [1012_dp.rs](1012_dp.rs) | Rust 1.75 x64 | dp | O(N·L), L = length of the answer | AC | 0.015 s | 520 KB |
