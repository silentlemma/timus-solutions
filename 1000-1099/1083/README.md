# 1083. A factorial with k exclamation marks

[Timus 1083](https://acm.timus.ru/problem.aspx?space=1&num=1083) · difficulty 68 · math

Original problem by Oleg Kats, from the Third Team Programming Contest for Schoolchildren of the Sverdlovsk Region, March 4, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

With `k` exclamation marks, `n!…!` is the product `n(n − k)(n − 2k)…`
that ends at `n mod k`, or at `k` when `k` divides `n`. For example,
`10!!! = 10 · 7 · 4 · 1`. Given `n` (`1 ≤ n ≤ 10`) and `k`
(`1 ≤ k ≤ 20`) marks, print the value.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`n`, one space, then `k` exclamation marks.

## Output

The value of `n!…!`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
9 !!
```

Output:

```
945
```

## Solution

Both endings in the definition are the last positive term of
`n, n − k, n − 2k, …`, so multiply the terms while they stay positive.
`O(n/k)`.

Pitfalls:

- `k` is not a number in the input but the length of the string of marks;
- when `k ≥ n` there is only one factor, `n` itself;
- `10! = 3 628 800` is the largest value, which fits 32-bit integers.

The answers were checked against a direct reading of the definition with
both endings.

## Language notes

- C++, Go, Java and Rust read the marks as one token and take its length;
  Python counts the `!` characters after the space.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1083_math.cpp](1083_math.cpp) | G++ 13.2 x64 | math | O(n/k) | AC | 0.015 s | 396 KB |
| [1083_math.go](1083_math.go) | Go 1.14 x64 | math | O(n/k) | AC | 0.031 s | 1076 KB |
| [1083_math.java](1083_math.java) | Java 1.8 | math | O(n/k) | AC | 0.125 s | 1544 KB |
| [1083_math.py](1083_math.py) | Python 3.12 x64 | math | O(n/k) | AC | 0.093 s | 340 KB |
| [1083_math.rs](1083_math.rs) | Rust 1.75 x64 | math | O(n/k) | AC | 0.015 s | 232 KB |
