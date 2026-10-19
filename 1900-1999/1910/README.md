# 1910. The Strongest Consecutive Triple

[Timus 1910](https://acm.timus.ru/problem.aspx?space=1&num=1910) · difficulty 34 · two_pointers

Original problem by Denis Dublennykh, from NEERC 2012, Eastern subregional contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given a sequence of positive values, find the three consecutive elements
with the largest sum. Report that sum and the 1-based position of the
middle element. The maximizing triple is guaranteed to be unique.
Limits: 1 second and 64 MB.

## Input

First n, 3≤n≤1000, then n integers aᵢ with 1≤aᵢ≤10⁶.
Whitespace and line breaks are interchangeable separators.

## Output

Print the maximum sum followed by the 1-based middle position.

## Checking

Two exact integers, checked token by token.

## Examples

```
6
1 4 4 4 1 1
```

```
12 3
```

## Solution

Maintain a sliding window of length three. Initialize its sum from the
first three values and its middle position to 2. Moving the zero-based
start from s−1 to s removes a[s−1] and adds a[s+2]. If the resulting sum
exceeds the best seen, save it and the new middle position s+2.

The update preserves the invariant that the current sum belongs exactly
to the current triple. Initially the best is the first triple's sum;
after each comparison it is the maximum over all examined triples.
Every possible start 0,…,n−3 is examined once, so the final sum is optimal
and the saved position belongs to its unique maximizing triple.

For n=3, the initial window is the only one and the update loop is empty.
The middle position is neither the first nor the last index of the window.
In the sample the values at positions 2,3,4 sum to 12, and the middle is 3.

Time is O(n). The implementations store the input in O(n) space and use
O(1) additional state. A triple sums to at most 3·10⁶, safely within a
signed 32-bit integer.

## Language notes

C++, Go 1.14, Java 8 and Rust 1.75 use integer arrays or vectors.
Python 3.12 reads integer tokens and uses the same rolling update.
No floating point or large integer arithmetic is necessary. Update only
on a strictly larger sum; the input guarantee excludes tied maxima.

The answers agree with summing all triples directly on all 14 157
sequences of lengths 3 to 7 over values 1 to 4 with a unique best
triple.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1910_two_pointers.cpp](1910_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n) | AC | 0.015 s | 432 KB |
| [1910_two_pointers.go](1910_two_pointers.go) | Go 1.14 x64 | two_pointers | O(n) | AC | 0.015 s | 1096 KB |
| [1910_two_pointers.java](1910_two_pointers.java) | Java 1.8 | two_pointers | O(n) | AC | 0.125 s | 2376 KB |
| [1910_two_pointers.py](1910_two_pointers.py) | Python 3.12 x64 | two_pointers | O(n) | AC | 0.078 s | 496 KB |
| [1910_two_pointers.rs](1910_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(n) | AC | 0.015 s | 240 KB |
