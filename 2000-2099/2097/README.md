# 2097. Find a section that differs by a linear function

[Timus 2097](https://acm.timus.ru/problem.aspx?space=1&num=2097) · difficulty 2202 · strings

Original problem by Dmitry Ivankov, from the Open Ural FU Personal Contest 2014.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A new slope has heights x₀ … x_m, and n older slopes are given the same
way. A section y₀ … y_m of an older slope is similar when
xᵢ − yᵢ = a·i + b for all i and some a and b. Find a slope and a start of
a similar section with the smallest |a|, or output −1. Any such answer
is accepted. The limits are 1 second and 64 MB.

## Input

n ≤ 10⁵, then m ≤ 10⁵ and x₀ … x_m, then each older slope as its length
and its heights; the lengths add up to at most 10⁵ and the heights are
up to 10⁹ in absolute value.

## Output

The number of the slope and the start of the section (the number of
metres from its beginning), or −1.

## Checking

A checker accepts −1 only when the expected output says so, and
otherwise checks that the section is similar and that its |a| is the
smallest one.

## Examples

### Example 1

Input:

```
2
2 3 2 1
5 21 15 10 6 3 2
4 10 7 5 3 2
```

Output:

```
2 1
```

### Example 2

Input:

```
3
2 0 0 0
1 0 0
2 1 2 4
1 5 17
```

Output:

```
-1
```

## Solution

The difference xᵢ − yᵢ is linear exactly when its second differences
vanish, that is when the second differences of x and of the section are
equal. So the m − 1 second differences of x are searched in the second
differences of every older slope with the Knuth–Morris–Pratt algorithm;
each occurrence at position j is a similar section starting at j, and
its a is (x₁ − x₀) − (y_{j+1} − y_j). The smallest |a| over all
occurrences is kept. When m = 1 the pattern is empty and every start of
every long enough slope matches. Values reach 4·10⁹, so 64-bit integers
are used, and the work is linear in the input size.

In the first example the new slope 3, 2, 1 has the second difference 0,
which occurs in the second slope 10, 7, 5, 3, 2 only at position 1.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2097_strings.cpp](2097_strings.cpp) | G++ 13.2 x64 | strings | O(input) | AC | 0.218 s | 2808 KB |
| [2097_strings.go](2097_strings.go) | Go 1.14 x64 | strings | O(input) | AC | 0.078 s | 9636 KB |
| [2097_strings.java](2097_strings.java) | Java 1.8 | strings | O(input) | AC | 0.140 s | 15548 KB |
| [2097_strings.py](2097_strings.py) | Python 3.12 x64 | strings | O(input) | AC | 0.265 s | 24900 KB |
| [2097_strings.rs](2097_strings.rs) | Rust 1.75 x64 | strings | O(input) | AC | 0.046 s | 5388 KB |
