# 2102. Does a number have exactly twenty prime factors

[Timus 2102](https://acm.timus.ru/problem.aspx?space=1&num=2102) · difficulty 147 · number_theory

Original problem by Vladimir Leskov, from the Ural FU Junior Championship 2016.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Tell whether the prime factorisation of n has exponents adding up to
exactly 20, that is whether n is a product of exactly 20 primes counted
with multiplicity. The limits are 2 seconds and 64 MB.

## Input

n, 1 ≤ n ≤ 10¹⁸.

## Output

`Yes` or `No`.

## Examples

### Example 1

Input:

```
2
```

Output:

```
No
```

### Example 2

Input:

```
1048576
```

Output:

```
Yes
```

### Example 3

Input:

```
10000000000
```

Output:

```
Yes
```

## Solution

Divide n by every d from 2 up to B = 2·10⁶ while d² ≤ n, counting the
prime factors removed. If the loop stops because d² exceeds what is
left, the rest is 1 or a prime and adds 0 or 1. Otherwise the rest is at
least B² = 4·10¹², so the removed part is at most 10¹⁸ / B², less than
2¹⁸, which means fewer than 18 factors so far; the rest has no factor
below B and is at most 10¹⁸ < B³, so it adds at most two. The total
cannot reach 20, and the answer is No. The work is O(min(sqrt n, B)).

In the third example 10¹⁰ = 2¹⁰ · 5¹⁰ has 20 prime factors.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2102_number_theory.cpp](2102_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 124 KB |
| [2102_number_theory.go](2102_number_theory.go) | Go 1.14 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.046 s | 1120 KB |
| [2102_number_theory.java](2102_number_theory.java) | Java 1.8 | number_theory | O(min(sqrt n, B)) | AC | 0.156 s | 1636 KB |
| [2102_number_theory.py](2102_number_theory.py) | Python 3.12 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.484 s | 428 KB |
| [2102_number_theory.rs](2102_number_theory.rs) | Rust 1.75 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 232 KB |
