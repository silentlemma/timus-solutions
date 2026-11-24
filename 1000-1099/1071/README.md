# 1071. The smallest base in which crossing out digits turns x into y

[Timus 1071](https://acm.timus.ru/problem.aspx?space=1&num=1071) · difficulty 626 · math

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

## Optimized solutions

Match small-base digits from right to left. For larger bases, bound the quotient directly and search divisors of the difference to find the smallest candidate base.

Python submission 11317873 took 0.078 s and used 516 KB. The simple version took 0.078 s and used 524 KB.

Java submission 11317892 took 0.093 s and used 388 KB. The simple version took 0.109 s and used 1652 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322392 · Go 1.14 x64 №11322458 · Rust 1.75 x64 №11322435 · Java 1.8 №11322459 · Python 3.12 x64 №11322460.

Go skips ranges of bases where both numbers have the same number of digits. It checks the remaining small bases by matching digits from right to left and derives the larger candidates by division. Go 1.14 x64, submission 11322927. Time 0.015 → 0.015 s, memory 1172 → 336 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1071_math.cpp](1071_math.cpp) | G++ 13.2 x64 | math | O(√x · log x) | AC | 0.015 s | 172 KB | 11322392 |
| [1071_math.go](1071_math.go) | Go 1.14 x64 | math | O(√x · log x) | AC | 0.015 s | 1172 KB | 11322458 |
| [1071_math.java](1071_math.java) | Java 1.8 | math | O(√x · log x) | AC | 0.109 s | 1652 KB | 11322459 |
| [1071_math.py](1071_math.py) | Python 3.12 x64 | math | O(√x · log x) | AC | 0.078 s | 524 KB | 11322460 |
| [1071_math.rs](1071_math.rs) | Rust 1.75 x64 | math | O(√x · log x) | AC | 0.031 s | 216 KB | 11322435 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1071_math_optimized.py](1071_math_optimized.py) | Python 3.12 x64 | math | O(√x · log x) | AC | 0.078 s | 516 KB | 11317873 |
| [1071_math_optimized.java](1071_math_optimized.java) | Java 1.8 | math | O(√x · log x) | AC | 0.093 s | 388 KB | 11317892 |
| [1071_math_optimized.go](1071_math_optimized.go) | Go 1.14 x64 | math | O(√x · log x) | AC | 0.015 s | 336 KB | 11322927 |
