# 1720. Summit Online Judge

[Timus 1720](https://acm.timus.ru/problem.aspx?space=1&num=1720) · difficulty 978 · math

Original problem by Alex Samsonov, from the NEERC 2009 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Every contest has from x to y problems. A volume size is correct if
some number of contests can hold exactly that many problems. Count the
correct sizes from l to r.

## Input

x, y, l and r (1 ≤ x ≤ y ≤ 10¹⁸, 1 ≤ l ≤ r ≤ 10¹⁸).

## Output

The number of correct sizes in [l, r].

## Examples

### Example 1

Input:

```
4 5 7 13
```

Output:

```
5
```

## Solution

With k contests the reachable totals are exactly the interval
[kx, ky]. Interval k + 1 starts at (k + 1)x. It touches interval k,
whose last number is ky, when (k + 1)x ≤ ky + 1, that is
k(y − x) ≥ x − 1. This holds from some K on, and from K·x on every
number is covered. Before K the intervals are apart. So count the
covered numbers up to t, and answer C(r) − C(l − 1):

- if x = y, the covered numbers are the multiples of x, so C(t) = ⌊t/x⌋;
- otherwise K = max(1, ⌈(x − 1)/(y − x)⌉). The intervals k < K that
  end by t, those with k ≤ ⌊t/y⌋, add
  (y − x)·f(f + 1)/2 + f for their count f;
- the next interval may end past t and adds t − kx + 1 if it starts by
  t;
- from K·x on, everything up to t counts.

In the example, K = 3: the intervals [4, 5] and [8, 10] are apart, and
everything from 12 on is covered, so 8, 9, 10, 12 and 13 are correct.
`O(1)`.

Pitfalls:

- with x = 1 the very first interval already joins the rest:
  ⌈0/(y − x)⌉ = 0, so K must be at least 1;
- K·x can reach 10³⁶, so compare K ≤ ⌊t/x⌋ instead of K·x ≤ t; the sum
  of the separate intervals stays below t and fits 64 bits;
- x = y has no joining point at all.

The counts match a brute force for every x, y and t up to small bounds,
and an independent accepted implementation on 700 random cases up to
10¹⁸.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1720_math.cpp](1720_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1720_math.go](1720_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1108 KB |
| [1720_math.java](1720_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1608 KB |
| [1720_math.py](1720_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 496 KB |
| [1720_math.rs](1720_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 224 KB |
