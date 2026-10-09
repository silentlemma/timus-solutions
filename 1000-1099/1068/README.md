# 1068. The sum of all integers between 1 and N

[Timus 1068](https://acm.timus.ru/problem.aspx?space=1&num=1068) · difficulty 37 · math

Original problem from the trial round of the ACM ICPC Northeastern European Regional Contest 2000–2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An integer `N` with `|N| ≤ 10000` is given. Print the sum of all integers
between 1 and `N`, both included.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`.

## Output

The sum.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
-3
```

Output:

```
-5
```

## Solution

The numbers between 1 and `N` form one interval of `|N − 1| + 1` numbers,
whichever side of 1 `N` is on. The sum of an interval is its length times
the average of its ends, `(1 + N) / 2`. The product `(1 + N) · (|N − 1| + 1)`
is always even, since its two factors add up to an odd number when
`N ≤ 0` and are `N + 1` and `N` otherwise, so the division is exact. `O(1)`.

Pitfalls:

- `N` may be zero or negative: then the interval runs from `N` up to 1, and
  `N(N + 1)/2` gives a wrong answer, for example 0 instead of 1 for
  `N = 0`;
- the sum reaches about `5 · 10^7` in absolute value, which fits 32-bit
  integers; the solutions still multiply in 64 bits (Python in its
  unbounded integers).

The answers were checked against adding the numbers one by one.

## Language notes

- Python uses floor division `//`, which is exact here because the
  product is even; the other languages truncate, which is exact for the
  same reason.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1068_math.cpp](1068_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB |
| [1068_math.go](1068_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1072 KB |
| [1068_math.java](1068_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1568 KB |
| [1068_math.py](1068_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 448 KB |
| [1068_math.rs](1068_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB |
