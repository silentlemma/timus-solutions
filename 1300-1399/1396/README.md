# 1396. Maximum. Version 2

[Timus 1396](https://acm.timus.ru/problem.aspx?space=1&num=1396) · difficulty 1980 · math

Original problem prepared by Vladimir Yakovlev.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The same sequence as in [problem 1079](../../1000-1099/1079/README.md):
a₀ = 0, a₁ = 1, a₂ᵢ = aᵢ, a₂ᵢ₊₁ = aᵢ + aᵢ₊₁. For up to 10 000 numbers
n < 10¹⁸ print the largest aᵢ with 0 ≤ i ≤ n.

Time limit: 1 second. Memory limit: 64 MB.

## Input

One n per line, ending with 0.

## Output

The largest term up to each n.

## Examples

### Example 1

Input:

```
5
10
0
```

Output:

```
3
4
```

## Solution

A term is read from the binary digits of its index. Keep the pair
(aₘ, aₘ₊₁) for a prefix m of the bits: a digit 0 turns it into
(aₘ, aₘ + aₘ₊₁) and a digit 1 into (aₘ + aₘ₊₁, aₘ₊₁). Both maps are
linear, so r more digits turn the pair into p·aₘ + q·aₘ₊₁ for fixed p
and q.

Every i ≤ n is either n itself or agrees with n down to some digit 1
that it lowers to 0, with any r digits below it. So walk the digits of
n from the top, and at each digit 1 take the best of all r-digit
endings after the lowered prefix. The best ending is always one of
eight: alternating digits starting with 0 or with 1, as they are or
with the last digit set to 1 or the last two to 11 or 01. Their (p, q)
are computed once for every r up to 60, so each query takes
`O(log n)`. The terms below 2⁶⁰ stay under 3·10¹², within 64 bits.

Pitfalls:

- plain alternating digits are not enough: from a₀, a₁ two free digits
  give the most with 11, not with 01 or 10;
- the record values grow like Fibonacci numbers, past 32 bits for large
  n (test 04).

The eight endings were checked against the true maximum of every block
of 2ʳ indices below 2²² for r from 12 to 20, and all small cases by
trying every ending; the answers were compared with a direct scan for
every n up to 65 536.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1396_math.cpp](1396_math.cpp) | G++ 13.2 x64 | math | O(log n) | AC | 0.001 s | 216 KB |
| [1396_math.go](1396_math.go) | Go 1.14 x64 | math | O(log n) | AC | 0.015 s | 1360 KB |
| [1396_math.java](1396_math.java) | Java 1.8 | math | O(log n) | AC | 0.109 s | 2340 KB |
| [1396_math.py](1396_math.py) | Python 3.12 x64 | math | O(log n) | AC | 0.562 s | 2252 KB |
| [1396_math.rs](1396_math.rs) | Rust 1.75 x64 | math | O(log n) | AC | 0.001 s | 764 KB |
