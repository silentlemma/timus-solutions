# 2135. Fewest segments with products in a range

[Timus 2135](https://acm.timus.ru/problem.aspx?space=1&num=2135) · difficulty 991 · dp, two_pointers

Original problem by Anna Khanova, from the “Later is better than never” contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Split a sequence of n positive integers into the fewest consecutive
segments so that the product of every segment lies in [l, r], or report
that it is impossible. The limits are 2 seconds and 256 MB.

## Input

n, l and r, 1 ≤ n ≤ 50 000, 1 ≤ l ≤ r ≤ 10¹⁸, then the numbers, each
from 1 to 10⁹.

## Output

The fewest segments, or −1.

## Examples

### Example 1

Input:

```
7 8 20
2 4 8 16 1 3 5
```

Output:

```
4
```

### Example 2

Input:

```
7 10 20
2 4 8 16 1 3 5
```

Output:

```
-1
```

## Solution

Let best(i) be the fewest segments covering the first i numbers. The
last segment of a split of the first i numbers starts at some j, and its
product grows as j moves left, because all numbers are at least 1. So
the starts with product at most r form a suffix of positions from U,
and the starts with product at least l form a prefix of positions below
L; the allowed starts are the interval [U, L).

Both ends only move right as i grows, so two pointers keep them, each
with the product of its window: when the next number would push a
product over its bound, numbers are divided out from the left first,
which keeps every product within 64 bits. A number above r resets the
upper window, and a number at least l resets the lower one. The values
best(j) for j in [U, L) enter and leave a monotone deque, which gives
their minimum in O(1), so best(i) = 1 + that minimum. The whole run is
O(n).

In the first example 2 · 4 | 8 | 16 · 1 | 3 · 5 uses four segments with
products 8, 8, 16 and 15.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2135_dp_two_pointers.cpp](2135_dp_two_pointers.cpp) | G++ 13.2 x64 | dp, two_pointers | O(n) | AC | 0.015 s | 836 KB |
| [2135_dp_two_pointers.go](2135_dp_two_pointers.go) | Go 1.14 x64 | dp, two_pointers | O(n) | AC | 0.046 s | 3016 KB |
| [2135_dp_two_pointers.java](2135_dp_two_pointers.java) | Java 1.8 | dp, two_pointers | O(n) | AC | 0.093 s | 1344 KB |
| [2135_dp_two_pointers.py](2135_dp_two_pointers.py) | Python 3.12 x64 | dp, two_pointers | O(n) | AC | 0.156 s | 5472 KB |
| [2135_dp_two_pointers.rs](2135_dp_two_pointers.rs) | Rust 1.75 x64 | dp, two_pointers | O(n) | AC | 0.031 s | 1940 KB |
