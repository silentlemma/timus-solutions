# 1071. The smallest base in which crossing out digits turns x into y

[Timus 1071](https://acm.timus.ru/problem.aspx?space=1&num=1071) · difficulty 624 · math

Original problem by Dmitry Filimonenkov, from the Ural State University Personal Contest Online, February 2001, Students Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Two integers `1 ≤ y < x ≤ 1 000 000` are given. Find the smallest base
`b ≥ 2` in which the digits of `y` can be obtained from the digits of `x`
by crossing out some of them, or print `No solution` if there is no such
base.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`x` and `y` on one line.

## Output

The base, or `No solution`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
127 16
```

Output:

```
3
```

## Solution

Split the bases into three ranges.

- `b > x`: `x` is one digit and `y` is a different one, so nothing works.
- `b² ≤ x`: at most a thousand bases. Write both numbers in base `b` and
  check greedily that the digits of `y` appear in the digits of `x` in
  order.
- `b² > x` and `b ≤ x`: `x` has exactly two digits, `x div b` and
  `x mod b`, and `y < x` must be one of them.
  - `x div b = y` for `b` from `⌊x/(y+1)⌋ + 1` to `⌊x/y⌋`, so the smallest
    such base in this range is known at once.
  - `x mod b = y` means that `b` divides `x − y` and `b > y`, so take the
    smallest divisor of `x − y` that is large enough; the divisors come in
    pairs up to `√(x − y)`.

The small bases are tried first, so the first match there is the answer;
otherwise the answer is the smaller of the two candidates from the last
range. `O(√x · log x)`.

Pitfalls:

- the answer can be huge, for example 465379 for `932318 1560`, so a
  search that stops at base 10 or 36 is wrong;
- trying all bases up to `x` with a full conversion is fast enough in a
  compiled language, but the two-digit range is where almost all of them
  are, and handling it with arithmetic keeps every language quick;
- a digit is less than the base: for the low digit this is the condition
  `b > y`, for the high digit it holds by itself because `b² > x`.

The answers were checked against a brute force over every base with a
general subsequence test, for all pairs with `x < 700` and for random
large pairs.

## Language notes

- C++ and Java compute `b · b` in 64 bits in the loop condition; Go and
  Rust use 64-bit integers throughout.
- Python checks the subsequence with the `d in it` idiom on one iterator,
  which moves forward through the digits of `x`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1071_math.cpp](1071_math.cpp) | G++ 13.2 x64 | math | O(√x · log x) | AC | 0.015 s | 188 KB |
| [1071_math.go](1071_math.go) | Go 1.14 x64 | math | O(√x · log x) | AC | 0.031 s | 1192 KB |
| [1071_math.java](1071_math.java) | Java 1.8 | math | O(√x · log x) | AC | 0.125 s | 1636 KB |
| [1071_math.py](1071_math.py) | Python 3.12 x64 | math | O(√x · log x) | AC | 0.062 s | 572 KB |
| [1071_math.rs](1071_math.rs) | Rust 1.75 x64 | math | O(√x · log x) | AC | 0.031 s | 232 KB |
